Słownik baz danych
###################

.. glossary::

    SQL
        strukturalny język zapytań używany do tworzenia i zarządzania bazą danych.

    SQLite3
        silnik bezserwerowej, nie wymagającej dodatkowej konfiguracji, transakcyjnej bazy danych
        implementującej standard SQL.

    CRUD
        skrót opisujący podstawowe operacje na bazie danych z wykorzystaniem języka SQL,
        *Create* (tworzenie) odpowiada zapytaniom *INSERT*, *Read* (odczyt) - zapytaniom
        *SELECT*, *Update* (aktualizacja) - *UPDATE*, *Delete* (usuwanie) - *DELETE*.

    Transakcja
        zbiór powiązanych logicznie operacji na bazie danych, który powinien być
        albo w całości zapisany, albo odrzucony ze względu na naruszenie zasad
        spójności (ACID).

    ACID
        Atomicity, Consistency, Isolation, Durability – Atomowość, Spójność, Izolacja, Trwałość;
        zasady określające kryteria poprawnego zapisu danych w bazie. `Więcej o ACID »»» <http://pl.wikipedia.org/wiki/ACID>`_

    kwerenda
        Zapytanie do bazy danych zazwyczaj w oparciu o dodatkowe kryteria,
        którego celem jest wydobycie z bazy określonych danych lub ich modyfikacja.

    obiekt
        podstawowe pojęcie programowania obiektowego, struktura zawierająca
        dane i metody (funkcje), za pomocą których wykonuje ṣię na nich operacje.

    klasa
        definicja obiektu zawierająca opis struktury danych i jej interfejs
        (metody).

    instancja
        obiekt stworzony na podstawie klasy.

    konstruktor
        metoda wywoływana podczas tworzenia instancji (obiektu) klasy, zazwyczaj
        przyjmuje jako argumenty inicjalne wartości zdefiniowanych w klasie atrybutów.

    ORM
        (ang. Object-Relational Mapping) – mapowanie obiektowo-relacyjne, oprogramowanie
        odwzorowujące strukturę relacyjnej bazy danych na obiekty danego języka oprogramowania.

    Peewee
        prosty i mały system ORM, wspiera Pythona w wersji 2 i 3, obsługuje
        bazy SQLite3, MySQL, Posgresql.

    SQLAlchemy
        rozbudowany zestaw narzędzi i system ORM umożliwiający wykorzystanie
        wszystkich możliwości SQL-a, obsługuje bazy SQLite3, MySQL, Postgresql,
        Oracle, MS SQL Server i inne.
