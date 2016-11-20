#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np  # import biblioteki do obliczeń naukowych
import matplotlib.pyplot as plt  # import biblioteki do tworzenia wykresów
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # wpisz dowolną nazwę użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # wpisz dowolną nazwę komputera

mc = minecraft.Minecraft.create("192.168.1.10")  # połaczenie z mc


def plac(x, y, z, roz=10, gracz=False):
    """
    Funkcja tworzy podłoże i wypełnia sześcienny obszar od podanej pozycji,
    opcjonalnie umieszcza gracza w środku.
    Parametry: x, y, z - współrzędne pozycji początkowej,
    roz - rozmiar wypełnianej przestrzeni,
    gracz - czy umieścić gracza w środku
    Wymaga: globalnych obiektów mc i block.
    """

    podloga = block.STONE
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
        plt.plot(x, y)
    plt.title(tytul)
    # plt.xlabel(podpis)
    plt.grid(True)
    plt.show()


def uklad(blok=block.OBSIDIAN):
    """
    Funkcja rysuje układ współrzędnych
    """
    for i in range(-80, 81, 2):
        mc.setBlock(i, -1, 0, blok)
        mc.setBlock(0, -1, i, blok)
        mc.setBlock(0, i, 0, blok)


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


def rysuj_linie(x, y, z, blok=block.IRON_BLOCK):
    """
    Funkcja wizualizuje wykres funkcji, umieszczając bloki w pionie/poziomie
    w punktach wyznaczonych przez pary elementów list x, y lub x, z
    przy użyciu metody drawLine()
    """
    import local.minecraftstuff as mcstuff
    mcfig = mcstuff.MinecraftDrawing(mc)
    czylista = True if len(y) > 1 else False
    for i in range(len(x) - 1):
        x1 = int(x[i])
        x2 = int(x[i + 1])
        if czylista:
            y1 = int(y[i])
            y2 = int(y[i + 1])
            print (x1, y1, z[0], x2, y2, z[0])
            mcfig.drawLine(x1, y1, z[0], x2, y2, z[0], blok)
        else:
            z1 = int(z[i])
            z2 = int(z[i + 1])
            print (x1, y[0], z1, x2, y[0], z2)
            mcfig.drawLine(x1, y[0], z1, x2, y[0], z2, blok)


def fun1(blok=block.IRON_BLOCK):
    """
    Funkcja f(x) = a*x + b
    """
    a = int(raw_input('Podaj współczynnik a: '))
    b = int(raw_input('Podaj współczynnik b: '))
    x = range(-10, 11)  # lista argumentów x = <-10;10> z krokiem 1
    y = [a * i + b for i in x]  # wyrażenie listowe
    print x, "\n", y
    wykres(x, y, "f(x) = a*x + b")
    rysuj_linie(x, y, [1], blok)


def fun2(blok=block.REDSTONE_ORE):
    """
    Wykres funkcji f(x), gdzie x = <-1;2> z krokiem 0.15, przy czym
    f(x) = x/(x+2) dla x >= 1
    f(x) = x*x/3 dla x < 1 i x > 0
    f(x) = x/(-3) dla x <= 0
    """
    x = np.arange(-1, 2.15, 0.15)  # lista argumentów x
    y = []  # lista wartości f(x)

    for i in x:
        if i <= 0:
            y.append(i / -3)
        elif i < 1:
            y.append(i ** 2 / 3)
        else:
            y.append(i / (i + 2))
    wykres(x, y, "Funkcja mieszana")
    x = [round(i * 20, 2) for i in x]
    y = [round(i * 20, 2) for i in y]
    print x, "\n", y
    rysuj(x, y, [1], blok)


def fun3(blok=block.LAPIS_LAZULI_BLOCK):
    """
    Funkcja f(x) = log2(x)
    """
    x = np.arange(0.1, 41, 1)  # lista argumentów x
    y = [np.log2(i) for i in x]
    y = [round(i, 2) * 2 for i in y]
    print x, "\n", y
    wykres(x, y, "Funkcja logarytmiczna")
    rysuj(x, y, [1], blok)


def main():
    mc.postToChat("Funkcje w Minecrafcie")  # wysłanie komunikatu do mc
    plac(-80, -20, -80, 160)
    mc.player.setPos(-8, 10, 26)
    uklad(block.DIAMOND_BLOCK)
    fun1()
    fun2()
    fun3()
    return 0


if __name__ == '__main__':
    main()
