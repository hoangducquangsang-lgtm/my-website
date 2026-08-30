# -*- coding: utf-8 -*-
"""Rebuild only generated site files; never delete the site or touch source assets."""
from pathlib import Path
import importlib
import json
import shutil
from xml.sax.saxutils import escape
from common import PAGES, BASE_URL

ROOT = Path(__file__).resolve().parent.parent
MODULES = [
    "content_home_about", "content_company", "content_materials", "content_categories",
    "content_products", "content_solutions", "content_manufacturing", "content_guides",
]

def build():
    PAGES.clear()
    for module in MODULES:
        importlib.import_module(module).build(str(ROOT))
    shutil.copyfile(ROOT/"_source"/"style.css", ROOT/"assets"/"style.css")
    urls = "\n".join(f"  <url><loc>{escape(BASE_URL+path)}</loc></url>"
                     for path,data in sorted(PAGES.items()) if data["indexable"])
    (ROOT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'\n</urlset>\n',encoding="utf-8")
    (ROOT/"robots.txt").write_text("User-agent: *\nAllow: /\nDisallow: /_source/\n\nSitemap: "+BASE_URL+"/sitemap.xml\n",encoding="utf-8")
    (ROOT/"_source"/"page_manifest.json").write_text(json.dumps(PAGES,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Built {len(PAGES)} HTML pages; {sum(p['indexable'] for p in PAGES.values())} sitemap URLs. Existing assets preserved.")

if __name__ == "__main__":
    build()
