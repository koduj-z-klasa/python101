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

mc = minecraft.Minecraft.create("192.168.1.7")  # połączenie z serwerem


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


def model(r, x, y, z, klatka=False):
    """
    Fukcja buduje obrys kwadratu, którego środek to punkt x, y, z
    oraz koło wpisane w ten kwadrat
    """

    mcfig = mcstuff.MinecraftDrawing(mc)
    obrys = block.OBSIDIAN
    wypelniacz = block.AIR

    mc.setBlocks(x - r - 10, y - r, z - r - 10, x +
                 r + 10, y + r, z + r + 10, wypelniacz)
    mcfig.drawLine(x + r, y + r, z + r, x - r, y + r, z + r, obrys)
    mcfig.drawLine(x - r, y + r, z + r, x - r, y + r, z - r, obrys)
    mcfig.drawLine(x - r, y + r, z - r, x + r, y + r, z - r, obrys)
    mcfig.drawLine(x + r, y + r, z - r, x + r, y + r, z + r, obrys)

    mcfig.drawLine(x + r, y - r, z + r, x - r, y - r, z + r, obrys)
    mcfig.drawLine(x - r, y - r, z + r, x - r, y - r, z - r, obrys)
    mcfig.drawLine(x - r, y - r, z - r, x + r, y - r, z - r, obrys)
    mcfig.drawLine(x + r, y - r, z - r, x + r, y - r, z + r, obrys)

    mcfig.drawLine(x + r, y + r, z + r, x + r, y - r, z + r, obrys)
    mcfig.drawLine(x - r, y + r, z + r, x - r, y - r, z + r, obrys)
    mcfig.drawLine(x - r, y + r, z - r, x - r, y - r, z - r, obrys)
    mcfig.drawLine(x + r, y + r, z - r, x + r, y - r, z - r, obrys)

    mc.player.setPos(x + r, y + r + 1, z + r)

    if klatka:
        mc.setBlocks(x - r, y - r, z - r, x + r, y + r, z + r, block.GLASS)
        mc.setBlocks(x - r + 1, y - r + 1, z - r + 1, x +
                     r - 1, y + r - 1, z + r - 1, wypelniacz)
        mc.player.setPos(0, 0, 0)

    for i in range(-r, r + 1, 5):
        mcfig.drawHorizontalCircle(0, i, 0, r, block.GRASS)


def liczbaPi(klatka=False):
    r = int(raw_input("Podaj promień koła: "))
    model(r, 0, 0, 0, klatka)

    # pobieramy ilość punktów w kwadracie
    ileKw = int(raw_input("Podaj ilość losowanych punktów: "))
    ileKo = 0  # ilość punktów w kole
    wKwadrat = []  # pomocnicza lista punktów w kwadracie
    wKolo = []  # pomocnicza lista punktów w kole

    for i in range(ileKw):
        blok = block.OBSIDIAN
        x = round(random.uniform(-r, r))
        y = round(random.uniform(-r, r))
        z = round(random.uniform(-r, r))
        wKwadrat.append((x, y, z))
        print x, y, z
        if abs(x)**2 + abs(z)**2 <= r**2:
            blok = block.DIAMOND_BLOCK
            ileKo += 1
            wKolo.append((x, y, z))

        mc.setBlock(x, y, z, blok)

    mc.postToChat("W kole = " + str(ileKo) + " W Kwadracie = " + str(ileKw))
    pi = 4 * ileKo / float(ileKw)
    mc.postToChat("Pi w przyblizeniu: {:.10f}".format(pi))
    mc.postToChat("Stan na kamieniu!")

    while True:
        poz = mc.player.getPos()
        x, y, z = poz
        if mc.getBlock(x, y - 1, z) == block.STONE.id:
            for pkt in wKolo:
                x, y, z = pkt
                mc.setBlock(x, y, z, block.SAND)
            sleep(3)
            mc.player.setPos(0, r - 1, 0)
            break


def main():
    mc.postToChat("LiczbaPi")  # wysłanie komunikatu do mc
    plac(-50, 0, -50, 100)
    liczbaPi(False)
    return 0


if __name__ == '__main__':
    main()
