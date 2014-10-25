#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/03_petle_01.py

""" 
    ZADANIE:
    Wydrukuj alfabet w porządku naturalnym, a następnie odwróconym
    w formacie: mała - duża litera.
"""
print "Alfabet w porządku naturalnym:"

for i in range(65,91):
    litera = chr(i)
    tmp = litera + " => " + litera.lower()
    print tmp,

print "\nAlfabet w porządku odwróconym:"
for i in range(122,96,-1):
    litera = chr(i)
    print litera.upper(), "=>", litera,
