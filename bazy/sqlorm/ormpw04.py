#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

if os.path.exists('test.db'):
    os.remove('test.db')
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('test.db')  # ':memory:'

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
if Klasa.select().count() == 0:
    klasa = Klasa(nazwa='1A', profil='matematyczny')
    klasa.save()
    klasa = Klasa(nazwa='1B', profil='humanistyczny')
    klasa.save()

# tworzymy instancję klasy Klasa reprezentującą klasę "1A"
klasa = Klasa.select().where(Klasa.nazwa == '1A').get()
# dodajemy uczniów
uczen = Uczen(imie='Tomasz', nazwisko='Nowak', klasa=klasa)
uczen.save()
uczen = Uczen(imie='Adam', nazwisko='Kowalski', klasa=klasa)
uczen.save()


def czytajdane():
    """Funkcja pobiera i wyświetla dane z bazy"""
    for uczen in Uczen.select():  # lub szybsze: Uczen.select().join(Klasa)
        print uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa
    print ""

czytajdane()
