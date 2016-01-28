# -*- coding: utf-8 -*-

from peewee import *
from datetime import datetime

baza = SqliteDatabase('adresy.db')


class BazaModel(Model):  # klasa bazowa

    class Meta:
        database = baza


class Osoba(BazaModel):
    login = CharField(null=False, unique=True)
    haslo = CharField()

    class Meta:
        order_by = ('login',)


class Zadanie(BazaModel):
    tresc = TextField(null=False)
    datad = DateTimeField(default=datetime.now)
    wykonane = BooleanField(default=False)
    osoba = ForeignKeyField(Osoba, related_name='zadania')

    class Meta:
        order_by = ('datad',)


def polacz():
    baza.connect()  # nawiązujemy połączenie z bazą
    baza.create_tables([Osoba, Zadanie], True)  # tworzymy tabele
    return True


def loguj(login, haslo):
    try:
        osoba, created = Osoba.get_or_create(login=login, haslo=haslo)
        return osoba
    except IntegrityError:
        return None


def ladujDane():
    """ Przygotowanie początkowych danych testowych """
    if Osoba.select().count() > 0:
        return
    osoby = ('ala', 'piotr')
    zadania = ('Pierwsze zadanie', 'Drugie zadanie', 'Trzecie zadanie')
    for login in osoby:
        o = Osoba(login=login, haslo='123')
        o.save()
        for tresc in zadania:
            z = Zadanie(tresc=tresc, osoba=o)
            z.save()
    baza.commit()
    baza.close()
