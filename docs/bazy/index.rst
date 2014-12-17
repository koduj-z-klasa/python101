Bazy danych w Pythonie
============================

Tworzenie i zarządzanie bazami danymi za pomocą Pythona z wykorzystaniem
wbudowanego modułu `sqlite3 DB-API`_, a także zewnętrznych bibliotek ORM:
`Peewee`_ oraz `SQLAlchemy`_

.. _sqlite3 DB-API: https://docs.python.org/2/library/sqlite3.html
.. _Peewee: http://peewee.readthedocs.org/en/latest/index.html
.. _SQLAlchemy: http://www.sqlalchemy.org

.. note::

    Poniższe przykłady wykorzystywać będą prostą, wydajną, stosowaną
    zarówno w prostych, jak i zaawansowanych projektach, `bazę danych SQLite3`_.
    Gdy zajdzie potrzeba, można je jednak wyorzystać w pracy z innymi
    bazami, takimi jak np. MySQL, MariaDB czy PostgresSQL.
    Do testowania baz danych SQLite można wykorzystać przygotowane przez
    jej twórców konsolowe narzędzie `sqlite3`_. W linuksach opartych na Debianie
    (m. in. Ubuntu i pochodne) instalujemy je poleceniem typu:
    ``apt-get install sqlite3``; w systemach Windows natomiast rozpakowujemy
    z pobranego `archiwum`_.

.. _bazę danych SQLite3: http://www.sqlite.org/
.. _sqlite3: http://www.sqlite.org/cli.html
.. _archiwum: http://www.sqlite.org/download.html

SQL
-------------------

Jak wiadomo, do obsługi bazy danych wykorzystywany jest strukturalny
język zapytań `SQL`_. Jest on m.in. przedmiotem nauki na lekcjach informatyki
na poziomie rozszerzonym w szkołach ponadgimnazjalnych. Używając Pythona
można łatwo i efektywnie pokazać używanie SQL-a, zarówno z poziomu wiersza
poleceń, jak również z poziomu aplikacji internetowych WWW. Na początku
zajmiemy się skryptem konsolowym, co pozwala przećwiczyć "surowe" polecenia SQL-a.

.. _SQL: http://pl.wikipedia.org/wiki/SQL

Połączenie z bazą
^^^^^^^^^^^^^^^^^^^^

W ulubionym edytorze tworzymy plik `sqlraw.py` i umieszczamy w nim poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw01.py
    :linenos:

Przede wszystkim importujemy moduł `sqlite3` do obsługi baz SQLite3. Następnie w zmiennej ``con``
tworzymy połączenie z bazą danych przechowywaną w pliku na dysku (``test.db``, nazwa pliku
jest dowolona) lub w pamięci, jeśli podamy ``':memory:'``. Kolejna instrukcja ustawia właściwość
``row_factory`` na wartość ``sqlite3.Row``, aby możliwy był dostęp do kolumn (pól tabel) nie tylko
przez indeksy, ale również przez nazwy. Jest to bardzo przydatne podczas odczytu danych.

Aby móc wykonywać operacje na bazie, potrzebujemy obiektu tzw. kursora, tworzymy go
poleceniem ``cur = con.cursor()``. I tyle potrzeba, żeby rozpocząć pracę z bazą.
Skrypt możemy uruchomić poleceniem podanym niżej, ale na razie nic się jeszcze nie stanie...

.. code:: bash

    ~ $ python sqlraw.py

Model bazy
^^^^^^^^^^^^^^^^^^^^

Zanim będziemy mogli wykonywać podstawowe operacje na bazie danych określane skrótem
:term:`CRUD` – *Create* (tworzenie), *Read* (odczyt), *Update* (aktualizacja), *Delete* (usuwanie) -
musimy utworzyć tabele i relacje między nimi według zaprojektowanego schematu.
Do naszego pliku dopisujemy więc następujący kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw02.py
    :linenos:
    :lineno-start: 16
    :lines: 16-

Jak widać pojedyncze polecenia SQL-a wykonujemy za pomocą metody ``.execute()`` obiektu kursora.
Warto zwrócić uwagę, że w zależności od długości i stopnia skomplikowania instrukcji SQL,
możemy je zapisywać w różny sposób. Proste polecenia podajemy w cudzysłowach, bardziej
rozbudowane lub kilka instrukcji razem otaczamy potrójnymi cudzysłowami. Ale uwaga:
wiele instrukcji wykonujemy za pomocą metody ``.executescript()``.

Powyższe polecenia SQL-a tworzą dwie tabele. Tabela "klasa" przechowuje nazwę i profil klasy,
natomiast tabela "uczen" zawiera pola przechowujące imię i nazwisko ucznia oraz identyfikator
klasy (pole "klasa_id", tzw. klucz obcy), do której należy uczeń. Między tabelami zachodzi
relacja jeden-do-wielu, tzn. do jednej klasy może chodzić wielu uczniów.

Po wykonaniu wprowadzonego kodu w katalogu ze skryptem powinien pojawić się plik ``test.db``,
czyli nasza baza danych. Możemy sprawdzić jej zawartość przy użyciu wspomnianego interpretera
``sqlite3`` (``sqlite3.exe`` w Windows).

.. note::

    W katalogu z bazą danych wydajemy polecenie ``sqlite3 test.db``, w ten sposób wczytujemy
    bazę do interpretera. Do dyspozycji mamy polecenia:
    
    - ``.databases`` – pokazuje aktualną bazę danych;
    - ``.schema`` – pokazuje schemat bazy danych, czyli polecenia SQL tworzące tabele i relacje;
    - ``.table`` – pokaże tabele w bazie;
    - ``.quit`` – wychodzimy z powłoki interpretera.
    
    Możemy również wydawać wszelkie polecenia SQL-a operujące na bazie, np.
    ``SELECT * FROM klasa;`` – polecenia te zawsze kończymy średnikiem.

.. figure:: sqlite3.png

Wstawianie danych
^^^^^^^^^^^^^^^^^^^^

Do skryptu dopisujemy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw03.py
    :linenos:
    :lineno-start: 36
    :lines: 36-

Do wstawiania pojedynczych rekordów używamy odpowiednich poleceń SQL-a jako
argumentów wspominanej metody ``.execute()``, możemy też dodawać wiele rekordów
na raz posługując się funkcją ``.executemany()``. Zarówno w jednym, jak i drugim
przypadku wartości pól nie należy umieszczać bezpośrednio w zapytaniu SQL
ze względu na możliwe błędy lub ataki typu `SQL injection <http://pl.wikipedia.org/wiki/SQL_injection>` ("wstrzyknięcia" kodu SQL).
Zamiast tego używamy zastępników (ang. *placeholder*) w postaci znaków zapytania.
Wartości przekazujemy w tupli lub tuplach jako drugi argument.

Warto zwrócić uwagę, na trudności wynikające z relacyjnej struktury bazy danych.
Aby dopisać informacje o uczniach do tabeli "Uczeń", musimy znać identyfikator
(klucz podstawowy) klasy. Bezpośrednio po zapisaniu danych klasy, możemy go uzyskać
dzięki funkcji ``.lastrowid()``, która zwraca ostatni *rowid* (unikalny identyfikator rekordu),
ale tylko po wykonaniu pojedynczego polecenia *INSERT*. W innych przypadkach
trzeba wykonać kwerendę SQL z odpowiednim warunkiem *WHERE*, w którym również
stosujemy zastępniki.

Metoda ``.fechone()`` kursora zwraca listę zawierającą pola wybranego rekordu.
Jeżeli interesuje nas pierwszy, i w tym wypadku jedyny, element tej listy dopisujemy ``[0]``.

.. note::

    - Wartość ``NULL`` w poleceniach SQL-a i ``None`` w tupli z danymi uczniów
      odpowiadające kluczom głównym umieszczamy po to, aby baza danych utworzyła
      je automatycznie. Można by je pominąć, ale wtedy w poleceniu wstawiania danych
      musimy wymienić nazwy pól,
      np. ``INSERT INTO klasa (nazwa, profil) VALUES (?, ?), ('1C', 'biologiczny')``.
    
    - Jeżeli podajemy jedną wartość w tupli jako argument metody .execute(), musimy
      pamiętać o umieszczeniu dodatkowgo przecinka, np. ``('1A',)``, ponieważ
      w ten sposób tworzymy w Pythonie 1-elementowe tuple. W przypadku wielu
      wartości przecinek nie jest wymagany.

Metoda ``.commit()`` zatwierdza, tzn. zapisuje w bazie danych, operacje danej transakcji,
czyli grupy operacji, które albo powinny zostać wykonane razem, albo powinny
zostać odrzucone ze względu na naruszenie zasad `ACID`_ (Atomicity, Consistency,
Isolation, Durability – Atomowość, Spójność, Izolacja, Trwałość).

.. _ACID: http://pl.wikipedia.org/wiki/Transakcja_%28informatyka%29

Pobieranie danych
^^^^^^^^^^^^^^^^^^^^

Pobieranie danych (czyli :term:`kwerenda`) wymaga polecenia *SELECT* języka SQL.
Dopisujemy więc do naszego skryptu funkcję, która wyświetli listę uczniów oraz
klas, do których należą: 

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw04.py
    :linenos:
    :lineno-start: 57
    :lines: 57-

Funkcja ``czytajdane()`` wykonuje zapytanie SQL pobierające wszystkie dane z dwóch
powiązanych tabel: "uczen" i "klasa". Wydobywamy *id ucznia*, *imię* i *nazwisko*,
a także *nazwę* klasy na podstawie warunku w klauzuli *WHERE*. Wynik, czyli wszystkie
pasujące rekordy zwrócone przez metodę ``.fetchall()``, zapisujemy w zmiennej ``uczniowie``
w postaci tupli. Jej elementy odczytujemy w pętli ``for`` jako listę ``uczen``.
Dzięki ustawieniu właściwości ``.row_factory`` połączenia z bazą na ``sqlite3.Row``
odczytujemy poszczególne pola podając nazwy zamiast indeksów, np. ``uczen['imie']``.

Modyfikacja i usuwanie danych
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do skryptu dodajemy jeszcze kilka linii:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw05.py
    :linenos:
    :lineno-start: 67
    :lines: 67-

Aby zmienić przypisanie ucznia do klasy, pobieramy identyfikor klasy za pomocą
metody ``.execute()`` i polecenia *SELECT* SQL-a z odpowiednim warunkiem.
Póżniej konstruujemy zapytanie *UPDATE* wykorzystując zastępniki i wartości
przekazywane w tupli (zwróć uwagę na dodatkowy przecinek(!)) – w efekcie zmieniamy
przypisanie ucznia do klasy.

Następnie usuwamy dane ucznia o identyfikatorze 3, używając polecenia SQL
*DELETE*. Wywołanie funkcji ``czytajdane()`` wyświetla zawartość bazy po zmianach.

Na koniec zamykamy połącznie z bazą, wywołując metodę ``.close()``, dzięki
czemu zapisujemy dokonane zmiany i zwalniamy zarezerwowane przez skrypt zasoby.

Dane z pliku
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dane z tabel w bazach MS Accessa lub LibreOffice Base'a możemy eksportować
do formatu *csv*, czyli pliku tekstowego, w którym każda linia repreazentuje
pojedynczy rekord, a wartości pól oddzielone są jakimś separatorem, najczęściej
przecinkiem. Załóżmy więc, że mamy plik ``uczniowie.csv`` zawierający dane uczniów
w formacie: ``Jan,Nowak,2``.

Przed metodą ``.close()`` zamykającą połączenie z bazą dopiszmy następujący kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw06.py
    :linenos:
    :lineno-start: 77
    :lines: 77-95

Na początku funkcji ``czytaj_dane()`` sprawdzamy, czy istnieje plik
podany jako argumet. Wykorzystujemy metodę ``isfile()`` z modułu ``os``,
który należy wcześniej zaimportować. Następnie w konstrukci ``with``
otwieramy plik i wczytujemy jego treść do zmiennej ``zawartosc``.
Pętla ``for`` pobiera kolejne linie, które oczyszczamy ze znaków końca linii
(``.replace('\n','')``) i dekodujemy jako zapisane w standardzie *utf-8*.
Poszczególne wartości oddzielone przecinkiem wyodrębniamy (``.split(',')``)
do tupli, którą dodajemy do zdefiniowanej wcześniej tablicy (``dane.append()``).
Na koniec funkcja zwraca listę przekształconą na tuplę (a więc zagnieżdzone tuple),
która po przypisaniu do zmiennej ``uczniowie`` użyta zostanie, dokładnie
tak jak robiliśmy to już wczesniej, jako argument metody ``.executemany()``.

.. note::

    Znaki w pliku wejściowym powinny być zakodowane w standardzie ``utf-8``.

Poćwicz sam
^^^^^^^^^^^^
    
    Spróbuj napisać prosty konsolowy interfejs do zarządzania bazą danych.
    Wykorzystaj omówiony kod, aby umożliwić użytkownikowi: przeglądanie,
    wstawianie nowych danych z klawiatury, modyfikowanie i ich usuwanie.

Materiały
^^^^^^^^^^^^^

1. Dokumentacja modułu sqlite3 Pythona: https://docs.python.org/2/library/sqlite3.html
2. Dokumentacja bazy SQLite3: http://www.sqlite.org/ 
3. O języku SQL: http://pl.wikipedia.org/wiki/SQL

Systemy ORM
-------------------

Znajomość języka SQL jest oczywiście niezbędna, aby korzystać z wszystkich
możliwości baz danych, niemniej w wielu niespecjalistycznych projektach można
je obsługiwać inaczej, tj. za pomocą systemów ORM (ang. Object-Relational Mapping
– mapowanie obiektowo-relacyjne). Pozwalają one traktować tabele w sposób
obiektowy, co bywa wygodniejsze w budowaniu logiki aplikacji.

Używanie systemów ORM, takich jak :term:`Peewee` czy :term:`SQLAlchemy`,
w prostych projektach sprowadza się do schematu, który poglądowo można opisać
w trzech krokach:

1. Nawiązanie połączenia z bazą
2. Deklaracja modelu opisującego bazę i utworzenie struktury bazy
3. Wykonywanie operacji :term:`CRUD`

Poniżej spróbujemy pokazać, jak operacje wykonywane przy użyciu wbudowanego
w Pythona modułu sqlite3, zrealizować przy użyciu technik ORM.

.. note::

    Wyjaśnienia podanego niżej kodu są w wielu miejscach uproszczone,
    ze względu na przejrzystość i poglądowość instrukcji nie wgłębiamy
    się w techniczne różnice w implementacji technik ORM w obydwu omawianych
    rozwiązaniach. Również terminy, których używamy, nie zawsze ściśle
    odpowiadają opisywanym mechanizmom.

Połączenie z bazą
^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <div class="code_no">Peewee nr <script>var code_no2 = code_no2 || 1; document.write(code_no2++);</script></div>

.. literalinclude:: ormpw01.py
    :linenos:

.. raw:: html

    <div class="code_no">SQLAlchemy nr <script>var code_no3 = code_no3 || 1; document.write(code_no3++);</script></div>

.. literalinclude:: ormsa01.py
    :linenos:

W jednym i drugim przypadku importujemy najpierw potrzebne klasy.
Następnie tworzymy instancje ``baza`` służące do nawiązania połączeń
z bazą przechowywaną w pliku ``test.db``. Jeżeli zamiast nazwy pliku,
podamy ``:memory:`` bazy umieszczone zostaną w pamięci RAM (przydatne
podczas testowania).

.. note::
    
    Moduły ``os`` i ``sys`` nie są niezbędne do działania prezentowanego kodu,
    ale można z nich skorzystać, kiedy chcemy sprawdzić obecność pliku na
    dysku (``os.path.ispath()``) lub zatrzymać wykonywanie skryptu w dowolnym
    miejscu (``sys.exit()``). W podanych przykładach usuwamy plik bazy,
    jeżeli znajduje się na dysku, aby zapewnić bezproblemowe działanie
    kompletnych skryptów.

Model danych i baza
^^^^^^^^^^^^^^^^^^^^^

Przez model rozumiemy tutaj definicje tablic, pól, ich typów oraz wzajemnych
relacji za pomocą podejścia obiektowego, czyli deklaracji klas i ich właściwości (atrybutów).
Wzajemne powiązanie klas i ich właściwości z tabelami i kolumnami w bazie stanowi
właśnie istotę mapowania relacyjno-obiektowego, a systemy ORM zapewniają
mechanizmy obsługujące te związki.

.. raw:: html

    <div class="code_no">Peewee nr <script>var code_no2 = code_no2 || 1; document.write(code_no2++);</script></div>

.. literalinclude:: ormpw02.py
    :linenos:
    :lineno-start: 12
    :lines: 12-29

.. raw:: html

    <div class="code_no">SQLAlchemy nr <script>var code_no3 = code_no3 || 1; document.write(code_no3++);</script></div>

.. literalinclude:: ormsa02.py
    :linenos:
    :lineno-start: 14
    :lines: 14-34

W obydwu przypadkach deklarowanie modelu opiera się na pewnej "klasie" podstawowej,
którą nazwaliśmy ``BazaModel``. Dziedzicząc z niej, deklarujemy następnie
własne klasy o nazwach *Klasa* i *Uczen* reprezentujące tabele w bazie.
Właściwości tych klas odpowiadają kolumnom; w SQLAlchemy używamy nawet
klasy o nazwie ``Column()``, która wyraźnie wskazuje na rodzaj tworzonego atrybutu.
Obydwa systemy wymagają określenia *typu danych* definiowanych pól. Służą temu odpowiednie
klasy, np. ``CharField()`` lub ``String()``. Możemy również definiować dodatkowe
cechy pól, takie jak np. nie zezwalanie na wartości puste (``null=False`` lub ``nullable=False``)
lub określenie wartości domyślnych (``default=''``).

Warto zwrócić uwagę, na sposób określania relacji. W *Peewee* używamy 
konstruktora klasy: ``ForeignKeyField(Klasa, related_name = 'uczniowie')``.
Przyjmuje on nazwę klasy powiązanej, z którą tworzymy relację, i nazwę atrybutu
określającego relację zwrotną w powiązanej klasie. Dzięki temu
wywołanie w postaci ``Klasa.uczniowie`` da nam dostęp do obiektów
reprezentujących uczniów przypisanych do danej klasy. Zuważmy, że *Peewee*
nie wymaga definiowania kluczy głównych, są tworzone automatycznie
pod nazwą ``id``.

W SQLAlchemy dla odmiany nie tylko jawnie określamy klucze główne
(``primary_key=True``), ale i podajemy nazwy tabel (``__tablename__ = 'klasa'``).
Klucz obcy oznaczamy odpowiednim parametrem w klasie definiującej pole
(``Column(Integer, ForeignKey('klasa.id'))``). Relację zwrotną
tworzymy za pomocą konstruktora ``relationship('Uczen', backref='klasa')``,
w którym podajemy nazwę powiązanej klasy i nazwę atrybutu tworzącego
powiązanie. W tym wypadku wywołanie typu ``uczen.klasa`` udostępni obiekt
reprezentujący klasę, do której przypisano ucznia.

Po zdefiniowaniu przemyślanego modelu, co jest relatywnie najtrudniejsze, 
trzeba przetestować działanie mechanizmów ORM w praktyce, czyli utworzyć
tabele i kolumny w bazie. W ``Peewee`` łączymy się z bazą i wywołujemy
metodę ``.create_tables()``, której podajemy nazwy klas reprezentujących
tabele. Dodatkowy parametr ``True`` powoduje sprawdzenie przed utworzeniem,
czy tablic w bazie już nie ma. SQLAlchemy wymaga tylko wywołania metody
``.create_all()`` kontenera metadata zawartego w klasie bazowej.

Podane kody można już uruchomić, oba powinny utworzyć bazę ``test.db``
w katalogu, z którego uruchamiamy skrypt.

.. note::

    Wspominaliśmy już o interpreterze ``sqlite3`` pozwalającym pracować
    w konsoli z bazą. Warto go wykorzystać i sprawdzić, jak wygląda
    kod tworzący tabele wygenerowany przez ORM-y. Poniżej przykład
    ilustrujący SQLAlchemy.

.. figure:: sqlite3_2.png

Pojęcia
^^^^^^^^^^^^^

.. glossary::

    SQL
        strukturalny język zapytań używany do tworzenia i zarządzania bazą danych.

    SQLite3
        silnik bezserwerowej, nie wymagającej dodatkowej konfiguracji, transakcyjnej bazy danych
        implementującej standard SQL.

    CRUD
        skrót opisujący podstawowe operacje na bazie danych z wykorzystaniem języka SQL,
        *Create* (tworzenie) odpowiada zapytaniom *INSERT*, *Read* (odczyt) - zapytaniom
        *SELECT*, *Update* (aktualizacja) - *UPDATE*, *Delete* (usuwanie) - *DELETE*.

    Transakcja
        zbiór powiązanych logicznie operacji na bazie danych, który powinien być
        albo w całości zapisany, albo odrzucony ze względu na naruszenie zasad
        spójności (ACID).

    ACID
        Atomicity, Consistency, Isolation, Durability – Atomowość, Spójność, Izolacja, Trwałość;
        zasady określające kryteria poprawnego zapisu danych w bazie.
        Zob.: http://pl.wikipedia.org/wiki/ACID
        
    kwerenda
        Zapytanie do bazy danych zazwyczaj w oparciu o dodatkowe kryteria,
        którego celem jest wydobycie z bazy określonych danych lub ich modyfikacja.

    obiekt
        podstawowe pojęcie programowania obiektowego, struktura zawierająca
        dane i metody (funkcje), za pomocą których wykonuje ṣię na nich operacje.

    klasa
        definicja obiektu zawierająca opis struktury danych i jej interfejs
        (metody).

    instancja
        obiekt stworzony na podstawie klasy.

    ORM
        (ang. Object-Relational Mapping) – mapowanie obiektowo-relacyjne,
        czyli sposób odwzorowania obiektów na struktury bazy danych.
        
    Peewee
        prosty i mały system ORM, wspiera Pythona w wersji 2 i 3, obsługuje
        bazy SQLite3, MySQL, Posgresql.
    
    SQLAlchemy
        rozbudowany zestaw narzędzi i system ORM umożliwiający wykorzystanie
        wszystkich możliwości SQL-a, obsługuje bazy SQLite3, MySQL, Postgresql,
        Oracle, MS SQL Server i inne.

Źródła
^^^^^^^^^^^^^

* :download:`sqlraw.zip <sqlraw.zip>`

Kolejne wersje tworzenego kodu znajdziesz w katalogu ``~/python101/docs/bazy``.
Uruchamiamy je wydając polecenia:

.. code-block:: bash

    ~/python101$ cd docs/bazy
    ~/python101/docs/bazy$ python sqlraw0x.py

\- gdzie *x* jest numerem kolejnej wersji kodu (1-6).

Metryka
^^^^^^^

:Autorzy: Robert Bednarz (ecg@ecg.vot.pl)

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>


.. include:: ../copyright.rst
