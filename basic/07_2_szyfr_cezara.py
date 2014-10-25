#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/07_2_szyfr_cezara.py

"""
    ZADANIE
    Pobierz od użytkownika ciąg znaków, zaszyfruj go przy wykorzystaniu
    szyfru Cezara o kluczu 3, wyświetl zaszyfrowany ciąg.
"""

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

"""
    JAK TO DZIAŁA
    W programie możemy wykorzystywać zmienne globalne, np. KLUCZ.
    def nazwa_funkcji(argumenty): - tak definiujemy funkcje, które
    mogą lub nie zwracać jakieś wartości.
    nazwa_funkcji(argumenty) - tak wywołujemy funkcje.
    Napisy mogą być indeksowane (od 0), co daje dostęp do pojedynczych znaków.
    Funkcja len(str) zwraca długość napisu, wykorzystana jako argument funkcji
    range() pozwala iterować po znakach napisu.
    Operator += oznacza dodanie argumentu z prawej strony do wartości z lewej.
"""

"""
    CO MOGĘ ZMIENIĆ
    Napisz funkcję deszyfrującą deszyfruj(txt).
    Dodaj do funkcji szyfruj, deszyfruj drugi parametr w postaci długości klucza
    podawanej przez użytkownika.
    Dodaj poprawne szyfrowanie dużych liter, białych znaków i znaków interpunkcyjnych.

def deszyfruj(txt):
    dtxt = ""
    KLUCZM = KLUCZ % 26;
    for i in range(len(txt)):
        if (ord(txt[i]) - KLUCZM < 97):
            dtxt += chr(ord(txt[i]) - KLUCZM + 26)
        else:
            dtxt += chr(ord(txt[i]) - KLUCZM)
    return dtxt

dtxt = deszyfruj(stxt)
print "Ciąg zdeszyfrowany:\n", dtxt

"""
