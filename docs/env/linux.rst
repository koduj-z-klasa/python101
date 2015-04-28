Przygotowanie systemu Linux
###########################

W systemach linuksowych Python 2 jest zainstalowany domyślnie, wersję 3 również
zazwyczaj znajdziemy.
Instalacji brakujących elementów wykonujemy przy pomocy systemowego instalatora pakietów.

.. contents:: Spis treści
    :backlinks: none

.. note::

    Uwaga: nazwy pakietów w różnych dystrybucjach mogą się nieco różnić od podanych.


Instalacja apt-get
------------------

Instalację dodatkowych modułów w systemach opierających się na Debianie
(m. in. wszystkie wersje Ubuntu, LinuxMint itd.), przeprowadzamy przy użyciu
menedżera pakietów ``apt-get``.


.. code-block:: bash

    ~$ sudo apt-get update
    ~$ sudo apt-get install ipython python-pip python-virtualenv git
    ~$ sudo apt-get install python-flask python-django python-pygame

W pierwszej kolejności zainstalowane zostaną narzędzia, czyli rozszerzona
konsola ``ipython``, instalator modułów ``pip`` czy narzędzie pozwalające
ściągnąć i używać niniejsze materiały, czyli ``git``.


Biblioteki potrzebne do obsługi baz danych za pomocą ORM-ów można
zainstalować za pomocą menedżera systemowego lub (w razie niedostępności
danego pakietu) instalora Pythona ``pip``:

.. code-block:: bash

    ~$ sudo apt-get install python-peewee python-sqlalchemy python-flask-sqlalchemy
    ~$ sudo pip install peewee sqlalchemy flask-sqlalchemy


Instalacja pacman
-----------------

W systemach opartych na Arch Linuksie (Bridge Linux, Manjaro)
wykorzystują menedżer ``pacman``. W zależności od dystrybucji wydajemy polecenia:

.. code-block:: bash

    ~# pacman -Syu
    ~# pacman -S ipython2 python2-pip python2-virtualenv git
    ~# pacman -S install python2-flask python2-django python2-pygame

W pierwszej kolejności zainstalowane zostaną narzędzia, czyli rozszerzona
konsola ``ipython``, instalator modułów ``pip`` czy narzędzie pozwalające
ściągnąć i używać niniejsze materiały, czyli ``git``.


Biblioteki potrzebne do obsługi baz danych za pomocą ORM-ów można
zainstalować za pomocą menedżera systemowego lub (w razie niedostępności
danego pakietu) instalora Pythona ``pip``:

.. code-block:: bash

    ~# pacman -S python2-peewee  python2-sqlalchemy python2-flask-sqlalchemy
    ~# pip2 install peewee sqlalchemy flask-sqlalchemy

W innych systemach linuksowych należy korzystać z dedykowanych menedżerów
lub wspomnianego instalatora Pythona (``pip``).
