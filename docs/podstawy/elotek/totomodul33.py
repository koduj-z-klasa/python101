#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import json


def ustawienia():
    """Funkcja pobiera nick użytkownika, ilość losowanych liczb, maksymalną
    losowaną wartość oraz ilość typowań. Ustawienia zapisuje."""

    nick = raw_input("Podaj nick: ")
    nazwapliku = nick + ".ini"
    gracz = czytaj_ust(nazwapliku)
    odp = None
    if gracz:
        print "Twoje ustawienia:"
        print "Liczb:", gracz[1]
        print "Z Maks:", gracz[2]
        print "Losowań:", gracz[3]
        odp = raw_input("Zmieniasz (t/n)? ")

    if not gracz or odp.lower() == "t":
        while True:
            try:
                ile = int(raw_input("Podaj ilość typowanych liczb: "))
                maks = int(raw_input("Podaj maksymalną losowaną liczbę: "))
                if ile > maks:
                    print "Błędne dane!"
                    continue
                ilelos = int(raw_input("Ile losowań: "))
                break
            except:
                print "Błędne dane!"
                continue
        gracz = zapisz_ust(nazwapliku,
                           [nick, str(ile), str(maks), str(ilelos)])

    return gracz[0:1] + map(int, gracz[1:4])


def czytaj_ust(nazwapliku):
    if os.path.isfile(nazwapliku):
        plik = open(nazwapliku, "r")
        linia = plik.readline()
        if linia:
            return linia.split(";")
    return False


def zapisz_ust(nazwapliku, gracz):
    plik = open(nazwapliku, "w")
    plik.write(";".join(gracz))
    plik.close()
    return gracz


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
    print "Wytypuj %s z %s liczb: " % (ile, maks)
    typy = set()
    i = 0
    while i < ile:
        try:
            typ = int(raw_input("Podaj liczbę %s: " % (i + 1)))
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
        print "\nIlość trafień: %s" % len(trafione)
        print trafione
        trafione = ", ".join(map(str, trafione))
        print "Trafione liczby: %s" % trafione
    else:
        print "Brak trafień. Spróbuj jeszcze raz!"
    print "\n" + "x" * 40 + "\n"  # wydrukuj 40 znaków x

    return len(trafione)


def czytaj_json(nazwapliku):
    """Funkcja odczytuje dane w formacie json z pliku"""
    dane = []
    if os.path.isfile(nazwapliku):
        with open(nazwapliku, "r") as plik:
            dane = json.load(plik)
    return dane


def zapisz_json(nazwapliku, dane):
    """Funkcja zapisuje dane w formacie json do pliku"""
    with open(nazwapliku, "w") as plik:
        json.dump(dane, plik)
