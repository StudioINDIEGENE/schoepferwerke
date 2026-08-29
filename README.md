# Schöpferwerke der Agnes Aichholzer — Website

Nachbau der veröffentlichten Framer-Seite
`https://agreeable-kangaroo-034021.framer.app`, in Formatierung,
Bedienbarkeit und Zugänglichkeit nachgeschärft.

Statische Seite ohne Build-Schritt: reines HTML, CSS und JavaScript.
Einfach zu öffnen, zu bearbeiten und überall zu hosten (Netlify, Vercel,
GitHub Pages, jeder Webspace).

## Aufbau

```
Schoepferwerke Webseite/
├─ index.html            Startseite
├─ ueber-mich.html       Über mich
├─ angebote.html         Angebote
├─ initiationen.html     Initiationen
├─ session-buchen.html   Session buchen
├─ schoepferwerke.html   Die Schöpferwerke
├─ datenschutz.html      Datenschutzerklärung
├─ impressum.html        Impressum
├─ agb.html              AGB
├─ _alt/                 die früheren Fassungen
├─ _werkzeug/            Vorlage und Bauskript (nicht ausliefern)
└─ assets/
   ├─ site.css           gesamtes Design-System
   ├─ site.js            Einblendungen, Menü, Akkordeon, Formulare
   ├─ fonts.css          lokale Schrifteinbindung
   ├─ fonts/             Crimson Text und Inter als woff2
   └─ img/
      ├─ web/            web-taugliche Bildfassungen (webp und jpg)
      └─ Bilder/         Originale
         └─ Framer/      alle 25 Bilder der Framer-Seite
```

## Seiten ändern

Kopfbereich, Navigation, FAQ und Fußzeile stehen **einmal** in
`_werkzeug/vorlage.py`. Die Texte der Seiten liegen in `_werkzeug/inhalt_*.py`.
Nach einer Änderung neu erzeugen:

```
python3 _werkzeug/bauen.py
```

Heraus kommen neun ganz gewöhnliche HTML-Dateien. Zum Ausliefern der Seite
wird das Skript nicht gebraucht, es verhindert nur, dass du die Navigation
neunmal von Hand pflegen musst. Wer lieber direkt im HTML arbeitet, kann das
tun und den Ordner `_werkzeug` löschen.

## Fassung 2 (24. August 2026)

Auf Benjamins Wunsch wurde die Seite über den Nachbau hinaus visuell
veredelt. Die erste Fassung liegt vollständig unter `_alt/v1-nachbau/`.
Die Veredelung ist eine eigene Schicht (`assets/site-v2.css` und
`assets/site-v2.js`), die nach den Grunddateien lädt. Wer zur ersten
Fassung zurück will, entfernt die beiden v2-Zeilen aus der Vorlage.

Die Entscheidungen stammen aus einer Referenzrecherche zu
Premium-Coaching- und Wellness-Seiten:

- **Bilder komplett getauscht** (siehe `BILDNACHWEIS.md`): Seebensee im
  Hero, drei Elementar-Naturbilder für die Programme (Wasser, Licht,
  Gipfel), Nebelmeer als Breitbild, Drei Zinnen unter der Milchstraße für
  Initiationen und Schöpferwerke. Alles Unsplash, kommerziell nutzbar.
- **Farbdramaturgie**: warmes Papier statt reinem Weiß, zarte
  Salbei-Atempausen, genau eine dunkle Ankersektion (das große Zitat) in
  Tiefgrün. Die mittlere Preiskarte ist invertiert.
- **Gold nach der Drei-Stellen-Regel**: Logopunkt, Punkt vor den
  Sektionsmarken, Ornament-Trenner. Nie als Fläche.
- **Typografie**: kursive Serifen-Akzentwörter in zentralen Überschriften
  (Quelle, Schöpferkraft, Seele), das Ankerzitat kursiv mit
  Wasserzeichen-Anführungszeichen.
- **Textur und Form**: feines Filmkorn über der ganzen Seite
  (SVG-Rauschen, 4 Prozent), Bogenform für das Porträt mit farbigem Echo,
  zwei flache Kurven-Trenner (vor FAQ und Fußzeile), der Aufruf als
  rundum gerundetes Feld.
- **Bewegung**: langsamer Ken-Burns-Zoom im Hero, Titelzeilen steigen aus
  Masken auf, gestaffelte Einblendungen in Gruppen (90 ms Versatz),
  Kartenbilder setzen sich beim Erscheinen, Scroll-Hinweis mit wanderndem
  Lichtpunkt, zurückhaltende Parallaxe, Zähler-Mechanik für die
  Kennzahlen (wartet auf echte Werte). `prefers-reduced-motion` schaltet
  alles ab.

### Nachtrag vom 25. August 2026, zweiter Teil

- **Passendere Bildformate am Desktop**: Die Monumentalformate des
  Originals (bis 2125 Pixel hoch) weichen flachen Bändern (21:9 bei
  Angeboten und Breitbild, 16:7 bei den Kopfbildern). Tablet und Telefon
  bleiben unverändert.
- **Fließende Kopfbilder**: Auf Initiationen und Schöpferwerke läuft das
  Bild unten weich ins Papier aus, der Titel steigt in die
  Auflösungszone, dazu ein sehr langsamer Atemzoom über 30 Sekunden.
- **Neues Initiationsbild**: Waldweg zum lichtdurchfluteten Tor
  (Michael Held, Unsplash) — „Natur initiiert". Die Drei Zinnen unter
  der Milchstraße bleiben der Schöpferwerke-Seite vorbehalten.

### Nachtrag vom 25. August 2026

- **Rollende Schrittziffer** wie im Original: Bei „So arbeiten wir
  zusammen" steht rechts eine 227 Pixel große Ziffer, die beim Lesen
  stehen bleibt und beim nächsten Schritt weiterrollt.
- **Fenster-Effekt**: Die großen Bilder öffnen sich beim Erscheinen wie
  ein Fenster und schweben beim Scrollen leicht hinter ihrem Rahmen mit.
- **Mehr Fluss**: Die Kurven-Trenner treiben langsam wie eine
  Wasserlinie, die Hintergrund-Auren atmen, die Markenwellen zeichnen
  sich auf den Unterseiten langsam ein, die Stimmen stehen organisch
  versetzt.
- **Verkaufsoptimierung der Angebotsseite**: Ankerleiste zu den vier
  Programmen, Schild „Beliebteste Wahl" auf dem 8-Wochen-Programm und der
  mittleren Preiskarte, dazu eine feste Leiste am unteren Rand mit dem
  kostenfreien Kennenlerngespräch als risikofreiem Einstieg (erscheint
  nach dem ersten Scrollen, verschwindet am Buchungsformular). Die
  Schilder sind funktionale Zusätze und von Agnes freizugeben.
- **Kopf lesbar**: Auf allen hellen Unterseiten steht die Wortmarke in
  Tiefgrün, der goldene Ring hat eine sichtbare Kante. Nur über dem
  dunklen Hero der Startseite bleibt die helle Markenfarbe. Die Marke
  oben links führt wie im Original auf die Schöpferwerke-Seite.

## Was gegenüber dem Original anders ist

Gestaltung, Raster, Typografie und Farben sind an der laufenden
Originalseite gemessen. Die Seiten sind anschließend in Formatierung,
Bedienbarkeit und Zugänglichkeit nachgeschärft worden und deshalb bewusst
**nicht mehr pixelgleich** mit dem Original.

### Verbessert

**Absatzformatierung.** Die Datenschutzerklärung stand im Original als ein
einziger Absatz von fast 3000 Pixel Höhe da, ohne jede Gliederung. Sie hat
jetzt vierzehn Abschnitte mit echten Listen. Bei „Über mich" klebten die
fünfzehn Kompetenzen als Überschrift und Beschreibung ohne Trennung
aneinander, zwei waren sogar zu einem Block verschmolzen. Bei den Angeboten
standen Dauer und Investition am Ende des Fließtextes angehängt, jetzt stehen
sie als eigene Eckdaten. In den AGB waren die Aufzählungen der Punkte 6 und
10 als Fließtext mit Mittelpunkten zusammengelaufen. Sie stehen jetzt als
echte Listen. Punkt 4 ist in zwei Absätze getrennt, „Ratenzahlungen" ist als
Zwischenbegriff ausgezeichnet. Punkt 7 endete mit zwei leeren Zeilenumbrüchen,
der Satz „Wir geben keine Heilversprechen!" steht jetzt als hervorgehobener
Merksatz. Die Punkte 6 bis 13 lagen im Original in einem einzigen Rahmen mit
abweichendem Abstand, jetzt hat jeder Punkt seinen eigenen Abschnitt und alle
Abstände folgen demselben Maß.

**Der Wortlaut der Kundin ist unverändert.** Geändert wurde nur die
Gliederung, kein einziger Satz. Auch offensichtliche Tippfehler des Originals
(„Viele meiner Kund", „wo die Ursachen … liegt") stehen bewusst so da und
sollten von Agnes selbst korrigiert werden.

**Inhaltsverzeichnis.** Auf den drei Rechtsseiten war die linke Spalte im
Original leer. Dort steht jetzt ein mitlaufendes Verzeichnis, das den gerade
gelesenen Abschnitt markiert. Nur am Desktop.

**Bilder.** Aus 25,4 MB wurden 12,6 MB. Jedes Bild liegt in zwei Breiten als
WebP und JPEG vor, der Browser wählt selbst. Das größte fiel von 6,8 MB auf
60 KB.

**Einblendungen beim Scrollen.** Das Original blendet 98 Elemente beim
Scrollen ein. Das fehlte im ersten Nachbau und ist jetzt umgesetzt, über
`IntersectionObserver`, mit einem leichten Anheben. `prefers-reduced-motion`
wird beachtet, ohne JavaScript steht alles sofort sichtbar da.

**Lesbarkeit.** Silbentrennung im schmalen Satzspiegel, ruhigere Zeilenenden
über `text-wrap`, Abschnittsnummern im Markenton.

**Zugänglichkeit.** Überschriften laufen jetzt lückenlos von h1 über h2 zu h3
(vorher sprang die Seite von h1 auf h5). Sprungmarke zum Inhalt, Fokusring
mit ausreichendem Kontrast, das Menü auf schmalen Geräten ist ein echter
Dialog mit Fokusfalle, ohne JavaScript bleibt die Kopfnavigation erreichbar.

**Kontrast.** Das helle Salbeigrün erreicht auf Weiß nur 2,3:1 und ist damit
für Text zu schwach. Kleine Texte und die Schaltflächen nutzen jetzt
`--gruen-tief` (#3a7f77, 4,7:1). Die Wortmarke bleibt im hellen Markenton,
Logotypen sind von der Vorgabe ausgenommen.

**Druck.** Es gibt jetzt eine Druckdarstellung. Kopfbereich, Zierrat und
Fußzeile fallen weg, und alle Fragen werden vor dem Druck geöffnet, damit die
Antworten mit auf dem Papier stehen.

**Kopfbereich.** Kanonische Adresse, Open Graph, `theme-color`, Symbol für
den Startbildschirm.

### Bewusst nicht übernommen

Das „Made in Framer"-Abzeichen unten rechts, es gehört zu Framers kostenlosem
Hosting. Und die Bibliothek Lenis, mit der das Original das Scrollen
übersteuert: Sie fühlt sich auf Trackpads träge an und stört die
Bedienungshilfen. Bei Bedarf lässt sie sich nachrüsten.

### Eine Eigenheit der Vorlage wurde mitgenommen

Am Desktop ragt die zweizeilige Überschrift 24px über ihren Rahmen hinaus,
weil dieser im Original eine feste Höhe von 114px hat. Für natürlichen Fluss
in `assets/site.css` die Zeile `height: 114px` bei `.titelzeile__haupt`
entfernen.

### Noch von Agnes oder Benjamin zu klären

1. **Die vier Zählerwerte** (25+ Jahre, 3 Formate, 500+ begleitete
   Menschen, 1.200+ Sessions) hat Benjamin am 25. August 2026 bestätigt.
   Ändern in `_werkzeug/inhalt_start.py` bei `ZAHLEN`.
2. **Das Original widerspricht sich bei den Wochen.** Die Angebotsvorschau auf
   der Startseite nennt „6 Wochen Premium" und „13 Wochen High", der
   Preisblock und die Angebotsseite nennen „8 Wochen intensiv" und „13 Wochen
   transformativ". Beide Fassungen stehen so da wie im Original. Das ist eine
   geschäftliche Entscheidung, keine technische.
3. **Die E-Mail-Adresse.** Das Original zeigt `info@schöpferwerke.com` mit
   Umlaut, alle übrigen Seiten dieses Projekts nutzen
   `info@schoepferwerke.com`. Hier steht die Fassung ohne Umlaut. Bitte
   prüfen, welches Postfach wirklich existiert.
4. **Der Platzhalter in Punkt 4 der AGB.** „[inkl./zzgl.] gesetzlicher Umsatzsteuer"
   muss juristisch entschieden werden.
5. **Der Kontrast der Fußzeile.** Weiß auf Salbeigrün erreicht 2,3:1. Das ist
   eine Markenentscheidung: entweder ein tieferes Grün für die Fußzeile oder
   dunkle Schrift darauf.
6. **Die Formulare senden nichts.** Newsletter und Buchungsanfrage zeigen
   einen Hinweis, bis in `assets/site.js` bei `ZIEL` eine Adresse eingetragen
   ist. Im Original zeigte der Link „Schicke mir eine Email" übrigens auf
   `hello@world.com`, einen Rest der Vorlage. Hier steht die richtige Adresse.

7. **Tippfehler des Originals** stehen bewusst unverändert da und sollten von
   Agnes korrigiert werden: „Viele meiner Kund", „wo die Ursachen … liegt",
   „Diese Datenschutzerklärung wird bei Bedarf wird bei Bedarf angepasst".

## Die Bilder

`assets/img/Bilder/` enthält die eigenen Bildentwürfe (Dateien mit `hf_`).

`assets/img/Bilder/Framer/` enthält alle 25 Bilder, die auf der
veröffentlichten Framer-Seite liegen, über die Seitenmodule aller neun Routen
gesammelt und nach Verwendung benannt: `startseite-*`, `angebote-*`,
`initiationen-*`, `ueber-mich-*`, `gemeinsam-*` (mehrfach verwendet),
`vorschaubild-*` (nur als Vorschaubild beim Teilen hinterlegt) und
`symbol-*` (Favicon, Symbol für den Startbildschirm).

**Vor dem Einsatz verkleinern.** Mehrere Dateien sind zwischen 2 und 7 MB
groß, teils 6000 Pixel breit. So dürfen sie nicht auf die Seite. Sag
Bescheid, dann lege ich web-taugliche Fassungen daneben.

## Ansehen

Lokal genügt ein Doppelklick auf `index.html`. Für sauberes Verhalten der
relativen Pfade lieber über einen kleinen Server:

```
cd "Schoepferwerke Webseite"
python3 -m http.server 4321
# dann http://localhost:4321 öffnen
```

## Design-System (1:1 aus der Vorlage übernommen)

- **Farben:** Anthrazit-Grün `#2e3231`, Salbeigrün `#7fa69b`,
  Off-White `#fafafa`, Schwarz für die Zitat-Sektion
- **Schriften:** Crimson Text 400 (Serif-Überschriften), Inter (Fließtext +
  große Statements), Fragment Mono (Labels/Buttons/Eyebrows) — via Google Fonts
- **Details:** warm-körniger Hero (Film-Grain-Overlay), Versalien-Buttons mit
  Punkt, riesige Salbei-Prozesszahlen, überwiegend helle Flächen

## Was gegenüber der Vorlage verbessert wurde

- **Wochen vereinheitlicht:** Die Vorlage widersprach sich (Angebote „6/12
  Wochen", Preisboxen „8/13 Wochen"). Überall konsistent **6 und 12 Wochen**.
- **Nav-Kontrast:** Über dem Hero hell, wird beim Scrollen gläsern/dunkel.
- **Bewegung:** sanftes Scroll-Reveal, rotierendes Wort im Intro, hochzählende
  Statistik-Zahlen, animiertes FAQ-Akkordeon.
- **Formulare echt versendbar** (siehe unten) statt nur Frontend-Meldung.
- **Barrierearm:** semantisches HTML, `prefers-reduced-motion` respektiert,
  Alt-Texte, sichtbare Fokuszustände.

## Formulare (Buchung + Newsletter)

Beide Formulare sind für **Netlify Forms** vorbereitet (`data-netlify="true"`).
Beim Deploy auf Netlify werden sie automatisch erkannt; Einträge landen im
Netlify-Dashboard und können per E-Mail-Benachrichtigung an
`info@schoepferwerke.com` weitergeleitet werden — ohne eigenes Backend.
Läuft die Seite woanders, öffnet das Buchungsformular als Fallback das
E-Mail-Programm mit vorausgefüllter Nachricht.

Alternativen falls kein Netlify: Formspree o. ä. (nur `action`/`fetch`-Ziel
in `script.js` bzw. im `<form>` tauschen).

## Noch von Agnes / dir zu erledigen

1. **Echte Fotos** — aktuell Stimmungs-Stockbilder aus der Vorlage
   (`assets/img/`). Gegen eigene Aufnahmen tauschen; ein Porträt von Agnes
   könnte z. B. das Hero- oder Zitat-Bild ersetzen.
2. **Statistik-Zahlen** in `index.html` prüfen (Platzhalter: 15+ Jahre, 3
   Formate, 120+ Menschen, 900+ Sessions) — `data-count`-Werte anpassen.
3. **Rechtstexte** — Impressum, Datenschutz und AGB sind Gerüste mit
   `[Platzhaltern]` und müssen juristisch korrekt gefüllt werden (Sitz in
   Südtirol/Italien beachten).
4. **Schriften lokal einbinden** für volle DSGVO-Konformität (statt Google
   Fonts vom Google-Server zu laden).
5. **Buchungslink** — falls es ein Direktbuchungs-/Zahlungstool gibt, die
   „Jetzt buchen"-Buttons dorthin verlinken.

## Hinweis zu den Bildern

Die Bilder stammen aus der öffentlich einsehbaren Framer-Vorlage und dienen
dem originalgetreuen Nachbau. Vor dem Live-Gang durch eigene bzw. sauber
lizenzierte Fotos ersetzen.
