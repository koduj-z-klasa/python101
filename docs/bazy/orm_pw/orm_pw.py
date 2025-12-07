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

# dodajemy dwie klasy
klasa1 = Klasa.create(nazwa='1A', profil='matematyczny')
klasa2 = Klasa(nazwa='1B', profil='humanistyczny')
klasa2.save()

# lista uczniów, których dane zapisane są w słownikach
uczniowie = [
    {'imie': 'Tomasz', 'nazwisko': 'Nowak', 'klasa': klasa1},
    {'imie': 'Jan', 'nazwisko': 'Kos', 'klasa': klasa2},
    {'imie': 'Piotr', 'nazwisko': 'Kowalski', 'klasa': klasa2}
]
# dodajemy dane wielu uczniów
Uczen.insert_many(uczniowie).execute()

# odczytujemy wiele rekordów
print('Klasy:')
klasy = Klasa.select()
for klasa in klasy:
    print(klasa.id, klasa.nazwa, klasa.profil)
print()

# odczytujemy jeden rekord
klasa = Klasa.select().where(Klasa.nazwa == '1A').get()
# klasa = Klasa.get(Klasa.nazwa == '1A')
print('Klasa:', klasa.nazwa)
print()

def wypisz_listę_uczniow():
    """ Odczytujemy i wypisujemy dane uczniów, w tym klasę"""
    if Uczen().select().count():
        print('Uczniowie:')
        uczniowie = Uczen.select().join(Klasa)
        for uczen in uczniowie:
            print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
        print()
    else:
        print('Brak uczniów w bazie!')

wypisz_listę_uczniow()

# zmiana klasy ucznia o identyfikatorze 2
uczen = Uczen().select().join(Klasa).where(Uczen.id == 2).get()
nowa_klasa = Klasa.select().where(Klasa.nazwa == '1A').get()
print('Zmieniam klasę ucznia:', uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
uczen.klasa = nowa_klasa
uczen.save()  # zapisanie zmian w bazie
wypisz_listę_uczniow()

# usunięcie ucznia o identyfikatorze 3
uczen = Uczen.select().where(Uczen.id == 3).get()
print('Usuwam ucznia:', uczen.id, uczen.imie, uczen.nazwisko)
uczen.delete_instance()
wypisz_listę_uczniow()

print('Usuwam uczniów z klasy 1A')
zapytanie = Uczen.delete().where(Uczen.klasa == Klasa.get(Klasa.nazwa == '1A'))
zapytanie.execute()
wypisz_listę_uczniow()

baza.close()
