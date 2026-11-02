"""Regression checks for the owner-approved 2026-08-31 commercial corrections.

Read-only except the JSON test report. No browser or live enquiry submission.
The baseline is the ZIP immediately before this policy update.
"""
from pathlib import Path
from html import unescape
import json
import re
import sys
import zipfile

from validate_site import Document, ROOT, EXPECTED_ADDRESS, EXPECTED_TAGLINE


def parse(html):
    doc = Document()
    doc.feed(html)
    return doc


def normalized(text):
    return " ".join(unescape(text).split())


def run(backup):
    before_html = {}
    preserved_assets = 0
    with zipfile.ZipFile(backup) as archive:
        for name in archive.namelist():
            relative = name.replace("\\", "/").removeprefix(ROOT.name + "/")
            if relative.endswith("index.html") and not relative.startswith("_source/"):
                before_html[relative] = archive.read(name).decode("utf-8")
            if relative.startswith("assets/") and not relative.endswith("/"):
                assert (ROOT / relative).read_bytes() == archive.read(name), "Asset changed: " + relative
                preserved_assets += 1
            if relative in ("_source/guide_dates.py", "_source/style.css", "robots.txt", "sitemap.xml"):
                assert (ROOT / relative).read_bytes() == archive.read(name), "Unrelated file changed: " + relative
    pages = {p.relative_to(ROOT).as_posix(): p.read_text(encoding="utf-8")
             for p in ROOT.rglob("index.html") if "_source" not in p.parts}
    assert set(before_html) == set(pages) and len(pages) == 67
    texts = {}
    shared_terms_pages = []
    main_copy_changes = []
    metadata_changes = []
    allowed_meta_changes = {"about/index.html", "quality-control/index.html", "services/private-label-pet-toys/index.html"}
    approved_guide_copy_changes = {
        "guides/pet-toy-moq-fob-pricing-lead-times/index.html",
        "guides/pet-toy-safety-testing-requirements/index.html",
    }
    for relative, html in pages.items():
        old = parse(before_html[relative])
        new = parse(html)
        text = normalized(" ".join(new.main_text))
        texts[relative] = text
        assert old.h1 == new.h1 and old.title == new.title, "Unrequested title change: " + relative
        assert old.images == new.images, "Photo or responsive markup changed: " + relative
        assert old.nav_menus == new.nav_menus, "Menu markup changed: " + relative
        assert old.fields == new.fields and old.labels == new.labels, "Form changed: " + relative
        assert old.canonicals == new.canonicals, "Canonical changed: " + relative
        assert old.meta.get("robots") == new.meta.get("robots"), "Indexing changed: " + relative
        for key in ("og:image", "twitter:image", "author"):
            assert old.meta.get(key) == new.meta.get(key), "Unrequested metadata change: " + relative
        if old.meta.get("description") != new.meta.get("description"):
            assert relative in allowed_meta_changes, "Unapproved description change: " + relative
            metadata_changes.append(relative)
        for pattern in (r'<header\b.*?</header>', r'<form\b.*?</form>', r'<time\b[^>]*>.*?</time>', r'<script\b[^>]*\bsrc=[^>]*></script>'):
            assert re.findall(pattern, before_html[relative], re.S) == re.findall(pattern, html, re.S), "Protected markup changed: " + relative
        if normalized(" ".join(old.main_text)) != text:
            main_copy_changes.append(relative)
            if relative.startswith("guides/"):
                assert relative in approved_guide_copy_changes, "Unrelated Guide copy changed: " + relative
        footer = re.search(r'<footer class="site-footer">(.*?)</footer>', html, re.S).group(1)
        footer_text = normalized(re.sub(r'<[^>]+>', ' ', footer))
        assert EXPECTED_TAGLINE in footer_text and EXPECTED_ADDRESS in footer_text
        assert "biodegrad" not in footer_text.lower()
        for pattern in (r"\b2018\b", r"\b200\s*(?:pcs|pieces)\b", r"12\s*[–—-]\s*14\s*%",
                        r"15\s*[–—-]\s*20\s*(?:working\s*)?days", r"25\s*[–—-]\s*30\s*(?:working\s*)?(?:days|for OEM)",
                        r"five.stage (?:QC|quality.control|inspection)", r"five stages of inspection",
                        r"Van Phuc City", r"Free standard samples may be available", r"first.order shipping credit",
                        r"3\s*[–—-]\s*5\s*free samples"):
            assert not re.search(pattern, unescape(html), re.I), f"Retired claim {pattern}: {relative}"
        if not relative.startswith("guides/"):
            assert "biodegrad" not in new.meta["description"].lower(), "Environmental marketing metadata: " + relative
        org = next(s for s in new.schemas if s.get("@type") == "Organization")
        assert org["address"]["streetAddress"] == EXPECTED_ADDRESS
        assert "registered in Vietnam in 2019" in org["description"]
        assert org["email"] == "sarah@vietpaw.com" and org["telephone"] == "+84 906 111 016"
        for schema in new.schemas:
            if schema.get("@type") == "Article":
                previous = next(s for s in old.schemas if s.get("@type") == "Article")
                assert schema == previous, "Guide schema/date changed: " + relative
        if "<th scope=\"col\">Order detail</th>" in html:
            shared_terms_pages.append(relative)
            for phrase in ("Private-label runs start at 500 pcs", "3 free samples. Buyer covers courier.",
                           "within 1 working day", "5–7 days for orders under 500 pcs", "60–80 days for a full container",
                           "Custom hang tags, labels and printed boxes start at 500 pcs", "starts at 50 pcs",
                           "subject to destination/product requirements", "Batch moisture readings are available on request"):
                assert phrase in text, f"Missing shared term {phrase}: {relative}"
    assert shared_terms_pages, "No shared commercial tables checked"
    for relative in ("index.html", "about/index.html", "materials/index.html", "services/wholesale-pet-products/index.html"):
        assert "four material collections" in texts[relative] and "five-line catalogue" in texts[relative] and "Pet Beds" in texts[relative]
    for relative in ("index.html", "services/private-label-pet-toys/index.html", "request-a-quote/index.html", "how-to-order/index.html"):
        for phrase in ("3 free samples. Buyer covers courier.", "5–7 days for orders under 500 pcs", "60–80 days for a full container"):
            assert phrase in texts[relative], f"Commercial policy missing {phrase}: {relative}"
    for relative in ("quality-control/index.html", "factory/index.html", "products/coffee-wood-dog-chew/index.html", "collections/coffee-wood/index.html"):
        assert "below 14% before packing" in texts[relative], "Coffee moisture missing: " + relative
        assert "six-stage drying/quality protocol with five QC checkpoints" in texts[relative], "QC term missing: " + relative
    assert "12 November 2019" in texts["about/index.html"]
    assert EXPECTED_ADDRESS in texts["contact/index.html"]
    for phrase in ("Certificate of Origin (CO)", "Fumigation Certificate", "Phytosanitary Certificate", "Packing List",
                   "Commercial Invoice", "Bill of Lading (B/L)", "subject to destination/product requirements", "on request"):
        assert phrase in texts["certifications/index.html"], "Export document missing: " + phrase
    report = {"baseline": str(backup.resolve()), "pages_checked": len(pages), "assets_preserved_byte_for_byte": preserved_assets,
              "shared_commercial_tables_checked": len(shared_terms_pages), "footer_and_organization_policy_pages": len(pages),
              "main_copy_changed_pages": len(main_copy_changes), "main_copy_changed_routes": sorted(main_copy_changes),
              "meta_descriptions_updated": sorted(metadata_changes), "guide_dates_and_authors_unchanged": True,
              "photo_responsive_markup_menu_form_and_urls_unchanged": True,
              "browser_visual_tested": False, "live_form_submission_tested": False, "errors": []}
    (ROOT / "_source/review/commercial_policy_validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "main_copy_changed_routes"}, indent=2))


if __name__ == "__main__":
    run(Path(sys.argv[1]))
