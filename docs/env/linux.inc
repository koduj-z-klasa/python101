.. _linux-env:

Przygotowanie systemu Linux
***************************

Jeżeli nie masz zainstalowanego systemu Linux, możesz wykorzystać wersję
:ref:`Linux Live <linux-live>`, która po nagraniu na pendrajwa pozwoli
uruchomić komputer. Jeżeli masz Linuksa lub planujesz go zainstalować
na dysku, czytaj dalej.

.. _linux-distro:

Dystrybucje
===========

Najwygodniej pracować w systemie Linux zainstalowanym na dysku twardym,
np. obok MS Windows. Polecamy systemy, na których przetestowaliśmy scenariusze:

* `Linux Mint 18 <https://www.linuxmint.com/download.php>`_
* `Debian Jessie 8 <https://www.debian.org/index.pl.html>`_
* `Ubuntu 16.04 LTS <https://www.ubuntu.com/>`__ lub jego odmiany np.
  `Xbuntu <https://xubuntu.org/getxubuntu/>`__.

Środowisko graficzne (zob. :term:`środowisko graficzne`) dowolne, chociaż
osobom przyzwyczajonym do tradycyjnego pulpitu proponujemy proste i wydajne
`XFCE`_.

Wskazówki dotyczące instalacji:

* `Windows i Linux na jednym dysku <https://www.dobreprogramy.pl/Windows-i-Linux-Mint-na-jednym-dysku-poradnik-dla-poczatkujacych,News,81165.html>`_;
* `Zainstaluj Linuksa <http://ecg.vot.pl/?id=linux-instalacja>`_;
* `Instalacja Ubuntu <http://ecg.vot.pl/?id=lubuntu>`_;
* `Instalacja Debiana Jessie <http://ecg.vot.pl/?id=debian-stable-install>`_.


.. _linux-pakiety:

Narzędzia i biblioteki
======================

W systemach linuksowych Python 3.x zainstalowany jest domyślnie. Potrzebne
narzędzia i biblioteki instalujemy przy użyciu systemowego menedżera pakietów
(np. ``apt`` czy ``pacman``) i/lub instalatora pakietów Pythona ``pip``.

**Instalacja**

W systemach opartych na *Debianie* (*LinuxMint, (X)Ubuntu* itp.) w terminalu wydajemy
następujące polecenia:

.. code-block:: bash

    ~$ sudo apt update
    ~$ sudo apt install ipython ipython-qtconsole git sqlite3
    ~$ sudo apt install python3-pip python3-sip python3-pyqt5
    ~$ sudo pip3 install virtualenv
    ~$ sudo pip3 install matplotlib
    ~$ sudo pip3 install pygame
    ~$ sudo pip3 install flask django peewee sqlalchemy flask-sqlalchemy

W systemach opartych na *Arch Linuksie* (*Manjaro*, *Antergos* itp.)
w terminalu wydajemy następujące polecenia:

.. code-block:: bash

    ~# pacman -Syyu
    ~# pacman -S ipython-qtconsole git sqlite
    ~# pacman -S python-pip python-pyqt5
    ~# pip install virtualenv
    ~# pip install matplotlib
    ~# pip install pygame
    ~# pip install flask django peewee sqlalchemy flask-sqlalchemy

.. note::

    * Nazwy pakietów w różnych dystrybucjach mogą się nieco różnić od podanych.
    * Systemy *Debian* i *Arch Linux* w domyślnej konfiguracji nie wykorzystują
      mechanizmu podnoszenia uprawnień ``sudo``, dlatego polecenia instalacji
      należy wydawać z konta użytkownika root, co oznaczamy znakami ``~#``.
    * W systemach opartych na *Debianie* (*(X)Ubuntu, LinuxMint* itp.) interpreter
      wywołujemy poleceniem ``python3``, w systemach opartych na *Arch Linuksie* –
      ``python``.


**Omówienie narzędzi:**

* `pip <https://pip.pypa.io/en/stable/>`_  – instalator pakietów Pythona,
  podstawowe narzędzie służące do zarządzania pakietami Pythona zgromadzonymi np.
  w repozytorium `PyPI <https://pypi.python.org/pypi>`_  (Python Package Index);
* `virtualenv <https://virtualenv.readthedocs.org/en/latest/>`_  –
  menedżer wirtualnych środowisk Pythona, pozwala tworzyć katalogi zawierające
  izolowane środowisko Pythona umożliwiające instalowanie wybranych wersji pakietów
  przez zwykłych użytkowników;
* `klient git <https://git-scm.com/downloads>`_  – narzędzie wersjonowania kodu
  umożliwiające korzystanie z repozytoriów i dokumentacji w serwisie `Github <https://github.com/>`_
* `sqlite3 <https://www.sqlite.org/>`_ – konsolowa powłoka dla baz SQLite3,
  umożliwia przeglądanie schematów tabel oraz zarządzanie bazą za pomocą języka SQL.
* `ipython <http://ipython.org/>`_ i `qtconsole <http://jupyter.org/qtconsole/stable/>`_ – rozszerzona interaktywna konsola Pythona;
*   – rozszerzona interaktywna konsola
  Pythona wykorzystująca bibliotekę Qt, umożliwia m. in. wyświetlanie wykresów utworzonych
  z wykorzystaniem *matplotlib*.



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
