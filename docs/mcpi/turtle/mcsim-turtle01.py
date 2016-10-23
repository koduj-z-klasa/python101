#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import local.minecraft as minecraft  # import modułu minecraft
import local.block as block  # import modułu block
import local.minecraftturtle as mcturtle
from local.vec3 import Vec3  # klasa reprezentująca punkt w MC

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

mc = minecraft.Minecraft.create("")  # połaczenie z symulatorem
start = Vec3(0, 1, 0)  # pozycja początkowa
turtle = mcturtle.MinecraftTurtle(mc, start)  # obiekt "żółwia"


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


def kwadraty():
    # Funkcja rysuje dwa kwadraty w poziomie
    turtle.speed(0)  # szybkość budowania
    turtle.penblock(block.SAND)  # typ bloku
    for i in range(4):
        turtle.forward(10)  # do przodu 10 "króków"
        turtle.right(90)  # w prawo o 90 stopni
    turtle.left(90)  # w lewo o 90 stopni
    for i in range(4):
        turtle.forward(10)
        turtle.left(90)


def main():
    mc.postToChat("Biblioteka minecraftturtle")  # wysłanie komunikatu do mc
    plac(-15, 0, -15, 30)
    kwadraty()

    return 0


if __name__ == '__main__':
    main()
