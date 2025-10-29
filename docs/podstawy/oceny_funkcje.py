"""
    Moduł oceny_funkcje zawiera funkcje wykorzystywane w pliku oceny.py
"""

import math  # zaimportuj moduł matematyczny


def wypisz(sekwencja, kom='Sekwencja zawiera: '):
    print(kom)
    for e in sekwencja:
        print(e, end=' ')
    print()


def srednia(oceny):
    suma = sum(oceny)
    return suma / len(oceny)


def mediana(oceny):
    """
    Jeżeli liczba ocen jest parzysta, medianą jest średnia arytmetyczna
    dwóch środkowych ocen. Jeżeli liczba jest nieparzysta, mediana równa
    się elementowi środkowemu uporządkowanej rosnąco listy ocen.
    """
    oceny.sort()  # sortowanie niemalejące
    print(f'Oceny: {oceny}')
    if len(oceny) % 2 == 0:  # parzysta ilość ocen
        half = len(oceny) // 2
        # można tak:
        # return float(oceny[half-1]+oceny[half]) / 2
        # albo tak:
        return float(sum(oceny[half-1:half+1])) / 2
    else:  # nieparzysta ilość ocen
        return oceny[len(oceny) // 2]


def wariancja(oceny, srednia):
    """
    Wariancja to suma kwadratów różnicy każdej oceny i średniej
    podzielona przez ilość ocen:
    suma = ((o1-s)^2+(o2-s)^2+...+(on-s)^2) / n, gdzie:
    o1, o2, ..., on - kolejne oceny,
    s - średnia ocen,
    n - liczba ocen.
    """
    suma = 0
    for ocena in oceny:
        suma += (ocena - srednia)**2
    return suma / len(oceny)


def odchylenie(oceny, srednia):  # pierwiastek kwadratowy z wariancji
    w = wariancja(oceny, srednia)
    return math.sqrt(w)
