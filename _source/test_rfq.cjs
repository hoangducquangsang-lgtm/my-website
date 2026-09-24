/* Mock-only enquiry tests. Never contact Formspree or send real buyer data. */
const fs = require("node:fs"), path = require("node:path"), vm = require("node:vm");
const assert = require("node:assert/strict");
const source = fs.readFileSync(path.join(__dirname, "../assets/rfq.js"), "utf8");
const PRODUCTS = ["Coffee wood chew", "Coconut", "Hemp", "Loofah"];

function setup(options = {}) {
  const href = options.href || "https://vietpaw.com/request-a-quote/?product=Coffee%20wood%20dog%20chew";
  const kind = options.kind || "quote", url = new URL(href), events = {}, calls = [], timers = new Map();
  const status = { textContent: "" }, errorText = { textContent: "" };
  const error = { hidden: true, focus() { this.focused = true; } };
  const button = { disabled: false, textContent: kind === "quote" ? "Get Samples & Pricing" : "Send me the price list", focus() {} };
  const boxes = kind === "quote" ? PRODUCTS.map(value => ({ value, checked: !!(options.checked || []).includes(value), validity: "",
    setCustomValidity(m) { this.validity = m; }, addEventListener(t, cb) { this["on" + t] = cb; } })) : [];
  const group = kind === "quote" ? { querySelectorAll: sel => { assert.equal(sel, "[data-product-option]"); return boxes; } } : null;
  const selectors = { "[data-form-status]": status, "[data-form-error]": error, "[data-error-message]": errorText,
    'button[type="submit"]': button, "[data-product-interest]": group, "[data-attachment]": null, "[data-without-attachment]": null };
  const fields = kind === "quote" ? {
    name: "Buyer & Team", email: "buyer+test@example.com", phone: "+491234", company: "", country: "Germany",
    buyer_type: "Importer", _subject: "VietPaw — samples and pricing enquiry", enquiry_type: "samples_and_pricing", _gotcha: ""
  } : { email: "buyer@example.com", country: "Germany", segment: "Wholesaler / distributor",
    _subject: "VietPaw — catalogue price list request", enquiry_type: "catalogue_price_list", _gotcha: "" };
  const form = {
    action: "https://formspree.io/f/mvkpbvlb",
    dataset: { enquiryForm: kind, ...(kind === "quote" ? { successUrl: options.successUrl || "/request-a-quote/thank-you/" } : {}) },
    querySelector: s => selectors[s],
    reportValidity: () => options.valid !== false && boxes.every(b => !b.validity),
    addEventListener: (type, cb) => { events[type] = cb; },
    setAttribute: (k, v) => { form[k] = v; }, removeAttribute: k => { delete form[k]; }
  };
  const window = { location: { href, search: url.search, origin: url.origin, protocol: url.protocol },
    setTimeout: cb => { timers.set(1, cb); return 1; }, clearTimeout: id => timers.delete(id) };
  class FormDataStub {
    constructor(target) { assert.equal(target, form); this.values = new Map(Object.entries(fields));
      this.values.set("products", boxes.filter(b => b.checked).map(b => b.value)); }
    delete(k) { this.values.delete(k); }
  }
  vm.runInNewContext(source, { window, URL, URLSearchParams, AbortController, FormData: FormDataStub,
    document: { querySelectorAll: s => { assert.equal(s, "form[data-enquiry-form]"); return [form]; } },
    fetch: async (target, args) => {
      calls.push({ target, args });
      if (typeof options.reply === "function") return options.reply(args, calls.length);
      if (options.reply === "reject") throw new TypeError("Offline");
      return { ok: !options.status || options.status === 200, status: options.status || 200 };
    } });
  return { form, window, calls, timers, status, error, button, boxes, submit: () => events.submit({ preventDefault() {} }) };
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
  for (const key of ["name", "email", "phone", "country", "buyer_type"]) assert.ok(sent.args.body.values.get(key));
  assert.deepEqual(sent.args.body.values.get("products"), ["Coffee wood chew"]);
  assert.equal(sent.args.body.values.get("company"), "", "company is optional");
  assert.equal(good.window.location.href, "https://vietpaw.com/request-a-quote/thank-you/");
  await good.submit(); assert.equal(good.calls.length, 1);

  const none = setup({ href: "https://vietpaw.com/request-a-quote/" });
  await none.submit(); assert.equal(none.calls.length, 0, "at least one product must be ticked");
  assert.match(none.boxes[0].validity, /Select at least one/);
  none.boxes[2].checked = true; none.boxes[2].onchange();
  assert.equal(none.boxes[0].validity, "");
  await none.submit(); assert.equal(none.calls.length, 1);

  const multi = setup({ href: "https://vietpaw.com/request-a-quote/?product=Hemp%20rope%20and%20coffee%20wood" });
  assert.deepEqual(multi.boxes.filter(b => b.checked).map(b => b.value), ["Coffee wood chew", "Hemp"]);
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
  console.log("PASS: phone + buyer type required, company optional, product checkboxes (prefill, at-least-one), no attachment, payloads, errors, timeouts, duplicate guards, redirects. No real submissions.");
})().catch(e => { console.error(e); process.exitCode = 1; });
