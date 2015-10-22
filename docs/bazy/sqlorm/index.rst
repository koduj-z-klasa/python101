.. _sql-orm:

SQL v. ORM
##################

.. contents::
    :depth: 1
    :local:

Bazy danych są niezbędnym składnikiem większości aplikacji. Poniżej
zwięźle pokażemy, w jaki sposób z wykorzystaniem Pythona można je obsługiwać
przy użyiu języka :term:`SQL`, jak i systemów :term:`ORM` na przykładzie rozwiązania
*Peewee*.

.. note::

    Niniejszy materiał koncentruje się na poglądowym wyeksponowaniu różnic w kodowaniu,
    komentarz ograniczono do minimum. Dokładne wyjaśnienia poszczególnych instrukcji
    znajdziesz w materiale :ref:`SQL <sql_raw>` oraz :ref:`Systemy ORM <systemy_orm>`.
    W tym ostatnim omówiono również ORM SQLAlchemy.

Połączenie z bazą
***********************

Na początku pliku :file:`sqlraw.py` umieszczamy kod, który importuje moduł do obsługi bazy *SQLite3*
i przygotowuje obiekt kursora, który posłuży nam do wydawania poleceń SQL:

.. raw:: html

    <div class="code_no">Plik sqlraw.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: python

    #! /usr/bin/env python
    # -*- coding: utf-8 -*-

    import sqlite3

    con = sqlite3.connect(':memory:')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

System ORM Peewee inicjujemy w pliku :file:`ormpeewee.py` tworząc klasę bazową, która zapewni połączenie z bazą:

.. raw:: html

    <div class="code_no">Plik ormpeewee.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: python

    #! /usr/bin/env python
    # -*- coding: utf-8 -*-

    import os
    from peewee import *

    baza = SqliteDatabase(':memory:')


    class BazaModel(Model):
        class Meta:
            database = baza

.. note::

    Parametr ``:memory:`` powduje utworzenie bazy danych w pamięci operacyjnej,
    która istnieje tylko w czasie wykonywania programu. Aby utworzyć trwałą bazę,
    zastąp omawiany prametr nazwę pliku, np. :file:`test.db`.

Model bazy
***********************

Dane w bazie zorganizowane są w tabelach, połączonych najczęściej relacjami.
Aby utworzyć tabele ``klasa`` i ``uczen`` powiązane relacją jeden-do-wielu,
musimy wydać następujące polecenia SQL:

.. raw:: html

    <div class="code_no">Plik sqlraw.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: python

    cur.executescript("""
    DROP TABLE IF EXISTS klasa;
    CREATE TABLE IF NOT EXISTS klasa (
        id INTEGER PRIMARY KEY ASC,
        nazwa varchar(250) NOT NULL,
        profil varchar(250) DEFAULT ''
    );
    DROP TABLE IF EXISTS uczen;
    CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        klasa_id INTEGER NOT NULL,
        FOREIGN KEY(klasa_id) REFERENCES klasa(id)
    )""")

Wydawanie poleceń SQL-a wymaga koncentracji na poprawności użycia tego języka,
systemy ORM izolują nas od takich szczegółów pozwalając skupić się na logice danych.
Tworzymy więc klasy opisujące nasze tabele: atrybuty tych klas odpowiadają polom tabel,
ich instancje reprezentować będą z kolei rekordy.

.. raw:: html

    <div class="code_no">Plik ormpeewee.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: python

    class Klasa(BazaModel):
        nazwa = CharField(null=False)
        profil = CharField(default='')


    class Uczen(BazaModel):
        imie = CharField(null=False)
        nazwisko = CharField(null=False)
        klasa = ForeignKeyField(Klasa, related_name='uczniowie')

    baza.connect()
    baza.create_tables([Klasa, Uczen], True)

Ćwiczenie 1
============

Utwórz za pomocą tworzonych skryptów bazy w plikach o nazwach :file:`sqlraw.db` oraz
:file:`peewee.db`. Następnie otwórz te bazy w `interpreterze Sqlite <sqlite3>`_  i wykonaj
podane niżej polecenia. Porównaj struktury utworzonych tabel.

.. code-block:: bash

    sqlite> .table
    sqlite> .schema klasa
    sqlite> .schema uczen

Wstawianie danych
***********************

Chcemy wstawić do naszych tabel dane dwóch klas oraz jednego ucznia.
Korzystając z języka SQL użyjemy następujących poleceń:

.. raw:: html

    <div class="code_no">Plik sqlraw.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1A', 'matematyczny'))
    cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1B', 'humanistyczny'))
    cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1A',))
    klasa_id = cur.fetchone()[0]
    cur.execute('INSERT INTO uczen VALUES(?,?,?,?)', (None, 'Tomasz', 'Nowak', klasa_id))
    con.commit()

W systemie ORM pracujemy z obiektami ``klasa`` i ``uczen``. Nadajemy wartości ich
atrybutom i korzystamy z ich metody:

.. raw:: html

    <div class="code_no">Plik ormpeewee.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: python

    if Klasa.select().count() == 0:
        klasa = Klasa(nazwa='1A', profil='matematyczny')
        klasa.save()
        klasa = Klasa(nazwa='1B', profil='humanistyczny')
        klasa.save()

    klasa = Klasa.select().where(Klasa.nazwa == '1A').get()
    uczen = Uczen(imie='Tomasz', nazwisko='Nowak', klasa=klasa)
    uczen.save()

Pobieranie danych
***********************

Pobieranie danych (czyli :term:`kwerenda`) wymaga polecenia *SELECT* języka SQL.
Aby wyświetlić dane wszystkich uczniów zapisane w bazie użyjemy kodu:

.. raw:: html

    <div class="code_no">Plik sqlraw.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    cur.execute('SELECT uczen.id,imie,nazwisko,nazwa FROM uczen,klasa WHERE uczen.klasa_id=klasa.id')
    uczniowie = cur.fetchall()
    for uczen in uczniowie:
        print uczen['id'], uczen['imie'], uczen['nazwisko'], uczen['nazwa']
    print ""

W systemie ORM korzystamy z metody ``select()`` obiektu reprezentującego ucznia.
Dostęp do danych przechowywanych w innych tabelach uzyskujemy dzięki wyrażeniom
typu ``uczen.klasa.nazwa``, które generuje podzazpytanie zwracające nazwę
klasy przypisanej uczniowi.

.. raw:: html

    <div class="code_no">Plik ormpeewee.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: python

    for uczen in Uczen.select():
        print uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa
    print ""

.. tip::

    Ze względów wydajnościowych pobieranie danych z innych tabel możemy
    zasygnalizować już w głównej kwerendzie, używając metody ``join()``,
    np.: ``Uczen.select().join(Klasa)``.

Modyfikacja danych
*****************************

Edycja danych zapisanych już w bazie to kolejna częsta operacja. Jeżeli Chcemy
przepisać ucznia z klasy do klasy, musimy użyć następujących poleceń SQL:

.. raw:: html

    <div class="code_no">Plik sqlraw.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    cur.execute('SELECT id FROM uczen WHERE nazwisko="Nowak"')
    uczen_id = cur.fetchone()[0]
    cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1B',))
    klasa_id = cur.fetchone()[0]
    cur.execute('UPDATE uczen SET klasa_id=? WHERE id=?', (klasa_id, uczen_id))

W systemie ORM manipulujemy atrybutami obiektu reprezentującego ucznia:

.. raw:: html

    <div class="code_no">Plik ormpeewee.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: python

    uczen = Uczen.select().join(Klasa).where(Uczen.nazwisko == 'Nowak').get()
    uczen.klasa = Klasa.select().where(Klasa.nazwa == '1B').get()
    uczen.save()  # zapisanie zmian w bazie

Usuwanie danych
*****************************

Język SQL wymaga wskazania usuwanego rekordu w klauzuli ``WHERE``. Aby usunąć ucznia
o identyfikatorze ``1``, użyjemy instrukcji:

.. raw:: html

    <div class="code_no">Plik sqlraw.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    cur.execute('DELETE FROM uczen WHERE id=?', (1,))


Usuwając dane w przypadku systemu ORM, usuwamy instancję wskazanego obiektu:

.. raw:: html

    <div class="code_no">Plik ormpeewee.py. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: python

    Uczen.select().where(Uczen.id == 1).get().delete_instance()

.. note::

    Po wykonaniu wszystkich założonychoperacji na danych połączenie z bazą należy
    zamknąć, zwalniając w ten sposób zarezerwowane zasoby. W przypadku modułu ``sqlite3``
    wywołujemy polecenie ``con.close()``, w Peewee ``baza.close()``.

Podsumowanie
***********************

Bazę danych można obsługiwać za pomocą języka SQL na niskim poziomie. Zyskujemy wtedy na szybkości
działania, ale tracimy przejrzystość kodu, łatwość jego przeglądania i rozwijania.
O ile w prostych zastosowaniach można to zaakceptować, o tyle w bardziej rozbudowanych
projektach używa się systemów ORM, które pozwalają zarządzać danymi nie w formie tabel, pól i rekordów,
ale w formie obiektów reprezentujących logicznie spójne dane. Takie podejście
lepiej odpowiada obiektowemu wzorcowi projektowania aplikacji.

Dodatkową zaletą systemów ORM, nie do przecenienia, jest większa odporność na błędy i ewentualne
ataki na dane w bazie.

Systemy ORM można łatwo integrować z programami desktopowymi i frameworkami przeznaczonymi do tworzenia
aplikacji sieciowych. Wśród tych ostatnich znajdziemy również takie, w których system ORM jest
podstawowym składnikiem, np. *Django*.

Zadania dodatkowe
*******************

- Wykonajscenariusz aplikacji :ref:`Quiz ORM <quiz-orm>`, aby zobaczyć przykład wykorzystania systemów ORM
  w aplikacjach internetowych.

- Przejrzyj scenariusz aplikacji internetowej :ref:`Czat <czat-app>`, zbudowanej z wykorzystaniem
  frameworku *Django*, korzystającego z własnego modelu ORM.

Źródła
*******************

* :download:`sqlorm.zip <sqlorm.zip>`

Pełne wersje tworzenych skryptów znajdziesz w katalogu ``~/python101/docs/bazy/sqlorm``.
Uruchamiamy je wydając polecenia:

.. code-block:: bash

    ~/python101$ cd docs/bazy/sqlorm
    ~/python101/docs/bazy/sqlorm$ python sqlraw.py
    ~/python101/docs/bazy/sqlorm$ python sqlorm.py
