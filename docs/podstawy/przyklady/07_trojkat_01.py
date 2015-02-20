#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/07_1_trojkat.py

import math #dołączamy bibliotekę matematyczną

op = "t" #deklarujemy i inicjujemy zmienną pomocniczą
while op != "n": #dopóki wartość zmiennej op jest inna niż znak "n"
#   a, b, c = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")
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
