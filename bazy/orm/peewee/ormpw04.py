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

# dodajemy dwie klasy, jeżeli tabela jest pusta
if Klasa().select().count() == 0:
    klasa = Klasa(nazwa = '1A', profil = 'matematyczny')
    klasa.save()
    klasa = Klasa(nazwa = '1B', profil = 'humanistyczny')
    klasa.save()

# tworzymy instancję klasy Klasa reprezentującą klasę "1A"
klasa = Klasa.select().where(Klasa.nazwa == '1A').get()

# lista uczniów, których dane zapisane są w słownikach
uczniowie = [
    { 'imie':'Tomasz', 'nazwisko':'Nowak', 'klasa':klasa },
    { 'imie':'Jan', 'nazwisko':'Kos', 'klasa':klasa },
    { 'imie':'Piotr', 'nazwisko':'Kowalski', 'klasa':klasa }
]

# dodajemy dane wielu uczniów
Uczen.insert_many(uczniowie).execute()

# odczytujemy dane z bazy
def czytajdane():
    for uczen in Uczen.select().join(Klasa):
        print uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa
    print ""

czytajdane()

# zmiana klasy ucznia o identyfikatorze 2
uczen = Uczen().select().join(Klasa).where(Uczen.id == 2).get()
uczen.klasa = Klasa.select().where(Klasa.nazwa == '1B').get()
uczen.save() # zapisanie zmian w bazie

#usunięcie ucznia o identyfikatorze 3
Uczen.select().where(Uczen.id == 3).get().delete_instance()

czytajdane()
