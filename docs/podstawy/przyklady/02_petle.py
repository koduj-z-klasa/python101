#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("Alfabet w porządku naturalnym:")
x = 0
for i in range(65, 91):
    litera = chr(i)
    x += 1
    tmp = litera + " => " + litera.lower()
    if i > 65 and x % 5 == 0:
        x = 0
        tmp += "\n"
    print(tmp, end=" ")

x = -1
print("\nAlfabet w porządku odwróconym:")
for i in range(122, 96, -1):
    litera = chr(i)
    x += 1
    if x == 5:
        x = 0
        print("\n", end=" ")
    print(litera.upper(), "=>", litera, end=" ")
