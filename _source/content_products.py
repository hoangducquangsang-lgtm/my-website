# -*- coding: utf-8 -*-
from common import page, write_page, rfq_bar, breadcrumb_html, BRAND, BASE_URL

def faq_schema(pairs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}

def faq_html(pairs):
    items = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in pairs)
    return f'<section class="section"><div class="wrap"><h2>Frequently asked questions</h2>{items}</div></section>'

def product_schema(name, desc, img, category, sku=None, brand=BRAND):
    s = {
        "@context": "https://schema.org", "@type": "Product",
        "name": name, "description": desc, "image": img,
        "brand": {"@type": "Brand", "name": brand},
        "category": category,
        "manufacturer": {"@type": "Organization", "name": "WINVN INT CO., LTD"},
        "offers": {
            "@type": "Offer",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "businessFunction": "http://purl.org/goodrelations/v1#Sell",
            "eligibleQuantity": {"@type": "QuantitativeValue", "minValue": 50, "unitText": "pcs"},
            "seller": {"@type": "Organization", "name": "WINVN INT CO., LTD"},
            "url": f"{BASE_URL}/request-a-quote/"
        }
    }
    if sku:
        s["sku"] = sku
    return s

def related_grid(items):
    """items: list of (title, desc, href, img) -> a real card grid, not just buttons."""
    cards = ""
    for title, desc, href, img in items:
        imgtag = f'<div class="card-img"><img src="{img}" alt="{title}"></div>' if img else ""
        cards += f'<div class="card">{imgtag}<h3>{title}</h3><p>{desc}</p><a href="{href}">Explore &rarr;</a></div>'
    return f'<section class="section section-alt"><div class="wrap"><h2>Related products</h2><div class="grid grid-3">{cards}</div></div></section>'

def product_page(root, slug, parent_label, parent_href, name, meta_title, meta_desc, lede, hero_img,
                  specs_rows, faqs, related, body_extra="", related_cards=None, sku=None):
    bc, bc_s = breadcrumb_html([("Home","/"), (parent_label, parent_href), (name, None)])
    specs = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in specs_rows)
    content = f"""
{bc}
<section class="section">
  <div class="wrap grid grid-2">
    <img src="{hero_img}" alt="{name}">
    <div>
      <h1>{name}</h1>
      <p class="hero-lede">{lede}</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="/request-a-quote/">Request a Quote</a>
        <a class="btn btn-outline" href="/request-a-quote/">Request a Free Sample</a>
      </div>
      <h3 style="margin-top:28px">Specifications</h3>
      <table>{specs}</table>
    </div>
  </div>
</section>
{body_extra}
"""
    if related_cards:
        rel_section = related_grid(related_cards)
    else:
        rel = "".join(f'<a class="btn btn-outline" href="{r[1]}" style="margin-right:10px">{r[0]}</a>' for r in related)
        rel_section = f'<section class="section section-alt"><div class="wrap"><h3 class="mt0">You may also want</h3>{rel}</div></section>'
    html = page(meta_title, meta_desc, f"/products/{slug}/", content + rel_section + faq_html(faqs) + rfq_bar(), "",
                [bc_s, faq_schema(faqs), product_schema(name, meta_desc, hero_img, parent_label, sku=sku)])
    write_page(root, f"/products/{slug}/", html)


# ---- Rich body for the hero coffee-wood product (the strongest commercial product page) ----
COFFEEWOOD_BODY = """
<section class="section">
  <div class="wrap grid grid-2">
    <div>
      <h2 class="mt0">Why buyers choose our coffee wood dog chew</h2>
      <ul class="check-list">
        <li><strong>Single ingredient</strong> — 100% real coffee wood, no glue, resin, additives or artificial flavour.</li>
        <li><strong>Splinter-resistant</strong> — wears into soft fibres rather than sharp shards, unlike antler or bone.</li>
        <li><strong>Long-lasting</strong> — a dense hardwood that outlasts most soft, pressed and rawhide chews.</li>
        <li><strong>Naturally odourless</strong> — no chemical smell out of the box, with a faint natural aroma dogs are drawn to.</li>
        <li><strong>Upcycled &amp; sustainable</strong> — cut from retired coffee trees, a story your customers will pay more for.</li>
      </ul>
    </div>
    <img src="/assets/img/dog-chewing-coffeewood.jpg" alt="Dog chewing a natural coffee wood dog chew stick from VietPaw">
  </div>
</section>
<section class="section section-alt">
  <div class="wrap grid grid-2">
    <img src="/assets/img/process-raw-sticks.jpg" alt="Raw coffee wood before processing into natural dog chews">
    <div>
      <h2 class="mt0">The material &amp; where it comes from</h2>
      <p>Our coffee wood is sourced in Vietnam's Central Highlands — coffee country — from coffee trees retired at the end of their productive life. Cutting locally keeps the supply chain short and directly supports local farming communities, including ethnic minority households who prepare the raw material. Each piece is naturally dried and finished to retail-ready standards, then held at 12–14% moisture to prevent cracking and mold in transit.</p>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>OEM, private label &amp; packaging</h2>
    <p>Every coffee wood chew can ship under your brand. We offer laser-engraved logos directly on the chew, custom kraft labels, retail-ready and bulk packaging, and Amazon FBA-compliant barcodes and warning labels. Prototype samples are typically ready in about 7 days so you can approve branding before bulk production. <a href="/capabilities/">See private label options &rarr;</a></p>
    <table>
      <tr><td>Branding</td><td>Laser logo engraving, custom label &amp; kraft packaging</td></tr>
      <tr><td>Packaging</td><td>Bulk carton, retail-ready sleeve/box, custom, FBA-ready</td></tr>
      <tr><td>Moisture control</td><td>Held at 12–14%, vacuum-sealing available for long transit</td></tr>
    </table>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>Quality control &amp; compliance</h2>
    <p>Coffee wood chews pass our five-stage QC — raw material, in-process, semi-finished, final product and pre-shipment inspection — with moisture checked by calibrated meters on every batch. Defective goods are covered by a 1-for-1 replacement policy, and we arrange third-party testing (CPSIA, REACH) on request. Export documentation — Certificate of Origin/EUR1, phytosanitary, fumigation and inspection reports — ships with every order. <a href="/certifications/">See certifications &amp; compliance &rarr;</a></p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>Who it's for</h2>
    <p>The coffee wood dog chew is a proven entry SKU for pet retailers, eco pet shops, Amazon FBA sellers, subscription boxes and private-label brands looking for a differentiated, natural chew. Amazon sellers often pair it with coconut fiber and hemp fiber toys into a combo/gift box to lift average order value — see our <a href="/solutions/amazon-sellers/">Amazon sellers solution</a>.</p>
  </div>
</section>
"""

def build(root):
    product_page(root, "coffee-wood-dog-chew", "Coffee Wood", "/collections/coffee-wood/",
        "Coffee Wood Dog Chew Stick",
        f"Coffee Wood Dog Chew Supplier | Wholesale & Private Label | {BRAND}",
        "Coffee wood dog chew supplier from Vietnam. Natural single-ingredient, splinter-resistant, non-toxic. Wholesale & private label, low MOQ from 50 pcs, laser engraving, full export docs.",
        "A single-ingredient chew cut from real Vietnamese coffee trees, naturally dried and finished to retail-ready standards. Available in six sizes matched to dog weight, wholesale and private label from a real manufacturer.",
        "/assets/img/product-coffeewood-stick.jpg",
        [("Material","100% coffee wood, no additives"),
         ("Sizes","XS (&lt;3kg) · S (3–5kg) · M (5–8kg) · L (8–12kg) · XL (12–20kg) · XXL (20kg+)"),
         ("Moisture","12–14%, factory-controlled"),
         ("MOQ","50 pcs per SKU"),
         ("Customisation","Laser logo engraving, custom label & packaging"),
         ("Lead time","15–20 working days standard, 25–30 OEM/ODM")],
        [("Are coffee wood chews safe for dogs?", "Yes — single natural material, no chemicals, finished splinter-resistant. Choose the correct size and supervise chewing as with any chew."),
         ("What sizes are available?", "Six sizes from XS to XXL, sized to dog weight from under 3kg to over 20kg. See our full size guide."),
         ("Can I laser-engrave my logo?", "Yes, directly onto the chew, as part of our OEM/private label service."),
         ("What is the MOQ and can I get samples first?", "MOQ starts at 50 pcs per SKU. We offer a Trial Box of 3–5 free samples — you cover shipping, refunded on your first order."),
         ("Do you ship export documents?", "Yes — Certificate of Origin (incl. EUR1), phytosanitary, fumigation and inspection reports ship with every order.")],
        [("Coffee Wood Collection","/collections/coffee-wood/"), ("Size Guide","/guides/coffee-wood-chew-size-guide/")],
        body_extra=COFFEEWOOD_BODY,
        related_cards=[
            ("Coconut Fiber Dog Ball","Biodegradable fetch ball — pairs into a natural combo box.","/products/coconut-fiber-dog-ball/","/assets/img/dog-coconut-balls-lifestyle.jpg"),
            ("Hemp Fiber Rope Ball","Tough hemp rope ball for tug and multi-dog play.","/products/hemp-fiber-ball/","/assets/img/product-hemp-ball.jpg"),
            ("Coffee Wood Collection","Explore the full coffee wood range, sizes and formats.","/collections/coffee-wood/","/assets/img/product-coffeewood-single.jpg"),
        ],
        sku="VP-CW-CHEW")

    product_page(root, "coconut-fiber-cat-ball", "Coconut Fiber", "/collections/coconut-fiber/",
        "Coconut Fiber Cat Ball",
        f"Coconut Fiber Cat Ball | Natural, Plastic-Free | Wholesale | {BRAND}",
        "Natural coconut fiber cat ball, wholesale from Vietnam. Biodegradable, plastic-free, naturally textured. Low MOQ, OEM & private label.",
        "A springy, naturally textured ball made from coconut husk fibre — light enough to bat, tough enough to last.",
        "/assets/img/product-coconut-ball-sizes.jpg",
        [("Material","100% coconut fiber"),
         ("Sizes","S / M / L"),
         ("MOQ","50–100 pcs per SKU"),
         ("Customisation","Custom label & kraft packaging"),
         ("Lead time","15–20 working days standard")],
        [("Is this safe for cats?", "Yes — natural coconut husk fibre, cleaned and dried with no chemical treatment."),
         ("What's the minimum order?", "From 50–100 pcs per SKU depending on size.")],
        [("Coconut Fiber Collection","/collections/coconut-fiber/"), ("Cat Toys","/cat-toys/balls/")],
        sku="VP-CF-CATBALL")

    product_page(root, "coconut-fiber-dog-ball", "Coconut Fiber", "/collections/coconut-fiber/",
        "Coconut Fiber Dog Ball",
        f"Coconut Fiber Dog Ball | Wholesale | {BRAND}",
        "Wholesale coconut fiber dog fetch ball from Vietnam. Biodegradable, durable, plastic-free. Low MOQ, private label available.",
        "A durable, biodegradable fetch ball sized for daily play, in three sizes to suit small through large dogs.",
        "/assets/img/dog-coconut-balls-lifestyle.jpg",
        [("Material","100% coconut fiber"),
         ("Sizes","S / M / L"),
         ("MOQ","50–100 pcs per SKU"),
         ("Lead time","15–20 working days standard")],
        [("Is it durable enough for daily fetch?", "Yes, for normal fetch and carry play. It is not designed for aggressive power-chewing — pair with coffee wood for that use case."),
         ("Can this be private labelled?", "Yes, with custom tags and kraft packaging.")],
        [("Coconut Fiber Collection","/collections/coconut-fiber/"), ("Fetch & Ball Toys","/dog-toys/fetch-toys/")],
        sku="VP-CF-DOGBALL")

    product_page(root, "loofah-cat-toy", "Loofah", "/collections/loofah/",
        "Loofah Cat & Small Pet Toy",
        f"Loofah Cat Toy | Biodegradable Shapes | Wholesale | {BRAND}",
        "Wholesale loofah cat and small-pet toy from Vietnam. Biodegradable, naturally textured, mouse/fish/rabbit and other shapes. Low MOQ, OEM available.",
        "Dried loofah gourd fibre shaped into playful forms for cats and small animals — naturally textured for dental chewing.",
        "/assets/img/product-loofah-basket.jpg",
        [("Material","100% dried loofah fibre"),
         ("Shapes","Mouse, teddy bear, fish, fish-with-tail, rabbit, duck, bone and more"),
         ("Size range","Approx. 4–16 cm"),
         ("MOQ","100 pcs per SKU (mixed-shape trial cartons available)"),
         ("Lead time","15–20 working days standard")],
        [("Is loofah safe for rabbits and small pets?", "Yes — natural plant fibre commonly used for dental chewing in small animals."),
         ("Can shapes be customised?", "Yes, custom shapes and catnip-fill options are available on OEM runs.")],
        [("Loofah Collection","/collections/loofah/"), ("Cat Toys","/cat-toys/catnip-toys/")],
        sku="VP-LF-CATTOY")

    product_page(root, "hemp-fiber-ball", "Hemp Fiber", "/collections/hemp-fiber/",
        "Hemp Fiber Rope Ball",
        f"Hemp Fiber Rope Ball | Wholesale | {BRAND}",
        "Wholesale hemp fiber rope ball dog toy from Vietnam. Durable, plastic-free, biodegradable. Low MOQ, OEM & private label.",
        "A tightly wound hemp fiber ball built for tug, fetch and chew — a plastic-free alternative to synthetic rope toys.",
        "/assets/img/product-hemp-ball.jpg",
        [("Material","100% hemp fiber"),
         ("Sizes","S / M / L"),
         ("MOQ","50–100 pcs per SKU"),
         ("Lead time","15–20 working days standard")],
        [("Is hemp fiber tougher than coconut fiber?", "Generally yes for tug and rope applications — hemp strands are longer and higher tensile strength."),
         ("Can I mix this into a combo box?", "Yes — many Amazon sellers combine coffee wood, coconut fiber and hemp fiber into a single gift/combo box for higher AOV.")],
        [("Hemp Fiber Collection","/collections/hemp-fiber/"), ("Amazon Sellers Solution","/solutions/amazon-sellers/")],
        sku="VP-HF-BALL")

if __name__ == "__main__":
    import sys
    build(sys.argv[1] if len(sys.argv) > 1 else "site")
