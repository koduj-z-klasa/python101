# -*- coding: utf-8 -*-
# quiz-orm/dane.py

import os
import csv
from models import Pytanie, Odpowiedz


def pobierz_dane(plikcsv):
    """Funkcja zwraca tuplę zawierającą tuple z danymi z pliku csv."""
    dane = []
    if os.path.isfile(plikcsv):
        with open(plikcsv, newline='') as plikcsv:
            tresc = csv.reader(plikcsv, delimiter='#')
            for rekord in tresc:
                dane.append(tuple(rekord))
    else:
        print("Plik z danymi", plikcsv, "nie istnieje!")

    return tuple(dane)


def dodaj_pytania(dane):
    """Funkcja dodaje pytania i odpowiedzi przekazane w tupli do bazy."""
    for pytanie, odpowiedzi, odpok in dane:
        p = Pytanie(pytanie=pytanie, odpok=odpok)
        p.save()
        for o in odpowiedzi.split(","):
            odp = Odpowiedz(pnr=p.id, odpowiedz=o.strip())
            odp.save()
    print("Dodano przykładowe pytania")
