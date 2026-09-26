# -*- coding: utf-8 -*-
from content_helpers import (publish, section, p, ul, table, terms, trust_links, SAFETY, MOISTURE,
                             answer, fit, steps, spec_table, figure, media, CARTON, SEA_TRANSIT,
                             INCOTERMS, PAYMENT, CAFFEINE, WEAR_BEHAVIOUR, SIZE_ADVICE)
from content_products import product_cards

MATERIALS = {
"coffee-wood":dict(
 title="Coffee Wood Dog Chew Manufacturer | Wholesale | VietPaw",
 h1="Coffee Wood Dog Chews — Wholesale from Vietnam",
 lede="Build a coffee wood range with our own factory in Vietnam: standard chew sticks, custom wood-and-rope constructions and private-label packaging for international buyers.",
 image="coffee-wood-chew-grain-detail.jpg",products=["coffee-wood-dog-chew","gorilla-coffee-wood-dog-chew"],
 what="Coffee wood chews are shaped pieces of coffee-tree timber, not coffee beans or edible treats. VietPaw's product information identifies mature coffee wood from Gia Lai and describes cutting, bark removal, surface finishing and drying.",
 applications=[("Standard sticks","Start with a focused size assortment using the CC01 reference specification. Each size is a separate ordering decision."),
 ("Wood-and-rope designs","Discuss cotton or hemp rope variants, component declarations and connection checks; they are not single-material sticks."),
 ("Branded retail range","Add laser engraving, size labels, safety instructions and a pack format suited to the sales channel.")],
 approval=["Request the current size sheet and physical sample; older charts use different weight bands.",
 MOISTURE+" Confirm the measurement method and keep the reading with your order records.",
 "Check wood surfaces and visible cracking, and agree the condition in which stock is packed and stored."],
 caution="Do not describe coffee wood as splinter-free, edible, caffeine-tested or proven to clean teeth without evidence for that exact claim. A natural origin is not a safety guarantee: size the chew to the dog, supervise and replace it when damaged.",
 moq="From 50 pcs per SKU on standard sticks. Engraving, rope combinations and custom boxes are quoted separately."),
"coconut-fiber":dict(
 title="Coconut Fiber Pet Toys Manufacturer & Wholesale | VietPaw",
 h1="Coconut Fiber Pet Toys for Wholesale & Private Label",
 lede="Source coconut-husk fiber balls and discuss rope constructions for a textured natural-material range. Separate cat and dog specifications, then approve winding, dimensions and packaging.",
 image="coconut-fiber-ball-top-view.jpg",products=["coconut-fiber-dog-ball","coconut-fiber-cat-ball"],
 what="Coconut fiber, also called coir, comes from the coconut husk. The supplied product material describes preparation, drying and shaping for pet-toy formats. A finished ball may have additional components that must be declared before a whole-product claim is made.",
 applications=[("Dog balls","Specify diameter, finished weight and the intended fetch/carry use; evaluate the actual sample."),
 ("Cat balls","Create a separate cat-range specification and check for detachable or loose components."),
 ("Rope and other coir toys","Ask about current designs; each construction is specified on its own sample.")],
 approval=["Ask how the fiber is prepared and dried, including any treatment that must be declared.",
 "Check binding, core construction, strand shedding and natural variation against the sample.",
 "Agree packing dryness and storage instructions; no universal moisture number is claimed for every coir design."],
 caution="Coir toys are not dietary fiber or a hairball treatment. Loose fiber and damaged pieces should not be encouraged for ingestion.",
 moq="Request MOQ per ball size or rope format. Selected standard products start from 50 pcs; mixed-product orders still need line-by-line confirmation."),
"hemp-fiber":dict(
 title="Hemp Pet Toy Manufacturer | Rope & Balls Wholesale | VietPaw",
 h1="Hemp Fiber Pet Toys — Wholesale Rope & Ball Formats",
 lede="Develop a hemp-fiber assortment with standalone balls, knotted ropes and mixed-material designs. Match construction to supervised play and document the approved specification.",
 image="hemp-rope-balls-three-sizes.jpg",products=["hemp-fiber-ball","hemp-rope-dog-toy"],
 what="Hemp fiber is a plant fiber used for wound balls and rope constructions in VietPaw's product range. Catalogues identify ball diameter bands, while rope length and knot details are design-specific. Fiber identity and any blends need to be confirmed for the chosen product.",
 applications=[("Standalone balls","The catalogue lists S 4–5 cm, M 6–7 cm and L 8–9 cm diameter bands; confirm current dimensions."),
 ("Tug formats","Define rope length, diameter, handle opening and knot construction on the sample."),
 ("Coffee wood combinations","List wood, rope and any connector separately. Approve the connection rather than assuming a material's strength proves the whole toy.")],
 approval=["Confirm whether the rope is hemp, cotton, coir or a blend; the materials are not interchangeable.",
 "Specify the knot or attachment check and acceptance criteria; do not infer a tensile rating from appearance.",
 "Review fraying, loose strands and pack warnings for supervised use."],
 caution="The product is a fiber toy, not a CBD product, antimicrobial treatment or dental remedy. Avoid advertising comparative strength or breath-freshening effects without relevant product evidence.",
 moq="Selected standard hemp products start from 50 pcs. Custom rope geometry, mixed-material assemblies and branded boxes are quoted by project."),
"loofah":dict(
 title="Loofah Pet Toy Manufacturer | Cat Toys Wholesale | VietPaw",
 h1="Loofah Pet Toys for Wholesale & Private Label",
 lede="Create a lightweight cat-toy range from dried loofah-gourd fiber. Choose shapes, define attachments and approve packaging for your own retail or marketplace brand.",
 image="vietpaw-loofah-growing.png",products=["loofah-cat-toy"],
 what="Loofah is the fibrous interior of a mature gourd, not a sea sponge. Our supplied product sheet describes drying, cutting and shaping the fiber into toy forms. Shape, stitching and filling determine the finished specification.",
 applications=[("Cat play shapes","Discuss fish, mouse or other available shapes, with each design measured separately."),
 ("Brand-specific designs","Provide a drawing, target dimensions and attachment restrictions for an OEM/ODM feasibility review."),
 ("Catnip or other filling","Treat filling as an optional, separately specified component with its own source and labeling needs.")],
 approval=["Confirm the selected shape's dimensions rather than applying a single size range to the entire collection.",
 "Check cleanliness, dryness, seams and decorative parts against the approved sample.",
 "Confirm thread, filling, colors and labels before making composition or disposal claims."],
 caution="Loofah's plant origin does not prove that the entire toy or its packaging is compostable. It is not food, and suitability for cats does not automatically establish suitability for rabbits, hamsters or other species.",
 moq="MOQ is quoted per shape and construction. Ask about a trial assortment; do not assume a mixed carton automatically meets each SKU minimum."),
}


IMG = "/assets/img/"

# Per-collection editorial blocks. Only the collections in the current content
# brief carry the expanded structure; the rest keep the shared layout.
DEEP = {}

DEEP["coffee-wood"] = dict(
 title="Coffee Wood Dog Chews — Material, Process & Wholesale | VietPaw",
 h1="Coffee Wood for Dog Chews",
 lede="Seasoned Robusta coffee stem from Vietnam's Central Highlands, graded into six sizes and packed below 14% moisture. What the material is, how it is processed, and what it cannot be claimed to do.",
 image=IMG+"vietpaw-coffee-wood-sizes.png",
 blocks=lambda: [
  section("What coffee wood is",
    answer("Coffee wood is the woody stem of the coffee plant — in our case mature Robusta grown in Vietnam's Central Highlands, principally Dak Lak, Gia Lai and Dak Nong. Growers take out the trees that have stopped paying their way and leave the rest alone, so the stems reaching us are material that already existed and previously had a low-value use as firewood. Nobody fells a coffee tree that is still yielding cherries, and no forest is cleared for this product.")
    +p("One consequence matters for anyone writing product copy: coffee is a crop, not a commercial timber species, so it has no entry in the timber databases that publish density and Janka hardness. Olive wood, by contrast, has both (roughly 980 kg/m³ dried and around 2,710 lbf). If you see a hardness figure quoted for coffee wood, it is an estimate rather than a measurement.")
    +media(p("What we can describe is what the material does on the line. Green stems are heavy, dark and flexible; after their holding period — roughly a year — the same stems are pale, light and hard. Density still varies stem to stem, which is why sizes are graded into bands rather than machined to a number, and why two sticks of the same size will not weigh the same.")
           +ul(["Single untreated plant material in the standard stick: no glue, coating, preservative or colouring.",
                "Sourced from Dak Lak, Gia Lai and Dak Nong in the Central Highlands.",
                "Graded into six diameter bands, XS to XXL.",
                "Packed below 14% moisture, with the reading recorded per batch."]),
           IMG+"coffee-stem-diameter-caliper-check.jpg",
           "Caliper measuring the diameter of a mature coffee stem still on the plant",
           "Stem diameter is checked at source. It sets which size band a piece can become — the stem decides, not the machine.")),

  section("From plantation to sealed carton",
    p("Five checkpoints sit between a raw stem and a sealed carton. We publish the sequence but treats drying temperatures, cycle times and the order of the drying stages as proprietary, so those are not stated here or anywhere else.")
    +steps([
      ("Collection and holding",
       "Stems are lifted by hand onto trailers at the plantation edge and arrive from many scattered plots across a collection season.",
       "A seasoned stock of pale, hard stems after roughly a year of holding.",
       "Intake is spread across a season rather than arriving in container loads, which is why availability follows the agricultural calendar."),
      ("Cutting and shaping",
       "Stems are cross-cut to the length band, bark is removed and the surface is finished.",
       "Pieces within a ±3 mm length tolerance on the stick line."),
      ("Controlled drying",
       "Shaped pieces are racked for the drying stages.",
       "Finished moisture below 14%.",
       "Most of the process rejection happens here — pieces that were going to crack crack on the rack."),
      ("Grading",
       "Pieces are sorted into diameter bands; any cracked piece is pulled.",
       "Graded stock per size, with an internally reported reject rate of roughly one piece in five overall."),
      ("Moisture check and packing",
       "A pin-type meter reading is taken and photographed for the batch, pieces are bagged with a desiccant sachet, and carton marks are checked against the packing list.",
       "A sealed carton whose marks and moisture record match the paperwork."),
    ])
    +'<div class="grid grid-3">'
    +figure(IMG+"coffee-wood-workshop-stacked-billets.jpg","Workshop interior with stacked coffee wood billets and a worker at a bench","Seasoned billets waiting to be cut. The holding period is roughly a year.")
    +figure(IMG+"coffee-wood-chew-finishing-bench.jpg","Row of workers shaping and finishing coffee wood chew sticks at benches","Shaping and surface finishing. We do not publish machine or timing detail.")
    +figure(IMG+"coffee-wood-drying-rack-rows.jpg","Rows of coffee wood sticks laid out on drying racks","Drying racks, where most rejections occur.")
    +"</div>",True),

  section("Formats built from this material",
    media(ul(["<strong>Standard chew sticks.</strong> Six graded sizes, XS to XXL, with lengths from about 10 cm to 23 cm. This is the core reference range.",
              "<strong>Wood and rope constructions.</strong> A wood block combined with cotton or hemp rope. This is a multi-component product: declare the rope material separately rather than describing the whole toy as single-ingredient.",
              "<strong>Engraved retail lines.</strong> A brand mark burned into the wood surface, approved on a sample per size.",
              "<strong>Block and chunk formats.</strong> Available on request; specification confirmed per project rather than from the stick chart."]),
          IMG+"coffee-wood-cotton-rope-tug-pair.jpg",
          "Two coffee wood blocks with knotted cotton rope ends on a light background",
          "Wood-and-rope construction. Two materials and a connection, each needing its own approval.")
    +p('The full size table — lengths, diameters, weights, reference dog weights and carton counts — sits on the <a href="/products/coffee-wood-dog-chew/">coffee wood dog chew product page</a>.')),

  section("Where coffee wood fits, and where it does not",
    fit(["Ranges that need a hard, long-lasting chew that does not soften, swell or smell as it is used.",
         "Buyers replacing rawhide who want a single-material alternative with a clean component list.",
         "Brands that want an engraved product rather than a printed sleeve that peels off during chewing.",
         "Assortments where staff can advise on size at the point of sale."],
        ["Your customers are mostly power chewers and you only plan to stock the standard stick — offer the thicker Gorilla line instead.",
         "The brief calls for an edible or digestible chew; this is a toy.",
         "You need small, frequent reorders into the EU — that is where a locally sourced wood has a genuine logistics advantage.",
         "The listing needs a certified biodegradability or dental-health claim, which no supplier in this category can currently support."])
    +p(WEAR_BEHAVIOUR)
    +p("<strong>Dental and digestibility benefits</strong> have no evidence for this material and we publish neither. What the process does control is cracking at grading and moisture at packing, and those are records we can show you.")
    +p(CAFFEINE)
    +p(SAFETY),True),

  section("Shipping this material",
    p(CARTON)+p(SEA_TRANSIT)
    +p("Wood ships with moisture risk attached, and the risk is concentrated in the container rather than in our factory. A sealed box cools overnight, water condenses on the steel and drips onto the top of the cargo. Damage on the top layer and toward the doors points to condensation in transit; bloom spread evenly through the stack points to goods packed wet. Hanging desiccant is cheap relative to a claim and is the single most useful addition for a monsoon-season sailing.")
    +p('The HS code commonly used is 4421.99 — confirm the classification with your own broker. Per-shipment documents cover Certificate of Origin, fumigation and phytosanitary certificates; these are issued against the shipment and cannot be produced afterwards. See <a href="/certifications/">testing and export documents</a>.')),
 ],
 faqs=[
  ("Is coffee wood a sustainable material?",
   "It is a by-product of replanting: growers take out the coffee trees that have stopped paying their way, and those stems — which previously went to firewood or were burned off — become our raw material. Nobody fells a tree that is still yielding cherries and no forest is cleared, so the material-reuse story is a real one and it is the one we tell. It is not the same as a certified biodegradability claim or a carbon claim, and we publish neither: the finished toy, the bag, the box and any ink would all have to be assessed together for that."),
  ("Where does the wood come from?",
   "Mature Robusta coffee stems from Vietnam's Central Highlands — principally Dak Lak, Gia Lai and Dak Nong. Stems are cut to billets of roughly 50 to 70 cm in the field, then held for about a year in ventilated shade before machining. They arrive by trailer from many scattered smallholder plots across a collection season rather than in container loads, which is why availability follows the agricultural calendar."),
  ("What moisture content is the wood at?",
   "Below 14% before packing, measured with a pin-type meter and photographed per batch, then read again before the container is sealed. Below roughly 20% is the general threshold under which common mould and decay organisms cannot establish in timber, so the packing figure carries real margin — provided the goods stay dry in transit."),
  ("Why is diameter given as a range rather than a number?",
   "Because the stem sets it. Length is cut and held to ±3 mm, but diameter follows the natural stem and is controlled by grading pieces into bands. A size L is a piece that fell into the 3.5–4.5 cm band, not a piece machined to 4 cm."),
  ("How hard is coffee wood compared with olive wood?",
   "There is no published comparison, because coffee is an agricultural crop rather than a commercial timber and has never been through standardised timber testing. Olive wood has published figures precisely because it is timber. Anyone quoting a Janka number for coffee wood is estimating, and we would rather say so than repeat it."),
  ("Can I get the wood untreated and unfinished?",
   "The standard stick is already untreated — no glue, coating, preservative or colouring. If you mean unsanded or bark-on, that is a development request rather than a stock option; send the brief and we will come back on feasibility."),
 ])

DEEP["coconut-fiber"] = dict(
 title="Coconut Fiber (Coir) Pet Toys — Material & Wholesale | VietPaw",
 h1="Coconut Fiber for Pet Toys",
 lede="Coir from the coconut husk, wound into textured balls for cats and dogs. What the material gives you, what has to be declared beyond the fiber, and how to specify a ball you can reorder.",
 image="/assets/img/coconut-fiber-ball-top-view.jpg",
 blocks=lambda: [
  section("What coconut fiber is",
    answer("Coconut fiber — coir — is the coarse fiber from the husk that surrounds a coconut. For pet toys it is cleaned, dried and wound into a dense textured ball. It is a by-product of coconut processing: the husk is waste from the food and oil trade, so the fiber is a genuine reuse stream rather than a crop grown for toys.")
    +p("The texture is what buyers are actually purchasing. Coir has a springy, fibrous surface that feels different from moulded rubber or plastic in the mouth, and it sheds short fibers as it is worked. That shedding is normal for the material and is the main thing to set expectations about on a product listing.")
    +p("What coir does <em>not</em> give you is a predictable engineering spec. There is no published density, tensile or durability standard for a wound coir ball, and winding density varies with how the ball was made. This is a material you specify by approved sample and measured dimensions, not by a number in a catalogue.")),

  section("What has to be declared beyond the fiber",
    p("A coir ball is almost never one material. Depending on the construction there may be an inner core, a binding thread, an adhesive at the start and finish of the winding, and a tag or attachment. Each of those is a separate component with its own supply chain, and each one has to be listed before you can print a composition or a plastic-free claim on the pack.")
    +spec_table(["Component","What to confirm","Why it matters"],[
      ("Coir fiber","Origin, cleaning and drying method, and any treatment applied","A treatment that has to be declared on an import entry is easier to handle before production than after"),
      ("Core","Whether there is one, and what it is made from","A ball described as all-natural fails on an undeclared synthetic core"),
      ("Binding thread","Fiber type and colour","Cotton, jute and synthetic thread are not interchangeable in a composition claim"),
      ("Adhesive","Presence, type and where it sits","Often the only non-plant component in an otherwise plant-based toy"),
      ("Tag or attachment","Material, fixing method and pull security","The most common loose-part finding on inspection"),
    ], caption="Confirm each line for your own approved sample. A photograph of a finished ball does not show the core, the adhesive or the thread.")
    +p("Keep dog and cat versions separate even where they look similar in a photo. Diameter, winding density and attachment tolerance differ, and a cat listing that reuses a dog specification is a listing you cannot defend."),True),

  section("Specifying a ball you can reorder",
    steps([
      ("Fix the diameter and the weight together",
       "Give a target diameter in centimetres and a finished weight in grams, and measure both on the sample yourself.",
       "A spec that catches a loosely wound batch, which diameter alone would not.",
       "Diameter can be held while winding density drops. Weight is the check that catches it."),
      ("Decide the species first",
       "Write a cat specification or a dog specification, not a shared one.",
       "Size, attachment and packaging warnings that match the animal your listing names."),
      ("Approve the construction, not the photo",
       "Ask for a sample cut open, or written confirmation of core, thread and adhesive.",
       "A component list you can put behind a composition claim."),
      ("Set the shedding expectation",
       "Agree what an acceptable level of loose fiber looks like on a new ball, using the retained sample as the reference.",
       "A shared standard instead of an argument on arrival."),
      ("Pack dry and say so",
       "Agree packing dryness and the storage instruction that goes on the carton.",
       "Product that arrives in the condition it left in.",
       "Coir holds moisture differently from wood; no single moisture figure transfers from the coffee wood protocol to a coir ball."),
    ])
    +media(p("A wound ball is a supervised-play toy. It is not dietary fiber, not a hairball remedy and not a chew that should be reduced and swallowed. Loose fiber and damaged pieces should be removed rather than left with the animal, and that instruction belongs on your pack rather than only in your product description.")
           +p(SAFETY),
           IMG+"coconut-fiber-ball-with-rope-toy.jpg",
           "Coconut fiber ball beside a knotted coir rope toy",
           "Fetch and carry play. Winding density and diameter are what make one ball last longer than another.")),

  section("Where coconut fiber fits, and where it does not",
    fit(["Ranges built around texture and natural material rather than bounce or durability claims.",
         "Cat assortments that need a light batting toy with a surface a paw can grip.",
         "Brands that want a plant-derived reuse story they can actually substantiate — husk is food-trade waste.",
         "Mixed natural-material boxes sold alongside loofah and rope."],
        ["Your customer expects the durability of a moulded rubber fetch toy.",
         "Shedding fiber would be a problem for the listing or the return rate.",
         "You need a published performance specification; none exists for wound coir."])
    +p('See the <a href="/collections/loofah/">loofah collection</a> for the lighter cat-play material and the <a href="/collections/hemp-fiber/">hemp collection</a> for rope constructions.'),True),
 ],
 faqs=[
  ("Is coconut fiber safe if my dog swallows some?",
   "Small amounts of shed fiber are not the same as a swallowed piece of toy, but coir is not food and is not digestible, and we make no claim that any amount is safe to ingest. Sell it as a supervised-play toy, tell customers to remove loose fiber and replace damaged balls, and do not position it as a fiber supplement or a hairball treatment."),
  ("Does the ball shed a lot?",
   "It sheds. How much depends on winding density and how hard the animal works it, and a new ball sheds more than a settled one. Agree what an acceptable level looks like on your approved sample and keep that piece — it is the only practical way to settle the question on a later delivery."),
  ("Is a coir ball biodegradable?",
   "The fiber is plant material. The finished toy may also contain a core, a binding thread, an adhesive and a tag, and the bag and box around it are separate again. We do not publish a biodegradability claim for the finished product, because that claim would need evidence for the whole assembly under stated disposal conditions."),
  ("Can I use the same ball for cats and dogs?",
   "We would not recommend listing it that way. Diameter, winding density and attachment tolerance differ between the two, and a size that is a batting toy for a cat can be a swallowing hazard for a dog, or too light to interest one. Specify each separately."),
  ("What MOQ applies?",
   "Selected standard lines start from 50 pcs per SKU. Each size and construction needs its own confirmed minimum — a mixed carton does not automatically satisfy the minimum for every SKU inside it. Private-label packaging starts at 500 pcs."),
 ])

DEEP["hemp-fiber"] = dict(
 title="Hemp Fiber Rope & Ball Pet Toys — Material & Wholesale | VietPaw",
 h1="Hemp Fiber for Rope and Ball Toys",
 lede="Wound hemp balls, knotted rope and wood-and-rope constructions. How to specify a rope toy by geometry and knot rather than by appearance, and what a fiber name does and does not tell you.",
 image=IMG+"hemp-rope-toy-assortment.jpg",
 blocks=lambda: [
  section("What hemp fiber is",
    answer("Hemp fiber is the bast fiber from the stem of the industrial hemp plant, spun into cord and then wound into balls or knotted into rope toys. It is a textile fiber, not a CBD product, not an antimicrobial treatment and not a dental product — the finished toy carries none of those properties and we do not claim them.")
    +p("The practical issue with rope toys is that the fiber name on the listing is often not the fiber in the product. Hemp, cotton, jute and coir all look similar in a photograph once they are spun and knotted, and blends are common. If your listing says hemp, the specification has to say hemp, and the sample has to be the thing you approved.")
    +p("What the fiber choice actually changes is feel and fray behaviour: hemp cord is coarser and stiffer than cotton and frays into longer strands. That is a product characteristic to describe honestly rather than a durability advantage to advertise.")),

  section("Formats and how they differ",
    spec_table(["Format","What defines it","What to specify"],[
      ("Standalone wound ball","A ball with no handle or tail","Diameter band, finished weight, winding density. Catalogue bands are S 4–5 cm, M 6–7 cm, L 8–9 cm — confirm current tolerances."),
      ("Ball with rope","A wound ball with a rope handle attached","The ball spec plus overall length, rope diameter and the attachment method. This is a different product from the standalone ball, not a variant."),
      ("Knotted rope tug","Cord knotted into a tug with no rigid component","Finished length, cord diameter, number and position of knots, handle opening size."),
      ("Wood and rope","A coffee wood block joined to rope","Every component listed separately: wood size, rope fiber and diameter, and the connection itself."),
    ], caption="A photograph shows the silhouette. These four are separate products with separate specifications, minimums and approval paths.")
    +'<div class="grid grid-3">'
    +figure(IMG+"hemp-rope-balls-three-sizes.jpg","Three knotted hemp rope balls in small, medium and large","Standalone wound balls: diameter band, finished weight and winding density.")
    +figure(IMG+"hemp-rope-loop-ball-toy.jpg","Hemp rope toy with a loop handle and a knotted ball end","Ball with rope: the join between loop and ball is its own inspection point.")
    +figure(IMG+"hemp-ball-and-loop-toy-set.jpg","Hemp rope balls with a double-ended loop toy","A loop tug and two balls — three separate SKUs with separate specifications.")
    +"</div>",True),

  section("Specifying a rope toy",
    p("Rope toys fail at the join, not in the middle of the cord. Appearance tells you nothing about how much force it takes to pull a knot through or separate a ball from its handle, and no supplier in this category publishes a tensile rating for these constructions. Specify the check rather than assuming the rating.")
    +steps([
      ("Name the fiber, in writing",
       "State hemp, cotton, jute or a named blend in the specification, and confirm it against the sample.",
       "A composition line you can defend on a listing.",
       "This is the single most common gap between a rope toy listing and the product in the box."),
      ("Give the geometry in numbers",
       "Finished length, cord diameter, knot count and position, and the handle opening size.",
       "A drawing a second factory could quote against, not a description of a photo."),
      ("Agree an attachment check",
       "Define a pull or attachment check appropriate to the construction and the acceptance criterion.",
       "A pass/fail standard on the order instead of a judgement call at inspection.",
       "Ask for results if any numerical strength figure appears anywhere in your marketing."),
      ("Set the fray standard",
       "Use the retained sample to define acceptable loose strands on a new toy.",
       "A shared reference for the next delivery."),
      ("Match the warning to the construction",
       "Write supervision and replacement wording that names the actual failure modes: long loose strands, loops, and separated components.",
       "Pack copy that matches the product rather than generic boilerplate."),
    ])
    +p(SAFETY)),

  section("Where hemp fits, and where it does not",
    fit(["Tug and interactive play where the customer expects a fibrous, fraying toy and is told so.",
         "Ranges that want a plant-fiber alternative to nylon webbing.",
         "Mixed constructions with coffee wood, where the rope is the soft component.",
         "Brands that will print an honest supervision instruction rather than a durability claim."],
        ["The customer expects a rope that does not fray — no natural cord meets that.",
         "The dog swallows strands; long fibers are a genuine risk and this is the wrong category for that animal.",
         "You need a published tensile rating to support a marketing claim.",
         "The brief is a CBD, antimicrobial or breath-freshening product; hemp fiber is none of those."])
    +p('Rope pairs naturally with the wood range. See the <a href="/collections/coffee-wood/">coffee wood collection</a> for the rigid component and the <a href="/products/hemp-rope-dog-toy/">hemp rope dog toy</a> for the current rope formats.'),True),
 ],
 faqs=[
  ("Is hemp rope stronger than cotton rope?",
   "Hemp cord is generally coarser and stiffer, and it frays into longer strands. Whether the finished toy is stronger depends on cord diameter, knot construction and how components are joined — not on the fiber name. Neither we nor anyone else in this category publishes a tensile rating for these toys, so we specify an attachment check instead of quoting a number."),
  ("Does hemp contain CBD or THC?",
   "No. This is industrial hemp bast fiber used as a textile, in the same way linen is made from flax. It carries no cannabinoid content into the product and must not be marketed as though it did."),
  ("Is hemp naturally antibacterial or good for teeth?",
   "There is no product-specific evidence for either claim, so we do not make them and we would advise against printing them. A fiber toy is a play item; breath, plaque and dental health claims need clinical evidence tied to the specific product."),
  ("How do I know the rope is actually hemp?",
   "Put the fiber in the written specification, approve a physical sample, and keep a retained piece. Hemp, cotton, jute and blends are hard to tell apart in a photograph once spun and knotted, which is why the specification rather than the image has to carry it."),
  ("What sizes do the balls come in?",
   "The catalogue reference bands are S 4–5 cm, M 6–7 cm and L 8–9 cm in diameter. Confirm current dimensions and tolerances against a sample, and remember that a ball with a rope handle is a separate product from the standalone ball of the same diameter."),
  ("Can you combine rope with coffee wood?",
   "Yes, and it is one of the more popular constructions. Treat it as a multi-component product: the wood size, the cord fiber and diameter, and the connection each need their own approval. Do not describe the assembled toy as single-ingredient."),
 ])

GALLERY = {
 "coffee-wood": [("coffee-wood-chews-group-white-background.jpg","Several coffee wood chews of different sizes on a white background","Finished chews: grain, outline and shade vary piece to piece."),
                 ("coffee-wood-chews-mixed-sizes.jpg","Coffee wood chews in mixed sizes lying together","Mixed sizes from one grading run."),
                 ("coffee-wood-chews-packing-by-hand.jpg","Hands packing coffee wood chews into bags","Packing by hand at our warehouse.")],
 "coconut-fiber": [("coconut-fiber-ball-top-view.jpg","Wound coconut fiber ball seen from above","A wound coir ball."),
                   ("coconut-fiber-rope-toy-flat-lay.jpg","Knotted coconut fiber rope toy on a marble surface","Coir rope with knotted ends."),
                   ("coconut-fiber-ball-with-rope-toy.jpg","Coconut fiber ball beside a knotted coir rope toy","Ball and rope from the same coir line.")],
 "hemp-fiber": [("hemp-rope-ball-large.jpg","Large knotted hemp rope ball close up","Large hemp ball: check knot tightness."),
                ("hemp-rope-ball-vacuum-packed-size-l.jpg","Hemp rope ball vacuum-packed with a size L label","Packed with its size label."),
                ("hemp-rope-toy-assortment.jpg","Assortment of hemp rope balls and loop toys","Balls and loop toys, quoted as separate SKUs.")],
 "loofah": [("loofah-fish-cat-toy.jpg","Fish-shaped loofah cat toy with a small loop","Fish shape with a hanging loop."),
            ("loofah-mouse-cat-wand-toys.jpg","Two loofah mouse toys on wooden cat wands","Loofah mice on wands — each component specified separately."),
            ("loofah-rabbit-shape-cat-toy.jpg","Rabbit-shaped loofah cat toy","Rabbit shape cut from dried loofah fibre."),
            ("loofah-duck-cat-toy.jpg","Duck-shaped loofah cat toy","Duck shape."),
            ("loofah-bone-shape-pet-toy.jpg","Bone-shaped loofah pet toy","Bone shape."),
            ("loofah-mouse-toys-vacuum-pack.jpg","Loofah mouse toys vacuum-packed in a clear bag","Mouse toys packed for export.")],
}

def gallery_section(slug):
    items = GALLERY.get(slug)
    if not items:
        return []
    return [section("Product photos", '<div class="grid grid-3">'+"".join(figure(IMG+f,a,c) for f,a,c in items)+"</div>")]

def build(root):
    for slug,d in MATERIALS.items():
        deep = DEEP.get(slug)
        if deep:
            blocks = deep["blocks"]()
            sections = blocks[:1] + gallery_section(slug) + blocks[1:] + [
                section("Products in this collection", product_cards(d["products"])),
                section("MOQ, samples, packaging and lead time", terms(d["moq"])+trust_links(),True),
            ]
            publish(root,"/collections/"+slug+"/",deep["title"],deep["lede"],deep["h1"],deep["lede"],
                sections,active="Materials",image=deep["image"],
                trail=[("Home","/"),("Materials","/materials/"),(deep["h1"],None)],
                faqs=deep["faqs"])
            continue
        sections=[
            section("What this material is",p(d["what"])),
            *gallery_section(slug),
            section("Products and wholesale applications",product_cards(d["products"])+table(["Format","Buyer decision"],d["applications"]),True),
            section("From material sample to approved order",ul(d["approval"],True)+trust_links()),
            section("OEM, private label and range planning",p("Start with the sales channel, target pet, intended use and pack format. A standard product with your label follows a different approval path from a new shape or mixed-material construction.")+
                p('<a href="/services/private-label-pet-toys/">Private label</a> covers branding and packaging on approved designs. <a href="/services/oem-odm-pet-toy-manufacturing/">OEM/ODM</a> covers specification-led development. For a multi-material range, review <a href="/services/wholesale-pet-products/">wholesale ordering</a>.'),True),
            section("MOQ, samples, packaging and lead time",terms(d["moq"])),
            section("Claims, quality and safe-use boundaries",p(d["caution"])+p(SAFETY)+p('Review <a href="/sustainability/">material and packaging claim boundaries</a> before printing environmental language. Inspection records and third-party reports have different scopes.'),True)]
        publish(root,"/collections/"+slug+"/",d["title"],
            d["lede"],d["h1"],d["lede"],sections,active="Materials",image="/assets/img/"+d["image"],
            trail=[("Home","/"),("Materials","/materials/"),(d["h1"],None)],
            faqs=[("Can I order a mixed-material collection?", "Yes, discuss an assortment. Each SKU, size and packaging format needs a confirmed minimum, price and specification."),
                  ("Does natural material mean a certified finished product?", "No. Confirm every component and review the scope of any inspection or test report for the selected product."),
                  ("What should I send for a quote?", "Send product references, sizes, quantity per SKU, destination country and branding needs. Include your packaging and test requirements if known.")])
