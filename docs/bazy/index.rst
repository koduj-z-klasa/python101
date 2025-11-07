.. _bazy-python:

Bazy danych w Pythonie
#######################

W poniższych scenariuszach pokazujemy jak tworzyć i zarządzać bazą danych za pomocą Pythona.
Omawiamy następujące możliwości:

- `Sqlite3 DB-API <https://docs.python.org/2/library/sqlite3.html>`_ – wbudowany moduł Pythona do zarządzania
  bazami SQLite, który wymaga znajomości języka SQL;
- `Peewee <http://peewee.readthedocs.org/en/latest/index.html>`_ – prosty, mały system ORM;
- `SQLAlchemy <http://www.sqlalchemy.org>`_ – rozbudowany system ORM, oferujący zestaw narzędzi
   ułatwiających wykorzystanie możliwości języka SQL.

Znajomość języka SQL jest zalecana, aby rozumieć i korzystać z wszystkich możliwości baz danych.
Systemy ORM (ang. *Object-Relational Mapping* – mapowanie obiektowo-relacyjne) pozwalają jednak traktować
tabele i relacje w sposób obiektowy, co bywa wygodniejsze, kiedy obsługujemy bazę danych za pomocą
obiektowego języka programowania, jakim jest Python.

Poniższe przykłady wykorzystywać będą prostą, wydajną, stosowaną zarówno w prostych,
jak i zaawansowanych projektach, `bazę danych SQLite3 <http://www.sqlite.org/>`_.
Gdy zajdzie potrzeba, można je jednak wykorzystać w pracy z innymi bazami,
takimi jak np. MySQL, MariaDB czy PostgresSQL.

Do testowania baz danych SQLite można wykorzystać przygotowane przez jej twórców
konsolowe narzędzie `sqlite3 <http://www.sqlite.org/cli.html>`_
(zob.: :ref:`instalacja klienta SQLite3 <sqlite3-install>`) lub narzędzia z interfejsem graficznym,
np. polski program `SQLiteStudio <https://sqlitestudio.pl/>`_.

.. toctree::
    :maxdepth: 2

    sql/index
    orm_pw/index
    sqlorm/index
    sql/dane
    sqlite3

Materiały
***************

1. `Moduł sqlite3 Pythona`_
2. `Baza SQLite3`_
3. `Język SQL`_
4. `Peewee (ang.)`_
5. `Tutorial Peewee (ang.)`_
6. `SQLAlchemy ORM Tutorial (ang.)`_
7. `Tutorial SQLAlchemy (ang.)`_

.. _Moduł sqlite3 Pythona: https://docs.python.org/2/library/sqlite3.html
.. _Baza SQLite3: http://www.sqlite.org/
.. _Język SQL: http://pl.wikipedia.org/wiki/SQL
.. _Peewee (ang.): http://peewee.readthedocs.org/en/latest/index.html
.. _Tutorial Peewee (ang.): http://www.blog.pythonlibrary.org/2014/07/17/an-intro-to-peewee-another-python-orm/
.. _SQLAlchemy ORM Tutorial (ang.): http://www.sqlalchemy.org/
.. _Tutorial SQLAlchemy (ang.): http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/
