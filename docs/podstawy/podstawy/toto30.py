#! /usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy

# program główny

# ustalamy trudność gry
ileliczb, maksliczba, ilerazy = ustawienia()

# losujemy liczby
liczby = losujliczby(ileliczb, maksliczba)

# trzy razy pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
for i in range(ilerazy):
    typy = pobierztypy(ileliczb, maksliczba)
    trafione = set(liczby) & typy
    if trafione:
        print "\nIlość trafień: ", len(trafione)
        print "Trafione liczby: ", trafione
    else:
        print "Brak trafień. Spróbuj jeszcze raz!"

    print "\n" + "x" * 40 + "\n"  # wydrukuj 40 znaków x

print "Wylosowane liczby:", liczby
