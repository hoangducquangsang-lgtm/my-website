#!/usr/bin/env python3
"""Re-runnable performance pass for the VietPaw static site.
Run from the site root:  python _source/optimize_assets.py
It (1) generates resized WebP variants for every JPG in assets/img,
and (2) rewrites <img> tags across all index.html with webp src + srcset +
sizes + width/height + lazy/decoding, and preloads the eager hero image.
Idempotent: safe to run again after a rebuild. GTM-defer + hamburger markup
come from _source/common.py at build time."""
import os, re, json
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMGDIR = os.path.join(ROOT, "assets", "img")
WIDTHS, MAXW, Q = [400, 800, 1200], 1400, 74

def build_webp():
    man = {}
    for f in sorted(os.listdir(IMGDIR)):
        low = f.lower()
        if not low.endswith((".jpg", ".jpeg", ".png")) or low.startswith("logo"):
            continue
        im = Image.open(os.path.join(IMGDIR, f)).convert("RGB")
        w, h = im.size
        base_w = min(w, MAXW); base_h = round(h * base_w / w)
        stem = os.path.splitext(f)[0]; variants = []
        for tw in sorted(set(WIDTHS + [base_w])):
            if tw > base_w: continue
            img = im.resize((tw, round(h * tw / w)), Image.LANCZOS) if tw != w else im
            fn = f"{stem}.webp" if tw == base_w else f"{stem}-{tw}.webp"
            with open(os.path.join(IMGDIR, fn), "wb") as fp:
                img.save(fp, "WEBP", quality=Q, method=6)
            variants.append([tw, fn])
        man[f] = {"w": base_w, "h": base_h, "variants": variants}
    json.dump(man, open(os.path.join(IMGDIR, "_webp_manifest.json"), "w"), indent=1)
    return man

SIZES_HERO = "(max-width:860px) 100vw, 600px"
SIZES_CARD = "(max-width:600px) 100vw, (max-width:900px) 50vw, 360px"
IMG_RE = re.compile(r"<img\s+([^>]*?)/?>", re.S)
ATTR_RE = re.compile(r'(\w+)="([^"]*)"')

def patch_html(man):
    def build_img(attrs, holder):
        a = dict(ATTR_RE.findall(attrs))
        m = re.match(r"/assets/img/(.+\.jpg)$", a.get("src", ""))
        if not m or m.group(1) not in man: return None
        info = man[m.group(1)]; stem = m.group(1)[:-4]
        srcset = ", ".join(f"/assets/img/{fn} {w}w" for w, fn in info["variants"])
        eager = a.get("loading") == "eager"
        sizes = SIZES_HERO if eager else SIZES_CARD
        parts = [f'src="/assets/img/{stem}.webp"', f'srcset="{srcset}"', f'sizes="{sizes}"',
                 f'alt="{a.get("alt","")}"', f'width="{info["w"]}"', f'height="{info["h"]}"']
        parts += (['loading="eager"', 'fetchpriority="high"', 'decoding="async"'] if eager
                  else ['loading="lazy"', 'decoding="async"'])
        if "style" in a: parts.append(f'style="{a["style"]}"')
        if eager and holder[0] is None:
            holder[0] = (f"/assets/img/{stem}.webp", srcset, sizes)
        return "<img " + " ".join(parts) + ">"
    for base, dirs, files in os.walk(ROOT):
        if "_source" in base or "_to_delete" in base or ".git" in base: continue
        for fn in files:
            if fn != "index.html": continue
            p = os.path.join(base, fn)
            html = open(p, encoding="utf-8").read(); orig = html; holder = [None]
            html = IMG_RE.sub(lambda mo: build_img(mo.group(1), holder) or mo.group(0), html)
            if holder[0] and 'rel="preload" as="image"' not in html:
                href, srcset, sizes = holder[0]
                html = html.replace("</head>", f'<link rel="preload" as="image" href="{href}" '
                    f'imagesrcset="{srcset}" imagesizes="{sizes}" fetchpriority="high">\n</head>', 1)
            if html != orig:
                open(p, "w", encoding="utf-8").write(html)

if __name__ == "__main__":
    patch_html(build_webp())
    print("Optimized WebP + patched HTML.")
