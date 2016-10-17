#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import local.minecraft as minecraft  # import modułu minecraft
import local.block as block  # import modułu block
import local.minecraftstuff as mcstuff  # import biblioteki do rysowania figur
from local.vec3 import Vec3  # klasa reprezentująca punkt w MC

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

mc = minecraft.Minecraft.create("")  # połaczenie z symulatorem
figura = mcstuff.MinecraftDrawing(mc)  # obiekt do rysowania kształtów


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


def linie():
    # Funkcja rysuje linie
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


def kolo(x, y, z, r):
    # Funkcja rysuje koło pionowe i poziome o środku x, y, z i promieniu r
    figura.drawCircle(x, y, z, r, block.LEAVES, 2)
    figura.drawHorizontalCircle(x, y, z, r, block.LEAVES, 2)


def kula(x, y, z, r):
    # Funkcja rysuje kulę o środku x, y, z i promieniu r
    figura.drawSphere(x, y, z, r, block.WOOD, 2)


def ksztalt():
    # Funkcja łączy podane w liście wierzchołki i opcjonalnie wypełnia figurę
    ksztalt = []  # lista punktów
    ksztalt.append(Vec3(-11, 0, 11))  # współrzędne 1 wierzchołka
    ksztalt.append(Vec3(11, 0, 11))  # współrzędne 2 wierzchołka
    ksztalt.append(Vec3(0, 0, -11))  # współrzędne 3 wierzchołka
    figura.drawFace(ksztalt, True, block.SANDSTONE, 2)


def main():
    mc.postToChat("Biblioteka minecraftstuff")  # wysłanie komunikatu do mc
    plac(-15, 0, -15, 30)
    linie()
    kolo(0, 10, 0, 10)
    kula(0, 10, 0, 9)
    ksztalt()
    return 0


if __name__ == '__main__':
    main()
