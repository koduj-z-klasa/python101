Słownik
#######

.. glossary::

    ACID
        Atomicity, Consistency, Isolation, Durability – Atomowość, Spójność, Izolacja, Trwałość;
        zasady określające kryteria poprawnego zapisu danych w bazie. `Więcej o ACID »»» <http://pl.wikipedia.org/wiki/ACID>`_

    API
        (ang. *Application Programming Interfac*) – interfejs programistyczny aplikacji,
        określa sposób, czyli zasady i reguły komunikacji między oprogramowaniem;
        w Pythonie za pomocą API uzyskuje się dostęp do określonych bibliotek,
        np. Pygame lub Matplotlib.

    baza danych
        program przeznaczony do przechowywania i przetwarzania danych.

    ciasteczka
        (ang. *cookies*) zaszyfrowane dane tekstowe wysyłane przez serwer i zapamiętywane po stronie klienta,
        zawierają np. identyfikator sesji użytkownika.

    dana statyczna
        – (ang. static data), dane powiązane z klasą, a nie z jej instancjami, czyli obiektami.
        Tworzymy je definiując atrybuty klasy. Korzystamy z nich podając nazwę klasy, np.:
        ``Klasa.dana``. Wszystkie instancje klasy dzielą ze sobą jeden egzemplarz danych statycznych.

    dekorator
        funkcja, która jako argument otrzymuje inną funkcję, rozszerza jej działanie i zwraca ją.

    dystrybucja Linuksa
        określona wersja systemu operacyjnego oparta na jądrze Linux, udostępniana
        zazwyczaj w formie obrazów *iso*. Najbardziej znane to `Debian`_ i jego odmiany:
        `Ubuntu <http://ubuntu.pl>`_, `Linux Mint`_, `MX Linux`_.
        Zob.: `dystrybucjach Linuksa <http://pl.wikipedia.org/wiki/Dystrybucja_Linuksa>`_

    CRUD
        skrót opisujący podstawowe operacje na bazie danych z wykorzystaniem języka SQL,
        *Create* (tworzenie) odpowiada zapytaniom *INSERT*, *Read* (odczyt) - zapytaniom
        *SELECT*, *Update* (aktualizacja) - *UPDATE*, *Delete* (usuwanie) - *DELETE*.

    CSS
        język służący do opisu formy prezentacji stron WWW.

    dziedziczenie
        w programowaniu obiektowym nazywamy mechanizm współdzielenia funkcjonalności
        między klasami. Klasa może dziedziczyć po innej klasie, co w najprostszym przypadku oznacza,
        że oprócz swoich własnych atrybutów oraz zachowań, uzyskuje także te pochodzące
        z klasy, z której dziedziczy. Jest wiele odmian `dziedziczenia <https://pl.wikipedia.org/wiki/Dziedziczenie_%28programowanie%29>`_ .

    framework
        zestaw komponentów i bibliotek wykorzystywany do budowy aplikacji,
        przykładem jest biblioteka Pythona Flask.

    GET
        typ żądania HTTP, służący do pobierania zasobów z serwera WWW. `Więcej o GET »»» <https://pl.wikipedia.org/wiki/GET_%28metoda%29>`_

    główna pętla programu
        (ang. *mainloop*) – mechanizm komunikacji między aplikacją, systemem i użytkownikiem.
        Zapewnia przekazywanie zdarzeń do aplikacji. Zdarzenia wynikają z zachowania
        systemu lub użytkownika (kliknięcia, użycie klawiatury, czyli edycja danych itd.)
        i przekazywane są do widżetów apliakcji, które mogą – choć nie muszą – na nie reagować,
        np. wywołując jakąś metodę (funkcję).

    GUI
        (ang. Graphical User Interface) – graficzny interfejs użytkownika, czyli sposób prezentacji
        informacji na komputerze i innych urządzeniach oraz interakcji z użytkownikiem.

    HTML
        język znaczników wykorzystywany do formatowania dokumentów, zwłaszcza stron WWW.

    HTTP
        protokół przesyłania dokumentów WWW. `Więcej o HTTP »»» <http://pl.wikipedia.org/wiki/Http>`_

    inicjalizacja
        proces wstępnego przypisania wartości zmiennym i obiektom. Każdy obiekt jest inicjalizowany różnymi sposobami zależnie od swojego typu.

    instancja
        obiekt stworzony na podstawie klasy.

    iteracja
        czynność powtarzania (najczęściej wielokrotnego) tej samej instrukcji (albo wielu instrukcji) w pętli. Mianem iteracji określa się także operacje wykonywane wewnątrz takiej pętli.

    JSON
        JavaScript Object Notation – prosty tekstowy format wymiany danych
        oparty na podzbiorze języka JavaScript, obsługiwany przez większość
        języków programowania, szeroko stosowany w aplikacjach internetowych.

    klasa
        schematyczny model obiektu zawierający jego właściwości i metody;
        właściwości to dane, którymi manipuluje się za pomocą metod klasy implementowanych
        jako funkcje.

    kwerenda
        Zapytanie do bazy danych zazwyczaj w oparciu o dodatkowe kryteria,
        którego celem jest wydobycie z bazy określonych danych lub ich modyfikacja.

    kod źródłowy
        w przypadku języka Python są to instrukcje programu zapisane w plikach tekstowych
        zwanych skryptami, które wykonywane są przez interpreter Pythona

    kod odpowiedzi HTTP
        numeryczne oznaczenie stanu realizacji zapytania klienta, np. `200 (OK)` lub `404 (Not Found)`.
        `Więcej o kodach HTTP »»» <https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP>`_

    konstruktor
        metoda wywoływana podczas tworzenia instancji (obiektu) klasy, zazwyczaj
        przyjmuje jako argumenty inicjalne wartości zdefiniowanych w klasie atrybutów
        (właściwości); w Pythonie nazywa się ``__init()__``.

    kontroler
        logika aplikacji, we Flasku lub Django mechanizm obsługujący żądania HTTP
        powiązane z określonymi adresami URL za pomocą widoków (funkcji lub klas).

    Linux
        rodzina uniksopodobnych systemów operacyjnych opartych na jądrze Linux.
        Linux jest jednym z przykładów wolnego i otwartego oprogramowania
        (FLOSS): jego kod źródłowy może być dowolnie wykorzystywany,
        modyfikowany i rozpowszechniany. Źródło: `Wikipedia <http://pl.wikipedia.org/wiki/Linux>`_

    logowanie
        proces autoryzacji i uwierzytelniania użytkownika w systemie.

    metoda statyczna
        – (ang. static method), metody powiązane z klasą, a nie z jej instancjami, czyli obiektami.
        Tworzymy je używając w ciele klasy dekoratora ``@staticmethod``.
        Do metody takiej trzeba odwoływać się podając nazwę klasy, np. Klasa.metoda().
        Metoda statyczna nie otrzymuje parametru ``self``.

    migracja
        we frameworku Django jest to opis zmian w bazie danych przygotowany na podstawie modeli (klas)
        z pliku :file:`models.py` definiujących obiekty przetwarzane w aplikacji, np. wiadomości.
        Po każdej zmianie modelu należy migrację utworzyć, a następnie ją wykonać.

    model
        schemat opisujący strukturę danych w bazie, np. klasa definiująca tabele i relacje między nimi.
        `Więcej o modelu bazy danych »»» <https://pl.wikipedia.org/wiki/Model_bazy_danych>`_

    MVC
        (ang. Model-View-Controller) – Model-Widok-Kontroler, wzorzec projektowania aplikacji rozdzielający
        dane (model) od sposobu ich prezentacji (widok) i zarządzania ich przepływem (kontroler).

    obiekt
        podstawowe pojęcie programowania obiektowego, struktura zawierająca
        dane i metody (funkcje), za pomocą których wykonuje ṣię na nich operacje.

    obraz iso
        format zapisu danych dysków CD/DVD, tzw. hybrydowe obrazy iso, wykorzystywane
        do udostępniania dystrybucji linuksowych, umożliwiają uruchmianie
        systemu zarówno z płyt optycznych, jak i napędów USB.

    ORM
        (ang. Object-Relational Mapping) – mapowanie obiektowo-relacyjne, oprogramowanie
        odwzorowujące strukturę relacyjnej bazy danych na obiekty danego języka oprogramowania.

    szablon
        plik zawierający znaczniki HTML oraz tagi szablonów, za pomocą których można:
        dziedziczyć kod z szablonu bazowego, używać instrukcji sterujących i/lub
        wstawiać przekazane do szablonu dane

    sygnały i sloty
        – (ang. *signals and slots*), w kontekście biblioteki Qt sygnały powstają kiedy zachodzi jakieś wydarzenie.
        W odpowiedzi na sygnał wywoływane są sloty, czyli funkcje. Wiele sygnałów
        można łączyć z jednym slotem i odwrotnie. Można też łączyć ze sobą sygnały.
        Widżety Qt mają wiele predefiniowanych zarówno sygnałów, jak i slotów.
        Można jednak tworzyć własne. Dzięki temu obsługuje się tylko te zdarzenia,
        które nas interesują.

    POST
        typ żądania HTTP, służący do umieszczania zasobów na serwerze WWW. `Więcej o POST »»» <https://pl.wikipedia.org/wiki/POST_%28metoda%29>`_

    Peewee
        prosty i mały system ORM, wspiera Pythona w wersji 2 i 3, obsługuje
        bazy SQLite3, MySQL, Posgresql.

    przesłanianie
        w programowaniu obiektowym możemy w klasie dziedziczącej przesłonić metody
        z klasy nadrzędnej rozszerzając lub całkowicie zmieniając jej działanie

    Python
        język programowania wysokiego poziomu, wyposażony w wiele bibliotek
        standardowych, jak i dodatkowych. Cechuje go łatwość uczenia się,
        czytelność i zwięzłość kodu, a także dynamiczne typowanie.
        Jako język skryptowy, wymaga interpretera. Czytaj więcej o `Pythonie <http://pl.wikipedia.org/wiki/Python>`_

    renderowanie szablonu
        przetwarzanie szkieletowego kodu HTML oraz specjalnych tagów w celu
        uzyskania kompletnego kodu HTML strony zawierającego przekazane
        do szablonu dane.

    serwer deweloperski
        testowy serwer www używany w czasie prac nad oprogramowaniem.

    serwer WWW
        serwer obsługujący protokół HTTP.

    sesja
        w kontekście aplikacji wykorzystujących protokół HTTP sposób zapamiętywania po stronie serwera
        danych związanych z konkretnym użytkownikiem.

    środowisko graficzne
        w systemach linuksowych zestaw oprogramowania tworzący GUI, czyli graficzny
        interfejs użytkownika, często zawiera domyślny wybór aplikacji przeznaczonych
        do wykonywania typowych zadań. Najpopularnijesze środowiska to `XFCE`_,
        `Gnome`_, `KDE`_, `LXDE <http://pl.wikipedia.org/wiki/LXDE>`__, `Cinnamon`_, `Mate`_.

    szablon
        wzorzec (nazywany czasem templatką) strony WWW wykorzystywany do renderowania widoków.

    terminal
        inaczej zwany konsolą tekstową, wierszem poleceń itp. Program umożliwiający
        wykonywanie operacji w powłoce tekstowej systemu za pomocą wpisywanych poleceń.
        W systemach Linux często da się go uruchomić skrótem :kbd:`Win+T`
        lub :kbd:`Ctrl+Alt+T`. Jeśli skróty nie działają, szukamy w menu start.
        Skrót :kbd:`Ctrl+Shift+T` pozwala otworzyć kolejną kartę terminala,
        w każdej karcie możemy robić coś innego.

    typy danych
        rodzaj danych przetwarzanych przez programy zapisane w danym języku programowania.
        W Pythonie trzy podstawowe typy danych to: łańcuchy znaków (*str*, skrót od ang. *string*),
        liczby całkowite (*int*, skrót od ang. *integer*), liczby zmiennoprzecinkowe
        (*float*, skrót od ang. *floating point*), oraz wartość logiczna (*bool*, skrót od ang. *boolean*).

    SQL
        strukturalny język zapytań używany do tworzenia i zarządzania bazą danych.

    SQLAlchemy
        rozbudowany zestaw narzędzi i system ORM umożliwiający wykorzystanie
        wszystkich możliwości SQL-a, obsługuje bazy SQLite3, MySQL, Postgresql,
        Oracle, MS SQL Server i inne.

    SQLite3
        silnik bezserwerowej, nie wymagającej dodatkowej konfiguracji, transakcyjnej bazy danych
        implementującej standard SQL.

    Transakcja
        zbiór powiązanych logicznie operacji na bazie danych, który powinien być
        albo w całości zapisany, albo odrzucony ze względu na naruszenie zasad
        spójności (ACID).

    URL
        ustandaryzowany format adresowania zasobów w internecie (`przykład <http://pl.wikipedia.org/wiki/Uniform_Resource_Locator>`_).

    widok
        we Flasku lub Django jest to funkcja lub klasa, która obsługuje żądania wysyłane przez użytkownika,
        przeprowadza operacje na danych i najczęściej zwraca je np. w formie strony WWW do przeglądarki.

    widżet
        (ang. *widget*) – podstawowy element graficzny interfejsu, zwany czasami kontrolką,
        nie tylko główne okno aplikacji, ale również etykiety, pola edycyjne, przycicki itd.

    zdarzenie (ang. *event*)
        zapis zajścia w systemie komputerowym określonej sytuacji, np. poruszenie myszką, kliknięcie, naciśnięcie klawisza.


.. _Debian: https://www.debian.org/index.pl.html
.. _Linux Mint: https://www.linuxmint.com
.. _MX Linux: https://mxlinux.org/
.. _Arch Linux: http://archlinux.pl
.. _Slackware: http://pl.wikipedia.org/wiki/Slackware
.. _Gnome: http://pl.wikipedia.org/wiki/GNOME
.. _KDE: http://pl.wikipedia.org/wiki/KDE
.. _Cinnamon: http://en.wikipedia.org/wiki/Cinnamon_%28software%29
.. _Mate: http://pl.wikipedia.org/wiki/MATE
.. _XFCE: http://www.xfce.org/
.. _Bash: http://pl.wikipedia.org/wiki/Bash