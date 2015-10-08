.. _linux-live:

Linux Live
###########

Klucz Live USB
===============

Klucz startowy USB z systemem w wersji *live* pozwala na uruchomienie
komputera, testowanie i pracę bez ingerowania w dane zgromadzone na
twardym dysku (np. inne systemy). Dystrybujce *live* można zainstalować
również w maszynie wirtualnej, na dysku twardym lub wykorzystać do odzyskiwania danych.

.. note::

    Bootowalna płyta CD/DVD z systemem Linux w wersji *live* nada się do instalacji
    systemu na twardym dysku, ale nie do realizacji scenariuszy. Nie będzie zawierać
    wymaganych bibliotek i nie umożliwi łatwego zachowywania utworzonych
    dokumentów.

Poniżej opisujemy instalację *Linux Live* na kluczu USB oraz w maszynie wirtualnej tak,
aby można było instalować oprogramowanie, zapisywać ustawienia i tworzone dokumenty.

.. _dystrybucje:

Polecane dystrybucje
---------------------

* `LxPupTahr 15.05.02 <http://lx-pup.weebly.com/>`_ – system zaprojektowany
  od podstaw jako *live* z możliwością zapisywania zmian. Oparty na stabilnym
  Ubuntu 14.04 LTS. Środowisko graficzne LXDE. Nasza dostosowana wersja zawiera
  wszystkie dodatkowe narzędzia i wymagane biblioteki.
  **System ten polecamy do realizowania scenariuszy na warsztatach i nie tylko.**

.. figure:: lxpupimg/lxpuptahr.png

   System LxPupTahr

W trybie live mogą być również zainstalowane inne dystrybucje, np.:
`Xubutnu 14.04 LTS <http://xubuntu.org/>`_, `Szkolny Remiks Ucznia v.37 <Szkolny Remiks Ucznia: http://sru.e-swoi.pl>`_
czy `FREE_DESKTOP v.02 <http://cyfrowaszkola.waw.pl/free_desktop-edukacyjny-remiks-dla-wszystkich/>`_.
Są one oparte na stabilnych wydaniach Ubuntu i oferują środowisko graficzne XFCE.
Do realizowania naszych scenariuszy wymagają doinstalowania części narzędzi i bibliotek.

.. _usb-creator:

W Windows
===================

* Pobieramy :term:`obraz iso` wybranej :ref:`dystrybucji <dystrybucje>`:

  - `LxPupTahr <https://copy.com/9WzmbHVn8T8UxsSN/tahrpup/kzkbox.iso?download=1>`_ (320MB)
  - `LxPupTahr Full <https://copy.com/9WzmbHVn8T8UxsSN/tahrpup/kzkbox_full.iso?download=1>`_ (500MB, zawiera edytory PyCharm Professional 4.5.4 i SublimeText 3)
  - lub: `Xubuntu <http://se.archive.ubuntu.com/mirror/cdimage.ubuntu.com/xubuntu/releases/14.04/release/xubuntu-14.04.2-desktop-i386.iso>`_ (975MB), `SRU v.37 32-bit <http://iso.sru.e-swoi.pl/SRU_MT-14.04-37.iso>`_ (2,4GB), `FREE_DESKTOP_CEO <http://cyfrowaszkola.waw.pl/_pliki/FREE_Desktop_CEO_02.iso>`_ (2,1GB)

* Do wgrania *LxPupTahr* pobieramy program `Rufus <https://rufus.akeo.ie/>`_.
  Dla pozostałych: `program Unetbootin <http://unetbootin.sourceforge.net/unetbootin-windows-latest.exe>`_.

* Wpinamy pendrajwa o pojemności min. 2GB dla dystrybucji *LxPupTahr*, 4GB – dla pozostałych.
  Pendrajw powinien mieć przynajmniej jedną główną i aktywną partycję FAT32 – tak jest zazwyczaj.

* **LxPupTahr**: po uruchomieniu *Rufusa* z uprawnieniami administratora z listy "Urządzenie" wybierz pendrajwa,
  zaznacz opcję "Utwórz bootowalny dysk używając" -> "Obraz ISO", kliknij ikonę obok
  i wskaż ściągnięty obraz iso, wybierz "Opcje formatowania" i zaznacz
  "Dodaj łatkę dla starych biosów"; kliknij "Start" i poczekaj do 5 min. na napis "Gotowe".

.. figure:: img/rufus02.jpg

.. tip::

    Jeżeli wybrałeś system *LxPupTahr*, przeczytaj :ref:`Pierwsze uruchomienie <lxpuptahr>`!!!

* *Xubuntu*, *SRU*, *FREE DESKTOP*: po uruchomieniu programu *Unetbootin*
  zaznaczamy opcję "Obraz dysku", klikamy przycisk "..." i wskazujemy
  pobrany obraz. W polu "Przestrzeń używana do zachowania plików..."
  wpisujemy min. **512**. W polu "Napęd:" wskazujemy pendrajwa i klikamy "OK".
  Czekamy w zależności od wybranej dystrybucji i prędkości klucza USB od 5-25 minut.

.. figure:: img/unetbootin_win_lxpup.jpg

W Linuksie
===========

* W Ubuntu i pochodnych instalujemy program `Unetbootin <http://unetbootin.sourceforge.net>`_ poleceniami:

.. code-block:: bash

    ~$ sudo apt-add-repository ppa:gezakovacs/ppa
    ~$ sudo apt-get update
    ~$ sudo apt-get install unetbootin

* W Debianie Jessie 8 ściągamy pakiet `unetbootin_608-1_i386.deb <http://ftp.pl.debian.org/debian/pool/main/u/unetbootin/unetbootin_608-1_i386.deb>`_,
  a następnie w katalogu z pobranym plikiem wydajemy polecenia jako root:

.. code-block:: bash

    ~# dpkg -i unetbootin_608-1_i386.deb
    ~# apt-get install -f

*  W Arch Linuksie i pochodnych jako root wydajemy polecenia:

.. code-block:: bash

    ~# pacman -Syu
    ~# pacman -S unetbootin

* Wpinamy pendrajwa o pojemności min. 4GB dla dystrybucji *SRU* (*Xubuntu*). Pendrajw
  powinien mieć przynajmniej jedną główną i aktywną partycję FAT32 – tak jest zazwyczaj.
* Po uruchomieniu programu "Unetbootin" zaznaczamy opcję "Obraz dysku", klikamy
  przycisk "..." i wskazujemy pobrany obraz.
* Jeżeli wybraliśmy *LxPupTahr*, przechodzimy do następnego punktu.
  Jeżeli wybraliśmy obraz *Xubuntu*, *SRU* lub *FREE_DESKTOP*, w polu "Przestrzeń
  używana do zachowania plików..." wpisujemy min. **512**.
* Upewniamy się, że w polu "Napęd:" wyświetlona jest litera przydzielona
  właściwemu pendrajwowi i klikamy "OK". Czekamy w zależności od wybranej
  dystrybucji i prędkości klucza USB od 1-20 minut.

.. figure:: img/unetbootin_win_free.jpg

.. note::

    Jeżeli nagrywamy obraz *Xubuntu*, *SRU* lub *FREE_DESKTOP* możemy na pendrajwie
    utworzyć dodatkową partycję typu Ext4 o dowolnej pojemności, ale obowiązkowej
    etykiecie "home-rw". Zostanie ona wykorzystana jako miejsce montowania
    i zapisywania plików użytkownika. W takim wypadku pole "Przestrzeń używana
    do zachowania plików..." pozostawiamy puste!

    Dodatkową partycję utworzysz przy użyciu programu **gparted**. Instalacja:
    ``sudo apt-get update && sudo apt-get install gparted``.
    Niestety za pomocą standardowych narzędzi MS Windows nie utworzymy partycji Ext4.
    Ostateczny układ partycji powinien wyglądać tak jak na poniższym zrzucie:

.. figure:: img/sru_usb08.png

W maszynie wirtualnej
=====================

Dystrybucję *LxPupTahr* łatwo zainstalować i uruchamiać w Windows (lub w Linuksie!) za pomocą
tzw. maszyny wirtualnej.

Do zarządzania maszynami wirtualnymi wykorzystamy program VirtualBox, który pobieramy w wersji
dla naszego systemu ze strony `VirtualBox <https://www.virtualbox.org/wiki/Downloads>`_ i instalujemy.
Następnie uruchamiamy aplikację i tworzymy nową maszynę wirtualną:

* nazwa – np. "LxPup", typ – *Linux*, wersja – *Ubuntu (32-bit)*;
* rozmiar pamięci – min. 1024MB
* tworzymy dysk twardy VDI o stałym rozmiarze min. 1024MB

Po utworzeniu maszyny w sekcji "Storage" jako dysk rozruchowy wskazujemy ściągnięty :term:`obraz iso` dystrybucji,
np. ``kzkbox_20150921_full.iso``:

.. figure:: vboximg/vbox05.jpg

Uruchamiamy maszynę, ale na ekranie roruchowym systemu podajemy dodatkowe
parametry uruchomieniowe: ``puppy pmedia=cd``:

.. figure:: vboximg/vbox06.jpg

Po uruchomieniu systemu zamykamy kreatora konfiguracji, w przypadku problemów z rozdzielczością
przechodzimy do trybu pełnoekranowego (:kbd:`HOST+F` lub menu *View/Full screen Mode*)
i uruchamiamy instalatora poleceniem *Start/Konfiguracja/Puppy uniwersalny instalator*.

1) W oknie "Instaluj" wybieramy *Uniwersalny instalator*;
2) W kolejnym wybieramy *Wewnętrzny (IDE lub SATA) dysk twardy*;
3) Następnie wskaujemy dysk *sda ATA VBOX HARDDISK* za pomocą ikony;
4) Kolejne okno umożliwi uruchomienie edytora GParted, za pomocą którego
   założymy i sformatujemy partycję systemową;

.. figure:: vboximg/puppy_vb04.png

5) W edytorze GParted wybieramy kolejno:

   a) w menu *Urządzenie/Utwórz tablicę partycji*, kolejne okno potwierdzamy *Zastosuj*;
   b) Klikamy nieprzydzielone miejsce prawym klawiszem i wybieramy *Nowa*, wybieramy
      "Partycja główna" i system "Ext4", zatwierdzamy *Dodaj*;
   c) Następnie wybieramy *Edycja/Zastosj wszystkie działania* lub klikamy ikonę "zielonego ptaszka";
   d) Na koniec klikamy utworzoną partycję prawym klawiszem, wybieramy *Zarządzaj flagami*,
      zaznaczamy opcję "boot" i zatwierdzamy *Zamknij*; w efekcie powinniśmy zobaczyć
      co następuje:

.. figure:: vboximg/puppy_vb07.png

6) Po zamknięciu edytora GParted, ponownie wskazujemy dysk "sda",
   a w kolejnym, powtórzonym oknie klikamy ikonę w prawym górnym rogu obok
   napisu "Instaluj Puppy na sda1";
7) W kolejnym oknie potwierdzamy instalację przyciskiem *OK*;
8) W następnym klikamy przycisk *CD*, aby wskazać położenie plików systemowych,
   i jeszcze raz potwierdzamy przyciskiem "OK";
9) W kolejnym oknie wybieramy *OSZCZĘDNY* tryb instalacji – system będzie zachowywał się
   tak, jakby był zainstalowany na pendrajwie; następne wyjaśnienia potwierdzamy *OK*;
10) Podajemy nazwę katalogu, w którym znajdą się pliki systemowe, np. "lxpup";
11) Po skopiowaniu plików wybieramy instalację bootmenedżera *grub4dos* przyciskiem *Tak*;
12) W oknie instalacyjnym Grub4Dos zaznaczamy opcje zgodnie ze zrzutem:

.. figure:: vboximg/puppy_vb10.png

13) W kolejnym oknie zatwierdzamy listę wykrytych systemów *OK*,
    a w następnym potwierdzamy instalację bootmenedżera w MBR;
14) Na koniec zamykamy informację o udanej instalacji:

.. figure:: vboximg/puppy_vb12.png

Zamykamy LxPup (*Start/Zamknij*), usuwamy plik obrazu iso z wirtualnego napędu
i możemy uruchomić LxPupTahr w maszynie wirtualnej:

.. figure:: vboximg/vbox07.jpg

System zainstalowany w ten sposób działa tak samo jak zainstalowany na kluczu USB,
a więc wymaga potwierdzenia konfiguracji wstępnej i utworzenia pliku zapisu.
Zob.: :ref:`Pierwsze uruchomienie <lxpuptahr>`!!!

.. tip::

  Za pomocą VirtualBoksa można zainstalować dowolną inną dystrybucję Linuksa
  z pobranego obrazu *iso*. Taka instalacja zadziała jak "normalny" system,
  a więc umożliwi aktualizację i instalację oprogramowania, a także zapis
  tworzonych dokumentów.

.. tip::

  W przypadku problemów z działaniem myszy w wirtualnym systemie,
  warto spróbować wyłączyć ewentualną automatyczną integrację kursora
  za pomocą skrótu :kbd:`HOST+I`. Klawisz ``HOST`` to wskazany w menu
  *File/Preferences/Input/Virtual Machine* klawisz umożliwiający
  sterowanie wirtualną maszyną. Dla polskiej klawiatury można
  ustawić np. prawy CTRL.

Materiały
========================

.. toctree::
    :maxdepth: 2
    :numbered:

    lxpup.rst
    problemy.rst
    opcje.rst
