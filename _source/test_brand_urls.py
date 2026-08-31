"""Read-only regression checks for public branding and clean canonical URLs."""
from pathlib import Path
from urllib.parse import urlsplit, urljoin
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "_source"))
from common import page, BASE_URL, BRAND_ENTITY_STATEMENT
from validate_site import Document

EXPECTED_TITLES = {
    "/materials/": "Pet Toy Materials: Coffee Wood, Coir, Hemp & Loofah | VietPaw",
    "/factory/": "Pet Toy Factory Vietnam | VietPaw",
    "/quality-control/": "Pet Toy Quality Control | VietPaw",
    "/services/wholesale-pet-products/": "Wholesale Natural Pet Products Supplier | VietPaw",
    "/pet-toys-manufacturer-vietnam/": "Pet Toy Manufacturer Vietnam | OEM & Private Label | VietPaw",
}
manifest = json.loads((ROOT / "_source/page_manifest.json").read_text(encoding="utf-8"))
checked_links = 0
schema_urls = 0
contact = None
def check_schema(value):
    global schema_urls
    if isinstance(value, dict):
        for item in value.values():
            check_schema(item)
    elif isinstance(value, list):
        for item in value:
            check_schema(item)
    elif isinstance(value, str) and value.startswith(BASE_URL):
        assert not urlsplit(value).path.endswith("/index.html"), value
        schema_urls += 1

for route, data in manifest.items():
    html = (ROOT / route.strip("/") / "index.html").read_text(encoding="utf-8")
    doc = Document()
    doc.feed(html)
    assert "VietPaw" in doc.title and not re.search(r"\bWINVN\b", doc.title, re.I), route
    assert doc.meta["og:title"] == doc.meta["twitter:title"] == doc.title == data["title"], route
    assert doc.meta["og:site_name"] == "VietPaw", route
    assert doc.canonicals == [BASE_URL + route] and doc.meta["og:url"] == BASE_URL + route, route
    assert not any("WINVN" in heading for heading in doc.h1), route
    assert not re.search(r"Talk to WINVN|WINVN sales contact", html, re.I), route
    assert '<a class="brand"' in html and '>VietPaw<span class="brand-sub">by WINVN INT CO., LTD.</span>' in html, route
    for tag, attr, href in doc.links:
        url = urlsplit(urljoin(BASE_URL + route, href))
        if tag == "a" and url.hostname == "vietpaw.com":
            assert not url.path.endswith("/index.html"), (route, href)
            checked_links += 1
    check_schema(doc.schemas)
    organization = next(item for item in doc.schemas if item.get("@type") == "Organization")
    assert organization["legalName"] == "WINVN INT CO., LTD.", route
    if route in EXPECTED_TITLES:
        assert doc.title == EXPECTED_TITLES[route], (route, doc.title)
    if route == "/contact/":
        assert doc.h1 == ["Talk to VietPaw About Your Next Product"]
        assert BRAND_ENTITY_STATEMENT in " ".join(doc.main_text)
        contact = doc.h1[0]
sitemap = ET.parse(ROOT / "sitemap.xml")
urls = [item.text for item in sitemap.findall(".//{*}loc")]
assert set(urls) == {BASE_URL + route for route, data in manifest.items() if data["indexable"]}
assert all(not urlsplit(url).path.endswith("/index.html") for url in urls)
assert len(urls) == len(set(urls))

for title, route in (
    ("Pet Toy Materials | WINVN", "/materials/"),
    ("Pet Toy Materials | winvn", "/materials/"),
    ("Pet Toy Materials | Other Brand", "/materials/"),
    ("Pet Toy Materials | VietPaw", "/materials/index.html"),
    ("Pet Toy Materials | VietPaw", "/materials/?legacy=1"),
):
    try:
        page(title, "test", route, "")
    except ValueError:
        pass
    else:
        raise AssertionError(("Build did not reject old branding/duplicate URL", title, route))
print(json.dumps({
    "pages": len(manifest), "titles_and_social_titles_checked": len(manifest),
    "expected_titles": EXPECTED_TITLES, "contact_h1": contact,
    "clean_internal_links": checked_links, "clean_schema_urls": schema_urls,
    "sitemap_urls": len(urls), "build_guards_tested": 5,
    "live_redirects_modified": False, "errors": [],
}, ensure_ascii=False, indent=2))
