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

# dodajemy dwie klasy, jeżeli tabela jest pusta
if Klasa().select().count() == 0:
    klasa = Klasa(nazwa='1A', profil='matematyczny')
    klasa.save()
    klasa = Klasa(nazwa='1B', profil='humanistyczny')
    klasa.save()

# tworzymy instancję klasy Klasa reprezentującą klasę "1A"
klasa = Klasa.select().where(Klasa.nazwa == '1A').get()

# lista uczniów, których dane zapisane są w słownikach
uczniowie = [
    {'imie': 'Tomasz', 'nazwisko': 'Nowak', 'klasa': klasa},
    {'imie': 'Jan', 'nazwisko': 'Kos', 'klasa': klasa},
    {'imie': 'Piotr', 'nazwisko': 'Kowalski', 'klasa': klasa}
]
# dodajemy dane wielu uczniów
Uczen.insert_many(uczniowie).execute()

# odczytujemy dane z bazy
print('Klasy:')
klasy = Klasa.select()
for klasa in klasy:
    print(klasa.id, klasa.nazwa, klasa.profil)
print()

# odczytujemy dane z bazy
print('Uczniowie:')
def czytaj_dane():
    for uczen in Uczen.select().join(Klasa):
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    print()

czytaj_dane()

# zmiana klasy ucznia o identyfikatorze 2
uczen = Uczen().select().join(Klasa).where(Uczen.id == 2).get()
nowa_klasa = Klasa.select().where(Klasa.nazwa == '1B').get()
uczen.klasa = nowa_klasa
uczen.save()  # zapisanie zmian w bazie

# usunięcie ucznia o identyfikatorze 3
uczen = Uczen.select().where(Uczen.id == 3).get()
uczen.delete_instance()

czytaj_dane()
baza.close()
