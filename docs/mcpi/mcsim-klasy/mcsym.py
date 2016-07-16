#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Symulacja(object):
    """
    Klasa pomocnicza. Pozwala odseparować kod.
    """

    mc = None  # obiekt reprezentujący serwer MC
    block = None  # obiekt reprezentujący dostępne bloki

    def __init__(self, mc, block):
        self.mc = mc
        self.block = block
        self.plac()

    def plac(self, x, y, z, roz=10, gracz=False):
        """Funkcja wypełnia sześcienny obszar od podanej pozycji
        powietrzem i opcjonalnie umieszcza gracza w środku.
        Parametry: x, y, z - współrzędne pozycji początkowej,
        roz - rozmiar wypełnianej przestrzeni,
        blok - rodzaj bloku
        gracz - czy umieścić gracza w środku
        Wymaga globalnego obiektu block.
        """

        kamien = self.block.STONE
        powietrze = self.block.AIR

        # kamienna podłoże
        self.mc.setBlocks(x, y - 1, z, x + roz, y - 1, z + roz, kamien)
        # czyszczenie
        self.mc.setBlocks(x, y, z, x + roz, y + roz, z + roz, powietrze)
        # umieść gracza w środku
        if gracz:
            self.mc.player.setPos(x + roz / 2, y + roz / 2, z + roz / 2)

    def buduj(self):
        """
        Metoda pomocnicza wywołująca konstruktor i kolejne polecenia
        budujące.
        """
        self.mc.setBlock(1, 1, 0, self.block.CACTUS)
