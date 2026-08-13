# -*- coding: utf-8 -*-
"""Shared layout, CSS, nav, footer, schema helpers for the VietPaw site build."""
import json, os

DOMAIN = "vietpaw.com"
BASE_URL = f"https://{DOMAIN}"
BRAND = "VietPaw"
LEGAL_NAME = "WINVN INT CO., LTD"
PHONE = "+84 906 111 016"
PHONE_TEL = "+84906111016"
EMAIL = "sarah.winvn@gmail.com"
ADDRESS = "70 St. 10, Van Phuc City, Hiep Binh Ward, Ho Chi Minh City, Vietnam"
FOUNDED = "2018"
COUNTRIES = "30+"
CAPACITY = "5–6 million units/year"

NAV = [
    ("Dog Toys", "/dog-toys/", [
        ("All Dog Toys", "/dog-toys/"),
        ("Chew Toys", "/dog-toys/chew-toys/"),
        ("Rope & Tug Toys", "/dog-toys/rope-toys/"),
        ("Fetch & Ball Toys", "/dog-toys/fetch-toys/"),
        ("Puzzle & Enrichment", "/dog-toys/puzzle-toys/"),
    ]),
    ("Cat Toys", "/cat-toys/", [
        ("All Cat Toys", "/cat-toys/"),
        ("Balls & Chasers", "/cat-toys/balls/"),
        ("Catnip & Chew Toys", "/cat-toys/catnip-toys/"),
    ]),
    ("Materials", "/materials/", [
        ("All Materials", "/materials/"),
        ("Coffee Wood", "/collections/coffee-wood/"),
        ("Coconut Fiber", "/collections/coconut-fiber/"),
        ("Hemp Fiber", "/collections/hemp-fiber/"),
        ("Loofah", "/collections/loofah/"),
    ]),
    ("Solutions", "/solutions/", [
        ("Overview", "/solutions/"),
        ("For Amazon Sellers", "/solutions/amazon-sellers/"),
        ("For Wholesalers & Distributors", "/solutions/wholesalers/"),
        ("For Eco Pet Shops (EU)", "/solutions/eco-pet-shops/"),
        ("For Startup Brands", "/solutions/startup-brands/"),
    ]),
    ("Company", "/about/", [
        ("About / Our Factory", "/about/"),
        ("Capabilities (OEM/ODM)", "/capabilities/"),
        ("Certifications & Compliance", "/certifications/"),
        ("Sustainability", "/sustainability/"),
        ("How to Order", "/how-to-order/"),
    ]),
    ("Guides", "/guides/", []),
]

FOOTER_LINKS = [
    ("Materials", [
        ("Coffee Wood", "/collections/coffee-wood/"),
        ("Coconut Fiber", "/collections/coconut-fiber/"),
        ("Hemp Fiber", "/collections/hemp-fiber/"),
        ("Loofah", "/collections/loofah/"),
    ]),
    ("Solutions", [
        ("Amazon Sellers", "/solutions/amazon-sellers/"),
        ("Wholesalers", "/solutions/wholesalers/"),
        ("Eco Pet Shops (EU)", "/solutions/eco-pet-shops/"),
        ("Startup Brands", "/solutions/startup-brands/"),
    ]),
    ("Company", [
        ("About / Our Factory", "/about/"),
        ("Capabilities (OEM/ODM)", "/capabilities/"),
        ("Certifications", "/certifications/"),
        ("Sustainability", "/sustainability/"),
        ("How to Order", "/how-to-order/"),
        ("Wholesale Catalogue", "/wholesale-catalogue/"),
    ]),
    ("Get in Touch", [
        ("Request a Quote", "/request-a-quote/"),
        ("Contact", "/contact/"),
        ("Guides & Resources", "/guides/"),
    ]),
]


def nav_html(active_top=""):
    items = []
    for label, href, children in NAV:
        cls = "active" if label == active_top else ""
        if children:
            sub = "".join(f'<li><a href="{c[1]}">{c[0]}</a></li>' for c in children)
            items.append(
                f'<li class="has-sub {cls}"><a href="{href}">{label}</a>'
                f'<ul class="sub-nav">{sub}</ul></li>'
            )
        else:
            items.append(f'<li class="{cls}"><a href="{href}">{label}</a></li>')
    return "".join(items)


def footer_html():
    cols = ""
    for title, links in FOOTER_LINKS:
        lis = "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in links)
        cols += f'<div class="footer-col"><h4>{title}</h4><ul>{lis}</ul></div>'
    return f"""
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <div class="footer-logo">{BRAND}</div>
      <p class="footer-tagline">Natural, biodegradable pet toys manufactured in Vietnam — coffee wood, coconut fiber, hemp fiber &amp; loofah. Wholesale, private label &amp; OEM/ODM.</p>
      <p class="footer-legal">A brand of <strong>{LEGAL_NAME}</strong>, manufacturing natural pet products since {FOUNDED}. Exporting to {COUNTRIES} countries.</p>
      <ul class="footer-contact">
        <li>{ADDRESS}</li>
        <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </div>
    {cols}
  </div>
  <div class="wrap footer-bottom">
    <p>&copy; {FOUNDED}–2026 {LEGAL_NAME}. All rights reserved. {BRAND} is the export &amp; wholesale brand of {LEGAL_NAME}.</p>
  </div>
</footer>
"""


def rfq_bar(text="Ready to see samples in your hands?", cta="Request a Free Sample"):
    return f"""
<section class="rfq-bar">
  <div class="wrap rfq-bar-inner">
    <p>{text}</p>
    <a class="btn btn-primary" href="/request-a-quote/">{cta}</a>
  </div>
</section>
"""


def breadcrumb_html(trail):
    """trail: list of (label, href) tuples, last one has href=None"""
    items = []
    ld_items = []
    for i, (label, href) in enumerate(trail, start=1):
        if href:
            items.append(f'<li><a href="{href}">{label}</a></li>')
        else:
            items.append(f'<li aria-current="page">{label}</li>')
        ld_items.append({
            "@type": "ListItem", "position": i, "name": label,
            "item": f"{BASE_URL}{href}" if href else None
        })
    schema = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": ld_items
    }
    return f'<nav class="breadcrumb"><ul>{"".join(items)}</ul></nav>', schema


def page(title, meta_description, path, content, active_top="", schemas=None, og_image="/assets/img/hero-lifestyle-toys.jpg"):
    schemas = schemas or []
    canonical = f"{BASE_URL}{path}"
    schema_tags = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
        for s in schemas
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/assets/style.css">
<link rel="icon" href="/assets/img/logo-icon.png">
{schema_tags}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/">{BRAND}<span class="brand-sub">by {LEGAL_NAME}</span></a>
    <nav class="main-nav" aria-label="Main">
      <ul>{nav_html(active_top)}</ul>
    </nav>
    <a class="btn btn-primary btn-header" href="/request-a-quote/">Request a Quote</a>
  </div>
</header>
<main id="main">
{content}
</main>
{footer_html()}
</body>
</html>
"""


def write_page(root, path, html):
    """path like '/about/' -> root/about/index.html ; '/' -> root/index.html"""
    if path == "/":
        target = os.path.join(root, "index.html")
    else:
        target = os.path.join(root, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(html)
    return target
