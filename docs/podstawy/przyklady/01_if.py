#! /usr/bin/env python3
# -*- coding: utf-8 -*-

op = "t"
while op == "t":
    a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").split(" ")

    print("Wprowadzono liczby:", a, b, c)
    print("\nNajmniejsza:")

    if a < b:
        if a < c:
            najmniejsza = a
        else:
            najmniejsza = c
    elif b < c:
        najmniejsza = b
    else:
        najmniejsza = c

    print(najmniejsza)

    op = input("Jeszcze raz (t/n)? ")

print("Koniec.")
