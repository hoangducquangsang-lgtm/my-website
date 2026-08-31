"""Verify complete Proof removal and preserve every unrelated page and asset."""
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from PIL import Image
from build import MODULES
from validate_site import Document, ROOT
from retired_content import assert_retired_files_absent, is_retired_path


def parse(html):
    doc = Document()
    doc.feed(html)
    return doc


def run(backup):
    assert_retired_files_absent(ROOT)
    assert "content_proof" not in MODULES
    assert not (ROOT / "_source/content_proof.py").exists()
    manifest = json.loads((ROOT / "_source/page_manifest.json").read_text(encoding="utf-8"))
    assert len(manifest) == 67 and "/proof/" not in manifest
    preserved_assets = removed_assets = pages = photos = forms = 0
    with zipfile.ZipFile(backup) as archive:
        names = {n.replace("\\", "/"): n for n in archive.namelist()}
        prefix = next(n for n in names if n.endswith("_source/page_manifest.json")).removesuffix("_source/page_manifest.json")
        baseline_pages = set()
        for name, original in names.items():
            if not name.startswith(prefix):
                continue
            relative = name[len(prefix):]
            if name.endswith("/"):
                continue
            current = ROOT / relative
            if is_retired_path(relative):
                assert not current.is_file(), relative
                removed_assets += relative.startswith("assets/")
                continue
            previous = archive.read(original)
            if relative.startswith("assets/") and relative != "assets/style.css":
                assert current.read_bytes() == previous, "Unrelated asset changed: " + relative
                preserved_assets += 1
            if relative == "_source/guide_dates.py":
                assert current.read_bytes() == previous
            if not relative.endswith("index.html") or relative.startswith("_source/"):
                continue
            baseline_pages.add(relative)
            old_html = previous.decode("utf-8").replace("\r\n", "\n")
            html = current.read_text(encoding="utf-8")
            old, new = parse(old_html), parse(html)
            assert (new.title, new.meta, new.schemas, new.images) == (old.title, old.meta, old.schemas, old.images), relative
            for pattern in (r"<header\b.*?</header>", r"<footer\b.*?</footer>",
                            r"<form\b.*?</form>", r"<time\b.*?</time>",
                            r'<table><thead><tr><th scope="col">Order detail</th>.*?</table>'):
                assert re.findall(pattern, html, re.S) == re.findall(pattern, old_html, re.S), relative
            for _, _, link in new.links:
                path = urlsplit(urljoin("https://vietpaw.com/" + relative, link)).path
                assert not is_retired_path(path), (relative, link)
            assert "Proof document register" not in html
            pages += 1
            photos += len(new.images)
            forms += len(re.findall(r"<form\b", html))
        actual_pages = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("index.html") if "_source" not in p.parts}
        assert actual_pages == baseline_pages
    assert (pages, removed_assets, photos) == (67, 28, 85)
    image_manifest = json.loads((ROOT / "_source/review/responsive_images.json").read_text(encoding="utf-8"))
    derivatives = 0
    for relative, metadata in image_manifest["images"].items():
        assert not is_retired_path(relative)
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == metadata["sha256"]
        for variant in metadata["variants"]:
            with Image.open(ROOT / variant["path"]) as image:
                assert image.format == "WEBP" and image.size == (variant["width"], variant["height"])
            derivatives += 1
    assert derivatives == 131
    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    assert "/proof/" not in sitemap
    assert "/proof/" not in (ROOT / "_source/hosting/redirect-map.csv").read_text(encoding="utf-8")
    print(json.dumps({"pages_preserved": pages, "removed_proof_pages": 1,
                      "removed_proof_images": removed_assets, "unrelated_assets_unchanged": preserved_assets,
                      "inline_images_preserved": photos, "forms_preserved": forms,
                      "webp_variants_verified": derivatives, "errors": []}, indent=2))


if __name__ == "__main__":
    run(Path(sys.argv[1]))
