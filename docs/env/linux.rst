Przygotowanie systemu Linux
###########################

Jeżeli nie masz zainstalowanego systemu Linux, możesz wykorzystać wersję
Live, która po nagraniu na pendrajwa pozwol uruchomić komputer. Zob. :ref:`Linux Live <linux-live>`.
Jeżeli masz Linuksa lub planujesz go zainstalować na dysku, czytaj dalej.

W systemach linuksowych Python 2.7.x zainstalowany jest domyślnie,
wersję 3 również. Potrzebne narzędzia instalujemy przy użyciu systemowego
menedżera pakietów, natomiast biblioteki wykorzystywane w materiałach za pomocą
instalatora pakietów Pythona ``pip``.

Narzędzia:

* pip – instalator pakietów Pythona
* virtualenv – menedżer wirtualnych środowisk
* git – narzędzie umożliwiające korzystanie z zasobów serwisu `Github <https://github.com/>`
* ipython – rozszerzona interaktywna konsola Pythona

.. contents:: Spis treści
    :backlinks: none

.. note::

    * Nazwy pakietów w różnych dystrybucjach mogą się nieco różnić od podanych.
    * *Pygame* to jedyna biblioteka, którą trzeba instalować za pomocą systemowego
      menedżera pakietów.
    * Systemy Debian i Arch Linux w domyślnej konfiguracji nie wykorzytują
      mechanizmu podnoszenia uprawnień ``sudo``, dlatego polecenia instalacji
      należy wydawać z konta użytkownika root (w kodzie oznaczane znakami ``~#``).

Debian, Ubuntu i pochodne
-------------------------

W systemach opartych na Debianie (m. in. wszystkie wersje Ubuntu, LinuxMint itd.)
używamy menedżera ``apt-get`` i w terminalu wydajemy następujące polecenia:

.. code-block:: bash

    ~$ sudo apt-get update
    ~$ sudo apt-get install python-pip python-virtualenv git ipython
    ~$ sudo apt-get install python-pygame
    ~$ sudo pip install --upgrade install
    ~$ sudo pip install Flask Django
    ~$ sudo pip install peewee sqlalchemy flask-sqlalchemy

Jeśli ``apt-get`` zgłosi problem z dostępnością pakietu, w systemach Ubuntu i pochodnych
należy spróbować włączyć dodatkowe źródła oprogramowania:

.. figure:: img/universe.png

Arch Linux i pochodne
---------------------

W systemach opartych na Arch Linuksie (Bridge Linux, Manjaro)
wykorzystują menedżer ``pacman``. Odpowiednie polecenia mają postać:

.. code-block:: bash

    ~# pacman -Syyu
    ~# pacman -S python2-pip python2-virtualenv git ipython2
    ~# pacman -S python2-pygame
    ~# pip2 install Flask Django
    ~# pip2 install peewee sqlalchemy flask-sqlalchemy

W innych systemach linuksowych należy korzystać z dedykowanych menedżerów
lub wspomnianego instalatora Pythona (``pip``).
