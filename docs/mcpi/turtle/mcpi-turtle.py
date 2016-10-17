#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block
import local.minecraftturtle as mcturtle
from local.vec3 import Vec3  # klasa reprezentująca punkt w MC

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

mc = minecraft.Minecraft.create("192.168.1.10")  # połaczenie z symulatorem
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


def okna():
    # Funkcja rysuje kształt okien w pionie
    turtle.penblock(block.WOOD)
    turtle.setposition(10, 2, 0)
    turtle.up(90)
    turtle.forward(14)
    turtle.down(90)
    turtle.setposition(-10, 2, 0)
    turtle.up(90)
    turtle.forward(14)
    turtle.down(90)
    turtle.right(90)
    turtle.forward(19)
    turtle.setposition(0, 2, 0)
    turtle.up(90)
    turtle.forward(13)
    turtle.setposition(9, 10, 0)
    turtle.down(90)
    turtle.left(180)
    turtle.forward(19)


def szlaczek():
    # Funkcja rysuje przerywaną linię
    turtle.penblock(block.MELON)
    turtle.setx(-15)
    turtle.sety(2)
    turtle.setz(15)
    turtle.left(180)
    for i in range(8):
        if (i % 2 == 0):
            turtle.forward(1)
        else:
            turtle.forward(3)
        turtle.penup()
        turtle.forward(2)
        turtle.pendown()


def slonce():
    turtle.setposition(-20, 3, 0)
    turtle.speed(0)
    turtle.penblock(block.GOLD_BLOCK)
    while True:
        turtle.forward(80)
        turtle.left(165)
        x, y, z = turtle.position
        print max(x, z)
        if abs(max(x, z)) < 1:
            break


def wielokat(n):
    turtle.setposition(15, 3, -18)
    turtle.speed(0)
    turtle.penblock(block.OBSIDIAN)
    for i in range(n):
        turtle.forward(10)
        turtle.right(360 / n)


def main():
    mc.postToChat("Biblioteka minecraftturtle")  # wysłanie komunikatu do mc
    # plac(-15, 0, -15, 30)
    # kwadraty()
    # okna()
    # szlaczek()
    plac(-80, 0, -80, 160)
    slonce()
    wielokat(10)
    return 0


if __name__ == '__main__':
    main()
