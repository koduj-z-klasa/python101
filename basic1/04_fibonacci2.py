#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/04_2_fibonacci.py

"""
	ZADANIE
	Wypisz ciąg Fibonacciego aż do n-ego wyrazu podanego przez użytkownika.
	Ciąg Fibbonaciego to ciąg liczb naturalnych, którego każdy wyraz poza
    dwoma pierwszymi jest sumą dwóch wyrazów poprzednich.
    Początkowe wyrazy tego ciągu to:
    0 1 1 2 3 5 8 13 21
"""

def fibonacci(n): #definicja funkcji
    pwyrazy = (0, 1) #dwa pierwsze wyrazy ciągu zapisane w tupli
    a, b = pwyrazy #przypisanie wielokrotne, rozpakowanie tupli
    while a < n:
        print b,
        a, b = b, a+b #przypisanie wielokrotne

n = int(raw_input("Podaj numer wyrazu: "))
fibonacci(n)
print ""
print "=" * 20

def fibonacci2(n):
    pwyrazy = (0, 1)
    a, b = pwyrazy
    while a < n:
        a, b = b, a+b
    print a

fibonacci2(n)
