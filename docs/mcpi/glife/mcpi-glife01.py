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

mc = minecraft.Minecraft.create("192.168.1.10")  # połączenie z MCPi


class GraWZycie(object):
    """
    Łączy wszystkie elementy gry w całość.
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


if __name__ == "__main__":
    gra = GraWZycie(mc, 20, 10, 40)  # instancja klasy GraWZycie
    mc.player.setPos(10, 20, -5)
    gra.uruchom()  # wywołanie metody uruchom()
