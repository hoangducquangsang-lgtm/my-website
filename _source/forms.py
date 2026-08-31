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

def hidden_fields(prefix, subject, kind):
    return f'''<input type="hidden" name="_subject" value="{subject}">
<input type="hidden" name="enquiry_type" value="{kind}">
<div hidden aria-hidden="true"><label for="{prefix}-gotcha">Leave this field empty</label><input id="{prefix}-gotcha" name="_gotcha" tabindex="-1" autocomplete="off"></div>'''

def quote_form():
    return f'''<form id="rfq-form" class="card enquiry-form" data-enquiry-form="quote" action="{ENDPOINT}" method="post" enctype="multipart/form-data" data-success-url="/request-a-quote/thank-you/">
{hidden_fields("rfq", "VietPaw — samples and pricing enquiry", "samples_and_pricing")}
<h2>Tell us about your project</h2>
<p class="small required-note">Start with the five required fields. We usually reply within one business day with sample options, pricing and production timing. Fields marked * are required.</p>
<div class="form-grid">
<div class="field"><label for="rfq-name">Full name *</label><input id="rfq-name" name="name" autocomplete="name" required maxlength="120"></div>
<div class="field"><label for="rfq-email">Business email *</label><input id="rfq-email" name="email" type="email" autocomplete="email" required maxlength="254"></div>
<div class="field"><label for="rfq-company">Company *</label><input id="rfq-company" name="company" autocomplete="organization" required maxlength="180"></div>
<div class="field"><label for="rfq-country">Country / destination *</label><input id="rfq-country" name="country" autocomplete="country-name" required maxlength="100" placeholder="e.g. Germany"></div>
<div class="field field-full"><label for="rfq-products">Product interest *</label><textarea id="rfq-products" name="products" data-product-interest rows="3" maxlength="2500" required placeholder="Product name, material, size or catalogue reference"></textarea></div>
</div>
<details class="form-details"><summary>Optional project details</summary>
<div class="form-grid">
<div class="field"><label for="rfq-quantity">Estimated quantity</label><select id="rfq-quantity" name="quantity"><option value="">Not decided</option><option value="50-499">50–499</option><option value="500-4999">500–4,999</option><option value="5000+">5,000+</option></select></div>
<div class="field"><label for="rfq-service">Sourcing option</label><select id="rfq-service" name="service"><option value="">Please advise</option><option value="wholesale">Wholesale</option><option value="private_label">Private Label</option><option value="oem_odm">OEM / ODM</option></select></div>
<div class="field field-full"><label for="rfq-whatsapp">WhatsApp (including country code)</label><input id="rfq-whatsapp" name="whatsapp" type="tel" autocomplete="tel" maxlength="40" placeholder="+49 …"></div>
<div class="field field-full"><label for="rfq-message">Message</label><textarea id="rfq-message" name="message" rows="3" maxlength="4000" placeholder="Branding, packaging, target launch date or other requirements"></textarea></div>
<div class="field field-full"><label for="rfq-reference">Upload reference / design</label><input id="rfq-reference" name="attachment" type="file" data-attachment accept=".pdf,.jpg,.jpeg,.png,.webp" aria-describedby="rfq-file-note"><p id="rfq-file-note" class="small">One PDF, JPG, PNG or WebP file, up to 5 MB. Share only files you are authorized to send; please email confidential designs after agreeing a confidentiality process.</p></div>
</div></details>
<div class="form-actions"><button class="btn btn-primary" type="submit">Get Samples &amp; Pricing</button></div>
<p class="small form-privacy">We use your details to respond to this enquiry. This does not subscribe you to a newsletter.</p>
{feedback("rfq", attachments=True)}
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
