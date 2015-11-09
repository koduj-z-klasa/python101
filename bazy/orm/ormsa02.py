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
