# -*- coding: utf-8 -*-
from common import page, write_page, rfq_bar, breadcrumb_html, BRAND

ARTICLES = []  # (slug, cluster, title, meta_title, meta_desc, body_html, faqs, cta_href, cta_text)

def faq_schema(pairs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}

def faq_html(pairs):
    if not pairs: return ""
    items = "".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in pairs)
    return f'<div class="article">{items}</div>'

def add(slug, cluster, title, meta_title, meta_desc, body_html, faqs=None, cta_href="/request-a-quote/", cta_text="Request a Free Sample", img="/assets/img/hero-lifestyle-toys.jpg"):
    ARTICLES.append(dict(slug=slug, cluster=cluster, title=title, meta_title=meta_title,
                          meta_desc=meta_desc, body=body_html, faqs=faqs or [], cta_href=cta_href, cta_text=cta_text, img=img))

# ============================================================
# CLUSTER 1 — Natural Chew Toys
# ============================================================
add("natural-dog-chew-toys-guide", "Natural chew toys",
    "The Complete Guide to Natural Dog Chew Toys",
    f"The Complete Guide to Natural Dog Chew Toys | {BRAND}",
    "A wholesale buyer's guide to natural dog chew toys: materials, safety, sizing, and how to build a natural chew range that sells.",
    """
<p>"Natural chew" has become one of the fastest-growing categories in pet retail, and also one of the most confusing to buy for. Rawhide, bully sticks, antler, nylon, and now wood-based chews all claim the label. This guide breaks down what actually matters when you're deciding what to stock.</p>
<h2>What counts as a "natural" chew?</h2>
<p>A genuinely natural chew is made from a single, unprocessed or minimally processed material — wood, antler, dried plant fibre — with no synthetic binders, artificial flavouring, or chemical treatment. Products that use the word "natural" on packaging while containing processed hide, added flavouring, or plastic components are trading on the label without earning it.</p>
<h2>The main natural chew materials, compared</h2>
<table>
<tr><th>Material</th><th>Splinter risk</th><th>Sustainability story</th><th>Typical margin</th></tr>
<tr><td>Coffee wood</td><td>Low — wears into soft fibres</td><td>Strong (upcycled from retired trees)</td><td>Strong</td></tr>
<tr><td>Antler</td><td>Higher — can fracture into sharp shards</td><td>Moderate</td><td>Premium but volatile supply</td></tr>
<tr><td>Bully stick / rawhide</td><td>Choking risk from softened chunks</td><td>Weak — processing chemicals common</td><td>Thin, commoditised</td></tr>
<tr><td>Nylon</td><td>Low, but sheds micro-plastic</td><td>Weak — synthetic</td><td>Thin, commoditised</td></tr>
</table>
<p>Read the full comparison in <a href="/guides/coffee-wood-vs-antler-nylon-rawhide/">Coffee Wood vs Antler, Nylon &amp; Rawhide</a>.</p>
<h2>Sizing matters more than most retailers think</h2>
<p>The single most common cause of chew-related complaints isn't the material — it's the wrong size for the dog. A chew too small for a large, motivated chewer becomes a choking risk; a chew too large for a small dog just sits untouched. Match chew size to dog weight, and communicate that sizing clearly on pack.</p>
<h2>What to check before you stock a natural chew line</h2>
<ul class="check-list">
<li>Single-ingredient claim, verifiable against the supplier's documentation</li>
<li>Moisture control on wood products (12–14% prevents cracking and mould)</li>
<li>Export documentation — Certificate of Origin, Phytosanitary, Fumigation</li>
<li>A real factory behind the product, not a reseller repackaging unknown stock</li>
</ul>
<p>For a full vetting checklist, see <a href="/guides/how-to-vet-an-eco-pet-toy-supplier/">How to Vet an Eco Pet Toy Supplier</a>.</p>
""",
    [("What's the safest natural dog chew material?", "Coffee wood and properly finished antler are among the safer options; coffee wood has the added advantage of being single-ingredient and low splinter risk. Always size correctly regardless of material."),
     ("Are natural chews more expensive to stock?", "Materials cost varies, but natural chews with a genuine story typically support stronger retail margins than commoditised rawhide or nylon.")],
    img="/assets/img/dog-chewing-coffeewood.jpg")

add("are-coffee-wood-chews-safe-for-dogs", "Natural chew toys",
    "Are Coffee Wood Chews Safe for Dogs? What Retailers Should Know",
    f"Are Coffee Wood Chews Safe for Dogs? | {BRAND}",
    "Coffee wood chews are a natural, single-ingredient dog chew. Here's how they compare on safety, splintering, and caffeine — and what to check before stocking them.",
    """
<p>Short answer: yes, when they're made and sized correctly. Coffee wood has become one of the most popular natural chews in the pet trade, but if you're deciding whether to stock it, "popular" isn't enough — you need to understand why it's safe and what to check.</p>
<h2>Does coffee wood contain caffeine?</h2>
<p>This is the first question every buyer asks, and it's a fair one. The wood of the coffee tree is not the bean. Caffeine is concentrated in the coffee cherry and seed, not the trunk and branches. Chews are made from mature coffee timber, so the caffeine concern that applies to coffee grounds or beans doesn't carry over to the wood.</p>
<h2>What about splintering?</h2>
<p>Splintering is the real safety question with any hard chew. Coffee wood is a dense hardwood that tends to wear down into soft, fibrous strands rather than sharp shards — behaving very differently from bones or antlers, which can crack into dangerous points. No chew is indestructible: size the chew to the dog and remove it once it's small enough to swallow.</p>
<h2>Single-ingredient and chemical-free</h2>
<p>A quality coffee wood chew is 100% real coffee wood — one material, no glue, no additives, no artificial flavour, and no chemical smell out of the box. For pet parents scanning ingredient lists, "one ingredient" is a powerful and truthful claim.</p>
<h2>Why sourcing and QC matter for safety</h2>
<p>Safety isn't only about the material — it's about the batch. Ask your supplier how they control quality. The two things that matter most are moisture control (a 12–14% target prevents cracking and mould) and edge/surface finishing so there are no rough points.</p>
""",
    [("Do coffee wood chews have caffeine?", "No — caffeine is in the bean, not the timber. The chews are made from coffee-tree wood, with nothing added."),
     ("Can coffee wood splinter?", "It wears into soft fibres rather than sharp shards, but as with any chew, size it correctly and remove small pieces."),
     ("What makes one coffee wood chew safer than another?", "Proper moisture control (12–14%), edge finishing, and batch inspection, plus export and safety documentation.")],
    cta_href="/collections/coffee-wood/", cta_text="Browse the Coffee Wood Collection",
    img="/assets/img/product-coffeewood-single.jpg")

add("coffee-wood-vs-antler-nylon-rawhide", "Natural chew toys",
    "Coffee Wood vs Antler, Nylon & Rawhide Chews: A Retailer's Comparison",
    f"Coffee Wood vs Antler, Nylon & Rawhide Chews | {BRAND}",
    "A buyer's comparison of coffee wood, antler, nylon, and rawhide dog chews — on safety, durability, margin, and sustainability.",
    """
<p>Every natural pet buyer eventually has to decide which hard chew to build a range around. Here's how coffee wood stacks up against the three most common alternatives, from a retailer's point of view.</p>
<table>
<tr><th></th><th>Coffee Wood</th><th>Antler</th><th>Nylon</th><th>Rawhide</th></tr>
<tr><td>Material</td><td>Natural hardwood</td><td>Natural bone/antler</td><td>Synthetic plastic</td><td>Processed hide</td></tr>
<tr><td>Splinter risk</td><td>Low (soft fibres)</td><td>Higher (hard shards)</td><td>Low, but plastic bits</td><td>Choking on softened chunks</td></tr>
<tr><td>Sustainability story</td><td>Strong (upcycled)</td><td>Moderate</td><td>Weak (plastic)</td><td>Weak</td></tr>
<tr><td>Chemical-free</td><td>Yes</td><td>Yes</td><td>No</td><td>Often chemically treated</td></tr>
<tr><td>Retail margin</td><td>Strong</td><td>Premium but pricey</td><td>Thin, commoditised</td><td>Thin</td></tr>
</table>
<h2>Coffee wood</h2>
<p>Upcycled from retired coffee trees, single-ingredient, splinter-resistant, and long-lasting. Its standout advantage is the sustainability narrative — a story antler and nylon can't match and rawhide actively works against.</p>
<h2>Antler</h2>
<p>Genuinely natural and long-lasting, but harder on teeth and more prone to sharp fractures, and pricing is volatile because supply is seasonal. A fine premium add-on, but a risky sole anchor.</p>
<h2>Nylon</h2>
<p>Durable and cheap, but synthetic — it contradicts an eco range, sheds micro-plastic, and has become a commodity with thin margins.</p>
<h2>Rawhide</h2>
<p>The old default, now in decline: processing chemicals and choking risk have pushed both retailers and consumers away.</p>
<h2>The verdict for an eco range</h2>
<p>If you're building a natural, plastic-free range, coffee wood is the strongest anchor, with antler as an optional premium companion. Nylon and rawhide belong to the category coffee wood is replacing.</p>
""",
    [("Is coffee wood better than antler?", "For an eco range and everyday safety, yes — it splinters less and carries a stronger sustainability story. Antler works as a premium extra."),
     ("Why avoid rawhide?", "Processing chemicals and choking risk have made it a declining category, especially for natural-positioned shops.")],
    cta_href="/collections/coffee-wood/", cta_text="Browse the Coffee Wood Collection")

add("best-natural-chews-for-aggressive-chewers", "Natural chew toys",
    "Best Natural Chews for Aggressive Chewers",
    f"Best Natural Chews for Aggressive Chewers | Wholesale | {BRAND}",
    "Which natural chew materials and sizes hold up to power chewers — a sourcing guide for retailers stocking a heavy-duty natural range.",
    """
<p>"Aggressive chewer" is one of the highest-intent search phrases in the pet category — these buyers have already been through a pile of destroyed toys and are actively looking for something that lasts. Here's how to stock for them without overselling durability you can't back up.</p>
<h2>Why most "indestructible" claims fail</h2>
<p>No natural chew is truly indestructible, and claiming otherwise invites returns and bad reviews. What you can promise is relative durability and safe failure — a chew that wears down gradually into soft, swallowable-safe material rather than cracking into hazardous shards.</p>
<h2>What holds up best</h2>
<ul class="check-list">
<li><strong>Coffee wood, XL/XXL sizing</strong> — dense hardwood sized for dogs 12kg and up, wears down slowly rather than shattering</li>
<li><strong>Reinforced hemp fiber rope</strong> — high tensile strength for tug-of-war without synthetic fibres</li>
<li><strong>Avoid</strong> thin nylon and softened rawhide for this segment — both fail quickly under sustained power chewing</li>
</ul>
<h2>Sizing is the real safety lever</h2>
<p>For power chewers, undersized chews are the biggest risk — they get reduced to swallowable pieces fast. Always size up rather than down for confirmed aggressive chewers, and communicate a "supervise and replace" policy on pack. See our <a href="/guides/coffee-wood-chew-size-guide/">coffee wood size guide</a> for weight-to-size mapping.</p>
<h2>Merchandising this segment</h2>
<p>Aggressive-chewer buyers respond to specificity, not general "durable" claims. Lead with breed examples (Labrador, Shepherd, Bully breeds), size clearly, and set expectations that any chew should be supervised and retired once small enough to swallow.</p>
""",
    [("Is any natural chew truly indestructible?", "No — durability claims should be relative, not absolute. Coffee wood XL/XXL and reinforced hemp rope hold up well but should still be supervised."),
     ("What size should I recommend for a large power chewer?", "XL or XXL coffee wood, sized for dogs 12kg and above — see our full size guide.")],
    cta_href="/collections/aggressive-chewers/", cta_text="See the Aggressive Chewers Range")

add("how-long-do-coffee-wood-chews-last", "Natural chew toys",
    "How Long Do Coffee Wood Chews Last?",
    f"How Long Do Coffee Wood Chews Last? | {BRAND}",
    "A realistic look at coffee wood chew durability — what affects lifespan, and how to set customer expectations correctly.",
    """
<p>This is a fair question to ask before you stock any chew category, and the honest answer is: it depends on the dog. Here's what actually drives how long a coffee wood chew lasts, so you can set accurate expectations on pack and in listings.</p>
<h2>What affects lifespan</h2>
<ul class="check-list">
<li><strong>Chew intensity</strong> — a light nibbler and a power chewer will get very different mileage from the same chew</li>
<li><strong>Correct sizing</strong> — an undersized chew for the dog's strength gets consumed much faster</li>
<li><strong>Moisture and hardness</strong> — a well-dried chew (12–14% moisture) is denser and lasts longer than a poorly dried one</li>
<li><strong>Supervised vs. unsupervised chewing time</strong></li>
</ul>
<h2>Setting expectations without overselling</h2>
<p>Coffee wood typically outlasts soft, pressed and rawhide chews because it's a dense hardwood, but avoid absolute claims like "lasts for months" — that invites disappointment and returns from owners of strong chewers. A more accurate, defensible claim: "outlasts most soft and pressed chews; durability depends on your dog's chewing style."</p>
<h2>What to tell customers on pack</h2>
<p>The clearest guidance combines correct sizing with a simple safety rule: replace the chew once it's small enough to swallow, regardless of how long that takes. This protects both the dog and your review score.</p>
""",
    [("Does coffee wood last longer than rawhide?", "Generally yes, because it's a dense hardwood rather than a softened hide that breaks into chunks — but actual lifespan depends on the individual dog."),
     ("How do I know when to replace a coffee wood chew?", "Once it's worn down to a size the dog could swallow, it should be replaced regardless of how long it's lasted.")],
    cta_href="/collections/coffee-wood/", cta_text="Browse the Coffee Wood Collection")

# ============================================================
# CLUSTER 2 — Eco / Plastic-Free
# ============================================================
add("plastic-free-biodegradable-pet-toys-guide", "Eco / plastic-free",
    "Plastic-Free & Biodegradable Pet Toys: A Buyer's Guide",
    f"Plastic-Free & Biodegradable Pet Toys: A Buyer's Guide | {BRAND}",
    "What actually makes a pet toy plastic-free and biodegradable, and how to build a genuine eco range without greenwashing.",
    """
<p>"Eco-friendly" is one of the most overused claims in pet retail, and increasingly one that buyers — and regulators — scrutinise. This guide covers what actually makes a pet toy plastic-free and biodegradable, so you can stock (and market) with confidence.</p>
<h2>What "biodegradable" should actually mean</h2>
<p>A genuinely biodegradable toy breaks down through natural biological processes without leaving microplastics or persistent synthetic residue. That rules out most nylon, most nylon-blend rope, and any toy with plastic squeakers or reinforcement, even if the outer material is natural.</p>
<h2>Materials that qualify</h2>
<table>
<tr><th>Material</th><th>Biodegradable</th><th>Common use</th></tr>
<tr><td>Coffee wood</td><td>Yes</td><td>Dog chews</td></tr>
<tr><td>Coconut fiber</td><td>Yes</td><td>Balls, rope, substrate</td></tr>
<tr><td>Hemp fiber</td><td>Yes</td><td>Rope, tug toys</td></tr>
<tr><td>Loofah</td><td>Yes</td><td>Cat and small-pet toys</td></tr>
<tr><td>Nylon / polyester rope</td><td>No</td><td>Common in budget rope toys — often marketed as "natural-look"</td></tr>
</table>
<h2>Watch for greenwashing in your own supply chain</h2>
<p>A toy can use a natural-sounding material name while still containing plastic core, synthetic dye, or non-biodegradable stitching. Ask suppliers for material composition by weight, not just a headline material name. See <a href="/guides/are-dog-toys-biodegradable/">Are Dog Toys Biodegradable?</a> for a deeper checklist.</p>
<h2>Packaging counts too</h2>
<p>A biodegradable toy in a plastic clamshell undercuts the entire pitch. Kraft, vacuum-seal-only, or certified biodegradable packaging closes that gap — and increasingly, EU buyers ask about it directly. See <a href="/collections/plastic-free/">our plastic-free collection &rarr;</a>.</p>
""",
    [("Is coffee wood biodegradable?", "Yes — it's untreated natural hardwood with no synthetic additives."),
     ("What should I check before calling a product 'eco-friendly'?", "Material composition by weight, packaging materials, and any synthetic components like squeakers, stitching or reinforcement.")],
    cta_href="/collections/plastic-free/", cta_text="Browse the Plastic-Free Collection")

add("are-dog-toys-biodegradable", "Eco / plastic-free",
    "Are Dog Toys Biodegradable? A Buyer's Checklist",
    f"Are Dog Toys Biodegradable? A Buyer's Checklist | {BRAND}",
    "Most dog toys marketed as natural still contain non-biodegradable components. Here's how to check before you stock or claim it.",
    """
<p>Most dog toys are not biodegradable, even when marketed with earthy colours and natural-sounding names. Here's a practical checklist before you make (or trust) that claim.</p>
<h2>Check the full material list, not just the headline</h2>
<p>A "rope toy" might be listed as cotton, but woven around a plastic core, or finished with synthetic dye. A "wood chew" might be real wood glued to a synthetic handle. Ask for composition by weight and by component, not a single material name.</p>
<h2>Common non-biodegradable components hiding in "natural" toys</h2>
<ul class="check-list">
<li>Plastic squeakers inside stuffed or rope toys</li>
<li>Nylon-blend rope marketed as "natural fibre rope"</li>
<li>Synthetic stitching or reinforcement thread</li>
<li>Plastic-laminated tags or labels attached to the toy itself</li>
</ul>
<h2>Materials that pass the test</h2>
<p>Coffee wood, coconut fiber, hemp fiber and loofah — used without synthetic reinforcement — are fully biodegradable. That's the entire premise behind our range; see <a href="/materials/">our materials page</a> for how each is sourced.</p>
<h2>A simple question to ask any supplier</h2>
<p>"If I buried this in soil, what would still be there in five years?" A defensible biodegradable claim should have a short, honest answer: nothing, or close to it.</p>
""",
    [("Are rope toys usually biodegradable?", "Not always — many rope toys blend cotton with nylon or polyester, which doesn't biodegrade. Check composition by weight."),
     ("Does a natural material name guarantee biodegradability?", "No — check for hidden plastic components like squeakers, cores or synthetic stitching.")])

add("what-is-coconut-fiber-pet-toys", "Eco / plastic-free",
    "What Is Coconut Fiber, and Why Use It in Pet Toys?",
    f"What Is Coconut Fiber? Why It's Great for Natural Pet Toys | {BRAND}",
    "Coconut fiber is a biodegradable coconut-husk material used in pet balls, rope toys, and small-animal substrate. Here's why it's a strong material for eco pet ranges.",
    """
<p>If you're expanding a natural pet range beyond chews, coconut fiber is one of the most versatile — and underrated — materials available. Here's what it is and where it fits.</p>
<h2>What coconut fiber actually is</h2>
<p>Coconut fiber is the fibrous material from the husk of a coconut — the layer between the hard inner shell and the outer skin. It's a by-product of coconut farming that would otherwise be waste, which makes it both abundant and genuinely sustainable. Once cleaned and dried, it becomes a strong, springy natural fibre.</p>
<h2>Why it works for pets</h2>
<ul class="check-list">
<li>Biodegradable and plastic-free — a clean eco story for your packaging</li>
<li>Good moisture control — which is why it doubles as reptile and small-animal substrate</li>
<li>Naturally textured — satisfying for cats to bat and small animals to burrow and chew</li>
<li>Durable yet soft — holds up to play without hard edges</li>
</ul>
<h2>Product formats</h2>
<p>Coconut fiber shows up across a natural range as balls and chasers for cats and dogs, rope toys, and substrate for reptile and small-animal habitats. That versatility lets a retailer serve dog, cat and small-pet customers from a single sustainable material.</p>
<h2>What to check when sourcing</h2>
<p>Quality coconut fiber should be clean, well-dried and uniform — poorly dried fibre can hold moisture and develop odour. Ask your supplier about drying and inspection, and always request a sample to check texture and consistency.</p>
""",
    [("Is coconut fiber safe for pets?", "Yes — it's a natural, biodegradable coconut by-product with no chemicals when properly cleaned and dried."),
     ("What's coconut fiber used for?", "Cat and dog balls, rope toys, and substrate for reptiles and small animals.")],
    cta_href="/collections/coconut-fiber/", cta_text="Browse the Coconut Fiber Collection")

add("non-toxic-cat-toys-wholesale-buying-guide", "Eco / plastic-free",
    "Non-Toxic Cat Toys: What Retailers Should Look For",
    f"Non-Toxic Cat Toys: A Wholesale Buying Guide | {BRAND}",
    "What actually makes a cat toy non-toxic, and how to vet a supplier's claims before you stock a natural cat toy range.",
    """
<p>Cat owners scrutinise toy safety more than almost any other pet category, largely because cats mouth and chew toys directly. Here's what "non-toxic" should actually mean when you're sourcing.</p>
<h2>The three things that make a cat toy non-toxic</h2>
<ul class="check-list">
<li><strong>No added chemicals or dyes</strong> — natural fibre in its undyed or naturally-coloured state</li>
<li><strong>No small detachable parts</strong> — a real choking hazard in shaped toys like plush animals</li>
<li><strong>Verified material sourcing</strong> — a supplier who can document where the fibre comes from and how it's processed</li>
</ul>
<h2>Loofah as a non-toxic material</h2>
<p>Loofah — the dried interior of the loofah gourd — is naturally textured, chemical-free, and commonly used for dental chewing in cats. Its main safety consideration is the same as any shaped toy: check that attached elements (eyes, whiskers, tails) are stitched securely or avoided altogether in favour of a single-material design.</p>
<h2>Questions to ask before stocking a "non-toxic" cat toy line</h2>
<ul class="check-list">
<li>Is the base material single-ingredient, or a blend with synthetic reinforcement?</li>
<li>Are any dyes or scents added, and are they disclosed?</li>
<li>What safety testing has actually been run, versus just claimed?</li>
</ul>
<p>See our <a href="/collections/loofah/">loofah collection</a> for shape and sizing options, or <a href="/guides/pet-toy-safety-testing-requirements/">What Safety Tests Do Pet Toys Need?</a> for a testing overview.</p>
""",
    [("Is loofah safe for cats to chew?", "Yes — it's a natural, chemical-free plant fibre commonly used for dental chewing in cats and small animals."),
     ("What should I ask a supplier about non-toxic claims?", "Ask for material composition, any added dyes or scents, and what safety testing has actually been performed.")],
    cta_href="/collections/loofah/", cta_text="Browse the Loofah Collection")

add("sustainable-pet-toy-materials-compared", "Eco / plastic-free",
    "Sustainable Pet Toy Materials Compared",
    f"Sustainable Pet Toy Materials Compared | {BRAND}",
    "Coffee wood, coconut fiber, hemp fiber, loofah, bamboo and recycled plastic — how the main sustainable pet toy materials compare.",
    """
<p>"Sustainable" covers a wide range of materials with very different stories. Here's an honest comparison of the main options a natural pet range might use.</p>
<table>
<tr><th>Material</th><th>Source</th><th>Biodegradable</th><th>Best for</th></tr>
<tr><td>Coffee wood</td><td>Upcycled retired coffee trees</td><td>Yes</td><td>Dog chews</td></tr>
<tr><td>Coconut fiber</td><td>Coconut husk by-product</td><td>Yes</td><td>Balls, rope, substrate</td></tr>
<tr><td>Hemp fiber</td><td>Hemp plant fibre</td><td>Yes</td><td>Rope, tug toys</td></tr>
<tr><td>Loofah</td><td>Dried loofah gourd</td><td>Yes</td><td>Cat and small-pet toys</td></tr>
<tr><td>Bamboo</td><td>Fast-growing grass</td><td>Yes, if untreated</td><td>Rigid chew shapes</td></tr>
<tr><td>Recycled plastic</td><td>Post-consumer plastic</td><td>No</td><td>Durable toys, not biodegradable</td></tr>
</table>
<h2>Upcycled vs. simply renewable</h2>
<p>There's a meaningful difference between a material that's renewable (like bamboo, which is fast-growing but still newly harvested) and one that's upcycled from an existing waste stream (like coffee wood, from trees already removed from production, or coconut fiber, a farming by-product). Upcycled materials generally have a stronger, more defensible sustainability story because they don't require new cultivation.</p>
<h2>Recycled plastic: sustainable, but not biodegradable</h2>
<p>Recycled plastic toys reduce new plastic production, which is a real sustainability benefit — but they are not biodegradable and will still shed microplastic over their lifespan. Don't conflate "made from recycled material" with "eco-friendly" in the same way as a biodegradable natural material.</p>
<h2>Building a mixed-material eco shelf</h2>
<p>The strongest eco ranges combine a hero material (coffee wood or coconut fiber) with a supporting line (hemp fiber, loofah), giving a retailer breadth across dog, cat and small-pet categories from genuinely biodegradable materials. See <a href="/materials/">our full materials page &rarr;</a>.</p>
""",
    [("Is bamboo more sustainable than coffee wood?", "Both are defensible; coffee wood has the added advantage of being upcycled from trees already removed from coffee production, rather than newly harvested."),
     ("Is recycled plastic an eco-friendly material?", "It reduces new plastic production, but it isn't biodegradable and will still shed microplastic — a different sustainability trade-off than natural fibre.")])

# ============================================================
# CLUSTER 3 — Sourcing & Supplier
# ============================================================
add("sourcing-eco-pet-toys-vietnam", "Sourcing & supplier",
    "Sourcing Eco Pet Toys from Vietnam: A Wholesale Buyer's Guide",
    f"Sourcing Eco Pet Toys from Vietnam: Buyer's Guide | {BRAND}",
    "How pet brands and importers source natural, biodegradable pet toys from Vietnam — materials, MOQs, compliance, lead times, and how to vet a supplier.",
    """
<p>The natural pet-toy category is growing fast, and buyers are increasingly looking beyond the usual manufacturing hubs. Vietnam has quietly become one of the best places in the world to source genuinely sustainable pet toys. This guide walks through what's available, what to check, and how to run a first order.</p>
<h2>Why Vietnam for natural pet toys</h2>
<p>Vietnam offers three things that matter to a natural-pet buyer at once. First, raw materials: it's a major producer of coffee, coconut and loofah, so the base materials for eco toys are abundant, local and cheap to source. Second, a clean origin story: with US and EU scrutiny on tariffs and forced-labor compliance, sourcing with proper Certificates of Origin keeps your imports defensible. Third, craftsmanship at a workable cost, which is why many natural products here are handcrafted rather than moulded from plastic.</p>
<h2>The core materials, and what each is good for</h2>
<ul class="check-list">
<li><strong>Coffee wood</strong> — dense hardwood chews upcycled from retired coffee trees. Splinter-resistant, long-lasting, single-ingredient. Best for dog chew ranges.</li>
<li><strong>Coconut fiber</strong> — coconut husk fibre. Used for balls, rope toys, and small-animal/reptile substrates.</li>
<li><strong>Hemp fiber</strong> — durable natural fibre for ropes and ball toys, well suited to tug and multi-dog play.</li>
<li><strong>Loofah</strong> — the dried fibrous gourd. Light, biodegradable, ideal for cat and small-animal chew-and-play toys.</li>
</ul>
<h2>Understanding MOQs</h2>
<p>One of the biggest myths about overseas sourcing is that you need to commit to huge quantities. Look for suppliers with a low, flexible MOQ — ours starts at 50 pcs per SKU — so you can pilot a product, prove sell-through, and only then scale.</p>
<h2>Compliance: what to ask for before you buy</h2>
<p>Never place an order without confirming the paperwork. At minimum, a credible Vietnamese supplier should provide a Certificate of Origin, phytosanitary certificate, fumigation certificate, and an independent inspection report. If your market needs CPSIA (US) or REACH (EU) testing, confirm the supplier can arrange it and get scope in writing per SKU.</p>
<h2>Lead times and delivery, realistically</h2>
<p>Standard production typically runs 15–20 working days, and custom OEM/ODM work 25–30 working days. From dispatch, sea and air freight to Europe and the Americas generally takes 10–20 days.</p>
<h2>How to vet a supplier in five steps</h2>
<ol class="steps">
<li>Order a sample first — never judge from photos.</li>
<li>Check the documentation — ask to see real CO, phytosanitary, and inspection reports.</li>
<li>Confirm QC process — for wood, ask about moisture control (12–14% target).</li>
<li>Test communication — clear, fast, honest updates now predict how a bulk order will go.</li>
<li>Start small — a low-MOQ pilot before bulk protects your capital and your shelf.</li>
</ol>
""",
    [("What's the minimum order to source pet toys from Vietnam?", "It varies by supplier. We keep ours low — from 50 pcs per SKU — so brands can pilot before committing to bulk."),
     ("Is it hard to import pet toys from Vietnam?", "No, provided your supplier gives you the right documents: Certificate of Origin, phytosanitary and fumigation certificates, and an inspection report cover most import requirements."),
     ("How long does a first order take?", "Roughly 15–20 working days for standard production or 25–30 for custom work, plus 10–20 days freight to Europe or the Americas.")],
    cta_href="/capabilities/", cta_text="See Our Capabilities")

add("natural-dog-toy-manufacturer-vietnam", "Sourcing & supplier",
    "How to Choose a Natural Dog Toy Manufacturer in Vietnam",
    f"How to Choose a Natural Dog Toy Manufacturer in Vietnam | {BRAND}",
    "A practical checklist for vetting a Vietnamese natural pet toy manufacturer — MOQ, OEM capability, certifications, QC, and communication.",
    """
<p>Vietnam has dozens of workshops making natural pet products, and quality varies widely. If you're placing your brand — and your customers' safety — in a supplier's hands, here's how to separate a real manufacturing partner from a middleman.</p>
<h2>1. Do they actually manufacture, or just resell?</h2>
<p>Ask direct questions about the factory: location, size, and capacity. A genuine maker can tell you where the facility is, how big it is, and how batches are produced. A reseller will be vague. Only a real manufacturer can control quality and offer true customisation.</p>
<h2>2. Is the MOQ realistic for a pilot?</h2>
<p>Modern brands launch small. Look for a low, flexible MOQ so you can test a product before committing capital. A manufacturer geared only for container-loads isn't set up for how you actually grow.</p>
<h2>3. Can they do true OEM / private label?</h2>
<p>If you're building a brand, "can I put my logo on it" is only the start. A strong partner offers custom packaging, labelling, laser engraving, and product-shape development, plus a fast prototype.</p>
<h2>4. What documentation and QC do they provide?</h2>
<p>Never skip this. Require export documents (Certificate of Origin, phytosanitary, fumigation, inspection report) and a clear QC process — for wood, that means moisture control at 12–14% and edge finishing. Willingness to accept a third-party audit is a strong trust signal.</p>
<h2>5. How do they communicate?</h2>
<p>This is the quiet predictor of everything. Clear, fast, honest updates during sampling tell you how a bulk order will go.</p>
<h2>The five-point checklist</h2>
<ol class="steps">
<li>Real factory (location, size, capacity)</li>
<li>Low, flexible MOQ for pilots</li>
<li>Genuine OEM / private-label capability</li>
<li>Full export docs + documented QC</li>
<li>Clear, responsive communication</li>
</ol>
""",
    [("How do I verify a Vietnamese pet toy factory is real?", "Ask for factory location, size, and capacity; request export documents and a QC walkthrough; and welcome a third-party audit."),
     ("What's a reasonable first order?", "A low-MOQ pilot — ours starts at 50 pcs per SKU — with a sample first, before scaling to bulk.")],
    cta_href="/about/", cta_text="See Our Factory")

add("wholesale-coconut-fiber-cat-toys-supplier", "Sourcing & supplier",
    "Finding a Wholesale Coconut Fiber Cat Toys Supplier",
    f"Wholesale Coconut Fiber Cat Toys Supplier | {BRAND}",
    "What to look for in a coconut fiber cat toy supplier — quality signs, MOQ, and how to avoid inconsistent batches.",
    """
<p>Coconut fiber has become a go-to material for eco cat toy ranges, but supplier quality varies a lot — some coconut fiber balls fall apart within weeks, others hold up for months. Here's what separates a reliable supplier from a risky one.</p>
<h2>Signs of a well-made coconut fiber toy</h2>
<ul class="check-list">
<li>Tightly wound fibre with no loose, fraying strands out of the box</li>
<li>Uniform colour and texture across a batch — inconsistency signals poor drying or sorting</li>
<li>No synthetic binding thread mixed into the natural fibre</li>
<li>A clean, dry smell — mustiness signals a moisture problem</li>
</ul>
<h2>Why moisture control matters here too</h2>
<p>Coconut fiber that's poorly dried before manufacturing can hold residual moisture, leading to odour and mould risk during shipping and storage — the same failure mode as under-dried wood chews. Ask suppliers directly about their drying and inspection process before ordering.</p>
<h2>MOQ and format flexibility</h2>
<p>Coconut fiber suits multiple formats — balls, rope toys, and small-animal substrate — from a single material stream. A supplier who can flex MOQ per format (rather than requiring the same minimum across every SKU) is easier to build a first order around.</p>
<h2>Questions to ask before you order</h2>
<ul class="check-list">
<li>What's your drying process, and how do you check for residual moisture?</li>
<li>Can I get a mixed sample across ball, rope and substrate formats?</li>
<li>What documentation ships with the order for customs clearance?</li>
</ul>
""",
    [("How do I know if coconut fiber is well-made?", "Check for tight winding, uniform colour, no synthetic binding thread, and a clean dry smell — not musty."),
     ("What's the MOQ for coconut fiber cat toys?", "Typically 50–100 pcs per SKU, though rope and substrate formats may be quoted differently.")],
    cta_href="/collections/coconut-fiber/", cta_text="Browse the Coconut Fiber Collection")

add("private-label-oem-eco-pet-toys-explained", "Sourcing & supplier",
    "Private Label / OEM Eco Pet Toys, Explained",
    f"Private Label & OEM Eco Pet Toys Explained | {BRAND}",
    "The difference between OEM and private label, what's actually customisable on natural pet toys, and how the process works.",
    """
<p>"OEM" and "private label" get used almost interchangeably in pet sourcing conversations, but they mean different things — and knowing the difference helps you brief a supplier correctly.</p>
<h2>Private label vs. OEM vs. ODM</h2>
<ul class="check-list">
<li><strong>Private label</strong> — you put your branding (logo, label, packaging) on an existing product design.</li>
<li><strong>OEM (Original Equipment Manufacturer)</strong> — the manufacturer produces to your specification, using their existing production capability.</li>
<li><strong>ODM (Original Design Manufacturer)</strong> — the manufacturer co-develops a new product design with you, not just branding an existing one.</li>
</ul>
<p>Most natural pet toy brands start with private label on an existing SKU (fastest, lowest MOQ), then move to ODM once a product proves out and they want an exclusive shape or format.</p>
<h2>What's actually customisable on natural materials</h2>
<ul class="check-list">
<li><strong>Coffee wood</strong> — size, shape, and laser-engraved logo directly on the wood</li>
<li><strong>Coconut fiber &amp; hemp fiber</strong> — size, shape, colour blend, and label/tag branding</li>
<li><strong>Loofah</strong> — custom shapes and catnip-fill options</li>
<li><strong>Packaging</strong> — kraft, vacuum-seal, or fully biodegradable, with custom printing</li>
</ul>
<h2>What a private-label project actually costs in time</h2>
<p>Expect roughly a week for a free sample, a few days for a custom prototype once you confirm a brief, and 25–30 working days for full OEM/ODM production once the design is locked. Budget for this timeline when planning a launch date.</p>
<h2>A common mistake: skipping the prototype step</h2>
<p>Approving from photos alone, without a physical prototype, is the single most common cause of a disappointing first production run. Always confirm a physical sample before committing to bulk. See <a href="/capabilities/">our full OEM/ODM capabilities &rarr;</a>.</p>
""",
    [("What's the difference between private label and OEM?", "Private label puts your branding on an existing product; OEM produces to your specification using the manufacturer's existing capability; ODM co-develops a new design with you."),
     ("How long does a private label project take?", "Roughly a week for a sample, a few days for a custom prototype, and 25–30 working days for full production once the design is confirmed.")],
    cta_href="/capabilities/", cta_text="Start a Private-Label Project")

add("pet-toy-moq-fob-pricing-lead-times", "Sourcing & supplier",
    "Pet Toy MOQ, FOB Pricing & Lead Times, Explained",
    f"Pet Toy MOQ, FOB Pricing & Lead Times Explained | {BRAND}",
    "What MOQ, FOB, EXW and CIF actually mean for pet toy sourcing, and realistic lead times to plan your launch around.",
    """
<p>If you're new to importing, the shorthand suppliers use — MOQ, FOB, EXW, CIF — can obscure more than it explains. Here's what each term actually means for your order.</p>
<h2>MOQ (Minimum Order Quantity)</h2>
<p>The smallest quantity a supplier will produce or sell per SKU. Many established factories default to MOQs in the thousands; newer or more flexible suppliers may offer 50–100 pcs per SKU specifically to support pilot orders. Always ask whether MOQ applies per SKU or across a whole order — the difference matters a lot for a multi-product range.</p>
<h2>Incoterms: EXW, FOB, CIF</h2>
<table>
<tr><th>Term</th><th>What it means</th><th>Who arranges freight</th></tr>
<tr><td>EXW (Ex Works)</td><td>You collect from the factory door</td><td>You (or your forwarder)</td></tr>
<tr><td>FOB (Free on Board)</td><td>Supplier delivers to the export port, loaded</td><td>You, from the port onward</td></tr>
<tr><td>CIF (Cost, Insurance, Freight)</td><td>Supplier arranges freight and insurance to your destination port</td><td>Supplier, port-to-port</td></tr>
</table>
<p>New importers often start with CIF or FOB with a freight forwarder recommendation from the supplier, then move to EXW once they have their own logistics relationships.</p>
<h2>Realistic lead times</h2>
<ul class="check-list">
<li>Sample: about 7 days</li>
<li>Standard production: 15–20 working days</li>
<li>Custom OEM/ODM production: 25–30 working days</li>
<li>Freight to Europe or the Americas: 10–20 days after dispatch</li>
</ul>
<p>Build a buffer into your launch calendar, especially for a first order with a new supplier. See our full <a href="/how-to-order/">How to Order</a> page for the complete process.</p>
""",
    [("What does FOB mean in pet toy sourcing?", "The supplier delivers goods to the export port, loaded onto the vessel; you (or your forwarder) arrange onward shipping."),
     ("How long should I budget for a first order?", "Roughly 3–5 weeks for production depending on standard vs. custom, plus 10–20 days freight — build in a buffer for a first order with any new supplier.")],
    cta_href="/how-to-order/", cta_text="See How to Order")

# ============================================================
# CLUSTER 4 — Compliance & Risk
# ============================================================
add("pet-toy-safety-compliance-cpsia-reach", "Compliance & risk",
    "Pet Toy Safety & Compliance for Importers (CPSIA, REACH)",
    f"Pet Toy Safety & Compliance for Importers (CPSIA, REACH) | {BRAND}",
    "What CPSIA, REACH and other pet toy compliance frameworks require, and how to get the right documentation from your supplier.",
    """
<p>Pet toys generally face lighter regulation than children's toys, but that doesn't mean compliance doesn't matter — retailers, marketplaces and customs authorities increasingly expect documentation, and a supplier who can't provide it is a real business risk.</p>
<h2>CPSIA (United States)</h2>
<p>The Consumer Product Safety Improvement Act primarily governs children's products, but many US retailers and marketplaces apply similar lead and phthalate testing standards to pet products as a due-diligence baseline, especially for items that could be mouthed by children as well as pets. Ask your supplier whether CPSIA-equivalent testing is available and what it covers.</p>
<h2>REACH (European Union)</h2>
<p>REACH restricts hazardous chemical substances in products sold in the EU. For natural, single-ingredient materials like coffee wood, coconut fiber, hemp fiber and loofah, REACH compliance is generally straightforward since there's no chemical treatment to test — but any dyed, scented or treated variant should have REACH documentation on request.</p>
<h2>What documentation to request</h2>
<ul class="check-list">
<li>Material composition declaration (by weight, by component)</li>
<li>Any third-party lab test reports already on file (SGS, Intertek, or equivalent)</li>
<li>Confirmation of no added chemical treatment, dye, or fragrance — or disclosure if present</li>
<li>Certificate of Origin and phytosanitary/fumigation certificates for the shipment itself</li>
</ul>
<h2>A practical approach for a new SKU</h2>
<p>Confirm testing scope and cost per SKU before production, not after. Retrofitting compliance testing onto an already-produced batch is slower and more expensive than building it into the order from the start.</p>
""",
    [("Do pet toys need CPSIA certification?", "Not always required by law, but many US retailers and marketplaces expect equivalent safety testing as due diligence — ask your supplier what's available."),
     ("Are natural materials automatically REACH compliant?", "Untreated single-ingredient materials are generally straightforward, but any dyed, scented, or treated variant should have documentation confirmed on request.")],
    cta_href="/certifications/", cta_text="See Our Certifications")

add("sourcing-pet-toys-vietnam-vs-china", "Compliance & risk",
    "Sourcing Pet Toys: Vietnam vs China (Tariffs, UFLPA & Risk)",
    f"Sourcing Pet Toys: Vietnam vs China (Tariffs & UFLPA) | {BRAND}",
    "Why pet brands are diversifying pet-toy sourcing from China to Vietnam — tariff exposure, UFLPA forced-labor risk, materials, and how to make the switch.",
    """
<p>For years, China was the default for pet-toy manufacturing. That's changing fast — not because China can't make product, but because the risk attached to China-origin goods has climbed for US and EU importers. Here's an honest look at the trade-offs.</p>
<h2>The tariff picture</h2>
<p>China-origin goods carry meaningful and, lately, unpredictable tariff exposure for US importers, and rates have shifted repeatedly. Vietnam-origin goods generally sit in a more stable position, which is a large part of why brands are diversifying. Confirm current tariff rates for your product's HS code before you commit — rates change, and this article won't age well as a source of exact numbers.</p>
<h2>Forced-labor compliance (UFLPA)</h2>
<p>Under the US Uyghur Forced Labor Prevention Act (UFLPA), goods made wholly or in part in the Xinjiang region — or by listed entities — face a presumption of forced labor and can be detained at the border. Proving a clean supply chain back through Chinese sub-suppliers is difficult and expensive. Sourcing from Vietnam, with clear Certificates of Origin and documented supply chains, sidesteps that exposure.</p>
<h2>Materials advantage</h2>
<p>Vietnam isn't just a China alternative — for natural pet toys it's arguably the better origin. It's a major producer of coffee, coconut and loofah, so the raw materials for eco toys are local and abundant rather than imported. That means shorter material supply chains and a more authentic sustainability story.</p>
<h2>Where China may still win</h2>
<p>Be balanced: for high-volume, highly-moulded plastic or electronic toys, China's scale and tooling ecosystem can still be cheaper per unit. If your range is synthetic and volume is enormous, China may price lower. But for natural, handcrafted, eco-positioned ranges, Vietnam usually wins on both risk and story.</p>
<h2>Making the switch</h2>
<p>You don't have to move everything at once. Most brands pilot a natural line from Vietnam — low MOQ, a sample, a small first order — while keeping existing supply running, then shift volume as the new line proves out.</p>
""",
    [("Is it cheaper to source pet toys from Vietnam or China?", "For natural, handcrafted toys, Vietnam is often more competitive once tariff and compliance risk are factored in. For high-volume moulded plastic, China can still be cheaper per unit."),
     ("What is UFLPA and why does it matter?", "A US law creating a presumption that goods linked to the Xinjiang region are made with forced labor and can be blocked at the border. Vietnam-origin goods with clear documentation avoid this exposure.")],
    cta_href="/certifications/", cta_text="See Our Certifications & Compliance")

add("pet-toy-safety-testing-requirements", "Compliance & risk",
    "What Safety Tests Do Pet Toys Need?",
    f"What Safety Tests Do Pet Toys Need? | {BRAND}",
    "An overview of the safety tests commonly requested for pet toys, and when each one is actually necessary.",
    """
<p>Unlike children's toys, pet toys don't have one single mandatory global testing standard — which means test requirements vary by market, retailer and product type. Here's a practical overview.</p>
<h2>Physical safety tests</h2>
<ul class="check-list">
<li><strong>Small parts / choking hazard assessment</strong> — especially relevant for shaped toys with attached elements</li>
<li><strong>Tensile strength testing</strong> — for rope and tug toys, to confirm they won't fail catastrophically under load</li>
<li><strong>Sharp edge / splinter assessment</strong> — relevant for wood and rigid chews</li>
</ul>
<h2>Chemical safety tests</h2>
<ul class="check-list">
<li><strong>Heavy metals (lead, cadmium)</strong> — often requested even for natural materials, as a baseline due-diligence check</li>
<li><strong>Phthalates</strong> — relevant mainly for any synthetic or dyed component, not untreated natural fibre</li>
<li><strong>Fumigation / pest treatment verification</strong> — required for plant-based goods crossing many borders, separate from a "safety" test but equally necessary for customs</li>
</ul>
<h2>When testing is actually required vs. optional</h2>
<p>Amazon and other marketplaces increasingly request test documentation as part of listing approval for certain pet categories, even without a legal mandate. EU retailers may ask for REACH documentation specifically. US retailers may ask for CPSIA-equivalent testing. Confirm your specific channel's requirement before ordering — don't assume a general "safety tested" claim covers a specific retailer's ask.</p>
<h2>Who runs these tests</h2>
<p>Independent labs such as SGS or Intertek are the most commonly recognised for pet product testing. A supplier who readily arranges third-party testing (rather than only offering in-house results) is a stronger trust signal.</p>
""",
    [("Do pet toys legally require safety testing?", "There's no single mandatory global standard, but individual markets, retailers and marketplaces increasingly request specific documentation — confirm your channel's requirement directly."),
     ("Who should run pet toy safety tests?", "Independent, internationally recognised labs such as SGS or Intertek are the most commonly accepted for pet product testing.")],
    cta_href="/certifications/", cta_text="See Our Certifications")

add("how-to-vet-an-eco-pet-toy-supplier", "Compliance & risk",
    "How to Vet an Eco Pet Toy Supplier",
    f"How to Vet an Eco Pet Toy Supplier | {BRAND}",
    "A step-by-step checklist for verifying an eco pet toy supplier before you commit — from sample to factory audit.",
    """
<p>"Eco" claims are easy to print on packaging and hard to verify from a listing page. Here's a step-by-step process for vetting a supplier before you commit real order volume.</p>
<h2>Step 1: Request a sample before anything else</h2>
<p>Never judge material quality, texture, or finish from photos alone. A credible supplier offers a free or low-cost sample — if a supplier won't send one, that's a signal on its own.</p>
<h2>Step 2: Ask for real documentation, not just claims</h2>
<p>Request an actual Certificate of Origin, phytosanitary certificate, and inspection report — not a description of what they "can" provide. Vague answers here are the single biggest red flag in supplier vetting.</p>
<h2>Step 3: Confirm they're a manufacturer, not a reseller</h2>
<p>Ask directly about factory location, size, and production capacity. A real manufacturer answers specifically; a reseller repackaging unknown stock tends to stay vague or deflect.</p>
<h2>Step 4: Test their QC process, not just their claims</h2>
<p>Ask what happens between raw material intake and a finished, packed product. A supplier with a real, describable QC process (moisture checks, size sorting, batch inspection) is meaningfully more reliable than one who just says "we check everything."</p>
<h2>Step 5: Test communication before you test volume</h2>
<p>How a supplier communicates during a small first order — speed, clarity, honesty about delays — is the most reliable predictor of how they'll handle a larger one.</p>
<h2>A final gut check</h2>
<p>Would this supplier welcome a third-party factory audit? Willingness (not necessarily the audit itself) is one of the strongest trust signals in international sourcing.</p>
""",
    [("What's the single most important thing to check first?", "Request a real sample before making any other judgment — photos and claims don't substitute for handling the actual material."),
     ("How do I know if a supplier is a real manufacturer?", "Ask specific questions about factory location, size and capacity — real manufacturers answer directly; resellers tend to stay vague.")],
    cta_href="/certifications/", cta_text="Request Our Compliance Documents")

# ============================================================
# BONUS — Size guide (linked from product pages)
# ============================================================
add("coffee-wood-chew-size-guide", "Natural chew toys",
    "Coffee Wood Chew Size Guide: Matching Size to Dog Weight",
    f"Coffee Wood Chew Size Guide by Dog Weight & Breed | {BRAND}",
    "A full size guide for coffee wood dog chews — six sizes matched to dog weight and breed, for retailers and buyers.",
    """
<p>Sizing is the single biggest factor in both safety and satisfaction with a coffee wood chew. Undersized chews get consumed too fast (and pose a choking risk); oversized chews go untouched. Here's the full breakdown.</p>
<table>
<tr><th>Size</th><th>Dog weight</th><th>Example breeds</th></tr>
<tr><td>XS</td><td>Up to 3kg</td><td>Chihuahua, Maltese, Pomeranian, Yorkshire Terrier</td></tr>
<tr><td>S</td><td>3–5kg</td><td>Yorkshire Terrier, Bichon Frise, King Charles Spaniel, Miniature Poodle</td></tr>
<tr><td>M</td><td>5–8kg</td><td>Bichon Frise, Dachshund, Jack Russell Terrier, Pug, Shih Tzu</td></tr>
<tr><td>L</td><td>8–12kg</td><td>Dachshund, Cocker Spaniel, French Bulldog, Poodle, Sheltie, Shiba</td></tr>
<tr><td>XL</td><td>12–20kg</td><td>Beagle, Akita, Samoyed, Husky, Shar-Pei, Labrador</td></tr>
<tr><td>XXL</td><td>20kg and up</td><td>Chow-Chow, Boxer, Weimaraner, Bull Terrier, large Labrador/Husky</td></tr>
</table>
<h2>When to size up rather than down</h2>
<p>For confirmed strong or "aggressive" chewers, size up one level regardless of weight — a large, motivated chewer can reduce an appropriately-sized-by-weight chew to a swallowable piece faster than a light chewer of the same size. See our <a href="/guides/best-natural-chews-for-aggressive-chewers/">guide for aggressive chewers</a>.</p>
<h2>Merchandising sizing clearly</h2>
<p>Retailers who print a simple weight-to-size chart directly on pack see fewer sizing-related returns and complaints than those who leave sizing to guesswork. Use the table above as a starting template for your own packaging.</p>
""",
    [("How do I choose the right coffee wood chew size?", "Match the dog's weight to the size chart above, and size up one level for confirmed strong or aggressive chewers."),
     ("What sizes are available?", "Six sizes: XS, S, M, L, XL and XXL, covering dogs from under 3kg to over 20kg.")],
    cta_href="/products/coffee-wood-dog-chew/", cta_text="See Coffee Wood Chew Specifications")


def build(root):
    # ---- Guides hub ----
    bc, bc_s = breadcrumb_html([("Home","/"), ("Guides", None)])
    clusters = {}
    for a in ARTICLES:
        clusters.setdefault(a["cluster"], []).append(a)
    hub_sections = ""
    for cluster, arts in clusters.items():
        cards = "".join(
            f'<div class="card guide-card"><span class="tag tag-terracotta">{cluster}</span>'
            f'<h3><a href="/guides/{a["slug"]}/">{a["title"]}</a></h3>'
            f'<p>{a["meta_desc"]}</p></div>'
            for a in arts
        )
        hub_sections += f'<section class="section"><div class="wrap"><h2>{cluster}</h2><div class="grid grid-3">{cards}</div></div></section>'
    content = f"""
{bc}
<section class="hero" style="padding:40px 0 48px">
  <div class="wrap">
    <p class="hero-eyebrow">Guides &amp; Resources</p>
    <h1>Sourcing Guides for Natural Pet Toy Buyers</h1>
    <p class="hero-lede">Practical, no-fluff guides on materials, safety, compliance and sourcing — written for brand owners, Amazon sellers, retailers and importers.</p>
  </div>
</section>
{hub_sections}
"""
    html = page(f"Guides & Resources | Natural Pet Toy Sourcing | {BRAND}",
        "Practical guides on natural pet toy materials, safety, compliance and sourcing from Vietnam — for brand owners, Amazon sellers, retailers and importers.",
        "/guides/", content + rfq_bar(), "Guides", [bc_s])
    write_page(root, "/guides/", html)

    # ---- Individual articles ----
    for a in ARTICLES:
        bc, bc_s = breadcrumb_html([("Home","/"), ("Guides","/guides/"), (a["title"], None)])
        cta = f'<div class="callout"><strong>Ready to see it for yourself?</strong> <a href="{a["cta_href"]}">{a["cta_text"]} &rarr;</a></div>'
        content = f"""
{bc}
<article class="section">
  <div class="wrap article">
    <p class="tag tag-terracotta">{a['cluster']}</p>
    <h1>{a['title']}</h1>
    {a['body']}
    {cta}
  </div>
</article>
{faq_html(a['faqs'])}
"""
        schemas = [bc_s]
        if a["faqs"]:
            schemas.append(faq_schema(a["faqs"]))
        schemas.append({"@context":"https://schema.org","@type":"Article","headline":a["title"],
                         "description":a["meta_desc"]})
        html = page(a["meta_title"], a["meta_desc"], f"/guides/{a['slug']}/",
                    content + rfq_bar(), "Guides", schemas, og_image=a["img"])
        write_page(root, f"/guides/{a['slug']}/", html)
