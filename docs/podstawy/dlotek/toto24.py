#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
# print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

# print("Wylosowane liczby:", liczby)

print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
typy = set()
i = 0
while i < ileliczb:
    typ = input("Podaj liczbę %s: " % (i + 1))
    if typ not in typy:
        typy.add(typ)
        i = i + 1

print("Wytypowane liczby:", typy)

trafione = set(liczby) & typy
if trafione:
    print("\nIlość trafień: %s" % len(trafione))
    print("Trafione liczby: ", trafione)
else:
    print("Brak trafień. Spróbuj jeszcze raz!")
