# -*- coding: utf-8 -*-
"""VietPaw editorial guides. Author attribution supplied by the website owner."""
import re
from common import BASE_URL, BRAND, page, write_page, breadcrumb_html
from guide_dates import GUIDE_UPDATED_DATES, updated_time
from content_helpers import (section, p, ul, table, cards, rfq_bar, FTC, CPSC, ECHA, AAHA,
                             answer, fit, steps, spec_table, figure, SAFETY)
from content_products import coffee_size_table
from content_helpers import GORILLA, gorilla_table

ARTICLES=[]
def add(slug,cluster,title,description,intro,sections,commercial,related=(),sources=(),
        image="vietpaw-natural-toy-assortment.png",faqs=(),h1=None,figures=()):
    ARTICLES.append(dict(slug=slug,cluster=cluster,title=title,description=description,intro=intro,
        sections=sections,commercial=commercial,related=related,sources=sources,image=image,
        faqs=faqs,h1=h1 or title,figures=figures))

add("natural-dog-chew-toys-guide","Natural chew toys",
    "Natural Dog Chew Toys: Building a Range That Makes Sense",
    "How to choose natural dog toys for a wholesale range, from chewing behavior and material construction to sample approval and retail packaging.",
    answer("<strong>Short answer:</strong> build a natural dog toy range from a few products that each do one job — a thick-cut Gorilla "
           "coffee wood chew for strong chewers, a standard coffee wood stick for moderate gnawers, a coconut fiber ball for fetch and carry, "
           "and a hemp rope for owner-led tug. Choose two or three sizes of each, approve a physical sample per SKU, and put the use and "
           "replacement instructions on every pack."),
    [
    ("What a natural dog chew toy is",
      p("A <dfn>natural dog chew toy</dfn> is a non-edible toy made mainly from plant material — wood, coir, hemp or loofah — rather than "
        "rubber, nylon or plastic. It is different from an <em>edible chew</em> such as a treat or rawhide: a wooden stick is a non-food "
        "product, even when it sits beside treats on a retail shelf.")
      + p("A dog that carries a toy around the house and a dog that tries to pull it apart are asking very different things of the same product. "
          "That distinction belongs at the beginning of a buying brief. A range built around the word “natural”, without a clear use for each "
          "item, leaves store staff and customers to work out the important details themselves.")),

    ("Give each product a job",
      spec_table(["Product","Job in the range","Best for","Key specification"],[
        ("Gorilla coffee wood chew","Long, hard chewing","Strong chewers","Thick-cut; GRLS–GRLXL, 155–900 g"),
        ("Standard coffee wood stick (CC01)","Gnawing","Moderate chewers","XS–XXL by length, diameter and weight"),
        ("Coconut fiber ball","Fetch and carry","Dogs that carry and mouth","Diameter, finished weight, winding, any core"),
        ("Hemp rope toy","Owner-led tug","Interactive play with a person","Length, rope diameter, knots and joins"),
        ("Wood-and-rope combination","Tug plus chew","Dogs that like both","The join between wood and rope"),
      ], caption="One job per product keeps sizing, packaging and instructions simple.")
      + p("For a first order, a small number of clearly differentiated products is easier to support than several similar-looking designs. "
          "Decide who each item is for, what the owner does during play and when it should be removed.")),

    ("Building the range, step by step",
      steps([
        ("Map your customers’ dogs","List the sizes and chewing styles you actually sell to — gnawers, strong chewers, fetchers, tuggers.","A short list of jobs the range must cover."),
        ("Pick one product per job","Use the table above; add strong chewers to the Gorilla line rather than stretching the standard stick.","No overlap between SKUs."),
        ("Limit the sizes","Two or three sizes per product at launch.","Less stock tied up; clearer shelf advice."),
        ("Approve samples","Up to 3 free samples; you cover the courier. Measure and keep one reference per SKU.","A physical standard for every repeat order."),
        ("Agree pack and instructions","Pack count, barcode, supervision and replacement advice on every unit.","Staff and customers get the same message."),
        ("Review after one season","Sales, questions and returns by SKU and size.","A second order based on data, not on a toughness ranking."),
      ])),

    ("VietPaw chew and toy references",
      spec_table(["Line","Sizes","Minimum","Lead time"],[
        ("Coffee wood CC01","XS, S, M, L, XL, XXL","50 pcs per size; Trial Box 100 / Starting Box 500","5–7 days stock"),
        ("Coffee wood Gorilla","GRLS, GRLM, GRLL, GRLXL","Confirmed in the quote","Confirmed in the quote"),
        ("Coconut fiber dog ball","S / M / L references","Selected lines from 50 pcs","Confirmed in the quote"),
        ("Hemp rope dog toy","Quoted by design","Project-specific","Confirmed in the quote"),
        ("Private label (any line)","—","500 pcs per SKU","60–80 days"),
      ], caption="Planning figures; your quotation governs.")),

    ("The sample needs to answer more than one question",
      p("Handle the product before judging the photograph. With wood, compare the narrowest and widest points, surface finish and any crack — "
        "any cracked piece should have been removed at grading. With rope or wound fibre, look at knot placement, loose ends and how "
        "components are joined. Request the complete material list; a natural outer layer does not identify a hidden core or binding thread.")
      + p("Keep an approved sample, and put its important features into writing as well. A photograph cannot settle a later disagreement about "
          "diameter or weight. Natural grain and shade can vary; an unapproved change in construction is a different matter.")),

    ("Make the first order teach you something",
      p("Record quantities by SKU and size, not only the total number of toys. Agree the pack count, barcode placement and carton marks before "
        "production. At receiving, separate manufacturing defects from transit damage and keep the batch reference with each issue.")
      + p("After launch, review which sizes sell, which questions customers ask and why products are returned. That gives the second order a "
          "sounder basis than a broad promise such as “suitable for all dogs”.")),
    ],
    ("Explore VietPaw's natural dog toy range","/dog-toys/"),
    related=[("Coffee wood sizing","/guides/coffee-wood-chew-size-guide/"),("Toys for strong chewers","/guides/best-natural-chews-for-aggressive-chewers/"),
             ("Coconut fiber explained","/guides/what-is-coconut-fiber-pet-toys/"),("Wholesale ordering","/services/wholesale-pet-products/")],
    image="vietpaw-coffee-wood-sizes.png",
    faqs=[
      ("What are natural dog chew toys made of?",
       "Plant materials such as coffee wood, coconut fiber (coir), hemp and loofah, rather than rubber, nylon or plastic."),
      ("Are natural chew toys edible?",
       "No. A coffee wood stick or a coir ball is a toy, not food. Pieces and loose fibres should not be swallowed."),
      ("Which natural chew is best for a strong chewer?",
       "A thick-cut coffee wood chew from the Gorilla line, in four sizes from GRLS (155–230 g) to GRLXL (550–900 g)."),
      ("How many products should a first range have?",
       "Usually three to five, each with a distinct job, in two or three sizes each. It is easier to explain and to reorder than a long list."),
      ("How do I choose sizes for the range?",
       "Start from the dogs your customers own. For coffee wood, the CC01 table links each size to a reference dog weight; go up one size for "
       "keen chewers and use Gorilla for strong chewers."),
      ("Can I mix materials in one order?",
       "Yes. Minimums are confirmed per product and size in the quotation, and samples can cover several lines."),
    ],
    figures=[('shiba-inu-chewing-coffee-wood-stick.jpg','A Shiba Inu lying on the floor gnawing a coffee wood chew stick',"Gnawing rather than cracking. Chewing style decides which material suits a dog, more than the dog's weight does."),('puppy-with-rope-and-fiber-ball.jpg','Puppy nosing a natural fiber ball with a rope loop on a tiled floor','Fetch and carry is a different job from chewing — give each product one role in the range.'),('coconut-fiber-balls-and-rope-toy.jpg','Two coconut fiber balls of different sizes and a knotted rope toy','Balls and rope from the same coir line — one material, three formats.'),('catalogue-dog-with-hemp-ball.jpg','Golden retriever holding a hemp rope ball','Catalogue image: hemp rope balls for carrying and fetch.'),('catalogue-coffee-wood-six-sizes.jpg','Six coffee wood chew sizes from XS to XXL on a cream background','Catalogue image: the six standard CC01 sizes, XS to XXL.')])

add("are-coffee-wood-chews-safe-for-dogs","Natural chew toys",
    "Are Coffee Wood Chews Safe for Dogs?",
    "A practical look at coffee wood chew suitability, hard-chew risks, product inspection and the instructions retailers should give owners.",
    answer("<strong>Short answer:</strong> coffee wood chews can suit many adult dogs that gnaw rather than crack, when the chew is the "
           "right size, used under supervision and replaced once it cracks or wears small. For strong chewers, choose the thicker Gorilla line "
           "rather than a standard stick. Either way it is a toy, not food — pieces should not be swallowed."),
    [
    ("What a coffee wood chew is",
      p("A <dfn>coffee wood chew</dfn> is a stick cut from the stem wood of the coffee tree, seasoned, dried and shaped into a non-edible "
        "chew toy. VietPaw chews are one untreated plant material: no glue, coating, preservative or colouring. Every batch is dried to "
        "below 14% moisture before packing, and any cracked piece is removed at grading.")
      + p("The stick comes from the stem, not from the bean or the cherry. We do not publish a caffeine-free claim: no laboratory result has "
          "been produced for this material, and we would rather say so than print a figure nobody has measured.")
      + p("Its plant origin tells you where the chew comes from. It does not tell you whether it suits a particular dog’s teeth, mouth size "
          "or way of chewing — that is the real safety question.")),

    ("The risks, one by one",
      spec_table(["Risk","What can happen","How to reduce it"],[
        ("Strong chewing","A dog that bites down hard can wear down or split a standard stick quickly.","Choose the thicker Gorilla line for strong chewers; ask a vet first for puppies, seniors and dogs with dental problems."),
        ("Swallowing whole","A stick that is too small, or worn down small, can be swallowed or lodge in the throat.","Choose by the weight band and go up one size when in doubt; replace before it is swallowable."),
        ("Breaking off pieces","A powerful chewer can split a stick and swallow hard fragments.","Remove the chew at the first crack or split; stop using it if the dog tries to break pieces off."),
        ("Splinters","No supplier in this category has test data behind “splinter-free”.","In normal gnawing the surface wears into soft fibres; supervision covers the exceptions."),
        ("Softening in storage","Wood that picks up moisture softens and wears faster.","Keep bags sealed and store dry; chews are packed below 14% moisture."),
      ], caption="Hard is not the same as safe. The chew’s size and the dog’s chewing style decide most of the outcome.")
      + p("Size is the control that matters most. A chew that stays comfortably larger than the dog’s mouth is harder to swallow and lasts "
          "longer; for a dog that chews hard, the Gorilla line adds far more wood per piece than a longer standard stick.")),

    ("Which dogs it suits — and which it does not",
      fit(["Adult dogs that gnaw and shred slowly.",
           "Dogs that settle with a chew for a supervised session.",
           "Owners who will check the chew and replace it when it cracks or wears small."],
          ["The dog is a determined power chewer — choose the Gorilla line instead.",
           "The dog has dental disease, is a senior, or is a puppy still changing teeth.",
           "The owner wants an edible or digestible chew — this is not food.",
           "Nobody will be supervising, or the piece is small enough to swallow."],
          suit_head="Usually a reasonable choice", less_head="Choose something else when")),

    ("Using a coffee wood chew safely, step by step",
      steps([
        ("Choose the size","Start from the dog’s weight band, then go up one size for a dog at the top of the band or a keen chewer.","A chew that stays larger than the dog’s mouth for longer."),
        ("Inspect it before the first use","Look along the stick and at both ends for cracks, splits or sharp projections.","A damaged piece never reaches the dog."),
        ("Supervise the first sessions","Watch how the dog chews: gnawing and shredding, or biting down to crack.","You know within a few sessions whether this product suits the dog."),
        ("Check it before every session","Look for new cracks and compare its size with the dog’s mouth.","Wear is caught before it becomes a hazard."),
        ("Replace it on condition, not on the calendar","Remove it if it cracks, splits, breaks into hard pieces or wears small enough to swallow.","No damaged chew stays in use to reach a number of days."),
      ])
      + p(SAFETY)),

    ("VietPaw size reference",
      coffee_size_table()
      + p("When a dog sits at the top of a band, or is known to be a determined chewer, go up one size. The consequence of being one size too "
          "large is a chew that lasts longer; the consequence of being one size too small is the thing everybody is trying to avoid.")
      + "<h3>Gorilla line for strong chewers</h3>" + p(GORILLA) + gorilla_table()),

    ("What buyers should put on the label",
      p("Keep the advice short enough to be read: intended pet, size selection, supervised use, inspection and replacement. Put the same "
        "guidance on the product page and the pack.")
      + ul(["Say: not food; choose the size by weight; supervise; replace when cracked, split or worn small.",
            "Avoid: “safe for all dogs”, “splinter-free”, “indestructible”, “cleans teeth” and any lifespan in days.",
            "Refer: puppies, seniors and dogs with dental problems to a vet before using a hard chew."])
      + p("A sales claim can undo that care by creating a false expectation. The headline is remembered; the small print may not be.")),
    ],
    ("Coffee wood product specifications","/products/coffee-wood-dog-chew/"),
    related=[("Size guide","/guides/coffee-wood-chew-size-guide/"),("How long coffee wood chews last","/guides/how-long-do-coffee-wood-chews-last/"),
             ("Coffee wood vs antler, nylon and rawhide","/guides/coffee-wood-vs-antler-nylon-rawhide/"),("Quality-control workflow","/quality-control/")],
    image="coffee-wood-chew-grain-detail.jpg",
    faqs=[
      ("Are coffee wood chews safe for puppies?",
       "Ask a vet first. Puppies are still changing teeth, and a hard chew can damage them. If a vet agrees, choose a size the puppy cannot "
       "swallow and supervise every session."),
      ("Can dogs eat coffee wood?",
       "No. A coffee wood chew is a toy, not food. In normal gnawing the surface wears into soft fibres; hard pieces or chunks should not be "
       "swallowed, and a chew that breaks into pieces should be removed."),
      ("Do coffee wood chews contain caffeine?",
       "The chew is cut from the stem wood, not the bean or cherry. We do not publish a caffeine-free claim because no laboratory result has "
       "been produced for this material; ask us if your market requires a test."),
      ("Do coffee wood chews splinter?",
       "They usually wear into soft frayed fibres rather than sharp splinters, but that is an observation, not a guarantee. A powerful chewer "
       "can break a piece off, and no supplier in this category has test data behind “splinter-free”."),
      ("Are coffee wood chews safe for strong chewers?",
       "Choose the Gorilla line. It is cut much thicker than a standard stick — four sizes from GRLS (155–230 g) to GRLXL (550–900 g) — "
       "so a strong chewer has far more wood to work through. Supervise and replace it when it cracks or wears small."),
      ("What if my dog swallows a piece?",
       "Contact a vet, especially if the piece was large or the dog shows discomfort, vomiting or changes in appetite. Do not keep using a chew "
       "that is breaking apart."),
    ],
    figures=[('coffee-wood-chew-grain-detail.jpg','Close-up of a finished coffee wood chew stick showing grain and surface finish','One untreated plant material: no glue, coating, preservative or colouring.'),('grading-chews-before-packing.jpg','Hand holding a coffee wood stick above a crate of graded pieces','Grading. Any cracked piece is pulled out at this bench.'),('coffee-wood-chews-three-in-vacuum-pack.jpg','Three coffee wood chews sealed in a clear vacuum bag','Vacuum-packed at our warehouse: the bag keeps the wood at its packing moisture until it is opened.'),('catalogue-dog-with-coffee-wood-stick.jpg','Golden retriever chewing a coffee wood stick on a rug','Catalogue image: supervised chewing with a correctly sized stick.')])

add("coffee-wood-vs-antler-nylon-rawhide","Natural chew toys",
    "Coffee Wood, Antler, Nylon or Rawhide: What Are You Comparing?",
    "Compare coffee wood, antler, nylon and rawhide by intended use, product construction, retail presentation and purchasing requirements.",
    answer("<strong>Short answer:</strong> coffee wood is a single untreated plant material that does not soften, swell or smell as it is "
           "chewed. Antler is an animal-derived hard chew, nylon is a synthetic polymer that does not biodegrade in normal disposal, and "
           "rawhide is an edible processed animal hide that softens as it is chewed. They are four different product categories — compare "
           "them on origin, what happens during use, import paperwork and how you explain them to customers, not on a single toughness score."),
    [
    ("What each chew is",
      p("<dfn>Coffee wood chew</dfn>: a stick cut from the stem wood of the coffee tree, seasoned, dried below 14% moisture and shaped. "
        "Non-edible; no glue, coating, preservative or colouring.")
      + p("<dfn>Antler chew</dfn>: a cut piece of naturally shed deer or elk antler. Non-edible in the usual sense; animal-derived.")
      + p("<dfn>Nylon chew</dfn>: a moulded synthetic polymer toy, often flavoured. Non-edible; made from fossil-based plastic.")
      + p("<dfn>Rawhide</dfn>: the inner layer of cattle or other animal hides, cleaned, processed and pressed or rolled. Sold as an edible chew "
          "that softens as the dog works it.")),

    ("Coffee wood vs antler vs nylon vs rawhide",
      spec_table(["","Coffee wood","Antler","Nylon","Rawhide"],[
        ("Origin","Plant (coffee tree stem)","Animal (shed antler)","Synthetic polymer","Animal (processed hide)"),
        ("Edible?","No — a toy","No","No","Yes — a treat"),
        ("During use","Wears into soft fibres; does not soften, swell or smell","Wears slowly; can chip","Wears into nubs and plastic particles","Softens and becomes pliable"),
        ("Ingredients to declare","One material, untreated","One material","Polymer, flavouring, colour","Hide plus processing agents, flavours"),
        ("End of life","Plant material","Natural material","Does not biodegrade in normal disposal","Organic material"),
        ("Import paperwork","Phytosanitary and fumigation certificates; no veterinary certificate","Animal by-product rules may apply","Standard consumer-product documents","Animal by-product rules and veterinary certification in many markets"),
        ("Strong-chewer option","Gorilla thick-cut line","Larger pieces","Heavy-duty grades","Pressed or thick rolls"),
      ], caption="Category comparison for buyers; check requirements for your market with your broker.")),

    ("Choosing between them, step by step",
      steps([
        ("Decide edible or non-edible","A treat and a toy sit in different categories, with different labels and customer expectations.","You know whether rawhide is even in the comparison."),
        ("Decide on the material story","Plant-based, animal-derived or synthetic.","A clear line for your product page and packaging."),
        ("Check the import route","Animal-derived products often need veterinary documentation; coffee wood ships with plant-health documents.","No surprise at customs."),
        ("Match strong chewers to a thick product","For coffee wood, that is the Gorilla line rather than a longer standard stick.","Fewer returns from dogs that work through a chew quickly."),
        ("Compare quotes at the same point in the supply chain","Same spec, saleable unit, pack, quantity and Incoterm.","Prices you can actually compare."),
      ])),

    ("Coffee wood facts at a glance",
      spec_table(["Item","Figure"],[
        ("Material","Coffee tree stem wood; untreated"),
        ("Moisture at packing","Below 14%, checked on every batch"),
        ("Cracks","Any cracked piece is rejected at grading"),
        ("Standard sizes","CC01 XS–XXL, 23–440 g"),
        ("Strong-chewer line","Gorilla GRLS–GRLXL, 155–900 g"),
        ("Export documents","Seven, including phytosanitary and fumigation certificates"),
        ("Minimum order","50 pcs per size"),
      ])),

    ("Compare the quote at the same point in the supply chain",
      p("A loose stick quoted at the factory and a boxed, barcoded item delivered to your warehouse are not comparable prices. Match the "
        "specification, saleable unit, packaging, quantity and delivery basis. Then include inspection, testing, transport, duties and "
        "handling where applicable.")
      + p("Also consider what the product asks of the retail operation. Will staff need a size explanation? Does each variant require a separate "
          "barcode? Can damaged packaging be replaced locally? These details can outweigh a small saving in purchase price.")),

    ("Keep material and disposal claims separate",
      p("Wood has a different origin story from nylon, but an environmental statement still needs a defined scope. A wood-and-rope combination "
        "contains several components; a paper-looking pack may include a film window. Describe what is in the product before deciding which "
        "claims belong on the label.")
      + p("Retailers need a clear way to explain the differences without making a medical promise. Describe the material and intended use, then "
          "give the owner the relevant supervision and replacement guidance.")),
    ],
    ("Compare coffee wood wholesale options","/collections/coffee-wood/"),
    related=[("Coffee wood safety considerations","/guides/are-coffee-wood-chews-safe-for-dogs/"),("How long coffee wood chews last","/guides/how-long-do-coffee-wood-chews-last/"),
             ("Natural material comparison","/guides/sustainable-pet-toy-materials-compared/")],
    image="vietpaw-coffee-wood-sizes.png",
    faqs=[
      ("Is coffee wood better than antler?",
       "They suit different buyers. Coffee wood is plant-based and ships with plant-health documents; antler is animal-derived and may fall under "
       "animal by-product rules. Both are non-edible hard chews."),
      ("Is coffee wood a good rawhide alternative?",
       "For buyers who want a non-edible chew that does not soften, swell or develop an odour, yes. It is a toy, not a treat, so it replaces the "
       "chewing activity rather than the food."),
      ("Is a nylon chew biodegradable?",
       "No. Nylon is a synthetic polymer that does not biodegrade in normal disposal."),
      ("Does coffee wood need a veterinary certificate for export?",
       "No. It is a wood article, not an animal by-product. It ships with phytosanitary and fumigation certificates among seven export "
       "documents."),
      ("Which option is best for strong chewers?",
       "For coffee wood, the Gorilla line — thick-cut chews from GRLS (155–230 g) to GRLXL (550–900 g)."),
      ("Can I say coffee wood is safer than rawhide?",
       "Avoid comparative safety claims without evidence. You can say factually that coffee wood does not soften, swell or develop an odour as it "
       "is worked."),
    ],
    figures=[('coffee-wood-chew-size-row.jpg','Six coffee wood chew sticks laid out in increasing size on a light background','Coffee wood does not soften, swell or develop an odour as it is worked — a factual difference from rawhide.'),('french-bulldog-chewing-coffee-wood.jpg','French bulldog chewing a coffee wood stick on a wooden table','A powerful chewer can still break a piece off any hard chew.'),('coffee-wood-chews-size-range-packed.jpg','Coffee wood chews in several sizes laid out in their vacuum packs','The size range, packed: each size is graded into its own diameter band.'),('coffee-wood-chews-pair-in-vacuum-pack.jpg','Two coffee wood chews with a desiccant sachet in a vacuum bag','Two sticks per pack with a desiccant sachet — one of the standard retail formats.')])

add("best-natural-chews-for-aggressive-chewers","Natural chew toys",
    "Choosing Natural Toys for Strong Chewers",
    "How retailers can respond to strong-chewer requests without confusing hardness, size or an aggressive-chewer label with guaranteed suitability.",
    answer("<strong>Short answer:</strong> for a strong chewer, the best natural option is a thick-cut coffee wood chew — VietPaw’s Gorilla "
           "line, in four sizes from GRLS (155–230 g) to GRLXL (550–900 g) — given under supervision. Rope, coir and loofah toys are made for "
           "tug, fetch or batting and can be pulled apart, so they are not chew toys for power chewers. No natural chew is indestructible: "
           "size it to the dog and replace it when it cracks or wears small."),
    [
    ("What “strong chewer” actually means",
      p("A <dfn>strong chewer</dfn> — also called an aggressive or power chewer — is a dog that destroys toys quickly. That covers several "
        "different behaviours, and each one needs a different product:")
      + ul(["<strong>Gnawers</strong> work a chew slowly with the back teeth, wearing it down over time.",
            "<strong>Shredders</strong> tear at fibres, seams and rope ends.",
            "<strong>Crackers</strong> clamp down hard to split a solid object — the dogs that need the thickest chew.",
            "<strong>Swallowers</strong> try to gulp pieces rather than chew them."])
      + p("When a customer asks for the toughest chew you sell, the next question should be which of these the dog does. “Strong chewer” is a "
          "useful opening description, but it is not a product specification.")),

    ("Natural materials for strong chewers compared",
      spec_table(["Material","Made for","Fit for a strong chewer","Main risk"],[
        ("Gorilla coffee wood (thick-cut)","Strong, persistent chewing","The best natural fit for strong chewers","Swallowing a piece once it wears small"),
        ("Standard coffee wood stick","Gnawing","Good for moderate chewers, sized up","Worn down quickly by a strong chewer"),
        ("Hemp rope","Owner-led tug and carry","Supervised tug only — not left to chew","Swallowed strands"),
        ("Coconut coir ball","Fetch and carry","Not recommended for chewing","Unwinding; swallowed fibre"),
        ("Loofah","Light play, mainly cats","Not recommended","Breaks into small pieces"),
        ("Wood-and-rope combination","Tug and chew","Check the join as much as the materials","The join or knot coming apart"),
      ], caption="Match the product to the behaviour, not to the word “tough”.")
      + p("If a dog repeatedly breaks pieces off a standard stick, move it to the Gorilla line rather than a longer stick of the same "
          "diameter: thickness, not length, is what gives a strong chewer more wood to work through.")),

    ("Matching a product to a strong chewer, step by step",
      steps([
        ("Identify the behaviour","Ask whether the dog gnaws, shreds, cracks or swallows.","A product type, not just a toughness level."),
        ("Choose the product type","Strong chewers and crackers: the Gorilla line. Gnawers: a standard stick. Shredders: not alone with rope or coir.","Fewer returns and fewer injuries."),
        ("Choose the size","Pick the Gorilla size against the dog’s mouth — the piece should stay much larger than the mouth throughout use.","A chew that cannot be swallowed and lasts longer."),
        ("Supervise the first sessions","Watch how the dog actually uses the product.","Early confirmation — or an early switch to something else."),
        ("Replace on condition","Remove the item when it cracks, splits, frays badly or wears small enough to swallow.","The weakest point is caught before it fails."),
      ])),

    ("Gorilla line sizes",
      p(GORILLA)
      + gorilla_table()
      + p("Thickness is what makes the difference for a strong chewer: material volume rises sharply with diameter, so a Gorilla piece holds "
          "several times the wood of a standard stick of similar length. For moderate chewers, the standard CC01 range (XS–XXL) is on the "
          '<a href="/products/coffee-wood-dog-chew/">coffee wood product page</a>; go up one size for a dog at the top of its weight band.')),

    ("Look for the way a design can come apart",
      p("On a rope assembly, examine the knots, ends, handle and joins between materials. On a wood chew, look at the narrow sections, ends and "
        "any crack — at VietPaw, any cracked piece is removed at grading. A larger overall measurement does not explain the weakest part of an "
        "assembled toy.")
      + p("For procurement, write down the construction you approved: rope diameter, knot arrangement, component dimensions and attachment "
          "method. If you need a pull or attachment test, agree its method and acceptance criteria; a number quoted without a method is hard to "
          "use when inspecting a later batch.")),

    ("Give replacement advice a prominent place",
      p("Owners should supervise play, remove loose pieces or long frayed strands and replace damaged or worn items. Do not bury this advice "
        "beneath an “indestructible” headline — the headline is remembered; the small print may not be.")
      + p("Use returns to refine the range. Ask for the SKU, size, batch reference, a photograph and a description of use, and keep breakage on "
          "arrival separate from damage during play. If complaints cluster around one join or one size, that gives the supplier a specific "
          "question to investigate.")
      + p(SAFETY)),
    ],
    ("Strong-chewer product selection","/collections/aggressive-chewers/"),
    related=[("Hemp rope constructions","/products/hemp-rope-dog-toy/"),("Are coffee wood chews safe?","/guides/are-coffee-wood-chews-safe-for-dogs/"),
             ("Coffee wood size guide","/guides/coffee-wood-chew-size-guide/"),("How long coffee wood chews last","/guides/how-long-do-coffee-wood-chews-last/")],
    image="vietpaw-hemp-wood-assortment.jpg",
    faqs=[
      ("What is the best natural chew for an aggressive chewer?",
       "A thick-cut coffee wood chew from VietPaw’s Gorilla line, used under supervision. It comes in four sizes, from GRLS (155–230 g) to "
       "GRLXL (550–900 g)."),
      ("Are coffee wood chews indestructible?",
       "No. They are dense and usually wear into soft fibres, but a powerful chewer can split a stick or break a piece off. Nothing in this "
       "category is indestructible."),
      ("Are rope toys safe for power chewers?",
       "Only for supervised, owner-led tug. Left alone, a strong chewer can shred rope and swallow strands."),
      ("What size chew should a strong chewer have?",
       "A Gorilla piece that stays much larger than the dog’s mouth throughout use. The four sizes run from GRLS (5–6 × 8 cm) to GRLXL "
       "(10–12 × 15 cm); confirm the choice with a sample."),
      ("Why not just buy a longer standard stick?",
       "Length adds little for a strong chewer. Thickness adds far more wood per piece, which is why the Gorilla line is cut much thicker than "
       "the standard CC01 range."),
      ("When should a strong chewer’s toy be replaced?",
       "When it cracks, splits, frays badly, loses pieces or wears small enough to swallow — on condition, not on a calendar."),
    ],
    figures=[('golden-retriever-chewing-coffee-wood.jpg','Golden retriever chewing a coffee wood stick surrounded by other chews','A strong chewer needs a thicker chew — that is what the Gorilla line is for.'),('coffee-wood-chew-size-row.jpg','Coffee wood chew sticks in six sizes on a light background','Sizing up is usually safer than sizing down for a strong chewer.'),('thick-coffee-wood-chews-vacuum-pack.jpg','Three thick, knotted coffee wood pieces in a vacuum bag','Thicker stems give more wood per piece — the idea behind the Gorilla line.'),('catalogue-dog-with-coconut-rope-toy.jpg','Golden retriever with a coconut fiber rope toy','Catalogue image: rope toys are for owner-led tug, not unsupervised chewing.')])

add("how-long-do-coffee-wood-chews-last","Natural chew toys",
    "How Long Do Coffee Wood Chews Last?",
    "There is no published lifespan for a coffee wood chew, and this explains why: what actually drives wear, how to answer the question on a product page, and when a chew must be replaced.",
    "It is the question every customer asks and the one no honest supplier can answer with a number. We do not publish a figure in days or weeks, and this page sets out why, what determines the answer for an individual dog, and what to write on your product page instead of a promise you cannot keep.",
    [
    ("The short answer",
      answer("Anywhere from a few days to several months, and the dog decides. A light gnawer may keep a size M "
             "stick for two or three months; a determined chewer can reduce the same piece in under a week. There "
             "is no published lifespan figure for coffee wood from us or from any other supplier, because "
             "durability testing for chew toys would mean testing on animals and nobody in this category has "
             "done it.")
      + p("That is an unsatisfying answer for a product page, so the rest of this guide is about what to say "
          "instead \u2014 and it turns out that a specific, honest answer converts better than a vague confident one, "
          "because customers who buy on a lifespan promise are the ones who come back to complain.")),

    ("What actually drives the difference",
      p("Four variables account for most of the spread, and only two of them are under your control as a buyer.")
      + spec_table(["Variable","Effect on lifespan","Under your control?"],[
          ("Chewing style","The largest single factor. A dog that gnaws and shreds works through material slowly; a dog that bites down to crack things can split a stick in one session.","No \u2014 but you can advise on it at the point of sale"),
          ("Size relative to the dog","A stick too small for the dog disappears fast and becomes a swallowing risk; a correctly sized one lasts far longer. Material volume rises sharply with diameter, so an XL holds much more wood than an L.","Yes \u2014 this is the sizing decision"),
          ("Time actually spent with it","A chew left down all day wears in a fraction of the calendar time of one offered for twenty minutes a session.","Partly \u2014 through your use instructions"),
          ("Moisture and storage","Wood packed and stored dry stays hard. Wood that picks up moisture in a damp warehouse softens and works down faster.","Yes \u2014 through packing spec and warehouse conditions"),
        ], caption="Two of these \u2014 sizing and storage \u2014 are yours to get right. The other two belong to the customer, which is why the instruction on the pack matters as much as the product in it.")
      + p("The manufacturing side contributes one thing that is measurable: moisture at packing, held below 14% and "
          "read with a pin-type meter on each finished batch. That is not a lifespan guarantee \u2014 it is the reason "
          "a stick arrives hard rather than soft, and a soft stick has a short life whatever the dog does with it.")),

    ("What to write on your product page",
      p("The pattern that works is: set the expectation as a range, name the variable that drives it, and give the "
        "replacement rule. Something close to this:")
      + ('<div class="callout"><p><em>\u201cHow long it lasts depends on your dog. Gentle chewers often keep a '
         'stick for weeks or months; determined chewers get through one much faster. Choose the size that matches '
         'your dog\u2019s weight, supervise chewing, and replace the chew when it cracks, splinters or wears down '
         'small enough to swallow.\u201d</em></p></div>')
      + p("Then publish the dimensions. A customer who can see that a size L is 19\u201320 cm long, 3.5\u20134.5 cm across and "
          "120\u2013180 g can judge the value themselves, and a specific number builds more confidence than a vague "
          "superlative. The full table is on the "
          '<a href="/products/coffee-wood-dog-chew/">coffee wood chew product page</a>.')
      + p("Avoid three things specifically: a lifespan in days, the word \u201cindestructible\u201d or \u201clongest-lasting\u201d "
          "without a comparison you can evidence, and \u201csplinter-free\u201d \u2014 no supplier in this category has test data "
          "behind that phrase, and an independent trainer has documented a coffee wood stick breaking into hard "
          "pieces during use.")),

    ("When the chew has to be replaced",
      p("This is the part that matters more than lifespan, and it is a condition judgement rather than a calendar one.")
      + fit(["The stick is intact, still comfortably larger than the dog\u2019s mouth, and the surface is worn smooth.",
             "The dog is gnawing and shredding rather than trying to crack the piece.",
             "Chewing is supervised and the chew is put away between sessions."],
            ["It has cracked, split lengthwise or started breaking into hard pieces \u2014 remove it immediately.",
             "It has worn down to a size the dog could swallow whole.",
             "The dog has begun biting down to break pieces off rather than gnawing.",
             "Any piece has come loose, or the dog is trying to swallow fragments rather than chew them."],
            suit_head="Fine to keep in use", less_head="Replace it now")
      + figure("/assets/img/coffee-wood-chew-size-row.jpg",
               "Hand holding four coffee wood chew sticks of increasing size for scale comparison",
               "Judge the replacement point against the dog\u2019s mouth, not against the original size. A stick that "
               "has worn down to something swallowable has to go, however much wood is left.")
      + p("A chew is not suitable for continued use just because wood remains. Never ask a customer to keep using a "
          "damaged item to reach an advertised number of days \u2014 which is one more reason not to advertise one.")
      + p(SAFETY)),

    ("Collecting feedback you can actually act on",
      p("If you want a real answer for your own range, the way to get it is customer-service records rather than a "
        "durability claim borrowed from a supplier.")
      + steps([
          ("Record five fields, not a star rating",
           "Product and size, batch reference, the dog\u2019s approximate weight, the reported pattern of use, and the reason for replacement.",
           "Data you can group, instead of a score you cannot interpret."),
          ("Separate arrival condition from wear",
           "Keep a crack found on opening a carton in a different category from a stick worn down after a month of use.",
           "Two distinct investigations \u2014 one for our factory, one for the sizing advice.",
           "Mixing them into a single durability figure makes both impossible to diagnose."),
          ("Send our factory specifics, not impressions",
           "Batch reference, photographs and the measured dimensions of the piece in question.",
           "A grading or moisture record that can actually be checked against your complaint."),
          ("Revisit the size mix after one season",
           "Look at which sizes sold, which generated complaints and what the dog weights in those complaints were.",
           "A second order sized to your customers rather than to the supplier\u2019s size chart."),
        ])
      + p("These are observations, not a controlled study, and they should not be published as one. If you ever want "
          "to state an average or make a comparative claim, that needs a defined method, relevant data and proper "
          "animal-welfare safeguards. A handful of enthusiastic reviews does not establish a performance claim.")),
    ],
    ("Coffee wood sizes, weights and full specification","/products/coffee-wood-dog-chew/"),
    related=[("Choosing the right chew size","/guides/coffee-wood-chew-size-guide/"),
             ("Coffee wood vs antler, nylon and rawhide","/guides/coffee-wood-vs-antler-nylon-rawhide/"),
             ("Are coffee wood chews safe for dogs?","/guides/are-coffee-wood-chews-safe-for-dogs/"),
             ("Inspection and quality control","/quality-control/")],
    image="coffee-wood-chew-grain-detail.jpg",
    faqs=[
      ("How long does a coffee wood chew last on average?",
       "We do not publish an average, because the spread between a gentle chewer and a determined one is wider than any "
       "average would be useful for \u2014 days at one end, months at the other. Publish the dimensions and the replacement "
       "rule instead; customers can judge value from a real specification."),
      ("Does a bigger size last longer?",
       "Usually yes, and by more than the length suggests. Material volume rises with the square of the diameter, so an "
       "XL at 4.5\u20135.5 cm across holds considerably more wood than an L at 3.5\u20134.5 cm even though they differ by only "
       "2\u20133 cm in length. Size up only if the dog\u2019s weight supports it \u2014 an oversized chew is awkward rather than "
       "better."),
      ("Why does one stick last much longer than another of the same size?",
       "Coffee wood is a natural material and density varies from stem to stem, so two sticks in the same size band are "
       "not identical pieces. Grading controls the diameter band and the crack limit; it does not make every piece the "
       "same density. Storage matters too: a stick that has picked up moisture works down faster."),
      ("Can I advertise that these last longer than rawhide?",
       "Only with a comparison you can evidence, and we are not aware of published data supporting it for this material. "
       "What you can say factually is that coffee wood does not soften, swell or develop an odour as it is worked, which "
       "is a different \u2014 and defensible \u2014 statement about how it behaves."),
      ("When exactly should a customer throw the chew away?",
       "When it cracks or splits, when it starts breaking into hard pieces, when it has worn down small enough to swallow "
       "whole, or when the dog switches from gnawing to trying to crack pieces off. Condition decides, not the calendar."),
      ("Does the moisture level affect how long it lasts?",
       "Yes. Chews are packed below 14% moisture and that is why they arrive hard. Wood that picks up moisture in a damp "
       "warehouse softens and wears faster, so keep bags sealed until they go out, store on pallets away from exterior "
       "walls and roller shutters, and aim for around 25\u201328 \u00b0C with air circulation."),
    ],
    figures=[('coffee-wood-chew-size-row.jpg','Coffee wood chew sticks in six sizes on a light background','Material volume rises sharply with diameter — an XL holds far more wood than an L.'),('coffee-wood-chew-grain-detail.jpg','Close-up of a coffee wood chew surface showing the grain','In normal chewing the surface wears into soft fibres; replace the chew once it is small enough to swallow.'),('coffee-wood-chews-graded-sizes-stacked.jpg','Packs of graded coffee wood chews stacked from small to large','Graded sizes stacked from smallest to largest, ready for cartoning.')])

add("plastic-free-biodegradable-pet-toys-guide","Materials & claims",
    "Plastic-Free Pet Toys: What Belongs in the Buying Brief?",
    "Specify plastic-free pet toys and packaging clearly, with separate decisions on materials, components and end-of-life claims.",
    answer("<strong>Short answer:</strong> a pet toy is plastic-free only when every component — body, core, thread, adhesive, finish, tag — "
           "contains no plastic, and a plastic-free <em>pack</em> is a separate claim covering the bag, sleeve, window and insert. Write both into "
           "the buying brief as a component list, choose packaging that still protects the goods in transit, and keep “plastic-free” "
           "separate from “biodegradable”, which is a different claim needing different evidence."),
    [
    ("What plastic-free means",
      p("<dfn>Plastic-free</dfn> is a statement about composition: no component is made from plastic, including synthetic fibres, plastic "
        "threads, polymer adhesives, laminates and coatings. It says nothing about how the product breaks down at end of life.")
      + p("A toy can look entirely natural on a shelf and still contain synthetic binding thread, an internal core or a laminated tag. If "
          "plastic-free is part of your brand promise, those small components belong in the first conversation with the factory, not in a "
          "discussion after the packaging has been printed.")),

    ("Where plastic hides in a natural pet toy",
      spec_table(["Component","Where plastic can appear","Plastic-free option","What to verify"],[
        ("Toy body","Rarely, if the body is wood, coir, hemp or loofah","Coffee wood, coconut fiber, hemp, loofah","Material identity per approved sample"),
        ("Core or filling","Foam or plastic core in a wound ball","Fibre-only winding","Cut sample or construction declaration"),
        ("Thread and binding","Polyester or nylon sewing thread","Natural-fibre thread","Thread type on the component list"),
        ("Adhesive","Polymer glue at joins or winding ends","Mechanical fixing; no glue","Whether any adhesive is used"),
        ("Tag and label","Laminated or coated paper; plastic tag fastener","Uncoated paper; cotton or paper tie","Tag stock and fastener"),
        ("Retail pack","Poly bag, vacuum film, window film","Kraft box or paper sleeve","Coating, lamination, window"),
        ("Moisture protection","Plastic desiccant sachet, film liner","Paper-based sachet where suitable","Sachet material and performance"),
      ], caption="VietPaw coffee wood chews are one untreated material — no glue, coating, preservative or colouring.")),

    ("Writing a plastic-free brief, step by step",
      steps([
        ("Decide the boundary","Toy only, retail pack, or the complete delivered unit.","One clear promise the supplier can quote."),
        ("List components inside-out","Body, core, rope, thread, adhesive, finish, decoration — then bag, sleeve, label, window, insert.","A checklist the factory can confirm line by line."),
        ("Choose packaging for the journey","Ask how the goods will be protected against moisture and damage in transit.","Protection that does not rely on plastic you have excluded."),
        ("Approve the sample and the pack together","Confirm materials against the component list.","A reference for every repeat order."),
        ("Lock substitutions","Require approval for any change of thread, coating or packaging.","The claim stays true on reorders."),
      ])),

    ("VietPaw packaging options",
      spec_table(["Option","Minimum","Note"],[
        ("Bulk bag","With the order","Protective bulk packing; confirm material"),
        ("Individual pack","With the order","Confirm film or paper"),
        ("Paper or kraft box","With the order","Check coating and window"),
        ("Printed box, hang tag or label","500 pcs per SKU","Your artwork; specify uncoated stock if required"),
        ("Laser engraving (coffee wood)","50 pcs","Branding burned into the wood — no label needed on the product"),
      ])
      + p("Vacuum packing is a method, not a material description, and kraft-coloured paper may be coated or laminated. If your brief excludes "
          "these, resolve the alternative before approving the sample.")),

    ("Keep biodegradability out of the material shortcut",
      p("Plastic-free describes composition. Biodegradable describes breakdown under particular conditions; compostable adds another set of "
        "questions. One claim does not establish the others, and FTC guidance expects environmental claims to be qualified and supported.")
      + p("Where evidence is limited, precise language still works: “coffee wood stick”, “coconut-fiber outer surface”, “paper sleeve”. A "
          "customer should be able to understand exactly what each statement covers.")),
    ],
    ("Plan a plastic-free product range","/collections/plastic-free/"),
    related=[("Material and packaging approach","/sustainability/"),("Are dog toys biodegradable?","/guides/are-dog-toys-biodegradable/"),
             ("Natural materials compared","/guides/sustainable-pet-toy-materials-compared/")],
    sources=[("FTC environmental-claims guidance",FTC)],
    faqs=[
      ("What makes a pet toy plastic-free?",
       "Every component — body, core, thread, adhesive, finish and tag — contains no plastic. The pack is a separate claim."),
      ("Are coffee wood chews plastic-free?",
       "The chew itself is one untreated material with no glue, coating, preservative or colouring. Whether the retail unit is plastic-free "
       "depends on the pack you choose."),
      ("Is kraft paper packaging always plastic-free?",
       "No. Kraft-coloured paper can be coated or laminated, and a box may have a film window. Confirm the material specification."),
      ("Can I call a plastic-free toy biodegradable?",
       "Not on that basis. Plastic-free is about composition; biodegradable needs evidence for the finished product under stated disposal "
       "conditions."),
      ("How do I keep a plastic-free claim true on reorders?",
       "Keep the component list with the approved sample and require written approval for any change of material, thread or packaging."),
    ],
    figures=[('bagged-chews-with-desiccant.jpg','Coffee wood chews in a sealed bag with a desiccant sachet','The toy, the bag, the box and any ink are four separate claims, not one.'),('loofah-duck-cat-toy.jpg','Loofah gourd fibre cut into a duck-shaped cat toy','Plant-derived is not the same as certified compostable.'),('coffee-wood-chews-pack-with-desiccant.jpg','Coffee wood chews packed with a labelled desiccant sachet','Moisture protection is part of the pack specification — agree the sachet material as well as the bag.'),('hemp-rope-ball-vacuum-packed-size-l.jpg','Hemp rope ball vacuum-packed with a size L label','Size label on the pack: the same reference should appear on the quote and the packing list.')])

add("are-dog-toys-biodegradable","Materials & claims",
    "Are Dog Toys Biodegradable? Read the Claim Closely",
    "What a biodegradable dog toy claim should cover, and how to check the product, test scope and disposal instructions before printing it.",
    answer("<strong>Short answer:</strong> some dog toy <em>materials</em> are biodegradable, but very few finished dog toys can honestly "
           "be sold as biodegradable. Plant materials such as wood, coconut coir, hemp and loofah break down under the right conditions; "
           "nylon, TPR and most plastics do not in normal disposal. A biodegradable claim has to cover the whole finished toy and its pack, "
           "name the disposal conditions and time period, and be backed by test evidence for that product."),
    [
    ("Biodegradable, compostable, degradable: what the words mean",
      p("<dfn>Biodegradable</dfn> means microorganisms break a material down into water, carbon dioxide (or methane) and biomass. The word says "
        "nothing about how long that takes or where, which is why an unqualified claim is so easy to misread.")
      + p("<dfn>Compostable</dfn> means the material breaks down in a composting process within a defined time and leaves no harmful residue. "
          "<em>Industrial</em> composting runs hotter and faster than a <em>home</em> compost heap, and the two are tested to different standards.")
      + p("<dfn>Degradable</dfn> or <dfn>oxo-degradable</dfn> usually means a plastic fragments into smaller pieces. Fragmenting is not "
          "biodegrading, and oxo-degradable plastics are restricted in the EU.")),

    ("Dog toy materials compared",
      spec_table(["Material","Origin","Breaks down in normal disposal?","What a claim still needs"],[
        ("Coffee wood","Stem wood of the coffee tree","Wood decomposes, slowly, depending on conditions","Evidence for the finished chew and stated conditions"),
        ("Coconut coir","Husk fibre, a coconut by-product","Plant fibre decomposes; coir is known to be slow","A full component list — core, binding thread, adhesive"),
        ("Hemp fibre","Plant-derived fibre","Plant fibre decomposes","Fibre identity, blends and any synthetic thread"),
        ("Loofah","Dried gourd fibre","Plant fibre decomposes","Complete toy construction and any attachments"),
        ("Natural rubber","Latex from rubber trees","Very slowly; depends on additives","Formulation and test evidence"),
        ("Nylon, TPR, most plastics","Fossil-based polymers","No — they persist and fragment","Not a biodegradable product"),
      ], caption="General material behaviour, not a claim about any finished VietPaw product.")
      + p("The important word in a biodegradability claim is often the one that is missing. Which part of the product? Under what conditions? "
          "Over what period? Without those details, the same label means very different things to a manufacturer, a retailer and the person "
          "disposing of the toy.")),

    ("What the rules require",
      spec_table(["Market","Rule","What it means for a dog toy"],[
        ("United States","FTC Green Guides (16 CFR 260.8)","An unqualified degradable claim needs evidence that the entire item fully decomposes within a reasonably short time — the FTC says one year — after customary disposal. Items usually landfilled should not carry unqualified degradable claims."),
        ("European Union","Directive (EU) 2024/825, applying from 27 September 2026","Generic environmental claims such as “eco-friendly” or “biodegradable” are banned unless the trader can show recognised excellent environmental performance relevant to the claim."),
        ("Composting standards","EN 13432 (industrial); home-compost schemes such as OK compost HOME","A compostable claim should name the standard and whether it means industrial or home composting."),
      ], caption="Summary for orientation. Have the final wording for your market reviewed before printing.")),

    ("How to check a biodegradable claim before you print it",
      steps([
        ("List every component","Toy, core, thread, adhesive, dye, tag, bag, window film and insert.","You know exactly what the claim would have to cover."),
        ("Split the product from the pack","Customers throw away the bag on day one and the toy months later.","Two separate claims, each with its own evidence."),
        ("Match the evidence to your SKU","A report should identify the sample, method, conditions, result and limitations.","Evidence that covers your construction — not a brochure about the raw fibre."),
        ("Name the disposal route","Landfill, home compost and industrial compost are different environments.","An instruction customers can follow and local systems accept."),
        ("Have the wording reviewed","Check it against the rules for each market you sell in.","A claim you can defend if a regulator or competitor asks."),
        ("Keep a claim file","Save the wording, evidence, approved bill of materials and artwork version together.","Repeat orders do not silently change what the claim covers."),
      ])),

    ("What VietPaw can and cannot state",
      spec_table(["Statement","Can we support it?","Why"],[
        ("Made from coffee wood, coconut coir, hemp or loofah","Yes","Material identity, per approved sample"),
        ("Coffee wood chews are untreated — no glue, coating, preservative or colouring","Yes","One material, no additives"),
        ("Full component list for your SKU","Yes, on request","Part of the approved specification"),
        ("“Biodegradable” or “compostable” finished toy","No","No finished-product test or certificate is published"),
        ("A decomposition time in days or months","No","No test evidence for the finished product"),
      ])
      + p("Customers can understand a clear material story without being given an unsupported disposal promise. If the evidence does not "
          "support the claim you want, use a narrower description of the actual material.")),

    ("Disposal conditions are part of the claim",
      p("A customer should not be told to bury a toy or put it into a local compost collection simply because its main material comes from a "
        "plant. Local acceptance and the evidence supporting the instruction both matter.")
      + p("The packaging needs its own review. Combining the disposal advice for toy and pack into one green symbol can leave both instructions "
          "unclear.")),
    ],
    ("Explore VietPaw's material collections","/materials/"),
    related=[("Plastic-free buying brief","/guides/plastic-free-biodegradable-pet-toys-guide/"),("Sustainability and packaging","/sustainability/"),
             ("Natural materials compared","/guides/sustainable-pet-toy-materials-compared/")],
    sources=[("FTC guidance on degradable claims",FTC),
             ("EU Directive 2024/825 on empowering consumers for the green transition","https://eur-lex.europa.eu/eli/dir/2024/825/oj")],
    image="vietpaw-loofah-growing.png",
    faqs=[
      ("Are natural dog toys biodegradable?",
       "Their plant materials — wood, coir, hemp, loofah — decompose under the right conditions. Whether a finished toy can be called "
       "biodegradable depends on every component, the disposal conditions and test evidence for that product."),
      ("Can I label a coffee wood chew as biodegradable?",
       "Not without evidence for the finished chew under stated disposal conditions. You can say what it is made of: untreated coffee wood, with "
       "no glue, coating, preservative or colouring."),
      ("Are coconut fiber toys biodegradable?",
       "Coir is a plant fibre, but a coir ball may also contain a core, binding thread or adhesive. The claim has to cover all of them."),
      ("Is compostable the same as biodegradable?",
       "No. Compostable means breaking down within a defined time in a composting process, tested to a named standard such as EN 13432 for "
       "industrial composting. Home and industrial composting are different."),
      ("How long does a natural dog toy take to break down?",
       "There is no reliable general figure. It depends on the material, construction, size and conditions; VietPaw does not publish a "
       "decomposition time."),
      ("Can I still use “eco-friendly” in the EU?",
       "From 27 September 2026, generic environmental claims like “eco-friendly” are banned in the EU unless you can show recognised excellent "
       "environmental performance. Specific, evidenced statements about the material are the safer route."),
    ],
    figures=[('loofah-gourd-on-the-vine.jpg','A green loofah gourd hanging from its vine','Loofah is grown as a crop, so we do not describe it as agricultural waste.'),('marking-cartons-warehouse.jpg','Worker marking export cartons in a warehouse','Disposal claims need evidence for the finished assembly under stated conditions.'),('coconut-fiber-ball-top-view.jpg','Wound coconut fiber ball seen from above on a marble surface','A wound coir ball: the texture is the product — specify diameter and finished weight with it.'),('catalogue-coconut-fiber-ball-with-coconut.jpg','Coconut fiber ball next to a split coconut','Catalogue image: coir comes from the husk around the coconut.')])

add("what-is-coconut-fiber-pet-toys","Materials & claims",
    "Coconut Fiber in Pet Toys: Texture, Construction and Quality",
    "Understand coconut coir pet toys, including ball construction, winding consistency, loose fiber and wholesale packing considerations.",
    answer("<strong>Short answer:</strong> coconut fiber, or coir, is the coarse fibre from the husk around a coconut. In pet toys it is "
           "cleaned, dried and wound into textured balls — or twisted into rope — for fetch, carrying and batting play. It is a by-product "
           "of the coconut food and oil trade, it sheds short fibres as it is worked, and it is a play toy, not a chew for forceful chewers."),
    [
    ("What coconut fiber is",
      p("<dfn>Coir</dfn> is the fibre between the hard shell of the coconut and its outer skin. The husk is a by-product of the food and oil "
        "trade, so the fibre is a reuse stream rather than a crop grown for toys. Brown coir, from mature coconuts, is the coarse, stiff fibre "
        "used for textured pet toys; white coir, from green husks, is finer and softer.")
      + p("The texture is what buyers are purchasing. Coir has a springy, fibrous surface that feels different from moulded rubber or plastic in "
          "the mouth, and it sheds short fibres as it is worked. That shedding is normal for the material and is the main expectation to set on "
          "a product listing.")
      + p("What coir does not give you is an engineering spec. There is no published density, tensile or durability standard for a wound coir "
          "ball. It is a material you specify by approved sample and measured dimensions.")),

    ("Coconut fiber compared with other toy materials",
      spec_table(["","Coconut coir","Hemp rope","Loofah","Rubber / TPR"],[
        ("Feel","Coarse, springy, textured","Firm, twisted fibre","Light, open, spongy","Smooth, elastic"),
        ("Typical play","Fetch, carry, cat batting","Tug and carry","Cat batting and carrying","Chewing and fetch"),
        ("Sheds with use","Short fibres","Strands if frayed","Small pieces","Chunks if bitten through"),
        ("Main check","Winding, core, loose ends","Knots, ends, joins","Attachments, crumbling","Formulation, bite-through"),
        ("Strong chewers","Not recommended","Owner-led tug only","Not recommended","Depends on the product"),
      ], caption="General material behaviour; the approved sample decides the specification.")
      + p("Do not use coconut fiber and hemp interchangeably. They are different materials, even when both look brown and rustic. A material "
          "declaration is more reliable than matching the colour of a rope to a catalogue image.")),

    ("How a coir ball is put together",
      steps([
        ("Separate and clean the fibre","Fibre is separated from the husk, cleaned and dried.","Dry, clean fibre that will not turn musty in the carton."),
        ("Wind the ball","Fibre is wound around itself or around a core to the target diameter.","The ball’s size and density — the step that varies most between makers."),
        ("Secure the ends","The start and finish of the winding are tucked, bound or fixed.","Fewer loose ends at play; a component to declare if thread or adhesive is used."),
        ("Trim and shape","Protruding fibres are trimmed and the shape checked.","A consistent outline across the batch."),
        ("Inspect","Diameter, weight, loose strands, odour and any attachment are checked.","Musty, contaminated or poorly wound units are removed."),
        ("Pack","Single, multi-pack or assortment, with the agreed tag or box.","Units per pack and per carton match the order."),
      ], )
      + p("Ask how your sample was built. Two coir balls of the same diameter can differ in weight, winding and internal construction, and a "
          "core or binding may not be visible in the sales photograph.")),

    ("VietPaw coconut fiber range at a glance",
      spec_table(["Item","Detail"],[
        ("Products","Coconut fiber cat ball; coconut fiber dog ball (S / M / L references)"),
        ("Sizes","Diameter and finished weight set by the approved sample"),
        ("Minimum order","Selected standard lines from 50 pcs; per-size minimum confirmed in the quote"),
        ("Branding","Hang tags, labels or small boxes; printed items from 500 pcs per SKU"),
        ("Samples","3 free samples; you cover the courier"),
        ("Production","Three own factories in Vietnam; 100,000 pcs a month across the range"),
      ])),

    ("A cat ball is not simply the smallest dog ball",
      p("Specify the intended pet and type of play. For a cat range, consider dimensions, finished weight, surface construction and any "
        "decoration. For dogs, the fetch or carry use may lead to a different design. Neither becomes suitable for forceful chewing just "
        "because it is labelled natural.")
      + p("Instructions should call for supervised play and removal of loose strands or damaged parts. A bell, tail or other attachment deserves "
          "its own inspection rather than being treated as a cosmetic extra.")),

    ("What to compare across a sample set",
      ul(["Diameter and finished weight, measured consistently rather than judged from a photograph.",
          "Winding density and whether the shape holds across the sample set.",
          "Loose fibre, protruding ends and the security of any attachment.",
          "Odour, visible contamination and the condition of the packing."])
      + p("Agree which natural differences are acceptable and which are defects. A range of brown shades is a different issue from an "
          "unapproved core or a poorly secured join. For freight, confirm units per pack, packs per carton, carton dimensions and gross weight — "
          "a loose assortment and a retail multi-pack can have very different carton volumes.")),
    ],
    ("Coconut fiber wholesale collection","/collections/coconut-fiber/"),
    related=[("Cat ball specifications","/products/coconut-fiber-cat-ball/"),("Dog ball specifications","/products/coconut-fiber-dog-ball/"),
             ("Coconut-fiber cat toys for wholesale","/guides/wholesale-coconut-fiber-cat-toys-supplier/"),("Natural materials compared","/guides/sustainable-pet-toy-materials-compared/")],
    image="vietpaw-coconut-fiber-balls.jpg",
    faqs=[
      ("Is coconut fiber the same as coir?",
       "Yes. Coir is the name for coconut husk fibre. Brown coir from mature coconuts is the coarse type used in textured pet toys."),
      ("Are coconut fiber toys safe for dogs?",
       "They are designed for supervised fetch and carry play, not for forceful chewing. Choose a size that cannot be swallowed, remove loose "
       "strands and replace the toy when it starts to come apart."),
      ("Do coir toys shed?",
       "Yes, short fibres come away as the toy is worked. That is normal for the material; a toy that unwinds or loses large clumps should be "
       "replaced."),
      ("Can coconut fiber toys get wet?",
       "Coir tolerates moisture better than many plant fibres, but a toy should be dried thoroughly after it gets wet. Store stock dry; musty "
       "units are rejected at inspection."),
      ("Is coconut fiber good for cats?",
       "A light, textured coir ball suits batting and chasing. Specify the cat version separately — diameter, weight and any attachment — rather "
       "than using the smallest dog ball."),
      ("What is the minimum order for coconut fiber toys?",
       "Selected standard lines start from 50 pcs; the per-size minimum is confirmed in the quote. Printed tags, labels and boxes start at "
       "500 pcs per SKU."),
    ],
    figures=[('vietpaw-coconut-fiber-balls.jpg','Hand holding several wound coconut fiber balls outdoors','Coir from the husk — a by-product of the coconut food and oil trade.'),('puppy-with-rope-and-fiber-ball.jpg','Puppy with a natural fiber ball and rope loop','Specify diameter and finished weight together; diameter alone hides a loosely wound batch.'),('coconut-fiber-ball-sizes-with-rope-toy.jpg','Small and large coconut fiber balls beside a coir rope toy','Two ball sizes side by side: size names only mean something with measured diameters.'),('catalogue-coconut-fiber-balls-s-m-l.jpg','Coconut fiber balls in sizes S, M and L','Catalogue image: coconut fiber balls, S, M and L.'),('catalogue-corgi-with-coconut-fiber-balls.jpg','Corgi lying beside coconut fiber balls','Catalogue image: coir balls are made for fetch and carry play.')])

add("non-toxic-cat-toys-wholesale-buying-guide","Materials & claims",
    "Buying Natural Cat Toys: What to Check Beyond Non-Toxic",
    "A wholesale guide to cat toy materials, small components, sample inspection, packaging and evidence behind non-toxic claims.",
    answer("<strong>Short answer:</strong> “non-toxic” is not a defined standard for pet toys, so on its own it tells a buyer very little. "
           "Check four things instead: the complete component list, how small parts and attachments are secured, test evidence that names your "
           "product and the substances assessed, and clear play and replacement instructions. Natural cat toys made from loofah or coconut "
           "fiber still need the same checks."),
    [
    ("What “non-toxic” does and does not mean",
      p("<dfn>Non-toxic</dfn> is a general marketing term. For pet toys there is no single legal definition or certification behind it, so it "
        "does not identify the material, the substances tested, or how an attachment is secured. Like any product claim, it must be truthful "
        "and supported by evidence.")
      + p("A more useful description names what the toy is made of and what was checked: “loofah gourd fibre, uncoloured, no filling”, backed by "
          "the relevant report where one exists.")),

    ("Natural cat toy materials compared",
      spec_table(["Material","Typical cat format","What to check","Watch for"],[
        ("Loofah","Cut shapes: fish, mouse, roll","Shape, thickness, edge finish","Thread, eyes, tails, filling"),
        ("Coconut fiber (coir)","Textured balls","Diameter, weight, winding","Core, binding, loose fibre"),
        ("Hemp","Balls and small rope forms","Fibre declaration, knots","Synthetic blends, loose strands"),
        ("Catnip (optional)","Filling or inclusion","Amount and source per SKU","Assumed from a photo"),
        ("Dyes and coatings","Colour or finish","Whether any are used","“Undyed” claims that do not match"),
      ], caption="The approved sample, not the material name, defines the product.")),

    ("Checking a natural cat toy, step by step",
      steps([
        ("Get the complete component list","Body, thread, eyes, loop, wand, tail, filling, colour, coating, fragrance, catnip.","Every part you might need to test or declare."),
        ("Inspect small parts on the sample","Seams, knots and attachment points; look for loose parts and strands.","Physical risks a chemical report does not cover."),
        ("Define the test question","Give the reviewer the construction, destination market and claims you want to make.","A test plan that answers a specific question."),
        ("Read the report scope","Sample identity, substances or properties, method, result and limitations.","Evidence you can connect to your SKU."),
        ("Write the pack instructions","Play type, supervision, and when to remove damaged toys or loose parts.","Readable advice on even a small pack."),
      ])),

    ("VietPaw cat toy references",
      spec_table(["Product","Sizes","Minimum","Branding"],[
        ("Loofah cat toy","Dimensions confirmed per shape","Quoted per shape","Tags, labels or small boxes; printed items from 500 pcs per SKU"),
        ("Coconut fiber cat ball","Diameter and weight set by sample","Selected lines from 50 pcs","Tags, labels or small boxes; printed items from 500 pcs per SKU"),
      ])
      + p("Samples: 3 free, you cover the courier. Catnip is not included in every toy; each quoted SKU states whether it is unfilled or contains "
          "catnip.")),

    ("Make testing answer a defined question",
      p("A report for one material does not establish that every finished toy is non-toxic under every condition. Retailer requirements may also "
        "be more specific than the information supplied with a standard catalogue. Resolve that difference before approving artwork.")
      + p("Keep the approved construction with the reference sample so a later substitution — a different thread, a new colour — is easy to "
          "identify and, if needed, re-assessed.")),

    ("Prepare the product for the store and the home",
      p("Show the intended play type and supervision advice clearly, and explain when damaged toys or loose components should be removed. Keep "
        "warnings readable on a small pack.")
      + p("For wholesale, define whether a set is one saleable unit or several individually labelled items. That decision affects barcodes, "
          "pack counts and how a shop replaces a damaged unit.")),
    ],
    ("Browse VietPaw's natural cat toys","/cat-toys/"),
    related=[("Loofah product details","/products/loofah-cat-toy/"),("Coconut-fiber cat toys for wholesale","/guides/wholesale-coconut-fiber-cat-toys-supplier/"),
             ("Safety testing plan","/guides/pet-toy-safety-testing-requirements/"),("Testing and documentation","/certifications/")],
    image="vietpaw-loofah-play-shapes.png",
    faqs=[
      ("Is there a non-toxic certification for cat toys?",
       "No single one. Ask for test reports that name your product, the substances or properties assessed and the method."),
      ("Are loofah cat toys safe?",
       "Loofah is a light plant fibre suited to batting and carrying. Check the complete toy — thread, eyes, tails and any filling — and remove "
       "it when it is damaged or pieces come loose."),
      ("Do VietPaw cat toys contain catnip?",
       "Only where the quoted SKU says so. Catnip is optional, and its amount and source are confirmed per product."),
      ("Can I print “non-toxic” on the pack?",
       "Only with evidence that covers the finished toy for the claim you are making. A precise material description is usually more useful."),
      ("What is the minimum order for natural cat toys?",
       "Loofah shapes are quoted per shape; selected coconut fiber lines start from 50 pcs. Printed tags, labels and boxes start at 500 pcs per "
       "SKU."),
    ],
    figures=[('cat-loofah-toys-lifestyle.jpg','Cat playing with loofah toys on a rug','There is no universal pet-safety certification to carry — ask for the report that covers your SKU.'),('loofah-bear-shape-cat-toy.jpg','Loofah fibre cut into a bear-shaped cat toy','Confirm thread, filling and attachments before printing a composition claim.'),('catalogue-cat-with-loofah-toys.jpg','Tabby cat playing with loofah toys','Catalogue image: loofah shapes for batting and carrying.'),('hemp-rope-ball-small.jpg','Small tightly knotted hemp rope ball','A small hemp rope ball — the knot is the construction to inspect.')])

add("sustainable-pet-toy-materials-compared","Materials & claims",
    "Coffee Wood, Coir, Hemp and Loofah: Choosing the Right Material",
    "Compare four natural pet toy materials by construction, product format, quality-control priorities and packaging requirements.",
    answer("<strong>Short answer:</strong> choose the material by the job the toy has to do. Coffee wood suits hard, long chewing (with the "
           "thick-cut Gorilla line for strong chewers); coconut coir suits fetch and carry; hemp suits owner-led tug and rope forms; loofah "
           "suits light cat play. Coffee stem and coconut husk are by-products of existing agriculture, while hemp and loofah are grown crops — "
           "so each has a different, and differently provable, origin story."),
    [
    ("The four materials in one line each",
      p("<dfn>Coffee wood</dfn>: stem wood from coffee trees, seasoned and dried into hard chew sticks.")
      + p("<dfn>Coconut fiber (coir)</dfn>: coarse fibre from the coconut husk, wound into textured balls.")
      + p("<dfn>Hemp fiber</dfn>: plant fibre spun into rope and used for knotted toys and balls.")
      + p("<dfn>Loofah</dfn>: the dried fibrous interior of a gourd, cut into light shapes.")),

    ("Coffee wood vs coir vs hemp vs loofah",
      spec_table(["","Coffee wood","Coconut coir","Hemp","Loofah"],[
        ("Best for","Long, hard chewing","Fetch and carry","Owner-led tug","Light cat play"),
        ("Strong chewers","Yes — Gorilla line","No","Supervised tug only","No"),
        ("Feel","Hard, dense","Coarse, springy","Firm, twisted","Light, spongy"),
        ("Wears into","Soft fibres","Short shed fibres","Strands if frayed","Small pieces"),
        ("Origin","By-product of coffee farming","By-product of coconut processing","Grown crop","Grown crop"),
        ("Priority at sample approval","Dimensions, finish, cracks, moisture","Winding, core, loose ends, weight","Fibre declaration, knots, joins","Shape, thickness, edges, attachments"),
        ("VietPaw formats","CC01 sticks, Gorilla, wood-and-rope","Cat ball, dog ball","Rope toys, balls","Cat shapes"),
      ], caption="A buying guide, not a ranking of safety or durability.")),

    ("Choosing a material, step by step",
      steps([
        ("Name the play type","Chewing, fetch, tug or batting.","One or two materials already stand out."),
        ("Name the pet and chewing strength","Cat or dog; gentle, moderate or strong.","Strong chewers go to Gorilla coffee wood."),
        ("List every component","Core, thread, adhesive, rope, attachments, pack.","An accurate composition claim."),
        ("Check the origin story you can prove","By-product (coffee stem, coconut husk) or grown crop (hemp, loofah).","Claims that match the evidence."),
        ("Compare the packed unit","Packed dimensions, carton arrangement and landed cost.","A price that reflects shipping space, not just weight."),
        ("Sample a small set","A few distinct products rather than many near-identical variants.","Sales data before you expand."),
      ])),

    ("VietPaw material facts",
      spec_table(["Material","Key figures","Minimum"],[
        ("Coffee wood","Moisture below 14% at packing; any cracked piece rejected; CC01 XS–XXL, Gorilla GRLS–GRLXL","50 pcs per size"),
        ("Coconut fiber","Cat ball; dog ball S/M/L; diameter and weight set by sample","Selected lines from 50 pcs"),
        ("Hemp","Rope and ball formats; length, rope diameter and knots quoted by design","Project-specific"),
        ("Loofah","Shapes dimensioned per design; catnip optional","Quoted per shape"),
      ], caption="All four are made in VietPaw’s three factories; printed packaging from 500 pcs per SKU.")),

    ("Separate the origin story from the product claim",
      p("Coffee-tree wood and coconut husks offer specific material-reuse stories. Hemp and loofah are plant-derived, but that does not make every "
        "supply a waste stream. If you want to say upcycled or waste-derived, ask what was sourced, from whom and at which stage.")
      + p("The full construction still matters. A hemp rope joined to wood is a mixed-material product, and a loofah shape with thread and "
          "decoration contains more than loofah. Describe combinations accurately instead of extending a single-material claim across the toy.")),

    ("Compare the finished packed unit",
      p("Material choice affects size, weight and pack design. A light item in a bulky display box may use more shipping space than its weight "
        "suggests. Ask for packed dimensions and carton arrangement while the design can still change, and review moisture protection alongside "
        "shelf appearance.")
      + p("For a repeatable range, keep one approved file per SKU: component list, dimensions, sample photographs, packing details and label "
          "wording.")),
    ],
    ("Explore the four VietPaw material collections","/materials/"),
    related=[("Coconut fiber explained","/guides/what-is-coconut-fiber-pet-toys/"),("Toys for strong chewers","/guides/best-natural-chews-for-aggressive-chewers/"),
             ("Private-label development","/services/private-label-pet-toys/"),("Material and packaging claims","/sustainability/")],
    faqs=[
      ("Which natural material is most durable for dogs?",
       "Coffee wood. For strong chewers, VietPaw’s thick-cut Gorilla line gives the most wood per piece."),
      ("Which material is best for cats?",
       "Loofah shapes and small coconut fiber balls suit batting and carrying."),
      ("Is hemp the same as coconut fiber?",
       "No. They are different plant fibres. Hemp is spun into rope; coir is the coarse husk fibre of the coconut."),
      ("Which materials are by-products?",
       "Coffee stem wood and coconut husk come from existing agriculture. Hemp and loofah are grown crops, so we do not call them waste."),
      ("Can I mix materials in one order?",
       "Yes. Minimums are confirmed per product and size, and one sample request can cover several materials."),
    ],
    figures=[('loofah-drying-under-greenhouse-cover.jpg','Rows of loofah gourds drying under a greenhouse cover','Each material has a different, and differently provable, origin story.'),('coffee-wood-seasoning-racks.jpg','Rows of coffee wood sticks seasoning on factory drying racks','Coffee stem and coconut husk have genuine by-product stories. Hemp and loofah are grown crops.'),('catalogue-coconut-fiber-rope-toys-with-coconut.jpg','Three coconut fiber rope toys beside a coconut','Catalogue image: coconut fiber rope toys in three sizes.'),('hemp-rope-balls-three-sizes.jpg','Three hemp rope balls in small, medium and large','Three hemp ball sizes: measure each against the approved sample.'),('catalogue-hemp-rope-ball-on-wood.jpg','Hemp rope ball on a wooden slice','Catalogue image: a knotted hemp ball.')])

add("sourcing-eco-pet-toys-vietnam","Sourcing & trade",
    "Sourcing Natural Pet Toys from Vietnam: The First Order",
    "Plan a first natural pet toy order from Vietnam, covering the buying brief, samples, packaging, quality checks and shipment preparation.",
    answer("<strong>Short answer:</strong> a first order of natural pet toys from Vietnam runs in six stages — brief, samples, quote, "
           "approval, production and shipment. With VietPaw, stock-packed goods take 5–7 days to produce and 30–35 days by sea to the EU "
           "or the US; orders with your own branding take 60–80 days to produce. Start with 3 free samples, then a small stock-packed "
           "order from 50 pcs per SKU."),
    [
    ("What sourcing natural pet toys from Vietnam involves",
      p("<dfn>Sourcing</dfn> here means buying finished pet toys directly from a Vietnamese manufacturer and importing them under your own "
        "name — as a brand, retailer, distributor or marketplace seller. Vietnam’s natural-material base is the reason buyers look here: "
        "coffee wood is collected in the Central Highlands, and coconut and loofah are grown in the country.")
      + p("VietPaw manufactures across four material collections — coffee wood, coconut fiber, hemp and loofah — in three factories in Dak Lak, "
          "Gia Lai and Binh Duong. Packing, quality release and export documents run from our Ho Chi Minh City office and warehouse, and "
          "goods leave from Cat Lai port.")
      + p("Most of the useful work on a first order happens before the purchase order: narrowing the assortment, approving a sample and "
          "deciding what must be ready before the goods leave Vietnam.")),

    ("First-order options compared",
      spec_table(["Option","Quantity","Packaging","Production time","Best for"],[
        ("Samples","3 free; you cover the courier","As sampled","Dispatched within 1 working day","Checking material, size and finish"),
        ("Trial Box (coffee wood)","100 pcs","Stock packaging","5–7 days","Testing several sizes and early sell-through"),
        ("Starting Box (coffee wood)","500 pcs","Stock packaging","5–7 days","A first retail or marketplace launch"),
        ("Private label","From 500 pcs per SKU","Your label, printed box or engraving","60–80 days","Launching under your own brand"),
        ("Container","429 cartons (20 ft) / 850 (40 ft)","Stock or branded","Per quotation","Distributors and repeat volume"),
      ], caption="VietPaw planning figures. Selected standard products start from 50 pcs per SKU; your quotation confirms the mix.")
      + p("A small first order is not a failure of ambition. It gives you receiving data, customer questions and sell-through by size — the "
          "information that makes the second order accurate.")),

    ("The first order, step by step",
      steps([
        ("Send a brief we can price","Destination, sales channel, product references, sizes and quantity per SKU, and whether you want stock goods, your logo or a changed construction.","An itemised quote rather than a price list."),
        ("Approve samples","Up to 3 free samples, dispatched within 1 working day once the selection and courier are confirmed.","A physical reference with written dimensions."),
        ("Agree the terms","Incoterm with a named place, payment, document list and inspection stage.","No gaps about who pays for what, or when."),
        ("Approve artwork (branded orders)","Logo, barcode, warnings and pack contents on a proof.","Locked print files; the production clock can start."),
        ("Release production","30% deposit for stock, 50% for a branded order.","5–7 days stock; 60–80 days branded."),
        ("Inspect and ship","Final check, carton marks, seal number and the seven export documents.","Balance paid against documents; 30–35 days sea transit."),
        ("Receive and record","Count, inspect against the sample and log any issue with the batch reference.","A receiving report that improves the repeat order."),
      ])),

    ("Documents and shipping data for every order",
      spec_table(["Document or data","What it is","Why it matters"],[
        ("Commercial Invoice","Goods, value and terms of sale","Customs valuation and duty"),
        ("Packing List","Contents, cartons and weights","Clearance and receiving"),
        ("Bill of Lading or Air Waybill","Transport contract and receipt","Taking delivery of the goods"),
        ("Certificate of Origin","EUR.1 for the EU under the EVFTA; Form B as standard; Form VJ for Japan","Claiming preferential duty where the goods qualify"),
        ("Phytosanitary Certificate","Plant-health certificate for plant-based goods","Required by many destinations for wood and fiber"),
        ("Fumigation Certificate","Treatment record for the shipment","Wood and packaging import rules"),
        ("Forest-Product Declaration","Proof of legal acquisition of the material","A prerequisite for the Certificate of Origin"),
        ("Batch moisture readings","Coffee wood below 14% before packing","Available on request for your lot"),
        ("Master carton","51 × 31 × 39 cm, 0.062 m³, 30 per pallet","Freight booking and warehouse planning"),
      ])
      + p("We do not issue veterinary certificates — coffee wood is a wood article, not an animal by-product — or FSC certification, since "
          "coffee is an agricultural crop outside its scope. Laboratory testing is arranged separately on request. Have your forwarder or "
          "broker confirm the list for your destination before dispatch.")),

    ("Approve the retail pack as carefully as the toy",
      p("Request a sample of the proposed pack, including label placement, barcode area and any protective wrapping. Check how the product "
        "sits inside it and whether the important instructions remain readable. A product sample in a plain courier bag does not approve a "
        "future printed retail box.")
      + p("Keep the sample reference, agreed dimensions and artwork version together, and name who can approve a change. This avoids a "
          "familiar problem: a factory waiting for artwork while the buyer believes the production clock has already started.")),

    ("Build quality checks into the order",
      p("Agree the defects that matter for the construction, the inspection stage and what happens to non-conforming goods. For wood, "
        "discuss dimensions, finish, cracks and drying records. For fiber assemblies, include winding, knots and attachments. Add pack counts, "
        "labels and carton marks to the same inspection plan.")
      + p("A photograph from a previous order can show a process. It cannot replace inspection information for the lot you are purchasing. "
          "Your order needs an identifiable reference from sample approval through receiving.")),

    ("Work backwards from the date you need stock",
      spec_table(["Order type","Production","Sea transit","Factory to destination port"],[
        ("Stock packaging","5–7 days","30–35 days","About 35–42 days"),
        ("Your own branding","60–80 days","30–35 days","About 90–115 days"),
      ], caption="Add sample courier time, vessel booking, customs clearance and inland delivery.")
      + p("A factory completion date is not a warehouse delivery date. When the first shipment arrives, record any differences while the "
          "cartons and batch markings are still available. That receiving report is the foundation of a better repeat order.")),
    ],
    ("See the VietPaw ordering process","/how-to-order/"),
    related=[("Manufacturing in Vietnam","/pet-toys-manufacturer-vietnam/"),("MOQ, pricing and lead times","/guides/pet-toy-moq-fob-pricing-lead-times/"),
             ("How to vet a supplier","/guides/how-to-vet-an-eco-pet-toy-supplier/"),("Vietnam or China?","/guides/sourcing-pet-toys-vietnam-vs-china/")],
    sources=[("VietPaw export documents and testing scope","/certifications/")],
    image="export-packed-box.jpg",
    faqs=[
      ("How long does a first order from Vietnam take?",
       "With VietPaw, about 35–42 days from production start to an EU or US port for stock-packed goods (5–7 days production plus 30–35 days "
       "sea transit), or about 90–115 days with your own branding. Sample courier time, booking and clearance are extra."),
      ("What is the smallest first order?",
       "Selected standard products start from 50 pcs per SKU. For coffee wood chews, the usual first steps are a Trial Box of 100 pcs or a Starting Box of 500 pcs; "
       "private label starts at 500 pcs per SKU."),
      ("Are samples free?",
       "Yes, 3 free samples. You cover the courier, and standard samples are dispatched within 1 working day once the selection and courier "
       "arrangements are confirmed."),
      ("Which documents come with the shipment?",
       "Seven: Commercial Invoice, Packing List, Bill of Lading or Air Waybill, Certificate of Origin, Phytosanitary Certificate, Fumigation "
       "Certificate and a Forest-Product Declaration. Batch moisture readings are available on request."),
      ("Which port do goods ship from?",
       "Cat Lai, Ho Chi Minh City. Sea transit to the EU or the US is commonly quoted at 30–35 days port to port."),
      ("Can I visit the factory before ordering?",
       "Yes. Buyer visits and third-party inspection are welcome at any of our three factories; arrange in advance so the line is running when "
       "you arrive."),
    ],
    figures=[('coffee-wood-workshop-stacked-billets.jpg','Workshop interior with stacked coffee wood billets','Billets are cut to 50–70 cm in the field and held about a year in ventilated shade.'),('container-loading-forklift.jpg','Forklift loading pallets of cartons into a container','Loading port is Cat Lai, Ho Chi Minh City; 30–35 days port to port to the EU or the US.'),('coffee-wood-chews-graded-sizes-stacked.jpg','Packs of graded coffee wood chews stacked from small to large','Graded sizes stacked from smallest to largest, ready for cartoning.'),('hemp-rope-ball-packed-size-m.jpg','Hemp rope ball vacuum-packed with a size M label','Packed size M ball — pack format changes carton counts before it changes the price.')])

add("natural-dog-toy-manufacturer-vietnam","Sourcing & trade",
    "Choosing a Natural Dog Toy Manufacturer in Vietnam",
    "How to evaluate a Vietnam dog toy manufacturer by product expertise, production stages, sample consistency and order-specific capacity.",
    answer("<strong>Short answer:</strong> choose a natural dog toy manufacturer in Vietnam on three tests — it makes your material and "
           "construction in facilities it can show you, it can hold an approved sample through repeat orders, and its capacity fits your "
           "SKU mix rather than only a headline number. VietPaw manufactures coffee wood, coconut fiber, hemp and loofah toys in three "
           "factories in Dak Lak, Gia Lai and Binh Duong, with a capacity of 100,000 pieces a month."),
    [
    ("Manufacturer, trading company or sourcing agent?",
      p("A <dfn>natural dog toy manufacturer</dfn> makes chews and toys from plant materials — wood, coir, hemp, loofah — in its own "
        "production facilities, and can show you the line that makes your product. Buyers in Vietnam also meet two other kinds of supplier:")
      + spec_table(["Supplier type","What it does","What you gain","What to verify"],[
        ("Manufacturer","Makes the product in its own facilities","Direct control of specification, quality and schedule","The site that makes your SKU, and a walkthrough"),
        ("Trading company","Buys from one or more factories and resells","Range across categories, one invoice","Which factory makes each item; whether it can change"),
        ("Sourcing agent","Finds and manages factories for a fee","Local presence without your own staff","Fee structure, and who is liable if goods are wrong"),
      ])
      + p("None of these is wrong. What matters is that you know which one you are dealing with and where the work is done. VietPaw is a "
          "manufacturer: there is no trading layer between you and the production line.")),

    ("VietPaw at a glance",
      spec_table(["Item","Detail","Where to check"],[
        ("Company","Registered in Vietnam on 12 November 2019; exporting to 40+ countries","About page; contract details in your quotation"),
        ("Factories","Three own factories: Dak Lak and Gia Lai (Central Highlands), Binh Duong (south)","Factory page; visits by appointment"),
        ("Head office and export","Ho Chi Minh City office and warehouse; shipments leave from Cat Lai","Contact page"),
        ("Capacity","100,000 pcs a month across the three factories","Production slot confirmed per order"),
        ("Materials","Coffee wood, coconut fiber, hemp and loofah","Collection pages"),
        ("Coffee wood QC","Drying and quality protocol with five QC checkpoints; moisture below 14% before packing","Batch readings on request"),
        ("Minimums","From 50 pcs per SKU; private label from 500 pcs per SKU","How to order"),
        ("Lead time","5–7 days stock; 60–80 days with your own branding","Confirmed in the quotation"),
      ])),

    ("Follow one product through production",
      p("Choose a representative SKU and ask how it is made. For a rope assembly, identify who supplies the fiber, who makes the rope and where "
        "the knots and attachments are completed. For coffee wood, the path through our line looks like this:")
      + steps([
        ("Collect and cut the stems","Coffee wood is collected in the Central Highlands and cut into billets of 50–70 cm.","Raw material with a known origin."),
        ("Season the billets","Billets are held for about a year in ventilated shade.","Wood that is dry through before shaping."),
        ("Dry to the protocol","The drying and quality protocol runs with five QC checkpoints.","Moisture below 14% on every batch before packing."),
        ("Size and finish","Sticks are cut to the size bands and the surface is finished on our line.","Pieces within the size band for each SKU."),
        ("Grade","Any piece with a crack is removed at the grading bench.","Only graded pieces go to packing."),
        ("Pack and release","Packed to the approved pack, marked and released from Ho Chi Minh City.","Batch reference and moisture reading available for your lot."),
      ])
      + p("We keep the protocol’s operating parameters confidential; the published figure is the finished-batch moisture threshold, not the "
          "drying recipe. Ask for the record linked to your order.")),

    ("Evaluate capacity for your mix, not the largest headline",
      p("A monthly capacity figure tells you little about a short run of several sizes with different labels. Ask how your order fits the "
        "current schedule, which operation is likely to take the longest and when packaging must be available. A standard stick and a new "
        "mixed-material design may use different skills and approval steps.")
      + p("For a developing range, discuss the repeat order as well as the first. Can the supplier retain the approved reference and reproduce "
          "the same pack? What notice is needed for a change in quantity or size mix? Those answers matter to a retailer that cannot keep "
          "relabeling stock.")),

    ("Put the sample beside the specification",
      p("Natural materials will not look identical piece for piece. Set acceptable ranges for dimensions, weight and appearance, and "
        "distinguish them from defects. A knot in the grain and a damaged edge should not be grouped together as natural variation.")
      + p("Use the same principle for complete construction. If the sample uses one rope material, a similar-looking substitute still requires "
          "approval. Keep the component list and packaging details with the sample, so consistency does not depend on one person’s memory.")),

    ("Questions to ask any manufacturer",
      ul(["Which of your sites makes this SKU, and can I see it — in person, by video or through an inspector?",
          "Which stages, if any, involve another producer?",
          "What production slot can you give this SKU mix and pack, and what is the bottleneck?",
          "Which QC checkpoints apply, and which record will be linked to my lot?",
          "How do you retain the approved sample, and how are substitutions approved?",
          "Which company will be named on the contract and invoice?"])
      + p("Finish the review with a written quote and an agreed approval sequence. Knowing who answers product, quality and shipping questions "
          "is just as important as knowing the address of a production site.")),
    ],
    ("VietPaw pet toy manufacturing in Vietnam","/pet-toys-manufacturer-vietnam/"),
    related=[("Factory and production","/factory/"),("Supplier due diligence","/guides/how-to-vet-an-eco-pet-toy-supplier/"),
             ("Quality control","/quality-control/"),("First order from Vietnam","/guides/sourcing-eco-pet-toys-vietnam/")],
    image="process-raw-sticks.jpg",
    faqs=[
      ("Does VietPaw manufacture its own products?",
       "Yes. VietPaw manufactures in its own three factories in Dak Lak, Gia Lai and Binh Duong; there is no trading layer between you and the "
       "production line."),
      ("What is VietPaw’s production capacity?",
       "100,000 pieces a month across the three factories. The slot and dates for your order depend on the SKU mix and packaging and are "
       "confirmed in your quotation."),
      ("Which dog toys does VietPaw make?",
       "Coffee wood chews, coconut fiber toys, hemp rope toys and loofah toys, including wood-and-rope combinations made to an approved "
       "specification."),
      ("Can I visit the factory or send an inspector?",
       "Yes. Buyer visits and third-party inspection are welcome at any of the three factories. Arrange in advance so the line is running when "
       "you arrive."),
      ("What is the minimum order?",
       "Selected standard products start from 50 pcs per SKU. Private-label runs start at 500 pcs per SKU."),
      ("How do I tell a manufacturer from a trading company?",
       "Ask which site makes your specific SKU and request a walkthrough of that line. A manufacturer can show you; a trading company will "
       "usually name, or decline to name, the factories it buys from."),
    ],
    figures=[('coffee-wood-chew-finishing-bench.jpg','Row of workers shaping and finishing coffee wood chew sticks at benches','Shaping and surface finishing on our own line in the Central Highlands.'),('pallet-stack-inspection.jpg','Staff inspecting a stack of palletised export cartons','Buyer-arranged inspection is welcome — please arrange in advance so the line is running.'),('hemp-ball-and-loop-toy-set.jpg','Hemp rope balls with a double-ended loop toy','Hemp balls and a loop toy — specify each construction on its own line.'),('coffee-wood-chews-three-in-vacuum-pack.jpg','Three coffee wood chews sealed in a clear vacuum bag','Vacuum-packed at our warehouse: the bag keeps the wood at its packing moisture until it is opened.')])

add("wholesale-coconut-fiber-cat-toys-supplier","Sourcing & trade",
    "Sourcing Coconut-Fiber Cat Toys for Wholesale",
    "Build a wholesale coconut-fiber cat toy assortment with clear size specifications, sample checks, pack counts and private-label requirements.",
    answer("<strong>Short answer:</strong> to buy coconut-fiber cat toys wholesale, specify the ball (diameter, finished weight, full "
           "construction), then the saleable unit (single, two-pack or mixed box), then the carton. With VietPaw, selected standard lines start "
           "from 50 pcs, private-label tags and boxes from 500 pcs per SKU, samples are free (3, you cover the courier), and stock-packed goods "
           "ship in 5–7 days."),
    [
    ("Key terms",
      p("<dfn>Coconut-fiber cat ball</dfn>: a small, light ball of wound coir for batting and chasing — specified for cats, not scaled down from a "
        "dog ball.")
      + p("<dfn>Saleable unit</dfn>: what one line on the invoice means — one ball with a tag, a two-pack, or a boxed set. The same definition "
          "should appear in the quotation, packing list and receiving instructions.")
      + p("<dfn>Assortment</dfn>: a fixed mix of sizes or products in one pack or carton. It needs its contents written down, not described as "
          "“mixed”.")),

    ("Pack options compared",
      spec_table(["Pack option","Suits","Barcode","What to confirm"],[
        ("Single ball with hang tag","Pet shops, gift displays","One per ball","Tag size, attachment, readable instructions"),
        ("Two-pack or three-pack","Marketplace listings","One per pack","Pack contents and sizes"),
        ("Boxed assortment","Gift and seasonal ranges","One per box","Exact contents per box"),
        ("Bulk, unbranded","Wholesalers who repack","Per carton","Units per carton and carton marks"),
      ], caption="Printed tags, labels and boxes start at 500 pcs per SKU.")),

    ("Sourcing coconut-fiber cat toys, step by step",
      steps([
        ("Specify the ball","Diameter, finished weight, outer fibre, any core, binding thread and decoration.","A product both sides can measure."),
        ("Sample the sizes you will sell","Up to 3 free samples; you cover the courier.","Winding, shape and loose ends compared across the set."),
        ("Define the saleable unit","Single, multi-pack or boxed set, with barcode placement.","One meaning for “one unit” on every document."),
        ("Approve pack and artwork","Label size, attachment, barcode and play instructions.","A pack that works on the shelf and at receiving."),
        ("Confirm carton data","Units per carton, outer dimensions and gross weight.","Freight quotes based on packed volume, not a loose ball."),
        ("Place the trial order","Track sales and returns by SKU.","A reorder based on what customers actually bought."),
      ])),

    ("VietPaw order facts",
      spec_table(["Item","Detail"],[
        ("Minimum","Selected standard lines from 50 pcs; per-size minimum in the quote"),
        ("Private label","Hang tags, labels and printed boxes from 500 pcs per SKU"),
        ("Samples","3 free; buyer covers courier; dispatched within 1 working day once confirmed"),
        ("Production","5–7 days stock packaging; 60–80 days with your own label or box"),
        ("Export master carton","51 × 31 × 39 cm (0.062 m³); 30 cartons per pallet"),
        ("Sea transit","30–35 days port to port from Cat Lai to the EU or the US"),
        ("Payment","30% deposit stock / 50% branded; balance against documents"),
      ])),

    ("Look at the carton while there is still time to change it",
      p("Fibre balls can take more space than their weight suggests, especially in rigid display packaging. Your forwarder needs the packed data, "
        "not the dimensions of one loose ball.")
      + p("Agree clean, dry packing and storage with the supplier; musty units are rejected at inspection. At receiving, inspect product and "
          "packaging together and photograph any carton damage with its marks, so a transport issue can be told apart from a production "
          "defect.")),

    ("Use the first order to establish the reorder",
      p("A sensible trial is large enough to test the chosen sizes and presentation, but narrow enough to review carefully. If customers favour "
        "one size or a pack creates confusion, revise that detail before expanding the range.")
      + p("When requesting a quote, include your destination, quantity per size and preferred pack.")),
    ],
    ("VietPaw coconut-fiber cat ball specifications","/products/coconut-fiber-cat-ball/"),
    related=[("Coconut-fiber material guide","/guides/what-is-coconut-fiber-pet-toys/"),("Buying natural cat toys","/guides/non-toxic-cat-toys-wholesale-buying-guide/"),
             ("MOQ, pricing and lead times","/guides/pet-toy-moq-fob-pricing-lead-times/"),("Wholesale supply","/services/wholesale-pet-products/")],
    image="vietpaw-coconut-fiber-balls.jpg",
    faqs=[
      ("What is the minimum order for coconut-fiber cat toys?",
       "Selected standard lines start from 50 pcs; the per-size minimum is confirmed in the quote. Printed tags, labels and boxes start at "
       "500 pcs per SKU."),
      ("Can I get samples first?",
       "Yes — 3 free samples; you cover the courier. Standard samples are dispatched within 1 working day once confirmed."),
      ("Can I sell them under my own brand?",
       "Yes. Private-label hang tags, labels and printed boxes start at 500 pcs per SKU and take 60–80 days, mostly artwork approval and "
       "printing."),
      ("How long does delivery take?",
       "5–7 days to produce stock-packed goods, then 30–35 days by sea from Cat Lai to the EU or the US."),
      ("Is a cat ball just a small dog ball?",
       "No. Specify the cat version separately — diameter, weight and any attachment — and keep its instructions separate from dog toys."),
    ],
    figures=[('cat-playing-with-loofah-shape.jpg','Grey cat reaching for a loofah play shape on a table','Write a cat specification, not a scaled-down dog one.'),('vietpaw-loofah-play-shapes.png','Loofah cat play shapes arranged in a basket','Each shape is measured separately — one size range does not cover the collection.'),('coconut-fiber-ball-top-view.jpg','Wound coconut fiber ball seen from above on a marble surface','A wound coir ball: the texture is the product — specify diameter and finished weight with it.'),('catalogue-coconut-fiber-balls-s-m-l.jpg','Coconut fiber balls in sizes S, M and L','Catalogue image: coconut fiber balls, S, M and L.')])

add("private-label-oem-eco-pet-toys-explained","Sourcing & trade",
    "Private Label, OEM or ODM? Define the Work First",
    "Choose a practical development route for natural pet toys, with clear responsibilities for design, samples, branding and production approval.",
    answer("<strong>Short answer:</strong> private label puts your brand on an existing product; OEM means we manufacture to your design "
           "or a changed construction; ODM means we develop a new design with you. The more of the product you change, the more "
           "development, sampling and time the project needs. At VietPaw, engraving starts at 50 pcs, private-label packaging at 500 pcs "
           "per SKU, and branded orders take 60–80 days in production."),
    [
    ("Private label, OEM, ODM and white label defined",
      p("<dfn>Private label</dfn> is an existing, proven product sold under your brand. The construction stays the same; the logo, labels "
        "and retail packaging are yours.")
      + p("<dfn>OEM</dfn> (original equipment manufacturing) means the factory produces a product to the buyer’s design or specification — "
          "including a change to an existing construction, such as a new rope, join or dimension.")
      + p("<dfn>ODM</dfn> (original design manufacturing) means the factory designs and develops the product with you, from concept to "
          "approved prototype, and then manufactures it.")
      + p("<dfn>White label</dfn> usually means an unbranded standard product that several resellers can buy and label. Suppliers use it "
          "loosely, sometimes as a synonym for private label, so ask what exclusivity — if any — is included.")
      + p("Two suppliers can use OEM to describe very different amounts of work. Describe what you want changed before comparing prices; "
          "the work matters more than the acronym.")),

    ("Private label vs OEM vs ODM compared",
      spec_table(["","Private label","OEM","ODM"],[
        ("What changes","Branding and packaging only","Construction, materials or dimensions to your specification","The whole product, developed with our team"),
        ("Who provides the design","Existing VietPaw design","You","Developed jointly"),
        ("Design rights","No exclusivity on a standard design unless agreed","Your specification; agree ownership in writing","Agree ownership and usage rights before development"),
        ("Starting quantity at VietPaw","Engraving from 50 pcs; printed packaging from 500 pcs per SKU","Quoted per project","Quoted per project"),
        ("Samples","3 free standard samples; buyer covers courier","Prototype, quoted separately","Prototype rounds, quoted separately"),
        ("Production time","60–80 days with your label, box or engraving","Project schedule after prototype approval","Project schedule after prototype approval"),
        ("Best for","A fast, low-risk brand launch","Differentiating a proven format","A new product line"),
      ], caption="VietPaw planning figures; development charges and schedules are itemised in your quotation.")),

    ("An existing product with your branding",
      p("Private label is often the most direct route when the existing construction already fits your range. The project centers on the "
        "selected SKU, logo placement, labels and retail packaging.")
      + spec_table(["Branding option","Starting quantity","Note"],[
        ("Laser engraving","50 pcs","Burned into suitable coffee wood surfaces — nothing to peel off during chewing"),
        ("Hang tag or label","500 pcs per SKU","Printed to your artwork"),
        ("Printed box","500 pcs per SKU","Separate minimum from the product inside it"),
        ("Bulk bag, individual pack, kraft box","Quoted with the order","Standard options without custom print"),
      ])
      + p("Approve the branding on a physical sample. An engraving can look different across natural grain, and a logo that is clear on a "
          "screen may be too small on a narrow stick.")),

    ("A change to the construction",
      p("Adding a rope, changing a join or altering dimensions creates more work than a packaging update. Our production team needs to "
        "review feasibility, materials and the way the assembled product will be inspected. A sample of the old design does not approve the "
        "new one.")
      + p("Put the intended pet and play type in the brief. A change that looks attractive in a photograph can affect the handle opening, "
          "loose ends or attachment security. Agree the revised specification and any relevant assessment before committing to bulk "
          "production.")),

    ("A design developed with our production team",
      p("For a new concept, decide who provides the initial design, who develops prototypes and who approves the final construction. Record "
        "development charges, tooling if applicable, revision rounds and the ownership or usage rights you have agreed. Do not assume that a "
        "private-label order creates exclusive rights to a standard design.")
      + p("Allow separate time for development and production. A quote for making approved goods does not necessarily include the time spent "
          "refining a concept or revising artwork.")),

    ("The approval gates, step by step",
      steps([
        ("Agree the brief","Route (private label, OEM or ODM), intended pet and play type, market, target quantity and packaging.","A quote that separates development, branding, packaging and production."),
        ("Approve the sample or prototype","Standard samples for private label; a prototype for OEM or ODM.","Dimensions, components and appearance recorded against a reference."),
        ("Approve the artwork","Logo, warnings, barcode and pack contents checked on a proof.","Print files locked; changes after this point restart the clock."),
        ("Sign off the specification","Component list, tolerances, acceptable natural variation and pack count.","One document both sides inspect against."),
        ("Release production","50% deposit on a branded order.","Production scheduled; 60–80 days for private label, a project schedule for OEM or ODM."),
        ("Inspect and ship","Pre-shipment check against the approved reference and export documents.","Balance paid against shipping documents."),
      ])
      + p("VietPaw offers product customization, engraving and packaging support. Ask for a quotation that separates them — you will have a "
          "clearer budget and fewer surprises when the design changes.")),
    ],
    ("Discuss OEM and ODM pet toy development","/services/oem-odm-pet-toy-manufacturing/"),
    related=[("Private-label services","/services/private-label-pet-toys/"),("Sample and order process","/how-to-order/"),
             ("MOQ, pricing and lead times","/guides/pet-toy-moq-fob-pricing-lead-times/")],
    sources=[("VietPaw private-label and packaging options","/services/private-label-pet-toys/")],
    image="process-laser-engraving.jpg",
    faqs=[
      ("What is the difference between private label and OEM?",
       "Private label keeps the existing product and changes only the branding and packaging. OEM changes the product itself — its construction, "
       "materials or dimensions — to your specification, so it needs a prototype and a new approval."),
      ("What is the minimum order for private-label pet toys?",
       "At VietPaw, laser engraving starts at 50 pcs. Private-label runs and printed hang tags, labels or boxes start at 500 pcs per SKU."),
      ("Can I add my logo without printed packaging?",
       "Yes. Laser engraving on suitable coffee wood surfaces starts at 50 pcs and can ship in a standard pack; printed packaging is a separate "
       "decision with its own 500-pc minimum."),
      ("Do I own the design?",
       "For a standard product sold under private label, no exclusivity is created unless you agree it. For OEM and ODM work, agree ownership and "
       "usage rights in writing before development starts."),
      ("How long does a private-label order take?",
       "60–80 days of production when the order carries your own label, printed box or engraving, most of it artwork approval and tooling. Add "
       "30–35 days sea transit to the EU or the US. OEM and ODM projects get their own schedule after prototype approval."),
    ],
    figures=[('laser-engraving-coffee-wood-chew.jpg','Laser engraving head marking a logo onto a coffee wood chew stick','Engraving is burned into the wood — nothing to peel off during chewing. From 50 pcs.'),('bagged-chews-with-desiccant.jpg','Bagged coffee wood chews with a desiccant sachet ready for packing','Printed tags, labels and boxes start at 500 pcs per SKU — a separate minimum from engraving.'),('hemp-rope-ball-vacuum-packed-size-l.jpg','Hemp rope ball vacuum-packed with a size L label','Size label on the pack: the same reference should appear on the quote and the packing list.')])

add("pet-toy-moq-fob-pricing-lead-times","Sourcing & trade",
    "Pet Toy MOQ, FOB Pricing and Lead Times: Reading the Quote",
    "Understand pet toy minimum orders, packaging costs, FOB and FCA delivery terms, and the difference between production time and arrival date.",
    answer("<strong>Short answer:</strong> at VietPaw, selected standard products start at 50 pcs per SKU, laser engraving at 50 pcs and "
           "private-label packaging at 500 pcs per SKU. Stock-packed orders are produced in 5–7 days; orders with your own label, "
           "printed box or engraving take 60–80 days. An FOB price covers the goods loaded on board at a named port — sea transit "
           "to the EU or the US adds another 30–35 days."),
    [
    ("What MOQ, FOB and lead time mean",
      p("<dfn>MOQ</dfn> (minimum order quantity) is the smallest quantity a supplier will produce or pack under one set of terms. "
        "A single quotation can contain several minimums at once — one for the product, one for engraving, one for printed packaging.")
      + p("<dfn>FOB</dfn> (Free On Board) is an Incoterms® 2020 rule for sea freight. The seller clears the goods for export and delivers "
          "them on board the vessel at a named port of shipment; from that point, cost and risk pass to the buyer. An FOB price is not a "
          "delivered price.")
      + p("<dfn>FCA</dfn> (Free Carrier) is the rule for handing goods to the buyer’s carrier at a named place, before they are loaded on a "
          "vessel. It works for any transport mode, including air.")
      + p("<dfn>Lead time</dfn> is the production window after every approval has been given. It is not an arrival date: sample approval, "
          "artwork, transit and customs clearance sit either side of it.")
      + p("<dfn>Landed cost</dfn> is what one saleable unit costs once it is in your warehouse: goods, packaging, freight, insurance, "
          "duties and handling, divided by the units you actually receive.")),

    ("VietPaw minimums, timings and shipping data",
      spec_table(["Item","Figure","What it applies to"],[
        ("Standard product MOQ","50 pcs per SKU","Selected standard products; size and pack minimums confirmed in the quote"),
        ("Laser engraving","From 50 pcs","Suitable coffee wood surfaces; separate from the packaging minimum"),
        ("Private-label run","From 500 pcs","Your label or brand on an existing product"),
        ("Printed hang tags, labels, boxes","From 500 pcs per SKU","Custom printed packaging"),
        ("Trial Box / Starting Box","100 pcs / 500 pcs","Coffee wood chews: usual first steps above the 50-pc minimum"),
        ("Samples","3 free; buyer covers courier","Standard samples dispatched within 1 working day once confirmed"),
        ("Production, stock packaging","5–7 days","Standard sizes held in our warehouse"),
        ("Production, your own branding","60–80 days","Own label, printed box or engraving; most of it is artwork approval and tooling"),
        ("Sea transit","30–35 days port to port","From Cat Lai, Ho Chi Minh City, to the EU or the US"),
        ("Deposit","30% stock / 50% branded","Balance against shipping documents; air freight paid in full before handover"),
        ("Export master carton","51 × 31 × 39 cm (0.062 m³)","30 cartons per pallet"),
        ("Container load","429 cartons (20 ft) / 850 (40 ft)","Planning reference; confirm for your packed SKU"),
        ("Production capacity","100,000 pcs a month","Across our three factories; your slot is confirmed in the quotation"),
      ], caption="Planning figures published by VietPaw. The quotation for your order governs.")
      + p("An engraving-only order and a fully branded retail pack therefore need different budgets. Ask whether the minimum "
          "applies per SKU, per size, per artwork or per order. If the packaging minimum is higher than the product quantity, agree who "
          "pays for the balance, who stores it and whether it can be used on the next order.")),

    ("EXW, FCA, FOB, CIF, DAP or DDP: where the price stops",
      spec_table(["Incoterm","Delivery and risk pass to you","Main freight booked by","Transport"],[
        ("EXW","At our premises, before export clearance","Buyer","Any"),
        ("FCA","When handed to your carrier at the named place, export-cleared","Buyer","Any, including air"),
        ("FOB","On board the vessel at the named port of shipment","Buyer","Sea only"),
        ("CIF","On board at the port of shipment (seller pays freight and minimum insurance to the destination port)","Seller","Sea only"),
        ("DAP","At the named destination, ready for unloading; you clear import and pay duties","Seller","Any"),
        ("DDP","At the named destination, cleared for import with duties paid","Seller","Any"),
      ], caption="Incoterms® 2020 summary. Always name the place or port with the rule, for example “FOB Cat Lai”.")
      + p("VietPaw quotes EXW, FCA, FOB, CIF, DAP and DDP. For an air shipment, FCA is the correct rule — FOB is not. For containers handed "
          "to a carrier at a terminal before loading, ICC guidance also points buyers toward FCA. DDP suits a first-time importer who would "
          "rather not handle customs, though import VAT is usually not recoverable that way; DAP suits a VAT-registered buyer.")
      + p("Incoterms decide delivery, cost and risk. They do not replace the product specification, the payment agreement or the "
          "inspection plan.")),

    ("Compare the complete saleable unit",
      p("Separate the toy, customization, retail pack, master carton and any agreed testing or inspection charges. Confirm the currency, "
        "quotation validity and payment schedule. A one-off artwork or development charge should not disappear inside a unit price that "
        "you later expect on reorders.")
      + p("A simple landed-cost calculation for an FOB quote looks like this:")
      + ul(["Goods and packaging at the FOB price",
            "+ sea freight and insurance from the named port",
            "+ import duty and taxes on the declared value",
            "+ destination port, customs broker and delivery to your warehouse",
            "÷ the number of saleable units received"])
      + p("Use real forwarder and broker figures for the freight and duty lines. A supplier’s estimate of either is not a product price.")),

    ("From enquiry to stock on the shelf: the timeline",
      steps([
        ("Send the brief","Product references, sizes, quantity per SKU, destination, sales channel and branding.","An itemised quote that separates product, branding, packaging and freight."),
        ("Approve samples","Select up to 3 free samples; you cover the courier. Standard samples leave within 1 working day of confirmation.","A physical reference with recorded dimensions."),
        ("Approve artwork (branded orders only)","Logo, warnings, barcode and pack contents checked on a proof.","The stage that takes most of the 60–80-day window — start it early."),
        ("Pay the deposit and release production","30% on a stock order, 50% on a branded order.","The production clock starts: 5–7 days stock, 60–80 days branded."),
        ("Inspect and document","Final check, packing, carton marks and the seven export documents.","Balance paid against the shipping documents."),
        ("Ship and clear","Sea transit 30–35 days port to port, then import clearance and inland delivery.","Stock received, counted and inspected against the approved sample."),
      ])
      + spec_table(["Order type","Production","Sea transit","Planning total, factory to destination port"],[
        ("Stock packaging","5–7 days","30–35 days","About 35–42 days"),
        ("Your label, printed box or engraving","60–80 days","30–35 days","About 90–115 days"),
      ], caption="Excludes sample courier time, vessel booking, customs clearance and inland delivery.")
      + p("Work backwards from the date stock must be on sale, and leave time to receive and inspect it. Do not apply the stock window "
          "to a private-label launch.")),

    ("Questions that make two quotes comparable",
      ul(["Is the minimum per SKU, per size, per artwork or per order?",
          "Which Incoterm, with which named place or port, and which Incoterms edition?",
          "Which approval starts the production clock?",
          "What is included in the unit price — pack, insert, barcode, master carton?",
          "Which charges are one-off (artwork, tooling, development) and which recur?",
          "How long is the quotation valid, and in which currency?"])
      + p("Two quotes that answer the same six questions can be compared. Two quotes that do not are usually describing different orders.")),
    ],
    ("Prepare a product and pricing enquiry","/request-a-quote/"),
    related=[("Wholesale service","/services/wholesale-pet-products/"),("First-order planning","/guides/sourcing-eco-pet-toys-vietnam/"),
             ("Private label, OEM or ODM?","/guides/private-label-oem-eco-pet-toys-explained/"),("Vietnam or China?","/guides/sourcing-pet-toys-vietnam-vs-china/")],
    sources=[("VietPaw order minimums and lead times","/how-to-order/"),("ICC guidance: FCA or FOB?","https://academy.iccwbo.org/incoterms/article/incoterms-2020-fca-or-fob/")],
    image="container-wall-of-cartons.jpg",
    faqs=[
      ("What is the minimum order for VietPaw pet toys?",
       "Selected standard products start at 50 pcs per SKU. Laser engraving starts at 50 pcs; private-label runs and printed hang tags, labels "
       "or boxes start at 500 pcs per SKU. For coffee wood chews, the usual first steps are a Trial Box of 100 pcs or a Starting Box of 500 pcs."),
      ("Is the FOB price what I will pay in total?",
       "No. FOB covers the goods, export clearance and loading on board at the named port. Sea freight, insurance, import duty and taxes, "
       "destination charges and inland delivery are added on your side."),
      ("Should I buy FOB or FCA?",
       "FOB is for sea freight when the goods are loaded on board at the port. For air freight, or when your forwarder collects a container "
       "before it is loaded, FCA is the more accurate rule. Agree the choice with your forwarder."),
      ("Why does a private-label order take 60–80 days when stock takes 5–7?",
       "Stock sizes are already made and held in our warehouse. With your own label, printed box or engraving, most of the time goes on artwork "
       "approval, printing and tooling rather than on making the product."),
      ("When does the lead time start?",
       "After the sample, artwork and order are approved and the deposit is received. Production time is not an arrival date; add 30–35 days "
       "sea transit plus clearance."),
      ("What are the payment terms?",
       "A 30% deposit on a stock order or 50% on a branded order, with the balance against shipping documents. Air shipments are paid in full "
       "before the goods are handed over at the airport."),
    ],
    figures=[('container-wall-of-cartons.jpg','A full wall of export cartons loaded and netted inside a shipping container','429 cartons in a 20 ft, 850 in a 40 ft. Pack format changes the count before it changes the price.'),('warehouse-inspection-clipboard.jpg','Warehouse staff checking stock against a document','Stock sizes ship in 5–7 days; printed packaging is the part that takes 60–80.'),('coffee-wood-chews-pack-with-desiccant.jpg','Coffee wood chews packed with a labelled desiccant sachet','Moisture protection is part of the pack specification — agree the sachet material as well as the bag.'),('hemp-rope-ball-packed-size-m.jpg','Hemp rope ball vacuum-packed with a size M label','Packed size M ball — pack format changes carton counts before it changes the price.')])

add("pet-toy-safety-compliance-cpsia-reach","Compliance & risk",
    "CPSIA, REACH and Pet Toys: Ask the Right Compliance Question",
    "How pet toy buyers should approach CPSIA and REACH discussions, including product classification, material scope and report relevance.",
    answer("<strong>Short answer:</strong> CPSIA is the US law for <em>children’s</em> products (for children 12 and under), so a toy designed "
           "and marketed only for pets is not usually a children’s product — though marketing and labelling can change that. REACH is the EU "
           "chemicals regulation and applies to articles of every kind, pet toys included: restricted substances and Candidate List (SVHC) "
           "substances above 0.1% still matter. In the EU, pet toys also fall under the General Product Safety Regulation. The right question "
           "is which requirement applies to this product in this market."),
    [
    ("CPSIA, REACH and GPSR in one paragraph each",
      p("<dfn>CPSIA</dfn> (Consumer Product Safety Improvement Act, US, 2008) sets requirements for children’s products — including limits on "
        "lead and certain phthalates, third-party testing and a Children’s Product Certificate. Whether a product is a children’s product depends "
        "on who it is designed and marketed for.")
      + p("<dfn>REACH</dfn> (Regulation (EC) No 1907/2006) controls chemicals in the EU, including substances in imported articles. Annex XVII "
          "restrictions apply where relevant, and a Substance of Very High Concern on the Candidate List above 0.1% by weight triggers "
          "information duties to customers.")
      + p("<dfn>GPSR</dfn> (General Product Safety Regulation (EU) 2023/988, applying since 13 December 2024) covers consumer products without "
          "their own sector rules — pet toys included. It requires products to be safe, traceable and, when placed on the EU market, linked to "
          "a responsible economic operator in the EU.")),

    ("Which rule applies to a pet toy?",
      spec_table(["Rule","Market","Applies to a pet toy?","What to ask for"],[
        ("CPSIA","United States","Usually not, unless it is designed or marketed for children","An applicability review of the product and its marketing"),
        ("California Proposition 65","California","Yes, if listed chemicals are present above safe-harbour levels","Whether a warning is needed for the composition"),
        ("REACH Annex XVII","European Union","Yes — restrictions apply to articles","Which restrictions are relevant to the materials"),
        ("REACH Candidate List (SVHC)","European Union","Yes — duties above 0.1% w/w in an article","A declaration for the components"),
        ("GPSR","European Union","Yes — general consumer product safety","Risk assessment, traceability and the EU responsible person"),
      ], caption="Orientation only. The importer and qualified advisers confirm the current position for each product and market.")),

    ("Getting to the right compliance answer, step by step",
      steps([
        ("Describe the finished product","Intended pet, materials, components, colours, coatings, pack and marketing text.","A reviewer can classify the product correctly."),
        ("Name the markets and channels","Country, retailer or marketplace requirements.","The list of rules that actually apply."),
        ("Ask for an applicability review","Which requirements apply, and which do not, for this construction.","No children’s-toy statement copied onto a pet product."),
        ("Scope any testing","Substances or properties, method, sample and pass criteria.","A report that answers a defined question."),
        ("Link evidence to the order","Match the report to the sample and bill of materials.","A file that survives a component change."),
        ("Agree responsibilities","Who decides, who tests, who pays, what happens if a result fails.","No shipment waiting on an open question."),
      ])),

    ("What VietPaw provides",
      spec_table(["Item","Detail"],[
        ("Component list","Per approved sample, on request"),
        ("Coffee wood composition","One untreated material — no glue, coating, preservative or colouring"),
        ("Laboratory testing","Arranged separately on request"),
        ("Export documents","Seven with every order, including Certificate of Origin, phytosanitary and fumigation certificates"),
        ("Not issued","Veterinary certificates (not an animal by-product) and FSC certification (coffee is an agricultural crop)"),
      ])
      + p("Shipment documents such as origin or treatment certificates serve different purposes and are not substitutes for a product "
          "assessment.")),

    ("Connect the evidence to the order",
      p("Check the report’s product identification against the sample and bill of materials you approved. If the toy contains several components, "
        "ask which were included. A change in colour, adhesive, rope or supplier may need a fresh scope review even when the item looks the "
        "same.")
      + p("Retailers may request particular test methods as a purchasing condition. Keep that commercial request separate from the legal "
          "classification, and keep the reviewed evidence with the SKU and artwork version.")),
    ],
    ("VietPaw testing and export-document information","/certifications/"),
    related=[("Planning a safety assessment","/guides/pet-toy-safety-testing-requirements/"),("How to vet a supplier","/guides/how-to-vet-an-eco-pet-toy-supplier/"),
             ("Quality-control workflow","/quality-control/")],
    sources=[("CPSC toy-safety business guidance",CPSC),("ECHA: REACH restrictions",ECHA),
             ("EU General Product Safety Regulation (EU) 2023/988","https://eur-lex.europa.eu/eli/reg/2023/988/oj")],
    faqs=[
      ("Do pet toys need CPSIA testing?",
       "Usually not. CPSIA covers children’s products. A toy designed and marketed only for pets is not normally a children’s product, but "
       "marketing that appeals to children can change the assessment."),
      ("Does REACH apply to pet toys?",
       "Yes. REACH applies to articles sold in the EU, including pet toys. Restricted substances and Candidate List substances above 0.1% by "
       "weight are the usual questions."),
      ("What is GPSR and does it cover pet toys?",
       "The EU General Product Safety Regulation, applying since 13 December 2024. It covers consumer products without their own sector rules, "
       "including pet toys, and requires a responsible economic operator in the EU."),
      ("Is there a “REACH certificate”?",
       "Not as a universal approval. There are test reports and declarations for defined substances and samples; check what each one covers."),
      ("Does VietPaw provide test reports?",
       "Laboratory testing is arranged separately on request, scoped to your product and market."),
    ],
    figures=[('inspection-documents-at-pallets.jpg','Two staff reviewing inspection documents beside stacked pallets','Compliance is decided per SKU and per destination, not per supplier.'),('export-container-exterior.jpg','Worker beside a green export container being loaded at a warehouse','Customs and marketplace checks are separate gates with separate paperwork.'),('hemp-rope-balls-three-sizes.jpg','Three hemp rope balls in small, medium and large','Three hemp ball sizes: measure each against the approved sample.')])

add("sourcing-pet-toys-vietnam-vs-china","Sourcing & trade",
    "Vietnam or China for Pet Toys? Compare the Order, Not the Flag",
    "A practical sourcing comparison based on product fit, landed cost, capacity, origin requirements and repeat-order performance.",
    answer("<strong>Short answer:</strong> neither country is automatically cheaper or better. For natural-material pet toys — coffee wood, "
           "coconut fiber, hemp and loofah — Vietnam offers raw materials close to production and, for EU buyers, preferential duty under "
           "the EU–Vietnam Free Trade Agreement when the goods qualify and carry valid proof of origin. China offers deeper supply chains for "
           "synthetic, plush and multi-material toys. Decide by comparing two quotes for the same specification on landed cost, lead time "
           "and repeatability."),
    [
    ("What a Vietnam-or-China comparison actually measures",
      p("A country-level cost comparison can point a buyer in a direction, but it cannot select a supplier. Two factories in the same country "
        "may have very different skills, packaging options and production schedules. The useful comparison is between suppliers quoting the "
        "same finished order.")
      + p("<dfn>Landed cost</dfn> is the full cost of one saleable unit in your warehouse: goods, packaging, freight, insurance, duties and "
          "handling. <dfn>Country of origin</dfn> is where the goods were wholly obtained or last substantially transformed — not where they "
          "were packed or shipped from. Both depend on the product, not the flag on the quote.")),

    ("Vietnam vs China: factor-by-factor comparison",
      spec_table(["Factor","Vietnam (natural materials)","China","How to compare fairly"],[
        ("Material base","Coffee wood from the Central Highlands; coconut and loofah grown in the country","Broad supply of synthetic, rubber, plush and rope components","Ask where the main material is grown or made"),
        ("Product focus","Natural-material chews and toys","Wide range, from basic to highly engineered","Match the supplier’s strength to your construction"),
        ("EU import duty","EU–Vietnam FTA (in force since 1 August 2020): preferential rates for originating goods with valid proof of origin","Standard EU rates; no EU–China free-trade agreement","Broker checks the HS code and rate for your actual product"),
        ("US import duty","Tariff treatment has changed repeatedly since 2025","Tariff treatment has changed repeatedly since 2025","Check the current rate for both origins at the time of order"),
        ("Origin rules","Goods must be wholly obtained or substantially transformed in Vietnam","Same principle","Transshipped or merely repacked goods do not change origin"),
        ("Minimum order","VietPaw: from 50 pcs per SKU on selected standard products","Varies widely by supplier","Compare the same quantity and pack"),
        ("Lead time","VietPaw: 5–7 days stock, 60–80 days branded; 30–35 days sea to the EU or US","Varies by supplier and port","Compare approved sample to stock on sale, stage by stage"),
      ], caption="Duty rates and trade measures change. Confirm them for the actual goods with your customs broker before ordering.")),

    ("Build the landed-cost comparison line by line",
      table(["Cost or condition","Comparison basis"],[
        ("Product and customization","Same SKU, quantity, components and approved finish"),
        ("Retail and transit packaging","Same saleable unit and carton requirements"),
        ("Testing and inspection","Same agreed scope and release stage"),
        ("Transport and handling","Packed dimensions, weight, route and named delivery point"),
        ("Import charges","Current classification, origin and destination-specific assessment")])
      + p("A trade agreement is not a blanket zero-duty promise for everything shipped from a country. Preferential rates apply to goods "
          "that meet the rules of origin and are covered by the right proof — for VietPaw shipments to the EU, a EUR.1 certificate under "
          "the EVFTA. The European Commission’s Access2Markets service lists tariffs, origin rules and product requirements by HS code.")),

    ("How to run a fair two-country comparison",
      steps([
        ("Write one specification","Dimensions, components, quantity per SKU, pack and inspection requirements.","Both suppliers price the same product."),
        ("Request itemised quotes on the same Incoterm","For example, both FOB at a named port, or both DAP to your warehouse.","Freight is not hidden in one quote and missing from the other."),
        ("Compare physical samples side by side","Measure, weigh and check the finish and construction against the specification.","Differences in material or work are visible before price is discussed."),
        ("Have your broker assess duty and origin","HS code, origin and any preference for each quote.","Duty lines based on the real goods, not a country average."),
        ("Map the calendar","Sample, artwork, production, transit and receiving for each supplier.","A realistic date that stock can be on sale."),
        ("Start with a trial order","A small run from the preferred source before committing volume.","Receiving data that confirms — or corrects — the paper comparison."),
      ])),

    ("Compare the calendar and the communication",
      p("Measure the full path from approved sample to stock available for sale. Include development, artwork, testing, production, transport "
        "and receiving. A shorter production estimate may not produce an earlier arrival if another stage remains unresolved.")
      + p("Also assess how the supplier responds to a precise technical question. Can it explain a size tolerance, identify a packaging change "
          "and provide an updated drawing or sample? Clear answers during sampling are useful evidence of how a reorder may be managed.")),

    ("Make a second source genuinely usable",
      p("If diversification is the objective, qualify the alternative product rather than only adding another supplier name to a spreadsheet. "
        "Natural materials can differ in appearance and handling. Retest the retail presentation, label information and receiving specification "
        "for the alternative source.")
      + p("Choose on the basis of product fit, total cost and repeatability. Neither Vietnam nor China is automatically the better answer for "
          "every construction, order size or sales channel.")),
    ],
    ("Review VietPaw's Vietnam manufacturing capabilities","/pet-toys-manufacturer-vietnam/"),
    related=[("Supplier qualification","/guides/how-to-vet-an-eco-pet-toy-supplier/"),("Pricing and delivery terms","/guides/pet-toy-moq-fob-pricing-lead-times/"),
             ("First order from Vietnam","/guides/sourcing-eco-pet-toys-vietnam/")],
    sources=[("European Commission: importing into the EU","https://policy.trade.ec.europa.eu/help-exporters-and-importers/importing-eu_en"),
             ("Access2Markets: tariffs and origin rules","https://trade.ec.europa.eu/access-to-markets/en/home")],
    image="pallet-stack-inspection.jpg",
    faqs=[
      ("Is it cheaper to source pet toys from Vietnam or China?",
       "It depends on the product. Compare two itemised quotes for the same specification, on the same Incoterm, and add freight and duty for "
       "each. For natural-material toys, Vietnam’s local raw materials often matter more than the headline labour cost."),
      ("Do pet toys from Vietnam pay lower EU import duty?",
       "They can. Under the EU–Vietnam Free Trade Agreement, goods that meet the rules of origin and carry valid proof of origin, such as a EUR.1 "
       "certificate, can qualify for preferential rates. Your broker confirms the rate for the actual HS code."),
      ("What about US import duties?",
       "US tariff treatment of goods from both Vietnam and China has changed several times since 2025. Check the current rate for your product "
       "with a customs broker at the time of order rather than relying on an older comparison."),
      ("Can a Chinese product be shipped through Vietnam to change its origin?",
       "No. Origin follows where goods were wholly obtained or substantially transformed. Transshipped or merely repacked goods keep their "
       "original origin, and mis-declaring it is a customs violation."),
      ("Does VietPaw make synthetic or plush toys?",
       "No. VietPaw manufactures four natural-material collections — coffee wood, coconut fiber, hemp and loofah — in its own three factories "
       "in Vietnam."),
    ],
    figures=[('two-inspectors-container-check.jpg','Two staff checking stacked export cartons inside a container','Ask the same verification questions of every origin: moisture, marks, stuffing, documents.'),('stacking-cartons-in-container.jpg','Worker stacking cartons inside a shipping container','Consolidation and container choice move landed cost more than unit price often does.'),('coconut-fiber-rope-toy-knotted.jpg','Coconut fiber rope toy with a knot at each end','Coconut fiber rope with two knots, for supervised tug and carry.'),('catalogue-hemp-loop-toy-lifestyle.jpg','Hemp rope loop toy with a knotted ball','Catalogue image: hemp loop toy for tug play.')])

add("pet-toy-safety-testing-requirements","Compliance & risk",
    "Pet Toy Safety Testing: Build a Product-Specific Plan",
    "Prepare a useful pet toy assessment brief and distinguish laboratory testing, factory inspection and shipment documentation.",
    answer("<strong>Short answer:</strong> there is no single mandatory safety test for pet toys in the US or the EU. Build a plan for your "
           "product instead: describe the finished toy, list the markets and retailer requirements, then choose the checks that answer real "
           "questions — physical construction, chemical content for the materials used, and factory inspection of the production lot. Keep "
           "laboratory reports, inspection records and shipment documents separate; each answers a different question."),
    [
    ("Three kinds of evidence",
      p("<dfn>Laboratory testing</dfn> measures defined substances or properties in a named sample using a stated method — for example heavy "
        "metals in a dye or phthalates in a plastic part.")
      + p("<dfn>Physical-construction review</dfn> looks at how the toy could come apart: edges, loose parts, knots, seams and attachments.")
      + p("<dfn>Factory inspection</dfn> checks whether a production lot matches the approved specification — dimensions, finish, moisture, pack "
          "and carton marks. <dfn>Shipment documents</dfn>, such as phytosanitary or fumigation certificates, cover the movement of goods, not "
          "product safety.")),

    ("Checks buyers commonly request",
      spec_table(["Check","When it is relevant","Evidence"],[
        ("Heavy metals (e.g. lead, cadmium)","Coloured, coated or printed parts","Lab report with method and limits"),
        ("Phthalates","Plastic or PVC components","Lab report"),
        ("Azo dyes / formaldehyde","Dyed textiles, rope or fibre","Lab report"),
        ("Physical construction","Any toy with knots, seams or attachments","Construction review; pull test with agreed method"),
        ("Moisture (coffee wood)","Every coffee wood batch","Pin-type meter reading; below 14% before packing"),
        ("Cracks (coffee wood)","Every coffee wood piece","Grading record; any cracked piece rejected"),
        ("Lot inspection","Every order","Inspection report against the approved sample"),
      ], caption="Whether each check applies depends on the construction, market and retailer. Untreated coffee wood has no dye or coating to test.")),

    ("Building a test plan, step by step",
      steps([
        ("Describe the product","Dimensions, intended pet and play type, component list, claims, and photos of joins and attachments.","The reviewer sees what can actually go wrong."),
        ("List markets and buyer requirements","Destination country plus retailer or marketplace rules.","The checks that are required, not just nice to have."),
        ("Pick the checks","Match each check to a component or a claim.","A short, relevant plan instead of every certificate available."),
        ("Agree methods and pass criteria","For any pull test or chemical test, before testing.","Results that can be applied to later batches."),
        ("Plan for a failed result","Who receives results, who approves corrective action, whether retesting is needed.","Time in the launch schedule for a fix."),
        ("File the evidence with the SKU","Approved sample, specification, reports and inspection decision together.","A file the next buyer or QA manager can follow."),
      ])),

    ("VietPaw quality controls",
      spec_table(["Control","Figure"],[
        ("Coffee wood QC checkpoints","Five: intake, after seasoning, after shaping, at grading, at the packing bench"),
        ("Moisture","Below 14% before packing; batch readings on request"),
        ("Cracks","Any cracked piece rejected at grading"),
        ("Length tolerance","±3 mm on the coffee wood stick line"),
        ("Buyer inspection","Visits and third-party inspection welcome at all three factories"),
        ("Laboratory testing","Arranged separately on request"),
      ])),

    ("Read the report beyond the result line",
      p("Check the sample description, report number, testing body, dates, methods and results, and look at exclusions and limitations. If your "
        "order adds a different thread, colour or attachment, ask whether the existing report still covers the changed product.")
      + p("Do not treat a report for one size or component as automatic coverage for the full range. Agree how variants will be grouped with the "
          "responsible specialist, and keep that rationale in the product file.")),
    ],
    ("Discuss testing and documentation with VietPaw","/certifications/"),
    related=[("CPSIA, REACH and GPSR","/guides/pet-toy-safety-compliance-cpsia-reach/"),("Drying and quality protocol with five QC checkpoints","/quality-control/"),
             ("How to vet a supplier","/guides/how-to-vet-an-eco-pet-toy-supplier/")],
    image="vietpaw-moisture-check.jpg",
    faqs=[
      ("Is safety testing mandatory for pet toys?",
       "There is no single mandatory pet-toy test in the US or the EU, but products must be safe and chemical rules such as REACH apply. "
       "Retailers and marketplaces often set their own test requirements."),
      ("Which tests should I ask for?",
       "Those that match the components and claims: heavy metals for coloured parts, phthalates for plastic parts, a construction review for "
       "knots and attachments, and lot inspection for every order."),
      ("Does untreated coffee wood need chemical testing?",
       "It has no glue, coating, preservative or colouring, so there is little for a dye or coating test to find. Moisture and crack control "
       "are the relevant production checks. Testing can be arranged if your market or retailer requires it."),
      ("Is a phytosanitary certificate a safety certificate?",
       "No. It covers plant health for the shipment, not product safety."),
      ("Can one report cover my whole range?",
       "Only if a specialist agrees the variants can be grouped. A report for one size or material does not automatically cover others."),
    ],
    figures=[('carton-quality-check.jpg','Worker examining corrugated board quality in a packing area','Test reports have a defined scope. Ask for the one covering your SKU and your destination.'),('moisture-meter-on-the-line.jpg','Pin-type moisture meter reading taken on coffee wood sticks','A moisture record is order-specific evidence; a general description is not.'),('hemp-rope-ball-large.jpg','Large knotted hemp rope ball close up','Large hemp rope ball: look at knot tightness and loose ends on the sample.')])

add("how-to-vet-an-eco-pet-toy-supplier","Compliance & risk",
    "How to Vet a Natural Pet Toy Supplier Before the First Order",
    "Evaluate a pet toy supplier through company checks, specific samples, production visibility, claim evidence and a written order plan.",
    answer("<strong>Short answer:</strong> vet a natural pet toy supplier with six checks before paying a deposit — confirm the legal "
           "entity and payment beneficiary, test one real SKU against a written specification, verify where production happens, match "
           "every claim to evidence, agree inspection and documents in writing, and start with a small order. Each check should produce "
           "a document, not just a reassurance."),
    [
    ("What supplier vetting means",
      p("<dfn>Supplier vetting</dfn> (or supplier due diligence) is the set of checks a buyer makes to confirm that a supplier is who it says "
        "it is, can make the approved product repeatedly, and can back its claims with evidence. It is most useful when it follows the order "
        "you actually want to place.")
      + p("A well-presented catalogue can introduce the range. It cannot tell you whether the sample will be repeated, the right documents "
          "will arrive or a production change will be communicated before shipment.")),

    ("The supplier vetting checklist",
      spec_table(["Check","What to ask for","Red flag","What VietPaw provides"],[
        ("Legal entity and payment","Registration details and the beneficiary named on the contract","Bank account in a different name; bank details changed by email","Company details, beneficiary and terms in the quotation, invoice and contract"),
        ("Production location","Site details and a walkthrough for your product","Only warehouse photos; no named site","Three own factories in Dak Lak, Gia Lai and Binh Duong; visits and third-party inspection welcome"),
        ("Sample and specification","A sample with written dimensions, components and tolerances","Photo approval only; “same as before”","3 free samples; dimensions recorded at approval"),
        ("Quality records","Checkpoints and a record linked to your lot","Generic certificate, no batch reference","Coffee wood: five QC checkpoints; moisture below 14% before packing, batch readings on request"),
        ("Product claims","Evidence matched to the exact product and pack","“Non-toxic”, “splinter-free” or “biodegradable” without scope","Claims limited to what is documented; testing arranged on request"),
        ("Export documents","The document list for your destination","Unclear who issues the Certificate of Origin","Seven documents with every order"),
        ("Capacity","A production slot for your SKU mix","Only an annual headline figure","100,000 pcs a month; your slot confirmed in the quotation"),
      ])),

    ("Supplier vetting, step by step",
      steps([
        ("Confirm who you contract with","Match the company name, address and bank beneficiary across quote, invoice and contract.","One verified counterparty before any payment.","If payment details ever change, verify by a contact route you already trust."),
        ("Pick one real SKU","Ask for its construction, dimensions, packing and production sequence.","Concrete answers you can inspect later."),
        ("Approve a sample against a written spec","Measure it, list its components and record acceptable natural variation.","A reference that survives staff changes and repeat orders."),
        ("Verify where the work happens","Request site details and a walkthrough, or book an inspection.","You know who controls production and where to inspect."),
        ("Match claims to evidence","Component list for material claims; report scope for test claims; defined scope for environmental claims.","Only supportable claims reach your pack."),
        ("Put the order plan in writing","Approval stages, quality criteria, inspection timing, document list and a process for non-conforming goods.","A first delivery you can measure against what was agreed."),
        ("Start small","A stock-packed first order from 50 pcs per SKU.","Receiving data before you commit volume."),
      ])),

    ("Claims to test before they reach your pack",
      spec_table(["Claim","Evidence that would support it","Watch for"],[
        ("Non-toxic","A test report naming the product, the substances assessed and the method","A report for a different material or product"),
        ("Biodegradable or compostable","A defined scope, disposal conditions and supporting test data","A material claim applied to the whole toy and pack"),
        ("Splinter-free","Test data behind the phrase","No supplier in this category has published it"),
        ("Dental or health benefit","Clinical evidence","A medical promise on a toy"),
        ("CPSIA or REACH compliant","The applicable requirement for your market and a matching report","A certificate that names no product"),
      ])
      + p("For a material claim, review the component list. For a test claim, review the sample and report scope. A confident supplier should be "
          "able to distinguish what is documented from what still needs assessment.")),

    ("Ask questions tied to one real SKU",
      p("Ask what natural variation the factory expects and which defects it rejects. A supplier that can explain those distinctions gives you "
        "something concrete to inspect later.")
      + p("Keep a reference sample and ask how it will be retained at the factory. Confirm that substitutions in fiber, adhesive, finish or "
          "packaging need approval. A look-alike replacement may change the product or its claims even when it seems commercially convenient.")),

    ("Make the production review specific",
      p("Request current location information and a walkthrough or inspection arrangement for the relevant process. Discuss order-specific "
        "scheduling rather than relying only on a large annual-capacity figure.")
      + p("The goal is to understand who controls the work and how a problem will be traced. A warehouse image can show stock or packing, but "
          "it does not answer every question about production equipment, ownership or available capacity. Before the container is sealed, ask "
          "for the carton marks to be photographed against the packing list and for the seal number on your paperwork.")),
    ],
    ("Review VietPaw factory and production information","/factory/"),
    related=[("Testing and documents","/certifications/"),("Wholesale order planning","/services/wholesale-pet-products/"),
             ("Choosing a manufacturer in Vietnam","/guides/natural-dog-toy-manufacturer-vietnam/"),("Safety testing plan","/guides/pet-toy-safety-testing-requirements/")],
    sources=[("FTC Green Guides: environmental claims",FTC),("CPSC toy safety business guidance",CPSC)],
    image="pallet-stack-inspection.jpg",
    faqs=[
      ("How do I verify a pet toy supplier in Vietnam?",
       "Match the company name, address and bank beneficiary across the quote, invoice and contract; request site details and a walkthrough "
       "or a third-party inspection; and approve a physical sample against a written specification before paying a deposit."),
      ("What should I do if a supplier changes its bank details?",
       "Do not pay until you have confirmed the change through a contact route you already trust, such as a known phone number. Changed bank "
       "details sent by email are a common fraud pattern."),
      ("Do I need to visit the factory?",
       "Not always, but you should be able to. A walkthrough, a video tour of your product line or an independent inspection gives similar "
       "evidence. VietPaw welcomes visits and third-party inspection at all three factories."),
      ("Which documents should a natural pet toy supplier provide?",
       "At minimum a Commercial Invoice, Packing List and transport document. For plant-based goods, expect a Certificate of Origin, "
       "Phytosanitary and Fumigation Certificates; VietPaw also issues a Forest-Product Declaration."),
      ("How big should a first order be?",
       "Small enough to learn from. A stock-packed order from 50 pcs per SKU lets you check receiving quality and sell-through before "
       "committing to private label or container volume."),
    ],
    figures=[('inspector-checking-cartons-clipboard.jpg','Inspector in a hi-vis vest checking export cartons against a printed document','Ask for the carton marks to be photographed against the packing list before the container is sealed.'),('container-seal-applied.jpg','Hands fitting a numbered plastic seal to a shipping container door','The seal number belongs on your paperwork. It is the cheapest verification step there is.'),('coconut-fiber-balls-and-rope-toy.jpg','Two coconut fiber balls of different sizes and a knotted rope toy','Balls and rope from the same coir line — one material, three formats.'),('hemp-rope-loop-ball-toy.jpg','Hemp rope toy with a loop handle and a knotted ball end','Ball-with-rope: the join between loop and ball is a separate inspection point.')])

add("coffee-wood-chew-size-guide","Natural chew toys",
    "Coffee Wood Chew Sizes: VietPaw's XS–XXL Reference",
    "Compare VietPaw CC01 coffee wood chew dimensions and reference weight bands, with advice on sample approval, labels and size selection.",
    answer("<strong>Short answer:</strong> VietPaw’s standard CC01 coffee wood chews come in six sizes, from XS (10 cm, 23–30 g, dogs up to "
           "3 kg) to XXL (22–23 cm, 340–440 g, dogs of 20 kg and over). Choose by the dog’s weight band and go up one size for a dog at the top "
           "of its band. For strong chewers, use the thick-cut Gorilla line (GRLS–GRLXL, 155–900 g) instead of stretching the standard range."),
    [
    ("How coffee wood chews are sized",
      p("Each size is defined by three measurements together: <dfn>length</dfn> (cut to ±3 mm), <dfn>diameter</dfn> (which follows the natural "
        "stem and is graded into bands) and <dfn>weight</dfn> (a range, because wood density varies). A size label such as “M” is convenient "
        "for ordering, but it is not a measurement.")
      + p("The <dfn>reference dog weight</dfn> is a starting point for choosing a size. Beyond it, the dog’s mouth size and chewing style decide "
          "the fit — the chew must always stay too large to be swallowed whole.")),

    ("CC01 standard size reference",
      coffee_size_table()
      + p("When a dog sits at the top of a band, or is a keen chewer, go up one size. The consequence of one size too large is a chew that lasts "
          "longer; the consequence of one size too small is the thing everybody is trying to avoid.")),

    ("Gorilla line for strong chewers",
      p(GORILLA)
      + gorilla_table()
      + p("Keep the two tables separate on your listings. Gorilla and CC01 are different lines with different SKUs; do not merge them into one "
          "size ladder.")),

    ("Choosing and approving a size, step by step",
      steps([
        ("Start from the dog’s weight","Find the band in the CC01 table.","A first-choice size."),
        ("Adjust for chewing style","Keen chewer or top of the band: one size up. Strong chewer: Gorilla.","A size that lasts and cannot be swallowed."),
        ("Order samples of the sizes you will sell","Up to 3 free samples; you cover the courier.","Pieces to measure side by side."),
        ("Measure and record","Length, diameter at the narrowest and widest point, and weight.","A written reference that matches the table."),
        ("Keep one approved reference per SKU","Label it with the size and SKU code.","Repeat orders can be checked against it."),
        ("Match the label to the table","Use the same chart on the website, the pack and the quotation.","No mismatch between shelf and purchase order."),
      ])),

    ("Measure the product you are approving",
      p("Natural sticks are not perfect cylinders. Agree how length and diameter will be measured, what variation is acceptable and which "
        "reference identifies the size. Include the finished weight band in the specification so the factory and your receiving team use the "
        "same definition.")
      + p("For mixed cartons, show the quantity of each SKU clearly. “Assorted sizes” is not enough if the warehouse needs to reconcile barcode "
          "counts or replenish separate retail lines. Export carton counts for loose sticks are in the table above.")),

    ("Size changes during use",
      p("The starting dimensions are not the removal rule. Supervise use, inspect the chew and remove it when it cracks or wears down to a size "
        "that could be swallowed. Coffee wood chews are not food.")
      + p("Put that advice near the size information. Owners need to understand both how to select a size and when the chew they selected is no "
          "longer suitable. Do not treat XS as a puppy designation simply because it is the smallest size; for puppies and dogs with dental "
          "conditions, ask a vet first.")),
    ],
    ("Coffee wood product specifications and sample options","/products/coffee-wood-dog-chew/"),
    related=[("Coffee wood suitability","/guides/are-coffee-wood-chews-safe-for-dogs/"),("Toys for strong chewers","/guides/best-natural-chews-for-aggressive-chewers/"),
             ("How long coffee wood chews last","/guides/how-long-do-coffee-wood-chews-last/"),("Private-label pack development","/services/private-label-pet-toys/")],
    image="vietpaw-coffee-wood-sizes.png",
    faqs=[
      ("What size coffee wood chew should I choose for my dog?",
       "Use the dog’s weight: XS up to 3 kg, S 3–5 kg, M 5–8 kg, L 8–12 kg, XL 12–20 kg, XXL 20 kg and over. Go up one size for a keen chewer "
       "or a dog at the top of its band."),
      ("What size is best for a strong chewer?",
       "The thick-cut Gorilla line rather than a bigger standard stick. It runs from GRLS (5–6 × 8 cm, 155–230 g) to GRLXL (10–12 × 15 cm, "
       "550–900 g)."),
      ("Why do two sticks of the same size weigh differently?",
       "Coffee wood is natural and its density varies. Grading controls the size band; the weight is published as a range."),
      ("How accurate is the length?",
       "Length is cut to ±3 mm. Diameter follows the natural stem and is controlled by grading into bands."),
      ("Is XS suitable for puppies?",
       "Not automatically. XS is the smallest size, not a puppy product. Ask a vet before giving a puppy a hard chew."),
      ("How many sticks fit in an export carton?",
       "For loose sticks: S 512, M 224, L 126, XL 85; XS and XXL on request. Retail packaging reduces the count."),
    ],
    figures=[('coffee-wood-chew-size-row.jpg','Coffee wood chew sticks laid out from smallest to largest','Six graded sizes. Length is cut to ±3 mm; diameter follows the natural stem and is graded into bands.'),('puppy-holding-coffee-wood-chew.jpg','Golden retriever puppy holding a coffee wood chew in its mouth',"Judge the fit against the dog's mouth, not against the size label."),('catalogue-coffee-wood-six-sizes.jpg','Six coffee wood chew sizes from XS to XXL on a cream background','Catalogue image: the six standard CC01 sizes, XS to XXL.'),('coffee-wood-chews-size-range-packed.jpg','Coffee wood chews in several sizes laid out in their vacuum packs','The size range, packed: each size is graded into its own diameter band.')])


# Owner request 2026-09-24: a content-matched lead image on every guide (served as responsive WebP).
# Each lead image differs from the in-text figures of the same guide. Displayed dates are unchanged.
FEATURE = {
    "natural-dog-chew-toys-guide": ("vietpaw-hemp-wood-assortment.jpg", "Woven basket holding hemp rope toys and coffee wood chews", "Wood, rope and fiber: the chewing style decides which one fits the dog."),
    "are-coffee-wood-chews-safe-for-dogs": ("dog-chewing-coffeewood.jpg", "Golden retriever lying on a rug chewing a coffee wood stick", "Supervised chewing with a size the dog cannot swallow whole."),
    "coffee-wood-vs-antler-nylon-rawhide": ("vietpaw-home-lifestyle.jpg", "Small dog at home holding a coffee wood chew in its mouth", "A plant-based hard chew, compared honestly with antler, nylon and rawhide."),
    "best-natural-chews-for-aggressive-chewers": ("process-raw-sticks.jpg", "Thick coffee wood chew sticks of different diameters on a white surface", "For strong chewers, diameter matters more than length — size up when in doubt."),
    "how-long-do-coffee-wood-chews-last": ("dog-lifestyle-chew-1.jpg", "Small white dog lying on the floor gnawing a coffee wood chew", "How long a chew lasts depends on the dog, not on the calendar."),
    "coffee-wood-chew-size-guide": ("coffee-stem-diameter-caliper-check.jpg", "Digital caliper measuring the diameter of a coffee wood stem", "Diameter follows the natural stem and is graded into size bands."),
    "plastic-free-biodegradable-pet-toys-guide": ("vietpaw-natural-toy-assortment.png", "Basket of loofah shapes and coffee wood chews", "Plastic-free is a claim about every component, including the pack."),
    "are-dog-toys-biodegradable": ("peeling-dried-loofah-gourd.jpg", "Hands peeling the skin from a dried loofah gourd to expose the fiber", "Plant fiber at the start — but a biodegradability claim covers the finished toy."),
    "what-is-coconut-fiber-pet-toys": ("dog-coconut-balls-lifestyle.jpg", "Corgi lying beside three wound coconut fiber balls", "Coir from the coconut husk, wound into textured balls."),
    "non-toxic-cat-toys-wholesale-buying-guide": ("vietpaw-loofah-play-shapes.png", "Loofah cat play shapes arranged on a light surface", "Light loofah shapes for batting and carrying — specified for cats, not scaled-down dog toys."),
    "sustainable-pet-toy-materials-compared": ("product-hemp-rope-trio.jpg", "Three knotted coconut fiber rope toys beside a split coconut", "Coconut, hemp, loofah and coffee wood each have a different origin story."),
    "sourcing-eco-pet-toys-vietnam": ("coffee-wood-stem-cross-cutting.jpg", "Worker cross-cutting coffee wood stems with a saw in a Vietnamese workshop", "Cutting coffee wood stems to length at our factory."),
    "natural-dog-toy-manufacturer-vietnam": ("coffee-wood-drying-rack-rows.jpg", "Rows of coffee wood chew sticks laid out on drying racks", "Chews drying in rows before grading — our own line."),
    "wholesale-coconut-fiber-cat-toys-supplier": ("vietpaw-coconut-fiber-balls.jpg", "Hand holding several wound coconut fiber balls outdoors", "Coconut fiber balls: specify diameter and winding for cats separately."),
    "private-label-oem-eco-pet-toys-explained": ("coffee-wood-cotton-rope-tug-pair.jpg", "Two coffee wood and cotton rope tug toys on a white background", "A changed construction is an OEM project, not a label swap."),
    "pet-toy-moq-fob-pricing-lead-times": ("export-cartons-stacked-for-loading.jpg", "Export cartons stacked on pallets in a warehouse ready for loading", "Carton count and pack format drive the landed cost per piece."),
    "pet-toy-safety-compliance-cpsia-reach": ("vacuum-bagged-chews-stacked.jpg", "Vacuum-bagged coffee wood chews stacked with size labels", "Labels, warnings and pack materials are part of the compliance question."),
    "sourcing-pet-toys-vietnam-vs-china": ("pallet-stack-inspection.jpg", "Stacked export cartons on pallets being inspected", "Ask the same verification questions of every origin."),
    "pet-toy-safety-testing-requirements": ("moisture-reading-before-packing.jpg", "Moisture meter reading taken on a coffee wood chew before packing", "A production check, not a lab test — know which one you are looking at."),
    "how-to-vet-an-eco-pet-toy-supplier": ("coffee-wood-moisture-meter-check.jpg", "Hand holding a moisture meter against a coffee wood chew", "Ask for the record behind the claim — here, the moisture reading on your lot."),
}

def build(root):
    clusters={}
    for a in ARTICLES:
        clusters.setdefault(a["cluster"],[]).append(a)
    bc,bs=breadcrumb_html([("Home","/"),("Guides",None)])
    hub = bc + ('<section class="hero"><div class="wrap">'
        '<p class="hero-eyebrow">VietPaw \u00b7 Buyer guides</p>'
        '<h1>Sourcing Guides for Natural Pet Toys</h1>'
        '<p class="hero-lede">Written by Sarah for pet brands, retailers, distributors and importers. '
        'Specifications, sourcing decisions and the claims this category gets wrong \u2014 written from the '
        'supply side, including the parts that do not help us sell.</p></div></section>')
    hub += section("Start here",
        answer("If you are new to sourcing natural pet toys, three questions decide most of the rest: which "
               "material suits the chewing style you are selling to, what the minimum order and lead time "
               "actually are, and which claims you can legally put on the pack. One guide below covers each.")
        + cards([
            ("Which material for which dog",
             "Chewing style, not material name, decides what works. Start here before choosing a range.",
             "/guides/natural-dog-chew-toys-guide/","/assets/img/shiba-inu-chewing-coffee-wood-stick.jpg"),
            ("MOQ, pricing and lead times",
             "What the numbers mean, where the hidden minimums sit and how production time differs from arrival date.",
             "/guides/pet-toy-moq-fob-pricing-lead-times/","/assets/img/export-cartons-stacked-for-loading.jpg"),
            ("What you can and cannot claim",
             "Biodegradable, non-toxic, splinter-free, dental benefit \u2014 which of these survive scrutiny.",
             "/guides/plastic-free-biodegradable-pet-toys-guide/","/assets/img/bagged-chews-with-desiccant.jpg"),
          ])
        + p("Looking for specifications rather than guidance? Sizes, weights and carton data are on the "
            '<a href="/products/coffee-wood-dog-chew/">coffee wood product page</a>, and material detail is '
            'under <a href="/collections/coffee-wood/">coffee wood</a>, '
            '<a href="/collections/coconut-fiber/">coconut fiber</a>, '
            '<a href="/collections/hemp-fiber/">hemp fiber</a> and '
            '<a href="/collections/loofah/">loofah</a>.'))
    CLUSTER_NOTE = {
      "Natural chew toys": "Sizing, safety limits, lifespan and honest comparisons against rawhide, antler and nylon.",
      "Materials & claims": "What each material is, what it is not, and which environmental and safety claims can actually be supported.",
      "Sourcing & trade": "Minimums, pricing structures, lead times, private label versus OEM, and sourcing from Vietnam in practice.",
      "Compliance & risk": "Testing scope, CPSIA and REACH, and how to check a supplier before the first container.",
    }
    for cluster,articles in clusters.items():
        hub += section(cluster,
            (p(CLUSTER_NOTE[cluster]) if cluster in CLUSTER_NOTE else "")
            + cards([(a["title"],
                      a["description"]+f'<span class="guide-updated">Updated {updated_time(a["slug"])}</span>',
                      "/guides/"+a["slug"]+"/","/assets/img/"+FEATURE[a["slug"]][0]) for a in articles]),
            alt=(list(clusters).index(cluster) % 2 == 1))
    hub += section("How these guides are written",
        ul(["Figures are labelled as reference specifications or as internally reported planning numbers, never presented as audited measurements.",
            "Where no data exists \u2014 chew lifespan, coffee wood hardness, rope tensile ratings \u2014 we say so rather than estimating.",
            "Claims we will not support are named explicitly, including ones that would help us sell.",
            "External guidance is linked at the foot of the guide that relies on it."])
        + p("Guides are updated as specifications change; each carries its own update date. If something here "
            'conflicts with a quotation, the quotation governs \u2014 <a href="/contact/">tell us</a> and we will fix '
            'the page.'), True)
    write_page(root,"/guides/",page("Pet Toy Sourcing Guides | Specs, MOQ & Claims | VietPaw",
        "Buyer guides to natural pet toy materials, chew sizing, supplier verification, MOQ and lead times, and "
        "which product claims can actually be supported. Written from the supply side.",
        "/guides/",hub+rfq_bar(),"Guides",[bs]))
    for a in ARTICLES:
        path="/guides/"+a["slug"]+"/"
        bc,bs=breadcrumb_html([("Home","/"),("Guides","/guides/"),(a["title"],None)])
        figs=list(a.get("figures") or ())
        blocks=[]
        for i,(h,sec) in enumerate(a["sections"]):
            blocks.append("<h2>"+h+"</h2>"+sec)
            if figs:
                blocks.append(figure("/assets/img/"+figs[0][0], figs[0][1], figs[0][2]))
                figs.pop(0)
        lead=FEATURE[a["slug"]]
        assert lead[0] not in [f[0] for f in (a.get("figures") or ())], a["slug"]
        intro=a["intro"] if a["intro"].startswith("<") else p(a["intro"])
        body=figure("/assets/img/"+lead[0],lead[1],lead[2],lazy=False)+intro+"".join(blocks)
        if a["faqs"]:
            body+="<h2>Frequently asked</h2>"+"".join(
                f'<div class="faq-item"><h3>{q}</h3><p>{ans}</p></div>' for q,ans in a["faqs"])
        anchor,url=a["commercial"]
        body+=f'<div class="callout"><a href="{url}">{anchor}</a></div>'
        if a["related"]:
            body+="<h2>Further reading</h2>"+ul([f'<a href="{u}">{t}</a>' for t,u in a["related"]])
        if a["sources"]:
            body+='<div class="source-note"><h2>Reference guidance</h2>'+ul([f'<a href="{u}">{t}</a>' for t,u in a["sources"]])+'</div>'
        content=bc+f'<article class="section"><div class="wrap article"><p class="tag">{a["cluster"]}</p><h1>{a["h1"]}</h1><p class="meta article-byline">By <span class="author-name">Sarah</span> · VietPaw · Updated {updated_time(a["slug"])}</p>{body}</div></article>'
        schema={"@context":"https://schema.org","@type":"Article","@id":BASE_URL+path+"#article",
            "headline":a["title"],"description":a["description"],"dateModified":GUIDE_UPDATED_DATES[a["slug"]],
            "mainEntityOfPage":BASE_URL+path,"image":BASE_URL+"/assets/img/"+FEATURE[a["slug"]][0],
            "author":{"@type":"Person","name":"Sarah"},
            "publisher":{"@id":BASE_URL+"/#organization"}}
        extra=[]
        if a["faqs"]:
            extra.append({"@context":"https://schema.org","@type":"FAQPage","@id":BASE_URL+path+"#faq",
                "mainEntity":[{"@type":"Question","name":q,
                               "acceptedAnswer":{"@type":"Answer","text":re.sub(r"<[^>]+>","",ans)}}
                              for q,ans in a["faqs"]]})
        write_page(root,path,page(a["title"]+" | VietPaw",a["description"],path,content+rfq_bar(),
            "Guides",[bs,schema,*extra],og_image="/assets/img/"+FEATURE[a["slug"]][0]))
