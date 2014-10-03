#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/01_hello.py

"""
	ZADANIE:
	Pobierz od użytkownika imię, wiek i powitaj go komunikatem:
	"Mów mi Python, mam x lat.
	Witaj w moim świecie imie.
	Jesteś starszy(młodszy) ode mnie."
    POJĘCIA:
    Zmienne, wyrażenia, wejście i wyjście danych, instrukcje warunkowe
"""
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

"""
	JAK TO DZIAŁA:
	Deklaracja zmiennej polega na podaniu jej nazwy i przypisaniu jej jakiejś wartości za pomocą operatora "=".
    Zmiennym często przypisujemy wartości za pomocą wyrażeń, czyli działań na zmiennych i/lub stałych.
	Funkcja raw_input() zwraca pobrane z klawiatury znaki jako typ string (napis).
	Funkcja int() pozwala na konwersję typu string na integer (liczba całkowita), czyli pobranie liczby.
	Funkcja print drukuje podane argumenty, stałe napisowe lub zmienne, oddzielone przecinkami.
	Instrukcja warunkowa "if" oblicza podane wyrażenie zakończone dwukropkiem, w zależności od wyniku
    (True lub False) wykonuje pierwszą lub drugą (po else:) operację(e).
"""

"""
	CO MOGĘ ZMIENIĆ:
	Uwzględnij możliwość, że podany wiek i wiekPythona są równe.
"""
