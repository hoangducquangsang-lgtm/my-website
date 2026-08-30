# -*- coding: utf-8 -*-
"""Product specifications grounded in the supplied WINVN product sheets."""
from common import BASE_URL, BRAND, LEGAL_NAME
from content_helpers import publish, section, p, ul, table, cards, terms, trust_links, SAFETY

COFFEE_SIZES = [
    ("XS","CC01-XS","10","1.5–2.0","23–30","Under 5 kg"),
    ("S","CC01-S","13–14","2.0–2.5","35–45","5–10 kg"),
    ("M","CC01-M","17–18","2.5–3.5","90–110","10–20 kg"),
    ("L","CC01-L","19–20","3.5–4.5","110–150","20–30 kg"),
    ("XL","CC01-XL","21–22","4.5–5.5","150–225","30–40 kg"),
    ("XXL","CC01-XXL","22–23","5.5–7.0","325–450","Over 40 kg"),
]
def coffee_size_table():
    return table(["Size","Reference SKU","Length (cm)","Diameter (cm)","Weight (g)","Reference dog weight"],COFFEE_SIZES)+p("Reference: WINVN coffee wood product specification supplied for this website. Natural shape and weight vary; confirm the current size sheet and agreed tolerances with your sample. Dog weight is a starting reference, not a veterinary suitability assessment. Older charts use different weight bands; do not combine them.")

PRODUCTS = {
"coffee-wood-dog-chew":dict(name="Coffee Wood Dog Chew Stick",material="Coffee wood",collection="coffee-wood",group="Coffee Wood",
 image="winvn-coffee-wood-sizes.png",size="XS–XXL; six reference sizes",moq="From 50 pcs per SKU on standard coffee wood sticks.",
 lede="Source a coffee wood chew stick cut, shaped, dried and surface-finished in Vietnam. Compare six reference sizes, agree the finished sample, and add laser engraving or your own packaging.",
 overview="The standard stick is described in the WINVN product sheet as coffee wood without added flavor, glue or color. This composition statement is not a laboratory safety certificate or a statement about every treatment used in export preparation. Rope combinations and other custom constructions need their own component list.",
 options=["Standard stick sizes XS–XXL; natural grain, outline and shade vary.","Laser-engraved brand mark on an agreed area of the wood, with placement approved on a sample.","Coffee wood combined with cotton or hemp rope is a separate construction; specify the rope material rather than describing the whole toy as single-ingredient."],
 checks=["Confirm size, diameter and weight bands against the approved reference sample.","Inspect edges, surface finish and visible cracks; agree unacceptable defects before production.","Agree drying, storage and packing requirements. The supplier describes a 12–14% wood moisture target; request the method and batch record rather than treating it as a guarantee."]),
"coconut-fiber-cat-ball":dict(name="Coconut Fiber Cat Ball",material="Coconut fiber",collection="coconut-fiber",group="Coconut Fiber",
 image="winvn-coconut-fiber-balls.jpg",size="Size and diameter selected by sample",moq="Request the current per-size minimum; selected standard lines start from 50 pcs.",
 lede="A textured coconut-husk fiber ball for supervised batting and chasing. Build a cat-focused assortment with sample-approved dimensions, secure construction and private-label tags.",
 overview="This product uses coconut husk fiber as its headline material. Confirm the full construction, including any core, binding thread, adhesive or decorative attachment, before approving composition and environmental claims. Cat and dog versions should not be treated as interchangeable just because a photo looks similar.",
 options=["Choose the diameter and finished weight for the cat range; no dog-size chart is reused here.","Approve winding, surface texture and any internal or binding components.","Use a branded tag or small paper box; define whether units are sold singly or as a set."],
 checks=["Check for loose strands and attachment security before packing.","Compare sample diameter, mass and construction across the order.","Reject musty or visibly contaminated units and define clean, dry storage conditions."]),
"coconut-fiber-dog-ball":dict(name="Coconut Fiber Dog Ball",material="Coconut fiber",collection="coconut-fiber",group="Coconut Fiber",
 image="dog-coconut-balls-lifestyle.jpg",size="S / M / L references; confirm diameter",moq="Request MOQ by size and construction; selected standard lines start from 50 pcs.",
 lede="A natural-texture ball for supervised fetch and carry play. Quote the diameter, finished weight, fiber construction and packing format your dog-toy range needs.",
 overview="Coconut fiber offers a different texture from molded rubber or plastic. The approved sample should determine winding density, size and construction; the material name alone does not establish durability, bounce, buoyancy or suitability for power chewing.",
 options=["Specify S, M or L only together with measurable dimensions and an approved sample.","Choose individual, multi-pack or assortment presentation; quote each component of a mixed box.","Private-label tags and box artwork can carry your handling instructions and product identification."],
 checks=["Check diameter, mass, winding consistency and loose fiber against the agreed sample.","Confirm there are no unapproved changes to the core or binding materials.","Review labeling, carton count and moisture protection before shipment."]),
"hemp-fiber-ball":dict(name="Hemp Fiber Rope Ball",material="Hemp fiber",collection="hemp-fiber",group="Hemp Fiber",
 image="winvn-hemp-wood-assortment.jpg",size="S: 4–5 cm; M: 6–7 cm; L: 8–9 cm (catalogue reference)",moq="Confirm MOQ by size; selected standard hemp products start from 50 pcs.",
 lede="A wound hemp-fiber ball for supervised interactive play. Compare three catalogue diameter bands and agree fiber composition, knot construction and packaging before ordering.",
 overview="The 2026 WINVN catalogue lists hemp balls in three sizes. A ball without a handle and a ball-with-rope are different products: identify the exact construction in the quote. Fiber identity, any blend and all binding components should be declared for the selected item.",
 options=["Catalogue reference diameters: S 4–5 cm, M 6–7 cm, L 8–9 cm; confirm current tolerances.","Choose the standalone ball or discuss a separately specified rope-handle version.","Use branded tags and paper packaging; do not laser-engrave loose fiber as though it were wood."],
 checks=["Compare diameter, finished weight, winding and knots with the approved sample.","Agree an appropriate pull/attachment check for the specific construction; request results if numerical strength is claimed.","Inspect for strand shedding and provide supervised-use instructions."]),
"loofah-cat-toy":dict(name="Loofah Cat Toy",material="Loofah",collection="loofah",group="Loofah",
 image="winvn-loofah-play-shapes.png",size="Dimensions confirmed per shape",moq="Quoted per shape; ask about small trial quantities and mixed-shape feasibility.",
 lede="Lightweight loofah-gourd fiber shaped for supervised cat play. Choose the shape, dimensions and attachments, then approve your sample and private-label packaging.",
 overview="Loofah is the fibrous interior of a dried gourd. WINVN's product sheet describes cutting and shaping this material into play forms. Dimensions differ by design, so a fish, mouse or plain roll must each have a specification rather than a single universal size range.",
 options=["Request available shapes and a dimensioned sample for each chosen SKU.","Specify stitching, decorative parts and any filling as separate components.","Catnip inclusion is an optional development request, not standard contents; confirm source, amount and labeling for the target market."],
 checks=["Check surface cleanliness, dryness, shape consistency and seam or attachment security.","Agree the full component list before describing a finished toy as all-natural or plastic-free.","Match pack warnings to the selected species and construction; this cat page does not establish suitability for every small animal."]),
"hemp-rope-dog-toy":dict(name="Hemp Rope Dog Toy",material="Hemp fiber",collection="hemp-fiber",group="Hemp Fiber",
 image="winvn-hemp-wood-assortment.jpg",size="Length, rope diameter and knot format quoted by design",moq="Project-specific; discuss a trial run and separate packaging minimum.",
 lede="Develop a knotted hemp rope or ball-with-rope toy for supervised tug play. Specify finished length, rope diameter, knot geometry and branding instead of ordering from appearance alone.",
 overview="WINVN's supplied product materials describe knotted hemp ropes and hemp ball-with-rope formats. This page covers those rope-based constructions, distinct from the standalone hemp ball. The image is a range reference; your approved physical sample defines the supplied design.",
 options=["Define overall length, strand or rope diameter, handle opening and knot count.","Choose an all-fiber format or a coffee wood combination with every component listed.","Discuss tag attachment, printed sleeves, assortment packs and custom design feasibility."],
 checks=["Agree knot security and an attachment/pull-check method relevant to the intended play.","Check for loose long strands and unintended loops or attachments.","Do not advertise a tensile rating, reinforcement or lifetime durability without design-specific evidence."]),
}

def product_cards(slugs):
    return cards([(PRODUCTS[s]["name"],
        PRODUCTS[s]["material"]+" · "+PRODUCTS[s]["size"]+". "+PRODUCTS[s]["moq"]+" Private-label options available.",
        "/products/"+s+"/","/assets/img/"+PRODUCTS[s]["image"]) for s in slugs])

def build(root):
    for slug,d in PRODUCTS.items():
        path="/products/"+slug+"/"
        image="/assets/img/"+d["image"]
        specifications=table(["Specification","Details"],[
            ("Material",d["material"]+"; confirm complete component list"),
            ("Sizes",d["size"]),("MOQ",d["moq"]),
            ("Branding","Laser engraving for suitable wood; labels, tags or boxes for fiber products."),
            ("Sample","Request a sample of this exact product and chosen packaging."),
            ("OEM / ODM","Custom construction is subject to feasibility, sample approval and separate quotation.")])
        sections=[
            section("Product overview",p(d["overview"])),
            section("Product specifications",specifications+(coffee_size_table() if slug=="coffee-wood-dog-chew" else ""),True),
            section("Sizes, formats and private-label options",ul(d["options"])+p('For branding an existing item, see <a href="/services/private-label-pet-toys/">private-label pet toys</a>. For structural changes, use our <a href="/services/oem-odm-pet-toy-manufacturing/">OEM/ODM development service</a>.')),
            section("Quality control and use instructions",ul(d["checks"])+p(SAFETY)+trust_links(),True),
            section("Packaging, samples and export planning",terms(d["moq"])+p("Natural-material products are not interchangeable with their packaging. Confirm the bag film, paper coating, inks, adhesive and desiccant separately, especially for a plastic-free retail brief.")),
            section("Recommended buyers and related products",p("Suitable sourcing conversations include pet brands, wholesalers and retailers building a sample-approved natural-material range. Marketplace acceptance and retail suitability remain specific to your listing and target market.")+
                p(f'<a href="/collections/{d["collection"]}/">Explore the {d["group"].lower()} wholesale collection</a> or <a href="/services/wholesale-pet-products/">plan a mixed-product wholesale order</a>.'),True)]
        schema={"@context":"https://schema.org","@type":"Product","@id":BASE_URL+path+"#product",
            "name":d["name"],"description":d["lede"],"url":BASE_URL+path,"image":BASE_URL+image,
            "material":d["material"],"brand":{"@type":"Brand","name":BRAND},
            "manufacturer":{"@type":"Organization","name":LEGAL_NAME}}
        publish(root,path,d["name"]+" | Wholesale & Private Label | WINVN",
            f'Source {d["name"].lower()} from Vietnam. Review sizes, sample options, private-label packaging and order requirements before requesting a quote.',
            d["name"]+" — Wholesale & Private Label",d["lede"],sections,image=image,product=d["name"],
            trail=[("Home","/"),(d["group"],"/collections/"+d["collection"]+"/"),(d["name"],None)],
            faqs=[("Can I order this exact sample?", "Yes, request the product, size and packaging combination. We confirm availability, any sample charge and courier cost before dispatch."),
                  ("Are the photos and dimensions a binding specification?", "No. Photos show the range and natural variation. The agreed sample, drawing and purchase-order specification define the supplied product."),
                  ("Is private labeling available?", "Discuss the artwork, packaging and order quantity with us. New shapes, printed boxes and special finishes may have separate minimums and costs.")],
            schemas=[schema])
