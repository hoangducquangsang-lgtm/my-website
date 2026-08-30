# -*- coding: utf-8 -*-
"""Reusable editorial components, not unverified sales claims."""
from html import escape
from urllib.parse import urlencode
from common import page, write_page, breadcrumb_html, rfq_bar, BRAND

MOQ = "From 50 pcs per SKU on selected standard products; format, size and packaging minimums are confirmed in the quote."
SAMPLES = "Free standard samples may be available. Ask us to confirm the selection, preparation time, courier cost and any first-order shipping credit before dispatch."
LEAD = "Indicative production: 15–20 working days for standard orders and 25–30 for OEM/ODM, after sample, artwork and order approval. Development, testing and freight are additional."
SAFETY = "For supervised pet play only, not food. Select a size that cannot be swallowed whole. Remove damaged toys, loose strands or pieces, and replace worn items. Hard chews can damage teeth; seek veterinary advice for puppies, dental conditions or forceful chewing."
SOURCE_OEM = "https://www.winvnint.com/oem"
SOURCE_COMPANY = "https://www.winvnint.com/"
FTC = "https://www.ftc.gov/business-guidance/resources/environmental-claims-summary-green-guides"
CPSC = "https://www.cpsc.gov/Business--Manufacturing/Business-Education/Toy-Safety"
ECHA = "https://echa.europa.eu/en/regulations/reach/restriction"
AAHA = "https://www.aaha.org/resources/dont-chew-on-this/"
AMAZON = "https://sell.amazon.com/pricing"
IMAGE_DESCRIPTIONS = {
    "winvn-home-thu-cung-3.jpg": "A small dog holding a coffee wood chew stick indoors",
    "winvn-natural-toy-assortment.png": "WINVN loofah play shapes and coffee wood stick displayed in a basket",
    "winvn-coffee-wood-single.jpg": "Finished coffee wood chew stick on a light background",
    "winvn-coffee-wood-sizes.png": "Six coffee wood chew stick sizes on a light background",
    "winvn-coconut-fiber-balls.jpg": "Coconut-fiber balls held outdoors against green foliage",
    "winvn-hemp-wood-assortment.jpg": "Rope-ball and coffee wood combinations displayed in a sample basket",
    "winvn-loofah-play-shapes.png": "Loofah cat-play shapes in a basket on a light surface",
    "winvn-loofah-growing.png": "A green loofah gourd growing on its vine",
    "winvn-moisture-check-kiem-go-9.jpg": "Moisture meter checking a coffee wood stick above a carton of sticks",
}

def image_description(src, fallback):
    return IMAGE_DESCRIPTIONS.get(src.rsplit("/",1)[-1], fallback)

def p(text):
    return "<p>"+text+"</p>"

def ul(items, ordered=False):
    tag = "ol" if ordered else "ul"
    return f'<{tag}>'+"".join("<li>"+i+"</li>" for i in items)+f"</{tag}>"

def table(headers, rows):
    return '<div class="table-scroll" tabindex="0" role="region" aria-label="'+escape(" / ".join(headers))+'"><table><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(x)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>'

def section(title, body, alt=False):
    return f'<section class="section{" section-alt" if alt else ""}"><div class="wrap"><h2>{title}</h2>{body}</div></section>'

def cards(items, cols=3):
    # Each card: heading, copy, destination, optional image.
    result = []
    for item in items:
        title,body,url,*img = item
        visual = f'<div class="card-img"><img src="{img[0]}" alt="{escape(image_description(img[0],title))}" loading="lazy"></div>' if img else ""
        result.append(f'<div class="card">{visual}<h3><a href="{url}">{title}</a></h3><p>{body}</p></div>')
    return f'<div class="grid grid-{cols}">'+"".join(result)+"</div>"

def hero(title, lede, eyebrow="Wholesale & Private Label", image=None, request="sample", product=None, ctas=True):
    query = urlencode({"request":request, **({"product":product} if product else {})})
    actions = f'<div class="hero-ctas"><a class="btn btn-primary" href="/request-a-quote/?{escape(query, quote=True)}">{"Request This Product Sample" if product else "Request Samples & Pricing"}</a><a class="btn btn-outline" href="/wholesale-catalogue/">Get Wholesale Catalogue</a></div>' if ctas else ""
    content = f'<div><p class="hero-eyebrow">{eyebrow}</p><h1>{title}</h1><p class="hero-lede">{lede}</p>{actions}</div>'
    visual = f'<img src="{image}" alt="{escape(image_description(image,title))}" loading="eager">' if image else ""
    if image and image.endswith("winvn-hemp-wood-assortment.jpg"):
        visual = '<figure>'+visual+'<figcaption>Sample assortment showing rope-ball and coffee wood combinations. Standalone balls and rope-only designs are quoted separately; the approved sample defines your order.</figcaption></figure>'
    return f'<section class="hero"><div class="wrap{" hero-inner" if image else ""}">{content}{visual}</div></section>'

def faq(items):
    return section("Buyer questions", "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in items))

def terms(moq=MOQ):
    return table(["Order detail","Planning information"],[
        ("MOQ",moq),("Samples",SAMPLES),("Production lead time",LEAD),
        ("Branding","Laser engraving on suitable wood surfaces; labels, tags and packaging for other materials. Custom work is quoted separately."),
        ("Packaging","Bulk bags, individual packs and paper/kraft boxes are options. Custom printed boxes may require around 200 pcs per design; confirm the current minimum."),
        ("Shipping","Confirm destination, Incoterm with named place, transport mode, carton data and the shipment-specific document list. Freight is not included unless stated.")])

def trust_links():
    return p('Review <a href="/factory/">factory and production information</a>, the <a href="/quality-control/">five-stage QC workflow</a> and <a href="/certifications/">testing and export-document scope</a> before approving your order.')

def publish(root,path,title,description,h1,lede,sections,active="",image=None,faqs=(),trail=None,noindex=False,product=None,schemas=()):
    bc,bs=breadcrumb_html(trail or [("Home","/"),(h1,None)])
    content=bc+hero(h1,lede,image=image,product=product)+"".join(sections)
    if faqs: content+=faq(faqs)
    content+=rfq_bar()
    write_page(root,path,page(title,description,path,content,active,[bs,*schemas],og_image=image or "/assets/img/winvn-natural-toy-assortment.png",noindex=noindex))
