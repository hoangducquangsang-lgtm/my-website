/* One disclosure at a time; preserve native links and keyboard activation. */
(() => {
  "use strict";
  const nav = document.querySelector(".main-nav");
  if (!nav) return;
  const menus = Array.from(nav.querySelectorAll("details.nav-menu"));
  const closeMenus = (except = null) => {
    for (const menu of menus) {
      if (menu !== except && menu.open) menu.open = false;
    }
  };

  for (const menu of menus) {
    // Close siblings before native activation, including in browsers without
    // support for the shared details name attribute. Enter/Space still work.
    menu.querySelector("summary").addEventListener("click", () => closeMenus(menu));
    menu.addEventListener("toggle", () => {
      if (menu.open) closeMenus(menu);
    });
  }
  document.addEventListener("click", (event) => {
    if (!nav.contains(event.target) || event.target.closest("a[href]")) closeMenus();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    const active = menus.find(menu => menu.open);
    if (!active) return;
    closeMenus();
    active.querySelector("summary").focus();
    event.preventDefault();
  });
  nav.addEventListener("focusout", (event) => {
    if (event.relatedTarget && !nav.contains(event.relatedTarget)) closeMenus();
  });
  // Do not restore expanded menus when returning with the Back button.
  window.addEventListener("pageshow", () => closeMenus());
  closeMenus();
})();

/* Mobile menu toggle: collapsed by default under 1050px so the hero is visible. */
(function () {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.getElementById('main-nav');
  if (!btn || !nav) return;
  function setOpen(open) {
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    nav.classList.toggle('is-open', open);
  }
  btn.addEventListener('click', function () {
    setOpen(btn.getAttribute('aria-expanded') !== 'true');
  });
  nav.addEventListener('click', function (e) {
    if (e.target.closest('a')) setOpen(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') { setOpen(false); btn.focus(); }
  });
  window.addEventListener('resize', function () {
    if (window.innerWidth > 1050) setOpen(false);
  });
})();
