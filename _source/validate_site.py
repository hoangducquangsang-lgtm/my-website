"""Offline/source QA plus optional read-only local HTTP checks. No browser automation."""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from urllib.parse import urlsplit, unquote, urljoin
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from datetime import date
from guide_dates import GUIDE_UPDATED_DATES, updated_time

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://vietpaw.com"
EXPECTED_TAGLINE = "Natural pet toys manufactured in Vietnam — coffee wood, coconut fiber, hemp fiber & loofah. Wholesale, private label & OEM/ODM. Our manufacturer was registered in Vietnam in 2019. Exporting to 40+ countries."
EXPECTED_ADDRESS = "Floor 1, 70 Street No. 10, Van Phuc Residence 1, Quarter 22, Hiep Binh Ward, Ho Chi Minh City, Vietnam"

class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=set()
        self.links=[]
        self.headings=[]
        self.title=""
        self.h1=[]
        self.meta={}
        self.canonicals=[]
        self.schemas=[]
        self.json_buffer=None
        self.in_title=False
        self.h1_buffer=None
        self.main=False
        self.main_text=[]
        self.main_links=[]
        self.images=[]
        self.fields=[]
        self.labels=set()
        self.language=None
        self.nav_menus=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        if tag=="html": self.language=a.get("lang")
        if tag=="main": self.main=True
        if tag=="title": self.in_title=True
        if tag=="h1": self.h1_buffer=[]
        if tag in ("h1","h2","h3","h4"): self.headings.append(tag)
        if tag=="link" and a.get("rel")=="canonical": self.canonicals.append(a.get("href"))
        if tag=="meta": self.meta[a.get("name") or a.get("property")]=a.get("content")
        if tag=="script" and a.get("type")=="application/ld+json": self.json_buffer=[]
        if tag=="img": self.images.append(a)
        if tag=="details" and "nav-menu" in a.get("class", "").split(): self.nav_menus.append(a)
        if tag in ("input","select","textarea"): self.fields.append(a)
        if tag=="label": self.labels.add(a.get("for"))
        for key in ("href","src","action","data-success-url"):
            if key in a:
                self.links.append((tag,key,a[key]))
                if self.main and tag=="a": self.main_links.append(a[key])
        if "srcset" in a:
            for candidate in a["srcset"].split(","):
                self.links.append((tag,"srcset",candidate.strip().rsplit(" ",1)[0]))
    def handle_endtag(self,tag):
        if tag=="title": self.in_title=False
        if tag=="main": self.main=False
        if tag=="h1" and self.h1_buffer is not None:
            self.h1.append("".join(self.h1_buffer))
            self.h1_buffer=None
        if tag=="script" and self.json_buffer is not None:
            self.schemas.append(json.loads("".join(self.json_buffer)))
            self.json_buffer=None
    def handle_data(self,data):
        if self.in_title: self.title+=data
        if self.h1_buffer is not None: self.h1_buffer.append(data)
        if self.json_buffer is not None: self.json_buffer.append(data)
        elif self.main: self.main_text.append(data)

def route_for(path):
    parent=path.relative_to(ROOT).parent.as_posix()
    return "/" if parent=="." else "/"+parent+"/"

def run():
    errors=[]
    warnings=[]
    docs={}
    manifest=json.loads((ROOT/"_source/page_manifest.json").read_text(encoding="utf-8"))
    def check(ok,message):
        if not ok: errors.append(message)
    for file in sorted(ROOT.rglob("index.html")):
        if "_source" in file.parts: continue
        d=Document()
        html=file.read_text(encoding="utf-8")
        try: d.feed(html)
        except Exception as exc:
            errors.append(f"{file}: parse/schema error {exc}")
            continue
        route=route_for(file)
        docs[route]=(file,d)
        # The legal name is displayed only in the two shared brand signatures.
        check("VietPaw" in d.title,f"{route}: commercial brand missing from title")
        check("VietPaw INT CO., LTD" not in html,f"{route}: brand incorrectly used as legal company name")
        signature="Natural Pet Products by WINVN INT CO., LTD."
        check(html.count(signature)==2,f"{route}: expected exactly two manufacturer signatures")
        without_signatures=html.replace(signature,"")
        check(not re.search(r"\bWINVN\s+INT\b",without_signatures,re.I),f"{route}: manufacturer name outside the two signatures")
        check(d.meta.get("og:site_name")=="VietPaw",f"{route}: social site brand mismatch")
        header=re.search(r'<header\b.*?</header>',html,re.S)
        check(bool(header) and re.search(r'<a class="brand" href="[^"]+">VietPaw<span',header.group()),f"{route}: visible header brand mismatch")
        check(bool(header) and not re.search(r'<a\b[^>]*>Proof</a>',header.group()),f"{route}: Proof must not appear in main navigation")
        check('<span class="brand-sub">Natural Pet Products by WINVN INT CO., LTD.</span>' in html,f"{route}: brand signature missing from header")
        check('<p class="footer-brand-tagline"><em>Natural Pet Products by WINVN INT CO., LTD.</em></p>' in html,f"{route}: brand signature missing from footer")
        check("sarah.winvn@gmail.com" not in html,f"{route}: superseded email")
        check("Exporting to 30+" not in html,f"{route}: superseded export reach")
        footer=re.search(r'<footer class="site-footer">(.*?)</footer>',html,re.S)
        check(bool(footer),f"{route}: missing shared footer")
        if footer:
            plain=" ".join(unescape(re.sub(r"<[^>]+>"," ",footer.group(1))).split())
            check(EXPECTED_TAGLINE in plain,f"{route}: owner-requested footer text differs")
            for item in ("VietPaw","Natural Pet Products by WINVN INT CO., LTD.",EXPECTED_ADDRESS,"+84 906 111 016","WhatsApp: +84 906 111 016","sarah@vietpaw.com"):
                check(item in plain,f"{route}: footer field missing {item}")
            check("biodegrad" not in plain.lower(),f"{route}: environmental claim in shared footer")
            check(not re.search(r'<a\b[^>]*>Proof</a>',footer.group()),f"{route}: Proof must not appear in footer navigation")
        check(d.language=="en",f"{route}: wrong language")
        check(len(d.h1)==1,f"{route}: expected one H1, got {len(d.h1)}")
        check(bool(d.title.strip()),f"{route}: missing title")
        check(bool(d.meta.get("description")),f"{route}: missing description")
        check(d.canonicals==[BASE+route],f"{route}: wrong canonical")
        check(d.meta.get("og:url")==BASE+route,f"{route}: wrong OG URL")
        check(d.meta.get("og:title")==d.title,f"{route}: OG title mismatch")
        check(d.meta.get("twitter:title")==d.title,f"{route}: X title mismatch")
        check(d.meta.get("og:description")==d.meta.get("description"),f"{route}: OG description mismatch")
        check(d.meta.get("twitter:description")==d.meta.get("description"),f"{route}: X description mismatch")
        check("main" in d.ids,f"{route}: skip link target missing")
        check(len(d.nav_menus)==6,f"{route}: expected six navigation disclosure groups")
        check(all(m.get("name")=="main-navigation" and "open" not in m for m in d.nav_menus),f"{route}: navigation must share one exclusive group and start closed")
        check(any(tag=="script" and urlsplit(link).path.endswith("assets/navigation.js") for tag,_,link in d.links),f"{route}: navigation behavior script missing")
        check(all(i.get("alt") for i in d.images),f"{route}: image alt missing")
        for image in d.images:
            check(urlsplit(image.get("src", "")).path.endswith(".webp"),f"{route}: inline image is not WebP")
            check(bool(image.get("srcset")) and bool(image.get("sizes")),f"{route}: responsive image candidates missing")
            check(int(image.get("width",0))>0 and int(image.get("height",0))>0,f"{route}: image dimensions missing")
        check(route in manifest,f"{route}: missing from manifest")
        if route in manifest:
            expected="index,follow" if manifest[route]["indexable"] else "noindex,follow"
            check(d.meta.get("robots")==expected,f"{route}: robots mismatch")
        for schema in d.schemas:
            check(schema.get("@context")=="https://schema.org",f"{route}: bad schema context")
            if schema.get("@type")=="BreadcrumbList":
                items=schema["itemListElement"]
                check(items[-1].get("item")==BASE+route,f"{route}: final breadcrumb target missing")
                check(all(x.get("item","").startswith(BASE+"/") for x in items),f"{route}: incomplete breadcrumb")
            if schema.get("@type")=="Product":
                check(schema.get("brand",{}).get("name")=="VietPaw",f"{route}: product brand mismatch")
                check("manufacturer" not in schema,f"{route}: manufacturer must not be repeated outside the brand signatures")
                check(schema.get("image","").startswith(BASE+"/assets/"),f"{route}: product image not absolute")
                check(bool(schema.get("material")),f"{route}: product material missing")
                check(not any(k in schema for k in ("offers","aggregateRating","review","gtin")),f"{route}: unsupported commercial schema")
                check(schema.get("image")==d.meta.get("og:image"),f"{route}: product social image mismatch")
            if schema.get("@type")=="Article":
                check(schema.get("mainEntityOfPage")==BASE+route,f"{route}: article URL mismatch")
                check(bool(schema.get("author")) and bool(schema.get("publisher")),f"{route}: article responsibility missing")
                check(schema.get("author")=={"@type":"Person","name":"Sarah"},f"{route}: Sarah author schema missing")
                check(schema.get("headline")==d.h1[0],f"{route}: article headline mismatch")
                check(schema.get("description")==d.meta.get("description"),f"{route}: article description mismatch")
                check(schema.get("image")==d.meta.get("og:image"),f"{route}: article social image mismatch")
                check(schema.get("dateModified")==GUIDE_UPDATED_DATES.get(route.strip("/").split("/")[-1]),f"{route}: article update date mismatch")
            if schema.get("@type")=="Organization":
                check(schema.get("name")=="VietPaw",f"{route}: public organization/trade name mismatch")
                check("legalName" not in schema,f"{route}: legal name repeated in search metadata")
                check(schema.get("brand",{}).get("name")=="VietPaw",f"{route}: organization brand mismatch")
                check(schema.get("email")=="sarah@vietpaw.com",f"{route}: organization email mismatch")
                check(schema.get("address",{}).get("streetAddress")==EXPECTED_ADDRESS,f"{route}: legal address schema mismatch")
                check(not re.search(r"\bWINVN\b",json.dumps(schema),re.I),f"{route}: legal name outside permitted signatures")
            if schema.get("@type")=="Brand":
                check(schema.get("name")=="VietPaw" and schema.get("slogan")=="Natural Pet Products",f"{route}: brand schema mismatch")
        if route.startswith("/guides/") and route!="/guides/":
            check(any(urlsplit(u).path for u in d.main_links),f"{route}: missing contextual links")
            check('<span class="author-name">Sarah</span>' in html,f"{route}: visible Sarah byline missing")
            check(d.meta.get("author")=="Sarah",f"{route}: author metadata missing")
            check(updated_time(route.strip("/").split("/")[-1]) in html,f"{route}: visible editorial date mismatch")
            check('Not a veterinary assessment, legal opinion or product certificate.' not in html,f"{route}: obsolete boilerplate byline")
        if len(d.meta.get("description",""))>200:
            warnings.append(f"{route}: long meta description ({len(d.meta['description'])} chars)")
    titles=Counter(d.title for _,d in docs.values())
    guide_dates=sorted(date.fromisoformat(v) for v in GUIDE_UPDATED_DATES.values())
    check(len(guide_dates)==20 and len(set(guide_dates))==20,"Guides must have twenty distinct displayed dates")
    check(all((b-a).days in (3,4) for a,b in zip(guide_dates,guide_dates[1:])),"Guide dates must be spaced 3–4 days apart")
    hub_html=docs["/guides/"][0].read_text(encoding="utf-8")
    check(all(updated_time(slug) in hub_html for slug in GUIDE_UPDATED_DATES),"Guide list dates differ from article dates")
    hub_dates=[date.fromisoformat(value) for value in re.findall(r'<time datetime="([0-9-]+)">',hub_html)]
    check(hub_dates==list(reversed(guide_dates)),"Guide card order must use the same descending 3–4 day schedule")
    descriptions=Counter(d.meta.get("description") for _,d in docs.values())
    check(all(v==1 for v in titles.values()),"Duplicate page titles")
    check(all(v==1 for v in descriptions.values()),"Duplicate meta descriptions")
    incoming=Counter()
    for route,(file,d) in docs.items():
        for tag,key,link in d.links:
            u=urlsplit(link)
            if u.scheme or u.netloc: continue
            target=(ROOT/u.path.lstrip("/")) if u.path.startswith("/") else (file.parent/unquote(u.path))
            if not u.path: target=file
            if target.is_dir(): target=target/"index.html"
            target=target.resolve()
            check(target.is_relative_to(ROOT),f"{route}: link outside site {link}")
            check(target.exists(),f"{route}: broken {tag} {link}")
            if target.suffix==".html" and target.exists():
                dest=route_for(target)
                if dest!=route: incoming[dest]+=1
                if u.fragment and dest in docs:
                    check(unquote(u.fragment) in docs[dest][1].ids,f"{route}: missing anchor {link}")
        image=d.meta.get("og:image","")
        check(image.startswith(BASE+"/assets/"),f"{route}: invalid social image")
        check((ROOT/image.removeprefix(BASE+"/")).is_file(),f"{route}: missing social image")
    urls={n.text for n in ET.parse(ROOT/"sitemap.xml").getroot().iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
    expected={BASE+p for p,data in manifest.items() if data["indexable"]}
    check(urls==expected,"Sitemap differs from indexable manifest")
    check(set(docs)==set(manifest),"HTML route set differs from manifest")
    for route,data in manifest.items():
        if data["indexable"] and route!="/":
            check(incoming[route]>0,f"{route}: orphaned indexable URL")
    check("Sitemap: "+BASE+"/sitemap.xml" in (ROOT/"robots.txt").read_text(),"robots sitemap missing")
    replacements=json.loads((ROOT/"_source/review/image_replacements.json").read_text(encoding="utf-8"))
    # A relocated site may keep its original source-photo archive in another folder.
    raw_root=ROOT.parent/"1. Raw material/1. Hinh anh/HÌNH ẢNH"
    if "--raw-materials" in sys.argv:
        raw_root=Path(sys.argv[sys.argv.index("--raw-materials")+1]).resolve()
    for item in replacements:
        source=raw_root/item["source"]
        target=ROOT/"assets/img"/item["asset"]
        check(target.is_file(),"Replacement image missing: "+item["asset"])
        check(source.is_file() and target.is_file() and hashlib.sha256(source.read_bytes()).digest()==hashlib.sha256(target.read_bytes()).digest(),"Replacement is not the supplied original: "+item["asset"])
        for route,(file,d) in docs.items():
            references=[v for _,_,v in d.links]+[d.meta.get("og:image",""),d.meta.get("twitter:image","")]
            check(not any(urlsplit(v).path.endswith('/'+item["old"]) for v in references),f"{route}: retired image still referenced {item['old']}")
    rfq=docs["/request-a-quote/"][1]
    from content_guides import ARTICLES
    for article in ARTICLES:
        route="/guides/"+article["slug"]+"/"
        source_file,d=docs[route]
        target=(ROOT/article["commercial"][1].strip("/")/"index.html").resolve()
        targets={(source_file.parent/unquote(urlsplit(link).path)).resolve() for link in d.main_links
                 if not urlsplit(link).scheme and not urlsplit(link).netloc and urlsplit(link).path}
        check(target in targets,f"{route}: expected contextual commercial link missing")
    for field in rfq.fields:
        if field.get("type")=="hidden": continue
        check(field.get("id") in rfq.labels,"RFQ field has no label: "+str(field))
    names={f.get("name") for f in rfq.fields}
    check(names=={"name","company","email","segment","products","_subject","_gotcha"},"RFQ must match the legacy five-field form, subject and honeypot")
    check({f.get("name") for f in rfq.fields if "required" in f}=={"name","email"},"RFQ must require name and email only, as in the supplied old form")
    check(any(key=="action" and link=="https://formspree.io/f/mvkpbvlb" for _,key,link in rfq.links),"Legacy Formspree destination missing")
    check(docs["/request-a-quote/thank-you/"][1].meta.get("robots")=="noindex,follow","Thank-you page must be noindex")
    for route in ("/products/coffee-wood-dog-chew/","/guides/coffee-wood-chew-size-guide/"):
        text=" ".join(docs[route][1].main_text)
        for value in ("CC01-XS","CC01-XXL","Under 5 kg","Over 40 kg"):
            check(value in text,f"{route}: current reference size data missing {value}")
        check("3–5kg" not in text and "12–20kg" not in text,f"{route}: obsolete size bands")
    forbidden=("minimum 15% / $0.30","What our own AOV data shows","EWX","Trial Box of 3–5","Every material we use is biodegradable","safe when swallowed","no questions asked",
        "since 2018","200 pieces per design","200 pcs per design","12–14%","15–20 working days","25–30 for OEM/ODM",
        "five-stage QC workflow","five-stage inspection workflow","five stages of inspection","Free standard samples may be available","first-order shipping credit")
    for route,(_,d) in docs.items():
        text=" ".join(d.main_text)
        for phrase in forbidden: check(phrase.lower() not in text.lower(),f"{route}: obsolete claim {phrase}")
    backup=ROOT.parent/"_VietPaw_backups/VietPaw-before-SEO-2026-08-30.zip"
    preserved=0
    old_routes=set()
    if backup.exists():
        with zipfile.ZipFile(backup) as z:
            for name in z.namelist():
                norm=name.replace("\\","/")
                prefix=ROOT.name+"/"
                if not norm.startswith(prefix): continue
                rel=norm[len(prefix):]
                if rel.endswith("index.html"):
                    old_routes.add(rel)
                    check((ROOT/rel).exists(),"Existing URL deleted: "+rel)
                if rel.startswith("assets/") and rel not in ("assets/style.css","assets/rfq.js") and not rel.endswith("/"):
                    file=ROOT/rel
                    check(file.exists() and hashlib.sha256(file.read_bytes()).digest()==hashlib.sha256(z.read(name)).digest(),"Original asset changed: "+rel)
                    preserved+=1
    http_result=None
    if "--http" in sys.argv:
        def request(route):
            try:
                with urlopen("http://127.0.0.1:8765"+route,timeout=10) as response:
                    return route,response.status
            except Exception as exc: return route,str(exc)
        results=list(ThreadPoolExecutor(max_workers=8).map(request,docs))
        for route,status in results: check(status==200,f"HTTP {route}: {status}")
        http_result={"checked":len(results),"status_200":sum(s==200 for _,s in results)}
    report={"pages":len(docs),"indexed_sitemap_urls":len(urls),"guides":sum(p.startswith("/guides/") and p!="/guides/" for p in docs),
        "products":sum(p.startswith("/products/") for p in docs),"baseline_pages":len(old_routes),
        "original_assets_verified":preserved,"replacement_references_verified":len(replacements),
        "supplied_replacement_files_verified":len({x["asset"] for x in replacements}),
        "footer_pages_verified":len(docs),"sarah_authored_guides_verified":len(ARTICLES),"http":http_result,
        "navigation_pages_verified":len(docs),"guide_update_dates_verified":len(guide_dates),
        "displayed_guide_date_range":[guide_dates[0].isoformat(),guide_dates[-1].isoformat()],
        "content_words":{p:len(re.findall(r"\b[\w’-]+\b"," ".join(d.main_text))) for p,(_,d) in docs.items()},
        "warnings":warnings,"errors":errors}
    (ROOT/"_source/validation_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k!="content_words"},ensure_ascii=False,indent=2))
    if errors: raise SystemExit(1)

if __name__=="__main__": run()
