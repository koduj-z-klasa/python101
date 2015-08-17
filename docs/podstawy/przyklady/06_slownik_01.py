#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    ZADANIE
    Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia.
    Pobierz od użytkownika dane w formacie:
    wyraz obcy: znaczenie1, znaczenie2, ... itd.
    Pobieranie danych kończy wpisanie słowa "koniec".
"""

print """Podaj dane w formacie:
wyraz obcy: znaczenie1, znaczenie2
Aby zakończyć wprowadzanie danych, wpisz 'koniec'.
"""

slownik = {}  # pusty słownik


def oczysc(str):
    str = str.strip()  # usuń początkowe lub końcowe białe znaki
    str = str.lower()  # zmień na małe litery
    return str

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
    else:
        print "Błędny format!"


print "=" * 50
print "{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenia")
print "=" * 50
for wobcy in slownik:
    print "{0: <15}{1: <40}".format(wobcy, ",".join(slownik[wobcy]))
