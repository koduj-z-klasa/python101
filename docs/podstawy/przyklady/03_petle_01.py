#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("Alfabet w porządku naturalnym:")

for i in range(65, 91):
    litera = chr(i)
    tmp = litera + " => " + litera.lower()
    print(tmp, end=" ")

print("\nAlfabet w porządku odwróconym:")
for i in range(122, 96, -1):
    litera = chr(i)
    print(litera.upper(), "=>", litera, end=" ")
