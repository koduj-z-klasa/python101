#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# deklarujemy i inicjalizujemy zmienne
aktRok = 2014
pythonRok = 1989
# obliczamy wiek Pythona
wiekPythona = aktRok - pythonRok

# pobieramy dane
imie = input('Jak się nazywasz? ')
wiek = int(input('Ile masz lat? '))

# wyświetlamy komunikaty
print("Witaj", imie)
print("Mów mi Python, mam", wiekPythona, "lat.")

# instrukcja warunkowa
if wiek > wiekPythona:
    print('Jesteś starszy ode mnie.')
else:
    print('Jesteś młodszy ode mnie.')
