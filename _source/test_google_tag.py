"""Verify the owner-provided Google tag on every generated HTML page."""
import json
import re
from validate_site import ROOT

MEASUREMENT_ID = "G-XTXJ45XN8B"
manifest = json.loads((ROOT / "_source/page_manifest.json").read_text(encoding="utf-8"))
pages = sorted(path for path in ROOT.rglob("*.html")
               if "_source" not in path.relative_to(ROOT).parts
               and "_to_delete" not in path.relative_to(ROOT).parts)

assert len(pages) == len(manifest) == 67
for page in pages:
    relative = page.relative_to(ROOT).as_posix()
    html = page.read_text(encoding="utf-8")
    assert html.count(f"https://www.googletagmanager.com/gtag/js?id={MEASUREMENT_ID}") == 1, relative
    assert html.count(f"gtag('config', '{MEASUREMENT_ID}');") == 1, relative
    assert html.count("function gtag(){dataLayer.push(arguments);}") == 1, relative
    assert re.search(
        rf'<head>\s*<!-- Google tag \(gtag\.js\) -->\s*'
        rf'<script async src="https://www\.googletagmanager\.com/gtag/js\?id={MEASUREMENT_ID}"></script>',
        html,
    ), relative

print(json.dumps({
    "measurement_id": MEASUREMENT_ID,
    "html_pages_checked": len(pages),
    "tag_placements": len(pages),
    "duplicate_tags": 0,
    "errors": [],
}, indent=2))
