#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# importujemy funkcje z modułu ocenyfun zapisanego w pliku ocenyfun.py
from ocenyfun import drukuj, srednia, mediana, odchylenie

przedmioty = set(['polski', 'angielski'])  # definicja zbioru
drukuj(przedmioty, "Lista przedmiotów zawiera: ")

print("\nAby przerwać wprowadzanie przedmiotów, naciśnij Enter.")
while True:
    przedmiot = input("Podaj nazwę przedmiotu: ")
    if len(przedmiot):
        if przedmiot in przedmioty:  # czy przedmiot jest w zbiorze?
            print("Ten przedmiot już mamy :-)")
        przedmioty.add(przedmiot)  # dodaj przedmiot do zbioru
    else:
        drukuj(przedmioty, "\nTwoje przedmioty: ")
        przedmiot = input("\nZ którego przedmiotu wprowadzisz oceny? ")
        if przedmiot not in przedmioty:  # jeżeli przedmiotu nie ma w zbiorze
            print("Brak takiego przedmiotu, możesz go dodać.")
        else:
            break  # wyjście z pętli

oceny = []  # pusta lista ocen
ocena = None  # zmienna sterująca pętlą i do pobierania ocen
print("\nAby przerwać wprowadzanie ocen, podaj 0 (zero).")

while not ocena:
    try:
        ocena = int(input("Podaj ocenę (1-6): "))
        if (ocena > 0 and ocena < 7):
            oceny.append(float(ocena))
        elif ocena == 0:
            break
        else:
            print("Błędna ocena.")
        ocena = None
    except ValueError:
        print("Błędne dane!")

drukuj(oceny, przedmiot.capitalize() + " - wprowadzone oceny: ")
s = srednia(oceny)  # wywołanie funkcji z modułu ocenyfun
m = mediana(oceny)  # wywołanie funkcji z modułu ocenyfun
o = odchylenie(oceny, s)  # wywołanie funkcji z modułu ocenyfun
print("\nŚrednia: {0:5.2f}".format(s))
print("Mediana: {0:5.2f}\nOdchylenie: {1:5.2f}".format(m, o, ))
