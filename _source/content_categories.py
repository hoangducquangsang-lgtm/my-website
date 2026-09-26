# -*- coding: utf-8 -*-
from content_helpers import (publish, section, p, ul, cards, table, terms, trust_links, SAFETY,
                             answer, fit, steps, spec_table, figure, media)
from content_products import product_cards

CATEGORIES = [
("/dog-toys/","Wholesale Natural Dog Toys from Vietnam","Dog Toys","golden-retriever-gnawing-coffee-wood.jpg",
 "Build a wholesale dog-toy assortment around coffee wood, coconut fiber and hemp. Compare play types, sample-approved sizes and private-label packaging with a Vietnam manufacturer.",
 ["coffee-wood-dog-chew","coconut-fiber-dog-ball","hemp-rope-dog-toy"],
 [("Chew toys","Wood stick specifications and responsible chew-range planning.","/dog-toys/chew-toys/"),
 ("Rope & tug toys","Define length, knots and attachment checks.","/dog-toys/rope-toys/"),
 ("Fetch & balls","Compare diameter, construction and pack format.","/dog-toys/fetch-toys/"),
 ("Enrichment","Texture-led formats and development briefs.","/dog-toys/puzzle-toys/")],
 [("Coffee wood","Hard chew format","Size, surface, cracks and a conservative use label"),
 ("Coconut fiber","Supervised fetch and carry","Diameter, winding, loose fiber and internal components"),
 ("Hemp fiber","Supervised interactive play","Knot security, fraying and any rope connections")],
 "Start with a narrow assortment that has a clear role at shelf: a wood chew, a fetch ball and an interactive rope. For each, specify the intended dog size and play context. Add more designs after sample evaluation and actual sell-through data."),
("/dog-toys/chew-toys/","Natural Dog Chews Wholesale","Dog Toys","vietpaw-coffee-wood-sizes.png",
 "Source non-edible natural dog chew toys led by coffee wood sticks. Compare reference sizes, review use limitations and approve the product specification before placing a wholesale order.",
 ["coffee-wood-dog-chew","gorilla-coffee-wood-dog-chew"],[],
 [("Standard stick","Single wood component","Confirm size and composition"),
 ("Wood with rope","Multi-component toy","Confirm both materials and connection security"),
 ("Private-label pack","Brand-specific presentation","Size guide, warnings and pack protection")],
 "This category covers chew toys, not edible treats. Harder does not automatically mean safer or better for strong chewers. Select a range only after reviewing sample construction and clear supervised-use instructions. Coffee wood collection information supports supplier selection; the product page carries the detailed size table."),
("/dog-toys/rope-toys/","Rope & Tug Dog Toys Wholesale","Dog Toys","hemp-rope-loop-ball-toy.jpg",
 "Discuss natural-fiber rope, knotted and ball-with-rope designs for supervised tug play. Specify fiber identity, rope geometry and packaging for wholesale or private-label orders.",
 ["hemp-rope-dog-toy","hemp-fiber-ball"],[],
 [("Knotted rope","Length, diameter, knots","Inspect knot security and fraying"),
 ("Ball with rope","Ball and handle geometry","Assess the connection as a separate part"),
 ("Wood with rope","Wood and rope specification","Agree component and attachment checks")],
 "Hemp, cotton and coconut fiber are different materials; confirm the exact fiber or blend in the selected design. A catalogue photo is not proof of reinforcement or measured pull strength. Define any test method and acceptance criteria before using a strength claim on packaging."),
("/dog-toys/fetch-toys/","Natural Fetch & Ball Dog Toys Wholesale","Dog Toys","coconut-fiber-ball-sizes-with-rope-toy.jpg",
 "Compare coconut-fiber and hemp balls for a supervised fetch-and-carry assortment. Approve diameter, weight, surface and packing before committing to volume.",
 ["coconut-fiber-dog-ball","hemp-fiber-ball"],[],
 [("Coir ball","Texture and winding","Confirm diameter and any core"),
 ("Hemp ball","Wound-fiber construction","Confirm the three catalogue size references"),
 ("Multi-pack","Assortment and carton","Check every component and sold-as-set label")],
 "A natural-fiber ball is not a rubber ball with a different appearance. Do not assume bounce, flotation, weather resistance or a fixed lifespan. The ball must be too large to swallow whole, and the chosen sample should be assessed for the intended style of supervised play."),
("/dog-toys/puzzle-toys/","Natural Enrichment Dog Toys Wholesale","Dog Toys","vietpaw-hemp-wood-assortment.jpg",
 "Explore texture-led natural toys and discuss enrichment designs for your range. Current products emphasize material and shape; treat new treat-dispensing mechanisms as custom development.",
 ["hemp-rope-dog-toy","hemp-fiber-ball"],[],
 [("Knotted forms","Handling and supervised interaction","Define geometry and intended use"),
 ("Mixed textures","Range variety","Declare every component"),
 ("New mechanisms","OEM/ODM feasibility","Prototype, test and approve before claiming availability")],
 "This is an enrichment sourcing category, not a claim that the displayed products are tested food puzzles. If you need a treat dispenser or measured difficulty levels, submit a specific brief. Agree cleaning, moving-part and food-contact requirements with the appropriate specialists for that construction."),
("/cat-toys/","Wholesale Natural Cat Toys","Cat Toys","cat-hugging-loofah-toy.jpg",
 "Build a cat-toy range from coconut-fiber balls and loofah shapes. Compare construction, shape-specific dimensions and private-label packaging for international retail.",
 ["coconut-fiber-cat-ball","loofah-cat-toy"],
 [("Balls & chasers","Choose a cat-specific size and construction.","/cat-toys/balls/"),
 ("Catnip & play shapes","Optional filling and attachment requirements.","/cat-toys/catnip-toys/")],
 [("Coconut-fiber balls","Batting and chasing","Check size and loose fiber"),
 ("Loofah shapes","Lightweight play","Check stitching and detachable parts"),
 ("Optional catnip","Development request","Confirm inclusion, source and labeling")],
 "A cat assortment needs its own specifications rather than scaled-down dog-toy descriptions. Ask for each shape's measurements and every internal or attached component. Plan pack information around supervised play, inspection and replacement, without promising dental or therapeutic benefits."),
("/cat-toys/balls/","Natural Cat Balls & Chasers Wholesale","Cat Toys","coconut-fiber-ball-top-view.jpg",
 "Request coconut-fiber cat-ball samples and build a measured, consistent batting-and-chasing range with your own tags or packaging.",
 ["coconut-fiber-cat-ball"],[],
 [("Single ball","Diameter and mass","Approve a cat-specific sample"),
 ("Ball set","Quantity and size mix","Check individual and outer labeling"),
 ("Retail carton","Units and dimensions","Confirm master-carton packing")],
 "Specify the diameter, mass and finished texture rather than selecting from S/M/L alone. Check winding and any core or binding thread. A mixed-size photo is a range reference, not evidence that all sizes suit cats."),
("/cat-toys/catnip-toys/","Loofah Shapes & Catnip Options Wholesale","Cat Toys","vietpaw-loofah-play-shapes.png",
 "Source loofah play shapes and discuss optional catnip-filled designs. Confirm filling, seams and labeling for each selected SKU.",
 ["loofah-cat-toy"],[],
 [("Unfilled shape","Loofah and attachments","Confirm dimensions and seams"),
 ("Catnip option","Optional inclusion","Approve filling specification and source"),
 ("Custom silhouette","OEM/ODM development","Review detachable parts and feasibility")],
 "Catnip is not included in every toy. State clearly whether a quoted SKU is unfilled or contains catnip, and confirm the amount and source when relevant. A custom shape requires its own sample and component list."),
("/collections/aggressive-chewers/","Sourcing Toys for Strong Chewers: Limits & Options","Materials","golden-retriever-gnawing-coffee-wood.jpg",
 "For strong chewers, choose the Gorilla line: thick-cut coffee wood chews in four sizes. No chew is indestructible, so supervise and replace when worn.",
 ["gorilla-coffee-wood-dog-chew","coffee-wood-dog-chew","hemp-rope-dog-toy"],[],
 [("Gorilla coffee wood chew","GRLS–GRLXL, 155–900 g","Choose the size against the dog; supervise and replace when worn"),
 ("Rope play","Fraying and ingestion risks","Use only for supervised interaction"),
 ("Claims","No indestructible promise","Describe tested construction, not guaranteed outcomes")],
 "For a strong chewer, the Gorilla line is the better answer than stretching the standard CC01 stick to XL or XXL: it is cut much thicker, so there is more wood per piece. Size it against the dog’s mouth, supervise, and replace it when it cracks or wears small. Retail copy should not promise an indestructible chew or swallowable fibers."),
("/collections/teething-puppies/","Puppy Toy Sourcing: Size & Material Considerations","Materials","dog-lifestyle-chew-1.jpg",
 "Plan puppy-focused ranges with particular care around developing teeth, detachable parts and size. Small dimensions alone do not make a hard chew puppy-safe.",
 [],[],
 [("Age and dental stage","Individual suitability","Obtain veterinary advice"),
 ("Toy construction","Attachments and loose fibers","Approve a species-appropriate design"),
 ("Labeling","Supervision and replacement","Avoid universal puppy-safe claims")],
 "Do not automatically recommend coffee wood XS/S for teething puppies. Discuss a puppy-specific design, intended age range and professional suitability assessment. A loofah material reference can inform development, but an existing cat SKU is not a validated puppy product."),
("/collections/plastic-free/","Pet Toys for a Plastic-Free Sourcing Brief","Materials","vietpaw-natural-toy-assortment.png",
 "Explore coffee wood, coconut fiber, hemp and loofah options, then verify the complete product and packaging composition before using a plastic-free claim.",
 ["coffee-wood-dog-chew","coconut-fiber-dog-ball","hemp-fiber-ball","loofah-cat-toy"],[],
 [("Product body","Headline natural material","Check cores, thread, glue and coatings"),
 ("Retail packaging","Paper or kraft options","Check laminates, inks and windows"),
 ("Shipping protection","Bags and desiccants","Do not describe vacuum film as plastic-free")],
 "Natural, renewable, upcycled and biodegradable describe different properties. Coffee wood and coconut husks can support specific reuse stories; hemp and loofah should not automatically be called waste-derived. Whole-product disposal claims need evidence for the selected construction and conditions."),
]


IMG = "/assets/img/"

DOG_TOYS_LEDE = ("Coffee wood chews, coconut fiber balls and hemp rope toys, made in Vietnam. Compare the "
                 "materials by chewing style, size the range to the dogs your customers own, and take the "
                 "specification rather than the photograph.")

def dog_toys_sections():
    return [
    section("What VietPaw makes for dogs",
      answer("Three materials cover the dog range: coffee wood for hard chewing, coconut fiber for fetch and "
             "carry, and hemp or cotton rope for tug and interactive play. Wood and rope are also combined into "
             "multi-component toys. Everything is supervised-play product \u2014 none of it is edible, and none of it "
             "is sold with a dental or digestibility claim.")
      + p("The useful question for a buyer is not which material is best, but which chewing style each one "
          "actually serves. A range that puts a hard wood chew in front of a power chewer and a fraying rope in "
          "front of a strand-swallower will generate returns whatever the material story says.")
      + spec_table(["Material", "Chewing style it suits", "How lifespan behaves", "Main thing to check"], [
          ("Coffee wood", "Persistent gnawing and shredding", "Long \u2014 weeks to months for a moderate chewer; days for a determined one", "Size against the dog; strong chewers go to the thicker Gorilla line"),
          ("Coconut fiber (coir)", "Fetch, carry and light mouthing", "Moderate; set by winding density more than diameter", "Shedding fiber, and what sits under the winding \u2014 core, thread, adhesive"),
          ("Hemp / cotton rope", "Tug and interactive play with a person", "Short to moderate; frays by design", "The join, not the cord \u2014 rope toys fail where components meet"),
          ("Wood and rope combined", "Mixed chew and tug", "Set by whichever component goes first", "Three approvals: the wood, the cord and the connection"),
        ], caption="Lifespan is genuinely dog-dependent and no supplier in this category publishes a figure. "
                   "These are relative descriptions for planning an assortment, not a durability claim.")),

    section("Browse by play type", cards([
        ("Chew toys", "Coffee wood stick specifications and honest chew-range planning.", "/dog-toys/chew-toys/", IMG+"vietpaw-coffee-wood-sizes.png"),
        ("Rope & tug toys", "Cord geometry, knot construction and attachment checks.", "/dog-toys/rope-toys/", IMG+"hemp-rope-loop-ball-toy.jpg"),
        ("Fetch & balls", "Diameter, winding density, pack format.", "/dog-toys/fetch-toys/", IMG+"coconut-fiber-ball-with-rope-toy.jpg"),
        ("Enrichment", "Texture-led formats and development briefs.", "/dog-toys/puzzle-toys/", IMG+"hemp-rope-loop-coffee-wood-toy.jpg")], 4), True),

    section("Sizing the range to real dogs",
      media(p("Most first orders in this category buy too many sizes. Six coffee wood sizes look thorough on a "
              "spreadsheet, but two of them usually carry the sell-through while the rest tie up stock. Start "
              "with the dogs your customers actually own \u2014 for most European and North American pet retail that "
              "is the 5\u201320 kg band, which is sizes M, L and XL \u2014 then add the extremes once you have sell-through "
              "data rather than before.")
            + p("The reference dog weights below are a starting point for picking a size, not a veterinary "
                "suitability assessment. A 25 kg dog that chews gently and a 25 kg dog that cracks things need "
                "different products, and no weight chart captures that.")
            + p('Full lengths, diameters, weights and carton counts are on the '
                '<a href="/products/coffee-wood-dog-chew/">coffee wood product page</a>; sizing by behaviour is '
                'covered in the <a href="/guides/coffee-wood-chew-size-guide/">chew size guide</a>.'),
            IMG+"coffee-wood-chew-size-row.jpg",
            "Hand holding four coffee wood chew sticks of increasing size for scale comparison",
            "Four sizes in one hand. Scale is easier to judge on a sample than on a size chart.")),

    section("Where each material stops being the right answer",
      fit(["A range that needs a long-lasting hard chew and can carry a supervision instruction \u2014 coffee wood.",
           "Fetch and carry play where texture matters more than bounce \u2014 coconut fiber.",
           "Interactive tug that a person takes part in \u2014 hemp or cotton rope.",
           "A natural-material story you can substantiate: coffee stem and coconut husk are by-products of existing agriculture."],
          ["The dog is a determined power chewer \u2014 choose the thicker Gorilla line rather than a standard stick.",
           "The dog swallows strands \u2014 rope is the wrong category for that animal, whatever the fiber.",
           "The customer wants an edible or digestible chew \u2014 none of this is food.",
           "The listing needs certified biodegradability, dental benefit or \u201csplinter-free\u201d \u2014 none of those can be supported here."])
      + p(SAFETY), True),

    section("Product references for your brief", product_cards(["coffee-wood-dog-chew","coconut-fiber-dog-ball","hemp-rope-dog-toy"])
      + p('Planning a young-dog range? Review <a href="/collections/teething-puppies/">puppy-toy sourcing and '
          'suitability considerations</a> \u2014 a hard wood stick is not a teething product.')),

    section("Building the first order",
      steps([
        ("Pick three products, not thirty",
         "One hard chew, one fetch item, one interactive rope, each in the one or two sizes that match your customer base.",
         "An assortment with a clear role per SKU at shelf, and a manageable first order.",
         "Breadth is easy to add after sell-through data. It is expensive to add before."),
        ("Approve a sample of each and keep one",
         "Measure it, check the components a photo does not show, and retain a piece as your reference.",
         "A physical standard to check the next delivery against."),
        ("Write the warnings to match the construction",
         "Name the actual failure modes: hard-chew tooth risk for wood, loose fiber for coir, long strands and loops for rope.",
         "Pack copy that holds up, instead of generic boilerplate."),
        ("Settle pack format before artwork",
         "Bulk, single bag, vacuum pack or retail box \u2014 and singles or sets.",
         "A carton count and pack weight you can use for freight and listings.",
         "Pack format changes pieces per carton, so artwork sized before this usually has to be redone."),
      ])),

    section("Wholesale terms: MOQ, samples and lead time", terms() + trust_links(), True),

    section("Private label and development",
      p("Laser engraving on suitable coffee wood surfaces starts at 50 pcs and is separate from the 500 pcs per "
        "SKU minimum for printed tags, labels and boxes. That gap is useful: it lets you run a small engraved "
        "trial before committing to printed packaging.")
      + p('Explore <a href="/services/private-label-pet-toys/">private-label options</a> for branding an approved '
          'design, or <a href="/services/oem-odm-pet-toy-manufacturing/">OEM/ODM development</a> when the '
          'construction itself changes. For recurring assortments, see '
          '<a href="/services/wholesale-pet-products/">wholesale ordering</a>.')
      + p('Review <a href="/guides/pet-toy-safety-testing-requirements/">how to scope product testing</a> and '
          '<a href="/sustainability/">how material claims are qualified</a> before printing anything.')),
    ]

DOG_TOYS_FAQ = [
  ("Which natural dog toy lasts longest?",
   "Coffee wood, for most dogs \u2014 but lifespan is set by the dog rather than the material. A moderate gnawer may "
   "keep a size M stick for months while a determined chewer reduces the same piece in days. We do not publish a "
   "figure in days or weeks, because any number we gave you would be wrong for half your customers."),
  ("Are natural dog toys safe for aggressive chewers?",
   "Yes, with the right product. For strong chewers we make the Gorilla line \u2014 thick-cut coffee wood chews "
   "from GRLS (155\u2013230 g) to GRLXL (550\u2013900 g). No chew is indestructible, so size it to the dog, supervise "
   "and replace it when it cracks or wears small."),
  ("Can dogs swallow pieces of these toys?",
   "Pieces can break off any chew, and rope frays into strands. None of these materials is digestible. Every pack "
   "should carry a supervised-use instruction and a replace-when-damaged instruction, and customers should be told to "
   "remove loose fiber and strands rather than leave them with the animal."),
  ("How many sizes should I stock?",
   "Two or three. Six coffee wood sizes look comprehensive and usually tie up stock \u2014 the 5\u201320 kg band, sizes S and "
   "M, carries most of the sell-through in general pet retail. Add the extremes once your own data supports it."),
  ("Can I mix materials in one order?",
   "Yes, and it is a sensible way to build a first assortment. Each SKU, size and packaging format still needs its own "
   "confirmed minimum and price \u2014 a mixed carton does not automatically satisfy the minimum for every line inside it."),
  ("Do these toys carry a safety certification?",
   "There is no universal pet-toy safety certification to carry. Test reports have a defined scope covering specific "
   "substances or methods for a specific product, so ask for the report that matches your SKU and your destination "
   "market rather than a general reassurance."),
  ("What is the difference between wholesale, private label and OEM?",
   "Wholesale is an approved standard specification shipped as-is. Private label is that same approved design with your "
   "engraving, tags or printed box. OEM/ODM is a new construction built from your drawing or brief, through feasibility "
   "and prototype. They have different minimums, lead times and approval paths."),
]

def build(root):
    for path,h1,active,img,lede,products,subcategories,comparison,notes in CATEGORIES:
        if path=="/dog-toys/":
            publish(root,path,"Wholesale Natural Dog Toys from Vietnam | Coffee Wood, Coir & Rope | VietPaw",
                "Coffee wood chews, coconut fiber balls and hemp rope dog toys from Vietnam. Compare materials by "
                "chewing style, see sizes and carton data, and order wholesale or private label from 50 pcs.",
                "Natural Dog Toys, Wholesale from Vietnam", DOG_TOYS_LEDE, dog_toys_sections(),
                active=active, image=IMG+"french-bulldog-chewing-coffee-wood.jpg", faqs=DOG_TOYS_FAQ)
            continue
        puppy_link=p('Planning a young-dog range? Review <a href="/collections/teething-puppies/">puppy-toy sourcing and suitability considerations</a>.') if path=="/dog-toys/" else ""
        references=product_cards(products) if products else p('No puppy-specific SKU has been confirmed in the supplied specification. Use the <a href="/materials/">material overview</a> to discuss a dedicated design; do not relabel a cat toy or hard wood stick as puppy-safe.')
        parts=[section("Plan the assortment",p(notes)+(cards(subcategories,2) if subcategories else "")+puppy_link),
               section("Product references for your brief",references,True),
               section("Materials, formats and buying checks",table(["Option","What to specify","What to check"],comparison)),
               section("Wholesale terms: MOQ, samples and lead time",terms(),True),
               section("Private label, quality and export preparation",
                 p("Send quantities per SKU, destination country, intended sales channel and required launch date. Standard designs with your branding are quoted differently from new constructions. Separate product quantity from the minimum for printed boxes.")+
                 p('Explore <a href="/services/private-label-pet-toys/">private-label options</a> or <a href="/services/oem-odm-pet-toy-manufacturing/">OEM/ODM development</a>. For recurring assortments, use our <a href="/services/wholesale-pet-products/">wholesale service</a>.')+trust_links()),
               section("Clear use instructions belong on every pack",p(SAFETY)+p('Review <a href="/guides/pet-toy-safety-testing-requirements/">how to scope product testing</a> and <a href="/sustainability/">how material claims are qualified</a>.'),True)]
        publish(root,path,h1+" | VietPaw",lede,h1,lede,parts,active=active,image="/assets/img/"+img,
            faqs=[("Can I start with a small mixed order?", "Ask for a line-by-line quote. A minimum starting from 50 pcs applies only to selected standard products, not automatically to the whole assortment or every custom design."),
                  ("Can the products carry my brand?", "Yes, discuss labels, tags, packaging and wood engraving where suitable. Approve artwork and the physical sample before production."),
                  ("What does the quotation need to include?", "Product references, dimensions, quantities per SKU, branding, packaging, destination, timing and any buyer testing or document requirements.")])
