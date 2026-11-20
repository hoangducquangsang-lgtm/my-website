# -*- coding: utf-8 -*-
"""Reusable editorial components, not unverified sales claims."""
import re
from html import escape
from urllib.parse import urlencode
from common import page, write_page, breadcrumb_html, rfq_bar, BRAND

MOQ = "From 50 pcs per product. Sizes can be mixed inside the 50, and an own-label product carries the same minimum. Packaging quantities are confirmed in the quote."
PRIVATE_LABEL = "An own-label product carries the same 50 pcs minimum as a plain one. Laser engraving on the wood starts at 50 pcs and is charged separately. Printed retail packaging \u2014 ivory board or unbleached kraft, paper and card only, with no plastic window or laminate \u2014 is quoted with its own print quantity. Artwork files and a print proof are exchanged before production."
SAMPLES = "3 free samples per customer. Buyer covers the courier, which may be credited against a first qualifying order."
SAMPLE_DISPATCH = "Standard samples can be dispatched within 1 working day once the selection and courier arrangements are confirmed. Custom prototype timing is quoted separately."
LEAD = "Production lead time for plain goods: 8–10 days for 50–200 pcs, 10–15 days for 200–1,000 pcs, 25–27 days for 1,000–5,000 pcs and 30–45 days for a full 20 ft container. Own-label, printed-box and engraved orders are confirmed per order. These exclude sampling and transit; add 30–35 days port-to-port sea transit for the EU or the US. Production time is not an arrival date."
# Owner instruction 2026-11-20: publish the commitment stated on coffeewoodchew.com.
MOULD_COMMITMENT = ("The two things we commit to on coffee wood are no weevils and no mould. A claim is assessed on "
                    "evidence: photographs of the container interior and the affected cartons, the stack position, a carton "
                    "opened from the middle of the stack and your own pin-meter readings, sent before anything is disposed of. "
                    "A description without photographs cannot be assessed. Condensation during a sealed-container voyage is "
                    "outside our control and is normally a cargo claim against the carrier or insurer, though it can also be a "
                    "supplier claim depending on the evidence. Note that fumigation is not an antifungal treatment: a "
                    "phytosanitary or fumigation certificate does not guarantee mould-free goods.")
QC_PROTOCOL = "drying and quality protocol with five QC checkpoints"
MOISTURE = "Coffee wood moisture is checked on every batch: below 14% before packing at the factory, then the pieces are vacuum packed with a desiccant sachet. Batch moisture readings are available on request."
EXPORT_DOCS = ("Seven documents ship with every order: Commercial Invoice, Packing List, Bill of Lading or Air Waybill, "
               "Certificate of Origin (EUR.1 for the EU under the EVFTA, Form B as standard, Form VJ for Japan), "
               "Phytosanitary Certificate, Fumigation Certificate and a Forest-Product Declaration — the last of these "
               "proves legal acquisition of the material and is a prerequisite for the Certificate of Origin. "
               "Batch moisture readings are available on request. We do not issue veterinary certificates (this is a wood "
               "article, not an animal by-product) or FSC certification (coffee is an agricultural crop, outside its scope); "
               "laboratory testing is arranged separately on request.")
# Non-wood pages (coconut fiber, hemp, loofah, cat toys): no wood-only clauses
# (Forest-Product Declaration, veterinary/FSC wording) — those belong to coffee wood.
EXPORT_DOCS_FIBER = ("Standard export documents: Commercial Invoice, Packing List, Bill of Lading or Air Waybill and "
                     "Certificate of Origin (EUR.1 for the EU under the EVFTA, Form B as standard, Form VJ for Japan). "
                     "Phytosanitary and fumigation certificates are issued per shipment where the destination requires "
                     "them for plant-fiber goods, so list them at booking. Laboratory testing is arranged separately on request.")
RANGE_SCOPE = 'VietPaw manufactures and sells pet toys and chews across four material collections: coffee wood, coconut fiber, hemp and loofah.'
# Generic safe-use line for every page; the Gorilla/dog-chew advice is added only on dog-chew pages.
SAFETY = "For supervised pet play only, not food. Select a size that cannot be swallowed whole. Remove damaged toys, loose strands or pieces, and replace worn items."
SAFETY_DOG_CHEW = SAFETY + " Strong chewers need a larger, thicker chew such as our Gorilla line; seek veterinary advice for puppies and dogs with dental conditions."
SOURCE_OEM = "/services/oem-odm-pet-toy-manufacturing/"
SOURCE_COMPANY = "/about/"
FTC = "https://www.ftc.gov/business-guidance/resources/environmental-claims-summary-green-guides"
CPSC = "https://www.cpsc.gov/Business--Manufacturing/Business-Education/Toy-Safety"
ECHA = "https://echa.europa.eu/en/regulations/reach/restriction"
AAHA = "https://www.aaha.org/resources/dont-chew-on-this/"
AMAZON = "https://sell.amazon.com/pricing"
IMAGE_DESCRIPTIONS = {
    "hemp-rope-loop-ball-toy.jpg": "Hemp rope toy with a loop handle and a knotted ball end",
    "coconut-fiber-ball-with-rope-toy.jpg": "Coconut fiber ball beside a knotted coir rope toy",
    "hemp-rope-toy-assortment.jpg": "Assortment of hemp rope balls and loop toys",
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
    "sgs-test-report-astm-f963-cover.jpg": "First page of the SGS Vietnam test report naming the sample, method and conclusion",
    "sgs-test-report-heavy-elements-results.jpg": "SGS results page showing the eight soluble heavy elements recorded as not detected",
    "phytosanitary-certificate-coffee-wood-toys.jpg": "Phytosanitary certificate for coffee wooden pet toys shipped to Germany, consignee details redacted",
    "eur1-movement-certificate-coffee-wood-toys.jpg": "EUR.1 movement certificate for coffee wooden pet toys to Germany, consignee and reference numbers redacted",
    "coffee-stems-on-trailer-central-highlands.jpg": "Tractor trailer loaded with coffee stems at a plantation in the Central Highlands",
    "worker-loading-coffee-stems-onto-trailer.jpg": "Worker lifting cut coffee stems onto a trailer at the plantation",
    "collecting-coffee-stems-at-the-plantation.jpg": "Worker collecting cut coffee stems onto a cart beside the coffee plants",
    "coffee-stem-intake-yard.jpg": "Coffee stems delivered and heaped in the intake yard",
    "coffee-wood-stacked-for-air-seasoning.jpg": "Coffee stems stacked in open rows for air seasoning",
    "cut-coffee-wood-billets.jpg": "Coffee wood cut to short billets before machining",
    "coffee-wood-billets-after-cross-cutting.jpg": "Pile of coffee wood billets after cross-cutting",
    "coffee-wood-chews-on-drying-racks.jpg": "Rows of shaped coffee wood chews laid out on drying racks",
    "graded-coffee-wood-chews-on-rack-rows.jpg": "Graded coffee wood chews arranged by size on rack rows",
    "coffee-wood-chews-inside-drying-chamber.jpg": "Coffee wood chews stacked under cover in the drying area",
    "moisture-meter-reading-on-coffee-wood-chew.jpg": "Moisture meter reading taken on a finished coffee wood chew",
    "moisture-meter-probes-in-chew-stick.jpg": "Moisture meter probes pressed into a coffee wood chew stick",
    "moisture-check-before-packing.jpg": "Moisture check on a chew stick at the packing table",
    "laser-engraving-a-coffee-wood-chew.jpg": "Laser engraving a logo onto a coffee wood chew",
    "staff-packing-chews-into-export-carton.jpg": "Two staff packing coffee wood chews into an export carton",
    "bagging-coffee-wood-chews-for-export.jpg": "Staff bagging coffee wood chews before they go into the carton",
    "vacuum-packs-layered-in-export-carton.jpg": "Vacuum packs of coffee wood chews layered inside an export carton",
    "polybagged-chews-layered-in-carton.jpg": "Polybagged coffee wood chews layered in a carton",
    "packing-vacuum-packs-into-export-carton.jpg": "Warehouse staff laying vacuum packs into an export carton",
    "palletised-export-cartons-with-size-labels.jpg": "Palletised export cartons marked with size and quantity labels",
    "grading-chews-at-the-packing-bench.jpg": "Staff grading coffee wood chews at the packing bench",
    "vacuum-pack-with-desiccant-sachet-in-carton.jpg": "Vacuum pack of chews with a desiccant sachet inside the carton",
    "silica-gel-sachet-inside-vacuum-pack.jpg": "Silica gel sachet sealed inside a vacuum pack of coffee wood chews",
    "checking-packs-inside-an-export-carton.jpg": "Checking the sealed packs inside an opened export carton",
    "grading-chew-sticks-by-hand.jpg": "Chew sticks graded by hand from a collection tray",
    "ho-chi-minh-city-warehouse-aisle.jpg": "Aisle of stacked export cartons in the Ho Chi Minh City warehouse",
    "stretch-wrapped-pallet-of-export-cartons.jpg": "Stretch-wrapped pallet of export cartons ready for dispatch",
    "forklift-moving-an-export-pallet.jpg": "Forklift moving a pallet of export cartons in the warehouse",
    "warehouse-stock-of-packed-cartons.jpg": "Packed cartons held as warehouse stock",
    "labelled-export-cartons-on-a-pallet.jpg": "Labelled export cartons stacked on a pallet",
    "inspector-checking-cartons-with-a-checklist.jpg": "Inspector checking cartons against a printed checklist",
    "measuring-a-carton-stack-during-inspection.jpg": "Carton stack being measured during inspection",
    "pre-shipment-inspection-at-the-container-door.jpg": "Pre-shipment inspection recorded at the container door",
    "loading-cartons-into-the-container.jpg": "Team loading cartons into a container at the warehouse",
    "forklift-loading-a-pallet-into-the-container.jpg": "Forklift placing a pallet of cartons into the container",
    "stacking-cartons-inside-the-container.jpg": "Worker stacking cartons inside the container",
    "container-loaded-with-export-cartons.jpg": "Container loaded with stacked export cartons",
    "team-stacking-cartons-in-the-container.jpg": "Loading team stacking cartons in the container",
    "checking-the-carton-wall-inside-a-container.jpg": "Checking the finished carton wall inside a loaded container",
    "warehouse-container-loading-bay.jpg": "Forklift working at the warehouse container loading bay",
    "applying-the-container-seal-before-departure.jpg": "Numbered seal applied to the container before departure",
    "sealed-container-leaving-the-warehouse.jpg": "Sealed container at the warehouse before it leaves for the port",
    "forklift-loading-a-container-for-export.jpg": "Forklift loading an export container at the warehouse",
}


CARTON = "Export master carton 51 × 31 × 39 cm as packed (0.062 m³), one carton size across the range; port of loading Cat Lai, Ho Chi Minh City. Pieces per carton depend on the size and pack configuration — see the packing table. Pallet configuration and cartons per container are calculated for the actual order rather than published."
COFFEE_PRODUCTION_LEAD = ("Where a size is not in stock and has to be produced, the published production ladder for plain goods is "
                          "8\u201310 days for 50\u2013200 pcs, 10\u201315 days for 200\u20131,000 pcs, 25\u201327 days for 1,000\u20135,000 pcs and 30\u201345 days for a full "
                          "20 ft container, before sampling and transit. Stock sizes do not wait for a production run.")
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


# Owner instruction 2026-11-20: publish our own factory, warehouse and export photos
# as capability evidence. Every file here is from the owner's photo folder.
def gallery(items, cols=3):
    """items: (filename, caption) using IMAGE_DESCRIPTIONS for alt text."""
    figs = "".join(
        figure("/assets/img/" + name, image_description(name, caption), caption)
        for name, caption in items)
    return f'<div class="grid grid-{cols}">' + figs + '</div>'

def video_figure(src, poster, caption, fallback):
    """Click-to-play WebM figure. preload=none keeps it off the critical path."""
    return ('<figure class="video-figure"><video controls preload="none" playsinline '
            f'poster="{poster}" width="480" height="854">'
            f'<source src="{src}" type="video/webm">{fallback}</video>'
            f'<figcaption>{caption}</figcaption></figure>')


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
ORDER_TIERS = ("Trial Box 100 pcs and Starting Box 500 pcs are the usual first steps above the 50 pcs per product "
               "minimum, which sizes can be mixed inside. Where a size is already packed in our warehouse it is picked "
               "from stock; anything else follows the production ladder above rather than a stock promise.")

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
    actions = f'<div class="hero-ctas"><a class="btn btn-primary" href="/request-a-quote/?{escape(query, quote=True)}">{"Request This Product Sample" if product else "Request Samples & Pricing"}</a><a class="btn btn-outline" href="/how-to-order/">How to Order</a></div>' if ctas else ""
    content = f'<div><p class="hero-eyebrow">{eyebrow}</p><h1>{title}</h1><p class="hero-lede">{lede}</p>{actions}</div>'
    visual = f'<img src="{image}" alt="{escape(image_description(image,title))}" loading="eager">' if image else ""
    if image and image.endswith("vietpaw-hemp-wood-assortment.jpg"):
        visual = '<figure>'+visual+'<figcaption>Sample assortment showing rope-ball and coffee wood combinations. Standalone balls and rope-only designs are quoted separately; the approved sample defines your order.</figcaption></figure>'
    return f'<section class="hero"><div class="wrap{" hero-inner" if image else ""}">{content}{visual}</div></section>'

def faq(items):
    return section("Buyer questions", "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in items))

def terms(moq=MOQ, wood=True):
    return table(["Order detail","Planning information"],[
        ("Product MOQ",moq),("Private label",PRIVATE_LABEL),
        ("Samples",SAMPLES+" "+SAMPLE_DISPATCH),("Production lead time",LEAD),
        ("Branding","Laser engraving on suitable coffee wood surfaces starts at 50 pcs and is charged separately. Custom development is quoted separately."),
        ("Packaging","Bulk bags, individual packs and paper or card boxes — ivory board or unbleached kraft, no plastic window or laminate. Print quantities for boxes, hang tags and labels are confirmed in the quote."),
        ("Export documents",EXPORT_DOCS if wood else EXPORT_DOCS_FIBER),
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
# Aligned 2026-11-20 with coffeewoodchew.com: the line runs S to XL, 8-16 cm long,
# 155 g to 1.1 kg. Dimensional tolerance and recommended dog weight are not published.
GORILLA_SIZES = [
    ("S","GRLS","5–6 × 8","155–230","60"),
    ("M","GRLM","6–8 × 10","260–350","52"),
    ("L","GRLL","8–10 × 12","350–480","52"),
    ("XL","GRLXL","10–12 × 15","550–1,100","On request"),
]
GORILLA = ("For strong chewers we make the <a href=\"/products/gorilla-coffee-wood-dog-chew/\">Gorilla line</a>: thick-cut coffee wood chews in four sizes, from GRLS "
           "(155–230 g) to GRLXL (550–900 g), with far more wood per piece than a standard stick of similar length.")

def gorilla_table():
    return spec_table(["Size","Reference SKU","Dimensions (cm)","Weight (g)","Pcs per carton"], GORILLA_SIZES,
        caption="Gorilla line — thick-cut coffee wood chews for strong chewers. Reference specification; coffee wood is a "
                "natural material and outline, grain and mass vary within each size. A dimensional tolerance and a recommended "
                "dog-weight band are not published for this line. Confirm the size with your sample.")
