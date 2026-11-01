# -*- coding: utf-8 -*-
"""Rebuild only generated site files; never delete the site or touch source assets."""
from pathlib import Path
from datetime import date
import importlib
import json
import shutil
from xml.sax.saxutils import escape
from common import PAGES, BASE_URL
from lastmod import resolve as resolve_lastmods
from responsive_images import save_manifest

ROOT = Path(__file__).resolve().parent.parent
MODULES = [
    "content_home_about", "content_company", "content_materials", "content_categories",
    "content_products", "content_solutions", "content_manufacturing", "content_guides",
]

# Retrieval/citation crawlers are allowed so the site can be quoted in AI answers;
# model-training crawlers stay blocked. Groups are exclusive in robots.txt, so each
# named agent repeats the /_source/ exclusion.
AI_SEARCH_AGENTS = [
    "OAI-SearchBot", "ChatGPT-User", "Claude-SearchBot", "Claude-User",
    "PerplexityBot", "Perplexity-User", "GoogleOther", "Bingbot",
]
AI_TRAINING_AGENTS = [
    "GPTBot", "ClaudeBot", "Google-Extended", "Applebot-Extended",
    "Meta-ExternalAgent", "Bytespider", "CCBot",
]


def build_robots():
    lines = ["# vietpaw.com crawler policy",
             "# AI search and user-triggered retrieval: allowed. Model training: blocked.",
             "",
             "User-agent: *", "Allow: /", "Disallow: /_source/", ""]
    lines.append("# AI search / retrieval crawlers - allowed")
    for agent in AI_SEARCH_AGENTS:
        lines += [f"User-agent: {agent}", "Allow: /", "Disallow: /_source/", ""]
    lines.append("# Model-training crawlers - blocked")
    for agent in AI_TRAINING_AGENTS:
        lines += [f"User-agent: {agent}", "Disallow: /", ""]
    lines += ["Sitemap: " + BASE_URL + "/sitemap.xml", ""]
    return "\n".join(lines)


RETIRED_REDIRECTS = {"wholesale-catalogue": "/request-a-quote/"}


def write_retired_redirects():
    """Client-side redirects for retired routes.

    GitHub Pages serves this site and ignores the .htaccess 301 rules, so a retired
    route needs a stub page that forwards the visitor and tells search engines the
    canonical destination. Keep both in step if hosting moves back to Apache.
    """
    for route, target in RETIRED_REDIRECTS.items():
        url = BASE_URL + target
        html = (
            '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<title>Moved - Request a Quote | VietPaw</title>\n'
            '<meta name="robots" content="noindex, follow">\n'
            f'<link rel="canonical" href="{url}">\n'
            f'<meta http-equiv="refresh" content="0; url={target}">\n'
            '</head>\n<body>\n'
            f'<p>This page has moved. Continue to <a href="{target}">request a quote</a>.</p>\n'
            f'<script>window.location.replace("{target}");</script>\n'
            '</body>\n</html>\n'
        )
        destination = ROOT / route
        destination.mkdir(parents=True, exist_ok=True)
        (destination / "index.html").write_text(html, encoding="utf-8")


def build():
    from retired_content import assert_retired_files_absent
    assert_retired_files_absent(ROOT)
    PAGES.clear()
    for module in MODULES:
        importlib.import_module(module).build(str(ROOT))
    if "/proof/" in PAGES:
        raise ValueError("The retired Proof route must not be published again.")
    shutil.copyfile(ROOT/"_source"/"style.css", ROOT/"assets"/"style.css")
    # lastmod reflects the page's own content history, not this build's clock.
    lastmods = resolve_lastmods(ROOT, PAGES, date.today().isoformat())
    urls = "\n".join(
        f"  <url><loc>{escape(BASE_URL+path)}</loc><lastmod>{lastmods[path]}</lastmod></url>"
        for path,data in sorted(PAGES.items()) if data["indexable"])
    (ROOT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'\n</urlset>\n',encoding="utf-8")
    (ROOT/"robots.txt").write_text(build_robots(), encoding="utf-8")
    (ROOT/"_source"/"page_manifest.json").write_text(json.dumps(PAGES,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    save_manifest()
    write_retired_redirects()
    from deployment import write_redirect_plan
    write_redirect_plan(ROOT, PAGES)
    print(f"Built {len(PAGES)} HTML pages; {sum(p['indexable'] for p in PAGES.values())} sitemap URLs. Existing assets preserved.")

if __name__ == "__main__":
    build()
