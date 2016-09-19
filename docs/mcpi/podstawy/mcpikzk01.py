#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dodanie ścieżki do biblioteki minecraft
# import modułów minecrafta
# ustawienie nazwy użytkownika i komputera
import sys
sys.path.append("/root/mcpi-sim")
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block
import os
os.environ["USERNAME"] = "Steve"  # wpisz dowolną nazwę użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # wpisz dowolną nazwę komputera

# utworzenie połączenia z minecraftem
# UWAGA: wpisujemy adres IP minikomputera Raspberry Pi!
mc = minecraft.Minecraft.create("192.168.1.8")


def main(args):
    mc.postToChat("Czesc! Tak dziala MC chat!")  # wysłanie komunikatu do mc
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
