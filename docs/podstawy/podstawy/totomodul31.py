#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

def ustawienia():
    """Funkcja pobiera ilość losowanych liczb, maksymalną losowaną wartość
    oraz ilość prób. Pozwala określić stopień trudności gry."""
    while 1:
        try:
            ile = int(raw_input("Podaj ilość typowanych liczb: "))
            maks = int(raw_input("Podaj maksymalną losowaną liczbę: "))
            if ile > maks:
                print "Błędne dane!"
                continue
            ilelos = int(raw_input("Ile losowań: "))
            return (ile, maks, ilelos)
        except:
            print "Błędne dane!"
            continue

def losujliczby(ile, maks):
    """Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks"""
    liczby = []
    i = 0
    while i < ile:
        liczba = random.randint(1, maks)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1
    return liczby


def pobierztypy(ile, maks):
    """Funkcja pobiera od użytkownika jego typy wylosowanych liczb"""
    print "Wytypuj",ile,"z",maks," liczb: "
    typy = set()
    i = 0
    while i < ile:
        try:
            typ = int(raw_input("Podaj liczbę "+str(i+1)+": "))
        except ValueError:
            print "Błędne dane!"
            continue

        if 0 < typ <= maks and typ not in typy:
            typy.add(typ)
            i = i + 1
    return typy

def wyniki(liczby, typy):
    trafione = liczby & typy
    if trafione:
        print "\nIlość trafień: ",len(trafione)
        print "Trafione liczby: ",trafione
    else:
        print "Brak trafień. Spróbuj jeszcze raz!"
    print "\n"+"x"*40+"\n" # wydrukuj 40 znaków x

    return len(trafione)
