#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
from time import sleep
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block
import local.minecraftstuff as mcstuff

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

mc = minecraft.Minecraft.create("192.168.1.10")  # połączenie z serwerem


def plac(x, y, z, roz=10, gracz=False):
    """Funkcja wypełnia sześcienny obszar od podanej pozycji
    powietrzem i opcjonalnie umieszcza gracza w środku.
    Parametry: x, y, z - współrzędne pozycji początkowej,
    roz - rozmiar wypełnianej przestrzeni,
    gracz - czy umieścić gracza w środku
    Wymaga: globalnych obiektów mc i block.
    """

    podloga = block.STONE
    wypelniacz = block.AIR

    # kamienna podłoże
    mc.setBlocks(x, y - 1, z, x + roz, y - 1, z + roz, podloga)
    # czyszczenie
    mc.setBlocks(x, y, z, x + roz, y + roz, z + roz, wypelniacz)
    # umieść gracza w środku
    if gracz:
        mc.player.setPos(x + roz / 2, y + roz / 2, z + roz / 2)


def model(promien, x, y, z):
    """
    Fukcja buduje obrys kwadratu, którego środek to punkt x, y, z
    oraz koło wpisane w ten kwadrat
    """

    mcfig = mcstuff.MinecraftDrawing(mc)
    obrys = block.SANDSTONE
    wypelniacz = block.AIR

    mc.setBlocks(x - promien, y, z - promien, x +
                 promien, y, z + promien, obrys)
    mc.setBlocks(x - promien + 1, y, z - promien + 1, x +
                 promien - 1, y, z + promien - 1, wypelniacz)
    mcfig.drawHorizontalCircle(0, 0, 0, promien, block.GRASS)


def liczbaPi():
    r = float(raw_input("Podaj promień koła: "))
    model(r, 0, 0, 0)


def main():
    mc.postToChat("LiczbaPi")  # wysłanie komunikatu do mc
    plac(-50, 0, -50, 100)
    mc.player.setPos(20, 20, 0)
    liczbaPi()
    return 0


if __name__ == '__main__':
    main()
