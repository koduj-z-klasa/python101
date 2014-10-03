#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/07_1_trojkat.py

"""
	ZADANIE
	Program ma sprawdzić, czy z odcinków a, b i c podanych przez użytkownika
	da się utworzyć trójkąt. Jeżeli tak dodatkowo mamy sprawdzić, czy
	jest to trójkąt prostokątny i wydrukować odpowiednią informację.
	Następnie liczymy obwód, pole (ze wzoru Herona) i drukujemy wyniki
	na ekranie.
	Jeżeli z podanych boków nie da się zbudować trójkąta, dajemy szansę
	na ponowne wprowadzenie wartości przez użytkownika.
"""

import math #dołączamy bibliotekę matematyczną

op = "t" #deklarujemy i inicjujemy zmienną pomocniczą
while op != "n": #dopóki wartość zmiennej op jest inna niż znak "n"
#	a, b, c = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")
	#a, b, c = [int(x) for x in raw_input("Podaj 3 boki trójkąta (oddzielone spacjami): ").split()]
	if a+b > c and a+c > b and b+c > a: #warunek złożony
		print "Z podanych boków można zbudować trójkąt."
		if ((a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2): #czy boki spełniają warunki trójkąta prostokątnego?
			print "Do tego prostokątny!"
		
		print "Obwód wynosi:", (a+b+c) #na wyjściu możemy wyprowadzać wyrażenia
		p = 0.5 * (a + b + c) #obliczmy współczynnik wzoru Herona
		P = math.sqrt(p*(p-a)*(p-b)*(p-c)) #liczymy pole ze wzoru Herona
		print "Pole wynosi:", P
		op = "n" #ustawiamy zmienną tak, aby wyjść z pętli while
	else:
		print "Z podanych odcinków nie można utworzyć trójkąta prostokątnego."
		op = raw_input("Spróbujesz jeszcze raz (t/n): ")

print "Do zobaczenia..."

"""
	JAK TO DZIAŁA
	Pętla while wykonuje się dopóki warunek jest prawdziwy, czyli zmienna kontrolna "op"
    różna jest od "n". Dzięki temu użytkownik może wielokrotnie wprowadzać wartości
    boków tworzące trójkąt.
	
	Są dwie metody pobierania kilku wartości z wejścia (np. klawiatury) na raz.
	Funkcja raw_input() zwraca wprowadzone dane zakończone nową linią jako napis.
    Funkcja input() wartości pobrane z wejścia (np. klawiatury) traktuje jak kod Pythona.
	Konstrukcja "int(x) for x in raw_input().split()" wywołuje funkcję int(), która
	usiłuje przekształcić podaną wartość na liczbę całkowitą dla każdej
	wartości wyodrębnionej z ciągu wejściowego przez funkcję split(). Separatorem
	kolejnych wartości są dla funkcji split() białe znaki (spacje, tabulatory).
	Funkcja input() pobiera wejście w postaci napisu, ale próbuje zinterpretować go
	jakby był częścią kodu w Pythonie. Dlatego dane oddzielone przecinkami w postaci
	np. "1, 2, 3" przypisywane są podanym zmiennym.
	
	Funkcje if sprawdzają warunki złożone oparte na koniunkcji (and) i alternatywie (or).
	Wyrażenie x**y oznacza podnoszenie podstawy x do potęgi y.
	Funkcja sqrt() (pierwiastek kwadratowy) zawarta jest w module math, który na początku
	programu trzeba zaimportować.
"""
