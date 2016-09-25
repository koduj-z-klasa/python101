#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

# utworzenie połączenia z minecraftem
mc = minecraft.Minecraft.create("192.168.1.10")  # podaj adres IP Rpi


def idzDo(x=0, y=0, z=0):
    """Funkcja przenosi gracza w podane miejsce.
    Parametry: x, y, z - współrzędne miejsca
    """
    y = mc.getHeight(x, z)  # ustalenie wysokości podłoża
    mc.player.setPos(x, y, z)
    return mc.player.getPos()


def przesunSie(x1=0, y1=0, z1=0):
    """Funkcja przesuwa gracza o podaną liczbę bloków
    i zwraca nową pozycję.
    Parametry: x1, y1, z1 - ilość bloków, o którą powiększamy
    lub pomniejszamy współrzędne pozycji gracza.
    """

    x, y, z = mc.player.getPos()  # aktualna pozycja
    y = mc.getHeight(x + x1, z + z1)  # ustalenie wysokości podłoża
    mc.player.setPos(x + x1, y + y1, z + z1)
    return mc.player.getPos()


def drukujPoz():
    """Drukuje pozycję gracza.
    Wymaga globalnego obiektu połączenia mc.
    """

    pos = mc.player.getPos()
    print pos
    pos_str = map(str, (pos.x, pos.y, pos.z))
    mc.postToChat("Pozycja: " + ", ".join(pos_str))


def main(args):
    mc.postToChat("Czesc! Tak dziala MC chat!")  # wysłanie komunikatu do mc
    print idzDo(50, 0, 50)  # wywołanie funkcji idzDo()
    print przesunSie(20)  # wywołanie funkcji przesunSie()
    drukujPoz()  # wywołanie funkcji drukujPoz()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
