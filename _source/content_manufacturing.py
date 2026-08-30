# -*- coding: utf-8 -*-
"""Distinct commercial intents: manufacturer, service routes, factory and QC."""
from content_helpers import publish, section, p, ul, table, cards, terms, trust_links, SOURCE_OEM, LEAD
from content_products import product_cards

def build(root):
    publish(root,"/pet-toys-manufacturer-vietnam/","Pet Toy Manufacturer Vietnam | OEM & Private Label | WINVN",
        "Evaluate WINVN as a natural pet toy manufacturing partner in Vietnam. Review material ranges, OEM/ODM, QC, factory information and sample ordering.",
        "Natural Pet Toy Manufacturer in Vietnam for B2B Brands",
        "Source coffee wood, coconut fiber, hemp and loofah pet toys with a Vietnam manufacturing partner. Evaluate the product, production route and documentation before committing your brand to a supplier.",
        [section("A Vietnam manufacturing brief, not just a product list",
            p("WINVN INT CO., LTD manufactures natural pet products in Vietnam for wholesale and private-label customers. Coffee wood sourcing is centered on the Central Highlands, with export coordination through Ho Chi Minh City. Our product range also includes coconut fiber, hemp fiber and loofah.")+
            p("For your order, confirm the actual production location, the approved product specification and the company named in the contract. A manufacturer description should lead to verifiable project details, not replace them.")),
         section("Natural materials we manufacture",cards([
            ("Coffee wood dog chews","Standard sticks and specification-led wood/rope combinations.","/collections/coffee-wood/"),
            ("Coconut fiber pet toys","Cat and dog ball constructions and other coir formats.","/collections/coconut-fiber/"),
            ("Hemp pet toys","Standalone balls, rope forms and mixed-material designs.","/collections/hemp-fiber/"),
            ("Loofah pet toys","Lightweight shapes with design-specific dimensions.","/collections/loofah/")],4),True),
         section("OEM, ODM and private-label manufacturing",p("A brand using an existing design needs artwork and pack approval. A buyer changing the construction needs a documented brief, prototype and feasibility review. Both need a final specification against which production can be checked.")+
            cards([("OEM / ODM","Develop to an agreed specification.","/services/oem-odm-pet-toy-manufacturing/"),
                   ("Private label","Brand an approved standard design.","/services/private-label-pet-toys/"),
                   ("Wholesale","Plan a standard or mixed-material order.","/services/wholesale-pet-products/")])),
         section("Factory and quality checks before purchase",ul([
            "Identify the current site making the chosen product, with an address and project contact.",
            "Request a walkthrough or inspection arrangement suitable for the order.",
            "Agree a physical reference sample, measurable dimensions and acceptable natural variation.",
            "Confirm the QC record, shipment-document list and responsibility for any outside testing."])+trust_links(),True),
         section("From sample to repeatable supply",p(LEAD)+p("Ask for a production slot based on SKU mix and packaging, not annual capacity alone. Freight time, testing, artwork changes and importer clearance are separate. A small initial run can help you evaluate receiving quality and sell-through before increasing volume.")+
            p('<a href="/how-to-order/">Review the order sequence</a> and <a href="/request-a-quote/">send a manufacturing enquiry</a>.'))],
        active="Manufacturing",image="/assets/img/process-raw-sticks.jpg",
        faqs=[("Do you serve international brands and importers?", "The offer is designed for wholesale buyers, pet brands, retailers and marketplace sellers. Quote the destination and product requirements for your order."),
              ("Where can I verify the factory?", "Use the factory page as an overview, then request current site details, a walkthrough and project-specific inspection arrangements."),
              ("What is the starting MOQ?", "Selected standard products start from 50 pcs per SKU. Custom constructions, dimensions and packaging minimums are confirmed separately.")])
    publish(root,"/services/oem-odm-pet-toy-manufacturing/","OEM & ODM Pet Toy Manufacturing in Vietnam | WINVN",
        "Develop custom natural pet toys with WINVN: specification review, prototypes, material selection, packaging and production approval in Vietnam.",
        "OEM & ODM Pet Toy Manufacturing",
        "Turn a drawing or product idea into an agreed manufacturing specification. Start with intended use, materials and dimensions, then work through prototype and production approval.",
        [section("OEM or ODM: define the scope first",table(["Route","Starting point","Approval focus"],[
            ("OEM","Your defined design/specification","Feasibility, tolerances and conformance to your brief"),
            ("ODM","A design developed or adapted with the manufacturer","Prototype, construction, ownership and final specification"),
            ("Private label","An existing approved design","Branding and packaging rather than structural development")])+
            p("These terms are used differently by suppliers. The written scope, deliverables and approvals matter more than the label.")),
         section("Natural-material development options",ul([
            "Coffee wood: stick dimensions, surface finish, engraving and wood/rope assemblies.",
            "Coconut fiber: ball dimensions, winding or other coir constructions.",
            "Hemp: rope geometry, knots, balls and connection details.",
            "Loofah: silhouette, dimensions, stitching and optional fillings."])+
            p(f'WINVN outlines design and packaging options on its <a href="{SOURCE_OEM}">OEM/ODM service page</a>. Material, construction, tooling, test and print requirements are quoted for the specific project.'),True),
         section("The development and approval sequence",ul([
            "<strong>Brief review:</strong> target pet, play context, destination, intended claims and indicative volume.",
            "<strong>Feasibility:</strong> material availability, workable dimensions, manufacturing method and cost drivers.",
            "<strong>Prototype:</strong> review form, finish, attachments and complete component list.",
            "<strong>Design approval:</strong> freeze drawings, reference sample, artwork and inspection criteria.",
            "<strong>Production release:</strong> confirm commercial terms, timing, quality records and change control."],True)),
         section("What to include in your OEM RFQ",table(["Input","Why it matters"],[
            ("Drawing / reference and dimensions","Makes the design and tolerance discussion concrete"),
            ("Target pet, use and market","Informs construction, instructions and the test brief"),
            ("Materials and excluded components","Prevents unexpected blends, cores or finishes"),
            ("Quantity per SKU and forecast","Separates development economics from reorder economics"),
            ("Packaging and barcode files","Defines printing, assembly and carton requirements"),
            ("Ownership / confidentiality expectations","Allows terms to be agreed before sharing sensitive design files")])+
            p("Design exclusivity, intellectual-property ownership and confidentiality are negotiated terms, not automatic benefits. Request an agreed process before sending sensitive files."),True),
         section("Timing and cost boundaries",terms("Custom designs are quoted by construction and order size. The 50-piece starting MOQ is not a universal custom-development minimum.")+trust_links())],
        active="Manufacturing",image="/assets/img/process-laser-engraving.jpg",
        faqs=[("Can you copy a competitor's design?", "Provide a design you are entitled to use and describe your functional needs. Ownership and permission must be resolved before development."),
              ("Can a new design be finished in seven days?", "Do not assume so. Standard sampling and custom prototyping are different stages; timing depends on complexity, revisions and testing."),
              ("Do I need a prototype for a repeat order?", "Use a version-controlled approved sample. Re-sampling may be needed when materials, construction or packaging change.")])
    publish(root,"/services/private-label-pet-toys/","Private Label Pet Toys | Natural Materials | WINVN",
        "Launch private-label coffee wood, coconut fiber, hemp and loofah pet toys. Review labels, engraving, packaging minimums and sample approval.",
        "Private-Label Pet Toys for Your Brand",
        "Put your identity on an existing natural-material design. Agree the product sample, labels, artwork and packaging before your first branded production run.",
        [section("Start with an existing product, then define the brand presentation",product_cards(["coffee-wood-dog-chew","hemp-fiber-ball","loofah-cat-toy"])+
            p("Private label is suited to buyers who want a branded range without beginning with a new product construction. A changed shape or assembly may move the brief into OEM/ODM development.")),
         section("Branding options by surface and pack",table(["Option","Typical application","What to approve"],[
            ("Laser engraving","Suitable coffee wood surfaces","Logo size, placement, contrast and effect on the surface"),
            ("Hang tag / label","Fiber toys and shaped products","Attachment, legibility, material and product identification"),
            ("Paper / kraft box","Single products or assortment sets","Dieline, print, fit, coating and pack dimensions"),
            ("Individual or bulk wrapping","Protection and handling","Bag specification, packing count and any required warning language")]),True),
         section("A pack brief that prevents avoidable revisions",ul([
            "Brand name, logo file, approved colors and contact information for the relevant market.",
            "Product name, complete material description, size and intended use.",
            "Supervision and replacement instructions appropriate to the product.",
            "Barcode artwork from the buyer and clear unit/set/carton identification.",
            "Any environmental or performance claim with evidence and scope."])+
            p("A natural-material toy in a plastic film is not a plastic-free pack. Confirm coatings, inks, glue and wrapping before approving final sustainability language.")),
         section("Minimums and commercial scope",p("Selected standard products can start from 50 pcs per SKU, but this does not mean every printing or packaging option has the same minimum. WINVN's service information describes custom box quantities around 200 pieces per design; the current specification and quote decide the applicable minimum.")+
            p("Ask the quote to distinguish product cost, engraving, label printing, box printing, artwork support, media and freight. Do not assume customization is free.")+
            p('<a href="/solutions/amazon-sellers/">Amazon preparation</a> · <a href="/solutions/eco-pet-shops/">Eco-retail packaging</a> · <a href="/solutions/startup-brands/">Startup launch planning</a>'),True),
         section("Approval and reorder control",ul([
            "Approve the unbranded product and size.",
            "Approve a branded physical sample and packaging proof.",
            "Record the approved artwork version and component list.",
            "Confirm quote, lead time, inspection and shipping requirements.",
            "Reorder against the same reference, with changes approved before production."],True)+trust_links())],
        active="Manufacturing",image="/assets/img/process-laser-engraving.jpg",
        faqs=[("Can I use my own logo?", "Yes. Engraving is for suitable wood surfaces; fiber toys usually use tags, labels or branded packaging."),
              ("Is private label the same as exclusivity?", "No. Brand presentation does not automatically make an existing product design exclusive. Discuss any exclusivity separately."),
              ("Can I start with a single SKU?", "Yes, discuss the standard-product minimum and the packaging minimum separately.")])
    publish(root,"/services/wholesale-pet-products/","Wholesale Natural Pet Products Supplier | WINVN",
        "Plan wholesale natural pet toy orders across coffee wood, coir, hemp and loofah. Confirm quantities per SKU, mixed cartons, pricing and reorder specifications.",
        "Wholesale Natural Pet Products for Focused Ranges",
        "Build an assortment across four core natural materials. We focus on pet toys and non-edible chew formats, with order terms confirmed per SKU and pack.",
        [section("Choose a range with a clear role for each item",cards([
            ("Dog toys","Chews, balls and interactive rope designs.","/dog-toys/"),
            ("Cat toys","Cat-specific balls and loofah play shapes.","/cat-toys/"),
            ("Material collections","Compare the four natural-material routes.","/materials/")])+
            p("Use one or two sample-approved products to establish the range, then add complementary designs where your retail data or distributor demand supports them. A broad catalogue is not a requirement to buy every format.")),
         section("A comparable wholesale quote",table(["Quote line","Confirm before purchase"],[
            ("Product and size","Reference SKU, dimensions, materials and tolerance"),
            ("Quantity","Minimum per SKU, size and packaging design"),
            ("Unit and packaging cost","What is included in each stated price"),
            ("Carton configuration","Units per pack/carton, carton size and gross weight"),
            ("Commercial basis","Currency, validity, payment and named-place Incoterm"),
            ("Additional services","Testing, inspection, artwork or other quoted costs"),
            ("Delivery plan","Production slot, transport mode and destination responsibilities")]),True),
         section("Mixed SKUs and volume planning",p("A mixed order combines approved line items; it does not erase each item's minimum. Confirm whether separate sizes or designs can share cartons and how retail units are identified. For a combo box, check that every item and the outer pack are specified.")+
            p("Volume pricing depends on product mix and packaging efficiency. Ask for relevant quantity breaks rather than assuming the same discount tiers for wood sticks, hand-shaped loofah and printed boxes.")+
            p('<a href="/solutions/wholesalers/">Distributor supply planning</a> and <a href="/solutions/retail-chains/">retail-chain preparation</a> address recurring orders and rollout needs.')),
         section("Samples and repeat orders",terms()+p("Keep an approved sample, artwork version and carton configuration for reorders. A production change should be reviewed before it becomes a receiving-quality problem.")+trust_links(),True)],
        active="Manufacturing",image="/assets/img/warehouse-winvn-boxes.jpg",
        faqs=[("Is there a universal wholesale price list?", "Request current pricing for the actual product, quantities and pack. Catalogue examples are not binding quotations."),
              ("Do you sell every type of pet product?", "This website focuses on coffee wood, coconut fiber, hemp and loofah pet toys, rather than an all-category pet-supply offer."),
              ("Can I order without my own branding?", "Discuss a standard wholesale configuration. Custom packaging and development are separate options.")])
    publish(root,"/factory/","Pet Toy Factory Vietnam | Process & Verification | WINVN",
        "Explore WINVN production in Vietnam, coffee wood processing and the factory information available for your natural pet toy order.",
        "Pet Toy Factory & Production in Vietnam",
        "Understand where and how your selected product is made. Use the supplier information below to prepare a current, product-specific factory review.",
        [section("Production locations and capacity: what the sources say",
            p("The supplied WINVN planning materials describe a three-factory network and indicative capacity of 5–6 million units per year. These are supplier-reported planning figures, not an audited measurement of current output or the capacity reserved for your order.")+
            p("Company sources describe Central Highlands production and sourcing, together with southern warehousing/export operations. Published location descriptions differ between documents and webpages. Confirm the exact site, current address and manufacturing role for your selected SKU before a visit or audit.")+
            p("Do not equate an office, warehouse, partner workshop and owned production facility. Ask which stages happen at each location and whether any work is subcontracted.")),
         section("Coffee wood process described in the supplied production sheet",ul([
            "Collect branches and trunks from coffee-growing areas.",
            "Clean raw material and carry out basic trimming.",
            "Dry before the next processing stages.",
            "Cut to the required size.",
            "Clean, smooth and finish the product.",
            "Check quality and pack the finished goods."],True)+
            p("The supplied production sheet labels the drying method as natural/sun drying and also refers to set temperature/humidity conditions. Ask the production team to confirm the current method, sequence and batch controls for your order; this page does not invent kiln parameters or cycle times."),True),
         section("Process and warehouse references",
            '<div class="grid grid-3"><figure><img src="/assets/img/process-raw-sticks.jpg" alt="Raw coffee wood preparation reference" loading="lazy"><figcaption>Raw material reference.</figcaption></figure><figure><img src="/assets/img/winvn-moisture-check-kiem-go-9.jpg" alt="Coffee wood moisture measurement reference" loading="lazy"><figcaption>Moisture-check reference.</figcaption></figure><figure><img src="/assets/img/warehouse-winvn-boxes.jpg" alt="Packed WINVN carton reference" loading="lazy"><figcaption>Packed-carton reference.</figcaption></figure></div>'+
            p("Images are from the supplied website asset library and show process/range references. They are not dated evidence of current capacity, equipment ownership or the status of a particular order.")),
         section("What to request in a factory verification pack",ul([
            "Current company registration and site details matching the proposed contract.",
            "A dated walkthrough identifying the product line and stages handled there.",
            "Production slot and capacity calculation for the actual SKU mix and pack.",
            "Quality checkpoints, measuring equipment and sample/lot identification.",
            "Subcontracting disclosure and arrangements for buyer or independent inspection.",
            "Authorized, appropriately redacted shipment examples where relevant."])+
            p('<a href="/quality-control/">Review the quality-control workflow</a> and <a href="/certifications/">document scope</a> before agreeing the inspection brief.'),True)],
        active="Manufacturing",image="/assets/img/process-raw-sticks.jpg",
        faqs=[("Is annual capacity a guaranteed order lead time?", "No. Capacity depends on the product mix, material availability, packing work and production schedule."),
              ("Can I arrange a factory visit?", "Request the current site address, contact, scope and appointment before traveling. Confirm whether a third-party inspection is needed.")])
    publish(root,"/quality-control/","Pet Toy Quality Control | Inspection Workflow | WINVN",
        "Review a five-stage QC workflow for natural pet toys: material intake, process, semi-finished, finished product and pre-shipment checks.",
        "Quality Control for Natural Pet Toy Orders",
        "Use an approved sample and agreed acceptance criteria to make quality measurable. The supplied WINVN service material describes five stages of inspection.",
        [section("Five inspection stages",table(["Stage","What to agree for your product","Record to request"],[
            ("1. Raw material","Material identity, cleanliness, visible defects and declared treatment","Intake record linked to material/lot"),
            ("2. In-process","Preparation, drying, cutting, winding or shaping against the process specification","Process check and deviation notes"),
            ("3. Semi-finished","Dimensions, assembly and consistency before final work","Intermediate measurements and correction record"),
            ("4. Final product","Finish, attachment security, sample match and packaging","Finished-product inspection results"),
            ("5. Pre-shipment","Order count, labels, cartons and shipment-document match","Release check and agreed shipment inspection")])+
            p("The checklist must be adapted to wood, coir, hemp or loofah. A stated workflow does not prove that a specific test has been performed on every unit.")),
         section("Material-specific checks",table(["Product","Priority checks"],[
            ("Coffee wood sticks","Dimension bands, visible cracks, edge finish and agreed moisture measurement"),
            ("Coir balls","Winding, diameter, loose fiber, core and binding components"),
            ("Hemp ropes/balls","Knots, strand shedding, dimensions and attachment/pull checks"),
            ("Loofah shapes","Dryness, seams, attachments, filling and shape consistency"),
            ("All retail packs","Artwork version, product identity, warnings, count and carton data")]),True),
         section("Moisture targets need a method and a record",
            p("WINVN's public material describes a 12–14% moisture target for wood. Treat it as a supplier process target to confirm for the selected product, not a universal pet-safety standard or a promise that mold and cracking cannot occur.")+
            p("Ask which meter/method is used, where readings are taken, how many units are checked, when measurements happen and how deviations are handled. Calibration status and a lot-linked record should be part of the discussion if moisture is a contractual acceptance criterion.")),
         section("Agree quality before the purchase order",ul([
            "Approved physical sample and current specification version.",
            "Measurable dimensions, material composition and acceptable natural variation.",
            "Defect definitions and agreed sampling/acceptance plan; no AQL level is assumed here.",
            "Any required independent lab test or third-party inspection, scoped separately.",
            "Hold/rework/rejection process and written receiving/claim terms."])+
            p("Do not use the phrase SGS-certified as a substitute for a report with a named product, method, date and scope. Inspection, laboratory testing and shipment documentation serve different purposes.")+
            p('<a href="/certifications/">Understand testing and export documents</a> or <a href="/services/oem-odm-pet-toy-manufacturing/">include QC in an OEM brief</a>.'),True)],
        active="Manufacturing",image="/assets/img/winvn-moisture-check-kiem-go-9.jpg")
