#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/07_2_szyfr_cezara.py

KLUCZ = 3

def szyfruj(txt):
    stxt = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            stxt += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            stxt += chr(ord(txt[i]) + KLUCZ)
    return stxt;

utxt = raw_input("Podaj ciąg do zaszyfrowania:\n")
stxt = szyfruj(utxt)
print "Ciąg zaszyfrowany:\n", stxt
