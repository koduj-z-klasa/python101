#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os  # moduł udostępniający funkcję isfile()
import csv  # moduł do obsługi formatu csv

slownik = {}  # pusty słownik
sFile = "slownik.csv"  # nazwa pliku zawierającego wyrazy i ich tłumaczenia


def otworz(plik):
    if os.path.isfile(sFile):  # czy istnieje plik słownika?
        with open(sFile, newline='') as plikcsv:  # otwórz plik do odczytu
            tresc = csv.reader(plikcsv)
            for linia in tresc:  # przeglądamy kolejne linie
                slownik[linia[0]] = linia[1:]
    return len(slownik)  # zwracamy ilość elementów w słowniku


def zapisz(slownik):
    # otwieramy plik do zapisu, istniejący plik zostanie nadpisany(!)
    with open(sFile, "w", newline='') as plikcsv:
        tresc = csv.writer(plikcsv)
        for wobcy in slownik:
            lista = slownik[wobcy]
            lista.insert(0, wobcy)
            tresc.writerow(lista)


def oczysc(str):
    str = str.strip()  # usuń początkowe lub końcowe białe znaki
    str = str.lower()  # zmień na małe litery
    return str


def main(args):
    print("""Podaj dane w formacie:
    wyraz obcy: znaczenie1, znaczenie2
    Aby zakończyć wprowadzanie danych, podaj 0.
    """)

    # wobce = set() # pusty zbiór wyrazów obcych
    # zmienna oznaczająca, że użytkownik uzupełnił lub zmienił słownik
    nowy = False
    ileWyrazow = otworz(sFile)
    print("Wpisów w bazie:", ileWyrazow)

    # główna pętla programu
    while True:
        dane = input("Podaj dane: ")
        t = dane.split(":")
        wobcy = t[0].strip().lower()  # robimy to samo, co funkcja oczysc()
        if wobcy == 'koniec':
            break
        elif dane.count(":") == 1:  # sprawdzamy poprawność danych
            if wobcy in slownik:
                print("Wyraz", wobcy, " i jego znaczenia są już w słowniku.")
                op = input("Zastąpić wpis (t/n)? ")
            # czy wyrazu nie ma w słowniku? a może chcemy go zastąpić?
            if wobcy not in slownik or op == "t":
                znaczenia = t[1].split(",")  # znaczenia zapisujemy w liście
                znaczenia = list(map(oczysc, znaczenia))  # oczyszczamy listę
                slownik[wobcy] = znaczenia
                nowy = True
        else:
            print("Błędny format!")

    if nowy:
        zapisz(slownik)

    print("=" * 50)
    print("{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenia"))
    print("=" * 50)
    for wobcy in slownik:
        print("{0: <15}{1: <40}".format(wobcy, ",".join(slownik[wobcy])))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
