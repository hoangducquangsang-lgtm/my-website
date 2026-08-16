# -*- coding: utf-8 -*-
from common import page, write_page, rfq_bar, breadcrumb_html, BRAND

def faq_schema(pairs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}

def faq_html(pairs):
    items = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in pairs)
    return f'<section class="section"><div class="wrap"><h2>Frequently asked questions</h2>{items}</div></section>'

def order_table(rows):
    trs = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in rows)
    return f'<table>{trs}</table>'

def collection_page(root, slug, title, meta, h1, lede, hero_img, body_sections, faqs, order_rows, product_type="dog"):
    bc, bc_s = breadcrumb_html([("Home","/"), ("Materials", "/materials/"), (h1, None)])
    body = "".join(body_sections)
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap hero-inner">
    <div>
      <p class="hero-eyebrow">Wholesale &amp; Private Label</p>
      <h1>{h1}</h1>
      <p class="hero-lede">{lede}</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="/request-a-quote/">Request a Free Sample</a>
        <a class="btn btn-outline" href="/request-a-quote/">Request a Quote</a>
      </div>
    </div>
    <img src="{hero_img}" alt="{h1}">
  </div>
</section>
{body}
<section class="section section-alt">
  <div class="wrap">
    <h2>Order terms at a glance</h2>
    {order_table(order_rows)}
  </div>
</section>
"""
    html = page(title, meta, f"/collections/{slug}/", content + faq_html(faqs) + rfq_bar(), "Materials",
                [bc_s, faq_schema(faqs)], og_image=hero_img)
    write_page(root, f"/collections/{slug}/", html)


def build(root):
    # ---------- COFFEE WOOD ----------
    body = [f"""
<section class="section">
  <div class="wrap grid grid-2">
    <div>
      <h2 class="mt0">What makes coffee wood different</h2>
      <p>Coffee wood is a dense hardwood that behaves nothing like rawhide, nylon or pressed chews. It splinters far less than antler or bone, lasts through repeated chewing sessions, and carries a faint natural aroma with no chemicals, no additives, and no artificial flavour.</p>
      <ul class="check-list">
        <li>100% real coffee wood — one material, nothing added</li>
        <li>Non-toxic and splinter-resistant — wears into soft fibres, not sharp shards</li>
        <li>Naturally odourless — no chemical smell out of the box</li>
        <li>Long-lasting — outlasts most soft and pressed chews</li>
        <li>Upcycled from retired coffee trees — a sustainability story buyers pay more for</li>
      </ul>
    </div>
    <img src="/assets/img/dog-chewing-coffeewood.jpg" alt="Dog chewing a coffee wood dog chew">
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>Sizes &amp; formats</h2>
    <p>Available in six sizes (XS&ndash;XXL) matched to dog weight from under 3&nbsp;kg to over 20&nbsp;kg, plus stick and bone formats. Custom sizing and laser engraving of your logo directly on the chew are available on OEM runs. <a href="/guides/coffee-wood-chew-size-guide/">See the full size guide &rarr;</a></p>
    <img src="/assets/img/product-coffeewood-stick.jpg" alt="Coffee wood chew sticks in a range of sizes">
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>Your wholesale &amp; private label coffee wood dog chew supplier</h2>
    <p>{BRAND} is the export brand of WINVN INT CO., LTD, a real coffee wood dog chew manufacturer in Vietnam's Central Highlands &mdash; not a trading middleman. Because we own production across three factories, we control quality, sizing and customisation end to end, and back every order with export documentation you can verify. Whether you're a pet retailer, eco shop, Amazon FBA seller or private-label brand, you buy direct from the factory. <a href="/pet-toys-manufacturer-vietnam/">See our full manufacturing capabilities &rarr;</a></p>
  </div>
</section>
<section class="section section-alt">
  <div class="wrap grid grid-2">
    <img src="/assets/img/process-moisture-check.jpg" alt="Worker checking the moisture of coffee wood with a calibrated meter">
    <div>
      <h2 class="mt0">Quality control &amp; export compliance</h2>
      <p>Every batch passes our five-stage QC &mdash; raw material, in-process, semi-finished, final product and pre-shipment inspection &mdash; with moisture held at 12&ndash;14% by calibrated meters to prevent cracking and mold in transit. Defective goods are covered by a 1-for-1 replacement policy, and CPSIA (US) or REACH (EU) testing is available on request. Certificate of Origin (incl. EUR1), phytosanitary, fumigation and inspection reports ship with every order. <a href="/certifications/">See certifications &amp; compliance &rarr;</a></p>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>Shop the coffee wood range</h2>
    <div class="grid grid-3">
      <div class="card"><div class="card-img"><img src="/assets/img/product-coffeewood-stick.jpg" alt="Coffee wood dog chew stick, six sizes"></div><h3>Coffee Wood Dog Chew Stick</h3><p>Six sizes XS&ndash;XXL, single-ingredient, laser engraving available.</p><a href="/products/coffee-wood-dog-chew/">View product &rarr;</a></div>
      <div class="card"><div class="card-img"><img src="/assets/img/product-coffeewood-single.jpg" alt="Dense coffee wood chew for aggressive chewers"></div><h3>For Aggressive Chewers</h3><p>Extra-dense XL/XXL sizing for dogs with strong jaws.</p><a href="/collections/aggressive-chewers/">Explore &rarr;</a></div>
      <div class="card"><div class="card-img"><img src="/assets/img/dog-lifestyle-chew-1.jpg" alt="Smaller coffee wood chew for teething puppies"></div><h3>For Teething Puppies</h3><p>Gentler XS/S sizing for developing jaws.</p><a href="/collections/teething-puppies/">Explore &rarr;</a></div>
    </div>
  </div>
</section>
"""]
    faqs = [
        ("Are coffee wood chews safe for dogs?", "Yes. They're made from a single natural material — real coffee wood — with no chemicals or additives, and finished to be splinter-resistant. As with any chew, supervise your dog and choose the correct size for their breed."),
        ("What is the minimum order quantity?", "Our MOQ starts at 50 pcs per SKU, kept deliberately low so new brands can test the market before scaling."),
        ("Can I put my own brand on the chews?", "Yes. We offer full private-label service including custom packaging and laser engraving of your logo directly onto the product."),
        ("How long do the chews last?", "Coffee wood is a dense hardwood that typically outlasts soft, pressed and rawhide chews, though longevity depends on the dog's size and chewing style."),
    ]
    order_rows = [("MOQ","From 50 pcs per SKU (low & flexible for pilots)"),
                  ("Samples","Trial Box of 3–5 free samples — you cover shipping, refunded on your first order"),
                  ("Sample lead time","Ready in ~7 days"),
                  ("Production","Standard 15–20 working days · OEM/ODM 25–30 working days"),
                  ("Private label","Logo, label, packaging & laser engraving available")]
    collection_page(root, "coffee-wood",
        f"Coffee Wood Dog Chews — Wholesale & Private Label | {BRAND}",
        "Wholesale coffee wood dog chews made in Vietnam from upcycled coffee trees. Natural, non-toxic, splinter-resistant. Low MOQ from 50 pcs, OEM/private label, free samples.",
        "Coffee Wood Dog Chews, Made for Brands That Sell Natural",
        "A single-ingredient chew your customers can trust and your buyers can price with confidence. Cut from real Vietnamese coffee trees, naturally dried, and finished to retail-ready standards.",
        "/assets/img/product-coffeewood-single.jpg", body, faqs, order_rows)

    # ---------- COCONUT FIBER ----------
    body = [f"""
<section class="section">
  <div class="wrap grid grid-2">
    <div>
      <h2 class="mt0">Why coconut fiber belongs in your range</h2>
      <p>Coconut fiber is the husk of the coconut — a farming by-product that would otherwise be waste. Cleaned and dried, it becomes a strong, springy, naturally textured fibre pets love to chase, chew and bat around.</p>
      <ul class="check-list">
        <li>100% biodegradable &amp; plastic-free</li>
        <li>Naturally textured — satisfying for cats to bat and small animals to burrow and chew</li>
        <li>Good moisture control — doubles as reptile and small-animal substrate</li>
        <li>Durable yet soft — holds up to play without hard edges</li>
        <li>One material, three customers — dog, cat and small-pet buyers from a single line</li>
      </ul>
    </div>
    <img src="/assets/img/dog-coconut-balls-lifestyle.jpg" alt="Dog playing with coconut fiber ball toys">
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>The formats we make</h2>
    <p>Balls and chasers for cats and dogs in three sizes, rope toys, and substrate for reptile and small-animal habitats. This range lets a retailer build a full natural shelf across pet types without adding another supplier.</p>
    <img src="/assets/img/product-coconut-ball-sizes.jpg" alt="Coconut fiber balls in three sizes">
  </div>
</section>
"""]
    faqs = [
        ("Is coconut fiber safe for pets?", "Yes — it's a natural, biodegradable coconut by-product with no chemicals when properly cleaned and dried."),
        ("What can coconut fiber be used for?", "Cat and dog balls, rope toys, and substrate for reptiles and small animals."),
        ("What's the minimum order?", "From 50 pcs per SKU, kept low so you can pilot before scaling."),
        ("Can I private-label coconut fiber products?", "Yes — with custom packaging and labelling to match your brand."),
    ]
    order_rows = [("MOQ","From 50 pcs per SKU (rope & substrate quoted per format)"),
                  ("Samples","Trial Box of 3–5 free samples — you cover shipping, refunded on your first order"),
                  ("Sample lead time","Ready in ~7 days"),
                  ("Production","Standard 15–20 working days · OEM/ODM 25–30 working days"),
                  ("Private label","Logo, label & eco packaging available")]
    collection_page(root, "coconut-fiber",
        f"Coconut Fiber Pet Toys Wholesale | {BRAND}",
        "Wholesale coconut fiber pet products from Vietnam — cat & dog balls, rope toys, substrate. Biodegradable, plastic-free, low MOQ, OEM & private label.",
        "Coconut Fiber Pet Products, Made for a Plastic-Free Shelf",
        "One versatile, biodegradable material — cat and dog balls, rope toys, and small-animal substrate, all upcycled from coconut husks and finished to retail standards.",
        "/assets/img/product-coconut-fiber-raw.jpg", body, faqs, order_rows)

    # ---------- HEMP FIBER ----------
    body = [f"""
<section class="section">
  <div class="wrap grid grid-2">
    <div>
      <h2 class="mt0">Built for tug, not just chew</h2>
      <p>Hemp fiber is twisted into rope and ball toys that hold up to the hardest play: tug-of-war, fetch, and multi-dog households. It's a tough, plastic-free alternative to synthetic rope toys, and fully biodegradable at end of life.</p>
      <ul class="check-list">
        <li>High tensile strength — built for tug and group play</li>
        <li>Plastic-free rope, no synthetic fibres</li>
        <li>Pairs naturally with coffee wood or coconut fiber cores</li>
        <li>Biodegradable, unlike nylon or polyester rope toys</li>
      </ul>
    </div>
    <img src="/assets/img/dog-rope-toy-lifestyle.jpg" alt="Dog playing with a hemp fiber rope toy">
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>The formats we make</h2>
    <p>Rope balls, tug ropes and knotted bone shapes in three sizes, sized for small to large dogs. <a href="/collections/aggressive-chewers/">See our range for aggressive chewers &rarr;</a></p>
    <img src="/assets/img/product-hemp-rope-trio.jpg" alt="Hemp fiber rope toys in three sizes">
  </div>
</section>
"""]
    faqs = [
        ("Is hemp fiber safe for dogs to chew and tug?", "Yes — it's a natural plant fibre with no synthetic additives, though as with any rope toy, supervise play and retire worn toys."),
        ("How is hemp fiber different from coconut fiber?", "Hemp fiber is a longer, tougher strand better suited to tug and rope formats; coconut fiber is shorter and springier, better suited to balls and chasers."),
        ("What's the minimum order?", "From 50 pcs per SKU."),
    ]
    order_rows = [("MOQ","From 50 pcs per SKU"),
                  ("Samples","Trial Box of 3–5 free samples — you cover shipping, refunded on your first order"),
                  ("Sample lead time","Ready in ~7 days"),
                  ("Production","Standard 15–20 working days · OEM/ODM 25–30 working days"),
                  ("Private label","Logo tag, label & eco packaging available")]
    collection_page(root, "hemp-fiber",
        f"Hemp Fiber Rope Pet Toys Wholesale | {BRAND}",
        "Wholesale hemp fiber rope and ball pet toys from Vietnam. Durable natural fibre for tug and play, plastic-free, low MOQ, OEM & private label.",
        "Hemp Fiber Rope &amp; Ball Toys, Built for Real Play",
        "A tough, plastic-free natural fibre twisted into rope and ball toys for tug-of-war, fetch and multi-dog households.",
        "/assets/img/product-hemp-ball.jpg", body, faqs, order_rows)

    # ---------- LOOFAH ----------
    body = [f"""
<section class="section">
  <div class="wrap grid grid-2">
    <div>
      <h2 class="mt0">Light, playful, fully biodegradable</h2>
      <p>Loofah is the dried, fibrous interior of the loofah gourd — grown and processed in Vietnam. It's naturally lightweight and textured, which makes it a favourite shape-driven material for cat toys and small-animal chew toys.</p>
      <ul class="check-list">
        <li>100% natural, biodegradable plant fibre</li>
        <li>Naturally rough texture — great for dental chewing in cats and small pets</li>
        <li>Lightweight — easy to bat, carry and toss</li>
        <li>Shaped into playful forms: mouse, teddy bear, fish, rabbit, duck, bone and more</li>
      </ul>
    </div>
    <img src="/assets/img/cat-loofah-toys-lifestyle.jpg" alt="Cat playing with loofah toys">
  </div>
</section>
<section class="section section-alt">
  <div class="wrap">
    <h2>Shapes we make</h2>
    <p>Mouse, teddy bear, fish, fish-with-tail, rabbit, duck, bone and character shapes, in heights from roughly 4&ndash;16&nbsp;cm. Loofah is also available cut into simple chew-stick rolls for small animals. Custom shapes are available on OEM runs.</p>
    <img src="/assets/img/product-loofah-basket.jpg" alt="Assorted loofah toy shapes in a basket">
  </div>
</section>
"""]
    faqs = [
        ("Is loofah safe for cats and small animals?", "Yes — loofah is a natural, biodegradable plant fibre with a gentle-but-textured surface, commonly used for dental chewing in cats, rabbits and other small pets."),
        ("What shapes are available?", "Mouse, teddy bear, fish, fish-with-tail, rabbit, duck, bone and other character shapes, plus plain chew-stick rolls."),
        ("What's the minimum order?", "From 100 pcs per SKU, given the shaped-molding process — ask about mixed-shape trial cartons for smaller pilots."),
    ]
    order_rows = [("MOQ","From 100 pcs per SKU (mixed-shape trial cartons available)"),
                  ("Samples","Trial Box of 3–5 free samples — you cover shipping, refunded on your first order"),
                  ("Sample lead time","Ready in ~7 days"),
                  ("Production","Standard 15–20 working days · OEM/ODM 25–30 working days"),
                  ("Private label","Custom shapes, tags & eco packaging available")]
    collection_page(root, "loofah",
        f"Loofah Pet Toys Wholesale | Biodegradable Cat Toys | {BRAND}",
        "Wholesale loofah pet toys from Vietnam — biodegradable cat and small-animal toys in mouse, fish, rabbit and other shapes. Low MOQ, OEM & private label, free samples.",
        "Loofah Pet Toys &mdash; Biodegradable &amp; Playful",
        "Handcrafted in Vietnam from dried loofah gourd fibre. Fully biodegradable, naturally textured, and shaped into playful forms cats and small pets love.",
        "/assets/img/raw-loofah-gourd.jpg", body, faqs, order_rows)
