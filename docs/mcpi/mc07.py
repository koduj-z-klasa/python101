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

# wysłanie wiadomości na czat
mc.postToChat("Cześć! Tak działa MC chat!")


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


def buduj():
    """
    Funkcja do testowania umieszczania bloków.
    Wymaga: globalnych obiektów mc i block.
    """
    for i in range(19):
        mc.setBlock(0 + i, 0, 18, block.CACTUS)


def polegry():
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
    x = y = z = 0
    for i in range(19):
        for j in range(19):
            if (i, j) in obstacle:
                mc.setBlock(x + i, y, z + j, block.GRASS)
            else:
                mc.setBlock(x + i, y, z + j, block.AIR)


def wybierz_blok(pid, hp):
    player1_bloki = (block.GRAVEL, block.SANDSTONE, block.BRICK_BLOCK,
                     block.FARMLAND, block.OBSIDIAN, block.OBSIDIAN)
    player2_bloki = (block.WOOL, block.LEAVES, block.CACTUS,
                     block.MELON, block.WOOD, block.WOOD)
    if pid:
        return player1_bloki[hp / 10]
    else:
        return player2_bloki[hp / 10]


def pokaz_runde(runda):
    from time import sleep
    polegry()
    for robot in runda:
        blok = wybierz_blok(robot['player_id'], robot['hp'])
        loc = robot['location']
        print robot['player_id'], blok, loc[0], loc[1]
        mc.setBlock(loc[0], 0, loc[1], blok)
    sleep(1)
    print


def pokaz_gre(ile=100):
    import json
    plik = open("lastgame.log", "r")
    dane = json.load(plik)
    runda_nr = 0

    for r in dane:
        print "Runda ", runda_nr
        # print(r)
        pokaz_runde(r)
        runda_nr = runda_nr + 1
        if runda_nr > ile:
            break


def main(args):
    plac(0, 0, 0, 18)
    # buduj()
    pokaz_gre(80)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
