.. _linux-env:

Przygotowanie systemu Linux
###########################

Jeżeli nie masz zainstalowanego systemu Linux, możesz wykorzystać wersję
:ref:`Linux Live <linux-live>`. Jeżeli masz Linuksa lub planujesz go zainstalować
na dysku, czytaj dalej.

.. _linux-distro:

Dystrybucje
===========

Najwygodniej pracować w systemie Linux zainstalowanym na dysku twardym,
np. obok albo zamiast MS Windows. Polecamy dystrybucje oparte na Debianie,
na których przetestowaliśmy scenariusze:

* `Linux Mint 20.04 <https://www.linuxmint.com>`_
* `Ubuntu 20.04 LTS <https://www.ubuntu.com/>`__.
* `MX Linux 21 <https://mxlinux.org/>`_

Środowisko graficzne (zob. :term:`środowisko graficzne`) dowolne.

**Wskazówki dotyczące instalacji:**

* `Windows i Linux na jednym dysku <https://www.dobreprogramy.pl/Windows-i-Linux-Mint-na-jednym-dysku-poradnik-dla-poczatkujacych,News,81165.html>`_;
* `Zainstaluj Linuksa <http://srv40578.seohost.com.pl/linux>`_;
* `Instalacja Ubuntu <http://srv40578.seohost.com.pl/lubuntu>`_;
* `Linux Mint Installation Guide <https://linuxmint-installation-guide.readthedocs.io/en/latest/index.html>`_

.. _linux-pakiety:

Interpreter, narzędzia i pakiety
================================

W Linuksach interpreter Pythona 3.x zainstalowany jest domyślnie.
Wymagane pakiety Pythona i/lub wersję Pythona 2.x, a także narzędzia dodatkowe
w razie potrzeby instalujemy za pomocą systemowego menedżera pakietów ``apt``.
Pakiety można również instalować przy użyciu instalatora pakietów Pythona
`pip <http://www.pip-installer.org/en/latest/>`_.

.. note::

   Polecenie ``sudo`` oznacza, że do instalacji potrzebne są uprawnienia administracyjne,
   czyli w praktyce należy być zalogowanym na koncie użytkownika utworzonym podczas instalacji systemu.

* Aktualizacja bazy oprogramowania i instalacja podstawowych narzędzi:

   .. code-block:: bash

       ~$ sudo apt update
       ~$ sudo apt install python3-pip python3-venv git sqlite3

* Ogólnosystemowa instalacja rozszerzonych powłok:

   .. code-block:: bash

       ~$ sudo apt install python3-qtconsole python3-tk python3-sip python3-pyqt5

* Ogólnosystemowa instalacja dodatkowych pakietów:

   .. code-block:: bash

       ~$ sudo pip3 install matplotlib
       ~$ sudo pip3 install pygame
       ~$ sudo pip3 install flask flask-wtf peewee sqlalchemy flask-sqlalchemy django

.. tip::

    Zamiast ogólnosystemowej instalacji rozszerzonych powłok i pakietów
    zalecamy instalację w :ref:`środowisku wirtualnym <pve>`
    dostępną dla zwykłego użytkownika.

.. note::

    * Nazwy pakietów w różnych dystrybucjach mogą się nieco różnić od podanych.
    * System *Debian* w domyślnej konfiguracji nie wykorzystuje
      mechanizmu podnoszenia uprawnień ``sudo``, wtedy polecenia instalacji
      należy wydawać z konta użytkownika *root*.
