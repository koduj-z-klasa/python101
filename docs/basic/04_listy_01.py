#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/04_1_listy.py

tupla = input("Podaj liczby oddzielone przecinkami: ")
lista = [] # deklaracja pustej listy
for i in range(len(tupla)):
    lista.append(int(tupla[i]))

print "Elementy i ich indeksy:"
for i, v in enumerate(lista):
    print v, "[",i,"]"

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

a, i = input("Podaj element do dodania i indeks, przed którym ma się on znaleźć: ")
lista.insert(i, a)
print lista

e = int(raw_input("Podaj liczbę, której wystąpienia w liście chcesz zliczyć? "))
print lista.count(e)
print "Pierwszy indeks, pod którym zapisana jest podana liczba to: "
print lista.index(e)

print "Pobieramy ostatni element z listy: "
print lista.pop()
print lista

i, j = input("Podaj indeks początkowy i końcowy, aby uzyskać frgament listy: ")
print lista[i:j]
