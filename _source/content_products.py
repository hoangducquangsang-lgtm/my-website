# -*- coding: utf-8 -*-
from common import page, write_page, rfq_bar, breadcrumb_html, BRAND

def faq_schema(pairs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}

def faq_html(pairs):
    items = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in pairs)
    return f'<section class="section"><div class="wrap"><h2>Frequently asked questions</h2>{items}</div></section>'

def product_schema(name, desc, img, category, brand=BRAND):
    return {
        "@context": "https://schema.org", "@type": "Product",
        "name": name, "description": desc, "image": img,
        "brand": {"@type": "Brand", "name": brand},
        "category": category,
        "manufacturer": {"@type": "Organization", "name": "WINVN INT CO., LTD"}
    }

def product_page(root, slug, parent_label, parent_href, name, meta_title, meta_desc, lede, hero_img,
                  specs_rows, faqs, related):
    bc, bc_s = breadcrumb_html([("Home","/"), (parent_label, parent_href), (name, None)])
    specs = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in specs_rows)
    rel = "".join(f'<a class="btn btn-outline" href="{r[1]}" style="margin-right:10px">{r[0]}</a>' for r in related)
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
<section class="section section-alt">
  <div class="wrap">
    <h3 class="mt0">You may also want</h3>
    {rel}
  </div>
</section>
"""
    html = page(meta_title, meta_desc, f"/products/{slug}/", content + faq_html(faqs) + rfq_bar(), "",
                [bc_s, faq_schema(faqs), product_schema(name, meta_desc, hero_img, parent_label)])
    write_page(root, f"/products/{slug}/", html)


def build(root):
    product_page(root, "coffee-wood-dog-chew", "Coffee Wood", "/collections/coffee-wood/",
        "Coffee Wood Dog Chew Stick",
        f"Coffee Wood Dog Chew | Wholesale & Private Label | {BRAND}",
        "Natural single-ingredient coffee wood dog chew, wholesale from Vietnam. Splinter-resistant, non-toxic, low MOQ from 50 pcs, laser engraving available.",
        "A single-ingredient chew cut from real Vietnamese coffee trees, naturally dried and finished to retail-ready standards. Available in six sizes matched to dog weight.",
        "/assets/img/product-coffeewood-stick.jpg",
        [("Material","100% coffee wood, no additives"),
         ("Sizes","XS (&lt;3kg) · S (3–5kg) · M (5–8kg) · L (8–12kg) · XL (12–20kg) · XXL (20kg+)"),
         ("Moisture","12–14%, factory-controlled"),
         ("MOQ","50 pcs per SKU"),
         ("Customisation","Laser logo engraving, custom label & packaging"),
         ("Lead time","15–20 working days standard, 25–30 OEM/ODM")],
        [("Are coffee wood chews safe for dogs?", "Yes — single natural material, no chemicals, finished splinter-resistant. Choose the correct size and supervise chewing as with any chew."),
         ("What sizes are available?", "Six sizes from XS to XXL, sized to dog weight from under 3kg to over 20kg. See our full size guide."),
         ("Can I laser-engrave my logo?", "Yes, directly onto the chew, as part of our OEM/private label service.")],
        [("Coffee Wood Collection","/collections/coffee-wood/"), ("Size Guide","/guides/coffee-wood-chew-size-guide/")])

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
        [("Coconut Fiber Collection","/collections/coconut-fiber/"), ("Cat Toys","/cat-toys/balls/")])

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
        [("Coconut Fiber Collection","/collections/coconut-fiber/"), ("Fetch & Ball Toys","/dog-toys/fetch-toys/")])

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
        [("Loofah Collection","/collections/loofah/"), ("Cat Toys","/cat-toys/catnip-toys/")])

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
        [("Hemp Fiber Collection","/collections/hemp-fiber/"), ("Amazon Sellers Solution","/solutions/amazon-sellers/")])
