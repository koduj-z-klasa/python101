#! /usr/bin/env python3
# -*- coding: utf-8 -*-

KLUCZ = 3


def szyfruj(tekst):
    zaszyfrowny = ""
    for znak in tekst:
        if ord(znak) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(znak) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(znak) + KLUCZ)
    return zaszyfrowny


def main(args):
    tekst = input("Podaj ciąg do zaszyfrowania:\n")
    print("Ciąg zaszyfrowany:\n", szyfruj(tekst))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
