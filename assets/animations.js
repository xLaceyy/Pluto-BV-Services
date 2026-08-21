/* Pluto BV Ltd — animations.js
   Decorative effects: magnetic buttons, custom cursor, hero particles, 3D tilt, count-up stats. */
(function () {
  "use strict";
  var reduced = window.PLUTO_REDUCED;
  var hasGsap = !!window.gsap;

  // ---- Hero particles ----
  var field = document.getElementById("heroParticles");
  if (field) {
    for (var i = 0; i < 26; i++) {
      var s = document.createElement("span");
      s.style.left = (Math.random() * 100) + "%";
      s.style.top = (Math.random() * 100) + "%";
      s.style.animationDelay = (Math.random() * 8) + "s";
      s.style.animationDuration = (7 + Math.random() * 6) + "s";
      field.appendChild(s);
    }
  }

  // ---- Hero P parallax ----
  var heroP = document.getElementById("heroP");
  if (heroP && !reduced && hasGsap) {
    window.addEventListener("mousemove", function (e) {
      var x = (e.clientX / window.innerWidth - 0.5) * 18;
      var y = (e.clientY / window.innerHeight - 0.5) * 18;
      gsap.to(heroP, { x: x, y: y, rotateZ: x * 0.08, duration: 1.2, ease: "power3.out" });
    });
    if (window.ScrollTrigger) {
      gsap.to(heroP, {
        yPercent: 14, ease: "none",
        scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true }
      });
      gsap.to(".hero-inner", {
        yPercent: -10, opacity: 0.6, ease: "none",
        scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true }
      });
    }
  }

  // ---- Statement / final P drift ----
  if (!reduced && hasGsap && window.ScrollTrigger) {
    if (document.querySelector(".statement-p-bg")) {
      gsap.to(".statement-p-bg", {
        yPercent: -10, rotate: 3, ease: "none",
        scrollTrigger: { trigger: ".statement", start: "top bottom", end: "bottom top", scrub: true }
      });
    }
    if (document.querySelector(".final-p")) {
      gsap.to(".final-p", {
        scale: 1.08, ease: "none",
        scrollTrigger: { trigger: ".final-cta", start: "top bottom", end: "bottom top", scrub: true }
      });
    }
  }

  // ---- Timeline fill ----
  var timelineFill = document.getElementById("timelineFill");
  if (timelineFill && window.ScrollTrigger) {
    ScrollTrigger.create({
      trigger: ".timeline",
      start: "top 70%",
      onEnter: function () { timelineFill.style.width = "100%"; }
    });
  }

  // ---- Magnetic buttons ----
  if (!reduced && hasGsap) {
    document.querySelectorAll(".magnetic").forEach(function (btn) {
      btn.addEventListener("mousemove", function (e) {
        var r = btn.getBoundingClientRect();
        var x = e.clientX - r.left - r.width / 2;
        var y = e.clientY - r.top - r.height / 2;
        gsap.to(btn, { x: x * 0.2, y: y * 0.3, duration: 0.6, ease: "power3.out" });
      });
      btn.addEventListener("mouseleave", function () {
        gsap.to(btn, { x: 0, y: 0, duration: 0.7, ease: "elastic.out(1,0.3)" });
      });
    });
  }

  // ---- Service row hover ----
  if (hasGsap) {
    document.querySelectorAll(".service-row").forEach(function (row) {
      row.addEventListener("mouseenter", function () {
        gsap.to(row, { paddingLeft: 20, duration: 0.6, ease: "power3.out" });
      });
      row.addEventListener("mouseleave", function () {
        gsap.to(row, { paddingLeft: 10, duration: 0.6, ease: "power3.out" });
      });
    });
  }

  // ---- Custom cursor ----
  var cursor = document.getElementById("cursor");
  var cursorLabel = document.getElementById("cursorLabel");
  if (cursor && hasGsap && window.matchMedia("(hover:hover)").matches) {
    window.addEventListener("mousemove", function (e) {
      gsap.to(cursor, { x: e.clientX, y: e.clientY, duration: 0.3, ease: "power2.out" });
    });
    document.querySelectorAll("a, button, .service-row, .people-card, .story-card").forEach(function (el) {
      el.addEventListener("mouseenter", function () {
        cursor.classList.add("is-active");
        if (cursorLabel) {
          if (el.classList.contains("service-row")) cursorLabel.textContent = "Explore";
          else if (el.classList.contains("people-card")) cursorLabel.textContent = "Learn";
          else if (el.classList.contains("story-card")) cursorLabel.textContent = "Read";
          else cursorLabel.textContent = "View";
        }
      });
      el.addEventListener("mouseleave", function () { cursor.classList.remove("is-active"); });
    });
  }

  // ---- 3D tilt for people cards ----
  if (hasGsap) {
    document.querySelectorAll(".people-card").forEach(function (card) {
      card.addEventListener("mousemove", function (e) {
        var rect = card.getBoundingClientRect();
        var x = (e.clientX - rect.left) / rect.width - 0.5;
        var y = (e.clientY - rect.top) / rect.height - 0.5;
        gsap.to(card, { rotateX: y * 4, rotateY: x * 4, duration: 0.6, ease: "power2.out" });
        var inner = card.querySelector(".card-inner");
        if (inner) gsap.to(inner, { x: x * 6, y: y * 4, duration: 0.6, ease: "power2.out" });
      });
      card.addEventListener("mouseleave", function () {
        gsap.to(card, { rotateX: 0, rotateY: 0, duration: 0.8, ease: "elastic.out(1,0.3)" });
        var inner = card.querySelector(".card-inner");
        if (inner) gsap.to(inner, { x: 0, y: 0, duration: 0.8, ease: "elastic.out(1,0.3)" });
      });
    });
  }

  // ---- Count-up stats ----
  if (hasGsap && window.ScrollTrigger) {
    document.querySelectorAll(".stat .num[data-count]").forEach(function (el) {
      var target = parseInt(el.getAttribute("data-count"), 10);
      if (isNaN(target)) return;
      ScrollTrigger.create({
        trigger: el,
        start: "top 90%",
        onEnter: function () {
          gsap.fromTo(el, { textContent: 0 }, {
            textContent: target,
            duration: 1.8,
            ease: "power2.out",
            snap: { textContent: 1 },
            onUpdate: function () { el.textContent = Math.round(this.targets()[0].textContent); }
          });
        }
      });
    });
  }
})();