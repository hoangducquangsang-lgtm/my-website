/* Mock-only enquiry tests. Never contact Formspree or send real buyer data. */
const fs = require("node:fs"), path = require("node:path"), vm = require("node:vm");
const assert = require("node:assert/strict");
const source = fs.readFileSync(path.join(__dirname, "../assets/rfq.js"), "utf8");

function setup(options = {}) {
  const href = options.href || "https://vietpaw.com/request-a-quote/?product=Coffee%20wood";
  const kind = options.kind || "quote", url = new URL(href), events = {}, calls = [], timers = new Map();
  const status = { textContent: "" }, errorText = { textContent: "" };
  const error = { hidden: true, focus() { this.focused = true; } };
  const button = { disabled: false, textContent: kind === "quote" ? "Get Samples & Pricing" : "Send me the price list", focus() { this.focused = true; } };
  const products = kind === "quote" ? { value: options.existing || "", maxLength: 2500 } : null;
  const attachment = kind === "quote" ? { name: "attachment", files: options.file ? [options.file] : [] } : null;
  if (attachment) Object.defineProperty(attachment, "value", { set(v) { if (v === "") this.files = []; }, get() { return ""; } });
  const without = kind === "quote" ? { hidden: true, addEventListener(type, cb) { this[type] = cb; } } : null;
  const selectors = { "[data-form-status]": status, "[data-form-error]": error,
    "[data-error-message]": errorText, 'button[type="submit"]': button,
    "[data-product-interest]": products, "[data-attachment]": attachment, "[data-without-attachment]": without };
  const fields = kind === "quote" ? {
    name: "Buyer & Team", email: "buyer+test@example.com", company: "Example Co.", country: "Germany",
    quantity: "500-4999", service: "private_label", whatsapp: "+491234", message: "Launch in November",
    _subject: "VietPaw — samples and pricing enquiry", enquiry_type: "samples_and_pricing", _gotcha: ""
  } : { email: "buyer@example.com", country: "Germany", segment: "Wholesaler / distributor",
    _subject: "VietPaw — catalogue price list request", enquiry_type: "catalogue_price_list", _gotcha: "" };
  const form = {
    action: "https://formspree.io/f/mvkpbvlb",
    dataset: { enquiryForm: kind, ...(kind === "quote" ? { successUrl: options.successUrl || "thank-you/" } : {}) },
    querySelector: selector => selectors[selector], reportValidity: () => options.valid !== false,
    addEventListener: (type, cb) => { events[type] = cb; },
    setAttribute: (key, value) => { form[key] = value; }, removeAttribute: key => { delete form[key]; }
  };
  const window = { location: { href, search: url.search, origin: url.origin, protocol: url.protocol },
    setTimeout: cb => { timers.set(1, cb); return 1; }, clearTimeout: id => timers.delete(id) };
  class FormDataStub {
    constructor(target) {
      assert.equal(target, form);
      this.values = new Map(Object.entries(fields));
      if (products) this.values.set("products", products.value);
      if (attachment) this.values.set("attachment", attachment.files[0] || { name: "", size: 0 });
    }
    delete(key) { this.values.delete(key); }
  }
  vm.runInNewContext(source, {
    window, URL, URLSearchParams, AbortController, FormData: FormDataStub,
    document: { querySelectorAll: selector => { assert.equal(selector, "form[data-enquiry-form]"); return [form]; } },
    fetch: async (target, args) => {
      calls.push({ target, args });
      if (typeof options.reply === "function") return options.reply(args, calls.length);
      if (options.reply === "reject") throw new TypeError("Offline");
      return { ok: !options.status || options.status === 200, status: options.status || 200 };
    }
  });
  return { form, window, calls, timers, status, error, errorText, button, products, attachment, without,
    submit: () => events.submit({ preventDefault() {} }) };
}
(async () => {
  const good = setup();
  assert.equal(good.calls.length, 0);
  assert.equal(good.products.value, "Coffee wood");
  await good.submit();
  const sent = good.calls[0];
  assert.equal(sent.target, "https://formspree.io/f/mvkpbvlb");
  assert.equal(sent.args.method, "POST");
  assert.equal(sent.args.headers.Accept, "application/json");
  assert.ok(!("Content-Type" in sent.args.headers), "Browser must generate multipart boundary");
  for (const key of ["name", "email", "company", "country", "products", "quantity", "service", "whatsapp", "message"]) assert.ok(sent.args.body.values.get(key));
  assert.equal(sent.args.body.values.get("enquiry_type"), "samples_and_pricing");
  assert.ok(!sent.args.body.values.has("attachment"));
  assert.equal(good.window.location.href, "https://vietpaw.com/request-a-quote/thank-you/");
  await good.submit(); assert.equal(good.calls.length, 1);

  for (const options of [{status: 400}, {status: 429}, {reply: "reject"}]) {
    const failed = setup(options), original = failed.window.location.href;
    await failed.submit();
    assert.equal(failed.window.location.href, original);
    assert.equal(failed.button.disabled, false);
    assert.equal(failed.button.textContent, "Get Samples & Pricing");
    assert.equal(failed.error.hidden, false); assert.equal(failed.error.focused, true);
    assert.equal(failed.products.value, "Coffee wood");
    assert.equal(failed.form["aria-busy"], undefined); assert.equal(failed.timers.size, 0);
    await failed.submit(); assert.equal(failed.calls.length, 2);
    if (options.status === 429) assert.match(failed.status.textContent, /wait before trying/);
  }
  const invalid = setup({valid:false}); await invalid.submit(); assert.equal(invalid.calls.length, 0);
  let resolve;
  const pending = setup({reply: () => new Promise(done => { resolve=done; })});
  const first = pending.submit(); await pending.submit(); assert.equal(pending.calls.length, 1);
  assert.equal(pending.button.disabled, true); resolve({ok:true,status:200}); await first;

  const timeout = setup({reply: ({signal}) => new Promise((_,reject) => {
    signal.addEventListener("abort",() => reject(Object.assign(new Error(),{name:"AbortError"})));
  })});
  const waiting=timeout.submit(); timeout.timers.get(1)(); await waiting;
  assert.match(timeout.status.textContent,/could not confirm delivery/);
  assert.equal(timeout.button.disabled,false);

  for (const file of [{name:"bad.exe",size:100}, {name:"large.pdf",size:6*1024*1024}, {name:"empty.jpg",size:0}]) {
    const upload=setup({file}); await upload.submit(); assert.equal(upload.calls.length,0);
    assert.equal(upload.without.hidden,false); upload.without.click(); assert.equal(upload.calls.length,0);
    await upload.submit(); assert.equal(upload.calls.length,1); assert.ok(!upload.calls[0].args.body.values.has("attachment"));
  }
  const file = {name:"reference.PDF",size:1024};
  const upload = setup({file}); await upload.submit();
  assert.equal(upload.calls[0].args.body.values.get("attachment"),file);
  const rejected = setup({file,reply:(_,n)=>({ok:n>1,status:n>1?200:422})});
  await rejected.submit(); assert.equal(rejected.without.hidden,false); rejected.without.click();
  assert.equal(rejected.calls.length,1); await rejected.submit(); assert.equal(rejected.calls.length,2);

  const catalogue = setup({kind:"catalogue",href:"https://vietpaw.com/wholesale-catalogue/"});
  const catalogueUrl=catalogue.window.location.href;
  await catalogue.submit(); assert.equal(catalogue.window.location.href,catalogueUrl);
  assert.match(catalogue.status.textContent,/price-list request/);
  assert.equal(catalogue.calls[0].args.body.values.get("enquiry_type"),"catalogue_price_list");
  await catalogue.submit(); assert.equal(catalogue.calls.length,1);

  const local=setup({href:"file:///D:/Site/request-a-quote/index.html?product=Hemp"});
  await local.submit(); assert.equal(local.window.location.href,"file:///D:/Site/request-a-quote/thank-you/index.html");
  const safe=setup({successUrl:"https://example.org/"}); const original=safe.window.location.href;
  await safe.submit(); assert.equal(safe.window.location.href,original);
  const hostile=setup({href:"https://vietpaw.com/request-a-quote/?product="+encodeURIComponent("<script>alert(1)</script>")});
  assert.equal(hostile.products.value,"<script>alert(1)</script>"); assert.ok(!("innerHTML" in hostile.products));
  assert.equal(setup({existing:"My edited brief"}).products.value,"My edited brief");
  assert.equal(setup({href:"https://vietpaw.com/request-a-quote/?product="+"a".repeat(3000)}).products.value.length,2500);
  assert.ok(!/localStorage|sessionStorage|gtag\(/.test(source));
  console.log("PASS: quote/catalogue payloads, no automatic sends, required validation, file checks and explicit file-free retry, timeout, network errors, rate limits, duplicate guards, clean/local redirects and safe prefill. No real submissions.");
})().catch(error=>{console.error(error);process.exitCode=1;});
