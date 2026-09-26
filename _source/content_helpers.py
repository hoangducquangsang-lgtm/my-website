# -*- coding: utf-8 -*-
"""Reusable editorial components, not unverified sales claims."""
import re
from html import escape
from urllib.parse import urlencode
from common import page, write_page, breadcrumb_html, rfq_bar, BRAND

MOQ = "From 50 pcs per SKU on selected standard products; format, size and packaging minimums are confirmed in the quote."
PRIVATE_LABEL = "Private-label runs start at 500 pcs. Custom hang tags, labels and printed boxes start at 500 pcs; confirm the quantity per SKU and artwork in your quote."
SAMPLES = "3 free samples. Buyer covers courier."
SAMPLE_DISPATCH = "Standard samples can be dispatched within 1 working day once the selection and courier arrangements are confirmed. Custom prototype timing is quoted separately."
LEAD = "Production lead time: 5–7 days for stock packaging. 60–80 days when the order carries your own label, printed box or engraving — most of that window is artwork approval and tooling rather than production. Add 30–35 days port-to-port sea transit for the EU or the US. Confirm the production start date after sample, artwork and order approval; production time is not an arrival date."
QC_PROTOCOL = "drying and quality protocol with five QC checkpoints"
MOISTURE = "Coffee wood moisture is checked on every batch: below 14% before packing. Batch moisture readings are available on request."
EXPORT_DOCS = ("Seven documents ship with every order: Commercial Invoice, Packing List, Bill of Lading or Air Waybill, "
               "Certificate of Origin (EUR.1 for the EU under the EVFTA, Form B as standard, Form VJ for Japan), "
               "Phytosanitary Certificate, Fumigation Certificate and a Forest-Product Declaration — the last of these "
               "proves legal acquisition of the material and is a prerequisite for the Certificate of Origin. "
               "Batch moisture readings are available on request. We do not issue veterinary certificates (this is a wood "
               "article, not an animal by-product) or FSC certification (coffee is an agricultural crop, outside its scope); "
               "laboratory testing is arranged separately on request.")
RANGE_SCOPE = 'VietPaw manufactures and sells pet toys and chews across four material collections: coffee wood, coconut fiber, hemp and loofah.'
SAFETY = "For supervised pet play only, not food. Select a size that cannot be swallowed whole. Remove damaged toys, loose strands or pieces, and replace worn items. Strong chewers need a larger, thicker chew such as our Gorilla line; seek veterinary advice for puppies and dogs with dental conditions."
SOURCE_OEM = "/services/oem-odm-pet-toy-manufacturing/"
SOURCE_COMPANY = "/about/"
FTC = "https://www.ftc.gov/business-guidance/resources/environmental-claims-summary-green-guides"
CPSC = "https://www.cpsc.gov/Business--Manufacturing/Business-Education/Toy-Safety"
ECHA = "https://echa.europa.eu/en/regulations/reach/restriction"
AAHA = "https://www.aaha.org/resources/dont-chew-on-this/"
AMAZON = "https://sell.amazon.com/pricing"
IMAGE_DESCRIPTIONS = {
    "gorilla-coffee-wood-chews-three-pieces.jpg": "Three thick-cut Gorilla coffee wood chews on a white background",
    "golden-retriever-chewing-coffee-wood-chew-floor.jpg": "Golden retriever lying on a wooden floor chewing a coffee wood chew",
    "vietpaw-home-lifestyle.jpg": "A small dog holding a coffee wood chew stick indoors",
    "vietpaw-natural-toy-assortment.png": "VietPaw loofah play shapes and coffee wood stick displayed in a basket",
    "coffee-wood-chew-grain-detail.jpg": "Finished coffee wood chew stick on a light background",
    "vietpaw-coffee-wood-sizes.png": "Six coffee wood chew stick sizes on a light background",
    "vietpaw-coconut-fiber-balls.jpg": "Coconut-fiber balls held outdoors against green foliage",
    "vietpaw-hemp-wood-assortment.jpg": "Rope-ball and coffee wood combinations displayed in a sample basket",
    "hemp-rope-balls-three-sizes.jpg": "Three knotted hemp rope balls in small, medium and large",
    "golden-retriever-gnawing-coffee-wood.jpg": "Golden retriever gnawing a coffee wood piece",
    "coconut-fiber-ball-sizes-with-rope-toy.jpg": "Small and large coconut fiber balls beside a coir rope toy",
    "cat-hugging-loofah-toy.jpg": "Cat hugging and biting a loofah toy",
    "coconut-fiber-ball-top-view.jpg": "Wound coconut fiber ball seen from above",
    "vietpaw-hemp-rope-dog-toy.jpg": "Two coffee wood toys with knotted rope ends on a light background",
    "vietpaw-loofah-play-shapes.png": "Loofah cat-play shapes in a basket on a light surface",
    "vietpaw-loofah-growing.png": "A green loofah gourd growing on its vine",
    "vietpaw-moisture-check.jpg": "Moisture meter checking a coffee wood stick above a carton of sticks",
}


CARTON = "Export master carton 51 × 31 × 39 cm (0.062 m³), 30 cartons per pallet, 429 cartons in a 20 ft container and 850 in a 40 ft. Treat these as planning references and confirm the carton data for your packed SKU before booking."
SEA_TRANSIT = "Sea transit from Cat Lai, Ho Chi Minh City, is commonly quoted at 30–35 days port to port for the EU and the US. Inland legs, customs clearance and any consolidation are additional."

def answer(text):
    """The direct answer a reader (or an AI assistant) should be able to lift verbatim."""
    return f'<div class="answer-box"><p>{text}</p></div>'

def fit(suitable, less_suitable, suit_head="Suitable for", less_head="Less suitable when"):
    return ('<div class="fit-grid">'
            f'<div><h3>{suit_head}</h3>'+ul(suitable)+'</div>'
            f'<div><h3>{less_head}</h3>'+ul(less_suitable)+'</div></div>')

def steps(items):
    """Step - action - result, the shape buyers and assistants can both follow."""
    out = []
    for i,(name,action,result,*note) in enumerate(items,1):
        extra = f'<p class="small"><strong>Note:</strong> {note[0]}</p>' if note else ""
        out.append(f'<li><strong>{name}</strong><br><em>Action:</em> {action}<br><em>Result:</em> {result}{extra}</li>')
    return '<ol class="steps">'+"".join(out)+"</ol>"

def _cells(headers, row):
    return ''.join('<td data-label="'+escape(re.sub(r"<[^>]+>","",str(h)),quote=True)+'">'+str(x)+'</td>' for h,x in zip(headers,row))

def _wrap_class(headers):
    # Up to 4 columns: stack into labelled cards on phones. Wider tables scroll with a hint.
    return "table-scroll stack" if len(headers) <= 4 else "table-scroll wide"

def spec_table(headers, rows, caption=None):
    cap = f'<caption>{caption}</caption>' if caption else ""
    return ('<div class="'+_wrap_class(headers)+'" tabindex="0" role="region" aria-label="'+escape(" / ".join(headers))+
            '"><table class="spec-table">'+cap+'<thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in headers)+
            '</tr></thead><tbody>'+''.join('<tr>'+_cells(headers,row)+'</tr>' for row in rows)+
            '</tbody></table></div>')

def figure(src, alt, caption, lazy=True):
    load = ' loading="lazy"' if lazy else ' loading="eager"'
    return f'<figure><img src="{src}" alt="{escape(alt, quote=True)}"{load}><figcaption>{caption}</figcaption></figure>'

def media(body, src, alt, caption, reverse=False):
    fig = figure(src, alt, caption)
    return ('<div class="grid grid-2">'+fig+'<div>'+body+'</div></div>') if reverse else \
           ('<div class="grid grid-2"><div>'+body+'</div>'+fig+'</div>')

INCOTERMS = ("EXW, FCA, FOB, CIF, DAP and DDP are quoted; always name the place with the term. "
             "FCA is the correct term for an air shipment — FOB is not. DDP suits a first-time importer who "
             "would rather not handle customs, though import VAT is usually not recoverable that way; DAP suits "
             "a VAT-registered buyer.")
PAYMENT = ("30% deposit on a stock order, 50% when the order carries your own label or printed box, balance "
           "against shipping documents. Air shipments are settled in full before the goods are handed over at "
           "the airport.")
CAFFEINE = ("Chew sticks are cut from the stem wood, not from the bean or the cherry. We do not publish a "
            "caffeine-free claim: no laboratory result has been produced for this material, and we would "
            "rather say so than print a figure nobody has measured. Ask us if your market requires a test.")
WEAR_BEHAVIOUR = ("In normal chewing the surface wears into soft frayed fibres rather than breaking into hard "
                  "fragments. That is an observation about how the material behaves, not a guarantee: a powerful "
                  "chewer can break a piece off a stick, and no supplier in this category has published test data "
                  "behind the phrase \u201csplinter-free\u201d.")
SIZE_ADVICE = ("When a dog sits at the top of a band, or is known to be a determined chewer, go up one size. "
               "The consequence of being one size too large is a chew that lasts longer; the consequence of being "
               "one size too small is the thing everybody is trying to avoid.")
ORDER_TIERS = ("Trial Box 100 pcs and Starting Box 500 pcs are the usual first steps above the 50 pcs per size "
               "minimum. Standard sizes are held in our warehouse, so a stock-packaging order does not wait for "
               "a production run.")

def image_description(src, fallback):
    return IMAGE_DESCRIPTIONS.get(src.rsplit("/",1)[-1], fallback)

def p(text):
    return "<p>"+text+"</p>"

def ul(items, ordered=False):
    tag = "ol" if ordered else "ul"
    return f'<{tag}>'+"".join("<li>"+i+"</li>" for i in items)+f"</{tag}>"

def table(headers, rows):
    return '<div class="'+_wrap_class(headers)+'" tabindex="0" role="region" aria-label="'+escape(" / ".join(headers))+'"><table><thead><tr>'+''.join('<th scope="col">'+x+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+_cells(headers,row)+'</tr>' for row in rows)+'</tbody></table></div>'

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
    if image and image.endswith("vietpaw-hemp-wood-assortment.jpg"):
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
    write_page(root,path,page(title,description,path,content,active,[bs,*schemas],og_image=image or "/assets/img/vietpaw-natural-toy-assortment.png",noindex=noindex))

# Owner instruction 2026-09-25: strong chewers are served by the Gorilla line (thick-cut coffee wood).
# Specification from the owner-confirmed source table; do not merge with the CC01 XS–XXL table.
GORILLA_SIZES = [
    ("S","GRLS","5–6 × 8","155–230"),
    ("M","GRLM","6–8 × 10","260–350"),
    ("L","GRLL","8–10 × 12","350–480"),
    ("XL","GRLXL","10–12 × 15","550–900"),
]
GORILLA = ("For strong chewers we make the <a href=\"/products/gorilla-coffee-wood-dog-chew/\">Gorilla line</a>: thick-cut coffee wood chews in four sizes, from GRLS "
           "(155–230 g) to GRLXL (550–900 g), with far more wood per piece than a standard stick of similar length.")

def gorilla_table():
    return spec_table(["Size","Reference SKU","Dimensions (cm)","Weight (g)"], GORILLA_SIZES,
        caption="Gorilla line — thick-cut coffee wood chews for strong chewers. Reference specification; coffee wood is a "
                "natural material and outline, grain and mass vary within each size. Confirm the size with your sample.")
