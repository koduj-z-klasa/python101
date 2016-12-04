#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from time import sleep
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

mc = minecraft.Minecraft.create("192.168.1.10")  # połączenie z MCPi


class GraRobotow(object):
    """Główna klasa gry"""

    obstacle = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),
        (10,0),(11,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(0,1),
        (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(12,1),(13,1),(14,1),(15,1),
        (16,1),(17,1),(18,1),(0,2),(1,2),(2,2),(3,2),(4,2),(14,2),(15,2),
        (16,2),(17,2),(18,2),(0,3),(1,3),(2,3),(16,3),(17,3),(18,3),(0,4),
        (1,4),(2,4),(16,4),(17,4),(18,4),(0,5),(1,5),(17,5),(18,5),(0,6),
        (1,6),(17,6),(18,6),(0,7),(18,7),(0,8),(18,8),(0,9),(18,9),(0,10),
        (18,10),(0,11),(18,11),(0,12),(1,12),(17,12),(18,12),(0,13),(1,13),
        (17,13),(18,13),(0,14),(1,14),(2,14),(16,14),(17,14),(18,14),(0,15),
        (1,15),(2,15),(16,15),(17,15),(18,15),(0,16),(1,16),(2,16),(3,16),
        (4,16),(14,16),(15,16),(16,16),(17,16),(18,16),(0,17),(1,17),(2,17),
        (3,17),(4,17),(5,17),(6,17),(12,17),(13,17),(14,17),(15,17),(16,17),
        (17,17),(18,17),(0,18),(1,18),(2,18),(3,18),(4,18),(5,18),(6,18),
        (7,18),(8,18),(9,18),(10,18),(11,18),(12,18),(13,18),(14,18),(15,18),
        (16,18),(17,18),(18,18)]

    plansza = []  # współrzędne dozwolonych pól gry

    def __init__(self, mc):
        """Konstruktor klasy"""
        self.mc = mc
        self.poleGry(0, 0, 0, 18)
        # self.mc.player.setPos(19, 20, 19)

    def poleGry(self, x, y, z, roz=10):
        """Funkcja tworzy pole gry"""

        podloga = block.STONE
        wypelniacz = block.AIR

        # podloga i czyszczenie
        self.mc.setBlocks(x, y - 1, z, x + roz, y - 1, z + roz, podloga)
        self.mc.setBlocks(x, y, z, x + roz, y + roz, z + roz, wypelniacz)
        # granice pola
        x = y = z = 0
        for i in range(19):
            for j in range(19):
                if (i, j) in self.obstacle:
                    self.mc.setBlock(x + i, y, z + j, block.GRASS)
                else:  # tworzenie listy współrzędnych dozwolonych pól gry
                    self.plansza.append((x + i, z + j))


def main(args):
    gra = GraRobotow(mc)  # instancja klasy GraRobotow
    print gra.plansza  # pokaż w konsoli listę współrzędnych pól gry
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
