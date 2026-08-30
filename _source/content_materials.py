# -*- coding: utf-8 -*-
from content_helpers import publish, section, p, ul, table, terms, trust_links, SAFETY
from content_products import product_cards

MATERIALS = {
"coffee-wood":dict(
 title="Coffee Wood Dog Chew Manufacturer | Wholesale | WINVN",
 h1="Coffee Wood Dog Chews — Wholesale from Vietnam",
 lede="Build a coffee wood range with a Vietnam manufacturing partner: standard chew sticks, custom wood-and-rope constructions and private-label packaging for international buyers.",
 image="winvn-coffee-wood-single.jpg",products=["coffee-wood-dog-chew"],
 what="Coffee wood chews are shaped pieces of coffee-tree timber, not coffee beans or edible treats. WINVN's product information identifies mature coffee wood from Gia Lai and describes cutting, bark removal, surface finishing and drying.",
 applications=[("Standard sticks","Start with a focused size assortment using the CC01 reference specification. Each size is a separate ordering decision."),
 ("Wood-and-rope designs","Discuss cotton or hemp rope variants, component declarations and connection checks; they are not single-material sticks."),
 ("Branded retail range","Add laser engraving, size labels, safety instructions and a pack format suited to the sales channel.")],
 approval=["Request the current size sheet and physical sample; older charts use different weight bands.",
 "Confirm the drying target and measurement method. Ask for a batch-linked moisture record when it is part of your specification.",
 "Check wood surfaces and visible cracking, and agree the condition in which stock is packed and stored."],
 caution="Do not describe coffee wood as splinter-free, edible, caffeine-tested or proven to clean teeth without evidence for that exact claim. Hard wood can crack and can damage teeth; a natural origin is not a safety guarantee.",
 moq="From 50 pcs per SKU on standard sticks. Engraving, rope combinations and custom boxes are quoted separately."),
"coconut-fiber":dict(
 title="Coconut Fiber Pet Toys Manufacturer & Wholesale | WINVN",
 h1="Coconut Fiber Pet Toys for Wholesale & Private Label",
 lede="Source coconut-husk fiber balls and discuss rope constructions for a textured natural-material range. Separate cat and dog specifications, then approve winding, dimensions and packaging.",
 image="product-coconut-fiber-raw.jpg",products=["coconut-fiber-dog-ball","coconut-fiber-cat-ball"],
 what="Coconut fiber, also called coir, comes from the coconut husk. The supplied product material describes preparation, drying and shaping for pet-toy formats. A finished ball may have additional components that must be declared before a whole-product claim is made.",
 applications=[("Dog balls","Specify diameter, finished weight and the intended fetch/carry use; evaluate the actual sample."),
 ("Cat balls","Create a separate cat-range specification and check for detachable or loose components."),
 ("Rope and other coir products","Ask about current designs. Substrate and bedding are separate uses and are not assumed to have the same specification as toys.")],
 approval=["Ask how the fiber is prepared and dried, including any treatment that must be declared.",
 "Check binding, core construction, strand shedding and natural variation against the sample.",
 "Agree packing dryness and storage instructions; no universal moisture number is claimed for every coir design."],
 caution="Coir toys are not dietary fiber or a hairball treatment. Loose fiber and damaged pieces should not be encouraged for ingestion. Do not transfer a toy specification to animal bedding or substrate.",
 moq="Request MOQ per ball size or rope format. Selected standard products start from 50 pcs; mixed-product orders still need line-by-line confirmation."),
"hemp-fiber":dict(
 title="Hemp Pet Toy Manufacturer | Rope & Balls Wholesale | WINVN",
 h1="Hemp Fiber Pet Toys — Wholesale Rope & Ball Formats",
 lede="Develop a hemp-fiber assortment with standalone balls, knotted ropes and mixed-material designs. Match construction to supervised play and document the approved specification.",
 image="winvn-hemp-wood-assortment.jpg",products=["hemp-fiber-ball","hemp-rope-dog-toy"],
 what="Hemp fiber is a plant fiber used for wound balls and rope constructions in WINVN's product range. Catalogues identify ball diameter bands, while rope length and knot details are design-specific. Fiber identity and any blends need to be confirmed for the chosen product.",
 applications=[("Standalone balls","The catalogue lists S 4–5 cm, M 6–7 cm and L 8–9 cm diameter bands; confirm current dimensions."),
 ("Tug formats","Define rope length, diameter, handle opening and knot construction on the sample."),
 ("Coffee wood combinations","List wood, rope and any connector separately. Approve the connection rather than assuming a material's strength proves the whole toy.")],
 approval=["Confirm whether the rope is hemp, cotton, coir or a blend; the materials are not interchangeable.",
 "Specify the knot or attachment check and acceptance criteria; do not infer a tensile rating from appearance.",
 "Review fraying, loose strands and pack warnings for supervised use."],
 caution="The product is a fiber toy, not a CBD product, antimicrobial treatment or dental remedy. Avoid advertising comparative strength or breath-freshening effects without relevant product evidence.",
 moq="Selected standard hemp products start from 50 pcs. Custom rope geometry, mixed-material assemblies and branded boxes are quoted by project."),
"loofah":dict(
 title="Loofah Pet Toy Manufacturer | Cat Toys Wholesale | WINVN",
 h1="Loofah Pet Toys for Wholesale & Private Label",
 lede="Create a lightweight cat-toy range from dried loofah-gourd fiber. Choose shapes, define attachments and approve packaging for your own retail or marketplace brand.",
 image="winvn-loofah-growing.png",products=["loofah-cat-toy"],
 what="Loofah is the fibrous interior of a mature gourd, not a sea sponge. WINVN's supplied product sheet describes drying, cutting and shaping the fiber into toy forms. Shape, stitching and filling determine the finished specification.",
 applications=[("Cat play shapes","Discuss fish, mouse or other available shapes, with each design measured separately."),
 ("Brand-specific designs","Provide a drawing, target dimensions and attachment restrictions for an OEM/ODM feasibility review."),
 ("Catnip or other filling","Treat filling as an optional, separately specified component with its own source and labeling needs.")],
 approval=["Confirm the selected shape's dimensions rather than applying a single size range to the entire collection.",
 "Check cleanliness, dryness, seams and decorative parts against the approved sample.",
 "Confirm thread, filling, colors and labels before making composition or disposal claims."],
 caution="Loofah's plant origin does not prove that the entire toy or its packaging is compostable. It is not food, and suitability for cats does not automatically establish suitability for rabbits, hamsters or other species.",
 moq="MOQ is quoted per shape and construction. Ask about a trial assortment; do not assume a mixed carton automatically meets each SKU minimum."),
}

def build(root):
    for slug,d in MATERIALS.items():
        sections=[
            section("What this material is",p(d["what"])),
            section("Products and wholesale applications",product_cards(d["products"])+table(["Format","Buyer decision"],d["applications"]),True),
            section("From material sample to approved order",ul(d["approval"],True)+trust_links()),
            section("OEM, private label and range planning",p("Start with the sales channel, target pet, intended use and pack format. A standard product with your label follows a different approval path from a new shape or mixed-material construction.")+
                p('<a href="/services/private-label-pet-toys/">Private label</a> covers branding and packaging on approved designs. <a href="/services/oem-odm-pet-toy-manufacturing/">OEM/ODM</a> covers specification-led development. For a multi-material range, review <a href="/services/wholesale-pet-products/">wholesale ordering</a>.'),True),
            section("MOQ, samples, packaging and lead time",terms(d["moq"])),
            section("Claims, quality and safe-use boundaries",p(d["caution"])+p(SAFETY)+p('Review <a href="/sustainability/">material and packaging claim boundaries</a> before printing environmental language. Inspection records and third-party reports have different scopes.'),True)]
        publish(root,"/collections/"+slug+"/",d["title"],
            d["lede"],d["h1"],d["lede"],sections,active="Materials",image="/assets/img/"+d["image"],
            trail=[("Home","/"),("Materials","/materials/"),(d["h1"],None)],
            faqs=[("Can I order a mixed-material collection?", "Yes, discuss an assortment. Each SKU, size and packaging format needs a confirmed minimum, price and specification."),
                  ("Does natural material mean a certified finished product?", "No. Confirm every component and review the scope of any inspection or test report for the selected product."),
                  ("What should I send for a quote?", "Send product references, sizes, quantity per SKU, destination country and branding needs. Include your packaging and test requirements if known.")])
