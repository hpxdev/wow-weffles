/* ==========================================================================
   Wow Weffles · shared interactions
   Vanilla JS, no dependencies. Loaded with `defer` on every page.
   Each feature guards for its own elements, so one file serves all pages.
   ========================================================================== */
(function () {
  "use strict";

  /* ---- Mobile nav toggle ------------------------------------------------ */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.getElementById("nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    // Close the drawer after tapping a link
    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---- Sticky-header shadow on scroll ----------------------------------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- Scroll reveal ---------------------------------------------------- */
  var reveals = document.querySelectorAll("[data-reveal]");
  if (reveals.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -10% 0px", threshold: 0.08 }
    );
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Back to top ------------------------------------------------------ */
  var toTop = document.querySelector(".to-top");
  if (toTop) {
    window.addEventListener("scroll", function () {
      toTop.classList.toggle("show", window.scrollY > 600);
    }, { passive: true });
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---- Menu category active-link highlight (menu.html) ------------------ */
  var menuNavLinks = document.querySelectorAll(".menu-nav a[href^='#']");
  var categories = document.querySelectorAll(".menu-category");
  if (menuNavLinks.length && categories.length && "IntersectionObserver" in window) {
    var setActive = function (id) {
      menuNavLinks.forEach(function (a) {
        a.classList.toggle("is-active", a.getAttribute("href") === "#" + id);
      });
    };
    var spy = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) setActive(entry.target.id);
        });
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 }
    );
    categories.forEach(function (c) { spy.observe(c); });
  }

  /* ---- Gallery lightbox (gallery.html) ---------------------------------- */
  var galleryImgs = document.querySelectorAll(".gallery-grid img");
  var lightbox = document.getElementById("lightbox");
  if (galleryImgs.length && lightbox) {
    var lbImg = lightbox.querySelector("img");
    var closeBtn = lightbox.querySelector(".lightbox__close");
    var open = function (src, alt) {
      lbImg.src = src;
      lbImg.alt = alt || "";
      lightbox.classList.add("is-open");
      document.body.style.overflow = "hidden";
    };
    var close = function () {
      lightbox.classList.remove("is-open");
      document.body.style.overflow = "";
    };
    galleryImgs.forEach(function (img) {
      img.parentElement.addEventListener("click", function () {
        open(img.currentSrc || img.src, img.alt);
      });
    });
    closeBtn.addEventListener("click", close);
    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox) close();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && lightbox.classList.contains("is-open")) close();
    });
  }

  /* ---- Contact form ----------------------------------------------------- */
  /* The contact form now POSTs to Django (server-side validation + storage),
     so no front-end submit handler is needed. The browser submits normally. */

  /* ---- Footer year ------------------------------------------------------ */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
