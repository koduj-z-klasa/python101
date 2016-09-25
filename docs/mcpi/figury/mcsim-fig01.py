#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import local.minecraft as minecraft  # import modułu minecraft
import local.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

# utworzenie połaczenia z symulatorem
mc = minecraft.Minecraft.create("")


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


def main(args):
    mc.postToChat("Czesc! Tak dziala MC chat!")  # wysłanie komunikatu do mc
    plac(-15, 0, -15, 30)

    from time import sleep
    import local.minecraftstuff as mcstuff
    from local.vec3 import Vec3  # klasa reprezentująca punkt 3D

    figura = mcstuff.MinecraftDrawing(mc)  # obiekt do rysowania kształtów

    # LINIE
    # tuple z współrzędnymi punktów
    punkty1 = ((-10, 0, -10), (10, 0, -10), (10, 0, 10), (-10, 0, 10))
    punkty2 = ((-15, 5, 0), (15, 5, 0), (0, 5, 15), (0, 5, -15))
    p1 = Vec3(0, 0, 0)  # punkt początkowy
    for punkt in punkty1:
        x, y, z = punkt
        p2 = Vec3(x, y, z)  # punkt końcowy
        figura.drawLine(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z, block.WOOL, 14)
    for punkt in punkty2:
        x, y, z = punkt
        p2 = Vec3(x, y, z)  # punkt końcowy
        figura.drawLine(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z, block.OBSIDIAN)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
