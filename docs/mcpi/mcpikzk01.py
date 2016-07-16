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
