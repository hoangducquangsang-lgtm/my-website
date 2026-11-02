/* Mock-only enquiry tests. Never contact Formspree or send real buyer data. */
const fs = require("node:fs"), path = require("node:path"), vm = require("node:vm");
const assert = require("node:assert/strict");
const source = fs.readFileSync(path.join(__dirname, "../assets/rfq.js"), "utf8");
const PRODUCTS = ["Coffee wood chew", "Coconut", "Hemp", "Loofah"];

function setup(options = {}) {
  const href = options.href || "https://vietpaw.com/request-a-quote/?product=Coffee%20wood%20dog%20chew";
  const kind = options.kind || "quote", url = new URL(href), events = {}, calls = [], timers = new Map();
  const leads = [];
  const status = { textContent: "" }, errorText = { textContent: "" };
  const error = { hidden: true, focus() { this.focused = true; } };
  const button = { disabled: false, textContent: kind === "quote" ? "Get Samples & Pricing" : "Send me the price list", focus() {} };
  const boxes = kind === "quote" ? PRODUCTS.map(value => ({ value, checked: !!(options.checked || []).includes(value), validity: "",
    setCustomValidity(m) { this.validity = m; }, addEventListener(t, cb) { this["on" + t] = cb; } })) : [];
  const group = kind === "quote" ? { querySelectorAll: sel => { assert.equal(sel, "[data-product-option]"); return boxes; } } : null;
  const UTM = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"];
  const utmFields = UTM.map(name => ({ value: "", dataset: { utm: name } }));
  const kindField = { value: kind === "quote" ? "samples_and_pricing" : "catalogue_price_list" };
  const selectors = { "[data-form-status]": status, "[data-form-error]": error, "[data-error-message]": errorText,
    'button[type="submit"]': button, "[data-product-interest]": group, "[data-attachment]": null,
    "[data-without-attachment]": null, "[data-enquiry-kind]": kindField };
  const fields = kind === "quote" ? {
    name: "Buyer & Team", email: "buyer+test@example.com", phone: "+491234", company: "", country: "Germany",
    buyer_type: "Importer", est_quantity: "500 – 4,999 pcs", message: "", _subject: "VietPaw — samples and pricing enquiry",
    enquiry_type: "samples_and_pricing", _gotcha: ""
  } : { email: "buyer@example.com", country: "Germany", segment: "Wholesaler / distributor",
    _subject: "VietPaw — catalogue price list request", enquiry_type: "catalogue_price_list", _gotcha: "" };
  const form = {
    action: "https://formspree.io/f/mvkpbvlb",
    dataset: { enquiryForm: kind, ...(kind === "quote" ? { successUrl: options.successUrl || "/request-a-quote/thank-you/" } : {}) },
    querySelector: s => selectors[s],
    querySelectorAll: s => (s === "[data-utm]" ? utmFields : []),
    reportValidity: () => options.valid !== false && boxes.every(b => !b.validity),
    addEventListener: (type, cb) => { events[type] = cb; },
    dispatchEvent: event => { leads.push(event); return true; },
    setAttribute: (k, v) => { form[k] = v; }, removeAttribute: k => { delete form[k]; }
  };
  const window = { location: { href, search: url.search, origin: url.origin, protocol: url.protocol },
    setTimeout: cb => { timers.set(1, cb); return 1; }, clearTimeout: id => timers.delete(id) };
  class FormDataStub {
    constructor(target) { assert.equal(target, form); this.values = new Map(Object.entries(fields));
      this.values.set("products", boxes.filter(b => b.checked).map(b => b.value)); }
    delete(k) { this.values.delete(k); }
    get(k) { const v = this.values.get(k); return Array.isArray(v) ? (v.length ? v[0] : null) : (v === undefined ? null : v); }
    getAll(k) { const v = this.values.get(k); return v === undefined ? [] : (Array.isArray(v) ? v.slice() : [v]); }
  }
  class CustomEventStub {
    constructor(type, init) { const o = init || {}; this.type = type; this.detail = o.detail; this.bubbles = !!o.bubbles; }
  }
  window.CustomEvent = CustomEventStub;
  vm.runInNewContext(source, { window, URL, URLSearchParams, AbortController, FormData: FormDataStub,
    document: { querySelectorAll: s => { assert.equal(s, "form[data-enquiry-form]"); return [form]; } },
    fetch: async (target, args) => {
      calls.push({ target, args });
      if (typeof options.reply === "function") return options.reply(args, calls.length);
      if (options.reply === "reject") throw new TypeError("Offline");
      return { ok: !options.status || options.status === 200, status: options.status || 200 };
    } });
  return { form, window, calls, timers, status, error, button, boxes, leads, utmFields, kindField,
    submit: () => events.submit({ preventDefault() {} }) };
}
(async () => {
  const good = setup();
  assert.equal(good.calls.length, 0);
  assert.deepEqual(good.boxes.filter(b => b.checked).map(b => b.value), ["Coffee wood chew"]);
  await good.submit();
  const sent = good.calls[0];
  assert.equal(sent.target, "https://formspree.io/f/mvkpbvlb");
  assert.equal(sent.args.method, "POST");
  assert.equal(sent.args.headers.Accept, "application/json");
  for (const key of ["name", "email", "country", "buyer_type", "est_quantity"]) assert.ok(sent.args.body.values.get(key));
  assert.equal(sent.args.body.values.get("message"), "", "the free-text field is optional");
  assert.deepEqual(sent.args.body.values.get("products"), ["Coffee wood chew"]);
  assert.equal(sent.args.body.values.get("company"), "", "company is optional");
  assert.equal(good.window.location.href, "https://vietpaw.com/request-a-quote/thank-you/");
  assert.equal(good.leads.length, 1, "one lead event per accepted submission");
  const lead = good.leads[0];
  assert.equal(lead.type, "vietpaw:lead");
  assert.equal(lead.bubbles, true, "must reach the document-level listener");
  assert.deepEqual(Object.keys(lead.detail).sort(),
    ["buyer_type", "country", "enquiry_type", "est_quantity", "form_id", "products"]);
  assert.equal(lead.detail.est_quantity, "500 – 4,999 pcs");
  assert.equal(lead.detail.country, "Germany");
  assert.equal(lead.detail.buyer_type, "Importer");
  assert.equal(lead.detail.products, "Coffee wood chew");
  assert.equal(lead.detail.enquiry_type, "samples_and_pricing");
  const reported = JSON.stringify(lead.detail);
  for (const personal of ["Buyer & Team", "buyer+test@example.com", "+491234"])
    assert.ok(!reported.includes(personal), "personal data must never reach analytics: " + personal);
  await good.submit(); assert.equal(good.calls.length, 1);
  assert.equal(good.leads.length, 1, "a blocked duplicate submit must not report a second lead");

  const campaign = setup({ href: "https://vietpaw.com/request-a-quote/?request=sample&product=Loofah&utm_source=linkedin&utm_medium=social&utm_campaign=eco_chews" });
  assert.deepEqual(campaign.utmFields.map(f => f.value), ["linkedin", "social", "eco_chews", "", ""]);
  assert.equal(campaign.kindField.value, "sample_request", "a sample CTA must be distinguishable from a pricing enquiry");
  const plain = setup({ href: "https://vietpaw.com/request-a-quote/?product=Loofah" });
  assert.deepEqual(plain.utmFields.map(f => f.value), ["", "", "", "", ""]);
  assert.equal(plain.kindField.value, "samples_and_pricing");

  const none = setup({ href: "https://vietpaw.com/request-a-quote/" });
  await none.submit(); assert.equal(none.calls.length, 0, "at least one product must be ticked");
  assert.match(none.boxes[0].validity, /Select at least one/);
  none.boxes[2].checked = true; none.boxes[2].onchange();
  assert.equal(none.boxes[0].validity, "");
  await none.submit(); assert.equal(none.calls.length, 1);

  const multi = setup({ href: "https://vietpaw.com/request-a-quote/?product=Hemp%20rope%20and%20coffee%20wood" });
  assert.deepEqual(multi.boxes.filter(b => b.checked).map(b => b.value), ["Coffee wood chew", "Hemp"]);
  await multi.submit();
  assert.equal(multi.leads[0].detail.products, "Coffee wood chew, Hemp", "every ticked product is reported");
  const loofah = setup({ href: "https://vietpaw.com/request-a-quote/?product=Loofah%20cat%20toy" });
  assert.deepEqual(loofah.boxes.filter(b => b.checked).map(b => b.value), ["Loofah"]);
  const hostile = setup({ href: "https://vietpaw.com/request-a-quote/?product=" + encodeURIComponent("<script>alert(1)</script>") });
  assert.equal(hostile.boxes.filter(b => b.checked).length, 0);

  for (const options of [{ status: 400 }, { status: 429 }, { reply: "reject" }]) {
    const failed = setup(options), original = failed.window.location.href;
    await failed.submit();
    assert.equal(failed.window.location.href, original);
    assert.equal(failed.button.disabled, false);
    assert.equal(failed.button.textContent, "Get Samples & Pricing");
    assert.equal(failed.error.hidden, false); assert.equal(failed.error.focused, true);
    assert.equal(failed.form["aria-busy"], undefined); assert.equal(failed.timers.size, 0);
    await failed.submit(); assert.equal(failed.calls.length, 2);
    assert.equal(failed.leads.length, 0, "a failed send is not a lead");
    if (options.status === 429) assert.match(failed.status.textContent, /wait before trying/);
  }
  const invalid = setup({ valid: false }); await invalid.submit(); assert.equal(invalid.calls.length, 0);
  let resolve;
  const pending = setup({ reply: () => new Promise(done => { resolve = done; }) });
  const first = pending.submit(); await pending.submit(); assert.equal(pending.calls.length, 1);
  assert.equal(pending.button.disabled, true); resolve({ ok: true, status: 200 }); await first;
  const timeout = setup({ reply: ({ signal }) => new Promise((_, reject) => {
    signal.addEventListener("abort", () => reject(Object.assign(new Error(), { name: "AbortError" }))); }) });
  const waiting = timeout.submit(); timeout.timers.get(1)(); await waiting;
  assert.match(timeout.status.textContent, /could not confirm delivery/);

  const catalogue = setup({ kind: "catalogue", href: "https://vietpaw.com/wholesale-catalogue/" });
  const catalogueUrl = catalogue.window.location.href;
  await catalogue.submit(); assert.equal(catalogue.window.location.href, catalogueUrl);
  assert.match(catalogue.status.textContent, /price-list request/);
  assert.equal(catalogue.calls[0].args.body.values.get("enquiry_type"), "catalogue_price_list");

  const local = setup({ href: "file:///D:/Site/request-a-quote/index.html?product=Hemp", successUrl: "thank-you/" });
  await local.submit(); assert.equal(local.window.location.href, "file:///D:/Site/request-a-quote/thank-you/index.html");
  const safe = setup({ successUrl: "https://example.org/" }); const original = safe.window.location.href;
  await safe.submit(); assert.equal(safe.window.location.href, original);
  assert.ok(!/localStorage|sessionStorage|gtag\(/.test(source));
  console.log("PASS: quantity + buyer type required, phone and company optional, utm capture, sample vs pricing enquiry, product checkboxes (prefill, at-least-one), no attachment, payloads, errors, timeouts, duplicate guards, redirects, lead event (business fields only, never on failure). No real submissions.");
})().catch(e => { console.error(e); process.exitCode = 1; });
