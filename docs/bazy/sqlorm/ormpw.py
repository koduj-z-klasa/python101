#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

if os.path.exists('test.db'):
    os.remove('test.db')
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('test.db')  # ':memory:'


# BazaModel to klasa bazowa dla klas Grupa i Uczen, które
# opisują rekordy tabel "grupa" i "uczen" oraz relacje między nimi
class BazaModel(Model):
    class Meta:
        database = baza


class Grupa(BazaModel):
    nazwa = CharField(null=False)
    profil = CharField(default='')


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    grupa = ForeignKeyField(Grupa, related_name='uczniowie')


baza.connect()  # nawiązujemy połączenie z bazą
baza.create_tables([Grupa, Uczen], True)  # tworzymy tabele

# dodajemy dwie klasy, jeżeli tabela jest pusta
if Grupa.select().count() == 0:
    inst_grupa = Grupa(nazwa='1A', profil='matematyczny')
    inst_grupa.save()
    inst_grupa = Grupa(nazwa='1B', profil='humanistyczny')
    inst_grupa.save()

# tworzymy instancję klasy Grupa reprezentującą klasę "1A"
inst_grupa = Grupa.select().where(Grupa.nazwa == '1A').get()
# dodajemy uczniów
inst_uczen = Uczen(imie='Tomasz', nazwisko='Nowak', grupa=inst_grupa)
inst_uczen.save()
inst_uczen = Uczen(imie='Adam', nazwisko='Kowalski', grupa=inst_grupa)
inst_uczen.save()


def czytajdane():
    """Funkcja pobiera i wyświetla dane z bazy"""
    for uczen in Uczen.select():  # lub szybsze: Uczen.select().join(Grupa)
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.grupa.nazwa)
    print()


czytajdane()

# przepisanie ucznia do innej klasy
inst_uczen = Uczen.select().join(Grupa).where(Uczen.nazwisko == 'Nowak').get()
inst_uczen.grupa = Grupa.select().where(Grupa.nazwa == '1B').get()
inst_uczen.save()  # zapisanie zmian w bazie
czytajdane()

# usunięcie ucznia o identyfikatorze 1
inst_uczen = Uczen.select().where(Uczen.id == 1).get()
inst_uczen.delete_instance()
czytajdane()

baza.close()
