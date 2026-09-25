# -*- coding: utf-8 -*-
"""Gorilla line — thick-cut coffee wood chews for strong chewers (owner instruction 2026-09-25)."""
from content_helpers import (section, p, ul, answer, fit, steps, spec_table, figure, media, SAFETY, MOISTURE,
                             CAFFEINE, GORILLA, PAYMENT, SEA_TRANSIT)

IMG = "/assets/img/"

GORILLA_ROWS = [
    ("GRLS","5–6 × 8","155–230","60","9.3–13.8"),
    ("GRLM","6–8 × 10","260–350","52","13.5–18.2"),
    ("GRLL","8–10 × 12","350–480","40","14.0–19.2"),
    ("GRLXL","10–12 × 15","550–900","Built to a target carton weight","Confirmed per order"),
]

GORILLA_ENTRY = dict(name="Gorilla Coffee Wood Dog Chew",material="Coffee wood",collection="coffee-wood",group="Coffee Wood",
 image="process-raw-sticks.jpg",size="GRLS–GRLXL; four thick-cut sizes",moq="From 50 pcs per SKU; 500 pcs with your own label.",
 lede="Thick-cut coffee wood chews for strong chewers — the same untreated coffee wood as our stick range, cut short and thick. Four sizes from GRLS (155–230 g) to GRLXL (550–900 g).",
 overview="",options=[],checks=[])

def gorilla_sections(specifications):
    return [
    section("What the Gorilla line is",
        answer("The Gorilla line is VietPaw’s thick-cut coffee wood chew for strong chewers. It is the same coffee wood as our standard "
               "stick range, cut short and thick instead of long and slender, in four sizes from GRLS (5–6 × 8 cm, 155–230 g) to GRLXL "
               "(10–12 × 15 cm, 550–900 g). Nothing is added to it, and nothing is done to it that is not done to a standard stick.")
        + p("Choose Gorilla when a dog gets through a standard chew within a weekend. For moderate chewers, the standard CC01 stick range "
            "(XS–XXL) remains the better fit — see the <a href=\"/products/coffee-wood-dog-chew/\">coffee wood dog chew</a> page.")
        + media(ul([
            "<strong>Thick-cut.</strong> Diameter, not length, is what a strong chewer works against.",
            "<strong>One material.</strong> Untreated coffee wood — no glue, coating, preservative or colouring.",
            "<strong>Dried and graded.</strong> Below 14% moisture on every batch; any cracked piece is rejected.",
            "<strong>Not food.</strong> A chew toy for supervised use.",
        ]), IMG+"thick-coffee-wood-chews-vacuum-pack.jpg",
            "Thicker coffee wood pieces vacuum-packed at our warehouse",
            "Coffee wood from our line, vacuum-packed. Gorilla pieces are cut from the thickest stems.")),

    section("Why diameter matters more than length",
        p("A wood chew stops working for a strong chewer when the dog can get a molar around it and lever rather than gnaw. What decides "
          "that is not length or weight but how far across the piece is at its thickest. A longer standard stick adds little; a thicker "
          "piece changes how the dog has to work at it.")
        + p("That is why Gorilla is a separate line rather than a bigger size on the CC01 ladder. Material volume rises sharply with diameter, "
            "so a Gorilla piece carries several times the wood of a standard stick of similar length."), True),

    section("Gorilla sizes and carton data",
        spec_table(["SKU","Dimensions (cm)","Weight per piece (g)","Pieces per carton","Carton weight (kg)"],GORILLA_ROWS,
            caption="Reference specification. Coffee wood is natural: outline, grain and mass vary within each size. Carton counts are "
                    "planning references — confirm the packed data for your order.")
        + p("GRLXL is the most requested size; GRLL is the lower-cost entry point for a first order.")
        + specifications),

    section("Who it is for",
        fit(["Dogs that finish a standard coffee wood stick within a weekend.",
             "Strong, persistent chewers that need more wood per piece.",
             "Retailers who want one clear strong-chewer answer on the shelf.",
             "Amazon and marketplace sellers who need a thick, giftable chew."],
            ["Moderate gnawers — the standard CC01 stick is the better fit.",
             "Puppies and dogs with dental conditions — ask a vet first.",
             "Customers who want an edible chew — this is a toy, not food.",
             "Unsupervised use — check the chew before each session."],
            suit_head="Choose Gorilla for", less_head="Choose something else for"), True),

    section("Ordering Gorilla, step by step",
        steps([
            ("Pick the sizes","Most buyers start with GRLL and GRLXL; add GRLM for medium dogs.","A short, clear strong-chewer range."),
            ("Request samples","3 free samples; you cover the courier.","Pieces to weigh and measure against the table."),
            ("Choose the pack","Bulk, individual pack, or your own label or box (from 500 pcs per SKU).","A saleable unit that matches your channel."),
            ("Confirm carton data","Especially for Amazon FBA — see below.","Cartons that pass inbound limits."),
            ("Release production","30% deposit for stock packaging, 50% for your own label.","Balance against shipping documents."),
        ])),

    section("Amazon FBA and carton weights",
        p("Standard Gorilla cartons for GRLS, GRLM and GRLL stay within Amazon’s 50 lb (22.7 kg) single-carton inbound limit. GRLXL "
          "pieces range from 550 to 900 g, so a fixed count can push a carton over the limit; for FBA shipments GRLXL cartons are built to a "
          "target weight rather than a fixed count. Tell us the channel when you request a quote.")
        + p(SEA_TRANSIT), True),

    section("Quality, moisture and documents",
        ul([MOISTURE,
            "Any cracked piece is rejected at grading. Roughly one piece in five is removed across the whole process.",
            "Seven export documents ship with every order, including phytosanitary and fumigation certificates and a Certificate of Origin.",
            "Buyer visits and third-party inspection are welcome at our factories."])
        + p(CAFFEINE)
        + p(SAFETY)),
    ]

GORILLA_FAQ = [
    ("What is the Gorilla coffee wood chew?",
     "A thick-cut coffee wood chew for strong chewers — the same untreated coffee wood as our stick range, cut short and thick, in four sizes "
     "from GRLS (155–230 g) to GRLXL (550–900 g)."),
    ("Which Gorilla size should I choose?",
     "Choose a piece that stays much larger than the dog’s mouth throughout use. GRLXL (10–12 × 15 cm) is the most requested size; GRLL "
     "(8–10 × 12 cm) is the lower-cost entry point."),
    ("How is Gorilla different from an XXL stick?",
     "Gorilla is cut much thicker. For a strong chewer, diameter matters more than length, so a Gorilla piece gives far more wood to work "
     "through than a longer standard stick."),
    ("What is the minimum order?",
     "50 pcs per SKU in stock packaging; 500 pcs per SKU with your own label, hang tag or printed box."),
    ("Can I ship Gorilla chews to Amazon FBA?",
     "Yes. GRLS, GRLM and GRLL cartons stay within the 50 lb (22.7 kg) inbound limit; GRLXL cartons are built to a target weight for FBA."),
    ("Are samples free?",
     "Yes, 3 free samples; you cover the courier."),
]
