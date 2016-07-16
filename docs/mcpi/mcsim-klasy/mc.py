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

# utworzenie połaczenia z 1) minecraftem lub 2) symulatorem
# Ad 1) w cudzysłowie należy podać adres IP Raspberry Pi
# Ad 2) cudzysłów pusty
mc = minecraft.Minecraft.create("")

# wysłanie wiadomości na czat
mc.postToChat("Czesc! Tak dziala MC chat!")

# import klasy budującej świat
if os.path.isfile('mcsym.py'):
    from mcsym import Symulacja
    mysym = Symulacja(mc, block)
