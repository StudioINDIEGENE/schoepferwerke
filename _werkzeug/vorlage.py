# -*- coding: utf-8 -*-
"""
Gemeinsame Vorlage für alle Seiten von Schöpferwerke.

Kopfbereich, Navigation, Menü, Wellen, FAQ und Fußzeile stehen hier ein
einziges Mal. Die einzelnen Seiten liefern nur ihren Inhalt.
So bleibt die Navigation an einer Stelle pflegbar, obwohl am Ende ganz
gewöhnliche, einzeln bearbeitbare HTML-Dateien herauskommen.
"""

SEITEN = [
    ("index.html",          "Startseite"),
    ("ueber-mich.html",     "Über mich"),
    ("angebote.html",       "Angebote"),
    ("initiationen.html",   "Initiationen"),
    ("session-buchen.html", "Session buchen"),
    ("schoepferwerke.html", "Schöpferwerke"),
    ("datenschutz.html",    "Datenschutz"),
    ("impressum.html",      "Impressum"),
    ("agb.html",            "AGB"),
]

MARKE = "Schöpferwerke der Agnes Aichholzer"
BASIS = "https://schoepferwerke.com"

# Solange die Seite noch auf Netlify zur Ansicht liegt, muss das Vorschaubild
# von dort kommen, sonst zeigt WhatsApp beim Weiterschicken kein Bild.
# Beim Umzug auf die eigene Adresse hier BASIS eintragen.
MEDIEN_BASIS = "https://schoepferwerke.netlify.app"
MAIL = "info@schoepferwerke.com"

WELLE_A = ("M 258.784 6000 C 172.776 5764.462 179.274 5473.637 486.263 5396.38 C 793.252 5319.123 "
"193.717 5766.427 155.057 5396.38 C 116.397 5026.333 836.552 5059.991 503.173 5016.262 C 169.794 "
"4972.533 588.875 4239.813 111.673 4606.955 C -365.528 4974.097 868.694 4380.924 425.173 4153.115 "
"C -18.348 3925.306 495.457 3731.808 212.173 3671.253 C -71.111 3610.699 806.443 4132.952 470.173 "
"3549 C 133.903 2965.048 112.591 2946.818 288.673 2985.5 C 464.755 3024.182 789.478 2831.518 "
"444.173 2530.898 C 98.868 2230.278 467.924 2108.466 567.173 2174.631 C 666.422 2240.796 258.499 "
"2410.716 168.173 2057.543 C 77.848 1704.371 457.414 2103.673 567.173 1974.481 C 676.933 1845.289 "
"467.466 1586.488 285.673 1672.254 C 103.88 1758.021 546.582 1614.947 339.423 1156.868 C 132.265 "
"698.788 405.515 832.674 425.173 927.195 C 444.831 1021.717 66.831 857.513 198.173 661.496 C "
"329.515 465.48 864.701 458.221 486.173 630 C 107.645 801.779 -173.336 422.329 204.673 284.5 C "
"582.682 146.671 339.423 0 339.423 0")

WELLE_B = ("M 266.813 6000 C 69.979 5600.924 301.736 5453.954 468.313 5414.5 C 634.89 5375.046 "
"489.208 5577.549 286.813 5545 C 84.419 5512.451 147.193 5157.619 413.167 5106.853 C 679.14 "
"5056.087 396.509 5120.799 365.184 4875.408 C 333.859 4630.017 400.707 4367.333 158.757 4545.561 "
"C -83.193 4723.789 -35.114 4837.426 211.738 4634.926 C 458.591 4432.426 758.721 4327.402 427.661 "
"4127.353 C 96.602 3927.305 396.36 3835.353 317.201 3727.219 C 238.041 3619.086 5.572 3641.137 "
"328.313 3791.5 C 651.055 3941.863 585.19 3811.107 345.691 3332.106 C 106.191 2853.106 216.714 "
"2985.692 413.167 2985.692 C 609.619 2985.692 671.66 2735.252 453.652 2561.961 C 235.644 2388.671 "
"218.585 2185.802 453.652 2166.346 C 688.72 2146.889 597.002 2252.713 468.147 2269.768 C 339.292 "
"2286.824 279.82 2251.783 211.738 2176.387 C 143.656 2100.991 25.115 1804.448 365.184 1955.485 C "
"705.253 2106.522 665.324 1621.971 386.676 1655.259 C 108.028 1688.547 329.372 1713.387 413.167 "
"1437.369 C 496.961 1161.352 156.457 941.144 254.723 842.44 C 352.989 743.736 530.053 1098.155 "
"345.691 980.002 C 161.329 861.848 70.663 676.487 274.216 558.28 C 477.769 440.072 823.225 "
"471.296 413.167 630.073 C 3.108 788.85 -61.485 387.104 211.738 300.226 C 484.961 213.348 483.079 "
"73.199 328.197 0")

PLUS = ("M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,"
"88.1,0,0,1,128,216Zm48-88a8,8,0,0,1-8,8H136v32a8,8,0,0,1-16,0V136H88a8,8,0,0,1,0-16h32V88a8,8,0,"
"0,1,16,0v32h32A8,8,0,0,1,176,128Z")

SOZIAL = [
    ("https://instagram.com", "Instagram",
     "M128,80a48,48,0,1,0,48,48A48.05,48.05,0,0,0,128,80Zm0,80a32,32,0,1,1,32-32A32,32,0,0,1,128,"
     "160ZM176,24H80A56.06,56.06,0,0,0,24,80v96a56.06,56.06,0,0,0,56,56h96a56.06,56.06,0,0,0,56-56"
     "V80A56.06,56.06,0,0,0,176,24Zm40,152a40,40,0,0,1-40,40H80a40,40,0,0,1-40-40V80A40,40,0,0,1,"
     "80,40h96a40,40,0,0,1,40,40ZM192,76a12,12,0,1,1-12-12A12,12,0,0,1,192,76Z"),
    ("https://www.threads.com/", "Threads",
     "M186.42,123.65a63.81,63.81,0,0,0-11.13-6.72c-4-29.89-24-39.31-33.1-42.07-19.78-6-42.51,1.19-"
     "52.85,16.7a8,8,0,0,0,13.32,8.88c6.37-9.56,22-14.16,34.89-10.27,9.95,3,16.82,10.3,20.15,21a81"
     ".05,81.05,0,0,0-15.29-1.43c-13.92,0-26.95,3.59-36.67,10.1C94.3,127.57,88,139,88,152c0,20.58,"
     "15.86,35.52,37.71,35.52a48,48,0,0,0,34.35-14.81c6.44-6.7,14-18.36,15.61-37.1.38.26.74.53,"
     "1.1.8C186.88,144.05,192,154.68,192,168c0,19.36-20.34,48-64,48-26.73,0-45.48-8.65-57.34-26.44"
     "C60.93,175,56,154.26,56,128s4.93-47,14.66-61.56C82.52,48.65,101.27,40,128,40c32.93,0,54,"
     "13.25,64.53,40.52a8,8,0,1,0,14.93-5.75C194.68,41.56,167.2,24,128,24,96,24,72.19,35.29,57.34,"
     "57.56,45.83,74.83,40,98.52,40,128s5.83,53.17,17.34,70.44C72.19,220.71,96,232,128,232c30.07,"
     "0,48.9-11.48,59.4-21.1C200.3,199.08,208,183,208,168,208,149.66,200.54,134.32,186.42,123.65Zm"
     "-37.89,38a31.94,31.94,0,0,1-22.82,9.9c-10.81,0-21.71-6-21.71-19.52,0-12.63,12-26.21,38.41-26"
     ".21A63.88,63.88,0,0,1,160,128.24C160,142.32,156,153.86,148.53,161.62Z"),
    ("https://facebook.com", "Facebook",
     "M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm8,191.63V152h24a8,8,0,0,0,0-16H136"
     "V112a16,16,0,0,1,16-16h16a8,8,0,0,0,0-16H152a32,32,0,0,0-32,32v24H96a8,8,0,0,0,0,16h24v63.63"
     "a88,88,0,1,1,16,0Z"),
    ("https://youtube.com", "YouTube",
     "M164.44,121.34l-48-32A8,8,0,0,0,104,96v64a8,8,0,0,0,12.44,6.66l48-32a8,8,0,0,0,0-13.32ZM120,"
     "145.05V111l25.58,17ZM234.33,69.52a24,24,0,0,0-14.49-16.4C185.56,39.88,131,40,128,40s-57.56-."
     "12-91.84,13.12a24,24,0,0,0-14.49,16.4C19.08,79.5,16,97.74,16,128s3.08,48.5,5.67,58.48a24,24,"
     "0,0,0,14.49,16.41C69,215.56,120.4,216,127.34,216h1.32c6.94,0,58.37-.44,91.18-13.11a24,24,0,"
     "0,0,14.49-16.41c2.59-10,5.67-28.22,5.67-58.48S236.92,79.5,234.33,69.52Zm-15.49,113a8,8,0,0,"
     "1-4.77,5.49c-31.65,12.22-85.48,12-86,12H128c-.54,0-54.33.2-86-12a8,8,0,0,1-4.77-5.49C34.8,"
     "173.39,32,156.57,32,128s2.8-45.39,5.16-54.47A8,8,0,0,1,41.93,68c30.52-11.79,81.66-12,85.85-"
     "12h.27c.54,0,54.38-.18,86,12a8,8,0,0,1,4.77,5.49C221.2,82.61,224,99.43,224,128S221.2,173.39,"
     "218.84,182.47Z"),
]

# Die Fragen sind auf allen Seiten dieselben. Antworten im Wortlaut der Kundin.
FAQ = [
 ("Für wen ist diese Arbeit geeignet?", [
  "Diese Arbeit ist für dich, wenn du bereit bist, dein Leben selbst in die Hand zu nehmen und "
  "dich an deiner inneren Wahrheit zu orientieren. Meine Arbeit führt dich zurück in die "
  "Verbindung mit dir selbst. Wenn du schon vieles versucht hast und spürst, dass oberflächliche "
  "Lösungen nicht mehr greifen — und wenn du bereit bist, dir selbst in der Tiefe zu begegnen und "
  "zu heilen, dann bist du hier genau richtig. Mit über 25 Jahren Erfahrung halte ich einen Raum, "
  "in dem sich dein System in seine ursprüngliche Ordnung zurückbewegt. Viele meiner Kund kommen "
  "genau deshalb — weil sie bereits viel ausprobiert haben und spüren, dass es tiefer gehen darf."]),
 ("Was passiert in einer Session?", [
  "Jede Session ist individuell. Es gibt kein festes Schema — wir arbeiten mit dem, was sich in "
  "dir zeigt. Ich öffne einen klaren Raum und verbinde mich mit deinem Feld. Daraus wird sichtbar, "
  "was in dir bereit ist, erkannt, gelöst und neu ausgerichtet zu werden.",
  "Ich arbeite direkt auf ursächlicher Ebene im Feld. Blockierende Strukturen, alte Prägungen und "
  "tief sitzende Muster werden erkannt und gelöst, während sich dein System neu ausrichtet. In "
  "diesem Prozess geschieht eine feine Einstimmung deiner Seelenessenz in deinen physischen "
  "Körper, sowie die Aktivierung deiner inneren Ordnungsenergie.",
  "Dabei können sich alte Spannungen lösen, abgespaltene Anteile integrieren und eine neue innere "
  "Stabilität entstehen. Oft zeigen sich Themen, begrenzende Glaubenssätze, emotionale oder "
  "zelluläre Prägungen, Ahnenmuster, fragmentierte Seelenanteile oder karmische Verstrickungen. "
  "Wir bringen diese Ebenen ins Bewusstsein und lösen, was deinen natürlichen Energiefluss "
  "behindert.",
  "Durch diese tiefe Neuausrichtung findest du zurück in deine innere Ordnung. Deine Wahrnehmung "
  "wird klarer, deine innere Stimme wieder hörbar. Eine Orientierung entsteht, die nicht im Außen "
  "liegt — sondern aus deiner eigenen inneren Stimmigkeit entsteht – in Übereinstimmung mit deiner "
  "individuellen Seelennatur."]),
 ("Wie läuft eine Session konkret ab?", [
  "Die Session ist bewusst geführt und klar gehalten — sie entsteht individuell aus dem, was sich "
  "in dir zeigt. Wir beginnen mit einem kurzen Ankommen. Anschließend verbinde ich mich mit deinem "
  "Feld und nehme wahr, was bereit ist, gesehen, geklärt und transformiert zu werden. Daraus "
  "entwickelt sich der weitere Verlauf der Session intuitiv und präzise.",
  "Du darfst in diesem Raum sprechen, fühlen oder einfach da sein. Die Arbeit geschieht "
  "gleichzeitig auf mehreren Ebenen — energetisch, emotional, zellulär und im Bewusstsein. Viele "
  "erleben die Session als tief klärend. Als würde sich etwas im Inneren neu ordnen und aufrichten.",
  "Die Wirkung geht über die Session hinaus. Die neue Ausrichtung integriert sich weiter, wird im "
  "Alltag spürbar und entfaltet sich in deinem eigenen Rhythmus weiter."]),
 ("Wie viele Sessions brauche ich?", [
  "Das ist individuell. Manche Bewusstseinsschichten klären sich in einer Session, andere Prozesse "
  "entfalten sich über einen längeren Zeitraum. Je tiefer wir gehen und je mehr sich löst, desto "
  "näher kommst du deinem inneren Kern — und kannst ihn klar und ungefiltert im Alltag leben. Es "
  "geht um deine Wahrhaftigkeit. Und du bestimmst, wie weit du gehen möchtest. Für eine nachhaltige "
  "Integration und wirkliche, dauerhafte Veränderung begleite ich dich auf Wunsch über mehrere "
  "Wochen."]),
 ("Was kann sich durch die Arbeit verändern?", [
  "Veränderung zeigt sich bei jedem Menschen individuell — oft leiser und gleichzeitig tiefer, als "
  "es zunächst greifbar ist. Innere Klarheit entsteht. Alte emotionale Verstrickungen beginnen sich "
  "zu lösen. Deine Energie fließt wieder. Dein Ausdruck wird freier.",
  "Du triffst Entscheidungen nicht mehr aus Unsicherheit, sondern aus einer spürbaren inneren "
  "Stimmigkeit. Aufrichtig und echt. So nimmst du dich klarer wahr, spürst, was für dich stimmig "
  "ist und was nicht, und beginnst, deinen Weg aus dir heraus zu erkennen und zu gehen. Daraus "
  "entsteht Mut. Ein innerer Wille. Und die Fähigkeit, dein Leben aus deiner eigenen Kraft heraus "
  "zu gestalten."]),
 ("Spüre ich sofort eine Veränderung?", [
  "Oft ja — aber nicht immer so, wie man es erwartet. Manche Veränderungen sind direkt spürbar, "
  "andere entfalten sich leise in den Tagen danach. Dein System integriert das, was sich zeigt, in "
  "seinem eigenen Tempo. Meine Arbeit basiert nicht auf einer Methode. Ich arbeite direkt im Feld "
  "— dort, wo die Ursachen von Mustern, Blockaden und inneren Programmen liegt. Deshalb ist jede "
  "Sitzung einmalig."]),
 ("Ersetzt diese Arbeit eine Therapie oder ärztliche Behandlung?", [
  "Nein. Meine Arbeit dient der persönlichen Entwicklung, energetischen Balance und "
  "Bewusstseinsarbeit. Sie ersetzt keine medizinische, psychologische oder therapeutische "
  "Behandlung. Wenn du körperliche oder psychische Beschwerden hast, wende dich bitte an "
  "entsprechende Fachpersonen."]),
 ("Online oder in Präsenz — was ist möglich?", [
  "Beides ist möglich. Die meisten Sessions finden online via Zoom statt — die Arbeit wirkt "
  "unabhängig von Raum und Distanz. Sessions in Präsenz sind nach individueller Absprache möglich."]),
 ("Wie buche ich eine Session?", [
  "Die einmalige 1:1 Session kannst du direkt über die Website buchen. Für eine intensivere "
  "Begleitung über mehrere Wochen beginnen wir mit einem unverbindlichen Kennenlerngespräch. So "
  "stellen wir sicher, dass dieser Weg wirklich zu dir passt."]),
 ("Kann ich die Kosten erstatten lassen?", [
  "In der Regel nicht. Meine Angebote fallen in den Bereich der persönlichen Entwicklung und "
  "Bewusstseinsarbeit und werden nicht von Krankenkassen übernommen."]),
 ("Ich arbeite für die Seele.", [
  "Ich freue mich über dein Interesse – Wenn wir im Seelenkern wieder integer sind, beginnt sich "
  "unser gesamtes System neu zu ordnen. Wir kommen vollständig in unserer physischen Verkörperung "
  "an und unser angelegtes Seelenpotenzial kann bewusst gelebt werden. Aus dieser Kohärenz entsteht "
  "eine Kraft, die nicht gesucht werden muss — sie ist da und beginnt, sich durch dich "
  "auszudrücken. Das heißt Heimkehr in sich selbst und das ist das Ergebnis meiner Arbeit."]),
]


def marke_der_dateien():
    """Kurzzeichen aus dem Inhalt der Stilblätter und Skripte.

    Damit trägt jede Adresse automatisch eine neue Marke, sobald sich
    eine dieser Dateien ändert. Vorher stand dort eine feste Zahl, die
    beim Ändern vergessen wurde: Besucher bekamen altes CSS.
    """
    import hashlib
    import pathlib
    wurzel = pathlib.Path(__file__).resolve().parent.parent
    roh = b""
    for name in ("site.css", "site-v2.css", "site.js", "site-v2.js", "fonts.css"):
        datei = wurzel / "assets" / name
        if datei.is_file():
            roh += datei.read_bytes()
    return hashlib.sha1(roh).hexdigest()[:8]


VERSION = marke_der_dateien()


def pille(text, ziel=None, art="gruen", extra="", hier=False):
    tag = "a" if ziel else "button"
    attr = f'href="{ziel}"' if ziel else 'type="button"'
    if hier:
        attr += ' aria-current="page"'
    kl = f"pille pille--{art} t-label{(' ' + extra) if extra else ''}"
    return (f'<{tag} class="{kl}" {attr}>'
            f'<span class="pille__punkt pille__punkt--b"></span>{text}'
            f'<span class="pille__punkt pille__punkt--a"></span></{tag}>')


def menue_link(text, ziel, aktiv):
    hier = ' aria-current="page"' if ziel == aktiv else ''
    return f'<a href="{ziel}"{hier}>{text}</a>'


def kopf(aktiv, hell=False):
    def link(text, ziel):
        hier = ' aria-current="page"' if ziel == aktiv else ''
        return (f'<a class="menue-link t-label" href="{ziel}"{hier}>{text}'
                f'<span class="menue-link__linie"></span></a>')
    klasse = " kopf--hell" if hell else ""
    return f"""<header class="kopf{klasse}">
  <nav class="kopf__innen" aria-label="Hauptnavigation">
    <a class="marke" href="schoepferwerke.html">
      <span class="logo" aria-hidden="true">
        <span class="logo__schein"></span>
        <span class="logo__ring"><span class="logo__punkt"></span></span>
      </span>
      <span class="wortmarke">
        <span class="wortmarke__name">Schöpferwerke</span>
        <span class="wortmarke__zusatz">der Agnes Aichholzer</span>
      </span>
    </a>
    <div class="kopf__menue">
      {link('Startseite', 'index.html')}
      {link('Über mich', 'ueber-mich.html')}
      {link('Angebote', 'angebote.html')}
      {link('Initiationen', 'initiationen.html')}
      {pille('Session buchen', 'session-buchen.html', hier=(aktiv == 'session-buchen.html'))}
    </div>
    <button class="pille pille--gruen t-label kopf__schalter" type="button"
            data-menue-auf aria-expanded="false" aria-controls="menue">
      <span class="pille__punkt pille__punkt--b"></span>Menü<span class="pille__punkt pille__punkt--a"></span>
    </button>
  </nav>
</header>

<div class="kopfschleier" aria-hidden="true">
  <span></span><span></span><span></span><span></span>
  <span></span><span></span><span></span><span></span>
</div>

<div class="ueberlagerung" id="menue" data-offen="nein" role="dialog" aria-modal="true" aria-label="Menü" hidden>
  {pille('Schließen', None, 'gruen', 'ueberlagerung__schliessen').replace('<button class', '<button data-menue-zu class')}
  <nav class="ueberlagerung__liste" aria-label="Menü">
    {menue_link('Startseite', 'index.html', aktiv)}
    {menue_link('Über mich', 'ueber-mich.html', aktiv)}
    {menue_link('Angebote', 'angebote.html', aktiv)}
    {menue_link('Initiationen', 'initiationen.html', aktiv)}
    {menue_link('Die Schöpferwerke', 'schoepferwerke.html', aktiv)}
    {menue_link('Session buchen', 'session-buchen.html', aktiv)}
  </nav>
</div>"""


def wellen():
    return f"""  <div class="wellen" aria-hidden="true">
    <svg viewBox="0 0 6000 680" xmlns="http://www.w3.org/2000/svg">
      <path opacity="0.4" fill="transparent" stroke="var(--gruen)"
            transform="translate(2689.827 -2660) rotate(90 309.75 3000)" d="{WELLE_A}"></path>
    </svg>
    <svg viewBox="0 0 6000 680" xmlns="http://www.w3.org/2000/svg">
      <path opacity="0.1" fill="transparent" stroke="var(--gruen)"
            transform="translate(2695.687 -2660) rotate(90 304 3000)" d="{WELLE_B}"></path>
    </svg>
  </div>"""


def faq_block():
    teile = []
    for i, (frage, antworten) in enumerate(FAQ):
        offen = " open" if i == 0 else ""
        text = "\n                ".join(f'<p class="t-klein">{a}</p>' for a in antworten)
        teile.append(f"""            <details class="fq auftritt"{offen}>
              <summary class="fq__kopf">
                <h3 class="fq__frage">{frage}</h3>
                <span class="fq__zeichen" aria-hidden="true"><svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg"><path d="{PLUS}"/></svg></span>
              </summary>
              <div class="fq__huelle"><div class="fq__antwort">
                {text}
              </div></div>
            </details>""")
    fragen = "\n\n".join(teile)
    return f"""    <div class="kurve kurve--fluss" aria-hidden="true"><svg viewBox="0 0 2880 96" preserveAspectRatio="none"><path d="M0,64 C360,20 1080,90 1440,40 C1800,16 2520,88 2880,64 L2880,96 L0,96 Z" fill="#eef5f4"/></svg></div>
    <section class="faq" aria-labelledby="faq-titel">
      <div class="bahn faq__zeile">
        <div class="s5 faq__links">
          <div class="block faq__kopfteil">
            <h2 class="t-h2 auftritt" id="faq-titel">Häufig gestellte Fragen</h2>
            <p class="auftritt">Diese Antworten geben dir Orientierung.</p>
          </div>
          <div class="block faq__unten">
            <p class="t-klein faq__hinweis auftritt">Du hast deine Antwort nicht gefunden?<br>Sende mir gerne eine persönliche Nachricht.</p>
            {pille('Über mich', 'ueber-mich.html', 'gruen', 'auftritt')}
          </div>
        </div>
        <div class="s1"></div>
        <div class="s6">
          <div class="block faq__liste">

{fragen}

          </div>
        </div>
      </div>
    </section>"""


def fuss(aktiv):
    def link(text, ziel):
        hier = ' aria-current="page"' if ziel == aktiv else ''
        return (f'<a class="sitemap__link" href="{ziel}"{hier}>{text}'
                f'<span class="menue-link__linie"></span></a>')
    sozial = "\n            ".join(
        f'<a href="{u}" rel="noopener noreferrer" target="_blank" aria-label="{n}">'
        f'<svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="{d}"/></svg></a>'
        for u, n, d in SOZIAL)
    return f"""  <div class="kurve kurve--fluss kurve--spaet" aria-hidden="true"><svg viewBox="0 0 2880 96" preserveAspectRatio="none"><path d="M0,40 C360,90 1080,10 1440,56 C1800,90 2520,14 2880,40 L2880,96 L0,96 Z" fill="#68b8b0"/></svg></div>
  <footer class="fuss">
    <div class="bahn fuss__a">
      <div class="s6">
        <div class="block newsletter">
          <div class="newsletter__text">
            <h2 class="t-h1 newsletter__titel auftritt">Bleib in Verbindung.</h2>
            <p class="newsletter__zeile auftritt">Melde dich an und erhalte inspirierende Impulse für deine innere Entwicklung. Dich erwarten kraftvolle, kostenfreie Meditationen, sowie ausgewählte Einblicke und Informationen zu meinen aktuellen Angeboten.</p>
          </div>
          <form class="newsletter__form auftritt" name="newsletter" method="post" data-newsletter
                data-netlify="true" netlify-honeypot="firmenname">
            <input type="hidden" name="form-name" value="newsletter">
            <p class="honigtopf" aria-hidden="true">
              <label>Bitte leer lassen: <input name="firmenname" tabindex="-1" autocomplete="off"></label>
            </p>
            <label class="newsletter__feldhuelle" for="nl-email">
              <span class="nur-vorlesen">E-Mail-Adresse</span>
              <input class="newsletter__feld" id="nl-email" type="email" name="Email"
                     placeholder="Deine beste E-Mail" required autocomplete="email">
            </label>
            {pille('Eintragen', None, 'weiss', 'newsletter__knopf').replace('type="button"', 'type="submit"')}
          </form>
          <p class="t-klein newsletter__dank" data-newsletter-meldung role="status"></p>
        </div>
      </div>
      <div class="s2"></div>
      <div class="s4">
        <div class="block sitemap">
          <h2 class="t-label sitemap__titel auftritt">Sitemap</h2>
          <div class="sitemap__spalten">
            <nav class="sitemap__spalte auftritt" aria-label="Seiten">
              {link('Startseite', 'index.html')}
              {link('Über mich', 'ueber-mich.html')}
              {link('Angebote', 'angebote.html')}
              {link('Initiationen', 'initiationen.html')}
              {link('Die Schöpferwerke', 'schoepferwerke.html')}
              {link('Session buchen', 'session-buchen.html')}
            </nav>
            <nav class="sitemap__spalte auftritt" aria-label="Rechtliches">
              {link('Datenschutz', 'datenschutz.html')}
              {link('Impressum', 'impressum.html')}
              {link('AGB', 'agb.html')}
            </nav>
          </div>
        </div>
      </div>
    </div>

    <div class="bahn fuss__b">
      <div class="s6">
        <div class="block kontaktblock">
          <p class="kontaktblock__zeile auftritt">Kontaktiere mich: <a href="mailto:{MAIL}">{MAIL}</a></p>
          <div class="sozial auftritt">
            {sozial}
          </div>
        </div>
      </div>
      <div class="s2"></div>
      <div class="s4">
        <div class="block abspann">
          <div class="abspann__vorlage"></div>
          <p class="t-klein abspann__recht auftritt">Copyright 2026 Schöpferwerke. <span lang="en">All rights reserved.</span></p>
        </div>
      </div>
    </div>
  </footer>"""


def seite(datei, titel, beschreibung, inhalt, mit_faq=True, nach_faq=''):
    """Setzt eine vollständige HTML-Datei zusammen."""
    voll = f"{titel} — {MARKE}" if datei != "index.html" else "Schöpferwerke der Agnes Aichholzer — Selbstermächtigung und Seelenintegration"
    return f"""<!DOCTYPE html>
<html lang="de" data-js="nein">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{voll}</title>
<meta name="description" content="{beschreibung}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#68b8b0">
<link rel="canonical" href="{BASIS}/{'' if datei == 'index.html' else datei[:-5]}">

<meta property="og:type" content="website">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="{MARKE}">
<meta property="og:title" content="{voll}">
<meta property="og:description" content="{beschreibung}">
<meta property="og:url" content="{BASIS}/{'' if datei == 'index.html' else datei[:-5]}">
<meta property="og:image" content="{MEDIEN_BASIS}/assets/img/web/teilen-karte.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Schöpferwerke der Agnes Aichholzer, Bergsee in den Alpen">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/Bilder/Framer/symbol-apple-touch.png">
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/crimson-text-400-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/inter-400-latin.woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css?v={VERSION}">
<link rel="stylesheet" href="assets/site-v2.css?v={VERSION}">
<script>document.documentElement.dataset.js = "ja";</script>
</head>
<body>

<a class="sprungmarke" href="#inhalt">Zum Inhalt springen</a>

{kopf(datei, hell=(datei == "index.html"))}

<main class="seite" id="inhalt">

{wellen()}

  <div class="inhalt">

{inhalt}

{faq_block() if mit_faq else ''}

{nach_faq}

  </div>

{fuss(datei)}
</main>

<script src="assets/site.js?v={VERSION}"></script>
<script src="assets/site-v2.js?v={VERSION}"></script>
</body>
</html>
"""
