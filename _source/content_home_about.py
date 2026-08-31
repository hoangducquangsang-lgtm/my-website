# -*- coding: utf-8 -*-
from common import BRAND, BRAND_INTRO, ADDRESS, PHONE, EMAIL, BASE_URL, REGISTRATION_DATE, page, write_page, organization_schema
from content_helpers import hero, section, cards, p, ul, table, faq, rfq_bar, trust_links, publish, SAMPLES, SAMPLE_DISPATCH, PRIVATE_LABEL, QC_PROTOCOL, RANGE_SCOPE, LEAD
from content_products import product_cards

def build(root):
    content=hero("Natural Pet Products for Global Brands",
        "Made in Vietnam from coffee wood, coconut fiber, hemp and loofah. Wholesale, OEM/ODM and private-label options, with selected standard products starting from 50 pcs per SKU.",
        eyebrow="VietPaw · International B2B sourcing", image="/assets/img/winvn-home-thu-cung-3.jpg")
    content+=section("Natural materials. Clear specifications. A practical first order.",
        '<div class="stats"><div><strong>4</strong><span>Core natural materials</span></div><div><strong>50 pcs</strong><span>Starting MOQ on selected standard SKUs</span></div><div><strong>OEM / ODM</strong><span>Specification-led development</span></div><div><strong>Private label</strong><span>Product and packaging support</span></div></div>'+
        p("Start with the product that fits your customer and channel, then confirm the sample, full material construction and order terms. A clear specification makes it easier to compare quotes and repeat the right product."))
    content+=section("Choose your wholesale product range",cards([
        ("Natural dog toys","Coffee wood chews, fiber balls and rope formats for a sample-approved range.","/dog-toys/","/assets/img/dog-chewing-coffeewood.jpg"),
        ("Natural cat toys","Coconut-fiber balls and loofah shapes with cat-specific construction and packaging.","/cat-toys/","/assets/img/cat-loofah-toys-lifestyle.jpg"),
        ("Natural dog chews","Compare stick sizes and review the limits of hard-chew suitability.","/dog-toys/chew-toys/","/assets/img/winvn-coffee-wood-sizes.png")]),True)
    content+=section("Four natural materials, one sourcing conversation",cards([
        ("Coffee wood","Mature coffee-tree wood shaped into chew sticks; engraving available on suitable surfaces.","/collections/coffee-wood/","/assets/img/winvn-coffee-wood-single.jpg"),
        ("Coconut fiber","Coconut-husk fiber used in textured balls and other coir formats.","/collections/coconut-fiber/","/assets/img/product-coconut-fiber-raw.jpg"),
        ("Hemp fiber","Wound balls, knotted rope and mixed-material development options.","/collections/hemp-fiber/","/assets/img/winvn-hemp-wood-assortment.jpg"),
        ("Loofah","Dried gourd fiber shaped into lightweight cat-play designs.","/collections/loofah/","/assets/img/winvn-loofah-growing.png")],4)+p(RANGE_SCOPE))
    content+=section("OEM, ODM and private-label pet toy manufacturing",cards([
        ("Develop your own construction","Bring a drawing or design brief. Agree feasibility, prototype, materials and production checks.","/services/oem-odm-pet-toy-manufacturing/"),
        ("Brand an existing product","Choose an approved design and add your logo, labels or packaging.","/services/private-label-pet-toys/"),
        ("Source a wholesale assortment","Plan quantities per SKU, pack configuration and repeat orders across the range.","/services/wholesale-pet-products/")])+
        p('<a href="/capabilities/">Compare all manufacturing services</a> and choose the level of customization your launch needs.'),True)
    content+=section("Meet the manufacturing partner behind your range",
        '<div class="grid grid-2"><div>'+p(BRAND_INTRO)+p("Our manufacturer, registered in Vietnam in 2019, makes natural pet products and supplies customers in 40+ countries. Our toy collections combine coffee wood from the Central Highlands with coconut fiber, hemp fiber and loofah, with wholesale, private-label and OEM/ODM options for international buyers.")+
        p('For a factory-focused sourcing review, start with our <a href="/pet-toys-manufacturer-vietnam/">pet toy manufacturer in Vietnam</a> page. Review production locations, order planning and the evidence to request before placing a purchase order.')+
        trust_links()+'</div><figure><img src="/assets/img/winvn-moisture-check-kiem-go-9.jpg" alt="Coffee wood moisture-check process reference" loading="lazy"><figcaption>Process reference from the supplied asset library; request current batch records for your order.</figcaption></figure></div>')
    content+=section("Built for how your business buys",cards([
        ("Amazon sellers","Pack dimensions, barcode artwork and marketplace-specific preparation.","/solutions/amazon-sellers/"),
        ("Wholesalers & distributors","Mixed-SKU orders, reorder specifications and rolling demand planning.","/solutions/wholesalers/"),
        ("Pet brands","Product development, change control and brand-specific packaging.","/solutions/pet-brands/"),
        ("Retail chains","Vendor onboarding, carton consistency and phased store launches.","/solutions/retail-chains/"),
        ("Startup brands","Small pilot orders and a manageable first-product brief.","/solutions/startup-brands/"),
        ("Eco pet shops","Specific material stories and carefully qualified packaging claims.","/solutions/eco-pet-shops/")]),True)
    content+=section("Product specifications before purchase",product_cards(["coffee-wood-dog-chew","coconut-fiber-dog-ball","loofah-cat-toy"]))
    content+=section("Sustainability starts with a specific claim",
        p("Coffee wood and coconut husks offer clear material-reuse stories. Hemp and loofah are plant-derived materials, but are not automatically agricultural waste. The composition of a finished toy and the bag, box, ink or coating around it must be evaluated separately.")+
        p('We do not publish biodegradability claims without appropriate evidence for the finished product and disposal conditions. “Natural” is not proof of safety or disposal performance. Read our <a href="/sustainability/">material and packaging approach</a>.'),True)
    content+=section("From sample request to agreed production",ul([
        "<strong>Share your brief.</strong> Tell us the product, quantity per SKU, destination and branding requirements.",
        "<strong>Review the sample and quote.</strong> Confirm dimensions, materials, packaging, timing, payment terms and document scope.",
        "<strong>Approve production and shipment.</strong> Agree the inspection and freight arrangements before dispatch."],True)+
        p(SAMPLES+" "+SAMPLE_DISPATCH)+p(LEAD)+p('<a href="/how-to-order/">See the full ordering process</a>.'))
    content+=faq([
        ("Do you offer wholesale and private label?", "Yes. Choose existing designs for wholesale or branded packaging, or discuss OEM/ODM for changes to construction. "+PRIVATE_LABEL),
        ("Does the 50-piece MOQ cover every product?", "No. It applies to selected standard SKUs; laser engraving on suitable coffee wood surfaces also starts at 50 pcs. Private-label runs, custom hang tags, labels and printed boxes start at 500 pcs."),
        ("Can I verify the factory and product documentation?", "Request current location information, a production walkthrough and the reports relevant to your chosen SKU and destination. A supplier's general description is not a substitute for order-specific evidence."),
        ("Are all natural toys suitable for every pet?", "No. Size, construction, chewing behavior and dental health matter. These products are not food and require supervision and replacement when damaged.")])
    content+=rfq_bar("Tell us your product, destination and first-order quantity.","Request Samples & a Quote")
    schemas=[organization_schema(),{"@context":"https://schema.org","@type":"WebSite","@id":BASE_URL+"/#website","name":BRAND,"url":BASE_URL+"/"}]
    write_page(root,"/",page("Natural Pet Products from Vietnam | VietPaw",
        "Explore VietPaw natural pet toys from Vietnam: coffee wood, coconut fiber, hemp and loofah for wholesale, private label and OEM/ODM.",
        "/",content,schemas=schemas,og_image="/assets/img/winvn-home-thu-cung-3.jpg"))
    publish(root,"/about/","About VietPaw | Natural Pet Toys Made in Vietnam",
        "Meet VietPaw and explore our natural pet toy range, Vietnam manufacturing, materials and sourcing support for international buyers.",
        "VietPaw: Natural Materials, Made for Global Brands",
        BRAND_INTRO+" Our manufacturer was registered in Vietnam in 2019 and supplies customers in 40+ countries.",
        [section("The materials behind the story",
            p("Our toy collections bring together coffee wood, coconut fiber, hemp fiber and loofah. Coffee wood is linked to Vietnam's Central Highlands, with preparation and finishing that turn mature timber into a defined product format.")+p(RANGE_SCOPE)+
            p("The next step for a buyer is practical: evaluate the sample, check who produces it, review the construction and confirm what will appear on the invoice and shipment documents.")),
         section("Brand, company and sales contact",table(["Role","Information"],[
            ("Website / site name",BRAND),("Commercial / export brand",BRAND),
            ("Manufacturing base","Vietnam"),("Manufacturer registered in Vietnam",REGISTRATION_DATE),
            ("VietPaw sales email",EMAIL),("VietPaw sales phone",PHONE),("Registered head office",ADDRESS)])+
            p("VietPaw is the name used for the commercial range and export enquiries. Confirm the contracting entity, registered details and payment beneficiary in your order documents. Historical samples do not replace current company verification.")+p('<a href="/proof/">Review the Proof document register</a> and request records relevant to your order.'),True),
         section("What we support",cards([
            ("Manufacturing review","Locations, process and a capacity discussion for your SKU mix.","/factory/"),
            ("Quality planning","An approved reference sample; coffee wood follows a "+QC_PROTOCOL+".","/quality-control/"),
            ("Brand development","Labels, packaging and specification-led OEM/ODM.","/capabilities/")])+
            p("Production, quality and export roles should be identified in your project conversation. We do not publish named technical reviewers or credentials that have not been confirmed.")),
         section("A clearer first conversation",p("Tell us your sales channel and destination before choosing a pack. An Amazon launch, a distributor assortment and a retail-chain rollout can require different carton configurations, warning language, documents and lead-time planning.")+
            p('<a href="/solutions/">Find your buyer solution</a> or <a href="/how-to-order/">review how a first order works</a>.'),True)],
         active="Company",image="/assets/img/process-raw-sticks.jpg")
