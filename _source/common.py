# -*- coding: utf-8 -*-
"""Shared layout and portable static-page writer. Content reviewed 2026-08-30."""
import json
import os
import re
from html import escape
from urllib.parse import urlsplit
from responsive_images import responsive_markup, optimized_url, optimize_schema

DOMAIN = "vietpaw.com"
BASE_URL = f"https://{DOMAIN}"
BRAND = "WINVN"
LEGAL_NAME = "WINVN INT CO., LTD"
# Contact and export reach supplied directly by the site owner on 2026-08-30.
PHONE = "+84 906 111 016"
PHONE_TEL = "+84906111016"
EMAIL = "sarah@vietpaw.com"
ADDRESS = "70 St. 10, Van Phuc City, Hiep Binh Ward, Ho Chi Minh City, Vietnam"
FOUNDED = "2018"
COUNTRIES = "40+"
CAPACITY = "5–6 million units/year"
REVIEW_DATE = "2026-08-30"
PAGES = {}

NAV = [
    ("Dog Toys", "/dog-toys/", [
        ("All Dog Toys", "/dog-toys/"), ("Chew Toys", "/dog-toys/chew-toys/"),
        ("Rope & Tug Toys", "/dog-toys/rope-toys/"), ("Fetch & Ball Toys", "/dog-toys/fetch-toys/"),
        ("Enrichment Toys", "/dog-toys/puzzle-toys/")]),
    ("Cat Toys", "/cat-toys/", [
        ("All Cat Toys", "/cat-toys/"), ("Balls & Chasers", "/cat-toys/balls/"),
        ("Catnip & Play Shapes", "/cat-toys/catnip-toys/")]),
    ("Materials", "/materials/", [
        ("All Materials", "/materials/"), ("Coffee Wood", "/collections/coffee-wood/"),
        ("Coconut Fiber", "/collections/coconut-fiber/"), ("Hemp Fiber", "/collections/hemp-fiber/"),
        ("Loofah", "/collections/loofah/")]),
    ("Manufacturing", "/capabilities/", [
        ("Manufacturing Overview", "/capabilities/"),
        ("Vietnam Manufacturer", "/pet-toys-manufacturer-vietnam/"),
        ("Factory & Production", "/factory/"), ("Quality Control", "/quality-control/"),
        ("OEM / ODM", "/services/oem-odm-pet-toy-manufacturing/"),
        ("Private Label", "/services/private-label-pet-toys/"),
        ("Wholesale", "/services/wholesale-pet-products/"),
        ("Testing & Export Documents", "/certifications/")]),
    ("Solutions", "/solutions/", [
        ("All Buyer Solutions", "/solutions/"), ("Amazon Sellers", "/solutions/amazon-sellers/"),
        ("Wholesalers & Distributors", "/solutions/wholesalers/"),
        ("Eco Pet Shops", "/solutions/eco-pet-shops/"),
        ("Startup Brands", "/solutions/startup-brands/"),
        ("Pet Brands", "/solutions/pet-brands/"), ("Retail Chains", "/solutions/retail-chains/")]),
    ("Company", "/about/", [
        ("About WINVN", "/about/"), ("Sustainability", "/sustainability/"),
        ("How to Order", "/how-to-order/"), ("Contact", "/contact/")]),
    ("Guides", "/guides/", []),
]
FOOTER_LINKS = [
    ("Materials", NAV[2][2][1:]),
    ("Manufacturing", [
        ("Vietnam Manufacturer", "/pet-toys-manufacturer-vietnam/"), ("Our Factory", "/factory/"),
        ("Quality Control", "/quality-control/"), ("OEM / ODM", "/services/oem-odm-pet-toy-manufacturing/"),
        ("Private Label", "/services/private-label-pet-toys/"), ("Wholesale", "/services/wholesale-pet-products/")]),
    ("Buyer Resources", [
        ("Solutions", "/solutions/"), ("Guides", "/guides/"), ("How to Order", "/how-to-order/"),
        ("Testing & Documents", "/certifications/"), ("Sustainability", "/sustainability/")]),
    ("Get in Touch", [
        ("Request a Quote / Sample", "/request-a-quote/"), ("Wholesale Catalogue", "/wholesale-catalogue/"),
        ("About", "/about/"), ("Contact", "/contact/")]),
]

def nav_html(active_top=""):
    items = []
    for label, href, children in NAV:
        cls = "active" if label == active_top else ""
        if children:
            sub = "".join(f'<li><a href="{h}">{escape(l)}</a></li>' for l,h in children)
            items.append(f'<li class="{cls}"><details class="nav-menu" name="main-navigation"><summary>{escape(label)}</summary><ul class="sub-nav">{sub}</ul></details></li>')
        else:
            items.append(f'<li class="{cls}"><a href="{href}">{escape(label)}</a></li>')
    return "".join(items)

def footer_html():
    cols = "".join('<div class="footer-col"><h4>'+t+'</h4><ul>'+
                   "".join(f'<li><a href="{h}">{l}</a></li>' for l,h in links)+'</ul></div>'
                   for t,links in FOOTER_LINKS)
    return f"""
<footer class="site-footer">
<div class="wrap footer-grid">
<div class="footer-brand"><div class="footer-logo">{BRAND}</div>
<p class="footer-tagline">Natural, biodegradable pet toys manufactured in Vietnam — coffee wood, coconut fiber, hemp fiber &amp; loofah. Wholesale, private label &amp; OEM/ODM. {LEGAL_NAME}, manufacturing natural pet products since {FOUNDED}. Exporting to {COUNTRIES} countries.</p>
<ul class="footer-contact"><li>{ADDRESS}</li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
<li><a href="https://wa.me/{PHONE_TEL[1:]}">WhatsApp: {PHONE}</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>{cols}</div>
<div class="wrap footer-bottom"><p>&copy; 2026 {LEGAL_NAME}. All rights reserved. Product specifications and order terms are confirmed in your quotation.</p></div>
</footer>"""

def rfq_bar(text="Ready to evaluate a sample for your range?", cta="Request Sample Options"):
    return f'<section class="rfq-bar"><div class="wrap rfq-bar-inner"><p>{text}</p><a class="btn btn-primary" href="/request-a-quote/?request=sample">{cta}</a></div></section>'

def breadcrumb_html(trail):
    items, ld_items = [], []
    for i,(label,href) in enumerate(trail,1):
        items.append(f'<li><a href="{href}">{escape(label)}</a></li>' if href else f'<li aria-current="page">{escape(label)}</li>')
        entry = {"@type":"ListItem","position":i,"name":label}
        if href:
            entry["item"] = BASE_URL+href
        ld_items.append(entry)
    return '<nav class="breadcrumb wrap" aria-label="Breadcrumb"><ul>'+"".join(items)+'</ul></nav>', {
        "@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":ld_items}

def organization_schema():
    return {"@context":"https://schema.org","@type":"Organization","@id":BASE_URL+"/#organization",
            "name":BRAND,"legalName":LEGAL_NAME,"url":BASE_URL+"/",
            "description":"Natural-material pet toys for wholesale, OEM/ODM and private label.",
            "telephone":PHONE,"email":EMAIL,
            "address":{"@type":"PostalAddress","streetAddress":ADDRESS,"addressCountry":"VN"}}

def page(title, meta_description, path, content, active_top="", schemas=None,
         og_image="/assets/img/winvn-natural-toy-assortment.png", noindex=False):
    canonical = BASE_URL+path
    content = responsive_markup(content)
    og_image = optimized_url(og_image)
    schemas = optimize_schema(list(schemas or []))
    if not any(s.get("@type")=="Organization" for s in schemas):
        schemas.append(organization_schema())
    for s in schemas:
        if s.get("@type")=="BreadcrumbList":
            s["itemListElement"][-1]["item"] = canonical
    schema_tags = "\n".join('<script type="application/ld+json">'+json.dumps(s,ensure_ascii=False).replace("<","\\u003c")+'</script>' for s in schemas)
    article_author = next((s.get("author",{}).get("name") for s in schemas if s.get("@type")=="Article"),None)
    author_meta = f'<meta name="author" content="{escape(article_author,quote=True)}">' if article_author else ""
    PAGES[path] = {"title":title,"description":meta_description,"indexable":not noindex}
    sticky = "" if path=="/request-a-quote/" else f'<aside class="sticky-contact" aria-label="Contact sales"><a class="btn btn-primary" href="/request-a-quote/?request=sample">Request Sample</a><a class="btn btn-outline desktop-contact" href="https://wa.me/{PHONE_TEL[1:]}">WhatsApp</a></aside>'
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title>
<meta name="description" content="{escape(meta_description,quote=True)}">
{author_meta}
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{'noindex,follow' if noindex else 'index,follow'}">
<meta property="og:title" content="{escape(title,quote=True)}">
<meta property="og:description" content="{escape(meta_description,quote=True)}">
<meta property="og:type" content="{'article' if path.startswith('/guides/') and path!='/guides/' else 'website'}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{BASE_URL}{og_image}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(title,quote=True)}">
<meta name="twitter:description" content="{escape(meta_description,quote=True)}"><meta name="twitter:image" content="{BASE_URL}{og_image}">
<link rel="stylesheet" href="/assets/style.css?v=20260830-menu-hemp"><link rel="icon" href="/assets/img/logo-icon.png">
{schema_tags}</head><body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="/">{BRAND}<span class="brand-sub">Natural Pet Products</span></a>
<nav class="main-nav" aria-label="Main"><ul>{nav_html(active_top)}</ul></nav>
<a class="btn btn-primary btn-header" href="/request-a-quote/">Request a Quote</a>
</div></header><main id="main">{content}</main>{footer_html()}{sticky}<script src="/assets/navigation.js?v=20260830-exclusive" defer></script></body></html>
"""

def write_page(root, path, html):
    target = os.path.join(root, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    # Keep the original offline-friendly delivery: relative HTML, assets and query strings.
    def relative_url(url):
        if url.startswith("//"):
            return url
        parts = urlsplit(url)
        dest = os.path.join(root, parts.path.lstrip("/"))
        if parts.path.endswith("/"):
            dest = os.path.join(dest, "index.html")
        rel = os.path.relpath(dest, os.path.dirname(target)).replace(os.sep,"/")
        if parts.query: rel += "?"+parts.query
        if parts.fragment: rel += "#"+parts.fragment
        return rel
    def relative(match):
        attr, url = match.groups()
        return f'{attr}="{relative_url(url)}"'
    def relative_srcset(match):
        candidates = []
        for candidate in match.group(1).split(","):
            url, descriptor = candidate.strip().rsplit(" ", 1)
            candidates.append(f'{relative_url(url) if url.startswith("/") else url} {descriptor}')
        return 'srcset="' + ", ".join(candidates) + '"'
    html = re.sub(r'(href|src|data-success-url)="(/[^"]*)"', relative, html)
    html = re.sub(r'srcset="([^"]+)"', relative_srcset, html)
    with open(target,"w",encoding="utf-8",newline="\n") as f:
        f.write(html)
    return target
