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
