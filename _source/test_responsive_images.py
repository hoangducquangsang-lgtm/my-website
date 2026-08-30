"""Check generated files, responsive candidates and preservation without a browser."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from PIL import Image
import hashlib
import json
import re
import sys
import zipfile

from validate_site import Document, ROOT
from responsive_images import SIZES
from content_helpers import IMAGE_DESCRIPTIONS

HEMP_IMAGES = {
    "products/hemp-fiber-ball/index.html": "assets/img/winvn-hemp-fiber-rope-ball.png",
    "products/hemp-rope-dog-toy/index.html": "assets/img/winvn-hemp-rope-dog-toy.jpg",
}


def unchanged_copy(html, relative):
    # Whitelist only the owner-requested date display and retired assortment caption.
    if relative.startswith("guides/"):
        html = re.sub(r'<span class="guide-updated">Updated <time[^>]*>[^<]*</time></span>', '', html)
        html = re.sub(r'<time[^>]*>[^<]*</time>', '<time>EDITORIAL_DATE</time>', html)
    if relative in HEMP_IMAGES:
        html = html.replace('<figcaption>Sample assortment showing rope-ball and coffee wood combinations. Standalone balls and rope-only designs are quoted separately; the approved sample defines your order.</figcaption>', '')
    return document(html).main_text


def document(html):
    result = Document()
    result.feed(html)
    return result


def local_path(file, url):
    path = unquote(urlsplit(url).path)
    return (ROOT / path.lstrip("/") if path.startswith("/") else file.parent / path).resolve()


def slot(image, viewport):
    content = min(viewport, 1180) - (36 if viewport <= 600 else 48)
    layout = next(key for key, value in SIZES.items() if value == image["sizes"])
    if layout == "hero":
        return content if viewport <= 860 else (content - 40) * .45
    if layout.startswith("grid-"):
        cols = int(layout[-1])
        if viewport <= 600:
            cols = 1
        elif viewport <= 900 and cols > 2:
            cols = 2
        return (content - 22 * (cols - 1)) / cols
    return content


def run(backup):
    manifest = json.loads((ROOT / "_source/review/responsive_images.json").read_text(encoding="utf-8"))["images"]
    variants = {}
    for original, info in manifest.items():
        source = ROOT / original
        assert hashlib.sha256(source.read_bytes()).hexdigest() == info["sha256"], original
        assert len(info["variants"]) >= 2, original
        for variant in info["variants"]:
            file = ROOT / variant["path"]
            assert file.stat().st_size == variant["bytes"], str(file)
            with Image.open(file) as photo:
                assert photo.format == "WEBP", str(file)
                assert photo.size == (variant["width"], variant["height"]), str(file)
                assert photo.width <= info["width"] and photo.width <= 1600, str(file)
                assert photo.height == round(info["height"] * photo.width / info["width"]), str(file)
                photo.load()
            variants[file.resolve()] = (original, info, variant)
    docs = {}
    inline_count = 0
    for file in sorted(ROOT.rglob("index.html")):
        if "_source" in file.parts:
            continue
        d = document(file.read_text(encoding="utf-8"))
        docs[file.relative_to(ROOT).as_posix()] = d
        for image in d.images:
            inline_count += 1
            original, info, default = variants[local_path(file, image["src"])]
            assert (int(image["width"]), int(image["height"])) == (info["width"], info["height"])
            widths = []
            for candidate in image["srcset"].split(","):
                url, descriptor = candidate.strip().rsplit(" ", 1)
                family, _, variant = variants[local_path(file, url)]
                assert family == original, "Mixed photos in one srcset"
                assert descriptor == str(variant["width"]) + "w", url
                widths.append(variant["width"])
            assert widths == sorted(set(widths)), image["srcset"]
            assert image["sizes"] in SIZES.values(), image["sizes"]
            assert not image["src"].startswith("/"), "File preview requires relative image paths"
            assert all(not part.strip().startswith("/") for part in image["srcset"].split(","))
            for viewport in (320, 390, 600, 601, 768, 860, 861, 900, 901, 1180, 1440):
                assert 0 < slot(image, viewport) <= 1132
        for meta in ("og:image", "twitter:image"):
            assert local_path(file, d.meta[meta]) in variants, "Social image must be optimized"
    old_docs = {}
    old_html = {}
    preserved_assets = 0
    with zipfile.ZipFile(backup) as archive:
        for name in archive.namelist():
            norm = name.replace("\\", "/")
            prefix = ROOT.name + "/"
            if not norm.startswith(prefix):
                continue
            relative = norm[len(prefix):]
            if relative.endswith("index.html") and not relative.startswith("_source/"):
                old_html[relative] = archive.read(name).decode("utf-8")
                old_docs[relative] = document(old_html[relative])
            if relative.startswith("assets/img/") and not name.endswith("/"):
                assert archive.read(name) == (ROOT / relative).read_bytes(), "Original image changed: " + relative
                preserved_assets += 1
    assert len(old_docs) == 67, "Use the backup immediately before the menu/hemp/date update"
    preserved_pages = 0
    approved_image_changes = 0
    for relative, before in old_docs.items():
        after = docs[relative]
        assert unchanged_copy(old_html[relative],relative) == unchanged_copy((ROOT/relative).read_text(encoding="utf-8"),relative), "Unrelated copy changed: " + relative
        assert before.title == after.title and before.meta["description"] == after.meta["description"]
        preserved_pages += 1
        assert len(before.images) == len(after.images), "Image added or removed: " + relative
        for a, b in zip(before.images, after.images):
            original, _, _ = variants[local_path(ROOT / relative, b["src"])]
            old_original, _, _ = variants[local_path(ROOT / relative, a["src"])]
            if old_original != original:
                assert old_original == "assets/img/winvn-hemp-wood-assortment.jpg" and original in HEMP_IMAGES.values(), "Unrequested photo change"
                assert b["alt"] == IMAGE_DESCRIPTIONS[Path(original).name]
                approved_image_changes += 1
            else:
                assert a["alt"] == b["alt"], "Unrequested photo description change"
        if relative in HEMP_IMAGES:
            assert variants[local_path(ROOT / relative, after.images[0]["src"])][0] == HEMP_IMAGES[relative], "Wrong photo for hemp product"
            assert variants[local_path(ROOT / relative, after.meta["og:image"])][0] == HEMP_IMAGES[relative]
    # Confirm the visible form content against the owner-provided old folder.
    legacy = Path("D:/1. Vietpaw/my-website - Copy/request-a-quote/index.html").read_text(encoding="utf-8")
    current = (ROOT / "request-a-quote/index.html").read_text(encoding="utf-8")
    old_form = re.search(r"<form\b.*?</form>", legacy, re.S).group()
    new_form = re.search(r"<form\b.*?</form>", current, re.S).group()
    assert re.search(r'<p class="small">(.*?)</p>', old_form, re.S).group(1) == re.search(r'<p class="small">(.*?)</p>', new_form, re.S).group(1)
    old_fields, new_fields = document(old_form).fields, document(new_form).fields
    assert [f.get("name") for f in old_fields] == [f.get("name") for f in new_fields]
    for old, new in zip(old_fields, new_fields):
        assert ("required" in old) == ("required" in new)
        assert old.get("type", "text") == new.get("type", "text")
        assert old.get("placeholder") == new.get("placeholder")
    assert re.findall(r"<option[^>]*>(.*?)</option>", old_form) == re.findall(r"<option[^>]*>(.*?)</option>", new_form)
    assert "Send Enquiry" in new_form and "Open Email Draft" not in new_form
    home_file = ROOT / "index.html"
    home = docs["index.html"]
    original_bytes = sum(f.stat().st_size for f in {ROOT/variants[local_path(home_file, i["src"])][0] for i in home.images})
    estimates = {}
    for name, viewport, dpr in [("phone_390px_2x", 390, 2), ("desktop_1440px_1x", 1440, 1), ("desktop_1440px_2x", 1440, 2)]:
        selected = set()
        for image in home.images:
            _, info, _ = variants[local_path(home_file, image["src"])]
            desired = slot(image, viewport) * dpr
            pick = next((v for v in info["variants"] if v["width"] >= desired), info["variants"][-1])
            selected.add(ROOT / pick["path"])
        total = sum(f.stat().st_size for f in selected)
        estimates[name] = {"image_bytes": total, "reduction_percent": round(100 * (1 - total / original_bytes), 2)}
    report = {
        "existing_image_files_preserved_against_backup": preserved_assets,
        "source_images_optimized": len(manifest), "webp_files_verified": len(variants),
        "inline_images_verified": inline_count, "pages_checked": len(docs),
        "pages_copy_preserved_except_requested_dates_and_caption": preserved_pages,
        "approved_hemp_image_positions_changed": approved_image_changes,
        "legacy_form_content_and_fields_match": True,
        "homepage_current_photos_original_bytes": original_bytes,
        "homepage_modeled_responsive_selection": estimates,
        "measurement_note": "Whole-page image-file totals modeled from CSS sizes and DPR, not browser network measurements, initial payload or Core Web Vitals.",
        "live_form_submission_tested": False, "browser_visual_tested": False
    }
    (ROOT / "_source/review/webp_validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run(Path(sys.argv[1]))
