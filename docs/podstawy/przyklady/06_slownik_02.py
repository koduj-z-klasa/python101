#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os.path  # moduł udostępniający funkcję isfile()

print """Podaj dane w formacie:
wyraz obcy: znaczenie1, znaczenie2
Aby zakończyć wprowadzanie danych, podaj 0.
"""

sFile = "slownik.txt"  # nazwa pliku zawierającego wyrazy i ich tłumaczenia
slownik = {}  # pusty słownik
# wobce = set() # pusty zbiór wyrazów obcych


def otworz(plik):
    if os.path.isfile(sFile):  # czy istnieje plik słownika?
        with open(sFile, "r") as sTxt:  # otwórz plik do odczytu
            for line in sTxt:  # przeglądamy kolejne linie
                # rozbijamy linię na wyraz obcy i tłumaczenia
                t = line.split(":")
                wobcy = t[0]
                # usuwamy znaki nowych linii
                znaczenia = t[1].replace("\n", "")
                znaczenia = znaczenia.split(",")  # tworzymy listę znaczeń
                # dodajemy do słownika wyrazy obce i ich znaczenia
                slownik[wobcy] = znaczenia
    return len(slownik)  # zwracamy ilość elementów w słowniku


def zapisz(slownik):
    # otwieramy plik do zapisu, istniejący plik zostanie nadpisany(!)
    file1 = open(sFile, "w")
    for wobcy in slownik:
        # "sklejamy" znaczenia przecinkami w jeden napis
        znaczenia = ",".join(slownik[wobcy])
        # wyraz_obcy:znaczenie1,znaczenie2,...
        linia = ":".join([wobcy, znaczenia])
        print >>file1, linia  # zapisujemy w pliku kolejne linie
    file1.close()  # zamykamy plik


def oczysc(str):
    str = str.strip()  # usuń początkowe lub końcowe białe znaki
    str = str.lower()  # zmień na małe litery
    return str


# zmienna oznaczająca, że użytkownik uzupełnił lub zmienił słownik
nowy = False
ileWyrazow = otworz(sFile)
print "Wpisów w bazie:", ileWyrazow

# główna pętla programu
while True:
    dane = raw_input("Podaj dane: ")
    t = dane.split(":")
    wobcy = t[0].strip().lower()  # robimy to samo, co funkcja oczysc()
    if wobcy == 'koniec':
        break
    elif dane.count(":") == 1:  # sprawdzamy poprawność wprowadzonych danych
        if wobcy in slownik:
            print "Wyraz", wobcy, " i jego znaczenia są już w słowniku."
            op = raw_input("Zastąpić wpis (t/n)? ")
        # czy wyrazu nie ma w słowniku? a może chcemy go zastąpić?
        if wobcy not in slownik or op == "t":
            znaczenia = t[1].split(",")  # podane znaczenia zapisujemy w liście
            znaczenia = map(oczysc, znaczenia)  # oczyszczamy elementy listy
            slownik[wobcy] = znaczenia
            nowy = True
    else:
        print "Błędny format!"

if nowy:
    zapisz(slownik)

print "=" * 50
print "{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenia")
print "=" * 50
for wobcy in slownik:
    print "{0: <15}{1: <40}".format(wobcy, ",".join(slownik[wobcy]))
