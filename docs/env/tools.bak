Narzędzia
#########

Podczas realizacji scenariuszy wykorzystujących Pythona będziemy korzystać z
następujących narzędzi:

* `pip <https://pip.pypa.io/en/stable/>`_  – instalator pakietów Pythona,
  podstawowe narzędzie służące do zarządzania pakietami Pythona zgromadzonymi
  w repozytorium `PyPI <https://pypi.python.org/pypi>`_  (Python Package Index);
* `virtualenv <https://virtualenv.readthedocs.org/en/latest/>`_  –
  menedżer wirtualnych środowisk Pythona, pozwala tworzyć katalogi zawierające
  izolowane wersje Pythona umożliwiające instalowanie wybranych wersji pakietów
  przez zwykłych użytkowników;
* `git <https://git-scm.com/downloads>`_  – konsolowy klient systemu wersjonowania kodu
  umożliwiający korzystanie z repozytoriów w serwisie `Github <https://github.com/>`_;
* `sqlite3 <https://www.sqlite.org/>`_ – konsolowa powłoka dla baz SQLite3,
  umożliwia przeglądanie schematów tabel oraz zarządzanie bazą za pomocą języka SQL;
* `ipython <http://ipython.org/>`_ i `qtconsole <http://jupyter.org/qtconsole/stable/>`_
  – rozszerzone interaktywne konsole Pythona.

.. _pve:

Środowisko wirtualne
====================

Aplikacje pisane w Pythonie przy użyciu rozbudowanych frameworków takich jak np.
Flask czy Django rozwija się najczęściej w środowisku wirtualnym (ang. *pve* – *Python
virtual environment*). Pozwala to na instalację przez zwykłego użytkownika tych samych
bibliotek w różnych wersjach wymaganych przez dany projekt.
Inne zalety to: łatwiejsze testowanie i niezaśmiecanie instalacji globalnej.

Praktycznie rzecz biorąc *pve* to po prostu katalog, do którego wgrywana jest wymagana
wersja interpretera i narzędzia *pip*, za pomocą którego instalujemy potrzebne moduły.

Wirtualne środowisko można utworzyć w dowolnym katalogu za pomocą narzędzia **virtualenv**.
Wystarczy polecenie w terminalu:

.. code-block:: bash

    ~$ virtualenv katalog

Uwaga: domyślnie zostanie użyta wersja Pythona, dla której zainstalowano *virtualenv*.
Możemy jednak wskazać wersję interpretera:

.. code-block:: bash

    ~$ virtualenv -p python3.5 katalog

Począwszy od wersji 3.3 do tworzenia wirtualnych środowisk Pythona 3 możemy
używać modułu *venv*:

.. code-block:: bash

    ~$ python3 -m venv katalog

**Aktywacja środowiska** – po utworzeniu wirtualnego środowiska trzeba je aktywować:

.. code-block:: bash

    ~$ source katalog/bin/activate
    (katalog) ~$ python skrypt.py

– drugie polecenie pokazuje, jak uruchamiać skrypty w utworzonym środowisku.

W systemie **Windows** skrypt aktywujący uruchamiamy poleceniem:

.. code-block:: bash

    > katalog\\Scripts\\activate.bat

**Deaktywacja środowiska** – sprowadza się do polecenia:

.. code-block:: bash

    (katalog) ~$ deactivate

Pip
===

Używając instalatora pakietów w środowisku wirtualnym nie potrzebujemy
uprawnień administratora wymaganych do instalacji systemowej (globalnej).
Przydatne polecenia:

.. code-block:: bash

    (katalog) ~$ pip install biblioteka==1.4  # instalacja biblioteki we wskazanej wersji
    (katalog) ~$ pip -V  # wersja narzędzia pip
    (katalog) ~$ pip list  # lista zainstalowanych pakietów
    (katalog) ~$ pip install nazwa_pakietu  # instalacja pakietu
    (katalog) ~$ pip install nazwa_pakietu -U  # aktualizacja pakietu
    (katalog) ~$ pip uninstall  # usunięcie pakietu