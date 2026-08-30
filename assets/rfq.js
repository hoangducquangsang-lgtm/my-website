/* Local-only enquiry preparation: no tracking, persistence or server submission. */
(() => {
  "use strict";
  const form = document.getElementById("rfq-form");
  if (!form) return;
  const preview = document.getElementById("rfq-preview");
  const status = document.getElementById("rfq-status");
  const params = new URLSearchParams(window.location.search);
  const product = params.get("product");
  if (product) document.getElementById("rfq-products").value = product.slice(0, 1800);
  if (params.get("request") === "sample") document.getElementById("rfq-request").value = "Sample and quotation";
  const prepare = () => {
    const lines = ["Hello WINVN,", "", "Please review my product enquiry:", ""];
    for (const [key, value] of new FormData(form).entries()) {
      lines.push(key + ": " + (String(value).trim() || "Not specified"));
    }
    lines.push("", "Please confirm MOQ, sample terms, packaging, timing and the quotation scope.");
    preview.value = lines.join("\n");
    return preview.value;
  };
  form.addEventListener("input", prepare);
  form.addEventListener("change", prepare);
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const body = prepare();
    const target = form.getAttribute("action").split("?")[0];
    window.location.href = target + "?subject=" + encodeURIComponent("WINVN product enquiry") + "&body=" + encodeURIComponent(body);
    status.textContent = "Email draft requested. Nothing has been sent by this website. Review and send it in your email app. If no draft opens, download the enquiry text or email sales directly.";
  });
  document.getElementById("rfq-download").addEventListener("click", () => {
    if (!form.reportValidity()) return;
    const blob = new Blob([prepare()], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "WINVN-product-enquiry.txt";
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.setTimeout(() => URL.revokeObjectURL(url), 1000);
    status.textContent = "Enquiry text downloaded. Nothing has been submitted; attach the file to an email to WINVN sales.";
  });
  prepare();
})();
