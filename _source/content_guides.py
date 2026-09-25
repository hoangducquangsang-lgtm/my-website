# -*- coding: utf-8 -*-
"""VietPaw editorial guides. Author attribution supplied by the website owner."""
import re
from common import BASE_URL, BRAND, page, write_page, breadcrumb_html
from guide_dates import GUIDE_UPDATED_DATES, updated_time
from content_helpers import (section, p, ul, table, cards, rfq_bar, FTC, CPSC, ECHA, AAHA,
                             answer, fit, steps, spec_table, figure, SAFETY)
from content_products import coffee_size_table

ARTICLES=[]
def add(slug,cluster,title,description,intro,sections,commercial,related=(),sources=(),
        image="vietpaw-natural-toy-assortment.png",faqs=(),h1=None,figures=()):
    ARTICLES.append(dict(slug=slug,cluster=cluster,title=title,description=description,intro=intro,
        sections=sections,commercial=commercial,related=related,sources=sources,image=image,
        faqs=faqs,h1=h1 or title,figures=figures))

add("natural-dog-chew-toys-guide","Natural chew toys",
    "Natural Dog Chew Toys: Building a Range That Makes Sense",
    "How to choose natural dog toys for a wholesale range, from chewing behavior and material construction to sample approval and retail packaging.",
    "A dog that carries a toy around the house and a dog that tries to pull it apart are asking very different things of the same product. That distinction belongs at the beginning of a buying brief. A range built around the word natural, without a clear use for each item, leaves store staff and customers to work out the important details themselves.",
    [
    ("Give each product a job",p("Separate chewing, fetch and owner-led tug play in your assortment. Coffee wood sticks belong in a different conversation from fiber balls and rope toys. Edible chews are another category again: a wooden stick is a non-food product, even if it sits beside treats on a retail shelf.")+
        p("For a first order, a small number of clearly differentiated products is easier to support than several similar-looking designs. Decide who each item is for, what the owner does during play and when the item should be removed. Those decisions will shape the size range, packaging and instructions.")),
    ("The sample needs to answer more than one question",p("Handle the product before judging the photograph. With wood, compare the narrowest and widest points, surface finish and visible cracks. With rope or wound fiber, look at knot placement, loose ends and the way components are joined. Request the complete material list; a natural outer layer does not identify a hidden core or binding thread.")+
        p("Keep an approved sample, but put its important features into writing as well. A photograph cannot settle a later disagreement about diameter or weight. Natural grain and shade can vary; an unapproved change in construction is a different matter.")),
    ("Build the range around use, not a toughness ranking",p("Hardness is not a universal quality score. AAHA cautions that very hard chews can damage teeth. A heavy dog is not automatically a suitable customer for a hard chew, and a small stick is not automatically suitable for a puppy. When dental condition or forceful chewing is a concern, individual veterinary advice matters more than the catalogue size label.")),
    ("Make the first order teach you something",p("Record quantities by SKU and size, rather than only the total number of toys. Agree the pack count, barcode placement and carton marks before production. At receiving, separate manufacturing defects from transit damage and keep the batch reference with each issue.")+
        p("After launch, review which sizes sell, which questions customers ask and why products are returned. That information gives the second order a sounder basis. A broad promise such as suitable for all dogs does not."))],
    ("Explore VietPaw's natural dog toy range","/dog-toys/"),
    related=[("Coffee wood sizing","/guides/coffee-wood-chew-size-guide/"),("Wholesale ordering","/services/wholesale-pet-products/")],
    sources=[("AAHA guidance on hard chews",AAHA)],
    image="vietpaw-coffee-wood-sizes.png",
    figures=[('shiba-inu-chewing-coffee-wood-stick.jpg','A Shiba Inu lying on the floor gnawing a coffee wood chew stick',"Gnawing rather than cracking. Chewing style decides which material suits a dog, more than the dog's weight does."),('puppy-with-rope-and-fiber-ball.jpg','Puppy nosing a natural fiber ball with a rope loop on a tiled floor','Fetch and carry is a different job from chewing — give each product one role in the range.')])

add("are-coffee-wood-chews-safe-for-dogs","Natural chew toys",
    "Are Coffee Wood Chews Safe for Dogs?",
    "A practical look at coffee wood chew suitability, hard-chew risks, product inspection and the instructions retailers should give owners.",
    "There is no honest yes-or-no answer that applies to every dog. Coffee wood is a hard, non-edible chew material. Its plant origin tells you where it comes from; it does not tell you whether it suits a particular dog's teeth, mouth size or way of chewing.",
    [
    ("Consider the dog before the stick",p("A dog that gnaws slowly places different demands on a chew from one that clamps down and tries to break pieces off. Existing dental problems, age and chewing behavior all affect the decision. For puppies, dogs with dental concerns or forceful chewers, ask a veterinarian whether a hard chew is appropriate before choosing a size.")+
        p("AAHA's warning about tooth damage from hard chewing objects is relevant here. Making a chew larger may reduce the chance of swallowing it whole, but it does not make the material softer or remove dental risk.")),
    ("What a finished product should tell you",p("The sample and label should identify the material, size and intended use. Examine the surface and ends for damage, sharp projections or developing cracks. Natural grain patterns are expected; a split that could release a piece needs attention. Do not sell a received item with visible damage as an acceptable natural variation.")+
        p("Ask our production team about drying and inspection records. These are useful production controls, but neither a moisture-meter photograph nor a smooth finish proves that a chew is safe for every dog.")),
    ("Supervision includes knowing when to stop",p("Check the chew before and during use. Remove loose pieces, and take the product away if it cracks, becomes damaged or wears down to a size the dog could swallow. If the dog is trying to break off and swallow chunks, discontinue that product rather than waiting for it to wear out.")+
        p("The pack should make clear that the product is not food. Avoid statements suggesting that every fiber or fragment is harmless to swallow. Suspected swallowing of a substantial piece or signs of injury need veterinary attention, not a recommendation to keep using the chew.")),
    ("What buyers should put on the label",p("Keep the advice short enough to be read: intended pet, size selection, supervised use, inspection and replacement. Put the same guidance on the product page and the pack. A sales claim such as splinter-free or safe for all dogs can undo that care by creating a false expectation.")+
        p("VietPaw's size reference is useful for comparing products. Use it alongside the actual dimensions and a suitability decision, not as a substitute for either."))],
    ("Coffee wood product specifications","/products/coffee-wood-dog-chew/"),
    related=[("Size guide","/guides/coffee-wood-chew-size-guide/"),("Quality-control workflow","/quality-control/")],
    sources=[("AAHA: hard-chew risks",AAHA)],
    image="coffee-wood-chew-grain-detail.jpg",
    figures=[('coffee-wood-chew-grain-detail.jpg','Close-up of a finished coffee wood chew stick showing grain and surface finish','One untreated plant material: no glue, coating, preservative or colouring.'),('grading-chews-before-packing.jpg','Hand holding a coffee wood stick above a crate of graded pieces','Grading. Pieces cracked beyond 2 mm are pulled out at this bench.')])

add("coffee-wood-vs-antler-nylon-rawhide","Natural chew toys",
    "Coffee Wood, Antler, Nylon or Rawhide: What Are You Comparing?",
    "Compare coffee wood, antler, nylon and rawhide by intended use, product construction, retail presentation and purchasing requirements.",
    "These products are often placed in one comparison chart because dogs chew them. For a buyer, that is not enough. A molded toy, a piece of antler, a wood stick and a processed hide chew differ in construction and commercial category. The useful comparison starts with the job you want the product to do.",
    [
    ("Separate the product categories",table(["Format","What the buyer needs to establish"],[
        ("Coffee wood","Non-edible stick; dimensions, finish, drying and use instructions."),
        ("Antler","Animal-derived hard chew; source, cut, dimensions and intended use."),
        ("Nylon","Manufactured polymer product; formulation, design and replacement instructions."),
        ("Rawhide","Processed animal-hide chew; ingredients, processing, labeling and applicable import category.")])+
        p("Do not borrow the feeding directions of one category for another. Product classification and import documentation should follow the actual article being shipped, not the shelf on which a retailer plans to display it.")),
    ("Harder does not settle the choice",p("Coffee wood, antler and hard synthetic products should not be ranked by hardness alone. A product that resists wear can still be unsuitable for a particular dog's teeth or chewing style. Rawhide raises a different discussion about the specific product, consumption and use instructions. None of these labels establishes a universal winner.")+
        p("Retailers need a clear way to explain those differences without making a medical promise. Describe the material and intended use, then give the owner the relevant supervision and replacement guidance.")),
    ("Compare the quote at the same point in the supply chain",p("A loose stick quoted at our factory and a boxed, barcoded item delivered to your warehouse are not comparable prices. Match the specification, saleable unit, packaging, quantity and delivery basis. Then include inspection, testing, transport, duties and handling where applicable.")+
        p("Also consider what the product asks of the retail operation. Will staff need a size explanation? Does each variant require a separate barcode? Can damaged packaging be replaced locally, or is the complete unit unsaleable? These details can outweigh a small saving in purchase price.")),
    ("Keep material and disposal claims separate",p("Wood has a different origin story from nylon, but the environmental statement still needs a defined scope. A wood-and-rope combination may contain several components; a paper-looking pack may include a film window. Describe what is in the product before deciding which disposal claims belong on the label.")+
        p("Choose the product you can specify, explain and reorder consistently. A comparison based on those three points is more useful than a table of unsupported safety scores."))],
    ("Compare coffee wood wholesale options","/collections/coffee-wood/"),
    related=[("Coffee wood safety considerations","/guides/are-coffee-wood-chews-safe-for-dogs/"),("Natural material comparison","/guides/sustainable-pet-toy-materials-compared/")],
    image="vietpaw-coffee-wood-sizes.png",
    figures=[('coffee-wood-chew-size-row.jpg','Six coffee wood chew sticks laid out in increasing size on a light background','Coffee wood does not soften, swell or develop an odour as it is worked — a factual difference from rawhide.'),('french-bulldog-chewing-coffee-wood.jpg','French bulldog chewing a coffee wood stick on a wooden table','A powerful chewer can still break a piece off any hard chew.')])

add("best-natural-chews-for-aggressive-chewers","Natural chew toys",
    "Choosing Natural Toys for Strong Chewers",
    "How retailers can respond to strong-chewer requests without confusing hardness, size or an aggressive-chewer label with guaranteed suitability.",
    "When a customer asks for the toughest chew you sell, the next question should be how the dog uses its toys. Does it gnaw, tear at seams, unravel rope or bite through solid objects? Strong chewer is a useful opening description, but it is not a product specification.",
    [
    ("Match the activity before recommending a material",p("A rope toy can be intended for short, owner-led tug sessions without being suitable for prolonged chewing. A ball designed for carrying and fetch should not become an unattended chew simply because the dog enjoys holding it. Give each product a stated purpose and merchandise it accordingly.")+
        p("If a dog repeatedly breaks off pieces, the solution is not automatically a harder version of the same item. Hard materials bring their own dental concerns. A veterinarian can help an owner decide what type of product is appropriate for that individual dog.")),
    ("Look for the way a design can come apart",p("On a rope assembly, examine the knots, ends, handle and joins between materials. On a wood chew, look at the narrow sections, ends and visible cracks. A larger overall measurement does not explain the weakest part of an assembled toy.")+
        p("For procurement, write down the construction you approved: rope diameter, knot arrangement, component dimensions and attachment method. If you need a pull or attachment test, agree its method and acceptance criteria. A number quoted without a method is difficult to use when inspecting a later batch.")),
    ("Give replacement advice a prominent place",p("Owners should supervise play, remove loose pieces or long frayed strands and replace damaged or worn items. Do not bury this advice beneath an indestructible headline. The headline is likely to be remembered; the small print may not be.")+
        p("Dog-weight bands are only a starting point for selecting dimensions. They do not measure bite force or dental condition. Going up a size should never be presented as a guarantee that a hard chew is suitable.")),
    ("Use returns to refine the range",p("Ask for the SKU, size, batch reference, a photograph and a description of use. Keep breakage on arrival separate from damage during play. If complaints cluster around one join or one size, that gives the supplier a specific design question to investigate.")+
        p("For a new range, order a manageable assortment and train the sales team on intended use. Fewer, clearly explained products are easier to recommend responsibly than a long ladder of increasingly strong claims."))],
    ("Strong-chewer product selection","/collections/aggressive-chewers/"),
    related=[("Hemp rope constructions","/products/hemp-rope-dog-toy/"),("Coffee wood safety","/guides/are-coffee-wood-chews-safe-for-dogs/")],
    image="vietpaw-hemp-wood-assortment.jpg",
    figures=[('golden-retriever-chewing-coffee-wood.jpg','Golden retriever chewing a coffee wood stick surrounded by other chews','Hard is not the same as safe: a determined chewer risks a fractured tooth on any hard material.'),('coffee-wood-chew-size-row.jpg','Coffee wood chew sticks in six sizes on a light background','Sizing up is usually safer than sizing down for a strong chewer.')])

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
    sources=[("AAHA guidance on hard chews",AAHA)],
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
    figures=[('coffee-wood-chew-size-row.jpg','Coffee wood chew sticks in six sizes on a light background','Material volume rises sharply with diameter — an XL holds far more wood than an L.'),('coffee-wood-chew-grain-detail.jpg','Close-up of a coffee wood chew surface showing the grain','In normal chewing the surface wears into soft fibres; replace the chew once it is small enough to swallow.')])

add("plastic-free-biodegradable-pet-toys-guide","Materials & claims",
    "Plastic-Free Pet Toys: What Belongs in the Buying Brief?",
    "Specify plastic-free pet toys and packaging clearly, with separate decisions on materials, components and end-of-life claims.",
    "A toy can look entirely natural on a shelf and still contain synthetic binding thread, an internal core or a laminated tag. If plastic-free is part of your brand promise, those small components belong in the first conversation with our production team, not in a discussion after the packaging has been printed.",
    [
    ("Define the boundary of the promise",p("Decide whether you mean the toy, the retail pack or the complete delivered unit. These are different briefs. A wood stick in a plastic bag is not a plastic-free retail unit, even if the stick itself contains no plastic. Equally, a paper sleeve does not tell you what holds an assembled fiber toy together.")+
        p("Use a component list that follows the product from the inside out: body, core, rope, sewing thread, adhesive, finish and decoration. Then list the bag, sleeve, label, window and any protective insert. This turns a broad ambition into something a supplier can quote and inspect.")),
    ("Choose packaging with the journey in mind",p("The retail display is only one part of the journey. The product also has to survive packing, transport, unloading and storage. Ask our factory to explain its proposed protection against moisture and damage, then review the materials used for that protection.")+
        p("Vacuum packing is a method, not a material description. Kraft-colored paper may be coated or laminated. If your brief excludes these options, resolve the alternative before approving the sample. Removing a bag without considering the rest of the packing plan can create a different problem at receiving.")),
    ("Keep biodegradability out of the material shortcut",p("Plastic-free describes composition. Biodegradable describes breakdown under particular conditions; compostable adds another set of questions. One claim does not establish the others. FTC guidance emphasizes evidence and qualification for environmental claims, including the conditions relevant to disposal.")+
        p("Ask exactly which article was assessed and whether the evidence covers the finished construction. Do not transfer a claim about raw fiber to a toy with additional components or to the package around it.")),
    ("Approve the words with the sample",p("Keep the agreed material declaration and final artwork beside the approved sample. A small substitution in thread, coating or packaging may change the claim even when the product looks unchanged. The purchase order should therefore require approval for material changes.")+
        p("Where evidence is limited, precise language is still useful: coffee wood stick, coconut-fiber outer surface or paper sleeve. A customer should be able to understand exactly what the statement covers."))],
    ("Plan a plastic-free product range","/collections/plastic-free/"),
    related=[("Material and packaging approach","/sustainability/"),("Biodegradability explained","/guides/are-dog-toys-biodegradable/")],
    sources=[("FTC environmental-claims guidance",FTC)],
    figures=[('bagged-chews-with-desiccant.jpg','Coffee wood chews in a sealed bag with a desiccant sachet','The toy, the bag, the box and any ink are four separate claims, not one.'),('loofah-duck-cat-toy.jpg','Loofah gourd fibre cut into a duck-shaped cat toy','Plant-derived is not the same as certified compostable.')])

add("are-dog-toys-biodegradable","Materials & claims",
    "Are Dog Toys Biodegradable? Read the Claim Closely",
    "What a biodegradable dog toy claim should cover, and how to check the product, test scope and disposal instructions before printing it.",
    "The important word in a biodegradability claim is often the one that is missing. Which part of the product? Under what conditions? Over what period? Without those details, the same label can mean very different things to a manufacturer, a retailer and the person disposing of the toy.",
    [
    ("Follow the claim to the actual article",p("A plain wood stick is not the same article as a wood stick joined to a rope, decorated with a label and sealed in film. Likewise, information about coconut husk fiber does not automatically describe a finished ball with binding or internal components. Begin with the complete construction of the SKU you intend to sell.")+
        p("The packaging needs its own review. Customers may discard the tag and bag immediately but keep the toy for much longer. Combining their disposal advice into one green symbol can leave both instructions unclear.")),
    ("What useful evidence looks like",p("A report should let your reviewer identify the tested sample, method, conditions, result and limitations. The product description or photograph should be specific enough to link the report to your order. A material supplier's general brochure is not the same as evidence covering your assembled product.")+
        p("If the report relates to a different size, color, adhesive or construction, ask whether that difference affects its applicability. This is a question for a competent reviewer or the testing body, not something to settle by changing the name on the cover page.")),
    ("Disposal conditions are part of the claim",p("Landfill, home composting and industrial composting are not interchangeable environments. A customer should not be told to bury a toy or put it into a local compost collection simply because its main material comes from a plant. Local acceptance and the evidence supporting the instruction both matter.")+
        p("The FTC's Green Guides are a useful starting point for understanding why unqualified degradability claims can mislead. For a particular market and label, have the proposed wording reviewed against the applicable requirements.")),
    ("Keep a claim file, not just a certificate folder",p("Save the final wording, the supporting evidence, the approved bill of materials and the artwork version together. Record who reviewed the claim and what changes would require another review. This is especially useful for repeat orders, when a packaging substitution can otherwise pass unnoticed.")+
        p("If the evidence does not support the desired claim, use a narrower description of the actual material. Customers can understand a clear material story without being given an unsupported disposal promise."))],
    ("Explore VietPaw's material collections","/materials/"),
    related=[("Plastic-free buying brief","/guides/plastic-free-biodegradable-pet-toys-guide/"),("Sustainability and packaging","/sustainability/")],
    sources=[("FTC guidance on degradable claims",FTC)],
    image="vietpaw-loofah-growing.png",
    figures=[('loofah-gourd-on-the-vine.jpg','A green loofah gourd hanging from its vine','Loofah is grown as a crop, so we do not describe it as agricultural waste.'),('marking-cartons-warehouse.jpg','Worker marking export cartons in a warehouse','Disposal claims need evidence for the finished assembly under stated conditions.')])

add("what-is-coconut-fiber-pet-toys","Materials & claims",
    "Coconut Fiber in Pet Toys: Texture, Construction and Quality",
    "Understand coconut coir pet toys, including ball construction, winding consistency, loose fiber and wholesale packing considerations.",
    "Coconut fiber, also called coir, comes from the husk around the coconut. In pet toys, its recognizable feature is the coarse, textured surface. That texture can be part of a product's appeal, but the material name alone tells a buyer surprisingly little about how a finished ball or rope is put together.",
    [
    ("Look beyond the outer layer",p("Two coir balls of the same diameter can differ in weight, winding and internal construction. One may have a core or additional binding that is not visible in the sales photograph. Ask for a full component description and, where useful, a construction sample that shows how the layers are assembled.")+
        p("Do not use coconut fiber and hemp interchangeably. They are different materials, even when both have a brown, rustic appearance. A material declaration is more reliable than matching the color of a rope to a catalogue image.")),
    ("A cat ball is not simply the smallest dog ball",p("Specify the intended pet and type of play. For a cat range, consider the dimensions, finished weight, surface construction and any added decoration. For a dog range, the same features still need review, but the intended carrying or fetch use may lead to a different design. Neither becomes suitable for forceful chewing just because it is labeled natural.")+
        p("The instructions should call for supervised play and removal of loose strands or damaged parts. If a design includes a bell, tail or other attachment, that component deserves its own inspection rather than being treated as a cosmetic extra.")),
    ("What to compare across a sample set",ul(["Diameter and finished weight, measured consistently rather than judged from a photograph.","Winding density and whether the shape holds consistently across the sample set.","Loose fiber, protruding ends and the security of any attachment.","Odor, visible contamination and the condition of the packing."])+
        p("Agree which natural differences are acceptable and which are defects. A range of brown shades is a different issue from an unapproved core or a poorly secured join.")),
    ("Think in cartons as well as individual balls",p("A loosely packed assortment and a retail multi-pack can have very different carton volumes. Confirm units per pack, packs per carton, carton dimensions and gross weight before comparing freight quotations. If several sizes share a carton, make the assortment visible on the packing list and carton marks.")+
        p("For repeat orders, retain the product and packing references together. Consistency at receiving depends on both."))],
    ("Coconut fiber wholesale collection","/collections/coconut-fiber/"),
    related=[("Cat ball specifications","/products/coconut-fiber-cat-ball/"),("Dog ball specifications","/products/coconut-fiber-dog-ball/")],
    image="vietpaw-coconut-fiber-balls.jpg",
    figures=[('vietpaw-coconut-fiber-balls.jpg','Hand holding several wound coconut fiber balls outdoors','Coir from the husk — a by-product of the coconut food and oil trade.'),('puppy-with-rope-and-fiber-ball.jpg','Puppy with a natural fiber ball and rope loop','Specify diameter and finished weight together; diameter alone hides a loosely wound batch.')])

add("non-toxic-cat-toys-wholesale-buying-guide","Materials & claims",
    "Buying Natural Cat Toys: What to Check Beyond Non-Toxic",
    "A wholesale guide to cat toy materials, small components, sample inspection, packaging and evidence behind non-toxic claims.",
    "Non-toxic is easy to put in a product description and difficult to interpret without context. It does not identify the material, explain how an attachment is secured or tell a buyer which substances were assessed. For a cat toy range, those details are more useful than the adjective on its own.",
    [
    ("Write down every component",p("A loofah shape may also include sewing thread, eyes, a hanging loop, a wand or a decorative tail. A coconut-fiber ball may contain a core or binding material. Ask for the complete list, including colors, coatings and any fragrance or catnip addition.")+
        p("Catnip should be specified as an ingredient or feature of a particular SKU, not assumed from a mouse-shaped photograph. The same applies to claims about an undyed or uncoated product: they should match the item and the manufacturing process being quoted.")),
    ("Inspect the small details that change during play",p("Review seams, knots and attachment points on the sample. Look for loose parts, exposed fastening elements and strands that may come away. A chemical assessment does not answer these physical-construction questions.")+
        p("Ask the supplier how those features will be checked during production. If an attachment test is part of the requirement, agree its method and acceptance criteria. Keep the approved construction with the reference sample so a later substitution is easy to identify.")),
    ("Make testing answer a defined question",p("Give the laboratory or compliance reviewer the complete product description and destination market. Ask what assessment is relevant to the actual construction and intended claims. Read the sample identification and report scope before treating a result as applicable to your order.")+
        p("A report for one material does not establish that every finished toy is non-toxic under every condition. Retailer requirements may also be more specific than the information supplied with a standard catalogue. Resolve that difference before approving artwork.")),
    ("Prepare the product for the store and the home",p("Show the intended play type and supervision advice clearly. Explain when damaged toys or loose components should be removed. Keep warnings readable on a small pack; reducing the type size until everything fits is not a useful solution.")+
        p("For wholesale orders, define whether a set is one saleable unit or several individually labeled items. That decision affects barcodes, pack counts and how a shop replaces a damaged unit. A well-specified cat range works for the receiving team as well as the customer."))],
    ("Browse VietPaw's natural cat toys","/cat-toys/"),
    related=[("Loofah product details","/products/loofah-cat-toy/"),("Testing and documentation","/certifications/")],
    image="vietpaw-loofah-play-shapes.png",
    figures=[('cat-loofah-toys-lifestyle.jpg','Cat playing with loofah toys on a rug','There is no universal pet-safety certification to carry — ask for the report that covers your SKU.'),('loofah-bear-shape-cat-toy.jpg','Loofah fibre cut into a bear-shaped cat toy','Confirm thread, filling and attachments before printing a composition claim.')])

add("sustainable-pet-toy-materials-compared","Materials & claims",
    "Coffee Wood, Coir, Hemp and Loofah: Choosing the Right Material",
    "Compare four natural pet toy materials by construction, product format, quality-control priorities and packaging requirements.",
    "The best material decision begins with the product you want to make. A shaped wood stick, a wound ball and a lightweight loofah figure do different jobs. Comparing them with a single eco score hides the design and purchasing decisions that will determine whether the finished item works for your range.",
    [
    ("Four materials, four different briefs",table(["Material","Typical format in the VietPaw range","Priority at sample approval"],[
        ("Coffee wood","Finished chew sticks and wood-and-rope combinations","Dimensions, surface finish, cracks and drying controls"),
        ("Coconut fiber / coir","Textured balls and fiber constructions","Winding, loose ends, complete construction and finished weight"),
        ("Hemp fiber","Rope, wound balls and knotted assemblies","Fiber declaration, rope diameter, knots and attachments"),
        ("Loofah","Lightweight cut shapes for cat play","Shape, thickness, edge finish and added components")])+
        p("The table is a buying guide, not a ranking of safety or durability. Suitability depends on the finished design and the pet, while an environmental comparison needs a defined scope and supporting information.")),
    ("Separate the origin story from the product claim",p("Coffee-tree wood and coconut husks offer specific material-use stories. Hemp and loofah are plant-derived, but that does not make every supply automatically a waste stream. If you want to say upcycled or waste-derived, ask what was sourced, from whom and at which stage.")+
        p("The full construction still matters. A hemp rope joined to wood is a mixed-material product, and a loofah shape with thread and decoration contains more than loofah. Describe those combinations accurately instead of extending a single-material claim across the whole toy.")),
    ("Compare the finished packed unit",p("Material choice affects size, weight and pack design. A light item in a bulky display box may use more shipping space than its weight suggests. Ask for the packed dimensions and carton arrangement while the design can still be changed.")+
        p("Review moisture protection and storage alongside the shelf appearance. The right answer may differ between a local retail delivery and a longer international shipment. The quotation should identify the proposed packing materials rather than simply calling them eco packaging.")),
    ("Use a sample range to make the decision",p("Choose a few products that have distinct uses and clear specifications. Compare their construction, how easily the label explains them and how they fit your intended retail price after landed costs. Avoid launching several near-identical variants before learning which size and format customers actually need.")+
        p("For a repeatable range, keep one approved file per SKU: component list, dimensions, sample photographs, packing details and label wording. That file is the link between a compelling material story and a product our factory can reproduce."))],
    ("Explore the four VietPaw material collections","/materials/"),
    related=[("Private-label development","/services/private-label-pet-toys/"),("Material and packaging claims","/sustainability/")],
    figures=[('loofah-drying-under-greenhouse-cover.jpg','Rows of loofah gourds drying under a greenhouse cover','Each material has a different, and differently provable, origin story.'),('coffee-wood-seasoning-racks.jpg','Rows of coffee wood sticks seasoning on factory drying racks','Coffee stem and coconut husk have genuine by-product stories. Hemp and loofah are grown crops.')])

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
    figures=[('coffee-wood-workshop-stacked-billets.jpg','Workshop interior with stacked coffee wood billets','Billets are cut to 50–70 cm in the field and held about a year in ventilated shade.'),('container-loading-forklift.jpg','Forklift loading pallets of cartons into a container','Loading port is Cat Lai, Ho Chi Minh City; 30–35 days port to port to the EU or the US.')])

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
        ("Grade","Pieces with cracks beyond 2 mm are removed at the grading bench.","Only graded pieces go to packing."),
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
    figures=[('coffee-wood-chew-finishing-bench.jpg','Row of workers shaping and finishing coffee wood chew sticks at benches','Shaping and surface finishing on our own line in the Central Highlands.'),('pallet-stack-inspection.jpg','Staff inspecting a stack of palletised export cartons','Buyer-arranged inspection is welcome — please arrange in advance so the line is running.')])

add("wholesale-coconut-fiber-cat-toys-supplier","Sourcing & trade",
    "Sourcing Coconut-Fiber Cat Toys for Wholesale",
    "Build a wholesale coconut-fiber cat toy assortment with clear size specifications, sample checks, pack counts and private-label requirements.",
    "A coconut-fiber cat ball may look like a simple purchase. The commercial details become more interesting once it is sold as a two-pack, assigned a barcode, packed into a mixed carton and shipped to a retailer. Defining that finished saleable unit early makes supplier quotations much easier to compare.",
    [
    ("Specify the ball before the bundle",p("Ask for diameter, finished weight and full construction. Identify the outer fiber, any core, binding thread and added decoration. If the supplier uses S, M and L, connect those labels to actual measurements. Size names are not standardized between manufacturers.")+
        p("Order samples of the sizes you intend to sell, not only one attractive catalogue example. Compare winding, shape, loose ends and consistency across the set. Keep the cat range separate from dog-ball size references and use instructions.")),
    ("Decide how the customer will buy it",p("Will each ball have a tag, or will several balls share one box? Is the assortment fixed, or can sizes be mixed? A retailer needs to know what one unit on the invoice means. The same definition should appear in the quotation, packing list and receiving instructions.")+
        p("For a private-label pack, approve the label size and attachment. Check that the barcode stays readable and that the customer can see supervision and replacement advice. If a pack is intended to contain several toys, specify its contents rather than accepting a loosely defined mixed assortment.")),
    ("Look at the carton while there is still time to change it",p("Ask for the number of retail units per carton, outer dimensions and gross weight. Fiber balls can occupy more space than their weight suggests, especially in rigid display packaging. Your forwarder needs the packed data, not the dimensions of one loose ball.")+
        p("Agree clean, dry packing and storage requirements with the supplier. At receiving, inspect the product and packaging condition together. Keep photographs of carton damage, affected units and identifying marks so a transport issue can be distinguished from a production defect.")),
    ("Use the first order to establish the reorder",p("A sensible trial is large enough to assess the chosen sizes and presentation, but narrow enough to review carefully. Track sales and returns by SKU. If customers favor one size or a pack creates confusion, revise that detail before expanding the range.")+
        p("When requesting a VietPaw quote, include your destination, quantity per size and preferred pack. Selected standard lines may support a small starting order; product and printed-packaging minimums still need to be confirmed separately."))],
    ("VietPaw coconut-fiber cat ball specifications","/products/coconut-fiber-cat-ball/"),
    related=[("Coconut-fiber material guide","/guides/what-is-coconut-fiber-pet-toys/"),("Wholesale supply","/services/wholesale-pet-products/")],
    image="vietpaw-coconut-fiber-balls.jpg",
    figures=[('cat-playing-with-loofah-shape.jpg','Grey cat reaching for a loofah play shape on a table','Write a cat specification, not a scaled-down dog one.'),('vietpaw-loofah-play-shapes.png','Loofah cat play shapes arranged in a basket','Each shape is measured separately — one size range does not cover the collection.')])

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
    figures=[('laser-engraving-coffee-wood-chew.jpg','Laser engraving head marking a logo onto a coffee wood chew stick','Engraving is burned into the wood — nothing to peel off during chewing. From 50 pcs.'),('bagged-chews-with-desiccant.jpg','Bagged coffee wood chews with a desiccant sachet ready for packing','Printed tags, labels and boxes start at 500 pcs per SKU — a separate minimum from engraving.')])

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
    figures=[('container-wall-of-cartons.jpg','A full wall of export cartons loaded and netted inside a shipping container','429 cartons in a 20 ft, 850 in a 40 ft. Pack format changes the count before it changes the price.'),('warehouse-inspection-clipboard.jpg','Warehouse staff checking stock against a document','Stock sizes ship in 5–7 days; printed packaging is the part that takes 60–80.')])

add("pet-toy-safety-compliance-cpsia-reach","Compliance & risk",
    "CPSIA, REACH and Pet Toys: Ask the Right Compliance Question",
    "How pet toy buyers should approach CPSIA and REACH discussions, including product classification, material scope and report relevance.",
    "A request for a CPSIA or REACH certificate can sound precise while leaving the essential question unanswered: which requirement applies to this particular product in its intended market? The starting point is the finished toy and how it will be sold, not the name of a certificate in a supplier's presentation.",
    [
    ("Do not classify a product by the word toy alone",p("CPSC's toy-safety business guidance addresses children's toys and the requirements connected with them. A product marketed for pets should not automatically be treated as a children's toy because both use the same everyday word. Equally, calling an item a pet toy does not by itself settle every applicable consumer-product obligation.")+
        p("Give your compliance reviewer the intended user, materials, design, packaging and marketing. Ask for an applicability review rather than copying a children's-toy compliance statement onto a pet product. Retailers may request particular test methods as a purchasing condition; distinguish that request from the legal classification.")),
    ("REACH questions follow the material and the article",p("ECHA explains that REACH restrictions can apply to substances in articles, including imported products. A plant-derived material is not a general exemption. Colors, coatings, adhesives and other components may be relevant to the assessment.")+
        p("Ask the reviewer which restrictions or other obligations need consideration for the actual composition and market. A report described as REACH tested is only useful once you know the sample, substances or requirements assessed, methods, results and limitations. It is not a universal approval for every item in a catalogue.")),
    ("Connect the evidence to the order",p("Check the report's product identification against the sample and bill of materials you approved. If the toy contains several components, ask which were included. A change in color, adhesive, rope or supplier may require a fresh scope review even when the finished item looks familiar.")+
        p("Keep the reviewed evidence with the SKU and artwork version. Shipment records, such as origin or treatment documents, serve different purposes and should not be presented as substitutes for a product assessment.")),
    ("Agree responsibilities before production",p("Identify who determines applicable requirements, who arranges testing, who pays and what happens if the result does not meet the agreed criteria. Put the required timing into the order plan so the shipment is not waiting on an unresolved assessment.")+
        p("CPSIA and REACH are not a complete worldwide compliance checklist. Requirements depend on destination, product and sales channel and can change. The importer and its qualified advisers should confirm the current position before approving the product and its claims."))],
    ("VietPaw testing and export-document information","/certifications/"),
    related=[("Planning a safety assessment","/guides/pet-toy-safety-testing-requirements/"),("Quality-control workflow","/quality-control/")],
    sources=[("CPSC toy-safety business guidance",CPSC),("ECHA: REACH restrictions",ECHA)],
    figures=[('inspection-documents-at-pallets.jpg','Two staff reviewing inspection documents beside stacked pallets','Compliance is decided per SKU and per destination, not per supplier.'),('export-container-exterior.jpg','Worker beside a green export container being loaded at a warehouse','Customs and marketplace checks are separate gates with separate paperwork.')])

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
    figures=[('two-inspectors-container-check.jpg','Two staff checking stacked export cartons inside a container','Ask the same verification questions of every origin: moisture, marks, stuffing, documents.'),('stacking-cartons-in-container.jpg','Worker stacking cartons inside a shipping container','Consolidation and container choice move landed cost more than unit price often does.')])

add("pet-toy-safety-testing-requirements","Compliance & risk",
    "Pet Toy Safety Testing: Build a Product-Specific Plan",
    "Prepare a useful pet toy assessment brief and distinguish laboratory testing, factory inspection and shipment documentation.",
    "A useful test plan begins with the ways a product could fail and the requirements of the market in which it will be sold. It does not begin with a request for every certificate the supplier has. The test sample, the approved product and the goods in the carton need to be recognizably the same construction.",
    [
    ("Give the reviewer a complete product",p("Provide the dimensions, intended pet and play type, component list and proposed label claims. Include photographs that show joins, knots, seams and attachments, not only a polished front view. Describe any coating, color, adhesive, filling or fragrance.")+
        p("Add the destination country and the retailer or marketplace requirements you have received. A laboratory can help assess an identified question; it cannot reliably infer your entire commercial brief from the phrase natural pet toy.")),
    ("Separate the kinds of assessment",p("Physical-construction review may consider edges, loose parts, knots, attachments and breakage. Material or chemical testing addresses specified substances or properties using defined methods. Factory inspection checks whether a production lot matches the agreed specification. These activities complement one another, but they are not interchangeable.")+
        p("A moisture reading belongs to a defined production-control method. A pull-test result needs its method, sample condition and acceptance limit. Neither number should be turned into a general safe-for-pets claim.")),
    ("Read the report beyond the result line",p("Check the sample description, report number, testing body, dates, methods and results. Look at exclusions and limitations. If your order adds a different thread, color or attachment, ask the reviewer whether the existing report still covers the changed product.")+
        p("Do not treat a report for one size or component as automatic coverage for the full range. Agree how variants will be grouped and assessed with the responsible specialist. Keep that rationale in the product file so the next buyer or quality manager can follow it.")),
    ("Plan the response to a failed check",p("Before production, decide who receives results, who approves corrective action and whether retesting or reinspection is needed. Allow time for that work in the launch schedule. It is much harder to resolve an ambiguous result when a freight booking is about to expire.")+
        p("At release, the file should connect the approved sample, current specification, relevant assessments and inspection decision. Keep shipment or treatment documents alongside it, but label them for their actual purpose. A document supporting movement of goods is not evidence for every product-safety claim."))],
    ("Discuss testing and documentation with VietPaw","/certifications/"),
    related=[("Drying and quality protocol with five QC checkpoints","/quality-control/"),("CPSIA and REACH scope","/guides/pet-toy-safety-compliance-cpsia-reach/")],
    image="vietpaw-moisture-check.jpg",
    figures=[('carton-quality-check.jpg','Worker examining corrugated board quality in a packing area','Test reports have a defined scope. Ask for the one covering your SKU and your destination.'),('moisture-meter-on-the-line.jpg','Pin-type moisture meter reading taken on coffee wood sticks','A moisture record is order-specific evidence; a general description is not.')])

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
    figures=[('inspector-checking-cartons-clipboard.jpg','Inspector in a hi-vis vest checking export cartons against a printed document','Ask for the carton marks to be photographed against the packing list before the container is sealed.'),('container-seal-applied.jpg','Hands fitting a numbered plastic seal to a shipping container door','The seal number belongs on your paperwork. It is the cheapest verification step there is.')])

add("coffee-wood-chew-size-guide","Natural chew toys",
    "Coffee Wood Chew Sizes: VietPaw's XS–XXL Reference",
    "Compare VietPaw CC01 coffee wood chew dimensions and reference weight bands, with advice on sample approval, labels and size selection.",
    "An M label is convenient for ordering, but it is not a measurement. When comparing coffee wood chews, use length, diameter and weight together. For pet suitability, the dog's mouth size, chewing behavior and dental condition still matter; the weight band is only a starting reference.",
    [
    ("The CC01 size reference",coffee_size_table()),
    ("Measure the product you are approving",p("Natural sticks do not have perfectly cylindrical outlines. Agree how length and diameter will be measured, what variation is acceptable and which reference identifies the size. Include the finished weight band in the specification so our factory and receiving team are using the same definition.")+
        p("For a first order, request the sizes you intend to sell and compare them side by side. Keep one approved reference per SKU. A photograph of the whole range is helpful for presentation but cannot replace individual measurements.")),
    ("Do not let a weight chart make the entire decision",p("A dog should not be able to swallow the chew whole. Beyond that basic dimension check, consider how it chews and whether a hard product is appropriate. Increasing the size does not remove the possibility of tooth damage or make a hard chew suitable for every strong chewer.")+
        p("For puppies, dogs with dental concerns or dogs that try to break off pieces, seek individual veterinary advice before using a hard chew. Do not treat XS as a puppy designation simply because it is the smallest product in the table.")),
    ("Keep the shelf label and purchase order aligned",p("Use the same size chart on the website, retail pack and quotation. If the specification changes, update those versions together. Combining weight bands from different historical charts can make two products with the same size name appear equivalent when they are not.")+
        p("For mixed cartons, show the quantity of each SKU clearly. A carton labeled assorted sizes is not enough if the warehouse needs to reconcile individual barcode counts or replenish separate retail lines.")),
    ("Size changes during use",p("The starting dimensions are not the final removal rule. Supervise use, inspect the product and remove it when damaged, cracked or worn down to a size that could be swallowed. Remove loose pieces promptly; coffee wood chews are not food.")+
        p("Put that advice near the size information. Owners need to understand both how to select a product and when the product they selected is no longer suitable for use."))],
    ("Coffee wood product specifications and sample options","/products/coffee-wood-dog-chew/"),
    related=[("Coffee wood suitability","/guides/are-coffee-wood-chews-safe-for-dogs/"),("Private-label pack development","/services/private-label-pet-toys/")],
    image="vietpaw-coffee-wood-sizes.png",
    figures=[('coffee-wood-chew-size-row.jpg','Coffee wood chew sticks laid out from smallest to largest','Six graded sizes. Length is cut to ±3 mm; diameter follows the natural stem and is graded into bands.'),('puppy-holding-coffee-wood-chew.jpg','Golden retriever puppy holding a coffee wood chew in its mouth',"Judge the fit against the dog's mouth, not against the size label.")])


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
