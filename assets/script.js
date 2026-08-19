// Pluto BV Services — shared front-end behaviour
(function () {
  "use strict";

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- Sticky nav contrast on scroll ---- */
  var navWrap = document.querySelector(".nav-wrap");
  if (navWrap) {
    var onScroll = function () {
      navWrap.classList.toggle("scrolled", window.scrollY > 12);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- Mobile sheet ---- */
  var toggle = document.querySelector(".nav-toggle");
  var sheet = document.querySelector(".mobile-sheet");
  var closeBtn = document.querySelector(".mobile-sheet-close");
  var backdrop = document.querySelector(".mobile-sheet-backdrop");

  function openSheet() {
    if (!sheet) return;
    sheet.classList.add("open");
    document.body.style.overflow = "hidden";
    toggle.setAttribute("aria-expanded", "true");
    if (closeBtn) closeBtn.focus();
  }
  function closeSheet() {
    if (!sheet) return;
    sheet.classList.remove("open");
    document.body.style.overflow = "";
    toggle.setAttribute("aria-expanded", "false");
    if (toggle) toggle.focus();
  }
  if (toggle && sheet) {
    toggle.addEventListener("click", openSheet);
    if (closeBtn) closeBtn.addEventListener("click", closeSheet);
    if (backdrop) backdrop.addEventListener("click", closeSheet);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && sheet.classList.contains("open")) closeSheet();
    });
    sheet.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", closeSheet);
    });
  }

  /* ---- Reveal on scroll ---- */
  var revealEls = document.querySelectorAll(".reveal");
  if (revealEls.length) {
    if (prefersReducedMotion || !("IntersectionObserver" in window)) {
      revealEls.forEach(function (el) { el.classList.add("in"); });
    } else {
      var io = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add("in");
              io.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.14, rootMargin: "0px 0px -40px 0px" }
      );
      revealEls.forEach(function (el, i) {
        el.style.transitionDelay = prefersReducedMotion ? "0ms" : Math.min(i % 4, 3) * 70 + "ms";
        io.observe(el);
      });
    }
  }

  /* ---- Contact / enquiry form handling (front-end only) ---- */
  var form = document.querySelector("[data-pluto-form]");
  if (form) {
    var status = form.querySelector(".form-status");

    function setStatus(kind, message) {
      if (!status) return;
      status.textContent = message;
      status.className = "form-status show " + kind;
    }

    function validateField(field) {
      var input = field.querySelector("input, textarea, select");
      if (!input) return true;
      var valid = input.checkValidity();
      field.classList.toggle("error", !valid);
      return valid;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var fields = form.querySelectorAll(".field");
      var allValid = true;
      fields.forEach(function (field) {
        if (!validateField(field)) allValid = false;
      });

      if (!allValid) {
        setStatus("error", "Please check the highlighted fields and try again.");
        return;
      }

      var submitBtn = form.querySelector('[type="submit"]');
      if (submitBtn) submitBtn.disabled = true;
      setStatus("loading", "Sending your message…");

      // Front-end only demo behaviour — wire this up to Pluto's real form
      // handler / CRM endpoint before going live.
      window.setTimeout(function () {
        setStatus("success", "Thank you — your enquiry has been received. A member of the Pluto BV Services team will be in touch shortly.");
        form.reset();
        if (submitBtn) submitBtn.disabled = false;
      }, 900);
    });

    form.querySelectorAll(".field input, .field textarea, .field select").forEach(function (input) {
      input.addEventListener("blur", function () {
        validateField(input.closest(".field"));
      });
    });
  }

  /* ---- Hero parallax (subtle, physical — image drifts slower than scroll) ---- */
  var heroMedia = document.querySelector(".hero-media img");
  if (heroMedia && !prefersReducedMotion) {
    var ticking = false;
    var applyParallax = function () {
      var rect = heroMedia.parentElement.getBoundingClientRect();
      var progress = Math.min(Math.max((0 - rect.top) / (rect.height || 1), -1), 1);
      heroMedia.style.transform = "translateY(" + (progress * 26) + "px) scale(1.02)";
      ticking = false;
    };
    window.addEventListener(
      "scroll",
      function () {
        if (!ticking) {
          window.requestAnimationFrame(applyParallax);
          ticking = true;
        }
      },
      { passive: true }
    );
    applyParallax();
  }

  /* ---- Physical tilt on hero media (desktop pointer only) ---- */
  var tiltEl = document.querySelector(".hero-media");
  if (tiltEl && !prefersReducedMotion && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    tiltEl.addEventListener("pointermove", function (e) {
      var rect = tiltEl.getBoundingClientRect();
      var px = (e.clientX - rect.left) / rect.width - 0.5;
      var py = (e.clientY - rect.top) / rect.height - 0.5;
      tiltEl.style.transform = "perspective(1400px) rotateX(" + (py * -6) + "deg) rotateY(" + (px * 6) + "deg)";
    });
    tiltEl.addEventListener("pointerleave", function () {
      tiltEl.style.transform = "perspective(1400px) rotateX(0deg) rotateY(0deg)";
    });
  }

  /* ---- Current year in footer ---- */
  var yearEls = document.querySelectorAll("[data-year]");
  yearEls.forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
