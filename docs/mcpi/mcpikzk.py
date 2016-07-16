#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dodanie ścieżki do biblioteki minecraft
import sys
sys.path.append("/root/mcpi-sim")
# import modułów minecrafta
import mcpi.minecraft as minecraft
import mcpi.block as block

# ustawienie nazwy użytkownika i komputera
import os
os.environ["USERNAME"] = "Steve"  # wpisz dowolną nazwę użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # wpisz dowolną nazwę komputera

# utworzenie połączenia z minecraftem
# UWAGA: wpisujemy adres IP minikomputera Raspberry Pi!
mc = minecraft.Minecraft.create("192.168.1.8")

# wysłanie komunikatu do mc
mc.postToChat("Czesc! Tak dziala MC chat!")


def przesun(x1=0, y1=0, z1=0):
    """Funkcja przesuwa gracza o podaną liczbę bloków
    i zwraca nową pozycję.

    Parametry: x1, y1, z1 - ilość bloków, o którą powiększamy
    lub pomniejszamy współrzędne pozycji gracza.
    """

    x, y, z = mc.player.getPos()
    mc.player.setPos(x + x1, y + y1, z + z1)
    return mc.player.getPos()

print przesun(20)


def drukujPoz():
    """Drukuje pozycję gracza.
    Wymaga globalnego obiektu połączenia mc.
    """

    pos = mc.player.getPos()
    print pos
    pos_str = map(str, (pos.x, pos.y, pos.z))
    mc.postToChat(", ".join(pos_str))

drukujPoz()

from time import sleep

krok = 10
mc.player.setPos(0, 0, 0)
# pobranie współrzędnych aktualnej pozycji gracza
x, y, z = mc.player.getPos()

for i in range(krok):
    przesun(0, 2, 0)  # idź 2*krok bloków do góry - latamy :-)
sleep(2)

mc.camera.setFollow()  # ustawienie kamery z góry

for i in range(krok):
    przesun(1)  # idź krok bloków w prawo
sleep(2)

for i in range(krok):
    przesun(-1)  # idź krok bloków w lewo
sleep(2)

for i in range(krok):
    przesun(0, 0, 1)  # idź krok bloków do przodu
sleep(2)

for i in range(krok):
    przesun(0, 0, -1)  # idź krok bloków do tyłu

drukujPoz()
mc.camera.setNormal()  # ustawienie kamery normalnie


def konstruktor(x, y, z, roz=10, gracz=False):
    """Funkcja wypełnia sześcienny obszar od podanej pozycji
    powietrzem i opcjonalnie umieszcza gracza w środku.
    Parametry: x, y, z - współrzędne pozycji początkowej,
    roz - rozmiar wypełnianej przestrzeni,
    blok - rodzaj bloku
    gracz - czy umieścić gracza w środku
    Wymaga globalnego obiektu block.
    """

    # kamienna podłoże
    mc.setBlocks(x, y - 1, z, x + roz, y - 1, z + roz, block.STONE)
    # czyszczenie
    mc.setBlocks(x, y, z, x + roz, y + roz, z + roz, block.AIR)
    # umieść gracza w środku
    if gracz:
        mc.player.setPos(x + roz / 2, y + roz / 2, z + roz / 2)

konstruktor(50, 0, 0, 20, True)
