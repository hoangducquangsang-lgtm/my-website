"""Current offline acceptance checks against the pre-audit backup."""
from pathlib import Path
from urllib.parse import urlsplit
import csv
import json
import re
import sys
import zipfile
from validate_site import Document, ROOT

def parse(html):
    d=Document();d.feed(html);return d

def run(backup):
    baseline={};assets=0
    with zipfile.ZipFile(backup) as archive:
        names={name.replace("\\","/"):name for name in archive.namelist()}
        manifest=next(n for n in names if n.endswith("_source/page_manifest.json"))
        prefix=manifest.removesuffix("_source/page_manifest.json")
        for name,original in names.items():
            if not name.startswith(prefix): continue
            relative=name[len(prefix):]
            if relative.endswith("index.html"):baseline[relative]=archive.read(original).decode("utf-8")
            if relative.startswith("assets/") and not relative.endswith("/") and relative not in ("assets/style.css","assets/rfq.js"):
                assert (ROOT/relative).read_bytes()==archive.read(original),"Asset changed: "+relative
                assets+=1
            if relative in ("_source/guide_dates.py","robots.txt","sitemap.xml"):
                assert (ROOT/relative).read_bytes()==archive.read(original),"Unrequested route/date change"
    pages={p.relative_to(ROOT).as_posix():p.read_text(encoding="utf-8") for p in ROOT.rglob("index.html") if "_source" not in p.parts}
    assert set(pages)==set(baseline) and len(pages)==68
    photos=guides=tables=products=clean_links=0
    for relative,html in pages.items():
        d=parse(html);old=parse(baseline[relative])
        assert '<span class="brand-sub">by WINVN INT CO., LTD.</span>' in html
        assert "VietPaw is the international B2B/export brand of WINVN INT CO., LTD., a Vietnamese pet-product manufacturer." in html
        assert d.meta["og:site_name"]=="VietPaw" and "VietPaw" in d.title
        assert d.canonicals==old.canonicals and all(not u.endswith("index.html") for u in d.canonicals)
        assert d.meta["robots"]==old.meta["robots"]
        expected_images=[dict(image) for image in old.images]
        if relative=="factory/index.html":
            for image in expected_images:
                if image.get("alt")=="Pet Toy Factory & Production in Vietnam":
                    image["alt"]="Factory Review for Your VietPaw Order"
        assert d.images==expected_images,relative
        photos+=len(d.images)
        assert d.meta["og:image"]==old.meta["og:image"] and d.meta["twitter:image"]==old.meta["twitter:image"]
        for tag,key,url in d.links:
            u=urlsplit(url)
            if not u.scheme and tag=="a" and u.path:
                assert not u.path.endswith("index.html"),(relative,url)
                clean_links+=1
            if key=="data-success-url":assert not u.path.endswith("index.html")
        header=re.search(r"<header\b.*?</header>",html,re.S).group()
        assert re.search(r'<a class="brand"[^>]*>VietPaw<span',header)
        assert not re.search(r'<a\b[^>]*>Proof</a>',header)
        org=next(s for s in d.schemas if s.get("@type")=="Organization")
        brand=next(s for s in d.schemas if s.get("@type")=="Brand")
        assert org["name"]==org["legalName"]=="WINVN INT CO., LTD."
        assert org["brand"]["name"]==brand["name"]=="VietPaw"
        for item in d.schemas:
            if item.get("@type")=="Product":
                products+=1
                assert item["brand"]["name"]=="VietPaw"
                assert item["manufacturer"]["name"]=="WINVN INT CO., LTD."
        pattern=r'<table><thead><tr><th scope="col">Order detail</th>.*?</table>'
        current=re.findall(pattern,html,re.S)
        assert current==re.findall(pattern,baseline[relative],re.S)
        tables+=len(current)
        if relative.startswith("guides/"):
            old_main=re.search(r'<main id="main">(.*?)</main>',baseline[relative],re.S).group(1).replace("index.html","")
            main=re.search(r'<main id="main">(.*?)</main>',html,re.S).group(1)
            assert main==old_main,"Guide editorial text changed: "+relative
            if relative!="guides/index.html":
                guides+=1
                assert next(s for s in d.schemas if s.get("@type")=="Article")==next(s for s in old.schemas if s.get("@type")=="Article")
    assert (guides,products,photos,tables)==(20,6,89,31)
    quote=parse(pages["request-a-quote/index.html"])
    assert {f["name"] for f in quote.fields if "required" in f}=={"name","email","company","country","products"}
    assert 'enctype="multipart/form-data"' in pages["request-a-quote/index.html"]
    assert "Get Samples &amp; Pricing" in pages["request-a-quote/index.html"]
    catalogue=pages["wholesale-catalogue/index.html"]
    catalogue_doc=parse(catalogue)
    assert {f["name"] for f in catalogue_doc.fields if "required" in f}=={"email","country"}
    download=re.search(r'<a[^>]+href="[^"]+\.pdf"[^>]*>Download Catalogue \(PDF\)</a>',catalogue).group()
    assert download and download not in re.search(r"<form\b.*?</form>",catalogue,re.S).group()
    assert len(re.findall(r'download="proof-[^"]+\.png"',pages["proof/index.html"]))==4
    with (ROOT/"_source/hosting/redirect-map.csv").open(encoding="utf-8",newline="") as file:redirects=list(csv.DictReader(file))
    assert len(redirects)==272
    for row in redirects:
        assert row["source_url"].endswith("/index.html") and row["status_code"]=="301"
        assert row["target_url"].startswith("https://vietpaw.com/") and row["target_url"].endswith("/")
        assert row["preserve_query_string"]=="True"
        relative=urlsplit(row["target_url"]).path.strip("/")
        assert (ROOT/relative/"index.html").is_file()
        assert urlsplit(row["source_url"]).path.removesuffix("index.html")==urlsplit(row["target_url"]).path
    report={"pages":len(pages),"sitemap_urls":66,"clean_internal_links":clean_links,
            "guides_and_dates_preserved":guides,"photos_preserved":photos,"unchanged_assets":assets,
            "commercial_tables_preserved":tables,"products_with_brand_and_manufacturer":products,
            "quote_required_fields":5,"optional_catalogue_capture":True,
            "redirect_rows_prepared":len(redirects),"live_301_applied":False,
            "real_form_submission_tested":False,"browser_visual_tested":False,"errors":[]}
    (ROOT/"_source/review/seo_leads_validation.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
if __name__=="__main__":run(Path(sys.argv[1]))
