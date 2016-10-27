#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys
import os
from random import randint
from time import sleep
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

mc = minecraft.Minecraft.create("192.168.1.10")  # połączenie z symulatorem


class GraWZycie(object):
    """
    Główna klasa gry, łączy wszystkie elementy.
    """

    def __init__(self, mc, szer, wys, ile=40):
        """
        Przygotowanie ustawień gry
        :param szer: szerokość planszy mierzona liczbą komórek
        :param wys: wysokość planszy mierzona liczbą komórek
        """
        self.mc = mc
        mc.postToChat('Gra o zycie')
        self.szer = szer
        self.wys = wys
        self.populacja = Populacja(mc, szer, wys)  # instancja klasy Populacja
        if ile:
            self.populacja.losuj(ile)

    def uruchom(self):
        """
        Główna pętla gry
        """
        self.plac(0, 0, 0, self.szer, self.wys)  # narysuj pole gry

    def plac(self, x, y, z, szer=20, wys=10):
        """
        Funkcja tworzy plac gry
        """
        podloga = block.STONE
        wypelniacz = block.AIR
        granica = block.OBSIDIAN

        # granica, podłoże, czyszczenie
        self.mc.setBlocks(
            x - 5, y, z - 5,
            x + szer + 5, y + max(szer, wys), z + wys + 5, wypelniacz)
        self.mc.setBlocks(
            x - 1, y - 1, z - 1, x + szer + 1, y - 1, z + wys + 1, granica)
        self.mc.setBlocks(x, y - 1, z, x + szer, y - 1, z + wys, podloga)
        self.mc.setBlocks(
            x, y, z, x + szer, y + max(szer, wys), z + wys, wypelniacz)


# magiczne liczby używane do określenia czy komórka jest żywa
DEAD = 0
ALIVE = 1
BLOK_ALIVE = 35  # block.WOOL


class Populacja(object):
    """
    Populacja komórek
    """

    def __init__(self, mc, ilex, iley):
        """
        Przygotowuje ustawienia populacji
        :param mc: obiekt Minecrafta
        :param ilex: rozmiar x macierzy komórek (wiersze)
        :param iley: rozmiar y macierzy komórek (kolumny)
        """
        self.mc = mc
        self.iley = iley
        self.ilex = ilex
        self.generacja = self.reset_generacja()

    def reset_generacja(self):
        """
        Tworzy i zwraca macierz pustej populacji
        """
        # wyrażenie listowe tworzy x kolumn o y komórkach
        # wypełnionych wartością 0 (DEAD)
        return [[DEAD for y in xrange(self.iley)] for x in xrange(self.ilex)]

    def losuj(self, ile=50):
        """
        Losowo wypełnia macierz żywymi komórkami, czyli wartością 1 (ALIVE)
        """
        for i in range(ile):
            x = randint(0, self.ilex - 1)
            y = randint(0, self.iley - 1)
            self.generacja[x][y] = ALIVE
        print self.generacja


if __name__ == "__main__":
    gra = GraWZycie(mc, 20, 10, 40)  # instancja klasy GraWZycie
    mc.player.setPos(20, 1, 10)
    gra.uruchom()  # wywołanie metody uruchom()
