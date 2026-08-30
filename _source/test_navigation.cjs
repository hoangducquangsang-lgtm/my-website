/* DOM/event model only. No browser, network, or user interaction is invoked. */
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const source = fs.readFileSync(path.join(__dirname, "../assets/navigation.js"), "utf8");

function setup() {
  const pending = new Set();
  let focused = null;
  class Element {
    constructor(tag, parent = null) { this.tag = tag; this.parent = parent; this.listeners = {}; }
    addEventListener(type, fn) { (this.listeners[type] ||= []).push(fn); }
    emit(type, extras = {}) {
      const event = { target: this, defaultPrevented: false, preventDefault() { this.defaultPrevented = true; }, ...extras };
      for (const fn of this.listeners[type] || []) fn(event);
      return event;
    }
    contains(node) { while (node) { if (node === this) return true; node = node.parent; } return false; }
    closest(selector) { let node = this; while (node) { if (selector === "a[href]" && node.tag === "a") return node; node = node.parent; } return null; }
    focus() { focused = this; }
  }
  const document = new Element("document"), window = new Element("window");
  const nav = new Element("nav", document), outside = new Element("button", document);
  const menus = Array.from({ length: 6 }, () => {
    const menu = new Element("details", nav);
    let open = false;
    Object.defineProperty(menu, "open", { get: () => open, set(value) { if (open !== value) { open = value; pending.add(menu); } } });
    menu.summary = new Element("summary", menu);
    menu.link = new Element("a", menu);
    menu.linkChild = new Element("span", menu.link);
    menu.padding = new Element("ul", menu);
    menu.querySelector = selector => selector === "summary" ? menu.summary : null;
    return menu;
  });
  nav.querySelectorAll = () => menus;
  document.querySelector = selector => selector === ".main-nav" ? nav : null;
  vm.runInNewContext(source, { document, window });
  function flush() {
    let limit = 30;
    while (pending.size) {
      assert.ok(limit-- > 0, "Toggle loop");
      const batch = Array.from(pending);
      pending.clear();
      batch.forEach(menu => menu.emit("toggle"));
    }
  }
  function activate(index, drain = true) {
    const menu = menus[index];
    menu.summary.emit("click");
    document.emit("click", { target: menu.summary });
    // Native default action, deliberately WITHOUT exclusive-name support:
    // the script itself must prevent the legacy multi-menu regression.
    menu.open = !menu.open;
    if (drain) flush();
  }
  return { document, window, nav, menus, outside, activate, flush, focused: () => focused,
    open: () => menus.map((menu, index) => menu.open ? index : -1).filter(index => index >= 0) };
}

const state = setup();
assert.deepEqual(state.open(), []);
for (let i = 0; i < 6; i++) {
  state.activate(i);
  assert.deepEqual(state.open(), [i], "Only the newly activated menu may stay open");
}
state.activate(5);
assert.deepEqual(state.open(), [], "Clicking an open summary closes it");
for (const index of [0, 1, 2, 3, 4, 5, 0]) state.activate(index, false);
state.flush();
assert.deepEqual(state.open(), [0], "Rapid clicks and queued toggle events remain exclusive");
state.document.emit("click", { target: state.menus[0].padding });
assert.deepEqual(state.open(), [0], "Clicking non-link menu content does not close it");
const linkClick = state.document.emit("click", { target: state.menus[0].linkChild });
assert.deepEqual(state.open(), []);
assert.equal(linkClick.defaultPrevented, false, "Never block normal link navigation");
state.activate(2);
state.document.emit("click", { target: state.outside });
assert.deepEqual(state.open(), []);
state.activate(3);
const escape = state.document.emit("keydown", { key: "Escape", target: state.menus[3].link });
assert.equal(escape.defaultPrevented, true);
assert.equal(state.focused(), state.menus[3].summary);
assert.deepEqual(state.open(), []);
assert.equal(state.document.emit("keydown", { key: "Escape", target: state.outside }).defaultPrevented, false);
state.activate(1);
state.nav.emit("focusout", { relatedTarget: state.menus[1].link });
assert.deepEqual(state.open(), [1], "Tabbing inside the menu keeps it open");
state.nav.emit("focusout", { relatedTarget: state.outside });
assert.deepEqual(state.open(), []);
state.activate(4);
state.document.emit("keydown", { key: "Tab" });
assert.deepEqual(state.open(), [4], "No keyboard trap");
state.window.emit("pageshow");
assert.deepEqual(state.open(), [], "Back/forward cache must not restore open menus");
state.menus[2].open = true;
state.flush();
state.menus[4].open = true;
state.flush();
assert.deepEqual(state.open(), [4], "Programmatic toggles use the same exclusivity rule");
assert.ok(!/window\.open|location\s*=|preventDefault\(\).*click/.test(source));
vm.runInNewContext(source, { document: { querySelector: () => null } });
console.log("PASS: exclusive menus, repeated/rapid activation, links, outside clicks, Escape/focus return, keyboard focus, programmatic changes and Back navigation; no browser invoked.");
