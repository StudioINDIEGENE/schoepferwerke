/* =========================================================================
   Schöpferwerke — Fassung 2, die Bewegungsschicht.

   Lädt nach site.js. Ergänzt: gestaffelte Reveals in Gruppen, den
   Hero-Auftritt, den Scroll-Hinweis, eine sehr zurückhaltende Parallaxe
   und die Zähler-Mechanik für die Kennzahlen.

   Ohne JavaScript ist alles sofort sichtbar, nichts hängt davon ab.
   ========================================================================= */

(function () {
  "use strict";

  var ruhig = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* -------------------------------------- Staffelung innerhalb von Gruppen
     Kinder derselben Reihe erscheinen mit 90ms Versatz nacheinander. */

  var GRUPPEN = [
    ".karten", ".preise__reihe", ".stimmen__gitter", ".zahlen__reihe",
    ".raeume__gitter", ".knopfreihe", ".faq__liste", ".eckdaten", ".wahlen"
  ];

  GRUPPEN.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (gruppe) {
      var i = 0;
      Array.prototype.forEach.call(gruppe.children, function (kind) {
        if (kind.classList.contains("auftritt")) {
          kind.style.setProperty("--warte", i++);
        }
      });
    });
  });

  /* ------------------------------------------------------- Hero-Auftritt */

  var hero = document.querySelector(".hero");

  if (hero) {
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        hero.classList.add("ist-da");
      });
    });
    /* Fallback für gedrosselte Hintergrund-Tabs, in denen
       requestAnimationFrame nicht feuert. */
    window.setTimeout(function () { hero.classList.add("ist-da"); }, 400);

    /* Scroll-Hinweis verschwindet, sobald gescrollt wird. */
    var cue = hero.querySelector(".hero__cue");
    if (cue) {
      var cueWeg = function () {
        if (window.scrollY > 80) {
          cue.classList.add("weg");
          window.removeEventListener("scroll", cueWeg);
        }
      };
      window.addEventListener("scroll", cueWeg, { passive: true });
    }

    /* Sehr zurückhaltende Parallaxe auf dem Hero-Bild. */
    var foto = hero.querySelector(".hero__foto");
    if (foto && !ruhig) {
      var letzte = 0, laeuft = false;
      var setzen = function () {
        var r = hero.getBoundingClientRect();
        if (r.bottom > 0) {
          foto.style.transform = "translate3d(0," + (letzte * 0.18).toFixed(1) + "px,0)";
        }
        laeuft = false;
      };
      window.addEventListener("scroll", function () {
        letzte = window.scrollY;
        if (!laeuft) { requestAnimationFrame(setzen); laeuft = true; }
      }, { passive: true });
    }
  }

  /* -------------------------------------------------- Zähler-Mechanik
     Zählt Kennzahlen beim ersten Sichtbarwerden hoch. Platzhalter wie
     "[ ]" bleiben unangetastet, die Mechanik wartet auf echte Werte. */

  function zaehlen(el) {
    var text = el.textContent.trim();
    var m = text.match(/^(\d[\d.]*)(\s*\+?)$/);
    if (!m) return;
    var ziel = parseInt(m[1].replace(/\./g, ""), 10);
    var zusatz = m[2] || "";
    if (!ziel || ruhig) return;

    var dauer = 1800, start = null;
    function schritt(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dauer, 1);
      var weich = 1 - Math.pow(1 - p, 5);
      el.textContent = Math.round(weich * ziel).toLocaleString("de-DE") + zusatz;
      if (p < 1) requestAnimationFrame(schritt);
    }
    el.textContent = "0" + zusatz;
    requestAnimationFrame(schritt);
  }

  var werte = document.querySelectorAll(".zahl__wert");
  if (werte.length && "IntersectionObserver" in window) {
    var zaehlSpion = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (!e.isIntersecting) return;
        zaehlen(e.target);
        zaehlSpion.unobserve(e.target);
      });
    }, { threshold: 0.6 });
    werte.forEach(function (el) { zaehlSpion.observe(el); });
  }
})();

/* ---------------------------------------------- Nachtrag: mehr Fluss */
(function () {
  "use strict";

  var ruhig = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Rollende Schrittziffer: der Schritt, dessen Oberkante die
     Bildschirmmitte passiert hat, bestimmt die Ziffer. */
  var stapel = document.querySelector(".rolle__stapel");
  if (stapel) {
    var schritte = Array.prototype.slice.call(
      document.querySelectorAll(".ablauf .schritt"));
    var rollen = function () {
      var mitte = window.innerHeight / 2, aktiv = 0;
      schritte.forEach(function (s, i) {
        if (s.getBoundingClientRect().top <= mitte) aktiv = i;
      });
      stapel.style.transform = "translateY(-" + aktiv + "em)";
    };
    window.addEventListener("scroll", rollen, { passive: true });
    rollen();
  }

  /* Sanftes Schweben der großen Bilder beim Scrollen. */
  if (!ruhig) {
    var schweber = Array.prototype.slice.call(document.querySelectorAll(
      ".breitbild__bild picture, .angebot__bild picture, .bildkopf__bild picture, .akademie__bild picture, .karte__bild picture"
    ));
    if (schweber.length) {
      var laeuft = false;
      var setzen = function () {
        schweber.forEach(function (img) {
          var r = img.parentElement.getBoundingClientRect();
          if (r.bottom < 0 || r.top > innerHeight) return;
          var delta = (r.top + r.height / 2 - innerHeight / 2) * 0.06;
          /* Bei niedrigen Rahmen (Kartenbilder am Telefon) reicht die
             Vergrößerung von 1.12 nicht aus, um die Verschiebung zu
             decken: das Bild rutschte aus seinem Rahmen. */
          var grenze = r.height * 0.05;
          delta = Math.max(-grenze, Math.min(grenze, delta));
          img.style.transform = "scale(1.12) translateY(" + delta.toFixed(1) + "px)";
        });
        laeuft = false;
      };
      window.addEventListener("scroll", function () {
        if (!laeuft) { requestAnimationFrame(setzen); laeuft = true; }
      }, { passive: true });
      setzen();
    }

    /* Die Markenwellen zeichnen sich beim Laden langsam ein. */
    document.querySelectorAll(".wellen path").forEach(function (pfad) {
      try {
        var l = pfad.getTotalLength();
        pfad.style.strokeDasharray = l;
        pfad.style.strokeDashoffset = l;
        pfad.style.transition = "stroke-dashoffset 8s ease-out .4s";
        requestAnimationFrame(function () {
          requestAnimationFrame(function () { pfad.style.strokeDashoffset = "0"; });
        });
        window.setTimeout(function () { pfad.style.strokeDashoffset = "0"; }, 700);
      } catch (e) { /* Pfad ohne Länge, nichts tun */ }
    });
  }
})();

/* ------------------------------------------- Nachtrag: die Kaufleiste */
(function () {
  "use strict";
  var leiste = document.querySelector("[data-kaufleiste]");
  if (!leiste) return;

  var buchung = document.querySelector(".buchung");

  function zeigen() {
    var nah = buchung &&
      buchung.getBoundingClientRect().top < window.innerHeight * 0.9;
    leiste.classList.toggle("da", window.scrollY > 900 && !nah);
  }

  window.addEventListener("scroll", zeigen, { passive: true });
  zeigen();
})();

/* ------------------------------------- Nachtrag: Kopfleiste auf Grund */
(function () {
  "use strict";
  var kopf = document.querySelector(".kopf");
  if (!kopf) return;

  /* Über dem Hero bleibt der Kopf durchsichtig, sobald darunter Inhalt
     liegt, stellt er sich auf eigenen Grund. */
  var schwelle = 40;
  var stand = null;

  function pruefen() {
    var fest = window.scrollY > schwelle;
    if (fest === stand) return;
    stand = fest;
    kopf.classList.toggle("kopf--fest", fest);
  }

  window.addEventListener("scroll", pruefen, { passive: true });
  window.addEventListener("resize", pruefen, { passive: true });
  pruefen();
})();
