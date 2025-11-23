import os
from peewee import SqliteDatabase, Model
from peewee import CharField, ForeignKeyField

plik_bazy = 'baza_pw.db'
if os.path.exists(plik_bazy):
    os.remove(plik_bazy)

# tworzymy instancję klasy Database do obsługi bazy
baza = SqliteDatabase(plik_bazy)  # ':memory:'

# klasa bazowa dla modeli
class Base(Model):
    class Meta:
        database = baza


# klasy Klasa i Uczen opisują rekordy tabel "klasa" i "uczen" oraz relacje między nimi
class Klasa(Base):
    nazwa = CharField(null=False)
    profil = CharField(default='')


class Uczen(Base):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')


baza.connect()  # nawiązujemy połączenie z bazą
baza.create_tables([Klasa, Uczen])  # tworzymy tabele
