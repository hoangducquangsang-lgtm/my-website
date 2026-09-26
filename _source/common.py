# -*- coding: utf-8 -*-
"""Shared layout and portable static-page writer. Company details reviewed 2026-08-31."""
import json
import os
import re
from html import escape
from urllib.parse import urlsplit
from responsive_images import responsive_markup, optimized_url, optimize_schema

DOMAIN = "vietpaw.com"
BASE_URL = f"https://{DOMAIN}"
GOOGLE_TAG_ID = "G-XTXJ45XN8B"
GOOGLE_TAG_HTML = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_TAG_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', '{GOOGLE_TAG_ID}');
</script>"""
BRAND = "VietPaw"
BRAND_TAGLINE = "Natural Pet Products"
BRAND_ENTITY_STATEMENT = f"{BRAND} is a Vietnamese manufacturer and exporter of natural-material pet toys"
BRAND_RELATIONSHIP = f"{BRAND_ENTITY_STATEMENT}, manufacturing in its own three factories in Vietnam."
BRAND_INTRO = f"{BRAND} manufactures natural-material pet toys in Vietnam and exports them to brands, wholesalers and retailers worldwide."
# Production and finishing sites. Street addresses are published only where confirmed.
# Owner instruction 2026-09-24: three own factories in Dak Lak, Gia Lai and Binh Duong; 100,000 pcs/month.
FACTORY_LOCATIONS = "Dak Lak, Gia Lai and Binh Duong"
SITES = [
    ("Factory — Dak Lak", "Dak Lak province, Central Highlands, Vietnam"),
    ("Factory — Gia Lai", "Gia Lai province, Central Highlands, Vietnam"),
    ("Factory — Binh Duong", "Binh Duong, southern Vietnam"),
    ("Head office, warehouse and export preparation",
     "Floor 1, 70 Street No. 10, Van Phuc Residence 1, Quarter 22, Hiep Binh Ward, Ho Chi Minh City, Vietnam"),
]
# Current audit brief: VietPaw is the site brand; our production team is identified in legal contexts.
# The contracting entity is named once per page, in the footer legal line.
CONTRACT_NOTICE = ("Company registration details, the payment beneficiary and the agreed terms are set out in your "
                   "quotation, invoice and contract. Ask for them in writing before placing an order — with any supplier.")
# Contact and export reach supplied directly by the site owner on 2026-08-30.
PHONE = "+84 906 111 016"
PHONE_TEL = "+84906111016"
EMAIL = "sarah@vietpaw.com"
# Legal details confirmed against WINVNINT and the owner's correction on 2026-08-31.
ADDRESS = "Floor 1, 70 Street No. 10, Van Phuc Residence 1, Quarter 22, Hiep Binh Ward, Ho Chi Minh City, Vietnam"
REGISTERED_YEAR = "2019"
REGISTRATION_DATE = "12 November 2019"
COUNTRIES = "40+"
CAPACITY = "100,000 pcs/month"
REVIEW_DATE = "2026-08-30"
# Owner instruction 2026-09-24: the only place the legal company is named on the site.
FOOTER_LEGAL = "VietPaw is an international B2B brand of WINVN INT CO., LTD"
PAGES = {}

NAV = [
    ("Dog Toys", "/dog-toys/", [
        ("All Dog Toys", "/dog-toys/"), ("Chew Toys", "/dog-toys/chew-toys/"),
        ("Gorilla Chews for Strong Chewers", "/products/gorilla-coffee-wood-dog-chew/"),
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
        ("About VietPaw", "/about/"), ("Sustainability", "/sustainability/"),
        ("How to Order", "/how-to-order/"), ("Contact", "/contact/")]),
    ("Guides", "/guides/", []),
]
SOCIAL = [
    ("LinkedIn", "https://www.linkedin.com/in/sarahhue",
     "M4.98 3.5A2.5 2.5 0 1 1 0 3.5a2.5 2.5 0 0 1 4.98 0zM.2 8.2h4.56V24H.2zM8.5 8.2h4.37v2.16h.06c.61-1.15 2.1-2.37 4.32-2.37 4.62 0 5.47 3.04 5.47 7v9.01h-4.56v-7.99c0-1.9-.03-4.35-2.65-4.35-2.66 0-3.06 2.07-3.06 4.21V24H8.5z"),
    ("Instagram", "https://www.instagram.com/sarah.naturalpettoys/",
     "M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16zM12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63c-.79.3-1.46.72-2.12 1.39C1.35 2.68.93 3.35.63 4.14.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.3.79.72 1.46 1.39 2.12.66.67 1.33 1.09 2.12 1.39.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56.79-.3 1.46-.72 2.12-1.39.67-.66 1.09-1.33 1.39-2.12.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91-.3-.79-.72-1.46-1.39-2.12-.66-.67-1.33-1.09-2.12-1.39-.76-.3-1.64-.5-2.91-.56C15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32zm0 10.16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm7.85-10.4a1.44 1.44 0 1 1-2.88 0 1.44 1.44 0 0 1 2.88 0z"),
    ("Facebook", "https://www.facebook.com/sarahhue6789",
     "M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.09 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.69.24 2.69.24v2.96h-1.52c-1.49 0-1.96.93-1.96 1.89v2.26h3.33l-.53 3.49h-2.8V24C19.61 23.09 24 18.1 24 12.07z"),
    ("YouTube", "https://www.youtube.com/@HueSarah-n4f",
     "M23.5 6.2a3.02 3.02 0 0 0-2.12-2.14C19.5 3.55 12 3.55 12 3.55s-7.5 0-9.38.51A3.02 3.02 0 0 0 .5 6.2C0 8.09 0 12 0 12s0 3.91.5 5.8a3.02 3.02 0 0 0 2.12 2.14c1.88.51 9.38.51 9.38.51s7.5 0 9.38-.51a3.02 3.02 0 0 0 2.12-2.14C24 15.91 24 12 24 12s0-3.91-.5-5.8zM9.55 15.57V8.43L15.82 12z"),
]

def social_html(heading="Follow VietPaw", heading_tag="h4", css_class="social-links"):
    items = "".join(
        f'<li><a href="{url}" class="social-link" rel="me noopener" target="_blank" '
        f'aria-label="{name} — opens in a new tab">'
        f'<svg class="social-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
        f'<path d="{path}"/></svg><span>{name}</span></a></li>'
        for name, url, path in SOCIAL)
    head = f"<{heading_tag}>{heading}</{heading_tag}>" if heading else ""
    return f'{head}<ul class="{css_class}">{items}</ul>'

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
<div class="footer-brand"><div class="footer-logo"><span class="brand-logo" aria-hidden="true"></span>{BRAND}</div>
<p class="footer-legal">{FOOTER_LEGAL}</p>
<p class="footer-brand-tagline"><em>Natural Pet Products</em></p>
<p class="footer-tagline">Natural pet toys manufactured in Vietnam — coffee wood, coconut fiber, hemp fiber &amp; loofah. Wholesale, private label &amp; OEM/ODM. Producing since {REGISTERED_YEAR} and exporting to {COUNTRIES} countries.</p>
<ul class="footer-contact"><li>{ADDRESS}</li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
<li><a href="https://wa.me/{PHONE_TEL[1:]}">WhatsApp: {PHONE}</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul>
<div class="footer-social">{social_html("Follow VietPaw")}</div></div>{cols}</div>
<div class="wrap footer-bottom"><p>&copy; 2026 {BRAND}. All rights reserved. Product specifications and order terms are confirmed in your quotation.</p></div>
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
            "name":BRAND,"url":BASE_URL+"/",
            "brand":{"@id":BASE_URL+"/#brand","@type":"Brand","name":BRAND},
            "description":BRAND_RELATIONSHIP,
            "telephone":PHONE,"email":EMAIL,
            "address":{"@type":"PostalAddress","streetAddress":ADDRESS,"addressCountry":"VN"}}

def brand_schema():
    return {"@context":"https://schema.org","@type":"Brand","@id":BASE_URL+"/#brand",
            "name":BRAND,"slogan":"Natural Pet Products","description":BRAND_INTRO,"url":BASE_URL+"/"}

# 2026-09-26 SEO pass: search-length titles and descriptions (<= ~65 / 120-160 chars) without changing on-page copy.
TITLE_OVERRIDES = {
 "/": "Natural Pet Toys Wholesale from Vietnam | VietPaw",
 "/dog-toys/": "Wholesale Natural Dog Toys from Vietnam | VietPaw",
}
META_OVERRIDES = {
 "/": "Coffee wood, coconut fiber, hemp and loofah pet toys made in Vietnam. Published sizes, moisture below 14%, wholesale and private label from 50 pcs.",
 "/about/": "Who VietPaw is, where our materials come from and which claims we will not make. Natural pet toys from Vietnam for wholesale, private label and OEM.",
 "/cat-toys/": "Build a cat-toy range from coconut-fiber balls and loofah shapes. Compare construction, dimensions and private-label packaging for retail.",
 "/collections/coconut-fiber/": "Coconut fiber (coir) pet toys from Vietnam: what the material is, what to declare beyond the fiber, and how to specify a ball you can reorder.",
 "/collections/coffee-wood/": "Seasoned Robusta coffee wood dog chews from Vietnam, six sizes plus the thick-cut Gorilla line, packed below 14% moisture. Process and limits.",
 "/collections/hemp-fiber/": "Hemp rope balls, knotted tugs and ball-with-rope toys from Vietnam. How to specify a rope toy by geometry and knot, not by appearance.",
 "/contact/": "Email sarah@vietpaw.com or WhatsApp +84 906 111 016 for natural pet toy samples, wholesale quotes, private label and OEM/ODM from Vietnam.",
 "/dog-toys/chew-toys/": "Non-edible natural dog chews led by coffee wood sticks and the Gorilla line for strong chewers. Compare sizes and specifications before ordering.",
 "/dog-toys/": "Coffee wood chews, coconut fiber balls and hemp rope toys from Vietnam. Compare by chewing style, see sizes, order wholesale or private label from 50 pcs.",
 "/dog-toys/puzzle-toys/": "Texture-led natural enrichment toys for dogs. Current products focus on material and shape; treat-dispensing designs are custom development.",
 "/dog-toys/rope-toys/": "Natural-fiber rope, knotted and ball-with-rope dog toys for supervised tug play. Specify fiber, rope geometry and packaging for wholesale.",
 "/guides/": "Buyer guides to natural pet toy materials, chew sizing, supplier checks, MOQ, lead times and which product claims can be supported.",
 "/products/coffee-wood-dog-chew/": "Coffee wood dog chews in six sizes XS–XXL with lengths, diameters, weights and carton counts. Below 14% moisture, ±3 mm length tolerance.",
 "/solutions/amazon-sellers/": "Natural pet toys for Amazon FBA sellers: pack dimensions, barcode artwork, carton weights and a marketplace prep brief before production.",
 "/solutions/eco-pet-shops/": "Natural pet toys for eco retailers: choose natural-material formats, check the whole pack and confirm which sourcing statements you can support.",
 "/solutions/pet-brands/": "Natural pet toy manufacturing for pet brands, with defined construction, artwork and approval stages that keep every reorder consistent.",
 "/solutions/retail-chains/": "Natural pet toy supply for retail chains: a consistent product and vendor pack, carton configuration, labeling and delivery windows.",
 "/solutions/startup-brands/": "Low-MOQ natural pet toys for startup brands: start from 50 pcs with a physical sample, then add branded packaging from 500 pcs per SKU.",
 "/solutions/": "Sourcing plans for Amazon sellers, distributors, startup brands, pet brands, eco shops and retail chains buying natural pet toys from Vietnam.",
 "/case-studies/": "VietPaw case study framework: how customer results will be verified before publication. No customer result is asserted on this draft page.",
}

def auto_faq_schema(content, path):
    items = re.findall(r'<div class="faq-item"><h3>(.*?)</h3><p>(.*?)</p></div>', content, re.S)
    if not items:
        return None
    strip = lambda t: re.sub(r"<[^>]+>", "", t).strip()
    return {"@context":"https://schema.org","@type":"FAQPage","@id":BASE_URL+path+"#faq",
            "mainEntity":[{"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for q,a in items]}

def page(title, meta_description, path, content, active_top="", schemas=None,
         og_image="/assets/img/vietpaw-natural-toy-assortment.png", noindex=False):
    # VietPaw is the public site brand; WINVN is identified in manufacturer/legal data.
    if re.search(r"\bWINVN\b", title, re.I) or not re.search(r"\bVietPaw\b", title):
        raise ValueError(f"Public page title must use VietPaw, not WINVN: {title}")
    if not path.startswith("/") or not path.endswith("/") or "index.html" in path or "?" in path or "#" in path:
        raise ValueError(f"Page path must be a clean canonical directory URL: {path}")
    title = TITLE_OVERRIDES.get(path, title)
    meta_description = META_OVERRIDES.get(path, meta_description)
    canonical = BASE_URL+path
    if not noindex and not any(isinstance(x,dict) and x.get("@type")=="FAQPage" for x in (schemas or [])):
        fq = auto_faq_schema(content, path)
        if fq: schemas = list(schemas or []) + [fq]
    content = responsive_markup(content)
    og_image = optimized_url(og_image)
    schemas = optimize_schema(list(schemas or []))
    if not any(s.get("@type")=="Organization" for s in schemas):
        schemas.append(organization_schema())
    if not any(s.get("@type")=="Brand" for s in schemas):
        schemas.append(brand_schema())
    for s in schemas:
        if s.get("@type")=="BreadcrumbList":
            s["itemListElement"][-1]["item"] = canonical
    schema_tags = "\n".join('<script type="application/ld+json">'+json.dumps(s,ensure_ascii=False).replace("<","\\u003c")+'</script>' for s in schemas)
    article_author = next((s.get("author",{}).get("name") for s in schemas if s.get("@type")=="Article"),None)
    author_meta = f'<meta name="author" content="{escape(article_author,quote=True)}">' if article_author else ""
    PAGES[path] = {"title":title,"description":meta_description,"indexable":not noindex}
    form_script = '<script src="/assets/rfq.js?v=20260924-form" defer></script>' if "data-enquiry-form" in content else ""
    sticky = "" if path=="/request-a-quote/" else f'<aside class="sticky-contact" aria-label="Contact sales"><a class="btn btn-primary" href="/request-a-quote/?request=sample">Request Sample</a><a class="btn btn-outline desktop-contact" href="https://wa.me/{PHONE_TEL[1:]}">WhatsApp</a></aside>'
    return f"""<!DOCTYPE html>
<html lang="en"><head>
{GOOGLE_TAG_HTML}
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title>
<meta name="description" content="{escape(meta_description,quote=True)}">
{author_meta}
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{'noindex,follow' if noindex else 'index,follow'}">
<meta property="og:title" content="{escape(title,quote=True)}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:description" content="{escape(meta_description,quote=True)}">
<meta property="og:type" content="{'article' if path.startswith('/guides/') and path!='/guides/' else 'website'}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{BASE_URL}{og_image}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(title,quote=True)}">
<meta name="twitter:description" content="{escape(meta_description,quote=True)}"><meta name="twitter:image" content="{BASE_URL}{og_image}">
<link rel="stylesheet" href="/assets/style.css?v=20260925-palette"><link rel="icon" type="image/svg+xml" href="/assets/vietpaw-favicon.svg">
{schema_tags}</head><body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="/"><span class="brand-logo" aria-hidden="true"></span>{BRAND}</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav" aria-label="Open menu"><span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span><span class="nav-toggle-bar"></span></button>
<nav class="main-nav" id="main-nav" aria-label="Main"><ul>{nav_html(active_top)}</ul></nav>
<a class="btn btn-primary btn-header" href="/request-a-quote/">Request a Quote</a>
</div></header><main id="main">{content}</main>{footer_html()}{sticky}<script src="/assets/local-preview.js?v=20260831-clean-urls" defer></script>{form_script}<script src="/assets/navigation.js?v=20260830-exclusive" defer></script></body></html>
"""

def write_page(root, path, html):
    target = os.path.join(root, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    # Public links use clean directory URLs; local-preview.js adapts file:// navigation only.
    def relative_url(url):
        if url.startswith("//"):
            return url
        parts = urlsplit(url)
        dest = os.path.join(root, parts.path.lstrip("/"))
        rel = os.path.relpath(dest, os.path.dirname(target)).replace(os.sep,"/")
        if parts.path.endswith("/"):
            rel = rel.rstrip("/") + "/"
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
