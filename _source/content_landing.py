# -*- coding: utf-8 -*-
"""Commercial landing pages (head-keyword money pages)."""
from common import page, write_page, rfq_bar, breadcrumb_html, BRAND, BASE_URL, LEGAL_NAME

def faq_schema(pairs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}

def faq_html(pairs):
    items = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in pairs)
    return f'<section class="section"><div class="wrap"><h2>Frequently asked questions</h2>{items}</div></section>'


def build(root):
    slug = "pet-toys-manufacturer-vietnam"
    path = f"/{slug}/"
    title = f"Natural Pet Toys Manufacturer in Vietnam | OEM, Private Label & Wholesale | {BRAND}"
    desc = ("VietPaw is a natural pet toys manufacturer in Vietnam — coffee wood, coconut fiber, hemp "
            "fiber & loofah. OEM/ODM, private label and wholesale, low MOQ from 50 pcs, free samples, "
            "full export documentation.")

    bc, bc_s = breadcrumb_html([("Home","/"), ("Pet Toys Manufacturer in Vietnam", None)])

    faqs = [
        ("Are you a real pet toy manufacturer or a trading company?",
         "We are the export and private-label brand of WINVN INT CO., LTD, a real manufacturer running three factories in Vietnam (Gia Lai, Dak Lak and Ho Chi Minh City) with 5–6 million units/year capacity. All export documents and certificates are issued under WINVN INT CO., LTD, so you can verify us independently before ordering."),
        ("What is your minimum order quantity (MOQ)?",
         "MOQ starts at 50 pcs per SKU, kept deliberately low so new brands can pilot before scaling. We also offer a Trial Box of 3–5 free samples (you cover shipping, refunded on your first order)."),
        ("Do you offer OEM, ODM and private label?",
         "Yes. We provide full OEM/ODM and private-label service: laser logo engraving, custom labels and packaging, and new product-shape development, typically with a ready-to-test prototype in days."),
        ("Which markets do you export to?",
         "We export to 30+ countries including the USA, UK, Germany, France, the Netherlands, Australia, Canada, Japan and Korea, with export documentation (Certificate of Origin/EUR1, phytosanitary, fumigation, inspection reports) on every shipment."),
        ("How long does production take?",
         "Standard production is 15–20 working days; OEM/ODM runs are 25–30 working days. Samples are usually ready in about 7 days."),
        ("Can you ship directly to Amazon FBA warehouses?",
         "Yes. We work with forwarders already routing to Amazon FBA, including dedicated EU and Asia lanes, with FBA-compliant barcode and warning labels built into OEM runs."),
    ]

    manufacturer_schema = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "additionalType": "https://schema.org/Manufacturer",
        "name": "VietPaw",
        "legalName": LEGAL_NAME,
        "url": f"{BASE_URL}{path}",
        "description": desc,
        "foundingDate": "2018",
        "areaServed": ["US","GB","DE","FR","NL","AU","CA","JP","KR","EU"],
        "makesOffer": {
            "@type": "Offer",
            "itemOffered": {"@type": "Service", "name": "Natural pet toy manufacturing (OEM/ODM, private label, wholesale)"},
            "businessFunction": "http://purl.org/goodrelations/v1#Sell",
            "eligibleCustomerType": "http://purl.org/goodrelations/v1#Business"
        }
    }

    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap hero-inner">
    <div>
      <p class="hero-eyebrow">Manufacturer &middot; Vietnam &middot; OEM / ODM / Private Label</p>
      <h1>Natural Pet Toys Manufacturer in Vietnam</h1>
      <p class="hero-lede">VietPaw is a natural, biodegradable pet toys manufacturer in Vietnam, producing coffee wood dog chews, coconut fiber, hemp fiber and loofah toys for brands, wholesalers and retailers worldwide. Low MOQ from 50 pcs, full OEM/ODM and private label, free samples, and export documentation on every shipment.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="/request-a-quote/">Request a Free Sample</a>
        <a class="btn btn-outline" href="/wholesale-catalogue/">Download Wholesale Catalogue</a>
      </div>
      <div class="hero-badges">
        <div><strong>30+</strong> countries served</div>
        <div><strong>5–6 million units/year</strong> production capacity</div>
        <div><strong>50 pcs</strong> MOQ per SKU</div>
        <div><strong>3</strong> factories in Vietnam</div>
      </div>
    </div>
    <img src="/assets/img/hero-lifestyle-toys.jpg" alt="Natural pet toys manufactured in Vietnam by VietPaw — coffee wood, coconut fiber, hemp fiber and loofah" loading="eager">
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">A real manufacturer, not a trading middleman</p>
      <h2>Manufacturing natural pet toys in Vietnam since 2018</h2>
    </div>
    <p>Choosing a pet toys manufacturer is a decision about trust as much as price. VietPaw is the export and private-label brand of <strong>{LEGAL_NAME}</strong>, a Vietnamese natural pet products manufacturer operating three factories in the Central Highlands and Ho Chi Minh City. Because we own production, we control quality, customisation and lead times end to end — and we can prove it with a factory address you can verify, export documents issued under our legal entity, and buyer-arranged audits welcome at any time. If you are sourcing a <strong>natural pet toys manufacturer in Vietnam</strong> for wholesale, OEM/ODM or private label, this page explains exactly what we make, how we work, and how to start.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">What we manufacture</p><h2>Four natural materials, one supplier</h2></div>
    <div class="grid grid-4">
      <div class="card"><h3>Coffee Wood</h3><p>Splinter-resistant, single-ingredient dog chews upcycled from retired coffee trees. <a href="/collections/coffee-wood/">Coffee wood chews &rarr;</a></p></div>
      <div class="card"><h3>Coconut Fiber</h3><p>Biodegradable balls and rope toys for cats, dogs and small pets. <a href="/collections/coconut-fiber/">Coconut fiber &rarr;</a></p></div>
      <div class="card"><h3>Hemp Fiber</h3><p>Tough natural rope and ball toys for tug and multi-dog play. <a href="/collections/hemp-fiber/">Hemp fiber &rarr;</a></p></div>
      <div class="card"><h3>Loofah</h3><p>Fully biodegradable gourd-fibre toys shaped for cats and small animals. <a href="/collections/loofah/">Loofah toys &rarr;</a></p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Why Vietnam</p><h2>Why brands source pet toys from Vietnam</h2></div>
    <div class="grid grid-2">
      <div>
        <ul class="check-list">
          <li><strong>China +1 diversification</strong> — reduce concentration risk with a stable, tariff-advantaged manufacturing base.</li>
          <li><strong>EVFTA / EUR1 preference</strong> — Certificate of Origin (EUR1) for reduced EU import duty.</li>
          <li><strong>Genuine natural materials</strong> — upcycled coffee wood, coconut, hemp and loofah, not plastic dressed up as "eco".</li>
          <li><strong>Short, transparent supply chain</strong> — raw material sourced locally in coffee country, supporting farming communities.</li>
        </ul>
      </div>
      <img src="/assets/img/process-coffeewood-styled.jpg" alt="Coffee wood raw material used by a natural pet toy manufacturer in Vietnam">
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Full-service manufacturing</p><h2>OEM, ODM, private label &amp; wholesale</h2></div>
    <div class="grid grid-3">
      <div class="card"><h3>Private label pet toys</h3><p>Laser-engraved logos, custom kraft labels and retail-ready packaging so the product ships under your brand. <a href="/capabilities/">See capabilities &rarr;</a></p></div>
      <div class="card"><h3>OEM / ODM development</h3><p>New shapes, sizes and material combinations developed to your spec, with a fast prototype before you commit to bulk.</p></div>
      <div class="card"><h3>Wholesale &amp; bulk</h3><p>From a 50-piece pilot to full containers, with consistent quality across reorders and 5–6M units/year capacity behind you.</p></div>
      <div class="card"><h3>Low, flexible MOQ</h3><p>Start from 50 pcs per SKU with a Trial Box of 3–5 free samples, refunded on your first order.</p></div>
      <div class="card"><h3>Export compliance</h3><p>Certificate of Origin (incl. EUR1), phytosanitary, fumigation and inspection reports on every order. <a href="/certifications/">See certifications &rarr;</a></p></div>
      <div class="card"><h3>Direct-to-FBA logistics</h3><p>Forwarders already routing to Amazon FBA, with FBA-compliant barcodes and warning labels built in.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Quality you can import with confidence</p><h2>Five-stage QC on every batch</h2></div>
    <p>Every order passes a five-stage quality control process — raw material, in-process, semi-finished, final product and pre-shipment inspection. On wood products, moisture is held at 12–14% with calibrated meters to prevent cracking and mold in transit, and defective goods are covered by a 1-for-1 replacement policy. Where your retail channel requires it, we arrange third-party testing (for example CPSIA for the US or REACH for the EU) through internationally recognised labs. <a href="/certifications/">See certifications &amp; compliance &rarr;</a></p>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Who we supply</p><h2>Built for every kind of B2B buyer</h2></div>
    <div class="persona-pills">
      <a href="/solutions/startup-brands/">Startup Brands</a>
      <a href="/solutions/amazon-sellers/">Amazon Sellers</a>
      <a href="/solutions/eco-pet-shops/">Eco Pet Shops (EU)</a>
      <a href="/solutions/wholesalers/">Wholesalers &amp; Distributors</a>
    </div>
    <p style="margin-top:18px">Distributors, wholesalers, retailers, importers, private-label buyers and OEM/ODM customers across the USA, UK, Germany, France, the Netherlands, Australia and Canada source natural pet toys from us. New to sourcing from Vietnam? Read our guide on <a href="/guides/natural-dog-toy-manufacturer-vietnam/">how to choose a natural dog toy manufacturer in Vietnam</a>.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center" style="margin:0 auto 32px"><p class="eyebrow">Start in three steps</p><h2>From free sample to export-ready goods</h2></div>
    <ol class="steps" style="max-width:640px;margin:0 auto">
      <li><strong>Request a free sample</strong> — feel the quality before you commit. Ready in about 7 days.</li>
      <li><strong>Confirm your order &amp; branding</strong> — low MOQ, custom packaging, laser engraving.</li>
      <li><strong>Receive export-ready goods</strong> — full documentation, on time, wherever you ship.</li>
    </ol>
  </div>
</section>
"""

    html = page(title, desc, path, content + faq_html(faqs) + rfq_bar(cta="Request a Free Sample"),
                active_top="", schemas=[bc_s, manufacturer_schema, faq_schema(faqs)])
    write_page(root, path, html)
    print("built", path)


if __name__ == "__main__":
    import sys
    build(sys.argv[1] if len(sys.argv) > 1 else "site")
