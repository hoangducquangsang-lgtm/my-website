"""Owner-authorized public copies of the four supplied Proof files.

Observed document names and dates are not authentication or proof of a relationship
between differently named entities. Downloadable PNGs preserve the supplied bytes;
responsive WebP images are display previews, not edited or reissued certificates.
"""
from html import escape
from urllib.parse import urlencode
from common import BRAND_RELATIONSHIP
from content_helpers import publish, section, p, ul, table

PROOF_RECORDS = [
    {
        "source": "CO.png", "title": "Certificate of Origin — Form VJ",
        "asset": "proof-co-form-vj.png",
        "status": "Historical reference · 2022",
        "scope": "The supplied copy describes wooden pet toys in a Vietnam–Japan origin document dated 2022.",
        "limit": "The exporter is written as WYNVN INT CO., LTD, not WINVN INT CO., LTD. The relationship between those names has not been verified. This copy is not presented as proof of origin for a current VietPaw order.",
    },
    {
        "source": "Fumigation Certificate.png", "title": "Fumigation Certificate",
        "asset": "proof-fumigation-2021.png",
        "status": "Historical reference · December 2021",
        "scope": "The supplied Vietnamcontrol copy records a fumigation treatment for a wooden-pet-toy shipment in December 2021.",
        "limit": "The visible copy does not identify WINVN INT CO., LTD as exporter. A treatment record relates to its named shipment; it does not establish current product safety or coverage of future orders.",
    },
    {
        "source": "Phytosanitary.png", "title": "Phytosanitary Certificate",
        "asset": "proof-phytosanitary-specimen.png",
        "status": "Illustrative specimen · not shipment proof",
        "scope": "The supplied file uses ABC company details and example fields, with a displayed date in May 2024.",
        "limit": "This is treated as an illustrative specimen, not an issued certificate for VietPaw or WINVN INT CO., LTD. Request the applicable shipment-specific record for your product and destination.",
    },
    {
        "source": "Surrendered.png", "title": "Bill of Lading — Surrendered Copy",
        "asset": "proof-surrendered-bl-2022.png",
        "status": "Historical reference · August 2022",
        "scope": "The supplied transport-document copy is marked SURRENDERED and displays an August 2022 issue date.",
        "limit": "The shipper is written as WYNVN INT CO., LTD. It is not presented as evidence that WINVN INT CO., LTD shipped the goods or that a current order has been released or delivered.",
    },
]


def build(root):
    cards = []
    for record in PROOF_RECORDS:
        query = urlencode({"product": "Proof request: " + record["title"] + ". Please confirm current documents for my product and destination."})
        original = "/assets/img/proof/" + record["asset"]
        alt = record["title"] + " — " + record["status"]
        scan = ('<figure class="proof-scan"><a href="'+original+'" aria-label="'+escape("Open original PNG: "+record["title"], quote=True)+'">'
                '<img src="'+original+'" alt="'+escape(alt, quote=True)+'" loading="lazy"></a>'
                '<figcaption>Full document shown without cropping. Select the image to read the original PNG.</figcaption></figure>')
        downloads = ('<div class="hero-ctas proof-actions"><a class="btn btn-outline" href="'+original+'">View full-size PNG</a>'
                     '<a class="btn btn-outline" href="'+original+'" download="'+record["asset"]+'">Download original PNG</a></div>')
        cards.append('<article class="card"><p class="tag">'+escape(record["status"])+
                     '</p><h3>'+escape(record["title"])+'</h3>'+scan+p(escape(record["scope"]))+
                     p('<strong>Scope limit:</strong> '+escape(record["limit"]))+
                     downloads+
                     p('<a href="/request-a-quote/?'+escape(query, quote=True)+'">Ask about current documentation</a>')+'</article>')
    publish(root, "/proof/", "Proof & Export Document References | VietPaw",
        "View and download supplied export-document examples, read their scope, and request current records for VietPaw orders manufactured by WINVN INT CO., LTD.",
        "Proof & Export Document References",
        "View the four supplied document images and download their original PNG copies. These are historical references or specimens, not a register of current certificates for every order.",
        [section("One commercial brand, one named legal manufacturer",
            p(BRAND_RELATIONSHIP)+table(["Role", "Name used for this website"], [
                ("Commercial / export brand", "VietPaw"), ("Legal manufacturer", "WINVN INT CO., LTD")])+
            p("A similar company name on an old document is not enough to establish the same legal entity. Check the contracting name, product, date and shipment details in the records prepared for your order.")),
         section("Supplied document register", '<div class="grid grid-2">'+"".join(cards)+'</div>', True),
         section("Request the evidence that matches your order", ul([
             "Current company registration and manufacturer details matching the contracting entity.",
             "The product reference, quantity and destination covered by the requested record.",
             "Certificate of Origin, Fumigation Certificate and Phytosanitary Certificate, subject to destination/product requirements.",
             "Commercial Invoice, Packing List and the relevant transport document, including Bill of Lading (B/L) for a sea shipment.",
             "Coffee wood batch moisture readings and agreed inspection records on request."])+
             p('For production controls, see <a href="/quality-control/">Quality Control</a>. For document applicability, see <a href="/certifications/">Testing & Export Documents</a>.')),
         section("Document access and verification", p("The four original PNG copies are publicly viewable and downloadable on this page at the website owner's request. They are reproduced as supplied: company names, dates, signatures, seals and existing blanked fields have not been changed. The responsive previews are optimized for display; download the PNG for the supplied original.")+
             p("The images and summaries do not authenticate signatures or seals, verify legal relationships, or turn a shipment record into a product-safety certificate. Different company names and specimen details remain visible so readers can assess the stated limits.")+
             p('<a class="btn btn-primary" href="/request-a-quote/?product=Proof%20request%3A%20current%20company%20and%20shipment%20documents">Request an Order-Specific Proof Pack</a>'), True)],
        active="Manufacturing", trail=[("Home", "/"), ("Manufacturing", "/capabilities/"), ("Proof", None)])
