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
    from local.vec3 import Vec3
    pos = Vec3(-14, 0, 0)
    mc3d = mcturtle.MinecraftTurtle(mc, pos)
    # litera K
    mc3d.speed(10)
    mc3d.up(90)
    mc3d.penblock(block.SAND.id, 1)
    mc3d.forward(14)
    x, y, z = mc3d.position
    y -= 7
    mc3d.setposition(x, y, z)
    mc3d.down(40)
    # mc3d.right(90)
    mc3d.forward(9)
    mc3d.setposition(x, y, z)
    mc3d.down(80)
    mc3d.forward(9)
    mc3d.penblock(block.LEAVES.id, 1)
    # litera z
    x, y, z = (-5, 10, -5)
    mc3d.setposition(x, y, z)
    mc3d.up(35)
    mc3d.forward(9)
    mc3d.down(140)
    mc3d.forward(13)
    mc3d.up(135)
    mc3d.forward(9)
    # litera K
    x, y, z = (7, 0, 0)
    mc3d.setposition(x, y, z)
    mc3d.up(90)
    mc3d.penblock(block.OBSIDIAN.id, 1)
    mc3d.forward(13)
    x, y, z = mc3d.position
    y -= 7
    mc3d.setposition(x, y, z)
    mc3d.down(40)
    # mc3d.right(90)
    mc3d.forward(10)
    mc3d.setposition(x, y, z)
    mc3d.down(80)
    mc3d.forward(9)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
