#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Moduł ocenyfun zawiera funkcje wykorzystywane w pliku 05_oceny_03.py
"""

import math  # zaimportuj moduł matematyczny


def drukuj(co, kom="Sekwencja zawiera: "):
    print(kom)
    for i in co:
        print(i, end=" ")


def srednia(oceny):
    suma = sum(oceny)
    return suma / float(len(oceny))


def mediana(oceny):
    """
    Jeżeli ilość ocen jest parzysta, medianą jest średnia arytmetyczna
    dwóch środkowych ocen. Jesli ilość  jest nieparzysta mediana równa
    się elementowi środkowemu ouporządkowanej rosnąco listy ocen.
    """
    oceny.sort()
    if len(oceny) % 2 == 0:  # parzysta ilość ocen
        half = int(len(oceny) / 2)
        # można tak:
        # return float(oceny[half-1]+oceny[half]) / 2.0
        # albo tak:
        return float(sum(oceny[half - 1:half + 1])) / 2.0
    else:  # nieparzysta ilość ocen
        return oceny[len(oceny) / 2]


def wariancja(oceny, srednia):
    """
    Wariancja to suma kwadratów różnicy każdej oceny i średniej
    podzielona przez ilość ocen:
    sigma = (o1-s)+(o2-s)+...+(on-s) / n, gdzie:
    o1, o2, ..., on - kolejne oceny,
    s - średnia ocen,
    n - liczba ocen.
    """
    sigma = 0.0
    for ocena in oceny:
        sigma += (ocena - srednia)**2
    return sigma / len(oceny)


def odchylenie(oceny, srednia):  # pierwiastek kwadratowy z wariancji
    w = wariancja(oceny, srednia)
    return math.sqrt(w)
