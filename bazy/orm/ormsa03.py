#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

if os.path.exists('test.db'):
    os.remove('test.db')
# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///test.db')  # ':memory:'

# klasa bazowa
BazaModel = declarative_base()


# klasy Klasa i Uczen opisują rekordy tabel "klasa" i "uczen"
# oraz relacje między nimi


class Klasa(BazaModel):
    __tablename__ = 'klasa'
    id = Column(Integer, primary_key=True)
    nazwa = Column(String(100), nullable=False)
    profil = Column(String(100), default='')
    uczniowie = relationship('Uczen', backref='klasa')


class Uczen(BazaModel):
    __tablename__ = 'uczen'
    id = Column(Integer, primary_key=True)
    imie = Column(String(100), nullable=False)
    nazwisko = Column(String(100), nullable=False)
    klasa_id = Column(Integer, ForeignKey('klasa.id'))

# tworzymy tabele
BazaModel.metadata.create_all(baza)

# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
BDSesja = sessionmaker(bind=baza)
sesja = BDSesja()

# dodajemy dwie klasy, jeżeli tabela jest pusta
if not sesja.query(Klasa).count():
    sesja.add(Klasa(nazwa='1A', profil='matematyczny'))
    sesja.add(Klasa(nazwa='1B', profil='humanistyczny'))

# tworzymy instancję klasy Klasa reprezentującą klasę "1A"
klasa = sesja.query(Klasa).filter_by(nazwa='1A').one()

# dodajemy dane wielu uczniów
sesja.add_all([
    Uczen(imie='Tomasz', nazwisko='Nowak', klasa_id=klasa.id),
    Uczen(imie='Jan', nazwisko='Kos', klasa_id=klasa.id),
    Uczen(imie='Piotr', nazwisko='Kowalski', klasa_id=klasa.id),
])


def czytajdane():
    for uczen in sesja.query(Uczen).join(Klasa).all():
        print uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa
    print ""

czytajdane()
