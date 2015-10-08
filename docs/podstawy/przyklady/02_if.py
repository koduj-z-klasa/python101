#! /usr/bin/env python
# -*- coding: utf-8 -*-

op = "t"
while op == "t":
    a, b, c = raw_input("Podaj trzy liczby oddzielone spacjami: ").split(" ")

    print "Wprowadzono liczby:", a, b, c,
    print "\nNajmniejsza: ",

    if a < b:
        if a < c:
            print a
        else:
            print c
    elif b < c:
        print b
    else:
        print c

    op = raw_input("Jeszcze raz (t/n)? ")

print "By, by..."
