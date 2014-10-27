#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/01_hello.py

# deklarujemy i inicjalizujemy zmienne
curYear = 2014
pythonYear = 1989
# obliczamy wiek Pythona
wiekPythona = curYear - pythonYear

# pobieramy dane
imie = raw_input('Jak się nazywasz? ')
wiek = int(raw_input('Ile masz lat? '))

print "Witaj w moim świecie ",imie
print "Mów mi Python, mam", wiekPythona, "lat."

# instrukcja warunkowa
if wiek > wiekPythona:
	print 'Jesteś starszy ode mnie.'
else:
	print 'Jesteś młodszy ode mnie.'
