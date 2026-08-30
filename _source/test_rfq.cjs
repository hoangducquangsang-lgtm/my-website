/* Unit-level behavior checks with a small DOM stub; no browser or external sends. */
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const assert = require("node:assert/strict");
const source = fs.readFileSync(path.join(__dirname, "../assets/rfq.js"), "utf8");

function setup(query = "", valid = true) {
  const events = {};
  const controls = Object.fromEntries(
    ["rfq-preview", "rfq-status", "rfq-products", "rfq-request", "rfq-download"].map(
      (id) => [id, { value: "", textContent: "", addEventListener: (event, callback) => { events[id + ":" + event] = callback; } }]
    )
  );
  let anchorClicks = 0;
  let revoked = false;
  let downloaded = null;
  const form = {
    reportValidity: () => valid,
    getAttribute: () => "mailto:sarah@vietpaw.com",
    addEventListener: (event, callback) => { events["form:" + event] = callback; }
  };
  controls["rfq-form"] = form;
  const window = { location: { search: query, href: "" }, setTimeout: (fn) => fn() };
  class FormDataStub {
    entries() {
      return new Map([
        ["Name", "Buyer & Team"], ["Email", "buyer+test@example.com"],
        ["Company and role", "Test Co."], ["Website", "https://example.com"],
        ["Destination country", "Japan"], ["Buyer type", "Pet brand"],
        ["Request type", controls["rfq-request"].value],
        ["Products and sizes", controls["rfq-products"].value],
        ["Quantity per SKU", "CC01-M 500"], ["Branding requirement", "Private label"],
        ["Destination details", "Tokyo"], ["Target date", "2026-11-01"],
        ["Additional requirements", "Kraft pack & barcode; tiếng Việt"]
      ]).entries();
    }
  }
  const context = {
    window, FormData: FormDataStub, URLSearchParams, encodeURIComponent, Blob,
    URL: { createObjectURL: (blob) => { downloaded = blob; return "blob:test"; }, revokeObjectURL: () => { revoked = true; } },
    document: {
      getElementById: (id) => controls[id],
      createElement: () => ({ click: () => { anchorClicks++; }, remove: () => {} }),
      body: { appendChild: () => {} }
    }
  };
  vm.runInNewContext(source, context);
  return { controls, events, window, results: () => ({ anchorClicks, revoked, downloaded }) };
}

const good = setup("?request=sample&product=Coffee%20Wood%20Dog%20Chew");
assert.equal(good.controls["rfq-products"].value, "Coffee Wood Dog Chew");
assert.equal(good.controls["rfq-request"].value, "Sample and quotation");
assert.match(good.controls["rfq-preview"].value, /Destination country: Japan/);
assert.match(good.controls["rfq-preview"].value, /Quantity per SKU: CC01-M 500/);
let prevented = false;
good.events["form:submit"]({ preventDefault: () => { prevented = true; } });
assert.ok(prevented);
assert.ok(good.window.location.href.startsWith("mailto:sarah@vietpaw.com?subject="));
const mail = new URL(good.window.location.href);
assert.equal(mail.searchParams.get("subject"), "WINVN product enquiry");
assert.match(mail.searchParams.get("body"), /buyer\+test@example\.com/);
assert.match(mail.searchParams.get("body"), /Kraft pack & barcode; tiếng Việt/);
assert.match(good.controls["rfq-status"].textContent, /Nothing has been sent/);
good.events["rfq-download:click"]();
assert.equal(good.results().anchorClicks, 1);
assert.ok(good.results().revoked);
assert.ok(good.results().downloaded instanceof Blob);
const invalid = setup("", false);
invalid.events["form:submit"]({ preventDefault: () => {} });
invalid.events["rfq-download:click"]();
assert.equal(invalid.window.location.href, "");
assert.equal(invalid.results().anchorClicks, 0);
const hostile = setup("?product=" + encodeURIComponent("<script>alert('test')</script>"));
assert.equal(hostile.controls["rfq-products"].value, "<script>alert('test')</script>");
assert.ok(!("innerHTML" in hostile.controls["rfq-products"]));
const long = setup("?product=" + "a".repeat(2000));
assert.equal(long.controls["rfq-products"].value.length, 1800);
assert.ok(!/localStorage|sessionStorage|fetch\(|XMLHttpRequest/.test(source));
console.log("PASS: RFQ query prefill, all qualifier fields, Unicode encoding, draft notice, validation guard, local download and plain-text input handling.");
