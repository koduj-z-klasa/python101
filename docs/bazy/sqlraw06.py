#! /usr/bin/env python2
# -*- coding: UTF-8 -*-

import sqlite3

# utworzenie połączenia z bazą przechowywaną na dysku
# lub w pamięci (':memory:')
con = sqlite3.connect('test.db')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()

# tworzenie tabel
cur.execute("DROP TABLE IF EXISTS klasa;")

cur.execute("""
    CREATE TABLE IF NOT EXISTS klasa (
        id INTEGER PRIMARY KEY ASC,
        nazwa varchar(250) NOT NULL,
        profil varchar(250) DEFAULT ''
    )""")

cur.executescript("""
    DROP TABLE IF EXISTS uczen;
    CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        klasa_id INTEGER NOT NULL,
        FOREIGN KEY(klasa_id) REFERENCES klasa(id)
    )""")

# wstawiamy jeden rekord danych
cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1A','matematyczny'))
cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1B','humanistyczny'))

# wykonujemy zapytanie SQL, które pobierze id klasy "1A" z tabeli "klasa".
cur.execute('SELECT id FROM klasa WHERE nazwa = ?',('1A',))
klasa_id = cur.fetchone()[0]

# tupla "uczniowie" zawiera tuple z danymi poszczególnych uczniów
uczniowie = (
    (None,'Tomasz','Nowak',klasa_id),
    (None,'Jan','Kos',klasa_id),
    (None,'Piotr','Kowalski',klasa_id)
)

# wstawiamy wiele rekordów
cur.executemany('INSERT INTO uczen VALUES(?,?,?,?)', uczniowie)

# zatwierdzamy zmiany w bazie
con.commit()

# odczytujemy dane z bazy
def czytajdane():
    cur.execute('SELECT uczen.id,imie,nazwisko,nazwa FROM uczen,klasa WHERE uczen.klasa_id=klasa.id')
    uczniowie = cur.fetchall()
    for uczen in uczniowie:
        print uczen['id'],uczen['imie'],uczen['nazwisko'],uczen['nazwa']
    print ""

czytajdane()

# zmiana klasy ucznia o identyfikatorze 2
cur.execute('SELECT id FROM klasa WHERE nazwa = ?',('1B',))
klasa_id = cur.fetchone()[0]
cur.execute('UPDATE uczen SET klasa_id=? WHERE id=?',(klasa_id,2))

#usunięcie ucznia o identyfikatorze 3
cur.execute('DELETE FROM uczen WHERE id=?',(3,))

czytajdane()

import os

def czytaj_dane(plikcsv):
    """Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv do zapisania w tabeli."""
    dane = [] # deklaracja pustą tabelę
    if os.path.isfile(plikcsv): # czy plik istnieje na dysku
        with open(plikcsv, "r") as zawartosc: # otwieramy plik do odczytu
            for linia in zawartosc:
                linia=linia.replace("\n","") # usuwamy znaki końca linii
                linia=linia.decode("utf-8") # odczytujemy znaki jako utf-8
                # dodajemy elementy do tupli a tuplę do tabeli
                dane.append(tuple(linia.split(",")))
    else:
        print "Plik z danymi",plikcsv,"nie istnieje!"
    
    return tuple(dane) #przekształcamy tabelę na tuplę i zwracamy ją

uczniowie = czytaj_dane('uczniowie.csv')
cur.executemany('INSERT INTO uczen (imie,nazwisko,klasa_id) VALUES(?,?,?)', uczniowie)

czytajdane()

con.close()
