#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from time import sleep
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

# utworzenie połączenia z minecraftem
mc = minecraft.Minecraft.create("192.168.1.10")  # podaj adres IP Rpi


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


def pomnik():
    """
    Funkcja ustawia blok lawy, nad nim blok wody, a później powietrza.
    """
    x, y, z = mc.player.getPos()

    lawa = 10
    woda = 8
    powietrze = 0

    mc.setBlock(x + 5, y + 3, z, lawa)
    sleep(10)
    mc.setBlock(x + 5, y + 5, z, woda)
    sleep(4)
    mc.setBlock(x + 5, y + 5, z, powietrze)


def main(args):
    mc.postToChat("Czesc! Tak dziala MC chat!")  # wysłanie komunikatu do mc
    plac(0, 0, 0, 18)
    pomnik()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
