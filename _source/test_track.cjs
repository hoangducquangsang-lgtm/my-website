/* Mock-only analytics tests. Never contacts Google and never sends real buyer data. */
const fs = require("node:fs"), path = require("node:path"), vm = require("node:vm");
const assert = require("node:assert/strict");
const source = fs.readFileSync(path.join(__dirname, "../assets/track.js"), "utf8");

function setup(options = {}) {
  const sent = [], observers = [], docOn = {}, winOn = {};
  const form = { id: "rfq-form" };
  const document = {
    readyState: options.readyState || "complete",
    documentElement: { scrollHeight: 2000, scrollTop: 0 },
    body: { scrollHeight: 2000 },
    addEventListener: (type, cb) => { (docOn[type] = docOn[type] || []).push(cb); },
    querySelector: sel => {
      assert.equal(sel, 'form[data-enquiry-form]');
      return options.noForm ? null : form;
    }
  };
  const window = {
    document,
    location: { href: "https://vietpaw.com/request-a-quote/" },
    innerHeight: 500,
    pageYOffset: 0,
    addEventListener: (type, cb) => { (winOn[type] = winOn[type] || []).push(cb); },
    removeEventListener: (type, cb) => { winOn[type] = (winOn[type] || []).filter(f => f !== cb); }
  };
  if (!options.noObserver) window.IntersectionObserver = class {
    constructor(cb, opts) { this.cb = cb; this.opts = opts; observers.push(this); }
    observe(el) { this.el = el; }
    disconnect() { this.disconnected = true; }
  };
  if (!options.noGtag) window.gtag = (kind, name, params) => { sent.push({ kind, name, params }); };
  vm.runInNewContext(source, { window });
  const fire = (map, type, arg) => (map[type] || []).slice().forEach(cb => cb(arg));
  return { sent, window, document, form, observers, docOn, winOn,
    doc: (type, arg) => fire(docOn, type, arg),
    win: (type, arg) => fire(winOn, type, arg) };
}
const link = href => ({ target: { closest: sel => (assert.equal(sel, "a[href]"), { getAttribute: () => href }) } });
const LEAD = { detail: { form_id: "rfq-form", buyer_type: "Importer", country: "Germany",
  products: "Coffee wood chew, Hemp", enquiry_type: "samples_and_pricing" } };

// 1. A confirmed enquiry reports exactly one lead, with business fields only.
const lead = setup();
lead.doc("vietpaw:lead", LEAD);
assert.equal(lead.sent.length, 1, "one lead must not fan out into several key events");
assert.equal(lead.sent[0].kind, "event");
assert.equal(lead.sent[0].name, "generate_lead");
assert.deepEqual(Object.keys(lead.sent[0].params).sort(),
  ["buyer_type", "country", "enquiry_type", "form_id", "lead_source", "products"]);
assert.equal(lead.sent[0].params.country, "Germany");
assert.equal(lead.sent[0].params.lead_source, "website_form");
for (const personal of ["name", "email", "phone", "company"])
  assert.ok(!(personal in lead.sent[0].params), "personal data must never be a GA4 parameter: " + personal);

// request_sample stays off while enquiry_type cannot vary; see the note in track.js.
assert.ok(!lead.sent.some(e => e.name === "request_sample"));

// 2. A lead event with no detail must not throw and must still report.
const bare = setup();
bare.doc("vietpaw:lead", {});
assert.equal(bare.sent[0].name, "generate_lead");
assert.equal(bare.sent[0].params.country, "");

// 3. Contact clicks.
const clicks = setup();
clicks.doc("click", link("https://wa.me/84906111016"));
clicks.doc("click", link("mailto:sales@vietpaw.com"));
clicks.doc("click", link("/guides/"));
assert.deepEqual(clicks.sent.map(e => e.name), ["contact_whatsapp", "contact_email"]);
assert.equal(clicks.sent[0].params.page_location, "https://vietpaw.com/request-a-quote/");

// 4. form_view fires once, at half the form or more, then stops observing.
const view = setup();
assert.equal(view.observers.length, 1);
assert.deepEqual(Array.from(view.observers[0].opts.threshold), [0.5]);  // cross-realm array
view.observers[0].cb([{ isIntersecting: true, intersectionRatio: 0.2 }]);
assert.equal(view.sent.length, 0, "a form barely on screen is not a view");
view.observers[0].cb([{ isIntersecting: true, intersectionRatio: 0.6 }]);
view.observers[0].cb([{ isIntersecting: true, intersectionRatio: 0.9 }]);
assert.deepEqual(view.sent.map(e => e.name), ["form_view"]);
assert.equal(view.observers[0].disconnected, true);

// 5. No form on the page, or no IntersectionObserver: no observer, no error.
assert.equal(setup({ noForm: true }).observers.length, 0);
assert.doesNotThrow(() => setup({ noObserver: true }));

// 6. scroll_75 fires once and then detaches.
const scroll = setup();
scroll.window.pageYOffset = 500;   // 500 / (2000 - 500) = 33%
scroll.win("scroll");
assert.equal(scroll.sent.length, 0);
scroll.window.pageYOffset = 1200;  // 80%
scroll.win("scroll");
scroll.window.pageYOffset = 1400;
scroll.win("scroll");
assert.deepEqual(scroll.sent.map(e => e.name), ["scroll_75"]);
assert.equal((scroll.winOn.scroll || []).length, 0, "the scroll listener must detach itself");

// 7. A page shorter than the viewport must not report a scroll.
const short = setup();
short.document.documentElement.scrollHeight = 400;
short.document.body.scrollHeight = 400;
short.window.pageYOffset = 0;
short.win("scroll");
assert.equal(short.sent.length, 0);

// 8. Without the Google tag the module must stay silent instead of throwing.
const silent = setup({ noGtag: true });
assert.doesNotThrow(() => { silent.doc("vietpaw:lead", LEAD); silent.doc("click", link("https://wa.me/1")); });

// 9. Before the document is ready, work waits for DOMContentLoaded.
const early = setup({ readyState: "loading" });
assert.equal(early.observers.length, 0);
early.doc("DOMContentLoaded");
assert.equal(early.observers.length, 1);

// 10. The module must not touch browser storage.
assert.ok(!/localStorage|sessionStorage|document\.cookie/.test(source));

console.log("PASS: generate_lead (business fields only, no personal data, no fan-out), contact_whatsapp/contact_email, form_view at >=50% once, scroll_75 once, safe without gtag or IntersectionObserver, no storage.");
