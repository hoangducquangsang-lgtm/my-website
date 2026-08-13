# -*- coding: utf-8 -*-
from common import page, write_page, rfq_bar, breadcrumb_html, BRAND

def cat_page(root, path, parent_label, parent_href, h1, meta_title, meta_desc, lede, img, cards, active_top):
    bc, bc_s = breadcrumb_html([("Home","/"), (parent_label, parent_href), (h1, None)] if parent_href else [("Home","/"), (h1, None)])
    card_html = "".join(
        f'<div class="card"><div class="card-img"><img src="{c[2]}" alt="{c[0]}"></div><h3>{c[0]}</h3><p>{c[1]}</p><a href="{c[3]}">Explore &rarr;</a></div>'
        for c in cards
    )
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap hero-inner">
    <div>
      <p class="hero-eyebrow">Wholesale</p>
      <h1>{h1}</h1>
      <p class="hero-lede">{lede}</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="/request-a-quote/">Request Wholesale Catalogue</a>
      </div>
    </div>
    <img src="{img}" alt="{h1}">
  </div>
</section>
<section class="section">
  <div class="wrap grid grid-3">{card_html}</div>
</section>
"""
    html = page(meta_title, meta_desc, path, content + rfq_bar(), active_top, [bc_s])
    write_page(root, path, html)


def build(root):
    cat_page(root, "/dog-toys/", "", "", "Wholesale Natural Dog Toys",
        f"Wholesale Natural Dog Toys | Made in Vietnam | {BRAND}",
        "Wholesale natural, biodegradable dog toys from Vietnam — coffee wood chews, coconut fiber balls, hemp fiber ropes. Low MOQ, OEM & private label, free samples.",
        "Chew toys, rope toys, fetch balls and enrichment toys, all made from natural, biodegradable materials sourced in Vietnam.",
        "/assets/img/dog-chewing-coffeewood.jpg",
        [("Chew Toys","Coffee wood chews, splinter-resistant and single-ingredient.","/assets/img/product-coffeewood-stick.jpg","/dog-toys/chew-toys/"),
         ("Rope & Tug Toys","Hemp fiber rope for tug and multi-dog play.","/assets/img/product-hemp-rope-trio.jpg","/dog-toys/rope-toys/"),
         ("Fetch & Ball Toys","Coconut fiber balls, biodegradable and durable.","/assets/img/product-coconut-ball-sizes.jpg","/dog-toys/fetch-toys/"),
         ("Puzzle & Enrichment","Natural enrichment shapes for mental stimulation.","/assets/img/product-hemp-dumbbell.jpg","/dog-toys/puzzle-toys/")],
        "Dog Toys")

    cat_page(root, "/dog-toys/chew-toys/", "Dog Toys", "/dog-toys/", "Natural Dog Chew Toys Wholesale",
        f"Natural Dog Chew Toys Wholesale | Coffee Wood | {BRAND}",
        "Wholesale natural dog chew toys from Vietnam, led by splinter-resistant coffee wood. Single-ingredient, low MOQ, OEM & private label available.",
        "Our chew range is led by coffee wood — a dense, splinter-resistant hardwood upcycled from retired coffee trees.",
        "/assets/img/dog-chewing-coffeewood.jpg",
        [("Coffee Wood Chew Stick","Six sizes, XS–XXL, matched to dog weight.","/assets/img/product-coffeewood-stick.jpg","/products/coffee-wood-dog-chew/"),
         ("For Aggressive Chewers","Extra-dense sizing for strong chewers.","/assets/img/product-coffeewood-single.jpg","/collections/aggressive-chewers/"),
         ("For Teething Puppies","Gentler sizing for young dogs.","/assets/img/dog-lifestyle-chew-1.jpg","/collections/teething-puppies/")],
        "Dog Toys")

    cat_page(root, "/dog-toys/rope-toys/", "Dog Toys", "/dog-toys/", "Natural Rope & Tug Dog Toys Wholesale",
        f"Natural Rope & Tug Dog Toys Wholesale | Hemp Fiber | {BRAND}",
        "Wholesale hemp fiber rope and tug dog toys from Vietnam. Durable natural fibre, plastic-free, low MOQ, OEM & private label.",
        "Hemp fiber twisted into rope balls, tug ropes and knotted bones — built for tug-of-war and multi-dog households.",
        "/assets/img/dog-rope-toy-lifestyle.jpg",
        [("Hemp Fiber Ball","A tough rope ball for tug and fetch.","/assets/img/product-hemp-ball.jpg","/products/hemp-fiber-ball/"),
         ("Hemp Rope Trio","Three sizes of knotted rope toys.","/assets/img/product-hemp-rope-trio.jpg","/collections/hemp-fiber/")],
        "Dog Toys")

    cat_page(root, "/dog-toys/fetch-toys/", "Dog Toys", "/dog-toys/", "Natural Fetch & Ball Dog Toys Wholesale",
        f"Natural Fetch & Ball Dog Toys Wholesale | Coconut Fiber | {BRAND}",
        "Wholesale natural fetch and ball dog toys from Vietnam, made from coconut fiber. Biodegradable, plastic-free, low MOQ, private label.",
        "Coconut fiber balls in three sizes — light enough to fetch, tough enough to last.",
        "/assets/img/puppy-ball-lifestyle.jpg",
        [("Coconut Fiber Dog Ball","Three sizes, biodegradable coconut fiber.","/assets/img/product-coconut-ball-sizes.jpg","/products/coconut-fiber-dog-ball/")],
        "Dog Toys")

    cat_page(root, "/dog-toys/puzzle-toys/", "Dog Toys", "/dog-toys/", "Natural Enrichment & Puzzle Dog Toys Wholesale",
        f"Natural Enrichment & Puzzle Dog Toys | Wholesale | {BRAND}",
        "Wholesale natural enrichment and puzzle dog toys from Vietnam. Eco materials, engaging designs, low MOQ, OEM & private label.",
        "Shape and texture-driven natural toys that reward chewing and nosing, without a shred of plastic.",
        "/assets/img/product-hemp-dumbbell.jpg",
        [("Hemp Dumbbell","A knotted natural enrichment shape.","/assets/img/product-hemp-dumbbell.jpg","/collections/hemp-fiber/")],
        "Dog Toys")

    cat_page(root, "/cat-toys/", "", "", "Wholesale Natural Cat Toys",
        f"Wholesale Natural Cat Toys | Loofah & Coconut Fiber | {BRAND}",
        "Natural, biodegradable cat toys wholesale from Vietnam — loofah, coconut fiber balls. Low MOQ from 50 pcs, private label, free samples.",
        "Loofah and coconut fiber toys shaped for the way cats actually play — batting, chasing and dental chewing.",
        "/assets/img/cat-loofah-toys-lifestyle.jpg",
        [("Balls & Chasers","Coconut fiber balls for batting and chasing.","/assets/img/product-coconut-ball-sizes.jpg","/cat-toys/balls/"),
         ("Catnip & Chew Toys","Loofah shapes for dental chewing and play.","/assets/img/product-loofah-basket.jpg","/cat-toys/catnip-toys/")],
        "Cat Toys")

    cat_page(root, "/cat-toys/balls/", "Cat Toys", "/cat-toys/", "Coconut Fiber Cat Balls Wholesale",
        f"Coconut Fiber Cat Balls Wholesale | Natural & Plastic-Free | {BRAND}",
        "Wholesale coconut fiber cat balls and chasers from Vietnam. Biodegradable, plastic-free, naturally textured. Low MOQ, private label.",
        "Light, springy coconut fiber balls sized for batting and chasing.",
        "/assets/img/product-coconut-ball-sizes.jpg",
        [("Coconut Fiber Cat Ball","Naturally textured, biodegradable.","/assets/img/product-coconut-ball-sizes.jpg","/products/coconut-fiber-cat-ball/")],
        "Cat Toys")

    cat_page(root, "/cat-toys/catnip-toys/", "Cat Toys", "/cat-toys/", "Natural Catnip & Chew Cat Toys Wholesale",
        f"Natural Catnip & Chew Cat Toys Wholesale | Loofah | {BRAND}",
        "Wholesale natural loofah chew toys for cats, made in Vietnam. Biodegradable, safe, low MOQ, OEM & private label.",
        "Loofah shapes built for dental chewing, with catnip-fill options available on OEM runs.",
        "/assets/img/cat-loofah-toys-lifestyle.jpg",
        [("Loofah Cat Toy","Mouse, fish, rabbit and more shapes.","/assets/img/product-loofah-basket.jpg","/products/loofah-cat-toy/")],
        "Cat Toys")

    # ---------- niche collections ----------
    cat_page(root, "/collections/aggressive-chewers/", "Materials", "/materials/", "Natural Dog Toys for Aggressive Chewers",
        f"Natural Dog Toys for Aggressive Chewers | Wholesale | {BRAND}",
        "Wholesale natural, durable dog toys for aggressive chewers — led by tough coffee wood. Splinter-resistant, low MOQ, OEM & private label.",
        "Extra-dense coffee wood sizing and reinforced hemp rope for dogs with strong jaws and high chew drive.",
        "/assets/img/dog-chewing-coffeewood.jpg",
        [("Coffee Wood XL/XXL","Sized for strong chewers 12kg+.","/assets/img/product-coffeewood-stick.jpg","/products/coffee-wood-dog-chew/"),
         ("Hemp Rope Bones","Reinforced knotted rope for tug.","/assets/img/product-hemp-rope-trio.jpg","/collections/hemp-fiber/")],
        "Materials")

    cat_page(root, "/collections/teething-puppies/", "Materials", "/materials/", "Natural Teething Toys for Puppies",
        f"Natural Teething Toys for Puppies | Wholesale | {BRAND}",
        "Wholesale natural, safe teething toys for puppies from Vietnam. Gentle materials, low MOQ, OEM & private label for pet brands.",
        "Smaller, softer-edged coffee wood and coconut fiber shapes sized for developing jaws.",
        "/assets/img/dog-lifestyle-chew-1.jpg",
        [("Coffee Wood XS/S","Sized for puppies and toy breeds.","/assets/img/product-coffeewood-single.jpg","/products/coffee-wood-dog-chew/")],
        "Materials")

    cat_page(root, "/collections/plastic-free/", "Materials", "/materials/", "Plastic-Free & Biodegradable Pet Toys",
        f"Plastic-Free & Biodegradable Pet Toys | Wholesale | {BRAND}",
        "Wholesale plastic-free, biodegradable pet toys from Vietnam — coffee wood, coconut fiber, hemp fiber & loofah. Low MOQ, OEM & private label.",
        "Every material across our range is biodegradable and upcycled — a genuine eco shelf, not a greenwashed one.",
        "/assets/img/hero-lifestyle-toys.jpg",
        [("Coffee Wood","Upcycled hardwood dog chews.","/assets/img/product-coffeewood-stick.jpg","/collections/coffee-wood/"),
         ("Coconut Fiber","Biodegradable balls & rope.","/assets/img/product-coconut-ball-sizes.jpg","/collections/coconut-fiber/"),
         ("Hemp Fiber","Plastic-free tug & rope.","/assets/img/product-hemp-ball.jpg","/collections/hemp-fiber/"),
         ("Loofah","Biodegradable cat & small-pet toys.","/assets/img/product-loofah-basket.jpg","/collections/loofah/")],
        "Materials")
