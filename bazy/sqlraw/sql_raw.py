import sqlite3

# utworzenie połączenia z bazą przechowywaną w pamięci RAM
con = sqlite3.connect('baza.db')
# dostęp do pól rekordów przez indeksy i przez nazwy pól
con.row_factory = sqlite3.Row
# utworzenie obiektu kursora
cur = con.cursor()

# tworzenie tabel
cur.execute("DROP TABLE IF EXISTS klasa")
cur.execute("DROP TABLE IF EXISTS uczen")
cur.executescript("""
    CREATE TABLE IF NOT EXISTS klasa (
        id INTEGER PRIMARY KEY,
        nazwa varchar(250) NOT NULL,
        profil varchar(250) DEFAULT ''
    );
    CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        klasa_id INTEGER NOT NULL,
        FOREIGN KEY(klasa_id) REFERENCES klasa(id)
    )""")

# dodajemy dwie klasy
cur.execute('INSERT INTO klasa VALUES(NULL,?,?)', ('1A', 'matematyczny'))
klasa1_id = cur.lastrowid
cur.execute('INSERT INTO klasa VALUES(NULL,?,?)', ('1B', 'humanistyczny'))
klasa2_id = cur.lastrowid

# lista uczniów, których dane zapisane są w krotkach
uczniowie = [
    ('Tomasz', 'Nowak', klasa1_id),
    ('Jan', 'Kos', klasa2_id),
    ('Piotr', 'Kowalski', klasa2_id)
]
# dodajemy dane wielu uczniów
cur.executemany('INSERT INTO uczen VALUES(NULL,?,?,?)', uczniowie)
con.commit()

def wypisz_listę_uczniow():
    """ Odczytujemy i wypisujemy dane uczniów, w tym klasę """
    cur.execute("SELECT count(*) FROM uczen")
    if (cur.fetchone()[0]):
        print('Uczniowie:')
        cur.execute(
            """
            SELECT uczen.id, imie, nazwisko, nazwa FROM uczen
            INNER JOIN klasa
            WHERE uczen.klasa_id=klasa.id
            """)
        uczniowie = cur.fetchall()
        for uczen in uczniowie:
            print(uczen['id'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'])
        print()

wypisz_listę_uczniow()

# przepisanie wybranego ucznia do innej klasy
cur.execute('SELECT id FROM uczen WHERE nazwisko=?', ('Nowak',))
uczen_id = cur.fetchone()[0]
cur.execute('SELECT id FROM klasa WHERE nazwa=?', ('1B',))
klasa_id = cur.fetchone()[0]
cur.execute('UPDATE uczen SET klasa_id=? WHERE id=?', (klasa_id, uczen_id))
wypisz_listę_uczniow()

# usunięcie ucznia o podanym imieniu i nazwisku
cur.execute('DELETE FROM uczen WHERE imie=? and nazwisko=?', ('Jan', 'Kos'))
wypisz_listę_uczniow()

con.close()
