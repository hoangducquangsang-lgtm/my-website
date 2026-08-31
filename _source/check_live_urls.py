"""Read-only live URL audit. No form submissions or indexing calls."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html import unescape
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, build_opener, HTTPRedirectHandler
import json
import re
import sys
ROUTES=["/","/about/","/materials/","/certifications/","/collections/coffee-wood/",
        "/products/coffee-wood-dog-chew/","/solutions/wholesalers/","/factory/",
        "/contact/","/wholesale-catalogue/","/sustainability/"]
class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):return None
def fetch(url):
    try:
        opener=build_opener(NoRedirect)
        req=Request(url,headers={"User-Agent":"VietPaw-ReadOnly-URL-Audit/1.0","Cache-Control":"no-cache"})
        try:response=opener.open(req,timeout=25)
        except HTTPError as error:response=error
        with response:
            content=response.read(4*1024*1024)
            html=content.decode("utf-8",errors="replace")
            title=re.search(r"<title>(.*?)</title>",html,re.S|re.I)
            canonical=re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)',html,re.I)
            obsolete=[p for p in ("Exporting to 30+","EXW and EWX","Every material we use is biodegradable",
                      "1-for-1 replacement policy","manufacturing natural pet products since 2018")
                      if p.lower() in html.lower()]
            return {"url":url,"status":response.code,"location":response.headers.get("Location"),
                    "server":response.headers.get("Server"),"etag":response.headers.get("ETag"),
                    "sha256":sha256(content).hexdigest(),"title":unescape(title.group(1)) if title else None,
                    "canonical":canonical.group(1) if canonical else None,"obsolete_phrases":obsolete}
    except Exception as error:return {"url":url,"error":str(error)}
def run(destination):
    urls=[f"https://vietpaw.com{route}{suffix}" for route in ROUTES for suffix in ("","index.html")]
    with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(fetch,urls))
    pairs=[]
    for i,route in enumerate(ROUTES):
        clean,index=results[i*2:i*2+2]
        pairs.append({"route":route,"clean_status":clean.get("status"),"index_status":index.get("status"),
                      "identical_body":bool(clean.get("sha256")) and clean.get("sha256")==index.get("sha256"),
                      "index_redirects_to_clean":index.get("status")==301 and index.get("location") in (route,"https://vietpaw.com"+route)})
    report={"checked_at_utc":datetime.now(timezone.utc).isoformat(),"pairs":pairs,"responses":results,
            "warning":"Live content may differ from the edited local build until deployment. Search caches are not current HTTP evidence."}
    Path(destination).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"pairs":pairs,"errors":[r for r in results if "error" in r]},indent=2))
if __name__=="__main__":run(sys.argv[1])
