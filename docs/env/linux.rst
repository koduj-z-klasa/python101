.. _linux-env:

Przygotowanie systemu Linux
###########################

Jeżeli nie masz zainstalowanego systemu Linux, możesz wykorzystać wersję
:ref:`Linux Live <linux-live>`, która po nagraniu na pendrajwa pozwoli uruchomić komputer.
Jeżeli masz Linuksa lub planujesz go zainstalować na dysku, czytaj dalej.

W systemach linuksowych Python 2.7.x zainstalowany jest domyślnie,
wersja 3.x również. Potrzebne narzędzia/biblioteki instalujemy przy użyciu systemowego
menedżera pakietów i/lub instalatora pakietów Pythona ``pip``.

Narzędzia wymagane:

* `pip <https://pip.pypa.io/en/stable/>`_  – instalator pakietów Pythona, podstawowe narzędzie
  służące do zarządzania pakietami Pythona zgromadzonymi np.
  w repozytorium `PyPI <https://pypi.python.org/pypi>`_  (Python Package Index);
* `virtualenv <https://virtualenv.readthedocs.org/en/latest/>`_  – menedżer wirtualnych środowisk Pythona,
  pozwala tworzyć katalogi zawierające izolowane środowisko Pythona umożliwiające instalowanie
  wybranych wersji pakietów przez zwykłych użytkowników;
* `klient git <https://git-scm.com/downloads>`_  – narzędzie umożliwiające korzystanie z repozytoriów
  kodu i dokumentacji w serwisie `Github <https://github.com/>`_
* `sqlite3 <https://www.sqlite.org/>`_ – konsolowa powłoka dla baz SQLite3, umożliwia przeglądanie
  schematów tabel oraz zarządzanie bazą za pomocą języka SQL.

Narzędzia dodatkowe:

* `ipython <http://ipython.org/>`_ – rozszerzona interaktywna konsola Pythona;
* `qtconsole <http://jupyter.org/qtconsole/stable/>`_  – rozszerzona interaktywna konsola
  Pythona wykorzystująca bibliotekę Qt, umożliwia m. in. wyświetlanie wykresów utworzonych
  z wykorzystaniem *matplotlib*.

.. contents:: Spis treści
    :backlinks: none

.. note::

    * Nazwy pakietów w różnych dystrybucjach mogą się nieco różnić od podanych.
    * Systemy *Debian* i *Arch Linux* w domyślnej konfiguracji nie wykorzystują
      mechanizmu podnoszenia uprawnień ``sudo``, dlatego polecenia instalacji
      należy wydawać z konta użytkownika root, co oznaczamy znakami ``~#``.
    * W systemach opartych na *Debianie* (*(X)Ubuntu, LinuxMint* itp.) polecenie ``python``
      domyślnie wywołuje Pythona 2, w systemach opartych na *Arch Linuksie* – Pythona 3.
      Aby użyć interpretera Pythona 2, w *Archu* itp. trzeba wydać polecenie ``python2``.

Narzędzia i biblioteki
-----------------------

W systemach opartych na *Debianie* (*(X)Ubuntu, LinuxMint* itp.)
w terminalu wydajemy następujące polecenia:

.. code-block:: bash

    ~$ sudo apt-get update
    ~$ sudo apt-get install python-pip python-pygame python-matplotlib git sqlite3
    ~$ sudo apt-get install ipython ipython-qtconsole
    ~$ sudo pip install virtualenv flask django peewee sqlalchemy flask-sqlalchemy

W systemach opartych na *Arch Linuksie* (*Manjaro* itp.)
w terminalu wydajemy następujące polecenia:

.. code-block:: bash

    ~# pacman -Syyu
    ~# pacman -S python2-pip python2-pygame python2-matplotlib git sqlite
    ~# pacman -S ipython2-notebook python2-pyqt5
    ~# pip2 install virtualenv flask django peewee sqlalchemy flask-sqlalchemy

Pip
-------

Przydatne polecenia:

.. code-block:: bash

    ~$ pip -V  # wersja narzędzia pip
    ~$ pip list  # lista zainstalowanych pakietów
    ~$ sudo pip install nazwa_pakietu  # instalacja pakietu
    ~$ sudo pip install nazwa_pakietu -U  # aktualizacja pakietu
    ~$ sudo pip uninstall  # usunięcie pakietu

.. note::

    Aktualizacja biblioteki *matplotlib* oraz narzędzi *ipython* i *qtconsole*
    w systemach opartych na Debianie wymaga doinstalowania środowiska
    umożliwijącego kompilację:

.. code-block:: bash

    ~$ sudo apt-get install build-essential libpng12-dev zlib1g-dev libfreetype6-dev python-dev
    ~$ sudo pip install matplotlib ipython qtconsole
