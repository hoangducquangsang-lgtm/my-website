# -*- coding: utf-8 -*-
from common import (BRAND, BRAND_INTRO, CONTRACT_NOTICE, ADDRESS, PHONE, EMAIL, BASE_URL,
                   REGISTRATION_DATE, COUNTRIES, SITES, page, write_page, organization_schema, social_html)
from content_helpers import (hero, section, cards, p, ul, table, faq, rfq_bar, trust_links, publish,
                             INCOTERMS, PAYMENT, CAFFEINE, SIZE_ADVICE, ORDER_TIERS,
                             answer, fit, steps, spec_table, figure, media,
                             SAMPLES, SAMPLE_DISPATCH, PRIVATE_LABEL, QC_PROTOCOL, RANGE_SCOPE, LEAD,
                             CARTON, SEA_TRANSIT, SAFETY)
from content_products import product_cards

IMG = "/assets/img/"

HOME_LEDE = ("Coffee wood, coconut fiber, hemp and loofah, manufactured in our own three factories in Vietnam for brands, "
             "wholesalers and retailers. Published specifications, five QC checkpoints, stock held in our "
             "warehouse, and standard products from 50 pcs per SKU.")

def home(root):
    content = hero("Wholesale Natural Pet Toys, Specified Before You Buy", HOME_LEDE,
        eyebrow="VietPaw \u00b7 Natural pet toys from Vietnam",
        image=IMG+"golden-retriever-chewing-coffee-wood-chew-floor.jpg")

    content += section("What VietPaw supplies",
        answer("VietPaw manufactures and exports natural-material pet toys from Vietnam: coffee wood chews, "
               "coconut fiber balls, hemp rope toys and loofah cat shapes. We manufacture ourselves in three "
               "factories \u2014 Dak Lak, Gia Lai and Binh Duong \u2014 with a capacity of 100,000 pieces a month, hold standard sizes in our Ho Chi Minh City warehouse, and ship on our own "
               "export documents. Sell wholesale from stock, add your branding under private label, or develop a "
               "new construction under OEM/ODM. Standard products start at 50 pcs per SKU; private-label "
               "packaging starts at 500 pcs.")
        + '<div class="stats">'
          '<div><strong>4</strong><span>Natural materials</span></div>'
          '<div><strong>50 pcs</strong><span>Starting MOQ, selected SKUs</span></div>'
          '<div><strong>&lt;14%</strong><span>Coffee wood moisture at packing</span></div>'
          '<div><strong>5</strong><span>QC checkpoints, stem to carton</span></div>'
          '</div>'
        + p("Most sourcing pages in this category lead with adjectives. We would rather lead with the numbers "
            "a buyer actually has to check: what size, at what moisture, in what carton, with which documents. "
            "Everything below is the reference specification \u2014 your approved sample and quotation are what "
            "the order is held to."))

    content += section("Four materials, four different conversations", cards([
        ("Coffee wood", "Seasoned Robusta stem, six graded sizes, packed below 14% moisture. The hard-chew line.",
         "/collections/coffee-wood/", IMG+"vietpaw-coffee-wood-sizes.png"),
        ("Coconut fiber", "Coir from the husk, wound into textured balls. Specified by sample and weight, not by catalogue number.",
         "/collections/coconut-fiber/", IMG+"coconut-fiber-ball-top-view.jpg"),
        ("Hemp fiber", "Wound balls, knotted tug rope and wood-and-rope constructions. Specified by geometry and knot.",
         "/collections/hemp-fiber/", IMG+"hemp-rope-toy-assortment.jpg"),
        ("Loofah", "Dried gourd fiber cut into light cat-play shapes. Dimensions confirmed per shape.",
         "/collections/loofah/", IMG+"loofah-duck-cat-toy.jpg")], 4)
        + p(RANGE_SCOPE), True)

    content += section("The specification, up front",
        p("Coffee wood is our most-specified line, so here is the short version. The full table \u2014 with "
          "diameters, weights and carton counts \u2014 sits on the "
          '<a href="/products/coffee-wood-dog-chew/">product page</a>.')
        + spec_table(["Size", "Length", "Weight", "Reference dog weight", "Pcs per export carton"], [
            ("XS", "10 cm", "23\u201330 g", "Up to 3 kg", "On request"),
            ("S", "13\u201314 cm", "35\u201345 g", "3\u20135 kg", "512"),
            ("M", "17\u201318 cm", "90\u2013110 g", "5\u20138 kg", "224"),
            ("L", "19\u201320 cm", "120\u2013180 g", "8\u201312 kg", "126"),
            ("XL", "21\u201322 cm", "230\u2013310 g", "12\u201320 kg", "85"),
            ("XXL", "22\u201323 cm", "340\u2013440 g", "20 kg and over", "On request"),
          ], caption="Reference figures for bulk-packed sticks. Coffee wood is a natural material and mass varies "
                     "within each band; dog weight is a starting point for choosing a size, not a veterinary "
                     "assessment. Retail-packed sets fit fewer units per carton.")
        + p(SIZE_ADVICE)
        + p(CARTON))

    content += section("What our factory actually controls",
        media(ul([
            "<strong>Moisture below 14% at packing.</strong> Pin-type meter reading, photographed per batch, taken again before the container is sealed.",
            "<strong>\u00b13 mm length tolerance</strong> on the coffee wood stick line. Diameter follows the natural stem and is controlled by grading into bands.",
            "<strong>Any cracked piece rejected</strong> at grading, checked piece by piece rather than on a sampled average.",
            "<strong>Roughly one piece in five rejected</strong> across the whole process, concentrated at the drying racks \u2014 an figure from our own production records that explains why lead time follows graded output.",
            "<strong>Five checkpoints</strong> between raw stem and sealed carton: intake, after seasoning, after shaping, at grading, and at the packing bench.",
          ]),
          IMG+"moisture-reading-before-packing.jpg",
          "Pin-type moisture meter held against a coffee wood chew stick above a packing carton",
          "The moisture reading is filed against the lot. Ask for the one attached to your order.")
        + p('Drying temperatures, cycle times and the stage sequence are treated as proprietary and are not '
            'published \u2014 by us or by our factory. What you can verify instead is the output: '
            '<a href="/quality-control/">the QC protocol</a>, '
            '<a href="/certifications/">the document scope</a>, and a third-party inspection that witnesses the '
            'moisture reading and the container stuffing before the doors close.'), True)

    content += section("How you buy from here", cards([
        ("Wholesale", "Order an approved standard specification. Fastest route to a first shipment.",
         "/services/wholesale-pet-products/"),
        ("Private label", "An approved design with your engraving, tags, labels or printed box.",
         "/services/private-label-pet-toys/"),
        ("OEM / ODM", "A new construction from your drawing or brief, through feasibility and prototype.",
         "/services/oem-odm-pet-toy-manufacturing/")])
        + steps([
            ("Send the brief",
             "Name the product, quantity per SKU, destination country and any branding requirement.",
             "A quote that can actually be compared against another supplier\u2019s."),
            ("Approve a sample",
             "Measure it, keep one piece as your retained reference, and confirm packaging at the same time.",
             "A physical standard a later delivery can be checked against.",
             "Three free samples; you cover courier. Standard samples dispatch within one working day once the selection and courier are confirmed."),
            ("Confirm terms and documents",
             "Fix the Incoterm with its named place, the carton data and the certificate list your customs entry needs.",
             "A shipment booked with its paperwork rather than chasing it after arrival."),
          ])
        + p(LEAD) + p('<a href="/how-to-order/">The full ordering process</a>.'))

    content += section("Built for how your business buys", cards([
        ("Amazon sellers", "Pack dimensions, barcode artwork and marketplace preparation.", "/solutions/amazon-sellers/"),
        ("Wholesalers & distributors", "Mixed-SKU orders, reorder specifications and rolling demand.", "/solutions/wholesalers/"),
        ("Pet brands", "Product development, change control and brand-specific packaging.", "/solutions/pet-brands/"),
        ("Retail chains", "Vendor onboarding, carton consistency and phased store launches.", "/solutions/retail-chains/"),
        ("Startup brands", "Small pilot orders and a manageable first-product brief.", "/solutions/startup-brands/"),
        ("Eco pet shops", "Specific material stories and carefully qualified packaging claims.", "/solutions/eco-pet-shops/")]), True)

    content += section("What we will not claim",
        p("It is worth being direct about this, because the claims below are common in our category and none of "
          "them can currently be supported for these products.")
        + spec_table(["Claim you will see elsewhere", "Our position"], [
            ("\u201cSplinter-free\u201d", "No supplier has published test data supporting it, and an independent trainer has documented a coffee wood stick breaking into hard pieces in use. We do not print it."),
            ("Cleans teeth / dental benefit", "No product-specific evidence exists, so we make no dental claim."),
            ("Digestible or edible", "These are toys, not food. Nothing here is digestible."),
            ("Biodegradable / compostable", "The toy, the bag, the box and any ink would all need evidence under stated disposal conditions. We publish no such claim."),
            ("Certified pet-safe", "There is no universal pet-safety certification. Test reports have a defined scope; ask for the one that covers your SKU and destination."),
          ], caption="Coffee wood and coconut husk do have honest material-reuse stories \u2014 both are by-products of "
                     "existing agriculture. That is a claim we will stand behind, and it is different from a "
                     "biodegradability claim.")
        + p(SAFETY)
        + p('Our <a href="/sustainability/">material and packaging approach</a> sets out where the line sits before '
            'you print environmental language.'))

    content += section("Specifications before purchase",
        product_cards(["coffee-wood-dog-chew", "coconut-fiber-dog-ball", "loofah-cat-toy"]), True)

    content += faq([
        ("What is the minimum order quantity?",
         "Selected standard SKUs start at 50 pcs. Laser engraving on suitable coffee wood surfaces also starts at 50 pcs. "
         "Private-label runs and custom hang tags, labels or printed boxes start at 500 pcs per SKU. The two minimums are "
         "separate, so a small engraved trial before committing to printed packaging is possible."),
        ("How long does production take?",
         "5\u20137 days for stock packaging, because standard sizes are held in our warehouse rather than made to order. "
         "60\u201380 days when the order carries your own label, printed box or engraving \u2014 most of that window is artwork "
         "approval and tooling, not production. Production time is not an arrival date: add roughly 30\u201335 days port to "
         "port for the EU or the US, plus clearance and inland legs."),
        ("Can I get samples before ordering?",
         "Three free samples, with the courier at your cost. Standard samples dispatch within one working day once the "
         "selection and courier arrangements are confirmed; custom prototypes are quoted separately on timing."),
        ("How do I verify our factory and the product?",
         "Ask for current location information, a production walkthrough, and the reports that cover your SKU and destination. "
         "For a shipment that matters, appoint a third party to witness the moisture reading, measure a sample, photograph the "
         "carton marks against the packing list and witness stuffing before the container is sealed. A supplier\u2019s general "
         "description is not order-specific evidence."),
        ("Which documents come with a shipment?",
         "Certificate of Origin, fumigation certificate, phytosanitary certificate, packing list, commercial invoice and bill of "
         "lading, subject to destination requirements. Batch moisture readings on request. Phytosanitary and fumigation "
         "certificates are issued per shipment and cannot be produced retrospectively \u2014 list them at booking."),
        ("Are these toys suitable for every pet?",
         "No. Size, construction and chewing style all matter \u2014 strong chewers belong on our thicker Gorilla line. "
         "These are supervised-play toys, not food. Each material page sets out where it fits and "
         "where it does not."),
      ])

    content += rfq_bar("Tell us the product, the destination and the first-order quantity.", "Request Samples & a Quote")
    schemas = [organization_schema(),
               {"@context": "https://schema.org", "@type": "WebSite", "@id": BASE_URL+"/#website", "name": BRAND, "url": BASE_URL+"/"}]
    write_page(root, "/", page(
        "Wholesale Natural Pet Toys from Vietnam | Specs & Private Label | VietPaw",
        "Coffee wood, coconut fiber, hemp and loofah pet toys made in Vietnam. Published sizes and carton data, "
        "moisture below 14%, five QC checkpoints. Wholesale, private label and OEM/ODM from 50 pcs.",
        "/", content, schemas=schemas, og_image=IMG+"golden-retriever-chewing-coffee-wood-chew-floor.jpg"))


def about(root):
    sections = [
      section("Who VietPaw is",
        answer("VietPaw is a Vietnamese manufacturer and exporter of natural-material pet toys. We make coffee "
               "wood chews, coconut fiber balls, hemp rope toys and loofah cat shapes ourselves, in our own three "
               "factories in Dak Lak, Gia Lai and Binh Duong, hold standard sizes in our warehouse in Ho Chi Minh City, and ship on our own "
               "export documents. Orders go from our stock or our line straight to your container — there is no "
               "trading layer in between.")
        + p("That matters for three practical reasons. Stock sizes ship in 5\u20137 days because they are already "
            "packed, not because we are chasing another factory. Quality decisions \u2014 what counts as a rejectable "
            "crack, what moisture we pack at \u2014 are ours to make and ours to change for your order. And when you "
            "want to verify something, you are asking the people who ran the line rather than a middleman relaying "
            "your question.")
        + p("What we will not do is overclaim. Most of what gets printed in this category \u2014 splinter-free, dental "
            "benefits, certified biodegradable \u2014 has no evidence behind it, and a buyer who prints it inherits "
            "the risk. We would rather lose a sale than hand you a claim that fails.")),

      section("Our three factories",
        p("We manufacture everything we sell ourselves, in three factories we operate in Vietnam: Dak Lak and Gia "
          "Lai in the Central Highlands, close to where the coffee wood is collected, and Binh Duong in the south. "
          "Packing, quality release and export documentation run from our Ho Chi Minh City office and warehouse.")
        + spec_table(["Site", "Location"], SITES,
            caption="Buyer-arranged visits and third-party inspection are welcome at any site; please arrange in "
                    "advance so the line is running when you arrive. Loading port is Cat Lai, Ho Chi Minh City.")
        + p("<strong>Production capacity: 100,000 pieces a month</strong> across our three factories. Volume and "
            "dates for your order are confirmed in your quotation.")),

      section("What we do and do not do",
        fit(["Specifying a product properly before the first order, including the components a photograph does not show.",
             "Wholesale from approved standard specifications across four materials.",
             "Private label \u2014 engraving from 50 pcs, printed packaging from 500 pcs per SKU.",
             "OEM/ODM development from a drawing or brief, through feasibility and prototype.",
             "Export documentation, carton planning and the moisture records that come with a wood shipment."],
            ["We do not claim certifications we do not hold, or present planning figures as audited output.",
             "We do not publish biodegradability, dental-health, digestibility or \u201csplinter-free\u201d claims.",
             "We do not quote a chew lifespan in days or weeks; the dog sets that, not the material."],
            suit_head="We do this", less_head="We do not do this"),
        True),

      section("The materials, and where they come from",
        media(p("Coffee wood comes from mature Robusta stems in Vietnam\u2019s Central Highlands \u2014 Dak Lak, Gia Lai "
                "and Dak Nong. Growers take out the trees that have stopped paying their way and leave the rest "
                "alone, so these stems already existed and previously went to firewood; nobody fells a coffee tree "
                "that is still yielding cherries. Stems are cut to billets of roughly 50 to 70 cm in the field, then "
                "held about a year in ventilated shade before anything is machined.")
              + p("Coconut fiber is coir from the husk, itself a by-product of the coconut food and oil trade. "
                  "Loofah is the dried fibrous interior of a gourd, grown on vines and peeled by hand. Hemp is a "
                  "bast fiber spun into cord.")
              + p("Two of those four \u2014 coffee wood and coconut husk \u2014 have a genuine material-reuse story we are "
                  "happy to put in writing. Hemp and loofah are plant-derived but are grown as crops, and we do "
                  "not describe them as agricultural waste."),
              IMG+"loofah-gourd-on-the-vine.jpg",
              "A green loofah gourd hanging from its vine against foliage",
              "Loofah on the vine. Grown as a crop \u2014 which is why we do not call it agricultural waste.")),

      section("Brand, company and sales contact",
        table(["Role", "Information"], [
          ("Website / site name", BRAND),
          ("Business", "Manufacturer and exporter, natural-material pet toys"),
          ("Factories", "Own factories in Dak Lak, Gia Lai and Binh Duong"),
          ("Production capacity", "100,000 pcs/month"),
          ("Producing since", REGISTRATION_DATE),
          ("Export markets", COUNTRIES+" countries"),
          ("Port of loading", "Cat Lai, Ho Chi Minh City"),
          ("VietPaw sales email", EMAIL),
          ("VietPaw sales phone", PHONE),
          ("Head office and warehouse", ADDRESS)])
        + p(CONTRACT_NOTICE)
        + p("Ask us for the registration details, company records and shipment documents that apply to your "
            "order before you contract. If a supplier \u2014 us included \u2014 will not put that in front of you, that "
            "is the answer to your question."), True),

      section("How we handle evidence",
        steps([
          ("We separate the reference from the record",
           "Everything published here is a reference specification; the record is the moisture reading, the grading result and the carton marks filed against your lot.",
           "You check the record, not the brochure."),
          ("We say when a figure is internally reported",
           "Reject rate and process figures come from our own production records, not audited measurements.",
           "You can weight them accordingly instead of treating them as verified."),
          ("We say when nothing exists",
           "There is no hardness figure for coffee wood, no tensile rating for these rope toys and no published chew lifespan.",
           "You do not build a listing on a number that was invented for marketing."),
          ("We support independent verification",
           "Third-party inspection can witness the moisture reading, measure a sample, photograph carton marks against the packing list and witness stuffing.",
           "Evidence that does not depend on trusting us."),
        ])
        + trust_links()),

      section("What we support", cards([
        ("Manufacturing review", "Locations, process and a capacity discussion for your SKU mix.", "/factory/"),
        ("Quality planning", "An approved reference sample; coffee wood follows a "+QC_PROTOCOL+".", "/quality-control/"),
        ("Brand development", "Labels, packaging and specification-led OEM/ODM.", "/capabilities/")])
        + p("Tell us your sales channel and destination before choosing a pack format. An Amazon launch, a "
            "distributor assortment and a retail-chain rollout need different carton configurations, warning "
            "language, documents and lead-time planning.")
        + p('<a href="/solutions/">Find your buyer solution</a> or '
            '<a href="/how-to-order/">review how a first order works</a>.'), True),
    ]
    publish(root, "/about/", "About VietPaw | Natural Pet Toy Supplier in Vietnam",
        "Who VietPaw is, what we specify, where the materials come from and which claims we will not make. "
        "Natural pet toys from Vietnam for wholesale, private label and OEM/ODM.",
        "About VietPaw",
        "A Vietnamese manufacturer and exporter of natural-material pet toys \u2014 how we produce, "
        "what we will not claim, and where you can come and look.",
        sections, active="Company", image=IMG+"coffee-wood-workshop-stacked-billets.jpg",
        faqs=[
          ("Does VietPaw manufacture its own products?",
           "Yes. We manufacture ourselves, in our own three factories in Dak Lak, Gia Lai and Binh Duong, with a "
           "production capacity of 100,000 pieces a month. There is no trading layer: the factory that makes your order "
           "is ours, and you are welcome to visit or send an inspector."),
          ("How long have you been exporting?",
           "The company has been registered in Vietnam since "+REGISTRATION_DATE+" and now ships to "+COUNTRIES+" countries. "
           "Country count is our own record rather than an audited figure, and we present it as such."),
          ("Can I visit our factory or send an inspector?",
           "Yes. Buyer-arranged inspection is welcome, and for a shipment that matters we would encourage it: a third party can "
           "witness the moisture reading, measure a sample, photograph carton marks against the packing list and witness "
           "stuffing before the container is sealed."),
          ("Why does the site carry so many caveats?",
           "Because the alternative is a listing you cannot defend. Most of what gets overclaimed in this category \u2014 "
           "splinter-free, dental benefits, biodegradability, certified pet-safe \u2014 has no evidence behind it, and a buyer who "
           "prints it inherits the risk. We would rather lose a sale than hand you a claim that fails."),
          ("Do you sell direct to consumers?",
           "No. VietPaw is business-to-business: wholesale, private label and OEM/ODM for brands, distributors, retailers and "
           "marketplace sellers."),
        ])


def build(root):
    home(root)
    about(root)
