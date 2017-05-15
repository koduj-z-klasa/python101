#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
# print("Wytypuj", ileliczb, "z", maksliczba, " liczb: ")

liczby = []
for i in range(ileliczb):
    liczba = random.randint(1, maksliczba)
    liczby.append(liczba)

print("Wylosowane liczby:", liczby)
