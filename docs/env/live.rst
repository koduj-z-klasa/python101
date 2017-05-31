.. _linux-live:

Linux Live
**********

Klucz Live USB
===============

Klucz startowy USB z systemem w wersji *live* pozwala na uruchomienie
komputera, testowanie i pracę bez ingerowania w dane zgromadzone na
twardym dysku (np. inne systemy). Dystrybucje *live* można zainstalować
również w maszynie wirtualnej, na dysku twardym lub wykorzystać do odzyskiwania danych.

**Na potrzeby szkoleń, do realizacji scenariuszy i codziennej pracy,
dla nauczycieli i uczniów** przygotowaliśmy specjalne wersje dystrybucji
`Porteus <http://porteus.org/>`_ (opartej na systemie Slackware)
i `LxPup <http://lx-pup.weebly.com/>`_ (opartej na Ubutnu).
Systemy zawierają wszystkie dodatkowe narzędzia i biblioteki,
pozwalają doinstalowywać programy, zapisują ustawienia i utworzone dokumenty.

.. figure:: img/porteus322X.jpg

   Porteus 3.2.2 XFCE 64-bit


.. figure:: lxpupimg/xenialpup701.jpg

   LxPupXenial 7.0.1 32-bit

.. _usb-creator:

* Na początku pobieramy wybrany :term:`obraz iso`:

  - `porteus322XFCE.iso <https://drive.google.com/open?id=0B1zG9cfNyT7WakRQN1BWUEV4UFk>`_ (597MB)
  - `LxPupXenial Full <https://drive.google.com/open?id=0B1zG9cfNyT7WUExnbTNkTWtnZFE>`_ (705MB)
  - `LxPupXenial Base <https://drive.google.com/open?id=0B1zG9cfNyT7WN2JCZEZMNTJnMjg>`_ (412MB)

.. note::

  Wszystkie wersje zawierają edytor Geany. Dodatkowe programy w postaci modułów
  (np. IDE SublimeText3, PyCharm Professional) są albo w obrazie
  albo do pobrania i dodania.


W Windows
===================

* Pobieramy program `Rufus <https://rufus.akeo.ie/>`_.

* Wpinamy pendrajwa o pojemności min. 2GB z jedną główną i aktywną partycją FAT32 – tak jest zazwyczaj.

* Uruchamiamy *Rufusa* z uprawnieniami administratora, z listy "Urządzenie" wybieramy pendrajwa,
  zaznaczamy opcję "Utwórz bootowalny dysk używając" -> "Obraz ISO", klikamy ikonę obok
  i wskazujemy ściągnięty obraz iso. Następnie wybieramy "Opcje formatowania" i zaznaczamy
  "Dodaj łatkę dla starych biosów"; klikamy "Start" i czekamy do 5 min. na napis "Gotowe".

.. figure:: img/rufus02.jpg

.. tip::

  Po nagraniu systemu **przeczytaj** `Pierwsze uruchomienie Porteusa <http://linetc.readthedocs.io/pl/latest/porteus/index.html#pierwsze-uruchomienie>`_ lub
  :ref:`Pierwsze uruchomienie LxPupXenial <lxpup>`.

  Polecamy też: `Moduły w Porteusie <http://linetc.readthedocs.io/pl/latest/porteus/index.html#moduly>`_ lub :ref:`Dodawanie programów w LxPupXenial <sfs-pet>`.

W Linuksie
===========

* instalujemy program `Unetbootin <http://unetbootin.sourceforge.net>`_, w Ubuntu i pochodnych:

.. code-block:: bash

    ~$ sudo apt-add-repository ppa:gezakovacs/ppa
    ~$ sudo apt-get update
    ~$ sudo apt-get install unetbootin


- W Debianie Jessie 8 ściągamy pakiet `unetbootin_608-1_i386.deb <http://ftp.pl.debian.org/debian/pool/main/u/unetbootin/unetbootin_608-1_i386.deb>`_, a następnie w katalogu z pobranym plikiem wydajemy polecenia jako root:

.. code-block:: bash

    ~# dpkg -i unetbootin_608-1_i386.deb
    ~# apt-get install -f


- W Arch Linuksie i pochodnych jako root wydajemy polecenia:

.. code-block:: bash

    ~# pacman -Syu
    ~# pacman -S unetbootin

* Wpinamy pendrajwa o pojemności min. 2GB z jedną główną i aktywną partycją FAT32 – tak jest zazwyczaj.
* Po uruchomieniu programu "Unetbootin" zaznaczamy opcję "Obraz dysku", klikamy
  przycisk "..." i wskazujemy pobrany obraz.
* Upewniamy się, że w polu "Napęd:" wyświetlone jest oznaczenie przydzielone
  właściwemu pendrajwowi i klikamy "OK". Czekamy w zależności od wybranej
  dystrybucji i prędkości klucza USB od 1-20 minut.

.. figure:: img/unetbootin_linux_lxpup.png


Materiały
========================

.. toctree::
    :maxdepth: 2
    :numbered:

    live_vb.rst
    problemy.rst
    opcje.rst
    lxpup.rst

