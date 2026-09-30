# -*- coding: utf-8 -*-
"""
Die drei Rechtsseiten: AGB, Datenschutz, Impressum.

Der Wortlaut stammt unverändert von der veröffentlichten Seite.
Geändert wurde ausschließlich die Gliederung: Aufzählungen, die im Original
als Fließtext mit Mittelpunkten zusammengelaufen sind, stehen hier als
echte Listen, und jeder Punkt hat seinen eigenen Abschnitt.
"""

MAIL = "schoepferwerke@gmail.com"

# ---------------------------------------------------------------------- AGB

AGB_DATUM = 'Stand: <time datetime="2026-09-01">01.09.2026</time>'

AGB_INTRO = ("Diese Allgemeinen Geschäftsbedingungen gelten für alle Angebote, "
             "Dienstleistungen und Programme von Agnes Aichholzer.")

AGB = [
 ("Geltungsbereich", [
  ("p", "Diese Allgemeinen Geschäftsbedingungen gelten für alle Angebote, Dienstleistungen und "
        "Programme von Agnes Aichholzer, insbesondere für 1:1 Begleitungen, Einzelsessions, "
        "Intensivräume, Gruppenprogramme sowie digitale Inhalte. Mit der Buchung eines Angebots "
        "erklärst du dich mit diesen AGB einverstanden."),
 ]),
 ("Art der Leistungen", [
  ("p", "Die angebotenen Leistungen sind ganzheitliche, energetische und bewusstseinsorientierte "
        "Begleitungen. Sie dienen der persönlichen Entwicklung, inneren Klärung und Aktivierung "
        "eigener Ressourcen. Die Angebote stellen keine medizinische, psychotherapeutische oder "
        "heilkundliche Behandlung dar und ersetzen keine solche."),
 ]),
 ("Vertragsschluss", [
  ("p", "Ein Vertrag kommt zustande, sobald eine Buchung über die Website, per E-Mail oder über "
        "ein Buchungssystem erfolgt und bestätigt wird."),
 ]),
 ("Preise und Zahlungsbedingungen", [
  ("p", "Alle Preise werden vor der Buchung klar kommuniziert und verstehen sich [inkl./zzgl.] "
        "gesetzlicher Umsatzsteuer. Die Zahlung erfolgt grundsätzlich im Voraus."),
  ("lead", "Ratenzahlungen:", "Sofern eine Ratenzahlung vereinbart wurde, verpflichtet sich die "
        "Kundin zur vollständigen Begleichung des Gesamtbetrages. Offene Raten bleiben auch dann "
        "zahlungspflichtig, wenn die Begleitung vorzeitig abgebrochen wird. Bei Zahlungsverzug "
        "behalten wir uns vor, Leistungen auszusetzen."),
 ]),
 ("Programme und längere Begleitungen", [
  ("p", "Bei mehrmonatigen Begleitungen oder Programmen handelt es sich um verbindliche "
        "Gesamtprozesse. Ein vorzeitiger Abbruch durch die Kundin entbindet nicht von der "
        "Zahlungspflicht. Rückerstattungen sind ausgeschlossen, es sei denn, es liegt ein "
        "gesetzlicher Anspruch vor."),
 ]),
 ("Termine und Ausfallregelung", [
  ("p", "Vereinbarte Termine sind verbindlich."),
  ("ul", ["Absagen oder Verschiebungen sind bis 24 Stunden vor dem Termin kostenfrei möglich.",
          "Bei kurzfristiger Absage oder Nichterscheinen wird der Termin vollständig berechnet."]),
  ("p", "Bei wiederholtem Nichterscheinen kann die Zusammenarbeit beendet werden."),
 ]),
 ("Mitwirkung und Eigenverantwortung", [
  ("p", "Die Teilnahme an allen Angeboten setzt eigenverantwortliches Handeln voraus. Die Kundin "
        "erklärt sich bereit, aktiv am Prozess mitzuwirken und Verantwortung für ihre "
        "Entscheidungen, Erfahrungen und Handlungen zu übernehmen."),
  ("merk", "Wir geben keine Heilversprechen!"),
 ]),
 ("Hinweis zu Gesundheit und psychischer Stabilität", [
  ("p", "Die Teilnahme setzt eine stabile psychische und physische Verfassung voraus. Bei "
        "bestehenden gesundheitlichen oder psychischen Herausforderungen wird empfohlen, parallel "
        "mit qualifizierten Fachpersonen (z.&nbsp;B. Arzt, Therapeut) zu arbeiten."),
 ]),
 ("Haftungsausschluss", [
  ("p", "Die angebotenen Leistungen ersetzen keine medizinische oder therapeutische Behandlung. Es "
        "werden keine Diagnosen gestellt und keine Heilversprechen gegeben. Die Inanspruchnahme der "
        "Angebote erfolgt eigenverantwortlich. Eine Haftung für direkte oder indirekte Schäden wird "
        "ausgeschlossen, soweit gesetzlich zulässig."),
 ]),
 ("Abbruch durch die Anbieterin", [
  ("p", "Agnes Aichholzer behält sich das Recht vor, eine Zusammenarbeit zu beenden, wenn:"),
  ("ul", ["notwendige Mitwirkung ausbleibt,",
          "vereinbarte Rahmenbedingungen wiederholt nicht eingehalten werden,",
          "eine weitere Begleitung aus fachlicher oder energetischer Sicht nicht sinnvoll erscheint."]),
  ("p", "In diesem Fall besteht kein Anspruch auf Rückerstattung bereits geleisteter Zahlungen."),
 ]),
 ("Vertraulichkeit", [
  ("p", "Alle Inhalte der Zusammenarbeit werden vertraulich behandelt. Persönliche Informationen "
        "werden nicht an Dritte weitergegeben, es sei denn, es besteht eine gesetzliche "
        "Verpflichtung."),
 ]),
 ("Urheberrecht", [
  ("p", "Alle Inhalte, Programme, Texte und Materialien sind urheberrechtlich geschützt. Eine "
        "Weitergabe, Vervielfältigung oder Nutzung ist ohne ausdrückliche Zustimmung nicht "
        "gestattet."),
 ]),
 ("Änderungen von Angeboten", [
  ("p", "Die Anbieterin behält sich vor, Inhalte, Abläufe oder Termine anzupassen, sofern dies den "
        "Gesamtcharakter des Angebots nicht wesentlich verändert."),
 ]),
 ("Schlussbestimmungen", [
  ("p", "Es gilt das Recht des Landes, in dem der Sitz von Agnes Aichholzer ist. Gerichtsstand ist "
        "– soweit gesetzlich zulässig – der Sitz der Anbieterin. Sollten einzelne Bestimmungen "
        "unwirksam sein, bleibt die Wirksamkeit der übrigen Bestimmungen unberührt."),
 ]),
]

AGB_KURZ = ["Geltungsbereich", "Art der Leistungen", "Vertragsschluss",
            "Preise und Zahlungsbedingungen", "Programme und längere Begleitungen",
            "Termine und Ausfallregelung", "Mitwirkung und Eigenverantwortung",
            "Gesundheit und psychische Stabilität", "Haftungsausschluss",
            "Abbruch durch die Anbieterin", "Vertraulichkeit", "Urheberrecht",
            "Änderungen von Angeboten", "Schlussbestimmungen"]

# -------------------------------------------------------------- Datenschutz

DS_DATUM = 'Stand: <time datetime="2026-07-21">21. Juli 2026</time>'

DS_INTRO = ("Der achtsame Umgang mit Ihren Daten ist für uns selbstverständlich. Diese Erklärung "
            "zeigt, welche Daten erhoben werden, wozu sie dienen und welche Rechte Sie haben.")

DATENSCHUTZ = [
 ("Verantwortliche Stelle", [
  ("p", "Verantwortlich für die Datenverarbeitung auf dieser Website ist:"),
  ("adr", ["Agnes Aichholzer", "Am Moosfeld 6", "39049 Wiesen",
           f'<a href="mailto:{MAIL}">{MAIL}</a>']),
 ]),
 ("Grundlegendes zum Umgang mit Daten", [
  ("p", "Der achtsame Umgang mit Ihren Daten ist für uns selbstverständlich. Wir behandeln Ihre "
        "personenbezogenen Informationen mit Sorgfalt, Klarheit und in Übereinstimmung mit den "
        "geltenden Datenschutzbestimmungen (DSGVO)."),
  ("p", "Personenbezogene Daten sind alle Informationen, die es ermöglichen, Sie als Person zu "
        "identifizieren."),
 ]),
 ("Erhebung personenbezogener Daten", [
  ("p", "Ihre Daten werden erhoben, wenn Sie uns diese freiwillig zur Verfügung stellen – etwa im "
        "Rahmen von:"),
  ("ul", ["Kontaktanfragen", "Buchungen oder Terminvereinbarungen", "E-Mail-Kommunikation"]),
  ("p", "Dabei kann es sich insbesondere um folgende Daten handeln:"),
  ("ul", ["Name", "E-Mail-Adresse", "Telefonnummer (falls angegeben)", "Inhalte Ihrer Nachricht"]),
  ("p", "Beim Besuch dieser Website werden zusätzlich automatisch technische Informationen "
        "erfasst:"),
  ("ul", ["Browsertyp und Version", "verwendetes Betriebssystem", "Referrer URL",
          "Zeitpunkt der Anfrage", "IP-Adresse (ggf. anonymisiert)"]),
 ]),
 ("Zweck der Verarbeitung", [
  ("p", "Die Verarbeitung Ihrer Daten dient dazu, einen klaren und verlässlichen Raum für "
        "Kommunikation und Zusammenarbeit zu ermöglichen. Konkret verwenden wir Ihre Daten für:"),
  ("ul", ["die Beantwortung Ihrer Anfragen",
          "die Durchführung von Buchungen und Begleitungen",
          "die Kommunikation im Rahmen unserer Zusammenarbeit",
          "die technische Bereitstellung und Weiterentwicklung dieser Website"]),
 ]),
 ("Rechtsgrundlagen (Art. 6 DSGVO)", [
  ("p", "Die Verarbeitung Ihrer Daten erfolgt auf Basis folgender rechtlicher Grundlagen:"),
  ("ul", ["Ihrer Einwilligung (Art. 6 Abs. 1 lit. a DSGVO)",
          "der Erfüllung eines Vertrags oder vorvertraglicher Maßnahmen (Art. 6 Abs. 1 lit. b DSGVO)",
          "unseres berechtigten Interesses an einer stabilen, sicheren und funktionierenden "
          "Website (Art. 6 Abs. 1 lit. f DSGVO)"]),
 ]),
 ("Sensible Inhalte und Vertraulichkeit", [
  ("p", "Über diese Website werden keine sensiblen personenbezogenen Daten aktiv abgefragt. "
        "Sollten Sie im Rahmen unserer Kommunikation persönliche oder tiefgehende Informationen "
        "mit uns teilen, geschieht dies freiwillig."),
  ("p", "Diese Inhalte werden von uns mit höchster Vertraulichkeit behandelt und ausschließlich im "
        "Kontext Ihrer Anfrage oder Begleitung verwendet."),
 ]),
 ("Weitergabe von Daten", [
  ("p", "Ihre Daten werden nicht verkauft, vermietet oder für werbliche Zwecke weitergegeben. Eine "
        "Weitergabe erfolgt nur, wenn dies zur Erbringung unserer Leistungen erforderlich ist oder "
        "gesetzlich vorgeschrieben wird. Dies betrifft insbesondere:"),
  ("ul", ["Hosting-Anbieter", "E-Mail-Dienstleister", "Zahlungsanbieter (z.&nbsp;B. Stripe, PayPal)",
          "Buchungssysteme", "Kommunikationsplattformen (z.&nbsp;B. Zoom)"]),
  ("p", "Alle eingesetzten Dienstleister verarbeiten Daten ausschließlich im Rahmen der "
        "gesetzlichen Vorgaben."),
 ]),
 ("Speicherdauer", [
  ("p", "Ihre Daten werden nur so lange gespeichert, wie es für den jeweiligen Zweck erforderlich "
        "ist oder gesetzliche Aufbewahrungsfristen bestehen."),
  ("ul", ["Kontaktanfragen: in der Regel bis zu 12 Monate",
          "Buchungs- und Vertragsdaten: entsprechend gesetzlicher Vorgaben"]),
 ]),
 ("Cookies", [
  ("p", "Diese Website verwendet Cookies, um die Nutzung für Sie möglichst klar und funktional zu "
        "gestalten. Cookies sind kleine Textdateien, die auf Ihrem Endgerät gespeichert werden."),
  ("p", "Sie können die Speicherung jederzeit über Ihre Browsereinstellungen steuern oder "
        "deaktivieren. Sofern ein Cookie-Banner eingesetzt wird, erfolgt die Nutzung nicht "
        "technisch notwendiger Cookies ausschließlich auf Grundlage Ihrer Einwilligung."),
 ]),
 ("Schriften, Bilder und externe Dienste", [
  ("p", "Diese Website lädt keine Inhalte von fremden Servern. Schriften, Bilder, Stilblätter "
        "und Skripte liegen ausschließlich auf dem Server dieser Website."),
  ("ul", [
    "Es werden keine Google Fonts oder vergleichbare Schriftdienste eingebunden.",
    "Es wird kein Auslieferungsnetz (CDN) verwendet.",
    "Es sind keine Karten, Videos oder Anmeldefenster Dritter eingebettet.",
    "Es findet keine Reichweitenmessung und kein Nutzerverhalten-Tracking statt.",
  ]),
  ("p", "Beim Aufruf der Seite wird deshalb keine Verbindung zu Dritten hergestellt und Ihre "
        "IP-Adresse an niemanden außerhalb dieser Website übermittelt."),
  ("lead", "Verweise auf soziale Netzwerke:", "Die Symbole in der Fußzeile sind einfache Links. "
           "Es werden keine Inhalte dieser Netzwerke geladen, eine Datenübertragung findet erst "
           "statt, wenn Sie einen Link anklicken und die fremde Seite öffnen."),
 ]),
 ("Datensicherheit", [
  ("p", "Zum Schutz Ihrer Daten setzen wir geeignete technische und organisatorische Maßnahmen "
        "ein. Die Übertragung Ihrer Daten erfolgt verschlüsselt (SSL-/TLS-Verbindung), sodass "
        "Inhalte nicht von Dritten mitgelesen werden können."),
  ("p", "Trotz aller Sorgfalt weisen wir darauf hin, dass keine digitale Übertragung vollständig "
        "frei von Risiken ist."),
 ]),
 ("Ihre Rechte", [
  ("p", "Sie haben jederzeit das Recht:"),
  ("ul", ["Auskunft über Ihre gespeicherten Daten zu erhalten",
          "unrichtige Daten berichtigen zu lassen",
          "die Löschung Ihrer Daten zu verlangen",
          "die Verarbeitung einzuschränken",
          "Ihre Daten in einem übertragbaren Format zu erhalten",
          "eine erteilte Einwilligung zu widerrufen"]),
  ("p", "Zur Ausübung Ihrer Rechte genügt eine formlose Mitteilung per E-Mail."),
 ]),
 ("Beschwerderecht", [
  ("p", "Wenn Sie der Ansicht sind, dass die Verarbeitung Ihrer Daten nicht im Einklang mit den "
        "Datenschutzbestimmungen erfolgt, steht Ihnen das Recht zu, sich bei einer zuständigen "
        "Aufsichtsbehörde zu beschweren."),
 ]),
 ("Änderungen dieser Erklärung", [
  ("p", "Diese Datenschutzerklärung wird bei Bedarf angepasst, um aktuellen rechtlichen "
        "Anforderungen zu entsprechen oder Veränderungen unserer Leistungen abzubilden."),
 ]),
 ("Kontakt", [
  ("p", "Bei Fragen zum Datenschutz erreichen Sie uns unter:"),
  ("adr", [f'<a href="mailto:{MAIL}">{MAIL}</a>']),
 ]),
]

DS_KURZ = ["Verantwortliche Stelle", "Umgang mit Daten", "Erhebung der Daten",
           "Zweck der Verarbeitung", "Rechtsgrundlagen", "Sensible Inhalte",
           "Weitergabe von Daten", "Speicherdauer", "Cookies", "Externe Dienste", "Datensicherheit",
           "Ihre Rechte", "Beschwerderecht", "Änderungen", "Kontakt"]

# ---------------------------------------------------------------- Impressum

IMP_DATUM = 'Angaben gemäß italienischem Recht (D.Lgs. 70/2003)'

IMP_INTRO = None

IMPRESSUM = [
 ("Diensteanbieter und Verantwortliche", [
  ("adr", ["Agnes Aichholzer", "Einzelunternehmerin",
           "Schöpferwerke – Mentoring für Selbstermächtigung &amp; Seelenintegration"]),
  ("adr", ["Am Moosfeld 6", "39049 Wiesen / Pfitsch", "Südtirol, Italien"]),
 ]),
 ("Kontakt", [
  ("adr", [f'E-Mail: <a href="mailto:{MAIL}">{MAIL}</a>',
           'Website: <a href="https://www.schoepferwerke.com">www.schoepferwerke.com</a>']),
 ]),
 ("Steuerliche Angaben", [
  ("lead", "Partita IVA:", "IT03354160214"),
  ("p", "Tätigkeit im Rahmen des Regime Forfettario gemäß Art. 1, commi 54–89, "
        "Legge n. 190/2014."),
  ("p", "Es wird keine Mehrwertsteuer ausgewiesen (IVA nicht anwendbar)."),
 ]),
 ("Verantwortlich für den Inhalt", [
  ("adr", ["Agnes Aichholzer", "(Anschrift wie oben)"]),
 ]),
 ("Haftung für Inhalte", [
  ("p", "Die Inhalte dieser Website wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, "
        "Vollständigkeit und Aktualität der Inhalte übernehmen wir jedoch keine Gewähr."),
 ]),
 ("Haftung für Links", [
  ("p", "Diese Website enthält Links zu externen Websites Dritter, auf deren Inhalte kein Einfluss "
        "besteht. Daher wird für diese fremden Inhalte keine Gewähr übernommen."),
 ]),
 ("Urheberrecht", [
  ("p", "Die durch die Seitenbetreiberin erstellten Inhalte und Werke auf dieser Website "
        "unterliegen dem Urheberrecht. Jede Art der Verwertung außerhalb der Grenzen des "
        "Urheberrechts bedarf der vorherigen schriftlichen Zustimmung."),
 ]),
 ("Bildnachweis", [
  ("p", "Folgende Landschaftsaufnahmen stammen von Unsplash und stehen unter der "
        "Unsplash-Lizenz, die eine kommerzielle Nutzung ausdrücklich erlaubt. Die Nennung der "
        "Urheber ist nicht verpflichtend, erfolgt hier aber aus Respekt vor ihrer Arbeit."),
  ("ul", [
    "Seebensee (Startseite): Daniel Jacob",
    "Drei Zinnen unter der Milchstraße (Die Schöpferwerke): Jan Valečka",
  ]),
  ("p", "Lizenztext: <a href=\"https://unsplash.com/de/lizenz\" rel=\"noopener noreferrer\" "
        "target=\"_blank\">unsplash.com/de/lizenz</a>"),
  ("p", "Weitere Landschafts- und Naturaufnahmen stammen von Pixabay und stehen unter der "
        "Pixabay-Inhaltslizenz, die eine kommerzielle Nutzung ohne Namensnennung erlaubt."),
  ("p", "Lizenztext: <a href=\"https://pixabay.com/de/service/license-summary/\" "
        "rel=\"noopener noreferrer\" target=\"_blank\">pixabay.com/de/service/license-summary</a>"),
  ("lead", "Private Aufnahmen:", "Die Porträts von Agnes Aichholzer und die Aufnahmen aus ihrem "
                                 "eigenen Bestand dürfen nicht ohne schriftliche Zustimmung "
                                 "verwendet werden."),
  ("lead", "Wortmarke und Symbol:", "Die Zeichen der Schöpferwerke sind geschützte "
                                    "Kennzeichen der Anbieterin."),
 ]),
 ("Hinweis zu den angebotenen Leistungen", [
  ("p", "Die angebotenen Leistungen dienen der persönlichen Weiterentwicklung, energetischen "
        "Balance sowie der Aktivierung der Selbstwahrnehmung und inneren Ressourcen."),
  ("p", "Sie stellen keine medizinische, psychologische oder therapeutische Leistung dar und "
        "ersetzen keine Diagnose oder Behandlung durch entsprechend qualifizierte Fachpersonen."),
  ("merk", "Es werden keine Heilversprechen abgegeben."),
  ("p", "Die Teilnahme an allen Angeboten erfolgt freiwillig und eigenverantwortlich."),
 ]),
 ("Haftungsausschluss", [
  ("p", "Die Inanspruchnahme der angebotenen Leistungen erfolgt auf eigene Verantwortung."),
  ("p", "Für Entscheidungen, Handlungen oder Ergebnisse, die aus der Nutzung der Inhalte oder "
        "Begleitungen entstehen, wird keine Haftung übernommen."),
 ]),
]

IMP_KURZ = ["Diensteanbieter", "Kontakt", "Steuerliche Angaben", "Verantwortlich für den Inhalt",
            "Haftung für Inhalte", "Haftung für Links", "Urheberrecht", "Bildnachweis",
            "Hinweis zu den Leistungen", "Haftungsausschluss"]
