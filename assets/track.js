/* VietPaw GA4 events. Business fields only: name, email, phone and company are never sent.
   The enquiry form itself stays free of analytics code; it dispatches a "vietpaw:lead"
   DOM event and this module decides what, if anything, is reported. */
(() => {
  "use strict";
  const doc = window.document;
  if (!doc || typeof doc.addEventListener !== "function") return;

  const send = (name, params) => {
    if (typeof window.gtag !== "function") return;
    window.gtag("event", name, params || {});
  };
  const here = () => (window.location && window.location.href) || "";

  // Fired by rfq.js once Formspree has accepted the submission. Deliberately not tied
  // to the thank-you page: a buyer who leaves before the redirect is still a lead.
  doc.addEventListener("vietpaw:lead", event => {
    const detail = (event && event.detail) || {};
    send("generate_lead", {
      form_id: detail.form_id || "",
      buyer_type: detail.buyer_type || "",
      country: detail.country || "",
      products: detail.products || "",
      est_quantity: detail.est_quantity || "",
      enquiry_type: detail.enquiry_type || "",
      lead_source: "website_form"
    });
    // request_sample is deliberately NOT sent. enquiry_type is a fixed hidden value on the
    // only enquiry form, so the event would duplicate generate_lead one for one and inflate
    // the key-event count. Send it once a sample-only form exists, or once enquiry_type varies.
  });

  const start = () => {
    doc.addEventListener("click", event => {
      const target = event && event.target;
      const link = target && typeof target.closest === "function" ? target.closest("a[href]") : null;
      if (!link) return;
      const href = link.getAttribute("href") || "";
      if (href.indexOf("wa.me") > -1) send("contact_whatsapp", { page_location: here() });
      else if (href.lastIndexOf("mailto:", 0) === 0) send("contact_email", { page_location: here() });
    }, true);

    const form = doc.querySelector("form[data-enquiry-form]");
    if (form && typeof window.IntersectionObserver === "function") {
      let seen = false;
      const observer = new window.IntersectionObserver(entries => {
        for (const entry of entries) {
          if (seen || !entry.isIntersecting || entry.intersectionRatio < 0.5) continue;
          seen = true;
          observer.disconnect();
          send("form_view", { form_id: form.id || "rfq-form", page_location: here() });
        }
      }, { threshold: [0.5] });
      observer.observe(form);
    }

    let scrolled = false;
    const onScroll = () => {
      if (scrolled) return;
      const root = doc.documentElement;
      if (!root) return;
      const total = Math.max(root.scrollHeight, doc.body ? doc.body.scrollHeight : 0) - window.innerHeight;
      if (total <= 0) return;
      const offset = window.pageYOffset || root.scrollTop || 0;
      if (offset / total < 0.75) return;
      scrolled = true;
      window.removeEventListener("scroll", onScroll);
      send("scroll_75", { page_location: here() });
    };
    window.addEventListener("scroll", onScroll, { passive: true });
  };

  if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", start, { once: true });
  else start();
})();
