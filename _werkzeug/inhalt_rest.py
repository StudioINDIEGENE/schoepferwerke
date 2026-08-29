# -*- coding: utf-8 -*-
"""
Angebote, Initiationen, Session buchen, Schöpferwerke.

Wortlaut unverändert von der veröffentlichten Seite. Geändert wurde nur die
Gliederung: Dauer und Investition standen im Original am Ende des Fließtextes
angeklebt, hier stehen sie als Eckdaten. Zusammengelaufene Sätze sind getrennt.
"""

# =============================================================== Angebote

ANG_BESCHREIBUNG = ("Die Begleitungsformate von Agnes Aichholzer: einmalige 1:1 Session, "
                    "6 Wochen Lichtkörperstabilisierung, 13 Wochen transformative Reise.")

ANG_TITEL = "Der Weg in deine Schöpferkraft."
ANG_UNTERZEILE = ("Entdecke die Begleitungsformate abgestimmt auf dein Thema, dein Tempo und "
                  "deine Tiefe.")

ANG_EINSTIEG = [
 "Meine Arbeit richtet sich an ausgewählte Menschen. Jene, die entschieden haben – wahrhaftig den "
 "eigenen Weg zu gehen. Die, die zu mir kommen suchen nicht „Input“ sondern Heimkehr, in ihre "
 "eigene Macht und Kraft.",
 "In einem Raum frei von Bewertung und mit tiefem Respekt für individuelle Entwicklung, begleite "
 "ich meine Klienten in feinsten Schritten und mit höchster Präzision auf ihrem Weg in die "
 "Selbstverantwortung und innere Ganzheit.",
 "Alle Programme werden individuell auf dich abgestimmt.",
 "Wenn du nachhaltige Veränderung anstrebst, bereit bist nach innen zu schauen und deine Wahrheit "
 "zu leben, dann findest du hier tiefe Heilung und dauerhafte Transformation.",
]

ANG_BLOECKE = [
 dict(kennung="portal", bild="natur-wasser",
      titel="1:1 – Das Transformation Portal. Transformierend.",
      unterzeile="Eine einmalige, tiefgehende multidimensionale Sitzung.",
      absaetze=[
        "In diesem Raum erfolgt die gezielte Einstimmung deiner Seelenessenz in deinen physischen "
        "Körper und die kraftvolle Aktivierung deiner eigenen göttlichen Ordnungsenergie.",
        "Ich arbeite präzise im Feld, löse Blockaden auf ursächlicher Ebene und richte dein System "
        "neu aus – klar, geführt und in direkter Anbindung. Diese Session wirkt über den Moment "
        "hinaus und setzt eine nachhaltige innere Neuordnung in Bewegung.",
      ],
      eckdaten=[("Dauer", "2,5 Stunden"), ("Deine Investition", "450 Euro")],
      knopf=("Jetzt buchen (450 €)", "session-buchen.html")),

 dict(kennung="lichtkoerper", bild="natur-licht", badge="Beliebteste Wahl",
      titel="6 Wochen – Lichtkörperstabilisierung. Intensiv.",
      unterzeile="Eine strukturierte, intensive Begleitung über sechs Wochen.",
      absaetze=[
        "Der Fokus liegt auf der Stabilisierung deines Lichtkörpers und der kontinuierlichen "
        "Integration der geöffneten kosmischen Frequenzen in deinen Alltag.",
        "Schritt für Schritt wird dein System geklärt, ausgerichtet und gestärkt, sodass deine "
        "Seelenfrequenz tragfähig wird und sich in deinem Leben verankern kann. Diese Begleitung "
        "ist klar geführt und ermöglicht dir eine stabile, sichere Entwicklung.",
      ],
      eckdaten=[("Dauer", "6 Wochen"), ("Deine Investition", "2.500 Euro")],
      knopf=("Jetzt buchen (2.500 €)", "session-buchen.html")),

 dict(kennung="seelenmacht", bild="natur-gipfelsonne",
      titel="13 Wochen – Erwacht in deiner Seelenmacht. Revolutionär.",
      unterzeile="Eine tiefgreifende, transformative Reise über dreizehn Wochen.",
      absaetze=[
        "Diese Begleitung führt dich durch eine vollständige Neuausrichtung deines Systems – hin "
        "zur Verkörperung deines ursprünglichen Selbstes. Ich arbeite mit dir auf allen relevanten "
        "Ebenen: energetisch, emotional, zellulär und bewusstseinsbezogen.",
        "Alte Strukturen lösen sich, Seelenanteile werden integriert und deine innere Ordnung "
        "richtet sich neu aus. Deine Seelenkraft beginnt sich klar in deinem Leben zu verkörpern – "
        "authentisch und stabil im Alltag.",
        "Dieser Raum ist intensiv, präzise geführt und auf nachhaltige Transformation "
        "ausgerichtet. Dein inneres Fundament wird neu geordnet, sodass du dich klar in deine "
        "eigene Wahrheit und Schöpferkraft stellen kannst. Eine tiefgreifende Transformation in "
        "Übereinstimmung mit deiner Seelenmission.",
      ],
      eckdaten=[("Dauer", "13 Wochen"), ("Deine Investition", "5.500 Euro")],
      knopf=("Jetzt buchen (5.500 €)", "session-buchen.html")),

 dict(kennung="kennenlernen", bild=None,
      titel="Kennenlerngespräch – dein erster Schritt. Bewusst.",
      unterzeile="Ein klar gehaltener Raum für unsere erste Begegnung.",
      absaetze=[
        "In dieser Session nehme ich dich in deinem Feld wahr, ich lese was sich zeigt und was "
        "bereit ist, gesehen zu werden. Du bekommst ein erstes Gefühl für meine Arbeit und "
        "Klarheit über den nächsten Schritt.",
        "Gleichzeitig entsteht für uns beide die Sicherheit zu fühlen, ob wir weiter arbeiten "
        "möchten oder nicht. Diese Session ist bewusst geführt, klar strukturiert und bereits ein "
        "erster Schritt in deine Selbstermächtigung.",
      ],
      eckdaten=[("Dauer", "30 Minuten"), ("Kosten", "unverbindlich und kostenfrei")],
      knopf=("Kennenlerngespräch anfragen", "session-buchen.html")),
]

ANG_PREISE_LABEL = "Preise"
ANG_PREISE_TITEL = "Wähle dein Format."
ANG_PREISE_UNTERZEILE = ("Drei klare Wege in die Begleitung — von der einzelnen Tiefen-Session bis "
                         "zur länger geführten Transformation.")

ANG_HINWEIS_TITEL = "Hinweis zur Eigenverantwortung und Haftung"
ANG_HINWEIS = [
 "Meine Arbeit versteht sich als ganzheitliche, energetische und bewusstseinsorientierte "
 "Begleitung. Sie ersetzt keine medizinische, psychotherapeutische oder heilkundliche Behandlung. "
 "Ich gebe keine Heilversprechen und garantiere keine bestimmten Ergebnisse. Jeder Prozess ist "
 "individuell und entfaltet sich im eigenen Tempo und in eigener Verantwortung.",
 "Mit der Inanspruchnahme meiner Angebote erklärst du dich damit einverstanden, die volle "
 "Verantwortung für dich selbst, deine Entscheidungen, deine Erfahrungen sowie deine körperliche "
 "und psychische Gesundheit zu übernehmen. Meine Begleitung eröffnet Räume für Erkenntnis, "
 "Klärung und Transformation – die Umsetzung und Integration liegt in deiner eigenen "
 "Verantwortung.",
]

# ============================================================ Initiationen

INI_BESCHREIBUNG = ("Initiationen und Entfaltungsräume von Agnes Aichholzer. Begleitete Programme "
                    "zum Lichtkörperprozess, derzeit in Vorbereitung.")

INI_BILD = "natur-initiation"
INI_LABEL = "Vorschau kommender Räume"
INI_TITEL = "Initiationen und Entfaltungsräume"
INI_KOPFTEXT = [
 "Hier findest du Wege und Werkzeuge – sie alle dienen dem Lichtkörperprozess: damit du deinen "
 "physischen Körper vollständig bewohnst und aus deiner eigenen Quelle wirkst.",
 "Wenn dein Lichtkörper kohärent ist, wird dein physischer Körper tragfähig für höhere "
 "Frequenzen. Dein Wirken wird klar und deine Seelenmission lebbar.",
]
INI_SCHILD = "Programme in Vorbereitung"

INI_LK_LABEL = "Lichtkörperprozess"
INI_LK_TITEL = "Das ist kein Luxus – es ist die Grundarchitektur deiner individuellen Freiheit."
INI_LK_TEXT = [
 "Diese Initiationen und Programme sind kein „Kurs“, kein weiteres Format im Markt der "
 "Möglichkeiten. Es sind strukturierte Wege der Rückkehr in deine ursprüngliche Wahrheit.",
 "Alle Initiationen und Übungen führen dich zurück in deine Essenz, deine Kohärenz, deine Kraft – "
 "in dein Licht und in die Liebe.",
 "Denn dieses Licht, das aus der eigenen Quelle schöpft, authentisch in sich selbst sowie im "
 "kosmisch-irdischen verankert ist und dem Göttlichen innig zugewandt bleibt, wird jetzt auf "
 "dieser Welt so dringend gebraucht.",
]

INI_KARTEN_TITEL = "Erlesene Programme für Rückkehr, Kohärenz und Verkörperung."
INI_KARTEN_INTRO = ("Es sind erlesene, frequenzerhöhende Initiationen, die ich im Format von "
                    "begleiteten Programmen mit Selbststudium anbiete — Abkürzungen zum "
                    "Wesentlichen, in klaren Schritten und mit persönlicher Begleitung.")

INI_KARTEN = [
 ("Initiation 01", "Lichtkörper-Kohärenz",
  "Ein Raum für innere Ordnung, körperliche Verankerung und das bewusste Bewohnen deiner eigenen "
  "Frequenz.", "In Vorbereitung"),
 ("Initiation 02", "Quelle und Seelenmission",
  "Ein geführter Weg zurück in deine ursprüngliche Wahrheit — damit dein Wirken klarer und deine "
  "Seelenmission lebbarer wird.", "Kommt bald"),
 ("Initiation 03", "Verankerung der Seelengröße",
  "Für Menschen, die bereit sind, selbstermächtigt in innere Stabilität, Verkörperung und "
  "schöpferische Präsenz zu gehen.", "In Vorbereitung"),
]

INI_SCHLUSS = [
 "Fühle dich eingeladen, diesen Raum für dich zu nutzen – als Segen für dich und für das, was "
 "durch dich in die Welt geboren werden möchte.",
 "All die lichtvollen Menschen, die jetzt inkarniert sind, um in diesem großen kosmischen "
 "Entwicklungsprozess mitzuwirken, sind aufgerufen, ihre Seelennatur zu leben – dem Ausdruck zu "
 "verleihen, was ihnen innewohnt.",
 "Ich begleite diese Räume persönlich. Sie erfordern deinen Einsatz und den klaren Willen, "
 "selbstermächtigt in deine Seelengröße, innere Verankerung und Stabilität zu gehen.",
]

# ========================================================== Schöpferwerke

SCH_BESCHREIBUNG = ("Schöpferwerke ist eine Forschungsakademie für die Heilung und Entfaltung der "
                    "menschlichen Schöpferkraft, gegründet von Agnes Aichholzer.")

SCH_BILD = "natur-sterne"
SCH_TITEL = "Was sind die Schöpferwerke?"

SCH_ZITAT = ("„Selbstermächtigung ist kein Konzept, sondern gelebte Schöpferkraft – und du bist "
             "deines eigenen Glückes Schmied.“")
SCH_ZITAT_QUELLE = "— Agnes Aichholzer"

SCH_TEXT = [
 ("auftakt",
  "Schöpferwerke ist eine Forschungsakademie. Ihr Hauptaugenmerk ist die Heilung und Entfaltung "
  "der globalen menschlichen Schöpferkraft."),
 "Gegründet von Agnes Aichholzer – Mentorin für Selbstermächtigung und Seelenintegration – öffnen "
 "sie einen Raum für Menschen, die bereit sind, ihr eigenes Schöpferwerk aus einer tiefen inneren "
 "Stimmigkeit in diese Welt zu bringen.",
 "Sie sind für Menschen, die bereit sind, tiefer zu gehen, die nicht länger im Außen suchen, "
 "sondern beginnen, sich selbst im Kern zu begegnen.",
 "Die Schöpferwerke öffnen ein Feld, in dem sich die innere Ordnung des Menschen wiederherstellt "
 "und sich dadurch das eigene Lebenswerk aus der Tiefe des Seins entwickeln kann.",
 "Hier findest du individuelle Wege und Werkzeuge, denn es geht um das unmittelbare Erfahren, "
 "Erinnern und Verkörpern dessen, was im Menschen ursprünglich angelegt ist.",
 ("kern", "Im Zentrum steht die Verbindung zur eigenen Quelle."),
 "Jede Begegnung, jede Session, jedes Programm ist ein Schritt in diese Rückverbindung. Ein "
 "tieferes Verstehen der eigenen Struktur – ein Ermächtigen der eigenen Wahrheit. Ein Erkennen "
 "der eigenen Schöpferkraft und ein Leben der eigenen Seelennatur.",
 "Diese Akademie öffnet den Raum der Erinnerung, der bewussten Forschung, Heilung und "
 "Transformation. Nicht im Außen – sondern im tiefsten Kern deines inneren Wesens, dort wo "
 "Schöpfer und Schöpfung eins sind.",
]

SCH_KNOPF = ("Kennenlerngespräch buchen", "session-buchen.html")

# ========================================================= Session buchen

SB_BESCHREIBUNG = ("Session bei Agnes Aichholzer anfragen: Kennenlerngespräch, einmalige 1:1 "
                   "Session oder mehrwöchige Begleitung.")
