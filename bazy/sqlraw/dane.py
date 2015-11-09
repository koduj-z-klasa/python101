#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os


def pobierz_dane(plikcsv):
    """
    Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv
    do zapisania w tabeli.
    """
    dane = []  # deklarujemy pustą tabelę
    if os.path.isfile(plikcsv):  # sprawdzamy czy plik istnieje na dysku
        with open(plikcsv, "r") as zawartosc:  # otwieramy plik do odczytu
            for linia in zawartosc:
                linia = linia.replace("\n", "")  # usuwamy znaki końca linii
                linia = linia.replace("\r", "")  # usuwamy znaki końca linii
                linia = linia.decode("utf-8")  # odczytujemy znaki jako utf-8
                # dodajemy elementy do tupli a tuplę do tabeli
                dane.append(tuple(linia.split(",")))
    else:
        print "Plik z danymi", plikcsv, "nie istnieje!"

    return tuple(dane)  # przekształcamy tabelę na tuplę i zwracamy ją
