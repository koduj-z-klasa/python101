#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def drukuj(co, kom="Sekwencja zawiera: "):
    print(kom)
    for i in co:
        print(i, end=" ")


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
