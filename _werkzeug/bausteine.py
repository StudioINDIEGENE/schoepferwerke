# -*- coding: utf-8 -*-
"""
Bausteine für den Seiteninhalt.

Ein Rechtstext wird als Liste von Abschnitten beschrieben. Jeder Abschnitt
hat eine Überschrift und beliebig viele Blöcke:

    ("p",    "Fließtext")
    ("ul",   ["Punkt", "Punkt"])
    ("adr",  ["Zeile", "Zeile"])
    ("merk", "Hervorgehobener Satz")
    ("lead", "Begriff", "Fortsetzung des Satzes")

Die Inhaltsseiten setzen sich aus den Bausteinen weiter unten zusammen.
Alle Maße und Schriftgrade sind an der Originalseite gemessen.
"""


# ===================================================================
# Rechtstexte
# ===================================================================

def block_html(art, *daten):
    if art == "p":
        return f'<p class="auftritt">{daten[0]}</p>'
    if art == "lead":
        return f'<p class="auftritt"><strong class="hervor">{daten[0]}</strong> {daten[1]}</p>'
    if art == "merk":
        return f'<p class="merksatz auftritt">{daten[0]}</p>'
    if art == "ul":
        punkte = "\n              ".join(f"<li>{p}</li>" for p in daten[0])
        return f'<ul class="liste auftritt">\n              {punkte}\n            </ul>'
    if art == "adr":
        zeilen = "<br>".join(daten[0])
        return f'<p class="anschrift auftritt">{zeilen}</p>'
    raise ValueError(f"Unbekannter Baustein: {art}")


def rechtstext(titel, datum, intro, abschnitte, kurz=None):
    """Baut den Inhaltsbereich einer Rechtsseite samt Inhaltsverzeichnis."""
    kurz = kurz or [t for t, _ in abschnitte]

    verzeichnis = "\n              ".join(
        f'<li><a href="#a{i+1}">{k}</a></li>' for i, k in enumerate(kurz))

    teile = []
    for i, (ueberschrift, bloecke) in enumerate(abschnitte, start=1):
        inhalt = "\n            ".join(block_html(*b) for b in bloecke)
        teile.append(f"""          <section class="block absatz" id="a{i}" aria-labelledby="a{i}-t">
            <h2 class="t-h4 auftritt" id="a{i}-t"><span class="absatz__nr">{i}.</span> {ueberschrift}</h2>
            {inhalt}
          </section>""")
    koerper = "\n\n".join(teile)

    intro_html = (f"""          <div class="block">
            <p class="t-h5 intro auftritt">{intro}</p>
          </div>\n\n""" if intro else "")

    return f"""    <div class="kopfabstand"></div>

    <div class="textbereich">

      <div class="bahn titelzeile">
        <div class="s10 titelzeile__haupt">
          <div class="block">
            <h1 class="t-h1 titel">{titel}</h1>
          </div>
        </div>
        <div class="s2">
          <div class="block datum">
            <p class="t-klein">{datum}</p>
          </div>
        </div>
      </div>

      <div class="bahn textzeile">

        <div class="s3">
          <nav class="block verzeichnis" aria-labelledby="verzeichnis-titel">
            <p class="t-label verzeichnis__titel" id="verzeichnis-titel">Inhalt</p>
            <ol class="verzeichnis__liste">
              {verzeichnis}
            </ol>
          </nav>
        </div>

        <div class="s9 textspalte">

{intro_html}{koerper}

        </div>
      </div>
    </div>"""


# ===================================================================
# Bilder
# ===================================================================

def bild_tag(name, alt, breite, hoehe, klasse="", laden="lazy", groessen=None,
             hat_gross=True, gross=1800):
    """<picture> mit webp und jpg, zwei Breiten."""
    sizes = f' sizes="{groessen}"' if groessen else ""
    gross_webp = f", assets/img/web/{name}@{gross}.webp {gross}w" if hat_gross else ""
    gross_jpg = f", assets/img/web/{name}@{gross}.jpg {gross}w" if hat_gross else ""
    return (f'<picture class="{klasse}">'
            f'<source type="image/webp" srcset="assets/img/web/{name}.webp 900w{gross_webp}"{sizes}>'
            f'<img src="assets/img/web/{name}.jpg" srcset="assets/img/web/{name}.jpg 900w{gross_jpg}"{sizes} '
            f'alt="{alt}" width="{breite}" height="{hoehe}" loading="{laden}" decoding="async">'
            f'</picture>')


# ===================================================================
# Seitenköpfe
# ===================================================================

def kopfbereich(titel, unterzeile=None):
    """Kopf ohne Bild. Überschrift im Original 130px."""
    unten = (f'\n            <p class="kopf-unterzeile auftritt">{unterzeile}</p>'
             if unterzeile else '')
    return f"""    <div class="kopfabstand"></div>

    <header class="bahn seitenkopf">
      <div class="s10">
        <div class="block">
          <h1 class="t-riesig titel auftritt">{titel}</h1>{unten}
        </div>
      </div>
      <div class="s2"></div>
    </header>"""


def bildkopf(bild, label, titel, absaetze, hinweis=None, mitte=False):
    """Seitenkopf mit großem Bild darüber. Überschrift im Original 72px."""
    text = "".join(f'<p class="bildkopf__text auftritt">{a}</p>' for a in absaetze)
    marke = f'<p class="t-label bildkopf__marke auftritt">{label}</p>' if label else ''
    schild = f'<p class="t-label schild auftritt">{hinweis}</p>' if hinweis else ''
    zentriert = " bildkopf--mitte" if mitte else ""
    return f"""    <div class="kopfabstand kopfabstand--klein"></div>

    <header class="bildkopf{zentriert}">
      <div class="bildkopf__bild">
        {bild_tag(bild, "", 1440, 1400, "", "eager", "100vw")}
      </div>
      <div class="bahn bildkopf__zeile">
        <div class="s8">
          <div class="block bildkopf__innen">
            {marke}
            <h1 class="t-h1 auftritt">{titel}</h1>
            {text}
            {schild}
          </div>
        </div>
        <div class="s4"></div>
      </div>
    </header>"""


# ===================================================================
# Text- und Bildabschnitte
# ===================================================================

def leitsatz(label, absaetze, id=None, titel=None, gross=True, titel_klasse="t-h2"):
    """Marke, Überschrift und Fließtext, wie der Einstieg im Original."""
    kennung = f' id="{id}"' if id else ''
    klasse = "t-h5 " if gross else ""
    def absatz(a):
        if isinstance(a, tuple) and a[0] == "merk":
            return f'<p class="leitsatz__merk auftritt">{a[1]}</p>'
        return f'<p class="{klasse}auftritt">{a}</p>'
    text = "\n            ".join(absatz(a) for a in absaetze)
    marke = f'<p class="t-label leitsatz__marke auftritt">{label}</p>\n            ' if label else ''
    if titel:
        marke += f'<h2 class="{titel_klasse} leitsatz__titel auftritt">{titel}</h2>\n            '
    return f"""    <section class="bahn leitsatz"{kennung}>
      <div class="s3"></div>
      <div class="s9">
        <div class="block leitsatz__text">
            {marke}{text}
        </div>
      </div>
    </section>"""


def bild_zitat(bild, alt, zitat, quelle):
    return f"""    <section class="bahn bild-zitat">
      <div class="s5">
        <div class="block">
          <figure class="bildrahmen bildrahmen--bogen auftritt">
            {bild_tag(bild, alt, 1104, 1472, "", "lazy", "(max-width: 809px) 90vw, 40vw", True, 1104)}
          </figure>
        </div>
      </div>
      <div class="s1"></div>
      <div class="s6">
        <div class="block zitatblock">
          <blockquote class="auftritt">
            <p class="t-h4">{zitat}</p>
          </blockquote>
          <p class="t-label zitat__quelle auftritt">{quelle}</p>
        </div>
      </div>
    </section>"""


def grosser_satz(absaetze):
    text = "\n          ".join(f'<p class="t-h2 auftritt">{a}</p>' for a in absaetze)
    return f"""    <section class="bahn grossersatz">
      <div class="s3"></div>
      <div class="s9">
        <div class="block">
          {text}
        </div>
      </div>
    </section>"""


def kompetenzen(titel, einleitung, eintraege, gruppen=None, id=None):
    """Die Kompetenzen, in Felder geordnet und fortlaufend nummeriert.

    Ohne `gruppen` bleibt es bei der einfachen Liste. Mit `gruppen`
    entsteht je Feld eine Überschrift und darunter ein Raster.
    """
    kennung = f' id="{id}"' if id else ''
    vor = "\n            ".join(f'<p class="auftritt">{a}</p>' for a in einleitung)

    def eintrag(nr, name, text):
        return (f'<article class="koennen__eintrag auftritt">'
                f'<span class="koennen__nr" aria-hidden="true">{nr:02d}</span>'
                f'<h4 class="koennen__name">{name}</h4>'
                f'<p class="t-klein koennen__text">{text}</p></article>')

    if gruppen:
        teile, nr = [], 0
        for feld, (feldtitel, feldzeile, plaetze) in enumerate(gruppen, start=1):
            karten = []
            for platz in plaetze:
                nr += 1
                karten.append(eintrag(nr, *eintraege[platz]))
            teile.append(
                f'<section class="koennen__feld">\n'
                f'              <header class="koennen__feld-kopf auftritt">\n'
                f'                <p class="t-label koennen__feld-marke">Feld {feld}</p>\n'
                f'                <h3 class="koennen__feld-titel">{feldtitel}</h3>\n'
                f'                <p class="t-klein koennen__feld-zeile">{feldzeile}</p>\n'
                f'              </header>\n'
                f'              <div class="koennen__feld-raster">' + "".join(karten) + '</div>\n'
                f'            </section>')
        liste = "\n            ".join(teile)
    else:
        liste = "\n            ".join(
            eintrag(n, name, text) for n, (name, text) in enumerate(eintraege, start=1))

    anzahl = len(eintraege)
    return f"""    <section class="bahn koennen"{kennung} aria-labelledby="koennen-titel">
      <div class="s3">
        <div class="block koennen__kopf">
          <p class="t-label koennen__marke auftritt">{anzahl} Ausbildungen</p>
          <h2 class="t-h2 auftritt" id="koennen-titel">{titel}</h2>
        </div>
      </div>
      <div class="s9">
        <div class="block koennen__spalte">
            {vor}
            {liste}
        </div>
      </div>
    </section>"""


def aufruf(titel, absaetze, knopf_text, knopf_ziel):
    text = "\n            ".join(f'<p class="auftritt">{a}</p>' for a in absaetze)
    return f"""    <section class="aufruf">
      <div class="bahn aufruf__zeile">
        <div class="s2"></div>
        <div class="s8">
          <div class="block aufruf__innen">
            <h2 class="t-h2 auftritt">{titel}</h2>
            {text}
            <a class="pille pille--gruen t-label auftritt" href="{knopf_ziel}"><span class="pille__punkt pille__punkt--b"></span>{knopf_text}<span class="pille__punkt pille__punkt--a"></span></a>
          </div>
        </div>
        <div class="s2"></div>
      </div>
    </section>"""


# ===================================================================
# Startseite
# ===================================================================

def hero(bild, titel, unterzeile, knopf_text, knopf_ziel):
    """Hero: Grundton, Naturfoto (Seebensee), Kreise, Lesbarkeitsverlauf.

    Der Titel wird zeilenweise maskiert, die Zeilen steigen nacheinander
    aus unsichtbaren Kanten auf (Fassung 2)."""
    zeilen = "".join(f'<span class="zeile"><span>{z.strip()}</span></span>'
                     for z in titel.split("<br>"))
    return f"""    <section class="hero">
      <div class="hero__cue" aria-hidden="true"><span></span></div>
      <div class="hero__lagen" aria-hidden="true">
        <div class="hero__grund"></div>
        <div class="hero__foto">
          {bild_tag(bild, "", 1440, 900, "", "eager", "100vw")}
        </div>
        <div class="hero__kreise">
          <span class="hero__kreis hero__kreis--a"></span>
          <span class="hero__kreis hero__kreis--b"></span>
          <span class="hero__kreis hero__kreis--c"></span>
        </div>
        <div class="hero__schleier"></div>
      </div>
      <div class="bahn hero__zeile">
        <div class="s8">
          <div class="block hero__text">
            <h1 class="t-h1 hero__titel">{zeilen}</h1>
            <p class="hero__unterzeile">{unterzeile}</p>
            <a class="pille pille--weiss t-label" href="{knopf_ziel}"><span class="pille__punkt pille__punkt--b"></span>{knopf_text}<span class="pille__punkt pille__punkt--a"></span></a>
          </div>
        </div>
        <div class="s4"></div>
      </div>
    </section>"""


def karten(label, titel, unterzeile, eintraege, knoepfe):
    """Angebotsvorschau. Überschrift im Original 76px, Kartentitel 34px."""
    # Die Karten reagierten beim Überfahren und taten beim Klick nichts.
    # Jetzt führt die Überschrift auf den zugehörigen Abschnitt der
    # Angebotsseite, und die ganze Karte ist über diesen Verweis greifbar.
    karten_html = "\n          ".join(
        f'<article class="karte karte--klick karte--{b} auftritt">'
        f'<div class="karte__bild">{bild_tag(b, alt, 377, 560, "", "lazy", "(max-width: 809px) 90vw, 377px", False)}</div>'
        f'<h3 class="karte__titel"><a class="karte__ziel" href="{z}">{h}</a></h3>'
        f'<p class="t-klein karte__text">{t}</p>'
        f'</article>'
        for b, alt, h, t, z in eintraege)
    kn = "\n          ".join(
        f'<a class="pille pille--{art} t-label auftritt" href="{ziel}"><span class="pille__punkt pille__punkt--b"></span>{txt}<span class="pille__punkt pille__punkt--a"></span></a>'
        for txt, ziel, art in knoepfe)
    return f"""    <section class="angebote" aria-labelledby="angebote-titel">
      <div class="bahn angebote__kopf">
        <div class="s8">
          <div class="block">
            <p class="t-label leitsatz__marke auftritt">{label}</p>
            <h2 class="t-gross auftritt" id="angebote-titel">{titel}</h2>
            <p class="angebote__unterzeile auftritt">{unterzeile}</p>
          </div>
        </div>
        <div class="s4"></div>
      </div>
      <div class="bahn">
        <div class="karten">
          {karten_html}
        </div>
      </div>
      <div class="bahn angebote__knoepfe">
        <div class="block knopfreihe">
          {kn}
        </div>
      </div>
    </section>"""


def schritte(titel, unterzeile, eintraege):
    """Wie im Original: Text links, rechts eine riesige Ziffer, die beim
    Scrollen von Schritt zu Schritt weiterrollt (sticky Rollfenster).
    Auf schmalen Geräten steht stattdessen eine kleine Ziffer im Schritt."""
    bloecke = "\n          ".join(
        f'<article class="schritt" data-nr="{i-1}">'
        f'<p class="schritt__mini" aria-hidden="true">{i:02d}</p>'
        f'<div class="schritt__inhalt auftritt">'
        f'<h3 class="t-h1 schritt__titel">{h}</h3>'
        + "".join(f'<p>{a}</p>' for a in absaetze) +
        f'</div></article>'
        for i, (h, absaetze) in enumerate(eintraege, start=1))
    ziffern = "".join(f'<span>{i}</span>' for i in range(1, len(eintraege) + 1))
    return f"""    <section class="ablauf" aria-labelledby="ablauf-titel">
      <div class="bahn">
        <div class="s8">
          <div class="block ablauf__kopf">
            <h2 class="t-riesig auftritt" id="ablauf-titel">{titel}</h2>
            <p class="t-h5 auftritt">{unterzeile}</p>
          </div>
        </div>
        <div class="s4"></div>
      </div>
      <div class="bahn ablauf__zeile">
        <div class="ablauf__schritte">
          {bloecke}
        </div>
        <div class="ablauf__rolle" aria-hidden="true">
          <div class="rolle__fenster"><div class="rolle__stapel">{ziffern}</div></div>
        </div>
      </div>
    </section>"""


def preise(label, titel, unterzeile, karten_daten, zentriert=False):
    karten_html = "\n          ".join(
        f'<article class="preis auftritt{" preis--hervor" if hervor else ""}">'
        + ('<p class="preis__badge t-label">Beliebteste Wahl</p>' if hervor else '')
        + f'<h3 class="preis__titel">{h}</h3>'
        f'<p class="t-klein preis__dauer">{dauer}</p>'
        f'<p class="t-h2 preis__betrag">{betrag}</p>'
        f'<ul class="preis__liste">' + "".join(f'<li>{p}</li>' for p in punkte) + '</ul>'
        f'<a class="pille pille--{"gruen" if hervor else "weiss"} t-label preis__knopf" href="session-buchen.html">'
        f'<span class="pille__punkt pille__punkt--b"></span>Jetzt buchen<span class="pille__punkt pille__punkt--a"></span></a>'
        f'<p class="t-klein preis__hinweis">{hinweis}</p>'
        f'</article>'
        for h, dauer, betrag, punkte, hinweis, hervor in karten_daten)
    mitte = " preise__kopf--mitte" if zentriert else ""
    return f"""    <section class="preise" aria-labelledby="preise-titel">
      <div class="bahn preise__kopf{mitte}">
        <div class="s8">
          <div class="block">
            <p class="t-label leitsatz__marke auftritt">{label}</p>
            <h2 class="t-h2 auftritt" id="preise-titel">{titel}</h2>
            <p class="auftritt">{unterzeile}</p>
          </div>
        </div>
        <div class="s4"></div>
      </div>
      <div class="bahn">
        <div class="preise__reihe">
          {karten_html}
        </div>
      </div>
    </section>"""


def breitbild(bild, alt, titel, absaetze, zitat=None, quelle=None):
    """Im Original steht die Überschrift über dem Bild, nicht darunter.

    Liegt ein Zitat an, steht es im Bild selbst, auf einem Schleier, der
    es lesbar hält. Es braucht dann keinen eigenen dunklen Block mehr.
    """
    text = "".join(f'<p>{a}</p>' for a in absaetze)
    spruch = ""
    if zitat:
        herkunft = (f'\n          <figcaption class="t-label breitbild__quelle">{quelle}</figcaption>'
                    if quelle else "")
        spruch = (f'\n        <figure class="breitbild__spruch">'
                  f'\n          <blockquote><p class="t-h2">{zitat}</p></blockquote>'
                  f'{herkunft}\n        </figure>')
    return f"""    <section class="breitbild">
      <div class="bahn breitbild__zeile">
        <div class="s2"></div>
        <div class="s8">
          <div class="block breitbild__text auftritt">
            <h2 class="t-h2">{titel}</h2>
            {text}
          </div>
        </div>
        <div class="s2"></div>
      </div>
      <div class="breitbild__bild auftritt fenster{" breitbild__bild--spruch" if zitat else ""}">
        {bild_tag(bild, alt, 1440, 1580, "", "lazy", "100vw")}{spruch}
      </div>
    </section>"""


def grosses_zitat(zitat, quelle):
    return f"""    <section class="grosszitat">
      <div class="bahn">
        <div class="s2"></div>
        <div class="s8">
          <div class="block grosszitat__innen auftritt">
            <blockquote><p class="t-h1">{zitat}</p></blockquote>
            <p class="t-label grosszitat__quelle">{quelle}</p>
          </div>
        </div>
        <div class="s2"></div>
      </div>
    </section>"""


def zahlen(titel, unterzeile, eintraege):
    liste = "\n          ".join(
        f'<div class="zahl auftritt"><p class="zahl__wert">{wert}</p>'
        f'<p class="t-klein zahl__text">{text}</p></div>'
        for wert, text in eintraege)
    return f"""    <section class="zahlen" aria-labelledby="zahlen-titel">
      <div class="bahn zahlen__kopf">
        <div class="s7">
          <div class="block">
            <h2 class="t-h2 auftritt" id="zahlen-titel">{titel}</h2>
          </div>
        </div>
        <div class="s1"></div>
        <div class="s4">
          <div class="block">
            <p class="t-klein auftritt">{unterzeile}</p>
          </div>
        </div>
      </div>
      <div class="bahn">
        <div class="zahlen__reihe">
          {liste}
        </div>
      </div>
    </section>"""


def stimmen(label, titel, eintraege):
    liste = "\n          ".join(
        f'<figure class="stimme auftritt">'
        f'<p class="stimme__zeichen" aria-hidden="true">&ldquo;</p>'
        f'<blockquote><p class="t-klein">{text}</p></blockquote>'
        f'<figcaption class="stimme__wer"><span class="stimme__name">{name}</span>'
        f'<span class="t-klein stimme__ort">{ort}</span></figcaption>'
        f'</figure>'
        for text, name, ort in eintraege)
    return f"""    <section class="stimmen" aria-labelledby="stimmen-titel">
      <div class="bahn stimmen__kopf">
        <div class="s8">
          <div class="block">
            <p class="t-label leitsatz__marke auftritt">{label}</p>
            <h2 class="t-h2 auftritt" id="stimmen-titel">{titel}</h2>
          </div>
        </div>
        <div class="s4"></div>
      </div>
      <div class="bahn">
        <div class="stimmen__gitter">
          {liste}
        </div>
      </div>
    </section>"""


# ===================================================================
# Angebote
# ===================================================================

def angebot(bild, titel, unterzeile, absaetze, eckdaten, knopf_text, knopf_ziel, kennung,
            badge=None):
    """Ein Angebotsblock. Im Original volle Breite, 88px Rand, Überschrift 84px."""
    text = "".join(f'<p>{a}</p>' for a in absaetze)
    badge_html = f'<p class="angebot__badge t-label auftritt">{badge}</p>' if badge else ''
    daten = "".join(f'<li><span class="eck__name">{n}</span><span class="eck__wert">{w}</span></li>'
                    for n, w in eckdaten)
    bildteil = (f'<div class="angebot__bild auftritt fenster">{bild_tag(bild, "", 1440, 1580, "", "lazy", "100vw")}</div>'
                if bild else '')
    return f"""    <section class="angebot" id="{kennung}" aria-labelledby="{kennung}-t">
      {bildteil}
      <div class="angebot__innen">
        {badge_html}<h2 class="t-angebot auftritt" id="{kennung}-t">{titel}</h2>
        <p class="angebot__unterzeile auftritt">{unterzeile}</p>
        <div class="angebot__text auftritt">{text}</div>
        <ul class="eckdaten auftritt">{daten}</ul>
        <a class="pille pille--gruen t-label auftritt" href="{knopf_ziel}"><span class="pille__punkt pille__punkt--b"></span>{knopf_text}<span class="pille__punkt pille__punkt--a"></span></a>
      </div>
    </section>"""


def hinweisblock(titel, absaetze):
    text = "".join(f'<p class="t-klein">{a}</p>' for a in absaetze)
    return f"""    <section class="hinweis">
      <div class="bahn">
        <div class="s3"></div>
        <div class="s9">
          <div class="block hinweis__innen auftritt">
            <h2 class="t-label hinweis__titel">{titel}</h2>
            {text}
          </div>
        </div>
      </div>
    </section>"""


# ===================================================================
# Initiationen
# ===================================================================

def initiationen(label, titel, absaetze, karten_titel, karten_intro, eintraege, schluss,
                 nebentitel=None):
    """Im Original: Überschrift links, Nebentitel rechts, beides mittig gesetzt."""
    text = "".join(f'<p class="t-h5 auftritt">{a}</p>' for a in absaetze)
    neben = (f'<div class="lichtkoerper__neben">'
             f'<p class="t-label leitsatz__marke auftritt">{label}</p>'
             f'<h3 class="lichtkoerper__nebentitel auftritt">{nebentitel}</h3></div>'
             if nebentitel else '')
    karten_html = "\n          ".join(
        f'<article class="initiation auftritt">'
        f'<p class="t-label initiation__nr">{nr}</p>'
        f'<h3 class="initiation__titel">{h}</h3>'
        f'<p class="t-klein initiation__text">{t}</p>'
        f'<p class="t-label initiation__stand">{stand}</p>'
        f'</article>'
        for nr, h, t, stand in eintraege)
    schlusstext = "".join(f'<p class="auftritt">{a}</p>' for a in schluss)
    return f"""    <section class="lichtkoerper" aria-labelledby="lk-titel">
      <div class="lichtkoerper__zeile">
        <div class="lichtkoerper__haupt">
          <h2 class="lichtkoerper__titel auftritt" id="lk-titel">{titel}</h2>
        </div>
        {neben}
      </div>
      <div class="lichtkoerper__text">
        {text}
      </div>
    </section>

    <section class="raeume" aria-labelledby="raeume-titel">
      <div class="raeume__kopf">
        <h2 class="t-h2 auftritt" id="raeume-titel">{karten_titel}</h2>
        <p class="raeume__intro auftritt">{karten_intro}</p>
      </div>
      <div class="bahn">
        <div class="raeume__gitter">
          {karten_html}
        </div>
      </div>
      <div class="raeume__schluss">
        <div class="raeume__schlusstext">{schlusstext}</div>
      </div>
    </section>"""


# ===================================================================
# Buchung
# ===================================================================

def buchung(label, titel, unterzeile, einleitung, absaetze, wege_titel, wege, mail, stufe=2):
    wege_html = "".join(
        f'<label class="wahl"><input type="radio" name="Begleitung" value="{w}"><span>{w}</span></label>'
        for w in wege)
    text = "".join(f'<p>{a}</p>' for a in absaetze)
    return f"""    <section class="buchung" aria-labelledby="buchung-titel">
      <div class="bahn buchung__kopf">
        <div class="s8">
          <div class="block">
            <p class="t-label buchung__marke auftritt">{label}</p>
            <h{stufe} class="t-h1 buchung__titel auftritt" id="buchung-titel">{titel}</h{stufe}>
            <p class="t-h5 buchung__unterzeile auftritt">{unterzeile}</p>
          </div>
        </div>
        <div class="s4"></div>
      </div>

      <div class="bahn buchung__zeile">
        <div class="s6">
          <div class="block buchung__text auftritt">
            <h3 class="t-h5">{einleitung}</h3>
            {text}
          </div>
        </div>
        <div class="s1"></div>
        <div class="s5">
          <div class="block">
            <form class="formular auftritt" name="session" method="post" data-buchung
                  data-netlify="true" netlify-honeypot="firmenname">
              <input type="hidden" name="form-name" value="session">
              <p class="honigtopf" aria-hidden="true">
                <label>Bitte leer lassen: <input name="firmenname" tabindex="-1" autocomplete="off"></label>
              </p>
              <p class="t-label formular__wegetitel">{wege_titel}</p>
              <div class="wahlen">{wege_html}</div>

              <div class="feld">
                <label for="b-name">Dein Name</label>
                <input id="b-name" name="Name" type="text" autocomplete="name" required>
              </div>
              <div class="feld">
                <label for="b-mail">Deine E-Mail-Adresse</label>
                <input id="b-mail" name="Email" type="email" autocomplete="email" required>
              </div>
              <div class="feld">
                <label for="b-text">Erzähle mir von dir</label>
                <textarea id="b-text" name="Nachricht" rows="5"></textarea>
              </div>

              <label class="zustimmung">
                <input type="checkbox" name="Newsletter" value="ja">
                <span class="t-klein">Ja, ich möchte Impulse erhalten. Kostenlose tiefe Impulse zur inneren Entwicklung, Einblicke aus der Arbeit und neue Angebote.</span>
              </label>

              <button class="pille pille--gruen t-label formular__knopf" type="submit"><span class="pille__punkt pille__punkt--b"></span>Session anfragen<span class="pille__punkt pille__punkt--a"></span></button>
              <p class="t-klein formular__meldung" data-buchung-meldung role="status"></p>
              <p class="t-klein formular__fussnote">Lieber erst schreiben? <a href="mailto:{mail}">Schicke mir eine E-Mail</a></p>
            </form>
          </div>
        </div>
      </div>
    </section>"""


def ornament():
    """Feiner Trenner: zwei auslaufende Linien, dazwischen der Goldpunkt."""
    return ('    <div class="ornament-trenner auftritt" aria-hidden="true">'
            '<span></span></div>')


def programm_nav(eintraege):
    """Ankerleiste zu den Programmen, direkt unter dem Seitenkopf."""
    links = "".join(f'<a href="{ziel}">{text}</a>' for text, ziel in eintraege)
    return (f'    <nav class="programm-nav auftritt" aria-label="Programme">{links}</nav>')


def kauf_leiste():
    """Feine feste Leiste am unteren Rand: der risikofreie Einstieg.

    Erscheint erst nach dem ersten Scrollen und verschwindet, sobald das
    Buchungsformular im Bild ist."""
    return ('    <div class="kaufleiste" data-kaufleiste>'
            '<p class="kaufleiste__text t-klein">Kennenlerngespräch — unverbindlich und kostenfrei</p>'
            '<a class="pille pille--gruen t-label" href="session-buchen.html">'
            '<span class="pille__punkt pille__punkt--b"></span>Session anfragen'
            '<span class="pille__punkt pille__punkt--a"></span></a></div>')


def inhaltsseite(*abschnitte):
    return "\n\n".join(abschnitte)


# ===================================================================
# Schöpferwerke, eigener Aufbau
# ===================================================================

def akademie(bild, titel, zitat, quelle, absaetze, knopf_text, knopf_ziel):
    """Eigener Aufbau: großes Bild, Überschrift 130px, Zitat 54px.

    Ein Absatz darf als ("auftakt", ...) oder ("kern", ...) ausgezeichnet
    sein. Der Auftakt steht größer, der Kernsatz wird als eigene Stufe
    aus dem Fließtext gehoben.
    """
    def absatz(a):
        if isinstance(a, tuple):
            art, wort = a
            if art == "auftakt":
                return f'<p class="akademie__auftakt">{wort}</p>'
            if art == "kern":
                return ('<div class="akademie__kern">'
                        '<span class="akademie__kern-zier" aria-hidden="true"></span>'
                        f'<p>{wort}</p>'
                        '<span class="akademie__kern-zier" aria-hidden="true"></span>'
                        '</div>')
        return f'<p>{a}</p>'
    text = "".join(absatz(a) for a in absaetze)
    return f"""    <div class="kopfabstand kopfabstand--klein"></div>

    <header class="akademie">
      <div class="akademie__bild">
        {bild_tag(bild, "", 1440, 2125, "", "eager", "100vw")}
      </div>
      <div class="akademie__innen">
        <h1 class="t-riesig akademie__titel auftritt">{titel}</h1>

        <blockquote class="akademie__zitat auftritt">
          <p>{zitat}</p>
          <footer class="akademie__quelle">{quelle}</footer>
        </blockquote>

        <div class="akademie__text auftritt">{text}</div>

        <a class="pille pille--gruen t-label akademie__knopf auftritt" href="{knopf_ziel}"><span class="pille__punkt pille__punkt--b"></span>{knopf_text}<span class="pille__punkt pille__punkt--a"></span></a>
      </div>
    </header>"""
