"""Two explicit opt-in enquiry flows. No tracking, subscription or automatic sends."""
from common import EMAIL

ENDPOINT = "https://formspree.io/f/mvkpbvlb"

def feedback(prefix, attachments=False):
    return f'''<p id="{prefix}-status" data-form-status class="small" role="status" aria-live="polite"></p>
<div id="{prefix}-error" data-form-error class="small form-error" role="alert" tabindex="-1" hidden>
<p data-error-message>Your enquiry could not be sent. Your entries have been kept.</p>
<p>Prefer email? Contact <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
{('<button type="button" class="btn btn-outline" data-without-attachment hidden>Continue without attachment</button>' if attachments else '')}
</div>'''

# Campaign attribution. Empty in the markup; assets/rfq.js copies any utm_* value from the
# landing URL so a lead can be credited to its channel. No cookies and no browser storage.
UTM_FIELDS = ("utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content")

def hidden_fields(prefix, subject, kind, utm=False):
    campaign = "".join(f'\n<input type="hidden" name="{field}" value="" data-utm="{field}">' for field in UTM_FIELDS) if utm else ""
    return f'''<input type="hidden" name="_subject" value="{subject}">
<input type="hidden" name="enquiry_type" value="{kind}" data-enquiry-kind>{campaign}
<div hidden aria-hidden="true"><label for="{prefix}-gotcha">Leave this field empty</label><input id="{prefix}-gotcha" name="_gotcha" tabindex="-1" autocomplete="off"></div>'''

BUYER_TYPES = ("Amazon seller", "Startup", "Eco shop", "Business owner", "Wholesale", "Importer", "Sourcing", "Other")
PRODUCT_INTERESTS = (("coffee_wood_chew", "Coffee wood chew"), ("coconut", "Coconut"), ("hemp", "Hemp"),
                     ("loofah", "Loofah"), ("other", "Other"))
# The single most useful qualifying answer: it decides whether the first reply can carry a
# price at all. "Not sure yet" is deliberately offered so the question never blocks a lead.
QUANTITY_BANDS = ("Samples only (under 50 pcs)", "50 – 499 pcs", "500 – 4,999 pcs",
                  "5,000 – 19,999 pcs", "20,000+ pcs or full container", "Not sure yet")
# A select instead of free text, so lead reporting by market stays countable.
FREQUENT_DESTINATIONS = ("United States", "Germany", "United Kingdom", "France", "Netherlands", "Canada",
                         "Australia", "Japan", "South Korea", "Spain", "Italy", "Poland", "Sweden")
COUNTRIES = (
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso",
    "Cambodia", "Cameroon", "Canada", "Chile", "China", "Colombia", "Costa Rica", "Croatia", "Cuba", "Cyprus",
    "Czechia", "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Estonia", "Ethiopia",
    "Fiji", "Finland", "France", "Georgia", "Germany", "Ghana", "Greece", "Guatemala", "Honduras",
    "Hong Kong SAR", "Hungary", "Iceland", "India", "Indonesia", "Iraq", "Ireland", "Israel", "Italy",
    "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos",
    "Latvia", "Lebanon", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau SAR", "Madagascar",
    "Malaysia", "Maldives", "Malta", "Mauritius", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro",
    "Morocco", "Mozambique", "Myanmar", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
    "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Paraguay",
    "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Rwanda", "Saudi Arabia", "Senegal",
    "Serbia", "Singapore", "Slovakia", "Slovenia", "South Africa", "South Korea", "Spain", "Sri Lanka",
    "Sweden", "Switzerland", "Taiwan", "Tanzania", "Thailand", "Trinidad and Tobago", "Tunisia", "Türkiye",
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan",
    "Venezuela", "Vietnam", "Zambia", "Zimbabwe",
)

def _options(values):
    return "".join(f'<option value="{v}">{v}</option>' for v in values)

def country_options():
    return ('<optgroup label="Frequent destinations">' + _options(FREQUENT_DESTINATIONS) + '</optgroup>'
            '<optgroup label="All countries">' + _options(COUNTRIES) + '</optgroup>'
            '<option value="Other / not listed">Other / not listed</option>')

def quote_form():
    product_boxes = "".join(
        f'<label class="check-option" for="rfq-product-{key}"><input type="checkbox" id="rfq-product-{key}" name="products" value="{label}" data-product-option> <span>{label}</span></label>'
        for key, label in PRODUCT_INTERESTS)
    return f'''<form id="rfq-form" class="card enquiry-form" data-enquiry-form="quote" action="{ENDPOINT}" method="post" data-success-url="/request-a-quote/thank-you/">
{hidden_fields("rfq", "VietPaw — samples and pricing enquiry", "samples_and_pricing", utm=True)}
<h2>Tell us about your project</h2>
<p class="small required-note">We usually reply within one business day with sample options, pricing and production timing. Fields marked * are required; everything else is optional.</p>
<div class="form-grid">
<fieldset class="field field-full check-group" data-product-interest><legend>What are you sourcing? * <span class="small">(select one or more)</span></legend>
<div class="check-options">{product_boxes}</div></fieldset>
<div class="field"><label for="rfq-quantity">Estimated first order quantity *</label><select id="rfq-quantity" name="est_quantity" required><option value="">Select a range</option>{_options(QUANTITY_BANDS)}</select><p class="small field-hint">A range is enough. It lets us put a price in the first reply instead of asking.</p></div>
<div class="field"><label for="rfq-buyer">What best describes you? *</label><select id="rfq-buyer" name="buyer_type" required><option value="">Select one</option>{_options(BUYER_TYPES)}</select></div>
<div class="field"><label for="rfq-country">Destination country *</label><select id="rfq-country" name="country" required><option value="">Select a country</option>{country_options()}</select></div>
<div class="field"><label for="rfq-company">Company / brand name</label><input id="rfq-company" name="company" autocomplete="organization" maxlength="180"><p class="small field-hint">Optional. If you are still setting up, write the brand name you plan to use.</p></div>
<div class="field field-full"><label for="rfq-message">Anything we should know? <span class="small">(packaging, certification, timeline)</span></label><textarea id="rfq-message" name="message" rows="4" maxlength="2000" placeholder="Tell us about packaging, certification or timeline requirements — anything that helps us quote accurately."></textarea></div>
<div class="field"><label for="rfq-name">Full name *</label><input id="rfq-name" name="name" autocomplete="name" required maxlength="120"></div>
<div class="field"><label for="rfq-email">Business email *</label><input id="rfq-email" name="email" type="email" autocomplete="email" required maxlength="254"></div>
<div class="field field-full"><label for="rfq-phone">Phone / WhatsApp</label><input id="rfq-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" maxlength="40" placeholder="Include country code, e.g. +49 …"><p class="small field-hint">Optional, and the fastest way to reach you. Email alone is fine.</p></div>
</div>
<div class="form-actions"><button class="btn btn-primary" type="submit">Get Samples &amp; Pricing</button></div>
<p class="small form-privacy">We use your details only to answer this enquiry. No newsletter, no third parties.</p>
{feedback("rfq")}
</form>'''

def catalogue_form():
    return f'''<form id="catalogue-form" class="card enquiry-form" data-enquiry-form="catalogue" action="{ENDPOINT}" method="post">
{hidden_fields("catalogue", "VietPaw — catalogue price list request", "catalogue_price_list")}
<h3>Want current MOQ &amp; pricing?</h3>
<p class="small">Request a price list for your market. This form is optional; the catalogue download is always available.</p>
<div class="form-grid">
<div class="field field-full"><label for="catalogue-email">Business email *</label><input id="catalogue-email" name="email" type="email" autocomplete="email" required maxlength="254"></div>
<div class="field field-full"><label for="catalogue-country">Country / destination *</label><input id="catalogue-country" name="country" autocomplete="country-name" required maxlength="100"></div>
<div class="field field-full"><label for="catalogue-buyer">Buyer type</label><select id="catalogue-buyer" name="segment"><option value="">Select if known</option><option>Pet brand</option><option>Wholesaler / distributor</option><option>Amazon seller</option><option>Retailer / eco pet shop</option><option>Startup brand</option><option>Other</option></select></div>
</div>
<div class="form-actions"><button class="btn btn-primary" type="submit">Send me the price list</button></div>
<p class="small form-privacy">We will reply with current terms relevant to your request, usually within one business day. No newsletter signup.</p>
{feedback("catalogue")}
</form>'''
