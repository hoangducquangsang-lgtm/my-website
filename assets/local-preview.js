/* Clean links stay in published HTML. Adapt directory links only for local file previews. */
(() => {
  "use strict";
  if (window.location.protocol !== "file:") return;
  document.querySelectorAll("a[href], [data-success-url]").forEach(element => {
    const attr = element.hasAttribute("data-success-url") ? "data-success-url" : "href";
    const original = element.getAttribute(attr);
    if (!original || original.startsWith("#")) return;
    const target = new URL(original, window.location.href);
    if (target.protocol === "file:" && target.pathname.endsWith("/")) {
      target.pathname += "index.html";
      element.setAttribute(attr, target.href);
    }
  });
})();
