# -*- coding: utf-8 -*-
# quiz_pw/dane.py

from models import Pytanie, Odpowiedz

import os


def pobierz_dane(plikcsv):
    """Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv."""
    dane = []
    if os.path.isfile(plikcsv):
        with open(plikcsv, "r") as sCsv:
            for line in sCsv:
                line = line.replace("\n", "")  # usuwamy znaki końca linii
                line = line.decode("utf-8")  # format kodowania znaków
                dane.append(tuple(line.split("#")))
    else:
        print "Plik z danymi", plikcsv, "nie istnieje!"

    return tuple(dane)


def dodaj_pytania(dane):
    """Funkcja dodaje pytania i odpowiedzi przekazane w tupli do bazy."""
    for pytanie, odpowiedzi, odpok in dane:
        pyt = Pytanie(pytanie=pytanie, odpok=odpok)
        pyt.save()
        for o in odpowiedzi.split(","):
            odp = Odpowiedz(pnr=pyt.id, odpowiedz=o.strip())
            odp.save()

    print "Dodano przykładowe pytania"
