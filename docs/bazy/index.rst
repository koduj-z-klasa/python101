Bazy danych w Pythonie
#######################

Tworzenie i zarządzanie bazami danymi za pomocą Pythona z wykorzystaniem
wbudowanego modułu `sqlite3 DB-API`_, a także zewnętrznych bibliotek ORM:
`Peewee`_ oraz `SQLAlchemy`_

.. _sqlite3 DB-API: https://docs.python.org/2/library/sqlite3.html
.. _Peewee: http://peewee.readthedocs.org/en/latest/index.html
.. _SQLAlchemy: http://www.sqlalchemy.org

.. note::

    Poniższe przykłady wykorzystywać będą prostą, wydajną, stosowaną
    zarówno w prostych, jak i zaawansowanych projektach, `bazę danych SQLite3`_.
    Gdy zajdzie potrzeba, można je jednak wyorzystać w pracy z innymi
    bazami, takimi jak np. MySQL, MariaDB czy PostgresSQL.
    Do testowania baz danych SQLite można wykorzystać przygotowane przez
    jej twórców konsolowe narzędzie `sqlite3`_. W linuksach opartych na Debianie
    (m. in. Ubuntu i pochodne) instalujemy je poleceniem typu:
    ``apt-get install sqlite3``; w systemach Windows natomiast rozpakowujemy
    z pobranego `archiwum`_.

.. _bazę danych SQLite3: http://www.sqlite.org/
.. _sqlite3: http://www.sqlite.org/cli.html
.. _archiwum: http://www.sqlite.org/download.html

.. toctree::
    :maxdepth: 2

    sql/index
    orm/index
    sqlorm/index
    sql/dane
    sqlite3
    glossary

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
