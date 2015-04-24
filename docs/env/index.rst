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


Przygotowane scenariusze zakładają również, że pracujemy w **katalogu domowym** użytkownika.
W systemach linuksowych jest to folder o nazwie użytkownika zalogowanego
znajdujący w katalogu ``/home``, np. ``/home/xubuntu``. W poleceniach wydawanych
w terminalu ścieżkę do tego katalogu symbolizuje znak ``~``. :term:`Terminal`
to inaczej konsola tekstowa, której w Linuksie często używa się, aby szybciej
wykonywać wiele operacji. W polecanym systemie uruchomimy ją za pomocą skrótu :kbd:`Win+T`.
Niekiedy podawany kod zawierać będzie sekwencje typu ``~/quiz2$``. Oznacza to,
że dane polecenie należy wykonać w katalogu ``quiz2`` znajdującym się
w katalogu domowym użytkownika. Znak ``$`` oznacza, że komendy wydajemy
jako zwykły użytkownik.

.. note::

    Omówione założenia nie znaczą, że materiału nie da się przećwiczyć
    na innych systemach, np. MS Windows. Da się, wystarczy doinstalować
    interpreter Pythona i potrzebne biblioteki, co zostanie omówione
    dalej.



Najwygodniej pracować w systemie zainstalowanym na stałe. Polecamy
`Xubuntu`_ 14.04 LTS. To :term:`dystrybucja Linuksa` będąca odmianą `Ubuntu`_ opartą o tradycyjne,
proste i wydajne :term:`środowisko graficzne` `XFCE`_. Instalacja i obsługa tego systemu
są intuicyjne. Aby zainstalować system, trzeba pobrać :term:`obraz iso`
z wybranego serwera wskazanego na stronie http://xubuntu.org/getxubuntu,
a następnie wypalić go na płycie DVD za pomocą dowolnego programu do nagrywania
płyt w systemie Linux lub MS Windows, można go też wgrać na klucz USB.

.. note::

    Xubuntu jest jedną z wielu dystrybucji Linuksa. Scenariusze można
    realizować w oparciu o dowolną dystrybucję, wystarczy doinstalować
    potrzebne biblioteki i korzystać z Pythona 2. Scenariusze testowano
    m. in. na takich dystrybucjach, jak: Debian (Wheezy, Jessie), który
    *nota-bene* jest podstawą Ubuntu, i Arch Linux. Środowisko graficzne
    nie ma oczywiście znaczenia.






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

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>



