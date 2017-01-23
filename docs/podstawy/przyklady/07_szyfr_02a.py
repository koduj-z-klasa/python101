#! /usr/bin/env python
# -*- coding: utf-8 -*-

KLUCZ = 3


def szyfruj(tekst):
    stxt = ""
    for znak in tekst:
        if ord(znak) > 122 - KLUCZ:
            stxt += chr(ord(znak) + KLUCZ - 26)
        else:
            stxt += chr(ord(znak) + KLUCZ)
    return stxt


u_tekst = raw_input("Podaj ciąg do zaszyfrowania:\n")
print "Ciąg zaszyfrowany:\n", szyfruj(u_tekst)
