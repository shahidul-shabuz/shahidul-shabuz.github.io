/* Progressive enhancement only — every byte of content renders without this file. */
(function () {
  "use strict";

  var root = document.documentElement;

  /* ---- theme ---------------------------------------------------------- */
  var stored = null;
  try { stored = localStorage.getItem("theme"); } catch (e) { /* private mode */ }
  if (stored === "dark" || stored === "light") root.setAttribute("data-theme", stored);

  function currentTheme() {
    var set = root.getAttribute("data-theme");
    if (set) return set;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  var themeBtn = document.getElementById("theme-btn");
  function paintThemeBtn() {
    if (!themeBtn) return;
    var dark = currentTheme() === "dark";
    themeBtn.textContent = dark ? "☀" : "☾";
    themeBtn.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
    themeBtn.setAttribute("title", themeBtn.getAttribute("aria-label"));
  }
  paintThemeBtn();

  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) { /* ignore */ }
      paintThemeBtn();
    });
  }

  /* ---- navigation ----------------------------------------------------- */
  var navBtn = document.getElementById("nav-btn");
  var nav = document.getElementById("nav");
  if (navBtn && nav) {
    navBtn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      navBtn.setAttribute("aria-expanded", String(open));
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("open");
        navBtn.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---- footer year ---------------------------------------------------- */
  var y = document.getElementById("year");
  if (y) y.textContent = String(new Date().getFullYear());
})();
