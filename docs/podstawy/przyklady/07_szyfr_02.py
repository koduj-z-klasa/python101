#! /usr/bin/env python
# -*- coding: utf-8 -*-

KLUCZ = 3


def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny

u_tekst = raw_input("Podaj ciąg do zaszyfrowania:\n")
print "Ciąg zaszyfrowany:\n", szyfruj(u_tekst)
