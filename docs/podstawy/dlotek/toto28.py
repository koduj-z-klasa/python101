#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

try:
    ileliczb = int(raw_input("Podaj ilość typowanych liczb: "))
    maksliczba = int(raw_input("Podaj maksymalną losowaną liczbę: "))
    if ileliczb > maksliczba:
        print "Błędne dane!"
        exit()
except:
    print "Błędne dane!"
    exit()

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

for i in range(3):
    print "Wytypuj %s z %s liczb: " % (ileliczb, maksliczba)
    typy = set()
    i = 0
    while i < ileliczb:
        try:
            typ = int(raw_input("Podaj liczbę %s: " % (i + 1)))
        except ValueError:
            print "Błędne dane!"
            continue

        if 0 < typ <= maksliczba and typ not in typy:
            typy.add(typ)
            i = i + 1

    trafione = set(liczby) & typy
    if trafione:
        print "\nIlość trafień: %s" % len(trafione)
        print "Trafione liczby: ", trafione
    else:
        print "Brak trafień. Spróbuj jeszcze raz!"

    print "\n" + "x" * 40 + "\n"  # wydrukuj 40 znaków x

print "Wylosowane liczby:", liczby
