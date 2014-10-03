#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/01_if.py
"""
    ZADANIE
    Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza
    i wydrukuj ją na ekranie.
"""
op = "t"
while op == "t":
    a, b, c = raw_input("Podaj trzy liczby oddzielone spacjami: ").split(" ")
    
    print "Wprowadzono liczby:", a, b, c,
    print "\nNajmniejsza: ",

    if a < b:
        if a < c:
            print a
    elif b < c:
        print b
    else:
        print c
        
    op = raw_input("Jeszcze raz (t/n)? ")

print "By, by..."
