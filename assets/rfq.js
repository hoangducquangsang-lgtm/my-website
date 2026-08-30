/* Restored legacy Formspree destination; no tracking or local persistence. */
(() => {
  "use strict";
  const form = document.getElementById("rfq-form");
  if (!form) return;
  const status = document.getElementById("rfq-status");
  const error = document.getElementById("form-error");
  const button = form.querySelector('button[type="submit"]');
  const products = document.getElementById("rfq-products");
  const params = new URLSearchParams(window.location.search);
  const product = params.get("product");
  if (product && !products.value) products.value = product.slice(0, products.maxLength);
  let sending = false;
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (sending || !form.reportValidity()) return;
    sending = true;
    error.hidden = true;
    button.disabled = true;
    button.textContent = "Sending...";
    form.setAttribute("aria-busy", "true");
    status.textContent = "Sending your enquiry...";
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 25000);
    let accepted = false;
    try {
      const response = await fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" },
        signal: controller.signal
      });
      if (!response.ok) throw new Error("Enquiry not accepted");
      accepted = true;
      status.textContent = "Your enquiry has been received. Thank you.";
      window.location.href = new URL(form.dataset.successUrl, window.location.href).href;
    } catch (reason) {
      status.textContent = reason.name === "AbortError"
        ? "We could not confirm delivery. Please contact us directly before submitting again."
        : "Your enquiry could not be sent. Your entries have been kept so you can try again.";
      error.hidden = false;
      error.focus();
    } finally {
      window.clearTimeout(timeout);
      form.removeAttribute("aria-busy");
      if (!accepted) {
        sending = false;
        button.disabled = false;
        button.textContent = "Send Enquiry";
      }
    }
  });
})();
