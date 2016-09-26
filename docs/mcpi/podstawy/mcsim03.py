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


def buduj():
    """
    Funkcja do testowania umieszczania bloków.
    Wymaga: globalnych obiektów mc i block.
    """
    for i in range(19):
        mc.setBlock(0 + i, 0, 0, block.WOOD)
        mc.setBlock(0 + i, 1, 0, block.LEAVES)
        mc.setBlock(0 + i, 0, 18, block.WOOD)
        mc.setBlock(0 + i, 1, 18, block.LEAVES)

    for i in range(19):
        mc.setBlock(9, 0, 18 - i, block.BRICK_BLOCK)
        mc.setBlock(9, 1, 18 - i, block.BRICK_BLOCK)


def main(args):
    mc.postToChat("Cześć! Tak działa MC chat!")  # wysłanie komunikatu do mc
    plac(0, 0, 0, 18)
    buduj()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
