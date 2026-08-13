# -*- coding: utf-8 -*-
from common import page, write_page, rfq_bar, breadcrumb_html, BRAND, COUNTRIES, CAPACITY

def faq_schema(pairs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}
def faq_html(pairs):
    items = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in pairs)
    return f'<section class="section"><div class="wrap"><h2>Frequently asked questions</h2>{items}</div></section>'

def solution_page(root, slug, tag, h1, meta_title, meta_desc, lede, pain_points, solutions, extra_section, faqs, hero_img):
    bc, bc_s = breadcrumb_html([("Home","/"), ("Solutions","/solutions/"), (h1, None)])
    pp = "".join(f"<li>{p}</li>" for p in pain_points)
    sol = "".join(f'<div class="card"><h3>{s[0]}</h3><p>{s[1]}</p></div>' for s in solutions)
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap hero-inner">
    <div>
      <p class="hero-eyebrow">Solutions for {tag}</p>
      <h1>{h1}</h1>
      <p class="hero-lede">{lede}</p>
      <div class="hero-ctas"><a class="btn btn-primary" href="/request-a-quote/">Talk to Us</a></div>
    </div>
    <img src="{hero_img}" alt="{h1}">
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>What we hear from {tag.lower()}</h2>
    <ul class="check-list">{pp}</ul>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>How {BRAND} solves it</h2>
    <div class="grid grid-2">{sol}</div>
  </div>
</section>
{extra_section}
"""
    html = page(meta_title, meta_desc, f"/solutions/{slug}/", content + faq_html(faqs) + rfq_bar(), "Solutions",
                [bc_s, faq_schema(faqs)], og_image=hero_img)
    write_page(root, f"/solutions/{slug}/", html)


def build(root):
    # ---------- HUB ----------
    bc, bc_s = breadcrumb_html([("Home","/"), ("Solutions", None)])
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">Solutions</p>
    <h1>Built Around How You Actually Buy</h1>
    <p class="hero-lede">We work with four kinds of buyers, and each has a different first question. Find yours below.</p>
  </div>
</section>
<section class="section">
  <div class="wrap grid grid-4">
    <div class="card"><h3>Startup Brands</h3><p>Low MOQ, branding help, and a way to test without tying up capital.</p><a href="/solutions/startup-brands/">Read more &rarr;</a></div>
    <div class="card"><h3>Amazon Sellers</h3><p>FBA-ready logistics, listing differentiation, and AOV strategy.</p><a href="/solutions/amazon-sellers/">Read more &rarr;</a></div>
    <div class="card"><h3>Eco Pet Shops (EU)</h3><p>Plastic-free materials, storytelling, and EVFTA documentation.</p><a href="/solutions/eco-pet-shops/">Read more &rarr;</a></div>
    <div class="card"><h3>Wholesalers &amp; Distributors</h3><p>Volume capacity, tiered pricing, and batch-to-batch consistency.</p><a href="/solutions/wholesalers/">Read more &rarr;</a></div>
  </div>
</section>
"""
    html = page(f"Solutions for Pet Product Buyers | {BRAND}",
        "How VietPaw solves sourcing for startup brands, Amazon sellers, EU eco pet shops, and wholesalers — natural pet toys manufactured in Vietnam.",
        "/solutions/", content + rfq_bar(), "Solutions", [bc_s])
    write_page(root, "/solutions/", html)

    # ---------- STARTUP BRANDS ----------
    solution_page(root, "startup-brands", "Startup Brands", "Launch a Natural Pet Toy Line Without Tying Up Capital",
        f"Solutions for Startup Pet Brands | Low MOQ & Branding | {BRAND}",
        "Low MOQ, sample support and full branding help for startup pet brands sourcing natural toys from Vietnam.",
        "High growth potential, limited capital, and one shot at a first impression. We built our offer so you can test the market before you commit real money.",
        ["Large supplier MOQs bury cash in inventory before you know if a product sells.",
         "No in-house brand identity — logo, label and packaging all need to be built from zero.",
         "Fear of testing the wrong product with no sales content to back a launch.",
         "Unclear which material or format will actually differentiate your shop."],
        [("Flexible, low MOQ", "MOQ starts at 50 pcs per SKU, with a Trial Box of 3–5 free samples — you pay shipping only, refunded on your first order."),
         ("Full branding support", "Laser logo engraving, custom kraft labels, and packaging concept suggestions, so a first-time brand looks retail-ready."),
         ("Free media assets included", "A complete set of product images ships with your Offer Box, so you're not starting your listing or shop page from zero."),
         ("Full export documentation", "Certificate of Origin, Phytosanitary and Fumigation certificates handled for you, so customs isn't the thing that stalls your launch.")],
        f"""
<section class="section">
  <div class="wrap">
    <h2>Offer Box: Start-Up</h2>
    <table>
      <tr><th>MOQ</th><td>50 pcs, packaged neatly in one carton</td></tr>
      <tr><th>Free packaging</th><td>Printed product information and tags</td></tr>
      <tr><th>Free media</th><td>A set of high-resolution product images for your listing or shop</td></tr>
    </table>
  </div>
</section>""",
        [("Do I need a design team to start?", "No — our packaging concepts and free product images are built for brands with no in-house design resources yet."),
         ("What if my first product doesn't sell?", "Because MOQ is low, a wrong first bet costs far less than a typical large-MOQ supplier order. Many brands pilot with a single SKU before expanding."),
         ("Which material should I start with?", "Coffee wood is our most requested first SKU because of its single-ingredient safety story and strong margins; talk to us about your target customer for a tailored recommendation.")],
        "/assets/img/dog-lifestyle-chew-1.jpg")

    # ---------- AMAZON SELLERS ----------
    solution_page(root, "amazon-sellers", "Amazon Sellers", "A Natural Product Line Built for FBA and AOV",
        f"Solutions for Amazon Sellers | Natural Pet Toys, FBA-Ready | {BRAND}",
        "Reliable supply, FBA-compliant labeling, and AOV strategy for Amazon sellers sourcing natural pet toys from Vietnam.",
        "You already know low rankings and unstable traffic are a supply problem as much as a marketing one. Here's how we help you stand out and protect margin.",
        ["Generic dog chew/toy listings blend together — hard to earn a premium price.",
         "FBA fees, storage fees and ad costs (minimum 15% / $0.30 per item on pet products) squeeze margin.",
         "High financial risk in testing a new SKU, with real fear of 1-star reviews from cracking, mold or wrong sizing.",
         "Strict FBA requirements — barcode, warning label, carton marking — that a new supplier can get wrong.",
         "Sales volume that outgrows what a small supplier can consistently produce."],
        [("A differentiated natural line", "Coffee wood, coconut fiber and hemp fiber combine into unique multi-material toy boxes your competitors selling generic chews can't easily copy."),
         ("FBA-ready packaging", "Barcode and warning-label compliance built into your OEM run, plus direct-to-FBA forwarding so you skip an extra logistics step."),
         ("QC that protects your rating", "Vacuum sealing, moisture control and five-stage inspection reduce the mold/cracking/sizing issues that drive 1-star reviews."),
         ("A 1-for-1 replacement policy", "If a shipment does have a defect, we replace it — so your listing doesn't carry that quality risk alone.")],
        f"""
<section class="section">
  <div class="wrap">
    <h2>What our own AOV data shows</h2>
    <p>We tracked order volume and average order value (AOV) across single items, 2-packs and combo/gift boxes for a coffee wood chew SKU. The pattern is consistent with what we see across sellers:</p>
    <table>
      <tr><th>Format</th><th>Orders</th><th>AOV</th><th>Role</th></tr>
      <tr><td>Single item</td><td>Highest (677 orders)</td><td>$15.09</td><td>Entry product — low price, low friction, drives new-customer trial</td></tr>
      <tr><td>Set of 2</td><td>Lowest (28 orders)</td><td>$28.20</td><td>Weak value proposition — only ~6.5% saving per unit, not enough to beat "just buy one to try"</td></tr>
      <tr><td>Combo / toy box</td><td>High value (100 orders)</td><td>$83.96</td><td>Revenue driver — 5.5x the AOV of a single item, with gift-like presentation</td></tr>
    </table>
    <p>Our recommendation: use single items as your traffic-driving entry SKU, skip the weak middle tier, and build a combo/gift box mixing coffee wood, coconut fiber and hemp fiber to lift AOV and offset ad costs.</p>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>Amazon Starter Pack</h2>
    <p>Laser-logo engraving, private label, FBA-compliant barcode and warning labels, and a Trial Box of 3–5 free samples — built specifically for sellers testing a new listing. <a href="/capabilities/">See full OEM capabilities &rarr;</a></p>
  </div>
</section>""",
        [("Can you ship directly to Amazon FBA warehouses?", "Yes — we work with forwarders already routing to FBA, including dedicated EU lanes and Asia express lanes."),
         ("Do you handle FBA barcode and warning label requirements?", "Yes, these are built into OEM/private label runs so your inventory arrives FBA-compliant."),
         ("What if my inventory needs exceed a small supplier's capacity?", "Our factories produce 5–6 million units a year across three sites, so we can scale with a growing listing."),
         ("How do you help with negative review risk?", "Five-stage QC, vacuum sealing and moisture control on wood products reduce the mold/cracking/sizing issues that drive 1-star reviews, backed by a 1-for-1 replacement policy.")],
        "/assets/img/warehouse-winvn-boxes.jpg")

    # ---------- ECO PET SHOPS EU ----------
    solution_page(root, "eco-pet-shops", "Eco Pet Shops in the EU", "Genuinely Plastic-Free Stock, With the Story to Back It",
        f"Solutions for Eco Pet Shops (EU) | Plastic-Free Wholesale | {BRAND}",
        "Plastic-free, chemical-free pet toys with transparent sourcing stories and EVFTA documentation for EU eco pet retailers.",
        "EU pet owners are demanding about animal health and environmental impact, and they're willing to pay for products that back that up. Generic or unverifiable \"eco\" stock doesn't cut it on your shelf.",
        ["Reluctance to stock generic plastic toys that contradict an eco-positioned shop.",
         "Need for a transparent, verifiable sourcing story to display in-store and use with customers.",
         "Requirement for chemical-free materials and a distinct concept per shop, not a copy-paste import.",
         "Uncertainty about import documentation and tariff exposure on natural goods from outside the EU."],
        [("Genuinely upcycled materials", "Coconut fiber, hemp fiber, coffee wood and loofah, all by-products of existing agriculture — not virgin material dressed up as eco."),
         ("Kraft and biodegradable packaging as standard", "Kraft tags, kraft boxes and biodegradable packaging options, with custom labelling per shop concept."),
         ("A story you can tell in-store", "Sourcing rooted in Vietnam's Central Highlands, supporting local farming communities including ethnic minority households who help process raw material."),
         ("EUR1 Certificate of Origin", "Provided under the EU–Vietnam Free Trade Agreement (EVFTA), helping you prove origin and reduce import tariffs.")],
        f"""
<section class="section">
  <div class="wrap">
    <h2>Reducing plastic beyond the toy itself</h2>
    <p>We've replaced synthetic silica gel desiccant packets with natural charcoal for moisture absorption in shipments — a small detail, but one that matters to buyers auditing an entire supply chain for plastic, not just the product on the shelf.</p>
  </div>
</section>""",
        [("Can you provide EUR1 Certificate of Origin for EVFTA?", "Yes, on every order, alongside Phytosanitary and Fumigation certificates."),
         ("Are your materials genuinely chemical-free?", "Yes — single-ingredient natural materials with no added chemicals, flavourings or synthetic treatments."),
         ("Can each shop get a distinct packaging concept?", "Yes — kraft labelling, tags and box concepts can be tailored per shop, not sold as one generic import.")],
        "/assets/img/raw-loofah-gourd.jpg")

    # ---------- WHOLESALERS ----------
    solution_page(root, "wholesalers", "Wholesalers & Distributors", "Volume Capacity Without Sacrificing Consistency",
        f"Solutions for Wholesalers & Distributors | {BRAND}",
        "Stable supply, volume-tiered pricing and batch-to-batch consistency for wholesale distributors of natural pet toys.",
        "Stockouts during peak season and inconsistent batches are what actually break distribution relationships — not price. Here's our production capacity and QC process in plain numbers.",
        ["Fear of supply instability disrupting distribution during peak season.",
         "Need for volume-tiered pricing to protect wholesale/reseller margins.",
         "Concern over batch-to-batch inconsistency — size, moisture, cleanliness.",
         "Need to verify a supplier's real production capacity and export documentation before committing volume."],
        [(f"Real manufacturing scale", f"{CAPACITY} across three factories (Gia Lai, Dak Lak, Ho Chi Minh City) plus warehousing in Linh Trung, Long An and Binh Duong."),
         ("Volume-tiered pricing", "EXW and EWX pricing tiers at MOQ 50, 500, 5,000 and 50,000 pcs, so margin improves as your order scales."),
         ("Standardised, published QC", "Five-stage inspection — raw material, in-process, semi-finished, final product, pre-shipment — with size sorting and vacuum sealing at every stage."),
         ("Full export documentation", "Certificate of Origin, Phytosanitary, Fumigation, Invoice, Packing List and Forest Product Declaration on every shipment.")],
        f"""
<section class="section">
  <div class="wrap">
    <h2>Volume pricing tiers</h2>
    <table>
      <tr><th>Tier</th><th>MOQ</th><th>Pricing basis</th></tr>
      <tr><td>Pilot</td><td>50 pcs</td><td>EXW price per piece</td></tr>
      <tr><td>Standard</td><td>500 pcs</td><td>EXW price per piece</td></tr>
      <tr><td>Distribution</td><td>5,000 pcs</td><td>EWX price per piece</td></tr>
      <tr><td>Master distribution</td><td>50,000 pcs</td><td>EWX price per piece</td></tr>
    </table>
    <p class="small">Exact pricing is quoted per SKU and material mix — request a quote for a tiered price sheet.</p>
  </div>
</section>""",
        [("What's your annual production capacity?", "5–6 million units per year across three factories."),
         ("How do you keep batches consistent?", "Standardised QC at five stages, including size sorting, moisture control and vacuum sealing, with published process documentation."),
         ("Can pricing scale with volume?", "Yes — EXW and EWX pricing tiers apply at 50, 500, 5,000 and 50,000 pcs MOQ."),
         ("Do you provide all export documentation for customs?", "Yes — CO, Phytosanitary, Fumigation, Invoice, Packing List and Forest Product Declaration on every shipment.")],
        "/assets/img/export-packed-box.jpg")
