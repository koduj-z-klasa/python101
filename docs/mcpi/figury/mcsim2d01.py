#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "Uruchamianie... Proszę czekać..."

# import modułów minecrafta
import local.minecraft as minecraft
import local.block as block

# ustawienie nazwy użytkownika i komputera
import os
os.environ["USERNAME"] = "Steve"  # wpisz dowolną nazwę użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # wpisz dowolną nazwę komputera

# utworzenie połaczenia z symulatorem
mc = minecraft.Minecraft.create("")


def plac(x, y, z, roz=10, gracz=False):
    """Funkcja wypełnia sześcienny obszar od podanej pozycji
    powietrzem i opcjonalnie umieszcza gracza w środku.
    Parametry: x, y, z - współrzędne pozycji początkowej,
    roz - rozmiar wypełnianej przestrzeni,
    blok - rodzaj bloku
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

    import local.minecraftstuff as mcstuff
    mcfig = mcstuff.MinecraftDrawing(mc)
    mcfig.drawLine(-14, 0, -14, -14, 0, 14, block.LEAVES)
    mcfig.drawLine(-14, 0, 0, -7, 0, 14, block.LEAVES)
    mcfig.drawLine(-14, 0, 0, -7, 0, -14, block.LEAVES)
    mcfig.drawLine(-5, 0, 0, 5, 0, 0, block.LEAVES)
    mcfig.drawLine(5, 0, 0, -5, 0, 14, block.LEAVES)
    mcfig.drawLine(-5, 0, 14, 5, 0, 14, block.LEAVES)
    mcfig.drawLine(7, 0, -14, 7, 0, 14, block.LEAVES)
    mcfig.drawLine(7, 0, 0, 14, 0, 14, block.LEAVES)
    mcfig.drawLine(7, 0, 0, 14, 0, -14, block.LEAVES)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
