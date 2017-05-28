#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

# utworzenie połączenia z bazą przechowywaną w pamięci RAM
con = sqlite3.connect(':memory:')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()

# tworzenie tabel
cur.executescript("""
    DROP TABLE IF EXISTS grupa;
    CREATE TABLE IF NOT EXISTS grupa (
        id INTEGER PRIMARY KEY ASC,
        nazwa varchar(250) NOT NULL,
        profil varchar(250) DEFAULT ''
    );
    DROP TABLE IF EXISTS uczen;
    CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        grupa_id INTEGER NOT NULL,
        FOREIGN KEY(grupa_id) REFERENCES grupa(id)
    )""")

# wstawiamy dane uczniów
cur.execute('INSERT INTO grupa VALUES(NULL, ?, ?);', ('1A', 'matematyczny'))
cur.execute('INSERT INTO grupa VALUES(NULL, ?, ?);', ('1B', 'humanistyczny'))

# wykonujemy zapytanie SQL, które pobierze id grupy "1A" z tabeli "grupa".
cur.execute('SELECT id FROM grupa WHERE nazwa = ?', ('1A',))
grupa_id = cur.fetchone()[0]

# wstawiamy dane uczniów
cur.execute('INSERT INTO uczen VALUES(?,?,?,?)',
            (None, 'Tomasz', 'Nowak', grupa_id))
cur.execute('INSERT INTO uczen VALUES(?,?,?,?)',
            (None, 'Adam', 'Kowalski', grupa_id))

# zatwierdzamy zmiany w bazie
con.commit()


def czytajdane():
    """Funkcja pobiera i wyświetla dane z bazy"""
    cur.execute(
        """
        SELECT uczen.id,imie,nazwisko,nazwa FROM uczen,grupa
        WHERE uczen.grupa_id=grupa.id
        """)
    uczniowie = cur.fetchall()
    for uczen in uczniowie:
        print(uczen['id'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'])
    print()


czytajdane()

# przepisanie ucznia do innej grupy
cur.execute('SELECT id FROM uczen WHERE nazwisko="Nowak"')
uczen_id = cur.fetchone()[0]
cur.execute('SELECT id FROM grupa WHERE nazwa = ?', ('1B',))
grupa_id = cur.fetchone()[0]
cur.execute('UPDATE uczen SET grupa_id=? WHERE id=?', (grupa_id, uczen_id))
czytajdane()

# usunięcie ucznia o identyfikatorze 1
cur.execute('DELETE FROM uczen WHERE id=?', (1,))
czytajdane()

con.close()
