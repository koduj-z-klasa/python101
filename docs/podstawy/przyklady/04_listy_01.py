#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ~/python/04_1_listy.py

tupla = input("Podaj liczby oddzielone przecinkami: ")
lista = []
for i in range(len(tupla)):
    lista.append(int(tupla[i]))

print "Elementy i ich indeksy:"
for i, v in enumerate(lista):
    print v, "[", i, "]"

print "Elementy w odwróconym porządku:"
for e in reversed(lista):
    print e,

print ""
print "Elementy posortowane rosnąco:"
for e in sorted(lista):
    print e,

print ""
e = int(raw_input("Którą liczbę usunąć? "))
lista.remove(e)
print lista

print "Dodawanie elementów do listy"
a, i = input("Podaj element i indeks oddzielone przecinkiem: ")
lista.insert(i, a)
print lista

print "Wyszukiwanie i zliczanie elementu w liście"
e = int(raw_input("Podaj liczbę: "))
print "Liczba wystąpień: "
print lista.count(e)
print "Indeks pierwszego wystąpienia: "
if lista.count(e):
    print lista.index(e)
else:
    print "Brak elementu w liście"

print "Pobieramy ostatni element z listy: "
print lista.pop()
print lista

print "Część listy:"
i, j = input("Podaj indeks początkowy i końcowy oddzielone przecinkiem: ")
print lista[i:j]
