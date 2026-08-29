# -*- coding: utf-8 -*-
"""
Schnürt aus dem Arbeitsordner das Veröffentlichungspaket.

Es wandert nur hinein, was die neun Seiten tatsächlich anfordern: die
Seiten selbst, die Stilblätter samt der von ihnen nachgeladenen Dateien,
das Skript, die Schriften und die benutzten Bilder. Das Werkzeug, die
alte Fassung und die unbenutzten Bildbestände bleiben draußen.

Aufruf: python3 _werkzeug/paket.py
Netlify ruft es als Bauschritt und veröffentlicht `_veroeffentlichung`.
"""

import os
import pathlib
import re
import shutil
import sys

WURZEL = pathlib.Path(__file__).resolve().parent.parent
ZIEL = WURZEL / "_veroeffentlichung"

# Verweise, die nicht auf eine Datei im Ordner zeigen können.
FREMD = ("http://", "https://", "mailto:", "data:", "tel:", "//")


def ist_fremd(pfad):
    return not pfad or pfad.startswith(FREMD)


def sammle(text, basis, treffer):
    """Trägt alle lokalen Verweise eines Textes in `treffer` ein."""

    def rein(pfad):
        pfad = pfad.split("?")[0].split("#")[0].strip()
        if ist_fremd(pfad):
            return
        treffer.add(os.path.normpath(os.path.join(basis, pfad)))

    for m in re.finditer(r'(?:href|src)="([^"]+)"', text):
        rein(m.group(1))
    for m in re.finditer(r'srcset="([^"]+)"', text):
        for teil in m.group(1).split(","):
            rein(teil.strip().split(" ")[0])
    for m in re.finditer(r'url\((["\']?)([^"\')]+)\1\)', text):
        rein(m.group(2))


def schnueren():
    if ZIEL.exists():
        shutil.rmtree(ZIEL)
    ZIEL.mkdir()

    treffer = set()
    seiten = sorted(WURZEL.glob("*.html"))
    if not seiten:
        sys.exit("Keine Seiten gefunden. Erst _werkzeug/bauen.py laufen lassen.")

    for seite in seiten:
        treffer.add(seite.name)
        sammle(seite.read_text(encoding="utf-8"), ".", treffer)

    # Zwei Durchgänge: ein Stilblatt kann ein weiteres nachladen.
    for _ in range(2):
        for rel in list(treffer):
            datei = WURZEL / rel
            if datei.suffix == ".css" and datei.is_file():
                basis = str(datei.parent.relative_to(WURZEL))
                sammle(datei.read_text(encoding="utf-8"), basis, treffer)

    dateien = sorted({pathlib.Path(t) for t in treffer if (WURZEL / t).is_file()})
    for rel in dateien:
        ziel = ZIEL / rel
        ziel.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(WURZEL / rel, ziel)

    vorlage = WURZEL / "_werkzeug" / "netlify.toml"
    if vorlage.is_file():
        shutil.copy2(vorlage, ZIEL / "netlify.toml")

    pruefen(dateien)


def pruefen(dateien):
    """Kein Verweis darf ins Leere zeigen."""
    fehler = []
    for seite in sorted(ZIEL.glob("*.html")):
        text = seite.read_text(encoding="utf-8")
        ziele = set(re.findall(r'(?:href|src)="([^"]+)"', text))
        for m in re.finditer(r'srcset="([^"]+)"', text):
            for teil in m.group(1).split(","):
                ziele.add(teil.strip().split(" ")[0])
        for z in ziele:
            z = z.split("?")[0].split("#")[0]
            if ist_fremd(z):
                continue
            if not (ZIEL / z).is_file():
                fehler.append(f"{seite.name} → {z}")

    groesse = sum(f.stat().st_size for f in ZIEL.rglob("*") if f.is_file())
    print(f"{len(dateien)} Dateien, {groesse / 1024 / 1024:.1f} MB "
          f"in {ZIEL.name}/")
    if fehler:
        for f in fehler:
            print(f"  fehlt: {f}")
        sys.exit(f"{len(fehler)} Verweise zeigen ins Leere.")
    print("Alle Verweise lösen auf.")


if __name__ == "__main__":
    schnueren()
