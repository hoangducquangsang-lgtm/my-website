/* Explicit quote and catalogue requests. No tracking, automatic sends or browser storage. */
(() => {
  "use strict";
  document.querySelectorAll("form[data-enquiry-form]").forEach(form => {
    const status = form.querySelector("[data-form-status]");
    const error = form.querySelector("[data-form-error]");
    const errorText = form.querySelector("[data-error-message]");
    const button = form.querySelector('button[type="submit"]');
    const without = form.querySelector("[data-without-attachment]");
    const attachment = form.querySelector("[data-attachment]");
    const productGroup = form.querySelector("[data-product-interest]");
    const productBoxes = productGroup ? Array.from(productGroup.querySelectorAll("[data-product-option]")) : [];
    const idleLabel = button.textContent;
    const params = new URLSearchParams(window.location.search);
    const product = (params.get("product") || "").toLowerCase();
    const matches = { coffee: "Coffee wood chew", coconut: "Coconut", hemp: "Hemp", loofah: "Loofah" };
    if (product) Object.keys(matches).forEach(key => {
      if (!product.includes(key)) return;
      productBoxes.forEach(box => { if (box.value === matches[key]) box.checked = true; });
    });
    const checkProducts = () => {
      if (!productBoxes.length) return true;
      const ok = productBoxes.some(box => box.checked);
      productBoxes[0].setCustomValidity(ok ? "" : "Select at least one product.");
      return ok;
    };
    productBoxes.forEach(box => box.addEventListener("change", checkProducts));
    let sending = false;
    const showError = message => {
      errorText.textContent = message;
      error.hidden = false;
      error.focus();
    };
    if (without) without.addEventListener("click", () => {
      if (sending) return;
      attachment.value = "";
      without.hidden = true;
      status.textContent = "Attachment removed. Your other entries are unchanged. Submit again without the file, then email the reference separately.";
      error.hidden = true;
      button.focus();
    });
    form.addEventListener("submit", async event => {
      event.preventDefault();
      checkProducts();
      if (sending || !form.reportValidity()) return;
      error.hidden = true;
      if (without) without.hidden = true;
      const file = attachment && attachment.files && attachment.files[0];
      if (file && (!/\.(pdf|jpe?g|png|webp)$/i.test(file.name) || file.size > 5 * 1024 * 1024 || !file.size)) {
        showError("Choose one PDF, JPG, PNG or WebP file no larger than 5 MB, or continue without the attachment.");
        without.hidden = false;
        return;
      }
      sending = true;
      button.disabled = true;
      button.textContent = "Sending...";
      form.setAttribute("aria-busy", "true");
      status.textContent = "Sending your request...";
      const controller = new AbortController();
      const timeout = window.setTimeout(() => controller.abort(), 25000);
      let accepted = false;
      try {
        const data = new FormData(form);
        if (attachment && !file) data.delete(attachment.name);
        const response = await fetch(form.action, {
          method: "POST", body: data, headers: { Accept: "application/json" }, signal: controller.signal
        });
        if (!response.ok) {
          const failure = new Error("Request not accepted");
          failure.status = response.status;
          throw failure;
        }
        accepted = true;
        status.textContent = form.dataset.enquiryForm === "catalogue"
          ? "Thank you. We have received your price-list request and will reply by email. You can still download the catalogue above."
          : "Your enquiry has been received. Thank you.";
        if (form.dataset.successUrl) {
          const target = new URL(form.dataset.successUrl, window.location.href);
          if (target.protocol === "file:" && target.pathname.endsWith("/")) target.pathname += "index.html";
          if (target.origin === window.location.origin) window.location.href = target.href;
        }
        button.textContent = "Request received";
      } catch (reason) {
        const uncertain = !reason.status;
        const message = reason.status === 429
          ? "Too many requests were received. Please wait before trying again, or contact us by email."
          : uncertain
            ? "We could not confirm delivery. Please contact us directly before submitting again. Your entries have been kept."
            : file
              ? "The request was not accepted. Try again, or continue without the attachment and email the reference separately. Your other entries have been kept."
              : "Your request could not be sent. Your entries have been kept so you can try again or contact us by email.";
        status.textContent = message;
        showError(message);
        if (without) without.hidden = !file || uncertain || reason.status === 429;
      } finally {
        window.clearTimeout(timeout);
        form.removeAttribute("aria-busy");
        if (!accepted) {
          sending = false;
          button.disabled = false;
          button.textContent = idleLabel;
        }
      }
    });
  });
})();
