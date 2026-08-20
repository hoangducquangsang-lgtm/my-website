# -*- coding: utf-8 -*-
"""Shared layout, CSS, nav, footer, schema helpers for the VietPaw site build."""
import json, os

DOMAIN = "vietpaw.com"
BASE_URL = f"https://{DOMAIN}"
BRAND = "VietPaw"
LEGAL_NAME = "WINVN INT CO., LTD"
PHONE = "+84 906 111 016"
PHONE_TEL = "+84906111016"
EMAIL = "sarah@vietpaw.com"
WHATSAPP = "+84 906 111 016"
WHATSAPP_NUM = "84906111016"  # for wa.me link (country code, no + or spaces)
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
        <li><a href="https://wa.me/{WHATSAPP_NUM}" target="_blank" rel="noopener">WhatsApp: {WHATSAPP}</a></li>
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
<!-- Google tag (gtag.js) - deferred load -->
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
(function(){{var id="G-XTXJ45XN8B",done=false;function load(){{if(done)return;done=true;var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id="+id;document.head.appendChild(s);gtag("js",new Date());gtag("config",id);}}var evs=["scroll","mousemove","touchstart","keydown","click"];function fire(){{load();evs.forEach(function(e){{window.removeEventListener(e,fire)}});}}evs.forEach(function(e){{window.addEventListener(e,fire,{{passive:true}})}});window.addEventListener("load",function(){{setTimeout(load,3500)}});}})();
</script>
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
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="main-nav"><span></span><span></span><span></span></button>
    <nav class="main-nav" id="main-nav" aria-label="Main">
      <ul>{nav_html(active_top)}</ul>
    </nav>
    <a class="btn btn-primary btn-header" href="/request-a-quote/">Request a Quote</a>
  </div>
</header>
<main id="main">
{content}
</main>
{footer_html()}
<a href="https://wa.me/{WHATSAPP_NUM}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp" style="position:fixed;right:18px;bottom:18px;z-index:999;width:56px;height:56px;border-radius:50%;background:#25D366;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.25)">
<svg viewBox="0 0 32 32" width="30" height="30" fill="#fff" aria-hidden="true"><path d="M16.02 3.2c-7.06 0-12.8 5.73-12.8 12.79 0 2.25.59 4.45 1.71 6.39L3.2 28.8l6.6-1.73a12.76 12.76 0 0 0 6.21 1.58h.01c7.06 0 12.79-5.73 12.79-12.79 0-3.42-1.33-6.63-3.75-9.05a12.7 12.7 0 0 0-9.04-3.61zm0 23.31h-.01a10.6 10.6 0 0 1-5.4-1.48l-.39-.23-3.92 1.03 1.05-3.82-.25-.4a10.56 10.56 0 0 1-1.62-5.63c0-5.86 4.77-10.63 10.64-10.63 2.84 0 5.51 1.11 7.52 3.12a10.58 10.58 0 0 1 3.11 7.52c0 5.86-4.77 10.63-10.63 10.63zm5.83-7.96c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.71.16-.21.32-.82 1.04-1 1.25-.18.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.59-.95-.85-1.59-1.9-1.78-2.22-.18-.32-.02-.49.14-.65.14-.14.32-.37.48-.55.16-.18.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.71-1.72-.98-2.35-.26-.62-.52-.53-.71-.54l-.61-.01c-.21 0-.56.08-.85.4-.29.32-1.11 1.09-1.11 2.65 0 1.56 1.14 3.07 1.3 3.28.16.21 2.25 3.43 5.44 4.81.76.33 1.35.52 1.81.67.76.24 1.45.21 2 .13.61-.09 1.89-.77 2.16-1.52.27-.75.27-1.39.19-1.52-.08-.13-.29-.21-.61-.37z"/></svg>
</a>
<script>(function(){{var h=document.querySelector(".site-header"),b=h&&h.querySelector(".nav-toggle");if(!b)return;b.addEventListener("click",function(){{var o=h.classList.toggle("nav-open");b.setAttribute("aria-expanded",o?"true":"false");}});h.querySelectorAll(".main-nav li.has-sub > a").forEach(function(a){{a.addEventListener("click",function(e){{if(window.matchMedia("(max-width:980px)").matches){{var li=a.parentNode;if(!li.classList.contains("open")){{e.preventDefault();li.parentNode.querySelectorAll(".has-sub.open").forEach(function(x){{if(x!==li)x.classList.remove("open");}});li.classList.add("open");}}}}}});}});}})();</script>
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
