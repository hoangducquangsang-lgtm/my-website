"""Deterministic WebP derivatives. Source images are never changed or cropped."""
from functools import lru_cache
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import hashlib
import json
import re

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "_source/review/responsive_images.json"
SETTINGS = {"version": 1, "widths": [320, 480, 640, 800, 960, 1200, 1600], "quality": 85, "method": 6}
OLD = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
IMAGES = {}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

# Matches style.css: wrap = min(100vw, 1180px), padding 24px (18px on phones),
# grid gap 22px; hero gap 40px with 1.1fr/.9fr columns above 860px.
SIZES = {
    "hero": "(max-width: 600px) calc(100vw - 36px), (max-width: 860px) calc(100vw - 48px), (max-width: 1180px) calc(45vw - 39.6px), 491.4px",
    "grid-2": "(max-width: 600px) calc(100vw - 36px), (max-width: 1180px) calc(50vw - 35px), 555px",
    "grid-3": "(max-width: 600px) calc(100vw - 36px), (max-width: 900px) calc(50vw - 35px), (max-width: 1180px) calc((100vw - 92px) / 3), 362.67px",
    "grid-4": "(max-width: 600px) calc(100vw - 36px), (max-width: 900px) calc(50vw - 35px), (max-width: 1180px) calc(25vw - 28.5px), 266.5px",
    "full": "(max-width: 600px) calc(100vw - 36px), (max-width: 1180px) calc(100vw - 48px), 1132px",
}
FALLBACK_WIDTH = {"hero": 800, "grid-2": 640, "grid-3": 480, "grid-4": 320, "full": 1200}


def source_path(url):
    parsed = urlsplit(url)
    if not parsed.path.startswith("/assets/img/") or Path(parsed.path).suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        return None
    file = (ROOT / parsed.path.lstrip("/")).resolve()
    if not file.is_relative_to(ROOT / "assets/img"):
        raise ValueError("Image path outside asset folder")
    return file


@lru_cache(maxsize=None)
def variants(url):
    source = source_path(url)
    if source is None:
        return None
    key = source.relative_to(ROOT).as_posix()
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if key in IMAGES and IMAGES[key]["sha256"] == digest:
        return IMAGES[key]
    cached = OLD.get("images", {}).get(key)
    if (OLD.get("settings") == SETTINGS and cached and cached.get("sha256") == digest
            and all((ROOT / v["path"]).is_file() and (ROOT / v["path"]).stat().st_size == v["bytes"] for v in cached["variants"])):
        IMAGES[key] = cached
        return cached
    dest = ROOT / "assets/img/webp"
    dest.mkdir(exist_ok=True)
    with Image.open(source) as opened:
        picture = ImageOps.exif_transpose(opened)
        if picture.mode not in {"RGB", "RGBA"}:
            picture = picture.convert("RGBA" if "transparency" in picture.info else "RGB")
        width, height = picture.size
        widths = sorted({w for w in SETTINGS["widths"] if w < width} | {min(width, 1600)})
        # No upscaling; preserve full composition, ratio and any alpha channel.
        outputs = []
        for w in widths:
            h = max(1, round(height * w / width))
            resized = picture.resize((w, h), Image.Resampling.LANCZOS) if (w, h) != picture.size else picture
            target = dest / f"{source.stem}-{source.suffix[1:].lower()}-{w}w.webp"
            options = {"quality": SETTINGS["quality"], "method": SETTINGS["method"]}
            if opened.info.get("icc_profile"):
                options["icc_profile"] = opened.info["icc_profile"]
            resized.save(target, "WEBP", **options)
            outputs.append({"path": target.relative_to(ROOT).as_posix(), "width": w, "height": h, "bytes": target.stat().st_size})
    result = {"sha256": digest, "width": width, "height": height, "bytes": source.stat().st_size, "variants": outputs}
    IMAGES[key] = result
    return result


def choose(info, desired):
    return next((v for v in info["variants"] if v["width"] >= desired), info["variants"][-1])


def optimized_url(url, desired=1200):
    info = variants(url)
    if not info:
        return url
    parsed = urlsplit(url)
    prefix = f"{parsed.scheme}://{parsed.netloc}" if parsed.netloc else ""
    return prefix + "/" + choose(info, desired)["path"]


def optimize_schema(value):
    if isinstance(value, dict):
        return {key: optimize_schema(item) for key, item in value.items()}
    if isinstance(value, list):
        return [optimize_schema(item) for item in value]
    if isinstance(value, str) and source_path(value):
        return optimized_url(value)
    return value


class ImageMarkup(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=False)
        self.html = html
        self.parents = []
        self.edits = []
        self.offsets = [0]
        for m in re.finditer("\n", html):
            self.offsets.append(m.end())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img":
            info = variants(a.get("src", ""))
            if info:
                layout = "full"
                for _, classes in reversed(self.parents):
                    if "hero-inner" in classes:
                        layout = "hero"
                        break
                    grid = next((c for c in classes if c in SIZES), None)
                    if grid:
                        layout = grid
                        break
                a["src"] = "/" + choose(info, FALLBACK_WIDTH[layout])["path"]
                a["srcset"] = ", ".join(f'/{v["path"]} {v["width"]}w' for v in info["variants"])
                a["sizes"] = SIZES[layout]
                a["width"], a["height"] = str(info["width"]), str(info["height"])
                a["decoding"] = "async"
                if layout == "hero" and a.get("loading") == "eager":
                    a["fetchpriority"] = "high"
                replacement = "<img " + " ".join(key if val is None else f'{key}="{escape(val, quote=True)}"' for key, val in a.items()) + ">"
                line, column = self.getpos()
                offset = self.offsets[line - 1] + column
                self.edits.append((offset, offset + len(self.get_starttag_text()), replacement))
        if tag not in VOID:
            self.parents.append((tag, a.get("class", "").split()))

    def handle_endtag(self, tag):
        for i in range(len(self.parents) - 1, -1, -1):
            if self.parents[i][0] == tag:
                del self.parents[i:]
                break


def responsive_markup(html):
    parser = ImageMarkup(html)
    parser.feed(html)
    for start, end, replacement in reversed(parser.edits):
        html = html[:start] + replacement + html[end:]
    return html


def save_manifest():
    result = {"settings": SETTINGS, "images": dict(sorted(IMAGES.items()))}
    MANIFEST.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    count = sum(len(i["variants"]) for i in IMAGES.values())
    print(f"Responsive images: {len(IMAGES)} originals preserved, {count} WebP derivatives.")
