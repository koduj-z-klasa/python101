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

# utworzenie połaczenia z 1) minecraftem lub 2) symulatorem
# Ad 1) w cudzysłowie należy podać adres IP Raspberry Pi
# Ad 2) cudzysłów pusty
mc = minecraft.Minecraft.create("")

# wysłanie wiadomości na czat
mc.postToChat("Cześć! Tak działa MC chat!")


def plac(self, x, y, z, roz=10, gracz=False):
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


def buduj():
    """
    Funkcja do testowania umieszczania bloków.
    Wymaga: globalnych obiektów mc i block.
    """
    mc.setBlock(1, 0, 30, block.CACTUS)


def main(args):
    plac(0, 0, 0, 20)
    buduj()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
