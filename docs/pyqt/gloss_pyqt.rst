Słownik (Py)Qt
################

.. glossary::

    GUI
        (ang. Graphical User Interface) – graficzny interfejs użytkownika, czyli sposób prezentacji
        informacji na komputerze i innych urządzeniach oraz interakcji z użytkownikiem.

    widżet
        (ang. *widget*) – podstawowy element graficzny interfejsu, zwany czasami kontrolką,
        nie tylko główne okno aplikacji, ale również etykiety, pola edycyjne, przycicki itd.

    główna pętla programu
        (ang. *mainloop*) – mechanizm komunikacji między aplikacją, systemem i użytkownikiem.
        Zapewnia przekazywanie zdarzeń do aplikacji. Zdarzenia wynikają z zachowania
        systemu lub użytkownika (kliknięcia, użycie klawiatury, czyli edycja danych itd.)
        i przekazywane są do widżetów apliakcji, które mogą – choć nie muszą – na nie reagować,
        np. wywołując jakąś metodę (funkcję).

    klasa
        – schematyczny model obiektu, czyli opis jego właściwości i działań na nich.
        Właściwości tworzą dane, którymi manipuluje się za pomocą metod klasy implementowanych
        jako funkcje.

    konstruktor
        – metoda wykonywana domyślnie w momncie tworzenia instancji klasy, czyli obiektu.
        Służy do inicjowania danych klasy. W Pythonie nazywa się ``__init()__``.

    obiekt
        – termin wieloznaczny; w kontekście OOP (ang. Object Oriented Programing), czyli programowania
        zorientowanego obiektowo, oznacza element rzeczywistości, który próbujemy
        opisać za pomocą klas. Np. osobę, ale też okno aplikacji.

    instancja
        – obiekt utworzony na podstawie klasy, która go opisuje. Posiada konkretne
        właściwości, które odróżniają go od innych instancji klasy.

    sygnały i sloty
        – (ang. signals and slots), sygnały powstają kiedy zachodzi jakieś wydarzenie.
        W odpowiedzi na sygnał wywoływane są sloty, czyli funkcje. Wiele sygnałów
        można łączyć z jednym slotem i odwrotnie. Można też łączyć ze sobą sygnały.
        Widżety Qt mają wiele predefiniowanych zarówno sygnałów, jak i slotów.
        Można jednak tworzyć własne. Dzięki temu obsługuje się tylko te zdarzenia,
        które nas interesują.

    dziedziczenie
        w programowaniu obiektowym nazywamy mechanizm współdzielenia funkcjonalności
        między klasami. Klasa może dziedziczyć po innej klasie, co w najprostszym przypadku oznacza,
        że oprócz swoich własnych atrybutów oraz zachowań, uzyskuje także te pochodzące
        z klasy, z której dziedziczy. Jest wiele odmian `dziedziczenia <https://pl.wikipedia.org/wiki/Dziedziczenie_%28programowanie%29>`_ .

    metoda statyczna
        – (ang. static method), metody powiązane z klasą, a nie z jej instancjami, czyli obiektami.
        Tworzymy je używając w ciele klasy dekoratora ``@staticmethod``.
        Do metody takiej trzeba odwoływać się podając nazwę klasy, np. Klasa.metoda().
        Metoda statyczna nie otrzymuje parametru ``self``.

    dana statyczna
        – (ang. static data), dane powiązane z klasą, a nie z jej instancjami, czyli obiektami.
        Tworzymy je definiując atrybuty klasy. Korzystamy z nich podając nazwę klasy, np.:
        ``Klasa.dana``. Wszystkie instancje klasy dzielą ze sobą jeden egzemplarz danych statycznych.