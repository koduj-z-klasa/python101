.. _webapps:

Aplikacje internetowe
#######################

`Python <https://www.python.org/>`_ znakomicie nadaje się do tworzenia aplikacji internetowych
dzięki takim rozszerzeniom jak micro-framework `Flask <http://flask.pocoo.org/>`_ czy bardziej
rozbudowany framework `Django <https://www.djangoproject.com/>`_. Obydwa rozwiązania
upraszczają projektowanie oferując gotowe rozwiązania wielu pracochłonnych
mechanizmów wymaganych w serwisach internetowych. Co więcej, w obydwu przypadkach,
dostajemy do dyspozycji gotowe środowisko testowe, czyli deweloperski serwer WWW,
nie musimy instalować żadnych dodatkowych narzędzi typu LAMP (WAMP).

.. note::

    Poniższe projekty uporządkowano pod względem złożoności, najlepiej realizować je
    według zaproponowanej kolejności. Na początku pokazujemy we Flasku (Quiz) mechanizm
    obsługi żądań klient – serwer typu GET i POST oraz wykorzystanie *widoków* i *szablonów*.
    Później dodajemy obsługę bazy danych za pomocą SQL-a (ToDo) i bazy SQLite oraz
    wprowadzamy do obsługi baz danych z wykorzystaniem systemów ORM Peewee i SQLAlchemy
    (Quiz ORM), na końcu zbieramy wszystko w scenariuszu omawiającym rozbudowany,
    co nie znaczy trudny, system Django wykorzystujący wszystkie powyższe mechanizmy.

.. toctree::
    :maxdepth: 2

    quiz/index
    todo/index
    quiz_orm/index
    czat/index
    mvc
    glossary

Materiały
***************

#. `Python`_
#. `Flask`_
#. `Django`_
#. `SQLite`_
#. `Peewee`_
#. `SQLAlchemy`_

.. _Python: https://www.python.org/
.. _Flask: http://flask.pocoo.org/
.. _Django: https://www.djangoproject.com/
.. _SQLite: http://www.sqlite.org
.. _Peewee: http://peewee.readthedocs.org/en/latest
.. _SQLAlchemy: http://www.sqlalchemy.org

