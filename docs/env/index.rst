System i oprogramowanie
#######################

Nasze materiały zakładają wykorzystanie języka :term:`Python` w większości w wersji 3.x,
w dwóch przypadkach (:ref:`Gra robotów <robot-game>` i częściowo :ref:`Minecraft Pi <mcpi-app>`)
wymagana jest wersja 2.x.
Mogą być realizowane w dowolnym systemie operacyjnym, jednak proponujemy systemy Linux,
w których Python 3.x i często 2.x są obecne domyślnie i nie ma problemów z instalacją
dodatkowych narzędzi i bibliotek.

Do realizacji materiałów można również wykorzystać system :ref:`Linux Live <linux-live>`
przeznaczony do instalacji na pendrajwach. Uruchamia się z napędu USB na większości komputerów
i ma możliwość zapamiętywania zmian i naszej pracy.

.. _tools:

Podczas realizacji scenariuszy wykorzystujących Pythona będziemy korzystać z
różnych narzędzi:

* `pip <https://pip.pypa.io/en/stable/>`_  – instalator pakietów Pythona,
  podstawowe narzędzie służące do zarządzania pakietami Pythona zgromadzonymi
  w repozytorium `PyPI <https://pypi.python.org/pypi>`_  (Python Package Index);
* `git <https://git-scm.com/downloads>`_  – konsolowy klient systemu wersjonowania kodu
  umożliwiający korzystanie z repozytoriów w serwisie `Github <https://github.com/>`_;
* `sqlite3 <https://www.sqlite.org/>`_ – konsolowa powłoka dla baz SQLite3,
  umożliwia przeglądanie schematów tabel oraz zarządzanie bazą za pomocą języka SQL;
* `ipython <http://ipython.org/>`_ i `qtconsole <http://jupyter.org/qtconsole/stable/>`_
  – rozszerzone interaktywne konsole Pythona.

Na kolejnych stronach wyjaśniamy, jak je zainstalować i wykorzystywać w systemie operacyjnym.

..  toctree::
    :maxdepth: 2

    linux
    live
    windows
    interpreter
    Edytory kodu <https://linetc.readthedocs.io/pl/latest/tools/edytory/index.html>
