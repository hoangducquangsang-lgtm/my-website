# -*- coding: utf-8 -*-
"""Product specifications grounded in our product sheets."""
from common import BASE_URL, BRAND
from content_helpers import (publish, section, p, ul, table, cards, terms, trust_links, SAFETY, MOISTURE,
                             answer, fit, steps, spec_table, figure, media, CARTON, SEA_TRANSIT,
                             INCOTERMS, PAYMENT, CAFFEINE, WEAR_BEHAVIOUR, SIZE_ADVICE, ORDER_TIERS,
                             GORILLA, gorilla_table)

COFFEE_SIZES = [
    ("XS","CC01XS","10","1.5–2.0","23–30","Up to 3 kg"),
    ("S","CC01S","13–14","2.0–2.5","35–45","3–5 kg"),
    ("M","CC01M","17–18","2.5–3.5","90–110","5–8 kg"),
    ("L","CC01L","19–20","3.5–4.5","120–180","8–12 kg"),
    ("XL","CC01XL","21–22","4.5–5.5","230–310","12–20 kg"),
    ("XXL","CC01XXL","22–23","5.5–7.0","340–440","20 kg and over"),
]
def coffee_size_table():
    return spec_table(
        ["Size","Reference SKU","Length (cm)","Diameter (cm)","Weight (g)","Reference dog weight","Pcs per export carton"],
        [(a,b,c,d,e,f,g) for (a,b,c,d,e,f),g in zip(COFFEE_SIZES,COFFEE_CARTON)],
        caption="Reference specification supplied for the VietPaw range. Coffee wood is a natural material: outline, grain and mass vary within each band. Dog weight is a starting reference for choosing a size, not a veterinary suitability assessment. Carton counts are for bulk-packed sticks; retail-packed and multi-piece sets fit fewer units per carton. Confirm the current size sheet, tolerances and carton data against your approved sample.")

COFFEE_CARTON = ["On request","512","224","126","85","On request"]

COFFEE_TOLERANCE = [
    ("Finished moisture","Below 14% before packing","Pin-type meter reading taken on the finished batch and again before the container is sealed. Ask for the reading filed against your lot."),
    ("Length tolerance","±3 mm on the stick line","Applies to the cut length. Diameter follows the natural stem and is controlled by grading into the bands above, not by machining."),
    ("Cracks","Any cracked piece is rejected at grading","Checked on the graded piece, not on a sampled average."),
    ("Reported reject rate","Roughly one piece in five across the whole process","Internally reported figure, concentrated at the seasoning-rack stage. It explains why lead time is driven by graded output rather than raw intake."),
    ("Quality checkpoints","Five, between raw stem and sealed carton","Intake, after seasoning, after shaping, at grading and at the packing bench."),
    ("Production capacity","100,000 pcs/month","Across our own three factories in Dak Lak, Gia Lai and Binh Duong. Volume and dates for your order are confirmed in the quotation."),
]

COFFEE_STEPS = [
    ("Choose the sizes, not the range",
     "Pick two or three sizes that match the dogs your customers actually own, using the reference weight column as a starting point.",
     "A short size list you can quote, photograph and reorder, instead of a six-size range that ties up stock.",
     "Buyers who launch with all six sizes usually find two of them carry most of the sell-through."),
    ("Approve a physical sample per size",
     "Request the sample, then measure length, diameter and weight yourself and keep one piece as the retained reference.",
     "An agreed physical standard that a later delivery can be checked against.",
     "Photographs show natural variation but are not a specification."),
    ("Fix the pack format before artwork",
     "Decide bulk bag, single poly bag, vacuum pack or retail box, and whether sticks ship singly or in sets.",
     "A carton count and a pack weight you can use for freight and marketplace listings.",
     "Pack format changes the pieces per carton, so artwork sized before this step usually has to be redone."),
    ("Agree the moisture and grading record",
     "Ask for the finished-batch moisture reading and confirm what counts as a rejectable crack or surface defect.",
     "A written acceptance standard attached to the order rather than an informal expectation.",
     None),
    ("Confirm documents and the sailing",
     "List the destination, Incoterm with named place, and the certificates your customs entry needs.",
     "A document set booked with the shipment instead of chased after arrival.",
     "Phytosanitary and fumigation certificates are issued per shipment; they cannot be produced retrospectively."),
]


PRODUCTS = {
"coffee-wood-dog-chew":dict(name="Coffee Wood Dog Chew Stick",material="Coffee wood",collection="coffee-wood",group="Coffee Wood",
 image="vietpaw-coffee-wood-sizes.png",size="XS–XXL; six reference sizes",moq="From 50 pcs per SKU on standard coffee wood sticks.",
 lede="Six graded sizes of seasoned Robusta coffee stem, packed below 14% moisture with a \u00b13 mm length tolerance. Full specification, carton data and the limits we will not claim \u2014 before you request a sample.",
 overview="The standard stick is described in our product sheet as coffee wood without added flavor, glue or color. This composition statement is not a laboratory safety certificate or a statement about every treatment used in export preparation. Rope combinations and other custom constructions need their own component list.",
 options=["Standard stick sizes XS–XXL; natural grain, outline and shade vary.","Laser-engraved brand mark on an agreed area of the wood, with placement approved on a sample.","Coffee wood combined with cotton or hemp rope is a separate construction; specify the rope material rather than describing the whole toy as single-ingredient."],
 checks=["Confirm size, diameter and weight bands against the approved reference sample.","Inspect edges, surface finish and visible cracks; agree unacceptable defects before production.",MOISTURE+" Agree drying, storage and packing requirements, including the measurement method and batch record."]),
"gorilla-coffee-wood-dog-chew":None,
"coconut-fiber-cat-ball":dict(name="Coconut Fiber Cat Ball",material="Coconut fiber",collection="coconut-fiber",group="Coconut Fiber",
 image="coconut-fiber-ball-top-view.jpg",size="Size and diameter selected by sample",moq="Request the current per-size minimum; selected standard lines start from 50 pcs.",
 lede="A textured coconut-husk fiber ball for supervised batting and chasing. Build a cat-focused assortment with sample-approved dimensions, secure construction and private-label tags.",
 overview="This product uses coconut husk fiber as its headline material. Confirm the full construction, including any core, binding thread, adhesive or decorative attachment, before approving composition and environmental claims. Cat and dog versions should not be treated as interchangeable just because a photo looks similar.",
 options=["Choose the diameter and finished weight for the cat range; no dog-size chart is reused here.","Approve winding, surface texture and any internal or binding components.","Use a branded tag or small paper box; define whether units are sold singly or as a set."],
 checks=["Check for loose strands and attachment security before packing.","Compare sample diameter, mass and construction across the order.","Reject musty or visibly contaminated units and define clean, dry storage conditions."]),
"coconut-fiber-dog-ball":dict(name="Coconut Fiber Dog Ball",material="Coconut fiber",collection="coconut-fiber",group="Coconut Fiber",
 image="coconut-fiber-ball-sizes-with-rope-toy.jpg",size="S: 4–6 cm; M: 6–8 cm; L: 8–10 cm (catalogue reference)",moq="Request MOQ by size and construction; selected standard lines start from 50 pcs.",
 lede="A natural-texture ball for supervised fetch and carry play. Quote the diameter, finished weight, fiber construction and packing format your dog-toy range needs.",
 overview="Coconut fiber offers a different texture from molded rubber or plastic. The approved sample should determine winding density, size and construction; the material name alone does not establish durability, bounce, buoyancy or suitability for power chewing.",
 options=["Specify S, M or L only together with measurable dimensions and an approved sample.","Choose individual, multi-pack or assortment presentation; quote each component of a mixed box.","Private-label tags and box artwork can carry your handling instructions and product identification."],
 checks=["Check diameter, mass, winding consistency and loose fiber against the agreed sample.","Confirm there are no unapproved changes to the core or binding materials.","Review labeling, carton count and moisture protection before shipment."]),
"hemp-fiber-ball":dict(name="Hemp Fiber Rope Ball",material="Hemp fiber",collection="hemp-fiber",group="Hemp Fiber",
 image="hemp-rope-balls-three-sizes.jpg",size="S: 4–5 cm; M: 6–7 cm; L: 8–9 cm (catalogue reference)",moq="Confirm MOQ by size; selected standard hemp products start from 50 pcs.",
 lede="A wound hemp-fiber ball for supervised interactive play. Compare three catalogue diameter bands and agree fiber composition, knot construction and packaging before ordering.",
 overview="Our supplied 2026 catalogue lists hemp balls in three sizes. A ball without a handle and a ball-with-rope are different products: identify the exact construction in the quote. Fiber identity, any blend and all binding components should be declared for the selected item.",
 options=["Catalogue reference diameters: S 4–5 cm, M 6–7 cm, L 8–9 cm; confirm current tolerances.","Choose the standalone ball or discuss a separately specified rope-handle version.","Use branded tags and paper packaging; do not laser-engrave loose fiber as though it were wood."],
 checks=["Compare diameter, finished weight, winding and knots with the approved sample.","Agree an appropriate pull/attachment check for the specific construction; request results if numerical strength is claimed.","Inspect for strand shedding and provide supervised-use instructions."]),
"loofah-cat-toy":dict(name="Loofah Cat Toy",material="Loofah",collection="loofah",group="Loofah",
 image="vietpaw-loofah-play-shapes.png",size="Dimensions confirmed per shape",moq="Quoted per shape; ask about small trial quantities and mixed-shape feasibility.",
 lede="Lightweight loofah-gourd fiber shaped for supervised cat play. Choose the shape, dimensions and attachments, then approve your sample and private-label packaging.",
 overview="Loofah is the fibrous interior of a dried gourd. Our product sheet describes cutting and shaping this material into play forms. Dimensions differ by design, so a fish, mouse or plain roll must each have a specification rather than a single universal size range.",
 options=["Request available shapes and a dimensioned sample for each chosen SKU.","Specify stitching, decorative parts and any filling as separate components.","Catnip inclusion is an optional development request, not standard contents; confirm source, amount and labeling for the target market."],
 checks=["Check surface cleanliness, dryness, shape consistency and seam or attachment security.","Agree the full component list before describing a finished toy as all-natural or plastic-free.","Match pack warnings to the selected species and construction; this cat page does not establish suitability for every small animal."]),
"hemp-rope-dog-toy":dict(name="Hemp Rope Dog Toy",material="Hemp fiber",collection="hemp-fiber",group="Hemp Fiber",
 image="hemp-rope-loop-ball-toy.jpg",size="Length, rope diameter and knot format quoted by design",moq="Project-specific; discuss a trial run and separate packaging minimum.",
 lede="Develop a knotted hemp rope or ball-with-rope toy for supervised tug play. Specify finished length, rope diameter, knot geometry and branding instead of ordering from appearance alone.",
 overview="Our product materials describe knotted hemp ropes and hemp ball-with-rope formats. This page covers those rope-based constructions, distinct from the standalone hemp ball. The image is a range reference; your approved physical sample defines the supplied design.",
 options=["Define overall length, strand or rope diameter, handle opening and knot count.","Choose an all-fiber format or a coffee wood combination with every component listed.","Discuss tag attachment, printed sleeves, assortment packs and custom design feasibility."],
 checks=["Agree knot security and an attachment/pull-check method relevant to the intended play.","Check for loose long strands and unintended loops or attachments.","Do not advertise a tensile rating, reinforcement or lifetime durability without design-specific evidence."]),
}


IMG = "/assets/img/"

def coffee_wood_sections(specifications):
    return [
    section("What a coffee wood dog chew actually is",
        answer("A coffee wood dog chew is a length of seasoned coffee-tree stem, cut to size, shaped and surface-finished into a chew. It is cut from the stem wood — not the bean, not the cherry — with no added flavouring, glue, coating, preservative or colouring. The piece your customer opens is one plant material and nothing else.")
        +p("The wood comes from mature Robusta coffee stems in Vietnam's Central Highlands — Dak Lak, Gia Lai and Dak Nong. Growers take out the trees that have stopped paying their way and leave the rest alone, so these stems are material that already existed and previously went to firewood. Nobody fells a coffee tree that is still yielding cherries. Because coffee is a crop and not a commercial timber species, it has no entry in standard timber databases, so there is no published Janka hardness or density figure for it. Anyone quoting one is estimating.")
        +p(CAFFEINE)
        +p("Density and grain vary from stem to stem, which is why the size bands below are graded rather than machined, and why two sticks of the same size will not weigh exactly the same. That variation is inherent to the material, not a defect.")
        +media(ul([
            "<strong>One material.</strong> No glue, coating, preservative or colouring in the standard stick.",
            "<strong>A by-product stream.</strong> Stems come from trees taken out at the end of their yielding life, not from clearing land for wood.",
            "<strong>Graded, not machined.</strong> Diameter follows the stem; sizes are sorted into bands.",
            "<strong>Not a food.</strong> It is a chew toy for supervised use, with no nutritional, dental or caffeine claim attached.",
        ]), IMG+"coffee-wood-chew-grain-detail.jpg",
        "Close-up of a finished coffee wood chew stick showing natural grain and surface finish",
        "Finished surface on a single stick. Grain, colour and outline vary between pieces of the same size.")),

    section("Specification",
        specifications+coffee_size_table()
        +"<h3>Gorilla line for strong chewers</h3>"+p(GORILLA)+gorilla_table()
        +"<h3>Measured limits and process figures</h3>"
        +spec_table(["Parameter","Figure","What it means in practice"],COFFEE_TOLERANCE,
            caption="Process figures reported by our production team for the coffee wood line. They describe how the line is run, not a guarantee for an individual piece. Ask for the records filed against your own lot.")
        +p(SIZE_ADVICE)
        +figure(IMG+"vietpaw-coffee-wood-sizes.png",
            "Six coffee wood chew sticks laid out from XS to XXL with size labels",
            "The six reference sizes side by side. Use the weight column in the table above as a starting point, then confirm the fit on a sample.")
        ,True),

    section("How the chew is made",
        p("Five checkpoints sit between a raw stem and a sealed carton. The sequence below is the part of the process we publish; drying temperatures, cycle times and the order of the drying stages are treated as proprietary and are not disclosed.")
        +steps([
            ("Intake and seasoning",
             "Stems arrive by trailer from scattered plots across a collection season and are held before processing — roughly a year, until green, flexible wood has become pale, light and hard.",
             "Stock that has already lost most of its free moisture before any cutting happens."),
            ("Cutting and shaping",
             "Stems are cross-cut to the length band, bark is removed and the surface is worked back.",
             "Pieces within the ±3 mm length tolerance, with the surface finish the sample was approved on."),
            ("Controlled drying",
             "Shaped pieces go onto racks for the drying stages.",
             "Finished moisture below 14%.",
             "Most rejections happen here, as pieces that were going to crack do so on the rack rather than in a carton."),
            ("Grading",
             "Pieces are sorted into diameter bands and any cracked piece is pulled out.",
             "Graded stock per size, with roughly one piece in five removed across the whole process."),
            ("Moisture check and packing",
             "A pin-type meter reading is taken and photographed for the batch, then pieces are bagged with a desiccant sachet and packed.",
             "A sealed carton with a moisture record attached to the lot.",
             "A second reading is taken before the container is sealed, because the container voyage — not our factory — is where most mould claims originate."),
        ])
        +'<div class="grid grid-3">'
        +figure(IMG+"coffee-wood-seasoning-racks.jpg","Rows of coffee wood sticks seasoning on factory drying racks","Drying racks. Pieces that will crack usually crack here.")
        +figure(IMG+"moisture-reading-before-packing.jpg","Pin-type moisture meter held against a coffee wood stick above a carton","Pin-type meter reading taken on the finished batch. Ask for the reading filed against your lot.")
        +figure(IMG+"grading-chews-before-packing.jpg","Hand holding a coffee wood stick above a crate of graded pieces","Grading. Any cracked piece is removed at this bench.")
        +"</div>"),

    section("Is it the right chew for this dog?",
        answer("Coffee wood suits moderate, persistent chewers that work at a chew rather than trying to crack it. For strong chewers, choose the thicker Gorilla line below rather than a standard stick.")
        +fit(
          ["Dogs that gnaw and shred rather than bite down hard, where a chew is expected to last weeks.",
           "Customers who want a single-material, plastic-free chew and will read a supervision instruction.",
           "Ranges that already sell rawhide alternatives and need something that does not soften or swell.",
           "Retailers who can stock two or three sizes and advise on sizing at the till."],
          ["The dog is a determined power chewer — use the Gorilla line instead of a standard stick.",
           "The dog has existing dental disease, is a senior, or is a puppy still changing teeth.",
           "The customer wants an edible or digestible chew; this is a toy and is not digestible.",
           "Nobody will be supervising, or the piece is small enough to be swallowed whole."])
        +p(WEAR_BEHAVIOUR)
        +p("There is also no evidence that the chew cleans teeth, prevents disease or is digestible, so we make none of those claims either.")
        +p(SAFETY),True),

    section("How to specify and order",
        steps(COFFEE_STEPS)
        +p(ORDER_TIERS)
        +p('Comparing it against what you already stock? See <a href="/guides/coffee-wood-vs-antler-nylon-rawhide/">coffee wood versus antler, nylon and rawhide</a>, <a href="/guides/coffee-wood-chew-size-guide/">how to size a chew to the dog</a> and <a href="/guides/how-long-do-coffee-wood-chews-last/">how long a chew actually lasts</a>.')),

    section("Branding and packaging",
        media(p("Laser engraving burns your mark into the wood surface. There is no ink, no label and nothing to peel off, which is why it survives a chew better than a printed sleeve. Engraving needs a reasonably flat area, so placement is approved on a sample per size rather than assumed.")
              +ul(["Engraving on suitable wood surfaces starts at 50 pcs and is separate from the packaging minimum.",
                   "Custom hang tags, printed labels and printed boxes start at 500 pcs per SKU.",
                   "Bulk bag, single poly bag, vacuum pack and paper or kraft box formats are all available.",
                   "Every pack carries a desiccant sachet; confirm the desiccant type in writing if your market restricts it."]),
              IMG+"laser-engraving-coffee-wood-chew.jpg",
              "Laser engraving head marking a brand logo onto a coffee wood chew stick",
              "Engraving is burned into the surface, so there is no label to peel away during chewing.")
        +p('Pricing for engraving and printed packaging is quoted with your order — we do not publish a per-piece figure here. See <a href="/services/private-label-pet-toys/">private label</a> for branding an approved design, or <a href="/services/oem-odm-pet-toy-manufacturing/">OEM/ODM</a> if the construction itself changes.'),True),

    section("Packing, cartons and shipping",
        p(CARTON)+p(SEA_TRANSIT)
        +spec_table(["Shipping detail","Reference"],[
            ("HS code","4421.99 — confirm the classification your own customs broker will use."),
            ("Master carton","51 × 31 × 39 cm, 0.062 m³"),
            ("Per pallet / 20 ft / 40 ft","30 cartons / 429 cartons / 850 cartons"),
            ("Port of loading","Cat Lai, Ho Chi Minh City"),
            ("Transit reference","30–35 days port to port, EU or US"),
            ("Incoterms",INCOTERMS),
            ("Payment",PAYMENT),
            ("Documents","Certificate of Origin, fumigation certificate, phytosanitary certificate, packing list, commercial invoice and bill of lading, subject to destination requirements. Batch moisture readings on request."),
        ], caption="Planning references. Carton counts assume bulk-packed sticks; confirm the figures for your own packed SKU before booking freight.")
        +p("<strong>The most common mistake in this category is moisture, and it happens at sea rather than at our factory.</strong> A sealed container cools overnight, water condenses on the steel and drips onto the top layers of cargo. Damage concentrated on the top layer and toward the doors points to condensation in transit; bloom spread evenly through the stack, including the middle and bottom, points to goods that were packed wet. Hanging desiccant in the container is inexpensive relative to a claim and is the single most useful addition for a monsoon-season sailing.")
        +media(ul(["Keep one sealed bag per lot and open it at month six — it tells you whether a later problem came from the shipment or from your own warehouse.",
                   "Store on pallets away from exterior walls and roller shutters, out of direct sun and away from metal-roofed structures.",
                   "Leave bags sealed until the goods go out, and finish an opened bag the same day.",
                   "Around 25–28 °C with air circulation is a workable warehouse target."]),
               IMG+"sealed-bag-pressed-into-export-carton.jpg",
               "Hand pressing a sealed bag of coffee wood chews into an export carton with a desiccant sachet",
               "Bagged and packed with a desiccant sachet. Most mould claims trace back to the voyage, not the bench.")),

    section("Order terms",terms("From 50 pcs per SKU on standard coffee wood sticks. Engraving, rope combinations and custom boxes are quoted separately.")
        +trust_links(),True),
    ]


COFFEE_FAQ = [
 ("Is coffee wood safe for dogs?",
  "It is safe in the sense that the standard stick is a single untreated plant material with no glue, coating, preservative or colouring, cut from stem wood rather than from the bean or cherry. It is not risk-free: any chew can break into pieces that should not be swallowed, and a strong chewer should have the thicker Gorilla line. Sell it with a supervision instruction and a replace-when-damaged instruction, and size it to the dog."),
 ("Does coffee wood splinter?",
  "It can. Neither we nor any other supplier in this category has published test data showing that it cannot, and an independent dog trainer has documented a stick that began breaking into hard pieces during use. We do not use the phrase \u201csplinter-free\u201d and we would advise you not to print it either. What the process does control is cracking: any cracked piece is removed at grading."),
 ("How long does one chew last?",
  "There is no published figure, because lifespan is set by the dog rather than by the material \u2014 a light gnawer may keep a size M stick for months while a determined chewer reduces the same piece in days. Size, moisture and how much time the dog actually spends with it all move the answer. Our guide on chew lifespan sets out what to tell customers instead of quoting a number."),
 ("Can coffee wood chews be private labelled?",
  "Yes, in two ways. Laser engraving burns your mark into the wood and starts at 50 pcs on suitable surfaces. Printed packaging \u2014 hang tags, labels, boxes \u2014 starts at 500 pcs per SKU. The two minimums are separate, so a small engraved trial run is possible before you commit to printed packaging."),
 ("What moisture level are the chews packed at, and how do I verify it?",
  "Below 14%, measured with a pin-type meter on the finished batch and photographed, then read again before the container is sealed. Ask for the reading filed against your lot number, and if the shipment matters, have a third party witness the moisture reading, measure a sample, photograph the carton marks and witness stuffing before the doors close."),
 ("How many pieces fit in a carton and a container?",
  "For bulk-packed sticks: 512 (S), 224 (M), 126 (L) and 85 (XL) per master carton of 51 \u00d7 31 \u00d7 39 cm. A carton is 0.062 m\u00b3, a pallet takes 30 cartons, a 20 ft container 429 and a 40 ft 850. Retail-packed and multi-piece sets fit noticeably fewer units per carton, so confirm the count for your own pack format before you cost the freight."),
 ("What documents come with the shipment?",
  "Certificate of Origin, fumigation certificate, phytosanitary certificate, packing list, commercial invoice and bill of lading, subject to what the destination requires. Batch moisture readings are available on request. Phytosanitary and fumigation certificates are issued per shipment and cannot be produced after the fact, so list them with the booking."),
 ("Coffee wood or olive wood \u2014 what is the practical difference?",
  "Olive wood has published timber data (roughly 980 kg/m\u00b3 dried, Janka around 2,710 lbf) because it is a commercial timber; coffee is a crop, so no equivalent figures exist. For an EU buyer the bigger difference is usually logistics: EU-sourced olive wood needs no customs entry, no duty and no phytosanitary certificate and can be reordered in small quantities, while coffee wood is a 30\u201335 day sea shipment with an import entry. Neither material can support digestibility or dental-benefit claims."),
]

from content_answers import PRODUCT_ANSWERS, PRODUCT_FAQS
from content_gorilla import GORILLA_ENTRY, gorilla_sections, GORILLA_FAQ
PRODUCTS["gorilla-coffee-wood-dog-chew"]=GORILLA_ENTRY

def product_cards(slugs):
    return cards([(PRODUCTS[s]["name"],
        PRODUCTS[s]["material"]+" · "+PRODUCTS[s]["size"]+". "+PRODUCTS[s]["moq"]+" Private-label options available.",
        "/products/"+s+"/","/assets/img/"+PRODUCTS[s]["image"]) for s in slugs])

def build(root):
    for slug,d in PRODUCTS.items():
        path="/products/"+slug+"/"
        image="/assets/img/"+d["image"]
        specifications=table(["Specification","Details"],[
            ("Manufacturer and exporter",BRAND),
            ("Material",d["material"]+"; confirm complete component list"),
            ("Sizes",d["size"]),("MOQ",d["moq"]),
            ("Branding","Laser engraving for suitable wood; labels, tags or boxes for fiber products."),
            ("Sample","Request a sample of this exact product and chosen packaging."),
            ("OEM / ODM","Custom construction is subject to feasibility, sample approval and separate quotation.")])
        gorilla = slug=="gorilla-coffee-wood-dog-chew"
        if gorilla:
            specifications=table(["Specification","Details"],[
                ("Manufacturer and exporter",BRAND),("Material","Coffee wood, untreated"),
                ("Sizes",d["size"]),("MOQ",d["moq"]),
                ("Branding","Laser engraving on the wood, or your own label, hang tag or printed box."),
                ("Sample","3 free samples; buyer covers courier."),
                ("Lead time","5–7 days stock packaging; 60–80 days with your own label, box or engraving.")])
            sections=gorilla_sections(specifications)
        elif slug=="coffee-wood-dog-chew":
            sections=coffee_wood_sections(specifications)
        else:
            sections=[
            section("Product overview",(answer(PRODUCT_ANSWERS[slug]) if slug in PRODUCT_ANSWERS else "")+p(d["overview"])),
            section("Product specifications",specifications,True),
            section("Sizes, formats and private-label options",ul(d["options"])+p('For branding an existing item, see <a href="/services/private-label-pet-toys/">private-label pet toys</a>. For structural changes, use our <a href="/services/oem-odm-pet-toy-manufacturing/">OEM/ODM development service</a>.')),
            section("Quality control and use instructions",ul(d["checks"])+p(SAFETY)+trust_links(),True),
            section("Packaging, samples and export planning",terms(d["moq"])+p("Natural-material products are not interchangeable with their packaging. Confirm the bag film, paper coating, inks, adhesive and desiccant separately, especially for a plastic-free retail brief.")),
            section("Recommended buyers and related products",p("Suitable sourcing conversations include pet brands, wholesalers and retailers building a sample-approved natural-material range. Marketplace acceptance and retail suitability remain specific to your listing and target market.")+
                p(f'<a href="/collections/{d["collection"]}/">Explore the {d["group"].lower()} wholesale collection</a> or <a href="/services/wholesale-pet-products/">plan a mixed-product wholesale order</a>.'),True)]
        schema={"@context":"https://schema.org","@type":"Product","@id":BASE_URL+path+"#product",
            "name":d["name"],"description":d["lede"],"url":BASE_URL+path,"image":BASE_URL+image,
            "material":d["material"],"brand":{"@id":BASE_URL+"/#brand","@type":"Brand","name":BRAND},
            "manufacturer":{"@id":BASE_URL+"/#organization","@type":"Organization","name":BRAND}}
        coffee = slug=="coffee-wood-dog-chew"
        publish(root,path,
            "Gorilla Coffee Wood Chew for Strong Chewers — Wholesale | VietPaw" if gorilla else
            "Coffee Wood Dog Chew — Sizes, Specification & Wholesale | VietPaw" if coffee
              else d["name"]+" | Wholesale & Private Label | VietPaw",
            ("Thick-cut coffee wood chews for strong chewers: GRLS–GRLXL, 155–900 g, carton data, FBA notes. From 50 pcs per SKU; private label from 500." if gorilla else
             "Six sizes XS–XXL with lengths, diameters, weights and carton counts. Packed below 14% moisture, ±3 mm length tolerance, five QC checkpoints. Wholesale and private label from Vietnam."
             if coffee else
             f'Source {d["name"].lower()} from Vietnam. Review sizes, sample options, private-label packaging and order requirements before requesting a quote.'),
            "Gorilla Coffee Wood Chew for Strong Chewers" if gorilla else "Coffee Wood Dog Chew Sticks" if coffee else d["name"]+" — Wholesale & Private Label",
            d["lede"],sections,image=image,product=d["name"],
            trail=[("Home","/"),(d["group"],"/collections/"+d["collection"]+"/"),(d["name"],None)],
            faqs=GORILLA_FAQ if gorilla else COFFEE_FAQ if slug=="coffee-wood-dog-chew" else [("Can I order this exact sample?", "Yes, request the product, size and packaging combination. Samples are free — up to 3 per request; you cover the courier. We confirm availability and the courier cost before dispatch."),
                  ("Are the photos and dimensions a binding specification?", "No. Photos show the range and natural variation. The agreed sample, drawing and purchase-order specification define the supplied product."),
                  ("Is private labeling available?", "Discuss the artwork, packaging and order quantity with us. New shapes, printed boxes and special finishes may have separate minimums and costs.")] + PRODUCT_FAQS.get(slug, []),
            schemas=[schema])
