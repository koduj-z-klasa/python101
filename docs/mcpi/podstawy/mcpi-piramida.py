#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

# utworzenie połaczenia z symulatorem
mc = minecraft.Minecraft.create("192.168.1.10")


def plac(x, y, z, roz=10, gracz=False):
    """Funkcja wypełnia sześcienny obszar od podanej pozycji
    powietrzem i opcjonalnie umieszcza gracza w środku.
    Parametry: x, y, z - współrzędne pozycji początkowej,
    roz - rozmiar wypełnianej przestrzeni,
    gracz - czy umieścić gracza w środku
    Wymaga: globalnych obiektów mc i block.
    """

    kamien = block.STONE
    powietrze = block.AIR

    # kamienna podłoże
    mc.setBlocks(x, y - 1, z, x + roz, y - 1, z + roz, kamien)
    # czyszczenie
    mc.setBlocks(x, y, z, x + roz, y + roz, z + roz, powietrze)
    # umieść gracza w środku
    if gracz:
        mc.player.setPos(x + roz / 2, y + roz / 2, z + roz / 2)


def kwadrat(bok, x, y, z):
    """
    Fukcja buduje kwadrat, którego środek to punkt x, y, z
    """
    pol = bok // 2
    piaskowiec = block.SANDSTONE
    mc.setBlocks(x - pol, y, z - pol, x + pol, y, z + pol, piaskowiec, 2)


def piramida(podstawa, x, y, z):
    """
    Buduje piramidę z piasku, której środek wypada w punkcie x, y, z
    """
    bok = podstawa
    wysokosc = y
    while bok >= 1:
        kwadrat(bok, x, wysokosc, z)
        bok -= 2
        wysokosc += 1


def main(args):
    mc.postToChat("Czesc! Tak dziala MC chat!")  # wysłanie komunikatu do mc
    plac(30, 0, 30, 30)
    piramida(28, 45, 0, 45)
    mc.player.setPos(45, 45, 45)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
