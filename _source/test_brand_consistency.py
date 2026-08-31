"""Current brand/menu regression checks against an immediately preceding site backup.

Offline only. Source image bytes, Guide dates, forms and order terms must survive.
"""
from pathlib import Path
from html import unescape
import hashlib
import json
import re
import sys
import zipfile
from PIL import Image
from common import BRAND, LEGAL_NAME, BRAND_TAGLINE, BRAND_INTRO, CONTRACT_NOTICE
from validate_site import Document, ROOT

def plain(value):
    value = re.sub(r"<(script|style)\b.*?</\1>", "", value, flags=re.S | re.I)
    return " ".join(unescape(re.sub(r"<[^>]*>", " ", value)).split())

def public_text(value):
    """Check readable metadata, not unchanged asset filenames or source URLs."""
    if isinstance(value, dict):
        return " ".join(public_text(item) for item in value.values())
    if isinstance(value, list):
        return " ".join(public_text(item) for item in value)
    if isinstance(value, str) and not re.match(r"^https?://", value):
        return value
    return ""

def doc(value):
    parsed = Document()
    parsed.feed(value)
    return parsed

def run(backup):
    assert BRAND == "VietPaw"
    assert LEGAL_NAME == "WINVN INT CO., LTD."
    assert BRAND_TAGLINE == "Natural Pet Products by WINVN INT CO., LTD."
    assert "WINVN" not in BRAND_INTRO
    baseline = {}
    assets = 0
    with zipfile.ZipFile(backup) as archive:
        names = {n.replace("\\", "/"): n for n in archive.namelist()}
        manifests = [n for n in names if n.endswith("_source/page_manifest.json")]
        assert len(manifests) == 1, "Backup must contain exactly one generated website"
        prefix = manifests[0].removesuffix("_source/page_manifest.json")
        for name, archived_name in names.items():
            if not name.startswith(prefix):
                continue
            relative = name[len(prefix):]
            if relative.endswith(".html"):
                baseline[relative] = archive.read(archived_name).decode("utf-8")
            if relative.startswith("assets/") and not relative.endswith("/"):
                assert (ROOT / relative).read_bytes() == archive.read(archived_name), "Asset changed: " + relative
                assets += 1
            if relative in ("_source/guide_dates.py", "sitemap.xml", "robots.txt"):
                assert (ROOT / relative).read_bytes() == archive.read(archived_name), "Unrequested change: " + relative
    pages = {p.relative_to(ROOT).as_posix(): p.read_text(encoding="utf-8")
             for p in ROOT.rglob("*.html") if "_source" not in p.relative_to(ROOT).parts}
    assert set(pages) == set(baseline) and len(pages) == 68, "Existing page set must be preserved"
    additions = {"about/index.html", "contact/index.html", "how-to-order/index.html",
                 "request-a-quote/index.html", "certifications/index.html"}
    guides = products = photos = commercial_tables = 0
    for relative, html in pages.items():
        old_html = baseline[relative]
        current, old = doc(html), doc(old_html)
        header = re.search(r"<header\b.*?</header>", html, re.S).group()
        footer = re.search(r"<footer\b.*?</footer>", html, re.S).group()
        assert re.search(r'<a class="brand" href="[^"]+">VietPaw<span', header)
        assert BRAND_TAGLINE in plain(header) and BRAND_TAGLINE in plain(footer)
        assert '<p class="footer-legal">' not in footer
        header_signature = f'<span class="brand-sub">{BRAND_TAGLINE}</span>'
        footer_signature = f'<p class="footer-brand-tagline"><em>{BRAND_TAGLINE}</em></p>'
        assert html.count(BRAND_TAGLINE) == 2
        assert header_signature in header and footer_signature in footer
        remaining = html.replace(header_signature, "").replace(footer_signature, "")
        assert not re.search(r"\bWINVN\s+INT\b", remaining, re.I), relative
        assert not re.search(r"\bWINVN\b", plain(remaining), re.I), relative
        assert header == re.search(r"<header\b.*?</header>", old_html, re.S).group()
        assert footer_signature in old_html
        assert not re.search(r'<a\b[^>]*>Proof</a>', header + footer), relative
        assert current.meta["og:site_name"] == BRAND and "VietPaw" in current.title
        assert not re.search(r"\bWINVN\b", public_text(current.schemas), re.I), relative
        assert not re.search(r"\bWINVN\b", public_text(current.meta), re.I), relative
        assert "WINVN INT CO., LTD.." not in html and "VietPaw INT CO." not in html
        org = next(s for s in current.schemas if s.get("@type") == "Organization")
        brand = next(s for s in current.schemas if s.get("@type") == "Brand")
        assert org["name"] == BRAND and "legalName" not in org
        assert org["brand"]["name"] == brand["name"] == BRAND
        assert org["brand"]["@id"] == brand["@id"]
        assert brand["slogan"] == "Natural Pet Products" and brand["description"] == BRAND_INTRO
        for schema in current.schemas:
            if schema.get("@type") == "WebSite":
                assert schema["name"] == BRAND
            if schema.get("@type") == "Product":
                products += 1
                assert schema["brand"]["name"] == BRAND and schema["brand"]["@id"] == brand["@id"]
                assert "manufacturer" not in schema
                previous = next(item for item in old.schemas if item.get("@type") == "Product")
                assert schema == {key: value for key, value in previous.items() if key != "manufacturer"}
                assert "<td>Legal manufacturer</td>" not in html
        assert current.canonicals == old.canonicals
        assert current.meta["robots"] == old.meta["robots"]
        assert current.images == old.images, "Photo markup changed: " + relative
        photos += len(current.images)
        for field in ("og:image", "twitter:image"):
            assert current.meta[field] == old.meta[field]
        assert re.findall(r"<form\b.*?</form>", html, re.S) == re.findall(r"<form\b.*?</form>", old_html, re.S)
        assert re.findall(r"<time\b.*?</time>", html, re.S) == re.findall(r"<time\b.*?</time>", old_html, re.S)
        pattern = r'<table><thead><tr><th scope="col">Order detail</th>.*?</table>'
        tables = re.findall(pattern, html, re.S)
        assert tables == re.findall(pattern, old_html, re.S), "Order terms changed: " + relative
        commercial_tables += len(tables)
        main = re.search(r'<main id="main">(.*?)</main>', html, re.S).group(1)
        old_main = re.search(r'<main id="main">(.*?)</main>', old_html, re.S).group(1)
        assert not re.search(r"\bWINVN\s+INT\b", main, re.I)
        if not re.search(r"\bWINVN\s+INT\b", old_main, re.I):
            assert main == old_main, "Unrequested editorial change: " + relative
        for field, value in old.meta.items():
            if not re.search(r"\bWINVN\s+INT\b", value or "", re.I):
                assert current.meta[field] == value, "Unrequested metadata change: " + relative
        if relative.startswith("guides/") and relative != "guides/index.html":
            guides += 1
            old_article = next(s for s in old.schemas if s.get("@type") == "Article")
            new_article = next(s for s in current.schemas if s.get("@type") == "Article")
            assert new_article == old_article
            assert new_article["author"] == {"@type": "Person", "name": "Sarah"}
    assert (guides, products, photos, commercial_tables) == (20, 6, 89, 31)
    for relative in additions - {"about/index.html"}:
        assert CONTRACT_NOTICE in plain(pages[relative]), "Company details missing: " + relative
    about = pages["about/index.html"]
    for label in ("Legal entity", "Legal manufacturer", "Invoices / contracts"):
        assert f"<td>{label}</td>" not in about
    assert "<td>Manufacturing base</td><td>Vietnam</td>" in about
    assert "<td>Manufacturer registered in Vietnam</td><td>12 November 2019</td>" in about
    proof = pages["proof/index.html"]
    assert len(doc(proof).images) == 4 and len(re.findall(r'download="proof-[^"]+\.png"', proof)) == 4
    assert 'target="_blank"' not in proof
    assert "WYNVN INT CO., LTD" in proof and "ABC company details" in proof
    manifest = json.loads((ROOT / "_source/review/responsive_images.json").read_text(encoding="utf-8"))
    variants = 0
    for relative, image in manifest["images"].items():
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == image["sha256"]
        for variant in image["variants"]:
            target = ROOT / variant["path"]
            assert target.stat().st_size == variant["bytes"]
            with Image.open(target) as opened:
                assert opened.format == "WEBP" and opened.size == (variant["width"], variant["height"])
            variants += 1
    assert variants == 155
    report = {
        "site_root": str(ROOT), "backup": str(backup), "pages": len(pages),
        "consistent_header_footer_pages": len(pages), "proof_removed_from_navigation": True,
        "proof_page_and_four_public_scans_preserved": True,
        "all_assets_unchanged": assets, "inline_photos_preserved": photos,
        "webp_variants_verified": variants, "guides_and_dates_preserved": guides,
        "products_without_repeated_manufacturer": products, "commercial_tables_preserved": commercial_tables,
        "pages_with_exactly_two_manufacturer_signatures": len(pages),
        "visible_manufacturer_name_in_body": False, "manufacturer_name_in_search_metadata": False,
        "live_deployment": False, "browser_visual_tested": False, "errors": []
    }
    (ROOT / "_source/review/brand_consistency_validation.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    run(Path(sys.argv[1]).resolve())
