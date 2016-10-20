#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np  # import biblioteki do obliczeń naukowych
import matplotlib.pyplot as plt  # import biblioteki do tworzenia wykresów
from random import randint
from time import sleep
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # wpisz dowolną nazwę użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # wpisz dowolną nazwę komputera

mc = minecraft.Minecraft.create("192.168.1.10")  # połaczenie z symulatorem


def plac(x, y, z, roz=10, gracz=False):
    """
    Funkcja tworzy podłoże i wypełnia sześcienny obszar od podanej pozycji,
    opcjonalnie umieszcza gracza w środku.
    Parametry: x, y, z - współrzędne pozycji początkowej,
    roz - rozmiar wypełnianej przestrzeni,
    gracz - czy umieścić gracza w środku
    Wymaga: globalnych obiektów mc i block.
    """

    podloga = block.WATER
    wypelniacz = block.AIR

    # podloga i czyszczenie
    mc.setBlocks(x, y - 1, z, x + roz, y - 1, z + roz, podloga)
    mc.setBlocks(x, y, z, x + roz, y + roz, z + roz, wypelniacz)
    # umieść gracza w środku
    if gracz:
        mc.player.setPos(x + roz / 2, y + roz / 2, z + roz / 2)


def wykres(x, y, tytul="Wykres funkcji", *extra):
    """
    Funkcja wizualizuje wykres funkcji, której argumenty zawiera lista x
    a wartości lista y i ew. dodatkowe listy w parametrze *extra
    """
    if len(extra):
        plt.plot(x, y, extra[0], extra[1])  # dwa wykresy na raz
    else:
        plt.plot(x, y, "o:", color="blue", linewidth="3", alpha=0.8)
    plt.title(tytul)
    plt.grid(True)
    plt.show()


def rysuj(x, y, z, blok=block.IRON_BLOCK):
    """
    Funkcja wizualizuje wykres funkcji, umieszczając bloki w pionie/poziomie
    w punktach wyznaczonych przez pary elementów list x, y lub x, z
    """
    czylista = True if len(y) > 1 else False
    for i in range(len(x)):
        if czylista:
            print(x[i], y[i])
            mc.setBlock(x[i], y[i], z[0], blok)
        else:
            print(x[i], z[i])
            mc.setBlock(x[i], y[0], z[i], blok)


def ruchyBrowna(dane=[]):

    if len(dane):
        lx, ly = dane  # rozpakowanie listy
        x = lx[-1]  # ostatni element lx
        y = ly[-1]  # ostatni element ly
    else:
        n = int(raw_input("Ile ruchów? "))
        r = int(raw_input("Krok przesunięcia? "))

        x = y = 0
        lx = [0]  # lista odciętych
        ly = [0]  # lista rzędnych

        for i in range(0, n):
            # losujemy kąt i zamieniamy na radiany
            rad = float(randint(0, 360)) * np.pi / 180
            x = x + r * np.cos(rad)  # wylicz współrzędną x
            y = y + r * np.sin(rad)  # wylicz współrzędną y
            x = int(round(x, 2))  # zaokrągl
            y = int(round(y, 2))  # zaokrągl
            print x, y
            lx.append(x)
            ly.append(y)

    # oblicz wektor końcowego przesunięcia
    s = np.fabs(np.sqrt(x**2 + y**2))
    print "Wektor przesunięcia: {:.2f}".format(s)

    wykres(lx, ly, "Ruchy Browna")
    rysuj(lx, [1], ly, block.WOOL)
    if not len(dane):
        zapisz_dane((lx, ly))


def zapisz_dane(dane):
    """Funkcja zapisuje dane w formacie json w pliku"""
    import json
    plik = open('rbrowna.log', 'w')
    json.dump(dane, plik)
    plik.close()


def czytaj_dane():
    """Funkcja odczytuje dane w formacie json z pliku"""
    import json
    dane = []
    nazwapliku = raw_input("Podaj nazwę pliku z danymi lub naciśnij ENTER: ")
    if os.path.isfile(nazwapliku):
        with open(nazwapliku, "r") as plik:
            dane = json.load(plik)
    else:
        print "Podany plik nie istnieje!"
    return dane


def main():
    mc.postToChat("Ruchy Browna")  # wysłanie komunikatu do mc
    plac(-80, -20, -80, 160)
    plac(-80, 0, -80, 160)
    ruchyBrowna(czytaj_dane())
    return 0


if __name__ == '__main__':
    main()
