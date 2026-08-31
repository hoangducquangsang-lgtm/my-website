# -*- coding: utf-8 -*-
"""Reusable editorial components, not unverified sales claims."""
from html import escape
from urllib.parse import urlencode
from common import page, write_page, breadcrumb_html, rfq_bar, BRAND

MOQ = "From 50 pcs per SKU on selected standard products; format, size and packaging minimums are confirmed in the quote."
PRIVATE_LABEL = "Private-label runs start at 500 pcs. Custom hang tags, labels and printed boxes start at 500 pcs; confirm the quantity per SKU and artwork in your quote."
SAMPLES = "3 free samples. Buyer covers courier."
SAMPLE_DISPATCH = "Standard samples can be dispatched within 1 working day once the selection and courier arrangements are confirmed. Custom prototype timing is quoted separately."
LEAD = "Production lead time: 5–7 days for orders under 500 pcs; 60–80 days for a full container. Orders of 500 pcs or more below container volume, mixed orders and custom development need a project-specific schedule. Confirm the production start date after sample, artwork and order approval. Development, testing and freight are additional; production time is not an arrival date."
QC_PROTOCOL = "six-stage drying/quality protocol with five QC checkpoints"
MOISTURE = "Coffee wood moisture is checked on every batch: below 14% before packing. Batch moisture readings are available on request."
EXPORT_DOCS = "Certificate of Origin (CO), Fumigation Certificate, Phytosanitary Certificate, Packing List, Commercial Invoice and Bill of Lading (B/L), subject to destination/product requirements. Batch moisture readings are available on request."
RANGE_SCOPE = 'VietPaw focuses on pet toys and chews across four material collections. Our manufacturer has a broader five-line catalogue that also includes Pet Beds; <a href="https://www.winvnint.com/">see the manufacturer’s full range</a> or ask Sarah about bed options.'
SAFETY = "For supervised pet play only, not food. Select a size that cannot be swallowed whole. Remove damaged toys, loose strands or pieces, and replace worn items. Hard chews can damage teeth; seek veterinary advice for puppies, dental conditions or forceful chewing."
SOURCE_OEM = "https://www.winvnint.com/"
SOURCE_COMPANY = "https://www.winvnint.com/"
FTC = "https://www.ftc.gov/business-guidance/resources/environmental-claims-summary-green-guides"
CPSC = "https://www.cpsc.gov/Business--Manufacturing/Business-Education/Toy-Safety"
ECHA = "https://echa.europa.eu/en/regulations/reach/restriction"
AAHA = "https://www.aaha.org/resources/dont-chew-on-this/"
AMAZON = "https://sell.amazon.com/pricing"
IMAGE_DESCRIPTIONS = {
    "winvn-home-thu-cung-3.jpg": "A small dog holding a coffee wood chew stick indoors",
    "winvn-natural-toy-assortment.png": "VietPaw loofah play shapes and coffee wood stick displayed in a basket",
    "winvn-coffee-wood-single.jpg": "Finished coffee wood chew stick on a light background",
    "winvn-coffee-wood-sizes.png": "Six coffee wood chew stick sizes on a light background",
    "winvn-coconut-fiber-balls.jpg": "Coconut-fiber balls held outdoors against green foliage",
    "winvn-hemp-wood-assortment.jpg": "Rope-ball and coffee wood combinations displayed in a sample basket",
    "winvn-hemp-fiber-rope-ball.png": "Golden retriever holding a rope ball indoors",
    "winvn-hemp-rope-dog-toy.jpg": "Two coffee wood toys with knotted rope ends on a light background",
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
        ("Product MOQ",moq),("Private label",PRIVATE_LABEL),
        ("Samples",SAMPLES+" "+SAMPLE_DISPATCH),("Production lead time",LEAD),
        ("Branding","Laser engraving on suitable coffee wood surfaces starts at 50 pcs. This is separate from the 500-pc private-label packaging minimum. Custom development is quoted separately."),
        ("Packaging","Bulk bags, individual packs and paper/kraft boxes are options. Custom hang tags, labels and printed boxes start at 500 pcs."),
        ("Export documents",EXPORT_DOCS),
        ("Shipping","Confirm destination, Incoterm with named place, transport mode, carton data and the shipment-specific document list. Freight is not included unless stated.")])

def trust_links():
    return p(f'Review <a href="/factory/">factory and production information</a>, the coffee wood <a href="/quality-control/">{QC_PROTOCOL}</a> and <a href="/certifications/">testing and export-document scope</a> before approving your order.')

def publish(root,path,title,description,h1,lede,sections,active="",image=None,faqs=(),trail=None,noindex=False,product=None,schemas=()):
    bc,bs=breadcrumb_html(trail or [("Home","/"),(h1,None)])
    content=bc+hero(h1,lede,image=image,product=product)+"".join(sections)
    if faqs: content+=faq(faqs)
    content+=rfq_bar()
    write_page(root,path,page(title,description,path,content,active,[bs,*schemas],og_image=image or "/assets/img/winvn-natural-toy-assortment.png",noindex=noindex))
