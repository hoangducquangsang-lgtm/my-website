"""Verify the VietPaw/legal-manufacturer split and safe Proof integration.

Uses the backup immediately before this branding update. No browser/network use.
"""
from pathlib import Path
from html import unescape
import hashlib
import json
import re
import sys
import zipfile
from urllib.parse import unquote
from validate_site import Document, ROOT, EXPECTED_ADDRESS, EXPECTED_TAGLINE
from content_proof import PROOF_RECORDS


def document(html):
    doc = Document()
    doc.feed(html)
    return doc


def plain(html):
    return " ".join(unescape(re.sub(r"<[^>]*>", " ", html)).split())


def branded(value):
    return re.sub(r"\bWINVN\b(?! INT CO\., LTD)", "VietPaw", value)


def run(backup):
    baseline = {}
    preserved_assets = 0
    with zipfile.ZipFile(backup) as archive:
        for name in archive.namelist():
            relative = name.replace("\\", "/").removeprefix(ROOT.name + "/")
            if relative.endswith("index.html") and not relative.startswith("_source/"):
                baseline[relative] = archive.read(name).decode("utf-8")
            if relative.startswith("assets/") and not relative.endswith("/") and relative != "assets/style.css":
                assert archive.read(name) == (ROOT / relative).read_bytes(), "Unrequested asset change: " + relative
                preserved_assets += 1
            if relative == "_source/guide_dates.py":
                assert archive.read(name) == (ROOT / relative).read_bytes(), "Guide dates changed"
    pages = {p.relative_to(ROOT).as_posix(): p.read_text(encoding="utf-8")
             for p in ROOT.rglob("index.html") if "_source" not in p.parts}
    assert len(baseline) == 67 and len(pages) == 68
    assert set(pages)-set(baseline) == {"proof/index.html"} and set(baseline) <= set(pages)
    shared_tables = 0
    photos = 0
    guides = 0
    products = 0
    for relative, html in pages.items():
        d = document(html)
        assert "VietPaw" in d.title and d.meta["og:site_name"] == "VietPaw"
        assert "VietPaw INT CO., LTD" not in html
        assert not re.search(r"\bWINVN\b", html.replace("WINVN INT CO., LTD", ""))
        header = re.search(r'<header\b.*?</header>', html, re.S).group()
        footer = re.search(r'<footer\b.*?</footer>', html, re.S).group()
        signature = "Natural Pet Products by WINVN INT CO., LTD."
        relation = "VietPaw is the commercial/export brand of WINVN INT CO., LTD, the legal manufacturer."
        assert signature in plain(header) and signature in plain(footer) and relation in plain(footer)
        assert EXPECTED_TAGLINE in plain(footer) and EXPECTED_ADDRESS in plain(footer)
        assert "biodegrad" not in footer.lower()
        proof_link = re.search(r'<a href="([^"]+)">Proof</a>', header)
        assert proof_link and ((ROOT / relative).parent / unquote(proof_link.group(1))).resolve() == (ROOT / "proof/index.html").resolve()
        assert 'vietpaw-favicon.svg' in html
        organization = next(s for s in d.schemas if s.get("@type") == "Organization")
        brand = next(s for s in d.schemas if s.get("@type") == "Brand")
        assert organization["name"] == organization["legalName"] == "WINVN INT CO., LTD"
        assert organization["brand"]["name"] == brand["name"] == "VietPaw"
        assert organization["brand"]["@id"] == brand["@id"]
        assert brand["slogan"] == signature and brand["description"] == relation
        assert organization["address"]["streetAddress"] == EXPECTED_ADDRESS
        assert "registered in Vietnam in 2019" in organization["description"]
        assert organization["email"] == "sarah@vietpaw.com" and organization["telephone"] == "+84 906 111 016"
        for s in d.schemas:
            if s.get("@type") == "Product":
                products += 1
                assert s["brand"]["name"] == "VietPaw" and s["brand"]["@id"] == brand["@id"]
                assert s["manufacturer"]["name"] == "WINVN INT CO., LTD" and s["manufacturer"]["@id"] == organization["@id"]
                assert "Commercial / export brand" in " ".join(d.main_text) and "Legal manufacturer" in " ".join(d.main_text)
        if relative not in baseline:
            continue
        old_html = baseline[relative]
        old = document(old_html)
        assert old.canonicals == d.canonicals and old.meta["robots"] == d.meta["robots"]
        assert [dict(i, alt=branded(i["alt"])) for i in old.images] == d.images, "Unrequested photo change: " + relative
        photos += len(d.images)
        assert d.meta["og:image"] == old.meta["og:image"] and d.meta["twitter:image"] == old.meta["twitter:image"]
        assert re.findall(r'<time\b[^>]*>.*?</time>', old_html) == re.findall(r'<time\b[^>]*>.*?</time>', html)
        # Only branding may change inside the restored five-field enquiry form.
        assert [branded(f) for f in re.findall(r'<form\b.*?</form>', old_html, re.S)] == re.findall(r'<form\b.*?</form>', html, re.S)
        old_tables = re.findall(r'<table><thead><tr><th scope="col">Order detail</th>.*?</table>', old_html, re.S)
        new_tables = re.findall(r'<table><thead><tr><th scope="col">Order detail</th>.*?</table>', html, re.S)
        assert [branded(t) for t in old_tables] == new_tables, "Commercial terms changed: " + relative
        shared_tables += len(new_tables)
        if relative.startswith("guides/") and relative != "guides/index.html":
            guides += 1
            old_article = next(s for s in old.schemas if s.get("@type") == "Article")
            new_article = next(s for s in d.schemas if s.get("@type") == "Article")
            assert new_article == json.loads(branded(json.dumps(old_article, ensure_ascii=False)))
            assert new_article["author"]["name"] == "Sarah"
            assert "By" in plain(html) and "Sarah · VietPaw · Updated" in plain(html)
    assert guides == 20 and products == 6 and shared_tables == 31 and photos == 85
    proof = pages["proof/index.html"]
    proof_text = plain(proof)
    for phrase in ("WYNVN INT CO., LTD", "ABC company details", "does not identify WINVN INT CO., LTD",
                   "not a register of current certificates", "publicly viewable and downloadable", "not authenticate signatures or seals"):
        assert phrase in proof_text, "Missing Proof scope warning: " + phrase
    for record in PROOF_RECORDS:
        assert record["title"] in proof_text and record["status"] in proof_text
    root_assets = list((ROOT / "assets").rglob("*"))
    asset_hashes = {hashlib.sha256(p.read_bytes()).hexdigest() for p in root_assets if p.is_file()}
    sources = []
    for record in PROOF_RECORDS:
        source = ROOT.parent / "7. Proof" / record["source"]
        sha = hashlib.sha256(source.read_bytes()).hexdigest()
        assert sha in asset_hashes, "Owner-authorized Proof original missing"
        target = ROOT / "assets/img/proof" / record["asset"]
        assert hashlib.sha256(target.read_bytes()).hexdigest() == sha, "Proof original altered"
        sources.append({"file": record["source"], "sha256": sha, "status": record["status"], "public_scan": True})
    for html in pages.values():
        assert not re.search(r'(?:src|href)="[^\"]*(?:7\. Proof|CO\.png|Fumigation(?:%20| )Certificate\.png|Phytosanitary\.png|Surrendered\.png)', html, re.I)
    proof_doc = document(proof)
    assert len(proof_doc.images) == 4, "Four owner-authorized scan previews must be shown"
    assert len(re.findall(r'download="proof-[^"]+\.png"', proof)) == 4
    assert 'target="_blank"' not in proof, "Proof images must not spawn new tabs"
    report = {"pages": 68, "sitemap_urls": 66, "brand_and_legal_entity_pages": 68,
              "new_proof_route": "/proof/", "proof_records": sources,
              "existing_assets_unchanged_except_stylesheet": preserved_assets,
              "existing_photo_positions_preserved": photos, "commercial_tables_unchanged": shared_tables,
              "product_brand_manufacturer_pairs": products, "guides_authors_and_dates_preserved": guides,
              "legacy_form_preserved_except_brand_subject": True, "original_proof_scans_public": True,
              "browser_visual_tested": False, "live_form_submission_tested": False, "errors": []}
    (ROOT / "_source/review/brand_proof_validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run(Path(sys.argv[1]))
