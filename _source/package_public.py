"""Export generated public files only. Never include sources, reports or backups."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys
import zipfile
from validate_site import Document, ROOT

def strings(value):
    if isinstance(value, dict):
        for item in value.values(): yield from strings(item)
    elif isinstance(value, list):
        for item in value: yield from strings(item)
    elif isinstance(value, str):
        yield value

def package(destination):
    target=Path(destination).resolve()
    if target.exists() or target.is_relative_to(ROOT):
        raise ValueError("Choose a new ZIP outside the website folder")
    manifest=json.loads((ROOT/"_source/page_manifest.json").read_text(encoding="utf-8"))
    included={ROOT/"robots.txt",ROOT/"sitemap.xml",ROOT/"CNAME"}
    for route in manifest:
        page=ROOT/route.strip("/")/"index.html"
        included.add(page)
        doc=Document()
        doc.feed(page.read_text(encoding="utf-8"))
        urls=[url for _,_,url in doc.links]+list(strings(doc.meta))+list(strings(doc.schemas))
        for value in urls:
            u=urlsplit(value)
            if u.scheme and u.netloc!="vietpaw.com": continue
            if u.scheme: asset=ROOT/unquote(u.path).lstrip("/")
            elif u.path.startswith("/"): asset=ROOT/unquote(u.path).lstrip("/")
            else: asset=page.parent/unquote(u.path)
            asset=asset.resolve()
            if asset.is_relative_to(ROOT/"assets") and asset.is_file(): included.add(asset)
    target.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(target,"x",zipfile.ZIP_DEFLATED) as archive:
        for source in sorted(included):
            archive.write(source,source.relative_to(ROOT).as_posix())
        archive.writestr(".nojekyll","")
    report={"zip":str(target),"files":len(included)+1,"html_pages":len(manifest),
            "contains_private_sources":False,"live_deployed":False}
    print(json.dumps(report,indent=2))
if __name__=="__main__": package(sys.argv[1])
