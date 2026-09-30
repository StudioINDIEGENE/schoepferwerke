# -*- coding: utf-8 -*-
"""
Erzeugt alle HTML-Seiten von Schöpferwerke.

Aufruf aus dem Projektordner:

    python3 _werkzeug/bauen.py

Heraus kommen ganz gewöhnliche, einzeln bearbeitbare HTML-Dateien.
Zum Ausliefern der Seite wird dieses Skript nicht gebraucht, es dient nur
dazu, Kopfbereich, Navigation und Fußzeile an einer Stelle zu pflegen.
"""

import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.dirname(HIER)
sys.path.insert(0, HIER)

import vorlage
import bausteine
import inhalt_recht as recht
import inhalt_ueber_mich as um
import inhalt_start as st
import inhalt_rest as re_


def schreibe(datei, text):
    pfad = os.path.join(WURZEL, datei)
    alt = None
    if os.path.exists(pfad):
        with open(pfad, encoding="utf-8") as f:
            alt = f.read()
    if alt == text:
        print(f"  unverändert  {datei}")
        return
    with open(pfad, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  geschrieben  {datei}  ({len(text)//1024} KB)")


def baue_rechtsseiten():
    seiten = [
        ("agb.html", "AGB", "Allgemeine Geschäftsbedingungen",
         "Allgemeine Geschäftsbedingungen für alle Angebote, Dienstleistungen und Programme von "
         "Agnes Aichholzer.",
         recht.AGB_DATUM, recht.AGB_INTRO, recht.AGB, recht.AGB_KURZ),

        ("datenschutz.html", "Datenschutz", "Datenschutzerklärung",
         "Welche Daten auf dieser Website erhoben werden, wozu sie dienen und welche Rechte Sie "
         "haben.",
         recht.DS_DATUM, recht.DS_INTRO, recht.DATENSCHUTZ, recht.DS_KURZ),

        ("impressum.html", "Impressum", "Impressum",
         "Anbieterkennzeichnung von Agnes Aichholzer, Schöpferwerke, Wiesen in Südtirol.",
         recht.IMP_DATUM, recht.IMP_INTRO, recht.IMPRESSUM, recht.IMP_KURZ),
    ]

    for datei, kurztitel, h1, beschreibung, datum, intro, abschnitte, kurz in seiten:
        inhalt = bausteine.rechtstext(h1, datum, intro, abschnitte, kurz)
        schreibe(datei, vorlage.seite(datei, kurztitel, beschreibung, inhalt))


def baue_ueber_mich():
    inhalt = bausteine.inhaltsseite(
        bausteine.kopfbereich(um.TITEL, um.UNTERZEILE, bild=um.KOPF_BILD),
        bausteine.leitsatz("Über mich", um.EINSTIEG),
        # Die Bildreihe bricht die längste Textstrecke der Seite auf.
        bausteine.bildreihe(um.BILDREIHE),
        bausteine.leitsatz(None, um.WER_ICH_BIN, titel="Wer ich bin",
                           titel_klasse="t-h1"),
        bausteine.bild_zitat(um.BILD, um.BILD_ALT, um.ZITAT, um.ZITAT_QUELLE),
        bausteine.grosser_satz(um.GROSSER_SATZ),
        bausteine.ornament(),
        bausteine.kompetenzen("Ausbildung und Kompetenzen", um.KOENNEN_EINLEITUNG,
                              um.KOENNEN, gruppen=um.KOENNEN_GRUPPEN),
        bausteine.aufruf(um.AUFRUF_TITEL, um.AUFRUF_TEXT, *um.AUFRUF_KNOPF),
    )
    schreibe("ueber-mich.html",
             vorlage.seite("ueber-mich.html", "Über mich", um.BESCHREIBUNG, inhalt))


BUCHUNG = dict(
    label="Lebe dein Potenzial",
    titel="Veränderung beginnt mit der bewussten Entscheidung für dich loszugehen.",
    unterzeile="Nimm Kontakt auf und informiere dich über meine Programme.",
    einleitung="Ich begleite jene, die entschieden sind.",
    absaetze=[
        "Menschen, die ihr Leben selbst in die Hand nehmen und bereit sind, Verantwortung für ihr "
        "inneres Erleben zu übernehmen und eine echte, nachhaltige Veränderung anstreben.",
        "Dieser Weg ist eine Meisterklasse, ein klar geführter Raum für tiefe Heilung und "
        "dauerhafte Transformation. Durch Selbstverantwortung und präzise, professionelle Führung "
        "entwickelst du deine eigene Selbstermächtigung.",
        "Es entsteht kein kurzfristiger Effekt, sondern ein neues inneres Fundament, ein "
        "Lebensgefühl, das dich stabil hält, dir klare Ausrichtung schenkt und in dem du dir "
        "selbst zur Heimat wirst.",
    ],
    wege_titel="Deine Möglichkeiten der Begleitung",
    wege=[
        "Kostenloses Kennenlerngespräch",
        "Einmalige 1:1 Session, das Transformationsportal",
        "6 Wochen intensive Begleitung, die Lichtkörperstabilisierung",
        "13 Wochen transformative Reise, erwache in deiner Seelenmacht",
        "Initiationen mit Selbststudium",
    ],
    mail=vorlage.MAIL,
    bild=("natur-weg-matterhorn", "Ein Wanderweg führt über grüne Hänge auf das Matterhorn zu"),
    gruss=("agnes-gruss", "Agnes Aichholzer mit Hut an einem Bergsee"),
)


def baue_startseite():
    inhalt = bausteine.inhaltsseite(
        bausteine.hero(st.HERO_BILD, st.HERO_TITEL, st.HERO_UNTERZEILE, *st.HERO_KNOPF),
        bausteine.leitsatz(None,
                           st.QUELLE_TEXT + st.QUELLE_DREI + st.QUELLE_SCHLUSS
                           + [st.QUELLE_ABSCHLUSS],
                           titel=st.QUELLE_TITEL, gross=False),
        bausteine.karten(st.ANGEBOTE_LABEL, st.ANGEBOTE_TITEL, st.ANGEBOTE_UNTERZEILE,
                         st.ANGEBOTE_KARTEN, st.ANGEBOTE_KNOEPFE),
        bausteine.schritte(st.ABLAUF_TITEL, st.ABLAUF_UNTERZEILE, st.ABLAUF),
        # Der Beleg steht jetzt vor dem Preis: Bild, Zahlen und Stimmen
        # zuerst, dann erst die Beträge. Von Sindri und Bragi unabhängig
        # gefordert, kein Wort ändert sich dabei.
        bausteine.breitbild(st.BREITBILD, st.BREITBILD_ALT, st.BREITBILD_TITEL,
                            st.BREITBILD_TEXT, zitat=st.ZITAT, quelle=st.ZITAT_QUELLE),
        bausteine.zahlen(st.ZAHLEN_TITEL, st.ZAHLEN_UNTERZEILE, st.ZAHLEN),
        bausteine.stimmen(st.STIMMEN_LABEL, st.STIMMEN_TITEL, st.STIMMEN),
        bausteine.ornament(),
        bausteine.aufruf(st.AUFRUF_TITEL, st.AUFRUF_TEXT, *st.AUFRUF_KNOPF),
        bausteine.preise(st.PREISE_LABEL, st.PREISE_TITEL, st.PREISE_UNTERZEILE, st.PREISE),
    )
    nach_faq = bausteine.buchung(**BUCHUNG)
    schreibe("index.html",
             vorlage.seite("index.html", "Startseite", st.BESCHREIBUNG, inhalt,
                           nach_faq=nach_faq))


def baue_angebote():
    bloecke = [bausteine.angebot(b["bild"], b["titel"], b["unterzeile"], b["absaetze"],
                                 b["eckdaten"], b["knopf"][0], b["knopf"][1], b["kennung"],
                                 badge=b.get("badge"))
               for b in re_.ANG_BLOECKE]
    inhalt = bausteine.inhaltsseite(
        bausteine.kopfbereich(re_.ANG_TITEL, re_.ANG_UNTERZEILE, bild=re_.ANG_BILD),
        bausteine.programm_nav([("1:1 Session", "#portal"), ("6 Wochen", "#lichtkoerper"),
                                ("13 Wochen", "#seelenmacht"),
                                ("Kennenlerngespräch", "#kennenlernen")]),
        bausteine.leitsatz("Angebote", re_.ANG_EINSTIEG),
        *bloecke,
        bausteine.zahlen(st.ZAHLEN_TITEL, st.ZAHLEN_UNTERZEILE, st.ZAHLEN),
        bausteine.stimmen(st.STIMMEN_LABEL, st.STIMMEN_TITEL, st.STIMMEN),
        bausteine.preise(re_.ANG_PREISE_LABEL, re_.ANG_PREISE_TITEL,
                         re_.ANG_PREISE_UNTERZEILE, st.PREISE, zentriert=True),
        # Der Haftungshinweis stand direkt hinter den Beträgen. Jetzt
        # hinter dem Beleg, wo er niemanden mehr abschreckt.
        bausteine.hinweisblock(re_.ANG_HINWEIS_TITEL, re_.ANG_HINWEIS),
        bausteine.kauf_leiste(),
    )
    schreibe("angebote.html",
             vorlage.seite("angebote.html", "Angebote", re_.ANG_BESCHREIBUNG, inhalt,
                           nach_faq=bausteine.buchung(**BUCHUNG)))


def baue_initiationen():
    inhalt = bausteine.inhaltsseite(
        bausteine.bildkopf(re_.INI_BILD, re_.INI_LABEL, re_.INI_TITEL,
                           re_.INI_KOPFTEXT, re_.INI_SCHILD, mitte=True),
        bausteine.initiationen(re_.INI_LK_LABEL, re_.INI_LK_TITEL, re_.INI_LK_TEXT,
                               re_.INI_KARTEN_TITEL, re_.INI_KARTEN_INTRO,
                               re_.INI_KARTEN, re_.INI_SCHLUSS,
                               nebentitel="Wege der Rückkehr",
                               bilder=re_.INI_KARTEN_BILDER),
    )
    schreibe("initiationen.html",
             vorlage.seite("initiationen.html", "Initiationen", re_.INI_BESCHREIBUNG, inhalt))


def baue_schoepferwerke():
    inhalt = bausteine.akademie(re_.SCH_BILD, re_.SCH_TITEL, re_.SCH_ZITAT,
                                re_.SCH_ZITAT_QUELLE, re_.SCH_TEXT, *re_.SCH_KNOPF)
    schreibe("schoepferwerke.html",
             vorlage.seite("schoepferwerke.html", "Die Schöpferwerke", re_.SCH_BESCHREIBUNG,
                           inhalt))


def baue_session_buchen():
    schreibe("session-buchen.html",
             vorlage.seite("session-buchen.html", "Session buchen", re_.SB_BESCHREIBUNG,
                           '    <div class="kopfabstand kopfabstand--klein"></div>\n\n'
                           + bausteine.buchung(**BUCHUNG, stufe=1)))


if __name__ == "__main__":
    print("Rechtsseiten:")
    baue_rechtsseiten()
    print("Inhaltsseiten:")
    baue_ueber_mich()
    baue_startseite()
    baue_angebote()
    baue_initiationen()
    baue_schoepferwerke()
    baue_session_buchen()
    print("fertig.")
