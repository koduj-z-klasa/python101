System i oprogramowanie
#######################

Nasze materiały zakładają wykorzystanie systemu :term:`Linux` i języka :term:`Python` w wersji 2.7.x,
który jest częścią wszystkich desktopowych dystrybucji. Oprócz interpretera języka, który
wystarcza do zapoznania się z podstawami, potrzebne są biblioteki wykorzystywane
w bardziej zaawansowanych przykładach, takich jak gry, aplikacje internetowe
czy obsługa baz danych za pomocą systemów ORM.

Poniżej znajdziesz pomoc w przygotowaniu i konfiguracji środowiska do pracy z naszymi materiałami.

.. toctree::
    :maxdepth: 2
    :numbered:

    windows
    linux
    ide
    live
    py3
    git/git


Przygotowane scenariusze zakładają również, że pracujemy w **katalogu domowym** użytkownika.
W systemach Linux jest to folder o nazwie zalogowanego użytkownika w katalogu ``/home``,
np. ``/home/xubuntu``. W poleceniach wydawanych w terminalu (zob. :term:`terminal`)
ścieżkę do tego katalogu symbolizuje znak ``~``.

Zapis typu ``~/quiz2$`` oznacza, że dane polecenie należy wykonać w podkatalogu ``quiz2``
katalogu domowego użytkownika. Znak ``$`` oznacza, że komendy wydajemy
jako zwykły użytkownik, natomiast ``#`` – jako root, czyli administrator.

.. note::

    Materiały da się bez większych problemów realizować również w systemach MS Windows.

Najwygodniej pracować w systemie zainstalowanym na stałe. Polecamy:

* `Xubuntu`_ 14.04 LTS. – stabilna odmiana `Ubuntu`_, zawiera proste i wydajne
  :term:`środowisko graficzne` `XFCE`_. Zob. `Instalacja Lubuntu <http://ecg.vot.pl/?id=lubuntu>`_
  (instalacja jest taka sama).

* `Debian Jessie 8` – ostatnia stabilna wersja, również proponujemy wersję ze środowiskiem
  `XFCE`_. Zob.: `Instalacja Debian Jessie <http://ecg.vot.pl/?id=debian-stable-install>`_.

Instalacja wymaga pobrania odpowiedniego obrazu dystrybucji (zob. :term:`obraz iso`)
i nagrania go na nośnik startowy, CD/DVD lub klucz USB. Zob.: :ref:`Linux Live <linux-live>`.

.. note::

    Xubuntu jest jedną z wielu dystrybucji Linuksa. Scenariusze można
    realizować w oparciu o dowolną inną. Scenariusze testowano
    na takich dystrybucjach, jak: Debian (Wheezy, Jessie), (X)Ubuntu 12.04, 14.04,
    Arch Linux. Środowisko graficzne nie ma oczywiście znaczenia.

Pojęcia
=============

.. glossary::

    Python
        język programowania wysokiego poziomu, wyposażony w wiele bibliotek
        standardowych, jak i dodatkowych. Cechuje go łatwość uczenia się,
        czytelność i zwięzłość kodu, a także dynamiczne typowanie.
        Jako język skryptowy, wymaga interpretera. Czytaj więcej o `Pythonie <http://pl.wikipedia.org/wiki/Python>`_

    Linux
        rodzina uniksopodobnych systemów operacyjnych opartych na jądrze Linux.
        Linux jest jednym z przykładów wolnego i otwartego oprogramowania
        (FLOSS): jego kod źródłowy może być dowolnie wykorzystywany,
        modyfikowany i rozpowszechniany. Źródło: `Wikipedia <http://pl.wikipedia.org/wiki/Linux>`_

    dystrybucja Linuksa
        określona wersja systemu operacyjnego oparta na jądrze Linux, udostępniana
        zazwyczaj w formie obrazów *iso*. Najbardziej znane to: `Debian`_,
        `Ubuntu`_ i jego odmiany (np. `Xubuntu`_), `Linux Mint`_, `Arch Linux`_, `Slackware`_,
        `Fedora`_, `Open Suse`_. Czytaj więcej o `dystrybucjach Linuksa <http://pl.wikipedia.org/wiki/Dystrybucja_Linuksa>`_

    obraz iso
        format zapisu danych dysków CD/DVD, tzw. hybrydowe obrazy iso, wykorzystywane
        do udostępniania dystrybucji linuksowych, umożliwiają uruchmianie
        systemu zarówno z płyt optycznych, jak i napędów USB.

    środowisko graficzne
        w systemach linuksowych zestaw oprogramowania tworzący GUI, czyli graficzny
        interfejs użytkownika, często zawiera domyślny wybór aplikacji przeznaczonych
        do wykonywania typowych zadań. Najpopularnijesze środowiska to `XFCE`_,
        `Gnome`_, `KDE`_, `LXDE`_, `Cinnamon`_, `Mate`_.

    terminal
        inaczej zwany konsolą tekstową, wierszem poleceń itp. Program umożliwiający
        wykonywanie operacji w powłoce tekstowej systemu za pomocą wpisywanych poleceń.
        W Linuksach rolę powłoki pełni najczęściej `Bash`_, w Ubuntu zastępuje ją mniejszy
        i szybszy odpowiednik, czyli Dash.

.. _Debian: https://www.debian.org/index.pl.html
.. _Ubuntu: http://ubuntu.pl
.. _Xubuntu: http://xubuntu.org/
.. _Linux Mint: http://pl.wikipedia.org/wiki/Linux_Mint
.. _Arch Linux: http://archlinux.pl
.. _Slackware: http://pl.wikipedia.org/wiki/Slackware
.. _Fedora: https://getfedora.org/pl/workstation
.. _Open Suse: https://pl.opensuse.org/Witamy_w_openSUSE.org
.. _Gnome: http://pl.wikipedia.org/wiki/GNOME
.. _KDE: http://pl.wikipedia.org/wiki/KDE
.. _LXDE: http://pl.wikipedia.org/wiki/LXDE
.. _Cinnamon: http://en.wikipedia.org/wiki/Cinnamon_%28software%29
.. _Mate: http://pl.wikipedia.org/wiki/MATE
.. _XFCE: http://www.xfce.org/
.. _Bash: http://pl.wikipedia.org/wiki/Bash
