# -*- coding: utf-8 -*-
from common import page, write_page, rfq_bar, breadcrumb_html, BRAND, LEGAL_NAME, PHONE, PHONE_TEL, EMAIL, ADDRESS, FOUNDED, COUNTRIES, CAPACITY

def faq_schema(pairs):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs
        ]
    }

def faq_html(pairs, heading="Frequently asked questions"):
    items = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in pairs)
    return f'<section class="section"><div class="wrap"><h2>{heading}</h2>{items}</div></section>'


def build(root):
    # ---------------- CAPABILITIES ----------------
    bc, bc_s = breadcrumb_html([("Home","/"), ("Capabilities (OEM/ODM)", None)])
    faqs = [
        ("What is the minimum order for private label?", "From 50 pcs per SKU. We keep it low so you can pilot a product before scaling to bulk."),
        ("How fast can I get a branded sample?", "Samples are typically ready within about 7 days, and prototypes for custom designs within a few days of confirming the brief."),
        ("Do you charge extra for OEM service?", "No extra service fees apply when you use our standard packaging. Custom packaging and special finishes are quoted per project."),
        ("Which products can be private-labelled?", "All of our natural lines — coffee wood chews, coconut fiber, hemp fiber and loofah toys."),
    ]
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">OEM &middot; ODM &middot; Private Label</p>
    <h1>Your Brand, Our Craft</h1>
    <p class="hero-lede">Whether you're launching your first collection or adding a natural line to an established range, we make it simple to put your brand on genuinely sustainable pet toys &mdash; with a low minimum, fast samples, and a design team that does the heavy lifting.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="/request-a-quote/">Start a Private-Label Project</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap grid grid-2">
    <div>
      <h2 class="mt0">What we can customise</h2>
      <ul class="check-list">
        <li>Logo &amp; labelling &mdash; your brand, front and centre</li>
        <li>Packaging design &mdash; vacuum, kraft, and fully biodegradable options</li>
        <li>Laser engraving &mdash; your logo cut directly into coffee wood products</li>
        <li>Product shape &amp; size &mdash; co-develop formats exclusive to your shop</li>
        <li>Materials mix &mdash; coffee wood, coconut fiber, hemp fiber and loofah</li>
      </ul>
      <p>No extra service fees apply when you use our standard packaging, and our design team can turn around a ready-to-test prototype within a few days.</p>
    </div>
    <img src="/assets/img/process-laser-engraving.jpg" alt="Laser engraving a custom logo onto a coffee wood chew">
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>Amazon Starter Pack</h2>
    <p>Built specifically for Amazon sellers: laser-logo engraving, private label, barcode &amp; FBA-compliant warning labels, and a Trial Box of 3&ndash;5 free samples (you cover shipping, refunded on your first order). Our own AOV data shows single-item SKUs drive new-customer trial while multi-product combo/gift boxes lift average order value several times over &mdash; we help you structure both.</p>
    <a class="btn btn-outline" href="/solutions/amazon-sellers/">See the Amazon Seller playbook &rarr;</a>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>How a private-label project runs</h2>
    <ol class="steps" style="max-width:640px">
      <li><strong>Tell us your idea</strong> &mdash; product, materials, brand direction</li>
      <li><strong>Free sample &amp; prototype</strong> &mdash; approve the real thing before you buy</li>
      <li><strong>Confirm the run</strong> &mdash; sizes, packaging, engraving, quantities</li>
      <li><strong>Production</strong> &mdash; 25&ndash;30 working days for OEM/ODM orders</li>
      <li><strong>Export &amp; delivery</strong> &mdash; full documentation, worldwide shipping</li>
    </ol>
  </div>
</section>
"""
    html = page(f"OEM & Private Label Pet Toys | Low MOQ | {BRAND}",
        f"OEM/ODM and private-label service for natural pet toys from Vietnam. Custom logos, packaging, laser engraving, low MOQ from 50 pcs.",
        "/capabilities/", content + faq_html(faqs) + rfq_bar(), "Company", [bc_s, faq_schema(faqs)])
    write_page(root, "/capabilities/", html)

    # ---------------- MATERIALS HUB ----------------
    bc, bc_s = breadcrumb_html([("Home","/"), ("Our Materials", None)])
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">Our Materials</p>
    <h1>Coffee Wood, Coconut Fiber, Hemp Fiber &amp; Loofah</h1>
    <p class="hero-lede">Four natural materials sourced and processed in Vietnam, each chosen because it's renewable, biodegradable, and tells a story your customers want to be part of.</p>
  </div>
</section>
<section class="section">
  <div class="wrap grid grid-2">
    <div class="card">
      <img src="/assets/img/product-coffeewood-single.jpg" alt="Coffee wood chew stick" style="margin-bottom:16px">
      <h3>Coffee Wood</h3>
      <p>Upcycled from 20&ndash;25 year old coffee trees that have finished producing beans. Dense hardwood that wears down into soft fibres rather than sharp shards. Single ingredient, non-toxic, splinter-resistant.</p>
      <a href="/collections/coffee-wood/">Explore the collection &rarr;</a>
    </div>
    <div class="card">
      <img src="/assets/img/product-coconut-fiber-raw.jpg" alt="Coconut fiber raw material" style="margin-bottom:16px">
      <h3>Coconut Fiber</h3>
      <p>The fibrous husk of the coconut, a farming by-product cleaned and dried into a strong, springy natural fibre. Used for balls, rope toys and small-animal substrate.</p>
      <a href="/collections/coconut-fiber/">Explore the collection &rarr;</a>
    </div>
    <div class="card">
      <img src="/assets/img/product-hemp-rope-trio.jpg" alt="Hemp fiber rope toys" style="margin-bottom:16px">
      <h3>Hemp Fiber</h3>
      <p>A tough natural fibre twisted into rope and ball toys built for tug-of-war and multi-dog households. Durable, plastic-free, and biodegradable at end of life.</p>
      <a href="/collections/hemp-fiber/">Explore the collection &rarr;</a>
    </div>
    <div class="card">
      <img src="/assets/img/raw-loofah-gourd.jpg" alt="Raw loofah gourd" style="margin-bottom:16px">
      <h3>Loofah</h3>
      <p>The dried fibrous interior of the loofah gourd, grown in Vietnam. Light, naturally textured, and fully biodegradable &mdash; shaped into playful cat and small-animal toys.</p>
      <a href="/collections/loofah/">Explore the collection &rarr;</a>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>Why source natural materials from Vietnam</h2>
    <p>Vietnam is a major producer of coffee, coconut and loofah, so the raw materials behind our toys are local and abundant rather than imported &mdash; a shorter supply chain and a more authentic sustainability story than assembling natural-look products elsewhere. Read the full case in our <a href="/guides/sourcing-eco-pet-toys-vietnam/">wholesale buyer's guide to sourcing from Vietnam</a>.</p>
  </div>
</section>
"""
    html = page(f"Materials: Coffee Wood, Coconut Fiber, Hemp & Loofah | {BRAND}",
        "The natural materials behind our pet toys — upcycled coffee wood, coconut fiber, hemp fiber and loofah. Sourced in Vietnam, biodegradable, and traceable.",
        "/materials/", content + rfq_bar(), "Materials", [bc_s])
    write_page(root, "/materials/", html)

    # ---------------- CERTIFICATIONS ----------------
    bc, bc_s = breadcrumb_html([("Home","/"), ("Certifications & Compliance", None)])
    faqs = [
        ("What certifications do you provide?", "Every order ships with a Certificate of Origin (including EUR1 for EU/EVFTA preference), phytosanitary certificate, fumigation certificate, and an independent inspection report. Additional testing is available on request."),
        ("Can you meet CPSIA or REACH requirements?", "Yes — we arrange third-party testing through recognised labs to meet the standard your market requires. We confirm scope and cost per SKU before production."),
        ("Can we audit your factory?", "Yes. We welcome buyer-arranged and third-party audits for complete supply-chain transparency."),
        ("What if a shipment arrives with a quality issue?", "We operate a 1-for-1 replacement policy on defective goods, backed by our five-stage QC process before anything leaves the factory."),
    ]
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">Trust &amp; Compliance</p>
    <h1>Certifications &amp; Compliance You Can Import With Confidence</h1>
    <p class="hero-lede">"Natural" and "safe" mean nothing to a customs officer without paperwork behind them. Every shipment leaves with the documentation your broker needs, and every batch is checked before it ships.</p>
    <div class="hero-ctas"><a class="btn btn-primary" href="/request-a-quote/">Request Compliance Documents</a></div>
  </div>
</section>
<section class="section">
  <div class="wrap grid grid-2">
    <div>
      <h2 class="mt0">Export documentation on every order</h2>
      <ul class="check-list">
        <li><strong>Certificate of Origin</strong> (including EUR1 form for EU/EVFTA tariff preference)</li>
        <li><strong>Phytosanitary Certificate</strong> &mdash; required for plant-based goods</li>
        <li><strong>Fumigation Certificate</strong> &mdash; treatment documentation for wood and natural-fibre products</li>
        <li><strong>Invoice, Packing List &amp; Forest Product Declaration</strong></li>
        <li><strong>Independent inspection report</strong> before export</li>
      </ul>
    </div>
    <img src="/assets/img/export-carton-labels.jpg" alt="Export carton labels showing WINVN INT CO., LTD and shipment details">
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>Five-stage quality control</h2>
    <div class="grid grid-4" style="text-align:center">
      <div class="card"><h3>1. Raw Material</h3><p class="small">Inspection at intake</p></div>
      <div class="card"><h3>2. In-Process</h3><p class="small">Checks during production</p></div>
      <div class="card"><h3>3. Semi-Finished</h3><p class="small">Mid-stage consistency check</p></div>
      <div class="card"><h3>4. Final Product</h3><p class="small">Full inspection before packing</p></div>
      <div class="card"><h3>5. Pre-Shipment</h3><p class="small">Final check before dispatch</p></div>
    </div>
    <p style="margin-top:20px">On wood products, moisture is held at 12&ndash;14% to prevent cracking and mold in transit — measured with calibrated moisture meters on every batch.</p>
    <img src="/assets/img/process-moisture-check.jpg" alt="Worker checking moisture level of coffee wood with a moisture meter">
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>Third-party testing on request</h2>
    <p>If your retail channel requires specific safety testing &mdash; for example CPSIA for the US or REACH for the EU &mdash; we support third-party testing through internationally recognised labs, and we welcome buyer-arranged audits of our facility for full transparency.</p>
    <p>Our production facility sits in Gia Lai, in Vietnam's Central Highlands, with warehousing in Binh Duong and export handling out of Ho Chi Minh City. Our products already ship to {COUNTRIES} countries, including the USA, Japan, Germany, Korea and the Netherlands.</p>
  </div>
</section>
"""
    html = page(f"Certifications & Export Compliance | {BRAND}",
        "Export docs for our natural pet toys: Certificate of Origin, phytosanitary & fumigation certificates, inspection reports, and QC support.",
        "/certifications/", content + faq_html(faqs) + rfq_bar(), "Company", [bc_s, faq_schema(faqs)])
    write_page(root, "/certifications/", html)

    # ---------------- SUSTAINABILITY ----------------
    bc, bc_s = breadcrumb_html([("Home","/"), ("Sustainability", None)])
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">Sustainability &amp; Impact</p>
    <h1>Turning Natural By-Products Into Joy for Pets</h1>
    <p class="hero-lede">Every material we use is upcycled from something that would otherwise go to waste. That's not a marketing line &mdash; it's the entire premise of the business.</p>
  </div>
</section>
<section class="section">
  <div class="wrap grid grid-2">
    <div>
      <h2 class="mt0">A story rooted in Vietnam's Central Highlands</h2>
      <p>Our coffee wood comes from trees that have finished their bean-producing life, in Vietnam's Central Highlands &mdash; coffee country. Rather than being burned, the wood is harvested, naturally dried, and crafted into chews. Sourcing locally keeps our supply chain short and supports coffee-farming communities, including ethnic minority households who help process the raw material.</p>
    </div>
    <img src="/assets/img/process-coffeewood-styled.jpg" alt="Coffee wood raw material with coffee cherries">
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>Reducing plastic across the supply chain</h2>
    <p>We continually look for ways to remove plastic, not just from the toys but from what ships around them. We've replaced synthetic silica gel desiccant packets with natural charcoal for moisture absorption, and we offer kraft, vacuum and fully biodegradable packaging options on request.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>What "upcycled" means for each material</h2>
    <table>
      <tr><th>Material</th><th>By-product of</th><th>Would otherwise become</th></tr>
      <tr><td>Coffee Wood</td><td>Retired coffee trees (20&ndash;25 years old)</td><td>Firewood</td></tr>
      <tr><td>Coconut Fiber</td><td>Coconut husks from farming</td><td>Agricultural waste</td></tr>
      <tr><td>Hemp Fiber</td><td>Hemp plant fibre</td><td>Underused byproduct stream</td></tr>
      <tr><td>Loofah</td><td>Dried loofah gourd interior</td><td>Discarded plant matter</td></tr>
    </table>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>EVFTA benefits for EU buyers</h2>
    <p>We provide Certificate of Origin Form EUR1 under the EU&ndash;Vietnam Free Trade Agreement, helping EU importers prove origin and reduce import tariffs &mdash; one more reason sourcing directly from Vietnam beats buying generic, unverifiable "eco" product through a reseller.</p>
  </div>
</section>
"""
    html = page(f"Our Sustainability & Impact | Natural Pet Toys | {BRAND}",
        "How our pet toys are made from upcycled natural by-products — retired coffee trees, coconut husks, hemp fibre, loofah — supporting Vietnamese farming communities.",
        "/sustainability/", content + rfq_bar(), "Company", [bc_s])
    write_page(root, "/sustainability/", html)

    # ---------------- HOW TO ORDER ----------------
    bc, bc_s = breadcrumb_html([("Home","/"), ("How to Order", None)])
    faqs = [
        ("What's your minimum order?", "From 50 pcs per SKU, so you can pilot before scaling."),
        ("Do you offer free samples?", "Yes — a Trial Box of 3–5 free samples; you cover shipping, refunded on your first order."),
        ("How long until I receive goods?", "Roughly 15–20 working days for standard production (25–30 for custom OEM/ODM), plus freight time to your destination."),
        ("Which Incoterms do you offer?", "EXW, FOB, or CIF — with full export documentation on every shipment."),
    ]
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">Process</p>
    <h1>How to Order</h1>
    <p class="hero-lede">Ordering from overseas shouldn't be a leap of faith. Here's exactly how a first order works, from free sample to delivered goods.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <ol class="steps" style="max-width:680px">
      <li><strong>Enquiry &amp; quote</strong> &mdash; tell us the products, quantities and any branding needs. We send a quote with pricing and terms.</li>
      <li><strong>Free sample</strong> &mdash; a Trial Box of 3&ndash;5 free samples so you can test quality and packaging. You cover shipping only, refunded against your first order. Ready in about 7 days.</li>
      <li><strong>Confirm the order</strong> &mdash; sizes, packaging, engraving, quantities and Incoterms.</li>
      <li><strong>Deposit &amp; production</strong> &mdash; production begins once your order is confirmed.</li>
      <li><strong>QC &amp; documentation</strong> &mdash; every batch is inspected and export documents are prepared.</li>
      <li><strong>Shipping &amp; delivery</strong> &mdash; we dispatch worldwide with full paperwork, including direct routing to Amazon FBA warehouses.</li>
    </ol>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap grid grid-2">
    <div>
      <h3>Minimum order quantity</h3>
      <p>Our MOQ starts at 50 pcs per SKU on EXW pricing, with volume tiers at 500, 5,000 and 50,000 pcs for wholesalers who need distribution-level margins. Trial OEM/ODM runs are welcome before scaling to bulk.</p>
    </div>
    <div>
      <h3>Lead times</h3>
      <table>
        <tr><th>Stage</th><th>Time</th></tr>
        <tr><td>Sample / Trial Box</td><td>~7 days</td></tr>
        <tr><td>Standard production</td><td>15&ndash;20 working days</td></tr>
        <tr><td>OEM/ODM production</td><td>25&ndash;30 working days</td></tr>
        <tr><td>Freight &mdash; Asia</td><td>3&ndash;7 days</td></tr>
        <tr><td>Freight &mdash; Europe &amp; Americas</td><td>10&ndash;20 days</td></tr>
      </table>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h3>Shipping &amp; logistics</h3>
    <p>We quote on EXW, FOB or CIF terms depending on how much of the logistics you want to manage. We work with dedicated forwarders for EU routes, air express lanes into Asia, and freight partners that route directly into Amazon FBA warehouses — so Amazon sellers don't need a separate 3PL step.</p>
    <h3>Customisation &amp; private label</h3>
    <p>Logo, labelling, packaging and laser engraving are all available. <a href="/capabilities/">See full OEM capabilities &rarr;</a></p>
  </div>
</section>
"""
    html = page(f"How to Order — MOQ, Samples, Lead Times & Shipping | {BRAND}",
        f"How to order wholesale natural pet toys from {BRAND}: free samples, low MOQ from 50 pcs, OEM process, Incoterms, lead times, and worldwide shipping.",
        "/how-to-order/", content + faq_html(faqs) + rfq_bar(), "Company", [bc_s, faq_schema(faqs)])
    write_page(root, "/how-to-order/", html)

    # ---------------- WHOLESALE CATALOGUE ----------------
    bc, bc_s = breadcrumb_html([("Home","/"), ("Wholesale Catalogue", None)])
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap center">
    <p class="hero-eyebrow">Download</p>
    <h1>Wholesale Catalogue</h1>
    <p class="hero-lede" style="margin:0 auto">Every SKU, size and MOQ across coffee wood, coconut fiber, hemp fiber and loofah — plus OEM/ODM options — in one PDF.</p>
    <div class="hero-ctas center" style="justify-content:center">
      <a class="btn btn-primary" href="/assets/downloads/vietpaw-wholesale-catalogue.pdf">Download the Catalogue (PDF)</a>
    </div>
    <p class="small">By downloading, you may receive occasional emails about new products and offers. Unsubscribe anytime.</p>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <img src="/assets/img/hero-lifestyle-toys.jpg" alt="{BRAND} wholesale catalogue preview">
  </div>
</section>
"""
    html = page(f"Wholesale Catalogue (PDF) | {BRAND}",
        f"Download the {BRAND} wholesale catalogue: coffee wood, coconut fiber, hemp fiber and loofah pet toys, sizes, MOQ and OEM/ODM options.",
        "/wholesale-catalogue/", content + rfq_bar(), "Company", [bc_s])
    write_page(root, "/wholesale-catalogue/", html)

    # ---------------- REQUEST A QUOTE ----------------
    bc, bc_s = breadcrumb_html([("Home","/"), ("Request a Quote", None)])
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">Let's talk</p>
    <h1>Request a Quote or Free Sample</h1>
    <p class="hero-lede">Tell us what you need and we'll reply with pricing, lead time and sample availability — usually within one business day.</p>
  </div>
</section>
<section class="section">
  <div class="wrap grid grid-2">
    <form class="card" action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <h3 class="mt0">Tell us about your project</h3>
      <p class="small">This form opens your email client addressed to {EMAIL}. Prefer not to use it? Email us directly or use WhatsApp/phone below.</p>
      <p><label>Full name<br><input style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px" name="name" required></label></p>
      <p><label>Company &amp; role<br><input style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px" name="company"></label></p>
      <p><label>Email<br><input style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px" type="email" name="email" required></label></p>
      <p><label>I am a...<br>
        <select style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px" name="segment">
          <option>Startup brand</option><option>Amazon seller</option><option>Eco pet shop (EU)</option><option>Wholesaler / distributor</option><option>Other</option>
        </select></label></p>
      <p><label>Products of interest<br><textarea style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px" name="products" rows="3" placeholder="e.g. Coffee wood chew stick, private label, MOQ 500"></textarea></label></p>
      <p><button class="btn btn-primary" type="submit">Send Enquiry</button></p>
    </form>
    <div>
      <h3>Or reach us directly</h3>
      <ul class="check-list">
        <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>Phone / WhatsApp: <a href="tel:{PHONE_TEL}">{PHONE}</a></li>
        <li>Address: {ADDRESS}</li>
      </ul>
      <p>Every enquiry gets a reply with indicative pricing, MOQ and lead time. If you're ready to test quality first, ask about our Trial Box of 3&ndash;5 free samples.</p>
    </div>
  </div>
</section>
"""
    html = page(f"Request a Quote | Wholesale Natural Pet Toys | {BRAND}",
        f"Request a quote or free sample of {BRAND} natural pet toys — coffee wood, coconut fiber, hemp fiber and loofah. Reply within one business day.",
        "/request-a-quote/", content, "", [bc_s])
    write_page(root, "/request-a-quote/", html)

    # ---------------- CONTACT ----------------
    bc, bc_s = breadcrumb_html([("Home","/"), ("Contact", None)])
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">Contact</p>
    <h1>Get in Touch</h1>
  </div>
</section>
<section class="section">
  <div class="wrap grid grid-2">
    <div class="card">
      <h3 class="mt0">{BRAND}</h3>
      <p class="small">A brand of {LEGAL_NAME}</p>
      <ul class="check-list">
        <li>{ADDRESS}</li>
        <li>Phone / WhatsApp: <a href="tel:{PHONE_TEL}">{PHONE}</a></li>
        <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
      <a class="btn btn-primary" href="/request-a-quote/">Request a Quote</a>
    </div>
    <div>
      <h3>Factories &amp; warehouses</h3>
      <p>Production: Gia Lai &amp; Dak Lak, Vietnam &middot; Warehousing: Linh Trung, Long An, Binh Duong &middot; Export office: Ho Chi Minh City</p>
      <h3>Business hours</h3>
      <p>Monday&ndash;Saturday, 8:00&ndash;17:30 (GMT+7). We typically reply to enquiries within one business day.</p>
    </div>
  </div>
</section>
"""
    schema = {"@context":"https://schema.org","@type":"Organization","name":BRAND,"alternateName":LEGAL_NAME,
              "address":{"@type":"PostalAddress","streetAddress":ADDRESS},"telephone":PHONE,"email":EMAIL}
    html = page(f"Contact {BRAND} | Natural Pet Toy Manufacturer Vietnam",
        f"Contact {BRAND} ({LEGAL_NAME}) — natural pet toy manufacturer in Vietnam. Phone, email, address and factory locations.",
        "/contact/", content, "", [bc_s, schema])
    write_page(root, "/contact/", html)
