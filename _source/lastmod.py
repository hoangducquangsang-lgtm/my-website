# -*- coding: utf-8 -*-
"""Sitemap <lastmod> driven by real content change, never by the build clock.

The build rewrites every HTML file on every run, so file mtime and git commit
dates both collapse to a single date across the whole site. Google ignores a
sitemap whose lastmod values look unreliable, so a date here must only move
when the page's own content moved.

Each indexable route keeps a fingerprint of its <main> region in
page_lastmod.json. Same fingerprint -> the stored date is reused. Changed
fingerprint -> the date advances to the build date. Guides are different: their
date is the owner-assigned editorial date in guide_dates.py, so the sitemap,
the visible <time> element and the Article dateModified never contradict each
other; if a guide's content moved without that date being updated, the build
stops and asks for a deliberate date.
"""
from pathlib import Path
import hashlib
import json
import re

from guide_dates import GUIDE_UPDATED_DATES

REGISTRY = Path(__file__).resolve().parent / "page_lastmod.json"
MAIN_REGION = re.compile(r"<main\b.*?</main>", re.S)
CACHE_BUSTER = re.compile(r"\?v=[0-9A-Za-z.\-]+")


def fingerprint(html):
    """Hash the page's own content, ignoring shared chrome and asset versions."""
    region = MAIN_REGION.search(html)
    text = region.group(0) if region else html
    return hashlib.sha256(CACHE_BUSTER.sub("", text).encode("utf-8")).hexdigest()[:16]


def page_path(root, route):
    root = Path(root)
    return root / "index.html" if route == "/" else root / route.strip("/") / "index.html"


def guide_slug(route):
    """Return the guide slug for a guide article route, else None."""
    if not route.startswith("/guides/") or route == "/guides/":
        return None
    slug = route.strip("/").split("/")[-1]
    return slug if slug in GUIDE_UPDATED_DATES else None


def load_registry():
    if REGISTRY.exists():
        return json.loads(REGISTRY.read_text(encoding="utf-8"))
    return {}


def resolve(root, pages, today):
    """Return {route: lastmod} for indexable pages and refresh the registry."""
    root = Path(root)
    previous = load_registry()
    current = {}
    for route, data in sorted(pages.items()):
        if not data["indexable"]:
            continue
        target = page_path(root, route)
        if not target.is_file():
            raise ValueError(f"{route}: indexable page has no built file at {target}")
        mark = fingerprint(target.read_text(encoding="utf-8"))
        stored = previous.get(route, {})
        slug = guide_slug(route)
        if slug:
            lastmod = GUIDE_UPDATED_DATES[slug]
            if stored and stored["fingerprint"] != mark and stored["lastmod"] == lastmod:
                raise ValueError(
                    f"{route}: guide content changed but GUIDE_UPDATED_DATES['{slug}'] "
                    f"is still {lastmod}. Assign a deliberate editorial date, then build again."
                )
        elif stored.get("fingerprint") == mark:
            lastmod = stored["lastmod"]
        else:
            lastmod = today
        current[route] = {"fingerprint": mark, "lastmod": lastmod}
    REGISTRY.write_text(
        json.dumps(current, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return {route: entry["lastmod"] for route, entry in current.items()}
