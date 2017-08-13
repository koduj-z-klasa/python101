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
np. obok MS Windows. Polecamy systemy, na których przetestowaliśmy scenariusze:

Oparte na Debianie:

* `Linux Mint 18 <https://www.linuxmint.com/download.php>`_
* `Ubuntu 16.04 LTS <https://www.ubuntu.com/>`__ lub jego odmiany np.
  `Xbuntu <https://xubuntu.org/getxubuntu/>`__.
* `Debian Stretch 9 <https://www.debian.org/index.pl.html>`_

Oparte na Arch Linuksie:

* `Manjaro <https://manjaro.org/>`_
* `Antergos <https://antergos.com/>`_

Środowisko graficzne (zob. :term:`środowisko graficzne`) dowolne, chociaż
osobom przyzwyczajonym do tradycyjnego pulpitu proponujemy `XFCE <http://www.xfce.org/>`_
lub `MATE <https://mate-desktop.org/pl/>`_.

**Wskazówki dotyczące instalacji:**

* `Windows i Linux na jednym dysku <https://www.dobreprogramy.pl/Windows-i-Linux-Mint-na-jednym-dysku-poradnik-dla-poczatkujacych,News,81165.html>`_;
* `Zainstaluj Linuksa <http://ecg.vot.pl/?id=linux-instalacja>`_;
* `Instalacja Ubuntu <http://ecg.vot.pl/?id=lubuntu>`_;
* `Instalacja Debiana <http://ecg.vot.pl/?id=debian-stable-install>`_.


.. _linux-pakiety:

Interpreter
===========

W Linuksach interpretery Pythona 2.x i 3.x zainstalowane są domyślnie.
W systemach opartych na *Debianie* domyślną wersją Pythona jest 2.7,
w systemach opartych na *Arch Linuksie* – 3.6. Uruchamiane są poleceniem
``python``. W każdym systemie można uruchomić potrzebną wersję
poleceniem ``python2`` lub ``python3``.

Narzędzia
=========

Potrzebne narzędzia dodajemy przy użyciu systemowego menedżera pakietów
(np. ``apt`` czy ``pacman``) lub instalatora pakietów Pythona ``pip``.

.. note::

  Poniżej podano polecenia dla instalacji ogólnosystemowej (globalnej),
  co wymaga uprawnień administracyjnych.

W systemach opartych na *Debianie* wydajemy polecenia w terminalu:

.. code-block:: bash

    ~$ sudo apt update
    ~$ sudo apt install python3-pip python3-venv git sqlite3
    ~$ sudo pip3 install virtualenv

W systemach opartych na *Arch Linuksie*:

.. code-block:: bash

    ~$ sudo pacman -Syyu
    ~$ sudo pacman -S python-pip python-virtualenv git sqlite

Biblioteki
==========

.. tip::

    W przypadku bibliotek warto rozważyć instalację
    w :ref:`środowisku wirtualnym <pve>` dostępną dla zwykłego użytkownika.

Jeżeli przeprowadzamy instalację ogólnosystemową i mamy uprawnienia administracyjne
wydajemy polecenia w terminalu. Dla Debiana i pochodnych:

.. code-block:: bash

    ~$ sudo apt install  ipython3-qtconsole python3-tk python3-sip python3-pyqt5
    ~$ sudo pip3 install matplotlib
    ~$ sudo pip3 install pygame
    ~$ sudo pip3 install flask flask-wtf peewee sqlalchemy flask-sqlalchemy django


Dla Archa i pochodnych:

.. code-block:: bash

    ~$ sudo pacman -S ipython python-qtconsole python-pyqt5 tk
    ~$ sudo pacman -S python-matplotlib
    ~$ sudo pip install pygame
    ~$ sudo pip install flask flask-wtf peewee sqlalchemy flask-sqlalchemy django

.. note::

    * Nazwy pakietów w różnych dystrybucjach mogą się nieco różnić od podanych.
    * Systemy *Debian* i *Arch Linux* w domyślnej konfiguracji nie wykorzystują
      mechanizmu podnoszenia uprawnień ``sudo``, wtedy polecenia instalacji
      należy wydawać z konta użytkownika *root*.
