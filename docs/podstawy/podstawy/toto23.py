#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

ileliczb = int(raw_input("Podaj ilość typowanych liczb: "))
maksliczba = int(raw_input("Podaj maksymalną losowaną liczbę: "))
#print "Wytypuj",ileliczb,"z",makliczba," liczb: "

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

#print "Wylosowane liczby:",liczby

print "Wytypuj",ileliczb,"z",maksliczba," liczb: "
typy = set()
i = 0
while i < ileliczb:
    typ = raw_input("Podaj liczbę "+str(i+1)+": ")
    if typ not in typy:
        typy.add(typ)
        i = i + 1

print "Wytypowane liczby:",typy
