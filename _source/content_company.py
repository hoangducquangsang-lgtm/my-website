# -*- coding: utf-8 -*-
from common import page, write_page, breadcrumb_html, BRAND, BRAND_INTRO, CONTRACT_NOTICE, PHONE, PHONE_TEL, EMAIL, ADDRESS
from content_helpers import publish, hero, section, p, ul, table, cards, terms, trust_links, SAMPLES, SAMPLE_DISPATCH, LEAD, PRIVATE_LABEL, EXPORT_DOCS, RANGE_SCOPE, SOURCE_OEM, FTC, CPSC, ECHA
from content_materials import MATERIALS
from forms import quote_form, catalogue_form

def build(root):
    publish(root,"/capabilities/","OEM, ODM & Private-Label Capabilities | VietPaw",
        "Compare VietPaw wholesale, OEM/ODM and private-label pet toy services. Choose the right route for standard products, custom development and branded packaging.",
        "OEM, ODM & Private-Label Pet Toy Manufacturing in Vietnam",
        "Choose an existing design, build to your specification or develop a new construction. We separate the product brief, sample approval and packaging decisions so your quote is clear.",
        [section("Choose the right manufacturing service",cards([
            ("OEM / ODM manufacturing","Specification-led production, prototype review and new construction development.","/services/oem-odm-pet-toy-manufacturing/"),
            ("Private-label pet toys","Existing designs with your label, wood engraving or branded packaging.","/services/private-label-pet-toys/"),
            ("Wholesale pet products","Standard products, multi-SKU orders and repeat-purchase planning.","/services/wholesale-pet-products/")])+
            table(["Route","What changes","What to approve"],[
                ("Wholesale","Quantity and packing on existing references","SKU list, sample and order terms"),
                ("Private label","Brand presentation","Product sample, artwork and packaging"),
                ("OEM / ODM","Product specification or construction","Brief, prototype, materials and inspection criteria")])),
         section("What can be customized",ul([
            "Logo engraving on suitable wood surfaces, with position and legibility agreed on the sample.",
            "Product tags, size labels, paper/kraft boxes and pack artwork.",
            "Wood-and-rope combinations, rope geometry and loofah shapes, subject to feasibility.",
            "Product photography or video support by agreement; scope and cost depend on the project."])+
            p(f'The manufacturer describes these services in its <a href="{SOURCE_OEM}">official manufacturing and order information</a>. VietPaw is the commercial/export brand. Specific charges, minimums and deliverables are confirmed in your quotation.'),True),
         section("Before approving a sample",ul([
            "Agree materials, dimensions, tolerances and intended pet/use.",
            "List every component, including thread, cores, adhesive and packaging film.",
            "Confirm artwork, barcode file, warnings and market-specific testing needs.",
            "Record approval and the circumstances that require a new sample."],True)+trust_links()),
         section("Order planning",terms(),True)],
        active="Manufacturing",image="/assets/img/process-laser-engraving.jpg",
        faqs=[("Is every customization included in the standard price?", "No. Engraving, printing, box production, new tooling, tests and media work must be itemized where applicable."),
              ("Does a small product MOQ also apply to printed boxes?", "No. Selected standard products and suitable coffee wood engraving start at 50 pcs. "+PRIVATE_LABEL)])
    publish(root,"/materials/","Pet Toy Materials: Coffee Wood, Coir, Hemp & Loofah | VietPaw",
        "Compare coffee wood, coconut fiber, hemp and loofah for wholesale pet toys. Review product formats, component declarations and sourcing questions.",
        "Four Natural Materials for Your Pet Toy Range",
        "Start with the material and intended play type, then verify the complete construction. A natural ingredient is the beginning of a sourcing decision, not a finished-product certification.",
        [section("Explore the material collections",cards([
            ("Coffee Wood","Mature coffee-tree timber for shaped chew sticks.","/collections/coffee-wood/","/assets/img/winvn-coffee-wood-single.jpg"),
            ("Coconut Fiber","Coconut-husk fiber for textured balls and coir formats.","/collections/coconut-fiber/","/assets/img/product-coconut-fiber-raw.jpg"),
            ("Hemp Fiber","Plant fiber used in wound balls and rope constructions.","/collections/hemp-fiber/","/assets/img/winvn-hemp-wood-assortment.jpg"),
            ("Loofah","Dried gourd fiber cut and shaped for lightweight toys.","/collections/loofah/","/assets/img/winvn-loofah-growing.png")],4)+p(RANGE_SCOPE)),
         section("Read the full bill of materials",p("Request the primary material, core, binding thread, adhesive, filling, decoration and any surface treatment for the selected product. A wood stick with a rope is not the same construction as a plain stick, and a loofah shape with filling is not the same as a plain cut piece.")+
            p("The retail pack needs its own material list. Paper boxes can include coatings or windows; vacuum bags are not automatically plastic-free.")+
            p('<a href="/sustainability/">Read the material-claim approach</a> and <a href="/certifications/">testing/document scope</a>.'),True),
         section("From material to commercial brief",p("Choose the product, target pet, use, dimensions and first-order quantity. Then decide whether to use a standard wholesale design, add private-label packaging, or develop a new construction.")+
            p('<a href="/capabilities/">Compare manufacturing options</a> or <a href="/services/wholesale-pet-products/">plan a mixed-material wholesale order</a>.'))],
        active="Materials")
    publish(root,"/certifications/","Pet Toy Testing & Export Documentation | VietPaw",
        "Understand product testing, inspection and shipment documents for VietPaw pet toys. Confirm report scope and destination requirements before ordering.",
        "Pet Toy Testing, Quality Records & Export Documents",
        "A test report, a factory inspection and a shipment certificate answer different questions. Agree the evidence your buyer, importer and destination require before production.",
        [section("Three different types of evidence",table(["Evidence","What it addresses","What it does not establish"],[
            ("Product/material test report","Named samples, methods, tested substances or physical properties","Blanket certification of every product and future batch"),
            ("QC / inspection record","Checks against an agreed specification for a sample or lot","Automatic legal approval in every country"),
            ("Export / shipment document","Origin, movement or treatment of specified goods","A universal pet-safety or sustainability certification")])),
         section("Confirm documents for your shipment",p(CONTRACT_NOTICE)+p("VietPaw’s export-document offer covers: "+EXPORT_DOCS)+table(["Document","How to scope it"],[
            ("Commercial invoice and packing list","Confirm product description, quantities, packages and contracting parties."),
            ("Certificate of Origin (CO)","Confirm the applicable form, issuing details and origin/destination requirements."),
            ("Fumigation Certificate","Confirm treatment applicability, covered goods, certificate details and destination requirements."),
            ("Phytosanitary Certificate","Confirm plant-material requirements for the selected product and destination."),
            ("Bill of Lading (B/L)","For sea shipments, check shipper, consignee, ports and cargo details against the invoice and packing list. Agree the transport document for other modes."),
            ("Batch moisture reading — on request","For coffee wood, request the batch-linked reading showing below 14% before packing. This is a QC record, not a customs certificate."),
            ("Preferential origin evidence, including EUR.1 where applicable","Have the importer or broker verify origin rules and tariff eligibility; preference is not automatic."),
            ("Inspection report","Agree who inspects, which lot, when, and against what criteria."),
            ("Other material or forestry records","Request where relevant to the selected product and applicable requirements.")])+
            p("A standard paperwork bundle cannot guarantee customs clearance. Use the destination, product construction and shipment details to agree the required list with your broker.")+
            p('<a href="/proof/">See the Proof document register</a> for the scope and limitations of the supplied reference files; they are not current shipment certificates.'),True),
         section("Product testing is scoped, not implied",
            p("Third-party testing can be discussed against the requirements applicable to your target market, retailer, product construction and buyer specification. Confirm the laboratory, sample identification, test method, report date, result and limits of the assessment.")+
            p(f'<a href="{CPSC}">CPSC toy-safety guidance</a> addresses children’s toys; do not assume every pet toy needs a children’s-product certificate. <a href="{ECHA}">REACH restrictions</a> can apply to substances in articles; natural materials do not automatically establish compliance.')+
            p("This website does not present a current, SKU-specific SGS, Intertek, CPSIA or REACH certificate as already verified. Ask us to confirm what relevant evidence is available and what needs to be arranged.")),
         section("What to request before signing the order",ul([
            "Current company details matching the contracting party and payment beneficiary.",
            "The precise SKU/material list covered by each report, including attachments and treatments.",
            "Report number, date and issuing organization, plus permission to verify the report.",
            "A shipment-linked document checklist, with responsibility for obtaining each item.",
            "Written claim-handling, inspection and acceptance terms rather than an assumed blanket replacement promise."])+trust_links(),True)],
        active="Manufacturing",image="/assets/img/export-packed-box.jpg",
        faqs=[("Does every order automatically include every certificate?", "No. Document applicability, availability, cost and timing are confirmed for the shipment."),
              ("Can I arrange an independent factory or shipment inspection?", "Discuss the proposed scope, inspector, access and schedule with us before production or dispatch."),
              ("Are historical sample documents proof for my order?", "No. Verify the entity, product scope, dates and shipment linkage; examples and templates are not current certificates.")])
    publish(root,"/sustainability/","Natural Materials & Responsible Product Claims | VietPaw",
        "Review VietPaw material sourcing and packaging options without blanket green claims. Separate reuse, plant origin and disposal evidence for each product.",
        "Natural Materials, Specific Claims, Clear Evidence",
        "We focus on coffee wood, coconut fiber, hemp and loofah. Responsible sourcing copy should explain what the selected product contains and what evidence supports each claim.",
        [section("Different materials, different sourcing stories",table(["Material","Supported starting description","Evidence to request"],[
            ("Coffee wood","Timber from mature coffee trees described in the product information","Sourcing location, material identity and removal/reuse history"),
            ("Coconut fiber","Fiber from coconut husks","Source and processing information for the selected supply"),
            ("Hemp fiber","Plant-derived fiber used in rope/ball designs","Fiber identity, blends and source"),
            ("Loofah","Dried gourd-fiber material","Cultivation/source, preparation and complete toy construction")])+
            p("Hemp and loofah are not automatically by-products or waste streams. We do not apply an upcycled claim to the entire range or publish carbon savings without a defined assessment.")),
         section("Product and packaging must be checked separately",
            p("Review every component: wood or fiber, internal core, thread, glue, filling, paint, ink, coating, tag and wrapping. Packaging can be discussed in bulk, individual or paper/kraft formats. Vacuum film, laminated paper and coated boxes should not be described as plastic-free without confirmation.")+
            p("Charcoal and silica gel are different desiccants; replacing the contents of a sachet does not establish that its outer packet or the shipment is plastic-free. Agree moisture protection on performance and the actual packaging specification."),True),
         section("Biodegradability requires conditions and scope",
            p("VietPaw does not publish biodegradability claims without appropriate evidence for the finished product and its disposal conditions.")+
            p(f'Material origin does not by itself substantiate a whole-product disposal claim. Define the component, disposal environment, time period and test evidence before using biodegradability or compostability language. See the <a href="{FTC}">FTC environmental-claims guidance</a>.')+
            p("No product-wide compostability certificate or fixed decomposition time is asserted here. Do not instruct customers to bury toys or dispose of them in a compost stream unless the exact construction and local acceptance support that instruction.")),
         section("What buyers can build into a sourcing brief",ul([
            "A complete bill of materials for the product and the pack.",
            "Clear requirements for thread, cores, adhesives, dyes, coatings and plastic components.",
            "Specific origin/reuse statements, avoiding unverified waste-diversion or carbon numbers.",
            "A test or evidence plan for the environmental claim you intend to print.",
            "Written approval of artwork and disposal language before production."])+
            p("Community-impact claims, beneficiary numbers, recycled percentages and comparative environmental advantages need their own records. They are not inferred from the location of a workshop.")+
            p('<a href="/solutions/eco-pet-shops/">Plan an eco-retail assortment</a> or <a href="/services/private-label-pet-toys/">review private-label packaging</a>.'),True)],
        active="Company",image="/assets/img/process-coffeewood-styled.jpg")
    publish(root,"/how-to-order/","How to Order Pet Toys: Samples, MOQ & Lead Time | VietPaw",
        "Plan your VietPaw sample and wholesale order: product brief, MOQ, artwork approval, production, inspection and destination-specific shipping.",
        "From Product Brief to Sample-Approved Order",
        "Make the first order manageable by agreeing the product, pack and responsibilities before paying for production.",
        [section("The ordering sequence",ul([
            "<strong>Send the brief.</strong> Product references, sizes, quantities per SKU, destination, channel and branding requirements.",
            "<strong>Review an itemized quote.</strong> Include product, packaging, development/testing, sample and freight items where applicable.",
            "<strong>Approve the physical sample and artwork.</strong> Record dimensions, materials, tolerances, label content and any changes.",
            "<strong>Confirm the order.</strong> Agree payment, lead time, Incoterm with named place, document scope and inspection terms.",
            "<strong>Produce and inspect.</strong> Use the approved reference and agreed checkpoints; resolve deviations before dispatch.",
            "<strong>Ship and receive.</strong> Review the packing list and shipment documents, then follow the agreed receiving and claim process."],True)),
         section("MOQ, samples and production timing",terms()+p("Sample preparation, custom prototyping, artwork revisions, outside testing and transport are separate stages. The production estimate starts only after the required approvals and commercial conditions are met."),True),
         section("Shipping and payment are order-specific",
            p(CONTRACT_NOTICE)+p("Ask for transport mode, named origin/destination, packed dimensions and weight before comparing shipping quotes. Air, courier and sea services are not interchangeable; there is no single worldwide freight timeline.")+
            p("EXW, FOB or CIF can be discussed with your forwarder, but the named place/port and the applicable version of the terms must be stated. Destination duties, taxes, clearance and local delivery should be itemized rather than assumed to be included.")+
            p("Payment schedule, inspection acceptance and handling of defective goods belong in the written order agreement. This page does not set an automatic credit, refund or replacement entitlement.")),
         section("For reorders",p("Keep the approved sample/version, product codes, artwork, carton configuration and inspection criteria together. Confirm material or packaging changes before repeat production. Share a rolling forecast with required delivery dates rather than relying on an annual capacity headline.")+
            p('<a href="/solutions/wholesalers/">Distributor reorder planning</a> · <a href="/solutions/retail-chains/">Retail-chain supply preparation</a>'),True)],
        active="Company")
    publish(root,"/wholesale-catalogue/","VietPaw Wholesale Pet Toy Catalogue (PDF) | VietPaw",
        "Download the manufacturer’s supplied pet toy catalogue and contact VietPaw for current specifications, prices, MOQ and private-label terms.",
        "Wholesale Pet Toy Catalogue",
        "Explore the VietPaw range. Use the manufacturer’s catalogue as a visual reference, then confirm the current range and terms with Sarah.",
        [section("Download instantly. Ask for pricing when you need it.",
            '<div class="grid grid-2"><div><p><a class="btn btn-primary" href="/assets/downloads/winvn-wholesale-catalogue.pdf">Download Catalogue (PDF)</a></p>'+
            p("This download is the original supplied manufacturer catalogue; its artwork has not been rebranded as VietPaw. It is not a newly certified product specification or live price list. Older safety, size, environmental or commercial wording in the PDF should not be copied into your packaging or order terms without review. Use the current website order information and your written quotation for samples, minimums and production timing.")+
            p("No email is required to download. If you would like current MOQ and pricing, use the optional form alongside the catalogue. We use those details to reply to your request, not to subscribe you to a newsletter.")+'</div><div>'+catalogue_form()+'</div></div>'),
         section("Send the product references you want quoted",p("Include the catalogue item or photo reference, dimensions, quantity per SKU, destination and packaging requirements. The approved sample and written quote take precedence over catalogue examples.")+
            p('<a href="/products/coffee-wood-dog-chew/">Coffee wood reference specifications</a> · <a href="/collections/hemp-fiber/">Hemp collection</a> · <a href="/request-a-quote/">Request current pricing</a>'),True)],active="Company")
    build_rfq(root)
    publish(root,"/contact/","Contact VietPaw | Samples & Wholesale Enquiries",
        "Contact Sarah at VietPaw for natural pet toy samples, wholesale quotations, private-label packaging and OEM/ODM projects in Vietnam.",
        "Talk to VietPaw About Your Next Product",
        "Share the product, destination and expected order quantity. Add your branding, packaging and timing requirements so we can respond to the right brief.",
        [section("VietPaw sales contact",p(BRAND_INTRO)+p(CONTRACT_NOTICE)+
            ul([f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>',f'Phone: <a href="tel:{PHONE_TEL}">{PHONE}</a>',
                f'WhatsApp: <a href="https://wa.me/{PHONE_TEL[1:]}">Open a conversation</a>',"Registered head office: "+ADDRESS])+
            p("Your contact: Sarah. Share your destination market, product selection and quantities so we can prepare the right sample and quotation options.")),
         section("Prepare for a manufacturing review",p('For production locations and inspection arrangements, see <a href="/factory/">Factory & Production</a>. Please arrange visits in advance and confirm the current site address and contact for your product line.')+
            p('<a href="/request-a-quote/">Prepare a structured enquiry</a> or <a href="/wholesale-catalogue/">download the catalogue</a>.'),True)],active="Company")

def build_rfq(root):
    bc,bs=breadcrumb_html([("Home","/"),("Request a Quote",None)])
    content=bc+hero("Request a Quote or Product Sample",
        "Tell us the product and destination first. Add what you know about quantities, branding and launch timing; you do not need a finished technical brief.",eyebrow="VietPaw B2B enquiries",ctas=False)
    content+=f"""
<section class="section"><div class="wrap grid grid-2">
{quote_form()}
<div><h2>What happens next</h2><p>We review your brief and confirm product availability, MOQ, sample terms and an indicative timeline. New development or testing may need a separate feasibility discussion.</p>
{ul(["Starting MOQ from 50 pcs on selected standard products; confirm each line.",SAMPLES+" "+SAMPLE_DISPATCH,PRIVATE_LABEL,LEAD,EXPORT_DOCS])}
<h3>Company details for your order</h3>{p(CONTRACT_NOTICE)}
<h3>Contact sales directly</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="https://wa.me/{PHONE_TEL[1:]}">WhatsApp</a></p>
<p class="small">Do not include payment-card information or confidential designs in this first enquiry. Request an agreed confidentiality process if needed.</p>
{trust_links()}</div></div></section>
"""
    write_page(root,"/request-a-quote/",page("Request Pet Toy Samples & Wholesale Quote | VietPaw",
        "Request a quote or product sample from VietPaw. Share your products of interest for pricing, lead time and sample availability — usually within one business day.",
        "/request-a-quote/",content,schemas=[bs]))
    bc,bs=breadcrumb_html([("Home","/"),("Request a Quote","/request-a-quote/"),("Thank You",None)])
    thanks=bc+hero("Thank you — we've got your enquiry",
        "Our team will get back to you, usually within one business day, with indicative pricing, MOQ and lead time. If your request is urgent, reach us directly on WhatsApp or by phone.",
        eyebrow="Enquiry received",ctas=False)
    thanks+=section("Stay in touch",p(f'<a class="btn btn-primary" href="https://wa.me/{PHONE_TEL[1:]}">Contact us on WhatsApp</a>')+
        p(f'<a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:{PHONE_TEL}">{PHONE}</a>')+
        p('<a href="/wholesale-catalogue/">Browse the catalogue</a> or <a href="/">return to the homepage</a>.'))
    write_page(root,"/request-a-quote/thank-you/",page("Thank You for Your Enquiry | VietPaw",
        "Thank you for contacting VietPaw. Our team will review your pet toy enquiry and reply with pricing, sample availability and lead time.",
        "/request-a-quote/thank-you/",thanks,schemas=[bs],noindex=True))
