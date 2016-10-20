.. _linux-env:

Przygotowanie systemu Linux
###########################

Jeżeli nie masz zainstalowanego systemu Linux, możesz wykorzystać wersję
:ref:`Linux Live <linux-live>`, która po nagraniu na pendrajwa pozwoli uruchomić komputer.
Jeżeli masz Linuksa lub planujesz go zainstalować na dysku, czytaj dalej.

.. _linux-distro:

Dystrybucje
===========

Najwygodniej pracować w systemie Linux zainstalowanym na stałe, np. obok MS Windows.
Polecamy systemy, na których przetestowaliśmy scenariusze:

* `Linux Mint 18 <https://www.linuxmint.com/download.php>`_  z dowolnym środowiskiem graficznym.

* `Debian Jessie 8 <https://www.debian.org/index.pl.html>`_  – ostatnia stabilna wersja,
   proponujemy wersję ze środowiskiem `XFCE`_. Zob.: `Instalacja Debiana Jessie <http://ecg.vot.pl/?id=debian-stable-install>`_.

* `Xubuntu <https://xubuntu.org/getxubuntu/>`_ 16.04 LTS – stabilna odmiana
  `Ubuntu <https://www.ubuntu.com/>`_, zawiera proste i wydajne
  :term:`środowisko graficzne` `XFCE`_.
  Zob. `Instalacja Lubuntu <http://ecg.vot.pl/?id=lubuntu>`_ (instalacja jest taka sama).

Instalacja powyższych systemów jest prosta, pomocne informacje można znaleźć
np. na stronie `Zainstalu Linuksa <http://ecg.vot.pl/?id=linux-instalacja>`_

.. _linux-pakiety:

Narzędzia i biblioteki
======================

W systemach linuksowych Python 2.7.x zainstalowany jest domyślnie,
wersja 3.x również. Potrzebne narzędzia/biblioteki instalujemy przy użyciu systemowego
menedżera pakietów (np. ``apt-get`` czy ``pacman``) i/lub instalatora pakietów Pythona ``pip``.

**Wymagane:**

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

**Dodatkowe:**

* `ipython <http://ipython.org/>`_ – rozszerzona interaktywna konsola Pythona;
* `qtconsole <http://jupyter.org/qtconsole/stable/>`_  – rozszerzona interaktywna konsola
  Pythona wykorzystująca bibliotekę Qt, umożliwia m. in. wyświetlanie wykresów utworzonych
  z wykorzystaniem *matplotlib*.

**Instalacja**

W systemach opartych na *Debianie* (*LinuxMint, (X)Ubuntu* itp.) w terminalu wydajemy następujące polecenia:

.. code-block:: bash

    ~$ sudo apt-get update
    ~$ sudo apt-get install python-pip python-pygame python-tk python-matplotlib git sqlite3
    ~$ sudo apt-get install ipython ipython-qtconsole
    ~$ sudo pip install virtualenv flask django peewee sqlalchemy flask-sqlalchemy

W systemach opartych na *Arch Linuksie* (*Manjaro* itp.) w terminalu wydajemy następujące polecenia:

.. code-block:: bash

    ~# pacman -Syyu
    ~# pacman -S python2-pip python2-pygame tk python2-matplotlib git sqlite
    ~# pacman -S ipython2-notebook python2-pyqt5
    ~# pip2 install virtualenv flask django peewee sqlalchemy flask-sqlalchemy

.. note::

    Ewentualna aktualizacja biblioteki *matplotlib* oraz narzędzi *ipython* i *qtconsole*
    w systemach opartych na Debianie wymaga doinstalowania środowiska
    umożliwijącego kompilację:

.. code-block:: bash

    ~$ sudo apt-get install build-essential libpng12-dev zlib1g-dev libfreetype6-dev python-dev
    ~$ sudo pip install matplotlib ipython qtconsole

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

Pip
-------

Przydatne polecenia:

.. code-block:: bash

    ~$ pip -V  # wersja narzędzia pip
    ~$ pip list  # lista zainstalowanych pakietów
    ~$ sudo pip install nazwa_pakietu  # instalacja pakietu
    ~$ sudo pip install nazwa_pakietu -U  # aktualizacja pakietu
    ~$ sudo pip uninstall  # usunięcie pakietu

.. _XFCE: http://www.xfce.org/