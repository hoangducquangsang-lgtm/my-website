# -*- coding: utf-8 -*-
"""Distinct commercial intents: manufacturer, service routes, factory and QC."""
from content_helpers import publish, section, p, ul, table, cards, terms, trust_links, gallery, MOULD_COMMITMENT, SOURCE_OEM, LEAD, PRIVATE_LABEL, SAMPLES, SAMPLE_DISPATCH, QC_PROTOCOL, MOISTURE, RANGE_SCOPE
from content_products import product_cards
from common import SITES

def build(root):
    publish(root,"/pet-toys-manufacturer-vietnam/","Pet Toy Manufacturer Vietnam | OEM & Private Label | VietPaw",
        "Source natural pet toys through VietPaw. Review Vietnam production, OEM/ODM, quality control, samples and order-specific manufacturing information.",
        "Natural Pet Toy Manufacturer in Vietnam for B2B Brands",
        "Source coffee wood, coconut fiber, hemp and loofah pet toys through VietPaw with product specifications, production checks and order-specific documentation.",
        [section("A Vietnam manufacturing brief, not just a product list",
            p("Coffee wood is produced at our two factories in Dak Lak and Gia Lai. The wood is collected in the Central Highlands; packing, quality release and export dispatch run from our Ho Chi Minh City warehouse. Our range covers coffee wood, coconut fiber, hemp fiber and loofah.")+
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
         section("What the work looks like",
            p("Coffee wood is produced at our two factories in Dak Lak and Gia Lai; goods are shipped from our warehouse in Ho Chi Minh City. These are our own photos of that run.")+
            gallery([
              ("coffee-stems-on-trailer-central-highlands.jpg","Stems collected in the Central Highlands."),
              ("coffee-wood-chews-on-drying-racks.jpg","Shaped chews on the drying racks."),
              ("moisture-meter-reading-on-coffee-wood-chew.jpg","Batch moisture read before packing."),
              ("staff-packing-chews-into-export-carton.jpg","Packing into export cartons."),
              ("ho-chi-minh-city-warehouse-aisle.jpg","Stock in the Ho Chi Minh City warehouse."),
              ("sealed-container-leaving-the-warehouse.jpg","Sealed container on its way to Cat Lai port."),
            ]),True),
         section("From sample to repeatable supply",p(LEAD)+p("Ask for a production slot based on SKU mix and packaging, not annual capacity alone. Freight time, testing, artwork changes and importer clearance are separate. A small initial run can help you evaluate receiving quality and sell-through before increasing volume.")+
            p('<a href="/how-to-order/">Review the order sequence</a> and <a href="/request-a-quote/">send a manufacturing enquiry</a>.'))],
        active="Manufacturing",image="/assets/img/process-raw-sticks.jpg",
        faqs=[("Do you serve international brands and importers?", "The offer is designed for wholesale buyers, pet brands, retailers and marketplace sellers. Quote the destination and product requirements for your order."),
              ("Where can I verify our factory?", "Use our factory page as an overview, then request current site details, a walkthrough and project-specific inspection arrangements."),
              ("What is the starting MOQ?", "Selected standard products start from 50 pcs per product. Custom constructions, dimensions and packaging minimums are confirmed separately.")])
    publish(root,"/services/oem-odm-pet-toy-manufacturing/","OEM & ODM Pet Toy Manufacturing in Vietnam | VietPaw",
        "Develop custom natural pet toys with VietPaw: specification review, prototypes, material selection, packaging and production approval in Vietnam.",
        "OEM & ODM Pet Toy Manufacturing",
        "Turn a drawing or product idea into an agreed manufacturing specification. Start with intended use, materials and dimensions, then work through prototype and production approval.",
        [section("OEM or ODM: define the scope first",table(["Route","Starting point","Approval focus"],[
            ("OEM","Your defined design/specification","Feasibility, tolerances and conformance to your brief"),
            ("ODM","A design developed or adapted with our production team","Prototype, construction, ownership and final specification"),
            ("Private label","An existing approved design","Branding and packaging rather than structural development")])+
            p("These terms are used differently by suppliers. The written scope, deliverables and approvals matter more than the label.")),
         section("Natural-material development options",ul([
            "Coffee wood: stick dimensions, surface finish, engraving and wood/rope assemblies.",
            "Coconut fiber: ball dimensions, winding or other coir constructions.",
            "Hemp: rope geometry, knots, balls and connection details.",
            "Loofah: silhouette, dimensions, stitching and optional fillings."])+
            p(f'We develop designs and packaging at our own two factories — see our <a href="{SOURCE_OEM}">manufacturing and order information</a>. Material, construction, tooling, test and print requirements are quoted for the specific project.'),True),
         section("The development and approval sequence",ul([
            "<strong>Brief review:</strong> target pet, play context, destination, intended claims and indicative volume.",
            "<strong>Feasibility:</strong> material availability, workable dimensions, manufacturing method and cost drivers.",
            "<strong>Prototype:</strong> review form, finish, attachments and complete component list.",
            "<strong>Design approval:</strong> freeze drawings, reference sample, artwork and inspection criteria.",
            "<strong>Production release:</strong> confirm commercial terms, timing, quality records and change control."],True)),
         section("Where development work happens",
            gallery([
              ("grading-chews-at-the-packing-bench.jpg","Sample grading at the bench."),
              ("laser-engraving-a-coffee-wood-chew.jpg","Engraving trials on the actual material."),
              ("cut-coffee-wood-billets.jpg","Billets the construction is cut from."),
            ]),True),
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
    publish(root,"/services/private-label-pet-toys/","Private Label Pet Toys | Natural Materials | VietPaw",
        "Private-label pet toys from the same 50 pcs minimum, with custom hang tags and printed boxes quoted on their print quantity. Coffee wood laser engraving is available separately from 50 pcs.",
        "Private-Label Pet Toys for Your Brand",
        "Put your identity on an existing natural-material design, with an own-label product carrying the same 50 pcs minimum. Agree the product sample, labels, artwork and packaging before production.",
        [section("Start with an existing product, then define the brand presentation",product_cards(["coffee-wood-dog-chew","hemp-fiber-ball","loofah-cat-toy"])+
            p("Private label is suited to buyers who want a branded range without beginning with a new product construction. A changed shape or assembly may move the brief into OEM/ODM development.")),
         section("Branding options by surface and pack",table(["Option","Typical application","What to approve"],[
            ("Laser engraving — from 50 pcs","Suitable coffee wood surfaces","Logo size, placement, contrast and effect on the surface"),
            ("Custom hang tag / label — print quantity quoted","Fiber toys and shaped products","Attachment, legibility, material and product identification"),
            ("Custom printed box — print quantity quoted","Single products or assortment sets","Dieline, print, fit, coating and pack dimensions"),
            ("Individual or bulk wrapping","Protection and handling","Bag specification, packing count and any required warning language")]),True),
         section("A pack brief that prevents avoidable revisions",ul([
            "Brand name, logo file, approved colors and contact information for the relevant market.",
            "Product name, complete material description, size and intended use.",
            "Supervision and replacement instructions appropriate to the product.",
            "Barcode artwork from the buyer and clear unit/set/carton identification.",
            "Any environmental or performance claim with evidence and scope."])+
            p("A natural-material toy in a plastic film is not a plastic-free pack. Confirm coatings, inks, glue and wrapping before approving final sustainability language.")),
         section("Minimums and commercial scope",p(PRIVATE_LABEL)+
            p("Selected standard products and laser engraving on suitable coffee wood surfaces start at 50 pcs. Engraving alone is a separate option; it does not lower the minimum for a private-label run with custom printed packaging.")+
            p(SAMPLES+" "+SAMPLE_DISPATCH)+p(LEAD)+
            p("Ask the quote to distinguish product cost, engraving, label printing, box printing, artwork support, media and freight. Do not assume customization is free.")+
            p('<a href="/solutions/amazon-sellers/">Amazon preparation</a> · <a href="/solutions/eco-pet-shops/">Eco-retail packaging</a> · <a href="/solutions/startup-brands/">Startup launch planning</a>'),True),
         section("Branding and packing, photographed",
            gallery([
              ("laser-engraving-a-coffee-wood-chew.jpg","Laser engraving on a coffee wood chew."),
              ("bagging-coffee-wood-chews-for-export.jpg","Bagging ahead of your own pack."),
              ("vacuum-packs-layered-in-export-carton.jpg","Packs layered into the export carton."),
            ]),True),
         section("Approval and reorder control",ul([
            "Approve the unbranded product and size.",
            "Approve a branded physical sample and packaging proof.",
            "Record the approved artwork version and component list.",
            "Confirm quote, lead time, inspection and shipping requirements.",
            "Reorder against the same reference, with changes approved before production."],True)+trust_links())],
        active="Manufacturing",image="/assets/img/process-laser-engraving.jpg",
        faqs=[("Can I use my own logo?", "Yes. Engraving is for suitable wood surfaces; fiber toys usually use tags, labels or branded packaging."),
              ("Is private label the same as exclusivity?", "No. Brand presentation does not automatically make an existing product design exclusive. Discuss any exclusivity separately."),
              ("Can I start with a single SKU?", "Yes. An own-label product carries the same 50 pcs minimum; confirm the print quantity for your chosen SKU and artwork. Standard products or engraving alone may start at 50 pcs.")])
    publish(root,"/services/wholesale-pet-products/","Wholesale Natural Pet Products Supplier | VietPaw",
        "Plan wholesale natural pet toy orders across coffee wood, coir, hemp and loofah. Confirm quantities per SKU, mixed cartons, pricing and reorder specifications.",
        "Wholesale Natural Pet Products for Focused Ranges",
        "Build an assortment across four core natural materials. We focus on pet toys and non-edible chew formats, with order terms confirmed per SKU and pack.",
        [section("Choose a range with a clear role for each item",cards([
            ("Dog toys","Chews, balls and interactive rope designs.","/dog-toys/"),
            ("Cat toys","Cat-specific balls and loofah play shapes.","/cat-toys/"),
            ("Material collections","Compare the four natural-material routes.","/materials/")])+
            p("Use one or two sample-approved products to establish the range, then add complementary designs where your retail data or distributor demand supports them. A broad catalogue is not a requirement to buy every format.")+p(RANGE_SCOPE)),
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
         section("Stock, picking and dispatch",
            p("Standard sizes that are already packed are picked from our Ho Chi Minh City warehouse; anything else follows the published production ladder, 8\u201310 days for 50\u2013200 pcs up to 30\u201345 days for a full 20 ft container.")+
            gallery([
              ("warehouse-stock-of-packed-cartons.jpg","Packed cartons held as stock."),
              ("forklift-moving-an-export-pallet.jpg","Picking a pallet for dispatch."),
              ("labelled-export-cartons-on-a-pallet.jpg","Cartons labelled by size and quantity."),
              ("stretch-wrapped-pallet-of-export-cartons.jpg","Wrapped and staged for collection."),
              ("forklift-loading-a-pallet-into-the-container.jpg","Loading into the container."),
              ("container-loaded-with-export-cartons.jpg","A loaded container before the doors close."),
            ])),
         section("Samples and repeat orders",terms()+p("Keep an approved sample, artwork version and carton configuration for reorders. A production change should be reviewed before it becomes a receiving-quality problem.")+trust_links(),True)],
        active="Manufacturing",image="/assets/img/pallet-stack-inspection.jpg",
        faqs=[("Is there a universal wholesale price list?", "Request current pricing for the actual product, quantities and pack. Catalogue examples are not binding quotations."),
              ("Do you sell every type of pet product?", "This website focuses on coffee wood, coconut fiber, hemp and loofah pet toys, rather than an all-category pet-supply offer."),
              ("Can I order without my own branding?", "Discuss a standard wholesale configuration. Custom packaging and development are separate options.")])
    publish(root,"/factory/","Pet Toy Factory Vietnam | Process & Verification | VietPaw",
        "Coffee wood is produced at VietPaw’s two factories in Dak Lak and Gia Lai, Vietnam, and goods ship from our Ho Chi Minh City warehouse. Process, quality control and export documents.",
        "Our Two Factories in Vietnam",
        "Coffee wood is produced at our two factories in Dak Lak and Gia Lai; goods are shipped from our warehouse in Ho Chi Minh City.",
        [section("Two factories, one specification",
            p("Coffee wood is produced at our two factories in Vietnam — one in Dak Lak and one in Gia Lai, both in the Central Highlands close to where the wood is collected. Both build to our specification and release against our quality checks. Goods are shipped from our warehouse in Ho Chi Minh City, where packing, quality release and export documents are prepared.")+
            table(["Site","Location"],SITES)+
            p("Monthly capacity is 100,000 pieces across the product lines. A monthly figure says little about a short run of several sizes with different labels, so the volume and dates for your order are planned against the actual SKU mix and confirmed in your quotation.")+
            p("Pre-shipment inspection can be arranged at our Ho Chi Minh City warehouse, and dated photos or a video walkthrough of your production line are available on request.")),
         section("Coffee wood drying and quality protocol",
            p("Coffee wood follows a "+QC_PROTOCOL+". The five checkpoints are inspection controls within that process.")+
            p(MOISTURE)+
            p('We keep its operating parameters confidential; the published figure is the finished-batch moisture threshold, not the drying recipe. Ask for the moisture record linked to your order. Drying temperatures, cycle times and the stage sequence are not published.'),True),
         section("From plantation to billet: raw material intake",
            p("Coffee wood reaches our factories as stems taken out during a grower\u2019s normal replanting cycle in Dak Lak and Gia Lai. "
              "They are cut to billets in the field, delivered to the intake yard and stacked in the open for about a year before machining.")+
            gallery([
              ("coffee-stems-on-trailer-central-highlands.jpg","Collection at the plantation edge in the Central Highlands."),
              ("worker-loading-coffee-stems-onto-trailer.jpg","Stems are loaded by hand onto the trailer."),
              ("collecting-coffee-stems-at-the-plantation.jpg","Cut stems gathered where the replanting happens."),
              ("coffee-stem-intake-yard.jpg","Intake yard at the factory."),
              ("coffee-wood-stacked-for-air-seasoning.jpg","Open-air seasoning stacks, roughly a year before machining."),
              ("cut-coffee-wood-billets.jpg","Billets cut and sorted ready for the line."),
            ])),
         section("Drying, grading and the moisture record",
            p("After shaping, chews are dried and graded before they are packed. Batch moisture is measured below 14% and the reading is filed against your lot.")+
            gallery([
              ("coffee-wood-chews-on-drying-racks.jpg","Shaped chews on the drying racks."),
              ("coffee-wood-chews-inside-drying-chamber.jpg","Chews held under cover while they come down to moisture \u2014 ambient air, not a kiln."),
              ("graded-coffee-wood-chews-on-rack-rows.jpg","Graded by size before packing."),
              ("moisture-meter-reading-on-coffee-wood-chew.jpg","Moisture meter reading on a finished chew."),
              ("moisture-meter-probes-in-chew-stick.jpg","Every batch is read below 14% before it is packed."),
              ("grading-chews-at-the-packing-bench.jpg","Grading at the packing bench; cracked pieces are rejected."),
            ]),True),
         section("Packing: vacuum pack, desiccant, export carton",
            p("Standard coffee wood is vacuum packed with a desiccant sachet inside, layered into the export master carton and labelled by size and quantity.")+
            gallery([
              ("staff-packing-chews-into-export-carton.jpg","Packing chews into the export carton."),
              ("bagging-coffee-wood-chews-for-export.jpg","Bagging before cartoning."),
              ("silica-gel-sachet-inside-vacuum-pack.jpg","Desiccant sachet sealed inside the pack."),
              ("vacuum-packs-layered-in-export-carton.jpg","Vacuum packs layered into the carton."),
              ("packing-vacuum-packs-into-export-carton.jpg","Carton built up pack by pack."),
              ("palletised-export-cartons-with-size-labels.jpg","Cartons marked with size and quantity."),
            ])),
         section("Ho Chi Minh City: warehouse, inspection and loading",
            p("Goods are shipped from our warehouse in Ho Chi Minh City. Stock sizes are held there, pre-shipment inspection can be arranged before the container is sealed, and the container leaves for Cat Lai port.")+
            gallery([
              ("ho-chi-minh-city-warehouse-aisle.jpg","Stock held in our Ho Chi Minh City warehouse."),
              ("stretch-wrapped-pallet-of-export-cartons.jpg","Pallets wrapped and staged for dispatch."),
              ("inspector-checking-cartons-with-a-checklist.jpg","Carton check against the packing list."),
              ("measuring-a-carton-stack-during-inspection.jpg","Carton dimensions verified during inspection."),
              ("loading-cartons-into-the-container.jpg","Loading at the warehouse bay."),
              ("stacking-cartons-inside-the-container.jpg","Cartons stacked by hand inside the container."),
              ("team-stacking-cartons-in-the-container.jpg","The loading team builds the stack row by row."),
              ("checking-the-carton-wall-inside-a-container.jpg","The finished carton wall is checked before the doors close."),
              ("applying-the-container-seal-before-departure.jpg","Numbered seal applied before departure."),
              ("sealed-container-leaving-the-warehouse.jpg","Sealed and on its way to Cat Lai port."),
              ("warehouse-container-loading-bay.jpg","The loading bay at the warehouse."),
            ]),True),
         section("What to request in a factory verification pack",ul([
            "Current company registration and site details matching the proposed contract.",
            "A dated walkthrough identifying the product line and stages handled there.",
            "Production slot and capacity calculation for the actual SKU mix and pack.",
            "Quality checkpoints, measuring equipment and sample/lot identification.",
            "Arrangements for independent pre-shipment inspection at the packing warehouse.",
            "Authorized, appropriately redacted shipment examples where relevant."])+
            p('<a href="/quality-control/">Review the quality-control workflow</a> and <a href="/certifications/">document scope</a> before agreeing the inspection brief.'),True)],
        active="Manufacturing",image="/assets/img/process-raw-sticks.jpg",
        faqs=[("How is production capacity confirmed?", "Monthly capacity is 100,000 pieces across the product lines. That figure is a ceiling, not a promise for your order: capacity is planned against your actual product mix and packaging, and the lead time and production slot are confirmed in your quotation."),
              ("Where is production carried out?", "Coffee wood is produced at our two factories, in Dak Lak and Gia Lai. The specification, the production plan, the QC checkpoints and the quality release are ours, and so are the export documents. Goods are shipped from our Ho Chi Minh City warehouse, and we will name the site that makes your order."),
              ("How can I verify production without travelling?", "Ask for dated photos of your line, a video walkthrough and the batch moisture record filed against your lot. Pre-shipment inspection can be arranged at our Ho Chi Minh City warehouse before the container is sealed.")])
    publish(root,"/quality-control/","Pet Toy Quality Control | VietPaw",
        "Coffee wood follows our drying and quality protocol with five QC checkpoints. Review batch moisture below 14% before packing and inspection records.",
        "Quality Control for Natural Pet Toy Orders",
        "Coffee wood follows a "+QC_PROTOCOL+". Use an approved sample, agreed acceptance criteria and batch-linked records to review your order.",
        [section("Six process stages and five QC checkpoints",
            p("The drying and quality protocol has six stages; the five QC checkpoints are controls inside those stages. VietPaw does not publish the confidential operating parameters or a detailed stage-by-stage sequence.")+
            p('See our <a href="/collections/coffee-wood/">coffee wood material page</a> for the current process summary. For other materials, agree the checks appropriate to the construction rather than applying a wood-drying protocol to every toy.')),
         section("Inspection records to agree for your order",table(["Review area","What to agree for your product","Record to request"],[
            ("Raw material","Material identity, cleanliness, visible defects and declared treatment","Intake record linked to material/lot"),
            ("In-process","Preparation, drying, cutting, winding or shaping against the process specification","Process check and deviation notes"),
            ("Semi-finished","Dimensions, assembly and consistency before final work","Intermediate measurements and correction record"),
            ("Final product","Finish, attachment security, sample match and packaging","Finished-product inspection results"),
            ("Pre-shipment","Order count, labels, cartons and shipment-document match","Release check and agreed shipment inspection")])+
            p("These are buyer review areas, not a disclosure of the drying sequence or the exact placement of the five checkpoints. Adapt the checklist to wood, coir, hemp or loofah and confirm the inspection plan for the chosen product.")),
         section("Material-specific checks",table(["Product","Priority checks"],[
            ("Coffee wood sticks","Dimension bands, visible cracks, edge finish and agreed moisture measurement"),
            ("Coir balls","Winding, diameter, loose fiber, core and binding components"),
            ("Hemp ropes/balls","Knots, strand shedding, dimensions and attachment/pull checks"),
            ("Loofah shapes","Dryness, seams, attachments, filling and shape consistency"),
            ("All retail packs","Artwork version, product identity, warnings, count and carton data")]),True),
         section("Coffee wood moisture: below 14% before packing",
            p(MOISTURE)+p("This is a production control, not a universal pet-safety standard or a promise that mold and cracking cannot occur. Dry storage and suitable moisture-protective packing still matter.")+
            p("Ask which meter/method is used, where readings are taken, how many units are checked, when measurements happen and how deviations are handled. Calibration status and a lot-linked record should be part of the discussion if moisture is a contractual acceptance criterion.")),
         section("What the checkpoints look like",
            p("Five QC checkpoints sit inside the process: at intake, after seasoning, after shaping, at grading and at the packing bench. Pre-shipment checks are made at our Ho Chi Minh City warehouse before the container is sealed.")+
            gallery([
              ("coffee-stem-intake-yard.jpg","Intake: material arriving at the yard."),
              ("graded-coffee-wood-chews-on-rack-rows.jpg","After seasoning: graded by size."),
              ("grading-chew-sticks-by-hand.jpg","At grading: cracked pieces are taken out."),
              ("moisture-meter-probes-in-chew-stick.jpg","At the bench: batch moisture below 14%."),
              ("moisture-check-before-packing.jpg","A second reading at the packing table."),
              ("checking-packs-inside-an-export-carton.jpg","Packs checked inside the carton."),
              ("vacuum-pack-with-desiccant-sachet-in-carton.jpg","Desiccant sachet in every vacuum pack."),
              ("inspector-checking-cartons-with-a-checklist.jpg","Carton check against the packing list."),
              ("measuring-a-carton-stack-during-inspection.jpg","Dimensions verified during inspection."),
              ("pre-shipment-inspection-at-the-container-door.jpg","Pre-shipment inspection at the container door."),
            ]),True),
         section("What we commit to, and how a claim is assessed",p(MOULD_COMMITMENT)),
         section("Agree quality before the purchase order",ul([
            "Approved physical sample and current specification version.",
            "Measurable dimensions, material composition and acceptable natural variation.",
            "Defect definitions and the sampling and acceptance plan (for example an AQL level) agreed for your order.",
            "Any required independent lab test or third-party inspection, scoped separately.",
            "Hold/rework/rejection process and written receiving/claim terms."])+
            p("Do not use the phrase SGS-certified as a substitute for a report with a named product, method, date and scope. Inspection, laboratory testing and shipment documentation serve different purposes.")+
            p('<a href="/certifications/">Understand testing and export documents</a> or <a href="/services/oem-odm-pet-toy-manufacturing/">include QC in an OEM brief</a>.'),True)],
        active="Manufacturing",image="/assets/img/vietpaw-moisture-check.jpg")
