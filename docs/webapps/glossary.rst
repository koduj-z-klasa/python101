Słownik aplikacji internetowych
###############################

.. glossary::

    aplikacja
        program komputerowy.

    framework
        zestaw komponentów i bibliotek wykorzystywany do budowy aplikacji,
        przykładem jest biblioteka Pythona Flask.

    HTML
        język znaczników wykorzystywany do formatowania dokumentów, zwłaszcza stron WWW.

    CSS
        język służący do opisu formy prezentacji stron WWW.

    HTTP
        protokół przesyłania dokumentów WWW. `Więcej o HTTP »»» <http://pl.wikipedia.org/wiki/Http>`_

    GET
        typ żądania HTTP, służący do pobierania zasobów z serwera WWW. `Więcej o GET »»» <https://pl.wikipedia.org/wiki/GET_%28metoda%29>`_

    POST
        typ żądania HTTP, służący do umieszczania zasobów na serwerze WWW. `Więcej o POST »»» <https://pl.wikipedia.org/wiki/POST_%28metoda%29>`_

    Kod odpowiedzi HTTP
    		numeryczne oznaczenie stanu realizacji zapytania klienta, np. `200 (OK)` lub `404 (Not Found)`. `Więcej o kodach HTTP »»» <https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP>`_

    logowanie
        proces autoryzacji i uwierzytelniania użytkownika w systemie.

    ORM
        (ang. Object-Relational Mapping) – mapowanie obiektowo-relacyjne, oprogramowanie
        odwzorowujące strukturę relacyjnej bazy danych na obiekty danego języka oprogramowania.

    Peewee
        prosty i mały system ORM, wspiera Pythona w wersji 2 i 3, obsługuje
        bazy SQLite3, MySQL, Posgresql.

    SQLAlchemy
        rozbudowany zestaw narzędzi i system ORM umożliwiający wykorzystanie
        wszystkich możliwości SQL-a, obsługuje bazy SQLite3, MySQL, Postgresql,
        Oracle, MS SQL Server i inne.

    serwer deweloperski
        testowy serwer www używany w czasie prac nad oprogramowaniem.

    serwer WWW
        serwer obsługujący protokół HTTP.

    baza danych
        program przeznaczony do przechowywania i przetwarzania danych.

    szablon
        wzorzec (nazywany czasem templatką) strony WWW wykorzystywany do renderowania widoków.

    URL
        ustandaryzowany format adresowania zasobów w internecie (`przykład <http://pl.wikipedia.org/wiki/Uniform_Resource_Locator>`_).

    MVC
        (ang. Model-View-Controller) – Model-Widok-Kontroler, wzorzec projektowania aplikacji rozdzielający
        dane (model) od sposobu ich prezentacji (widok) i zarządzania ich przepływem (kontroler).

    model
        schemat opisujący strukturę danych w bazie, np. klasa definiująca tabele i relacje między nimi.
        `Więcej o modelu bazy danych »»» <https://pl.wikipedia.org/wiki/Model_bazy_danych>`_

    widok
        we Flasku lub Django jest to funkcja lub klasa, która obsługuje żądania wysyłane przez użytkownika,
        przeprowadza operacje na danych i najczęściej zwraca je np. w formie strony WWW do przeglądarki.

    kontroler
        logika aplikacji, we Flasku lub Django mechanizm obsługujący żadania HTTP
        powiązane z określonymi adresami URL za pomocą widoków (funkcji lub klas).
