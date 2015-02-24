#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
from peewee import *

if os.path.exists('test.db'):
    os.remove('test.db')
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('test.db') # ':memory:'

# klasa bazowa
class BazaModel(Model):
    class Meta:
        database = baza

# klasy Klasa i Uczen opisują rekordy tabel "klasa" i "uczen"
# oraz relacje między nimi
class Klasa(BazaModel):
    nazwa = CharField(null=False)
    profil = CharField(default='')

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    klasa = ForeignKeyField(Klasa, related_name = 'uczniowie')

baza.connect() # nawiązujemy połączenie z bazą
baza.create_tables([Klasa, Uczen],True) # tworzymy tabele
