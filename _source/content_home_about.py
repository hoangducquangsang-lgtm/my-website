# -*- coding: utf-8 -*-
from common import page, write_page, rfq_bar, BRAND, LEGAL_NAME, PHONE, EMAIL, ADDRESS, FOUNDED, COUNTRIES, CAPACITY, BASE_URL

def build(root):
    # ---------------- HOME ----------------
    content = f"""
<section class="hero">
  <div class="wrap hero-inner">
    <div>
      <p class="hero-eyebrow">Manufacturer &middot; Vietnam &middot; Since {FOUNDED}</p>
      <h1>Natural Pet Toys Manufacturer in Vietnam</h1>
      <p class="hero-sub" style="font-size:1.2rem;font-weight:600;margin:6px 0 12px"><strong>Natural pet toys your brand can stand behind.</strong></p>
      <p class="hero-lede">{BRAND} manufactures natural, biodegradable pet toys in Vietnam &mdash; coffee wood chews, coconut fiber, hemp fiber and loofah. Low MOQ from 50 pcs, full OEM/private label, free samples, and export documentation on every shipment.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="/request-a-quote/">Request a Free Sample</a>
        <a class="btn btn-outline" href="/wholesale-catalogue/">Download Wholesale Catalogue</a>
      </div>
      <div class="hero-badges">
        <div><strong>{COUNTRIES}</strong> countries served</div>
        <div><strong>{CAPACITY}</strong> production capacity</div>
        <div><strong>50 pcs</strong> MOQ per SKU</div>
        <div><strong>3</strong> factories in Vietnam</div>
      </div>
    </div>
    <img src="/assets/img/hero-lifestyle-toys.jpg" alt="Dog and cat with natural coffee wood and coconut fiber pet toys made by {BRAND}" loading="eager">
  </div>
</section>

<section class="trust-bar" style="padding:16px 0;border-top:1px solid #ececec;border-bottom:1px solid #ececec;background:#faf7f2">
  <div class="wrap" style="text-align:center">
    <p class="small" style="margin:0;letter-spacing:.03em;text-transform:uppercase;opacity:.85">Trusted by pet brands, wholesalers &amp; Amazon sellers across the USA &middot; UK &middot; Germany &middot; France &middot; Netherlands &middot; Australia &middot; Canada &mdash; exporting to {COUNTRIES} countries since {FOUNDED}</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center" style="margin:0 auto">
      <p>{BRAND} is a <a href="/pet-toys-manufacturer-vietnam/">natural pet toys manufacturer in Vietnam</a>, producing coffee wood dog chews, coconut fiber, hemp fiber and loofah toys for wholesale, OEM/ODM and private label. As the export brand of {LEGAL_NAME}, we run three factories with {CAPACITY} capacity, low MOQ from 50 pcs, free samples, and full export documentation &mdash; helping distributors, retailers, eco pet shops, Amazon sellers and startup brands source natural pet products with confidence.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center" style="margin:0 auto 32px">
      <p class="eyebrow">Made by nature, built for retail</p>
      <h2>No plastic. No shortcuts. No surprises in your warehouse.</h2>
      <p>We manufacture pet toys from materials nature already provides, and back every order with the documentation, quality control, and branding support serious buyers need &mdash; whether you're a startup brand testing your first SKU or a wholesaler stocking a full natural range.</p>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Our Materials</p>
      <h2>Four natural materials, one supplier</h2>
    </div>
    <div class="grid grid-4">
      <div class="card material-card">
        <div class="card-img"><img src="/assets/img/product-coffeewood-stick.jpg" alt="Coffee wood dog chew sticks"></div>
        <span class="tag">Hero line</span>
        <h3>Coffee Wood</h3>
        <p>Upcycled from retired coffee trees. Splinter-resistant, single-ingredient dog chew.</p>
        <a href="/collections/coffee-wood/">Explore &rarr;</a>
      </div>
      <div class="card material-card">
        <div class="card-img"><img src="/assets/img/product-coconut-ball-sizes.jpg" alt="Coconut fiber pet balls in three sizes"></div>
        <span class="tag">Versatile</span>
        <h3>Coconut Fiber</h3>
        <p>Balls, rope toys and substrate. Biodegradable and naturally textured.</p>
        <a href="/collections/coconut-fiber/">Explore &rarr;</a>
      </div>
      <div class="card material-card">
        <div class="card-img"><img src="/assets/img/product-hemp-ball.jpg" alt="Hemp fiber ball toy"></div>
        <span class="tag">Durable</span>
        <h3>Hemp Fiber</h3>
        <p>Tough natural rope and ball toys built for tug and multi-dog play.</p>
        <a href="/collections/hemp-fiber/">Explore &rarr;</a>
      </div>
      <div class="card material-card">
        <div class="card-img"><img src="/assets/img/product-loofah-basket.jpg" alt="Loofah cat toys in assorted shapes"></div>
        <span class="tag">Light &amp; playful</span>
        <h3>Loofah</h3>
        <p>Fully biodegradable gourd fiber, shaped into playful cat and small-pet toys.</p>
        <a href="/collections/loofah/">Explore &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Why brands choose {BRAND}</p>
      <h2>Built for how modern brands actually source</h2>
    </div>
    <div class="grid grid-3">
      <div class="card">
        <h3>Low, flexible MOQ</h3>
        <p>Start from 50 pcs per SKU with a Trial Box (3&ndash;5 free samples, ship cost only, refunded on your first order) so you can pilot before you scale.</p>
      </div>
      <div class="card">
        <h3>Full OEM &amp; private label</h3>
        <p>Laser-engraved logos, custom kraft labels and packaging concepts, with a ready-to-test prototype in days. <a href="/capabilities/">See capabilities &rarr;</a></p>
      </div>
      <div class="card">
        <h3>Export-ready compliance</h3>
        <p>Certificate of Origin (incl. EUR1 for EU/EVFTA), Phytosanitary, Fumigation, and inspection reports on every order. <a href="/certifications/">See certifications &rarr;</a></p>
      </div>
      <div class="card">
        <h3>Consistent quality</h3>
        <p>Five-stage QC &mdash; raw material, in-process, semi-finished, final product, pre-shipment inspection &mdash; with moisture held at 12&ndash;14% on wood products.</p>
      </div>
      <div class="card">
        <h3>Direct-to-FBA logistics</h3>
        <p>Forwarders already routing to Amazon FBA warehouses, with dedicated EU and Asia lanes, so your inventory lands where it needs to.</p>
      </div>
      <div class="card">
        <h3>Real manufacturing capacity</h3>
        <p>{CAPACITY} across three factories in Gia Lai, Dak Lak and Ho Chi Minh City &mdash; not a trading middleman.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Built for your business</p>
      <h2>Solutions for every kind of buyer</h2>
      <p>Whether you're testing your first SKU or restocking a distribution network, we've mapped our offer to how you actually buy.</p>
    </div>
    <div class="persona-pills">
      <a href="/solutions/startup-brands/">Startup Brands</a>
      <a href="/solutions/amazon-sellers/">Amazon Sellers</a>
      <a href="/solutions/eco-pet-shops/">Eco Pet Shops (EU)</a>
      <a href="/solutions/wholesalers/">Wholesalers &amp; Distributors</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Genuinely sustainable</p>
      <h2>Not greenwashed &mdash; upcycled by design</h2>
    </div>
    <div class="grid grid-2">
      <div>
        <p>Every material we use is biodegradable and upcycled from a natural by-product: retired coffee trees, coconut husks, dried loofah gourds, hemp fiber. We've also replaced synthetic silica gel with natural charcoal for moisture absorption in our packaging.</p>
        <p>Our workshops sit in Vietnam's Central Highlands, where coffee wood sourcing directly supports local farming communities, including ethnic minority households who process and prepare the raw material. It's a sustainability story your customers can believe &mdash; and verify.</p>
        <a class="btn btn-outline" href="/sustainability/">Read our sustainability story &rarr;</a>
      </div>
      <img src="/assets/img/process-coffeewood-styled.jpg" alt="Coffee wood raw material styled with coffee beans and plants">
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head center" style="margin:0 auto 32px">
      <p class="eyebrow">Start in three steps</p>
      <h2>From free sample to export-ready goods</h2>
    </div>
    <ol class="steps" style="max-width:640px;margin:0 auto">
      <li><strong>Request a free sample</strong> &mdash; feel the quality before you commit. Ready in about 7 days.</li>
      <li><strong>Confirm your order &amp; branding</strong> &mdash; low MOQ, custom packaging, laser engraving.</li>
      <li><strong>Receive export-ready goods</strong> &mdash; full documentation, on time, wherever you ship.</li>
    </ol>
  </div>
</section>
"""
    schemas = [{
        "@context": "https://schema.org", "@type": "Organization",
        "name": BRAND, "alternateName": LEGAL_NAME, "url": BASE_URL,
        "logo": f"{BASE_URL}/assets/img/logo-winvn.png",
        "foundingDate": FOUNDED,
        "address": {"@type": "PostalAddress", "streetAddress": ADDRESS},
        "telephone": PHONE, "email": EMAIL,
        "sameAs": ["https://www.winvnint.com"]
    }, {
        "@context": "https://schema.org", "@type": "WebSite",
        "name": BRAND, "url": BASE_URL
    }]
    html = page(
        title=f"Natural Pet Toys, Wholesale & Private Label | {BRAND}",
        meta_description=f"{BRAND} makes natural pet toys in Vietnam — coffee wood, coconut fiber, hemp fiber & loofah. Low MOQ from 50 pcs, OEM/private label, free samples.",
        path="/", content=content, active_top="", schemas=schemas,
    )
    write_page(root, "/", html)

    # ---------------- ABOUT ----------------
    from common import breadcrumb_html
    bc, bc_schema = breadcrumb_html([("Home", "/"), ("About / Our Factory", None)])
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">About {BRAND}</p>
    <h1>Made by Nature, Built for Brands</h1>
    <p class="hero-lede">We started {BRAND} on a simple belief: pet products should be safe for pets, good for nature, and valuable for the brands that sell them. We are the export and private-label brand of {LEGAL_NAME}, a Vietnamese manufacturer that has been making natural pet products since {FOUNDED}.</p>
  </div>
</section>

<section class="section">
  <div class="wrap grid grid-2">
    <div>
      <h2 class="mt0">Our story</h2>
      <p>What began with a single idea &mdash; that the wood of a retired coffee tree could become a safe, sustainable chew instead of firewood &mdash; has grown into a full range of coconut fiber, hemp fiber and loofah toys. That heritage now reaches partners in {COUNTRIES} countries across Asia, Europe and the Americas.</p>
      <p>Our workshops are rooted in Vietnam's Central Highlands &mdash; coffee country &mdash; where sourcing coffee wood locally keeps our supply chain short and directly supports local farming communities, including ethnic minority households who help prepare the raw material.</p>
    </div>
    <img src="/assets/img/process-raw-sticks.jpg" alt="Raw coffee wood sticks before processing">
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <h2>Where we're made</h2>
    <div class="stats">
      <div><strong>3</strong><span>Factories: Gia Lai &amp; Dak Lak, Ho Chi Minh City</span></div>
      <div><strong>{CAPACITY.split(' units')[0]}</strong><span>Units produced per year</span></div>
      <div><strong>{COUNTRIES}</strong><span>Countries we export to</span></div>
      <div><strong>{FOUNDED}</strong><span>Manufacturing natural pet products since</span></div>
    </div>
    <p style="margin-top:24px">Warehousing and export handling run through Linh Trung, Long An and Binh Duong, keeping shipments consistent whether you're ordering a 50-piece pilot or a full container.</p>
    <img src="/assets/img/warehouse-winvn-boxes.jpg" alt="Warehouse pallets of packed WINVN INT CO., LTD export cartons">
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>What we make</h2>
    <div class="grid grid-4">
      <div class="card"><h3>Coffee Wood</h3><p>Upcycled hardwood chews for dogs, 6 sizes.</p></div>
      <div class="card"><h3>Coconut Fiber</h3><p>Balls and rope toys for cats, dogs and small pets.</p></div>
      <div class="card"><h3>Hemp Fiber</h3><p>Durable rope and ball toys for tug and play.</p></div>
      <div class="card"><h3>Loofah</h3><p>Light, biodegradable toys for cats and small animals.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <h2>What we stand for</h2>
    <ul class="check-list grid grid-2" style="list-style:none">
      <li>Safety first &mdash; single-ingredient materials, five-stage QC, and full export documentation on every order</li>
      <li>Genuine sustainability &mdash; upcycled by-products, not plastic dressed up as green</li>
      <li>Partnership &mdash; low MOQs, fast samples, and honest communication because your growth is our growth</li>
      <li>Craft &mdash; handmade quality that survives the journey to your shelf</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Legal entity &amp; verification</h2>
    <p><strong>{BRAND}</strong> is the international wholesale and private-label brand of <strong>{LEGAL_NAME}</strong>. All export documents, invoices and certificates (Certificate of Origin, Phytosanitary, Fumigation) are issued under {LEGAL_NAME}, so you can verify us independently before you order.</p>
    <p class="small">Address: {ADDRESS} &middot; Phone: {PHONE} &middot; Email: {EMAIL}</p>
  </div>
</section>
"""
    html = page(
        title=f"About {BRAND} — Natural Pet Toy Manufacturer from Vietnam",
        meta_description=f"{BRAND} crafts natural pet toys in Vietnam's Central Highlands — coffee wood, coconut fiber, hemp fiber & loofah — for brands worldwide.",
        path="/about/", content=content + rfq_bar(), active_top="Company",
        schemas=[bc_schema, {"@context":"https://schema.org","@type":"AboutPage"}],
    )
    write_page(root, "/about/", html)
