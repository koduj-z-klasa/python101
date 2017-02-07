#!/usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy


def main(args):
    # ustawienia gry
    ileliczb, maksliczba, ilerazy = ustawienia()

    # losujemy liczby
    liczby = losujliczby(ileliczb, maksliczba)

    # pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)
        trafione = set(liczby) & typy
        if trafione:
            print "\nIlość trafień: %s" % len(trafione)
            print "Trafione liczby: %s" % trafione
        else:
            print "Brak trafień. Spróbuj jeszcze raz!"

        print "\n" + "x" * 40 + "\n"  # wydrukuj 40 znaków x

    print "Wylosowane liczby:", liczby
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
