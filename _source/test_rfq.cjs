/* Offline behavior tests: fetch is mocked; never send a real enquiry. */
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const assert = require("node:assert/strict");
const source = fs.readFileSync(path.join(__dirname, "../assets/rfq.js"), "utf8");

function setup(options = {}) {
  const href = options.href || "https://vietpaw.com/request-a-quote/index.html?request=sample&product=Coffee%20wood";
  const events = {}, calls = [], timers = new Map();
  const controls = {
    "rfq-status": { textContent: "" },
    "form-error": { hidden: true, focus() { this.focused = true; } },
    "rfq-products": { value: options.existing || "", maxLength: 2500 }
  };
  const button = { disabled: false, textContent: "Send Enquiry" };
  const form = {
    action: "https://formspree.io/f/mvkpbvlb",
    dataset: { successUrl: "thank-you/index.html" },
    reportValidity: () => options.valid !== false,
    querySelector: () => button,
    addEventListener: (name, cb) => { events[name] = cb; },
    setAttribute: (name, value) => { form[name] = value; },
    removeAttribute: (name) => { delete form[name]; }
  };
  controls["rfq-form"] = form;
  const window = {
    location: { href, search: new URL(href).search },
    setTimeout: (cb) => { timers.set(1, cb); return 1; },
    clearTimeout: (id) => timers.delete(id)
  };
  class FormDataStub {
    constructor(target) {
      assert.equal(target, form);
      this.values = new Map([
        ["_subject", "New enquiry from WINVN website"], ["_gotcha", ""],
        ["name", "Buyer & Team"], ["company", "Test Co."],
        ["email", "buyer+test@example.com"], ["segment", "Startup brand"],
        ["products", controls["rfq-products"].value]
      ]);
    }
  }
  const context = {
    window, URL, URLSearchParams, AbortController, FormData: FormDataStub,
    document: { getElementById: id => controls[id] },
    fetch: async (url, args) => {
      calls.push({ url, args });
      if (typeof options.reply === "function") return options.reply(args);
      if (options.reply === "reject") throw new TypeError("Offline");
      return { ok: options.reply !== false };
    }
  };
  vm.runInNewContext(source, context);
  return { controls, button, form, window, calls, timers,
    submit: () => events.submit({ preventDefault() {} }) };
}

(async () => {
  const good = setup();
  assert.equal(good.calls.length, 0, "Do not send until user submits");
  assert.equal(good.controls["rfq-products"].value, "Coffee wood");
  await good.submit();
  assert.equal(good.calls.length, 1);
  assert.equal(good.calls[0].url, "https://formspree.io/f/mvkpbvlb");
  assert.equal(good.calls[0].args.method, "POST");
  assert.equal(good.calls[0].args.headers.Accept, "application/json");
  assert.equal(good.calls[0].args.body.values.get("email"), "buyer+test@example.com");
  assert.equal(good.calls[0].args.body.values.get("products"), "Coffee wood");
  assert.equal(good.window.location.href, "https://vietpaw.com/request-a-quote/thank-you/index.html");
  assert.equal(good.timers.size, 0);
  assert.equal(good.controls["form-error"].hidden, true);
  await good.submit();
  assert.equal(good.calls.length, 1, "Do not duplicate an accepted submission");

  for (const reply of [false, "reject"]) {
    const fail = setup({ reply });
    const originalUrl = fail.window.location.href;
    await fail.submit();
    assert.equal(fail.window.location.href, originalUrl);
    assert.equal(fail.button.disabled, false);
    assert.equal(fail.button.textContent, "Send Enquiry");
    assert.equal(fail.controls["form-error"].hidden, false);
    assert.equal(fail.controls["form-error"].focused, true);
    assert.equal(fail.controls["rfq-products"].value, "Coffee wood");
    assert.equal(fail.form["aria-busy"], undefined);
    await fail.submit();
    assert.equal(fail.calls.length, 2, "Allow explicit retry after failure");
  }
  const invalid = setup({ valid: false });
  await invalid.submit();
  assert.equal(invalid.calls.length, 0);

  let resolve;
  const pending = setup({ reply: () => new Promise(done => { resolve = done; }) });
  const first = pending.submit();
  assert.equal(pending.button.disabled, true);
  assert.equal(pending.form["aria-busy"], "true");
  await pending.submit();
  assert.equal(pending.calls.length, 1);
  resolve({ ok: true });
  await first;

  const timeout = setup({ reply: ({ signal }) => new Promise((_, reject) => {
    signal.addEventListener("abort", () => reject(Object.assign(new Error("Timeout"), { name: "AbortError" })));
  }) });
  const wait = timeout.submit();
  timeout.timers.get(1)();
  await wait;
  assert.match(timeout.controls["rfq-status"].textContent, /could not confirm delivery/);
  assert.equal(timeout.button.disabled, false);

  for (const href of [
    "file:///D:/Site/request-a-quote/index.html?product=Hemp",
    "https://vietpaw.com/request-a-quote/?request=sample"
  ]) {
    const portable = setup({ href });
    await portable.submit();
    assert.equal(portable.window.location.href, new URL("thank-you/index.html", href).href);
  }
  const hostile = setup({ href: "https://vietpaw.com/request-a-quote/?product=" + encodeURIComponent("<script>alert('test')</script>") });
  assert.equal(hostile.controls["rfq-products"].value, "<script>alert('test')</script>");
  assert.ok(!("innerHTML" in hostile.controls["rfq-products"]));
  const long = setup({ href: "https://vietpaw.com/request-a-quote/?product=" + "a".repeat(3000) });
  assert.equal(long.controls["rfq-products"].value.length, 2500);
  assert.equal(setup({ existing: "My edited brief" }).controls["rfq-products"].value, "My edited brief");
  assert.ok(!/localStorage|sessionStorage|gtag\(|mailto:.*subject=/.test(source));
  console.log("PASS: restored Formspree payload, five-field form, prefill, validation, no auto-send, success redirect, HTTP/network failure, timeout, retry and duplicate guards; no real submissions sent.");
})().catch(error => { console.error(error); process.exitCode = 1; });
