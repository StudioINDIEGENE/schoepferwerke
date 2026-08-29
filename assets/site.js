/* =========================================================================
   Schöpferwerke der Agnes Aichholzer
   Verhalten der Seite: Einblendungen beim Scrollen, Inhaltsverzeichnis,
   Akkordeon, Menü, Newsletter, Druckvorbereitung.

   Ohne JavaScript bleibt die Seite vollständig lesbar und bedienbar:
   nichts ist versteckt, die Fragen öffnen sich nativ über <details>,
   und die Kopfnavigation wird auf schmalen Geräten ausgeschrieben.
   ========================================================================= */

(function () {
  "use strict";

  var ruhig = window.matchMedia("(prefers-reduced-motion: reduce)");
  var sanft = !ruhig.matches;

  /* ------------------------------------------- Auftritt beim Scrollen */

  var auftritte = Array.prototype.slice.call(document.querySelectorAll(".auftritt"));

  if (!sanft || !("IntersectionObserver" in window)) {
    auftritte.forEach(function (el) { el.setAttribute("data-sichtbar", ""); });
  } else {
    var beobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.setAttribute("data-sichtbar", "");
        beobachter.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0 });

    auftritte.forEach(function (el) { beobachter.observe(el); });

    // Was beim Laden schon im Bild steht, erscheint ohne Verzögerung.
    requestAnimationFrame(function () {
      auftritte.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.94) {
          el.setAttribute("data-sichtbar", "");
          beobachter.unobserve(el);
        }
      });
    });
  }

  /* ------------------------------------------------ Inhaltsverzeichnis */

  var verzeichnisLinks = Array.prototype.slice.call(
    document.querySelectorAll(".verzeichnis__liste a")
  );

  if (verzeichnisLinks.length && "IntersectionObserver" in window) {
    var abschnitte = verzeichnisLinks
      .map(function (a) { return document.querySelector(a.getAttribute("href")); })
      .filter(Boolean);

    var sichtbare = new Set();

    var markieren = function () {
      var erster = abschnitte.find(function (s) { return sichtbare.has(s.id); });
      verzeichnisLinks.forEach(function (a) {
        if (erster && a.getAttribute("href") === "#" + erster.id) {
          a.setAttribute("data-hier", "");
        } else {
          a.removeAttribute("data-hier");
        }
      });
    };

    var spion = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (e.isIntersecting) sichtbare.add(e.target.id);
        else sichtbare.delete(e.target.id);
      });
      markieren();
    }, { rootMargin: "-119px 0px -55% 0px", threshold: 0 });

    abschnitte.forEach(function (s) { spion.observe(s); });
  }

  /* ------------------------------------------------------------ Akkordeon
     <details> öffnet und schließt von Haus aus. Hier kommt nur die weiche
     Höhenbewegung dazu, immer nur eine Frage bleibt offen. */

  var eintraege = Array.prototype.slice.call(document.querySelectorAll(".fq"));

  function hoeheAnimieren(huelle, von, bis, danach) {
    if (!sanft) { huelle.style.height = ""; if (danach) danach(); return; }
    huelle.style.height = von + "px";
    huelle.style.transition = "height .45s cubic-bezier(.22, .61, .36, 1)";
    requestAnimationFrame(function () { huelle.style.height = bis + "px"; });
    window.setTimeout(function () {
      huelle.style.transition = "";
      huelle.style.height = "";
      if (danach) danach();
    }, 460);
  }

  function schliessen(eintrag) {
    if (!eintrag.open) return;
    var huelle = eintrag.querySelector(".fq__huelle");
    if (!huelle) { eintrag.open = false; return; }
    hoeheAnimieren(huelle, huelle.scrollHeight, 0, function () { eintrag.open = false; });
  }

  eintraege.forEach(function (eintrag) {
    var kopf = eintrag.querySelector(".fq__kopf");
    var huelle = eintrag.querySelector(".fq__huelle");
    if (!kopf || !huelle) return;

    kopf.addEventListener("click", function (e) {
      e.preventDefault();

      if (eintrag.open) { schliessen(eintrag); return; }

      eintraege.forEach(function (anderer) {
        if (anderer !== eintrag) schliessen(anderer);
      });

      eintrag.open = true;
      hoeheAnimieren(huelle, 0, huelle.scrollHeight);
    });
  });

  /* ----------------------------------------------------------------- Menü */

  var ueberlagerung = document.getElementById("menue");
  var aufKnopf = document.querySelector("[data-menue-auf]");
  var zuKnopf = document.querySelector("[data-menue-zu]");
  var seiteninhalt = document.querySelector("main.seite");
  var kopfbereich = document.querySelector(".kopf");

  function fokussierbare() {
    if (!ueberlagerung) return [];
    return Array.prototype.slice.call(
      ueberlagerung.querySelectorAll("a[href], button:not([disabled])")
    );
  }

  function menueSetzen(offen) {
    if (!ueberlagerung) return;

    if (offen) ueberlagerung.removeAttribute("hidden");
    ueberlagerung.setAttribute("data-offen", offen ? "ja" : "nein");
    if (!offen) {
      window.setTimeout(function () {
        if (ueberlagerung.getAttribute("data-offen") === "nein") {
          ueberlagerung.setAttribute("hidden", "");
        }
      }, 0);
    }

    document.body.style.overflow = offen ? "hidden" : "";
    if (aufKnopf) aufKnopf.setAttribute("aria-expanded", offen ? "true" : "false");

    // Der Rest der Seite wird für Tastatur und Vorleseprogramme stillgelegt.
    [seiteninhalt, kopfbereich].forEach(function (el) {
      if (!el) return;
      if (offen) el.setAttribute("inert", "");
      else el.removeAttribute("inert");
    });

    if (offen && zuKnopf) zuKnopf.focus();
    else if (!offen && aufKnopf) aufKnopf.focus();
  }

  if (aufKnopf) aufKnopf.addEventListener("click", function () { menueSetzen(true); });
  if (zuKnopf) zuKnopf.addEventListener("click", function () { menueSetzen(false); });

  if (ueberlagerung) {
    ueberlagerung.addEventListener("click", function (e) {
      if (e.target.tagName === "A") menueSetzen(false);
    });

    // Fokusfalle, solange das Menü offen ist
    ueberlagerung.addEventListener("keydown", function (e) {
      if (e.key !== "Tab") return;
      var liste = fokussierbare();
      if (!liste.length) return;
      var erster = liste[0];
      var letzter = liste[liste.length - 1];
      if (e.shiftKey && document.activeElement === erster) {
        e.preventDefault();
        letzter.focus();
      } else if (!e.shiftKey && document.activeElement === letzter) {
        e.preventDefault();
        erster.focus();
      }
    });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && ueberlagerung &&
        ueberlagerung.getAttribute("data-offen") === "ja") {
      menueSetzen(false);
    }
  });

  /* -------------------------------------------------------- Newsletter
     Der Eintrag geht an Netlify Forms, also an dieselbe Adresse wie die
     Seite selbst. Die Einträge liegen im Netlify-Konto, eine
     Benachrichtigung an ein Postfach richtet Benjamin dort ein. */

  var form = document.querySelector("[data-newsletter]");
  var meldung = document.querySelector("[data-newsletter-meldung]");

  function sagen(text) { if (meldung) meldung.textContent = text; }

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var feld = form.querySelector("input[type=email]");
      if (!feld) return;

      if (!feld.value || !feld.checkValidity()) {
        sagen("Bitte gib eine gültige E-Mail-Adresse ein.");
        feld.focus();
        return;
      }

      sagen("Einen Moment.");
      fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(new FormData(form)).toString()
      }).then(function (antwort) {
        if (!antwort.ok) throw new Error("Antwort " + antwort.status);
        sagen("Danke, du bist eingetragen.");
        form.reset();
      }).catch(function () {
        sagen("Das hat nicht geklappt. Bitte später erneut versuchen.");
      });
    });
  }

  /* ------------------------------------------------- Buchungsformular */

  var bForm = document.querySelector("[data-buchung]");
  var bMeldung = document.querySelector("[data-buchung-meldung]");

  if (bForm) {
    bForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = bForm.querySelector("#b-name");
      var mail = bForm.querySelector("#b-mail");

      if (!name.value.trim()) {
        bMeldung.textContent = "Bitte trage deinen Namen ein.";
        name.focus();
        return;
      }
      if (!mail.value || !mail.checkValidity()) {
        bMeldung.textContent = "Bitte gib eine gültige E-Mail-Adresse ein.";
        mail.focus();
        return;
      }
      var knopf = bForm.querySelector("button[type=submit], .formular__knopf");
      if (knopf) knopf.disabled = true;
      bMeldung.textContent = "Einen Moment, deine Anfrage geht raus.";

      var daten = new URLSearchParams(new FormData(bForm)).toString();
      fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: daten
      }).then(function (antwort) {
        if (!antwort.ok) throw new Error("Antwort " + antwort.status);
        bForm.reset();
        bMeldung.textContent =
          "Danke, deine Anfrage ist angekommen. Agnes meldet sich bei dir.";
      }).catch(function () {
        bMeldung.textContent =
          "Das hat gerade nicht geklappt. Schreib mir bitte direkt an " +
          "info@schoepferwerke.com, dann geht nichts verloren.";
      }).then(function () {
        if (knopf) knopf.disabled = false;
      });
    });
  }

  /* ------------------------------------------------------------- Druck
     Beim Drucken werden alle Fragen geöffnet, damit die Antworten
     mit auf dem Papier stehen. Danach wird der Zustand wiederhergestellt. */

  var warOffen = [];

  function fuerDruckOeffnen() {
    warOffen = eintraege.map(function (d) { return d.open; });
    eintraege.forEach(function (d) {
      var huelle = d.querySelector(".fq__huelle");
      if (huelle) huelle.style.height = "";
      d.open = true;
    });
  }

  function nachDruckZuruecksetzen() {
    eintraege.forEach(function (d, i) { d.open = warOffen[i]; });
  }

  window.addEventListener("beforeprint", fuerDruckOeffnen);
  window.addEventListener("afterprint", nachDruckZuruecksetzen);

  if (window.matchMedia) {
    var druck = window.matchMedia("print");
    var beiDruckwechsel = function (e) {
      if (e.matches) fuerDruckOeffnen();
      else nachDruckZuruecksetzen();
    };
    if (druck.addEventListener) druck.addEventListener("change", beiDruckwechsel);
    else if (druck.addListener) druck.addListener(beiDruckwechsel);
  }
})();
