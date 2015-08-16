#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

if os.path.exists('peewee.db'):
    os.remove('peewee.db')
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('peewee.db')  # ':memory:'

# BazaModel to klasa bazowa dla klas Klasa i Uczen, które
# opisują rekordy tabel "klasa" i "uczen" oraz relacje między nimi


class BazaModel(Model):

    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)
    profil = CharField(default='')


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

baza.connect()  # nawiązujemy połączenie z bazą
baza.create_tables([Klasa, Uczen], True)  # tworzymy tabele

# dodajemy dwie klasy, jeżeli tabela jest pusta
if Klasa().select().count() == 0:
    klasa = Klasa(nazwa='1A', profil='matematyczny')
    klasa.save()
    klasa = Klasa(nazwa='1B', profil='humanistyczny')
    klasa.save()

# tworzymy instancję klasy Klasa reprezentującą klasę "1A"
klasa = Klasa.select().where(Klasa.nazwa == '1A').get()
uczen = Uczen(imie='Tomasz', nazwisko='Nowak', klasa=klasa)
uczen.save()

# odczytujemy dane z bazy
for uczen in Uczen.select().join(Klasa):
    print uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa
print ""

# zmiana klasy ucznia o identyfikatorze 2
uczen = Uczen().select().join(Klasa).where(Uczen.nazwisko == 'Nowak').get()
uczen.klasa = Klasa.select().where(Klasa.nazwa == '1B').get()
uczen.save()  # zapisanie zmian w bazie

# usunięcie ucznia o identyfikatorze 1
Uczen.select().where(Uczen.id == 1).get().delete_instance()

baza.close()
