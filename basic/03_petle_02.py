#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/03_petle_02.py

""" 
    ZADANIE:
    Wydrukuj alfabet w porządku naturalnym, a następnie odwróconym
    w formacie: mała - duża litera. W jednym wierszu drukujemy po pięć grup.
"""
print "Alfabet w porządku naturalnym:"
x = 0
for i in range(65,91):
    litera = chr(i)
    x += 1
    tmp = litera + " => " + litera.lower()
    if i > 65 and x % 5 == 0:
        x = 0
        tmp += "\n"
    print tmp,

x = -1
print "\nAlfabet w porządku odwróconym:"
for i in range(122,96,-1):
    litera = chr(i)
    x += 1
    if x == 5:
        x = 0
        print "\n",
    print litera.upper(), "=>", litera,

"""
    JAK TO DZIAŁA
    Iteracja polega na wyliczaniu elementów serii, np. zakresu liczb.
    Iteracja jest podstawą powtórzeń realizowanych w pętlach.
    Pętle wykorzystujemy do powtarzania różnych operacji.
    Funkcja range(x,y) generuje listę uporządkowanych wartości od x do y (y nigdy nie jest częścią wygenerowanej listy).
    Funkcja reversed() odwraca porządek listy.
    Funkcja chr(i) zwraca znak reprezentowany przez kod ASCII o wartości i.
    Metoda lower() obiektu string (napisu) zwraca małą literę.
    
    CO MOGĘ ZMIENIĆ
    Wydrukuj co z-tą literę alfabetu, przy czym wartość z podaje użytkownik.
"""
