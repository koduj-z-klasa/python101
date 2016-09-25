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

    import local.minecraftturtle as mcturtle
    from local.vec3 import Vec3  # klasa reprezentująca punkt 3D

    start = Vec3(0, 1, 0)  # pozycja początkowa
    turtle = mcturtle.MinecraftTurtle(mc, start)

    # KWADRATY
    turtle.speed(0)  # szybkość budowania
    turtle.penblock(block.SAND)  # typ bloku
    for i in range(4):
        turtle.forward(10)  # do przodu 10 "króków"
        turtle.right(90)  # w prawo o 90 stopni
    turtle.left(90)  # w lewo o 90 stopni
    for i in range(4):
        turtle.forward(10)
        turtle.left(90)

    # OKNA
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

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
