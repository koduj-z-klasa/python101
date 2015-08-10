.. _systemy_orm:

Systemy ORM
##################

.. contents::
    :depth: 1
    :local:

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

    Wyjaśnienia podanego niżej kodu są w wielu miejscach uproszczone.
    Ze względu na przejrzystość i poglądowość instrukcji nie wgłębiamy
    się w techniczne różnice w implementacji technik ORM w obydwu
    rozwiązaniach. Poznanie ich interfejsu jest wystarczające, aby
    efektywnie obsługiwać bazy danych. Co ciekawe, dopóki używamy
    bazy SQLite3, systemy ORM można traktować jako swego rodzaju
    nakładkę na owmówiony wyżej moduł *sqlite3* wbudowany w Pythona.

Połączenie z bazą
***********************

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
z bazą przechowywaną w pliku :file:`test.db`. Jeżeli zamiast nazwy pliku,
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
***********************

Przez model rozumiemy tutaj definicje tablic, pól, ich typów oraz wzajemnych
relacji za pomocą podejścia obiektowego, czyli deklaracji klas i ich właściwości (atrybutów).
Wzajemne powiązanie klas i ich właściwości z tabelami i kolumnami w bazie stanowi
właśnie istotę mapowania relacyjno-obiektowego, a systemy ORM zapewniają
mechanizmy obsługujące te związki.

.. raw:: html

    <div class="code_no">Peewee nr <script>var code_no2 = code_no2 || 1; document.write(code_no2++);</script></div>

.. literalinclude:: ormpw02.py
    :linenos:
    :lineno-start: 13
    :lines: 13-34

.. raw:: html

    <div class="code_no">SQLAlchemy nr <script>var code_no3 = code_no3 || 1; document.write(code_no3++);</script></div>

.. literalinclude:: ormsa02.py
    :linenos:
    :lineno-start: 14
    :lines: 14-37

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
tabele i kolumny w bazie. W Peewee łączymy się z bazą i wywołujemy
metodę ``.create_tables()``, której podajemy nazwy klas reprezentujących
tabele. Dodatkowy parametr ``True`` powoduje sprawdzenie przed utworzeniem,
czy tablic w bazie już nie ma. SQLAlchemy wymaga tylko wywołania metody
``.create_all()`` kontenera *metadata* zawartego w klasie bazowej.

Podane kody można już uruchomić, oba powinny utworzyć bazę ``test.db``
w katalogu, z którego uruchamiamy skrypt.

.. note::

    Warto wykorzystać :ref:`interpreter sqlite3 <sqlite3>`
    i sprawdzić, jak wygląda kod tworzący tabele wygenerowany przez ORM-y.
    Poniżej przykład ilustrujący SQLAlchemy.

.. figure:: sqlite3_2.png

Operacje CRUD
***********************

Wstawianie i odczytywanie danych
=================================

Podstawowe operacje wykonywane na bazie, np, wstawianie i odczytywanie danych,
w Peewee wykonywane są za pomocą obiektów reprezentujących rekordy
zdefiniowanych tabel oraz ich metod. W SQLAlchemy oprócz obiektów
wykorzystujemy metody sesji, w ramach której komunikujemy się z bazą.

.. raw:: html

    <div class="code_no">Peewee nr <script>var code_no2 = code_no2 || 1; document.write(code_no2++);</script></div>

.. literalinclude:: ormpw03.py
    :linenos:
    :lineno-start: 36
    :lines: 36-62

.. raw:: html

    <div class="code_no">SQLAlchemy nr <script>var code_no3 = code_no3 || 1; document.write(code_no3++);</script></div>

.. literalinclude:: ormsa03.py
    :linenos:
    :lineno-start: 39
    :lines: 39-64

Dodawanie informacji w systemach ORM polega na utworzeniu instancji odpowiedniego
obiektu i podaniu w jego konstruktorze wartości atrybutów reprezentujących pola rekordu:
``Klasa(nazwa = '1A', profil = 'matematyczny')``. Utworzony rekord zapisujemy metodą
``.save()`` obiektu w Peewee lub metodą ``.add()`` :ref:`sesji <sesja>` w SQLAlchemy.
Można również dodawać wiele rekordów na raz. Peewee oferuje metodę ``.insert_many()``,
która jako parametr przyjmuje listę słowników zawierających dane w formacie
"klucz":"wartość", przy czym kluczem jest nazwa pola klasy (tabeli).
SQLAlchemy ma metodę ``.add_all()`` wymagającą listy konstruktorów obiektów,
które chcemy dodać.

Zanim dodamy pierwsze informacje sprawdzamy, czy w tabeli *klasa* są jakieś wpisy, a więc
wykonujemy prostą kwerendę zliczającą. Peewee używa
metod odpowiednich obiektów: ``Klasa().select().count()``, natomiast
SQLAlchemy korzysta metody ``.query()`` sesji, która pozwala pobierać dane
z określonej jako klasa tabeli. Obydwa rozwiązania umożliwiają łańcuchowe
wywoływanie charakterytycznych dla kwerend operacji poprzez "doklejanie"
kolejnych metod, np. ``sesja.query(Klasa).count()``.

Tak właśnie konstruujemy kwerendy warunkowe. W Peewee definiujemy warunki jako
prametry metody ``.where(Klasa.nazwa == '1A')``. Podobnie w SQLAlchemy,
tyle, że metody sesji inaczej się nazywają i przyjmują postać
``.filter_by(nazwa = '1A')`` lub ``.filter(Klasa.nazwa == '1A')``. Pierwsza
wymaga podania warunku w formacie "klucz"="wartość", druga w postaci
wyrażenia SQL (należy uważać na użycie poprawnego operatora ``==``).

Pobieranie danych z wielu tabel połączonych relacjami może być w porównaniu
do zapytań SQL-a bardzo proste. W zależności od ORM-a wystarcza polecenie:
``Uczen.select()`` lub ``sesja.query(Uczen).all()``, ale przy próbie
odczytu klasy, do której przypisano ucznia (``uczen.klasa.nazwa``),
wykonane zostanie dodatkowe zapytanie, co nie jest efektywne.
Dlatego lepiej otwarcie wskazywać na powiązania między obiektami,
czyli w zależności od ORM-u używać:
``Uczen.select().join(Klasa)`` lub ``sesja.query(Uczen).join(Klasa).all()``.
Tak właśnie postępujemy w bliźniaczych funkcjach ``czytajdane()``, które
pokazują, jak pobierać i wyświetlać wszystkie rekordy z tabel powiązanych
relacjami.

Systemy ORM oferują pewne ułatwiania w zależności od tego, ile rekordów lub pól
i w jakiej formie chcemy wydobyć. Metody w Peewee:

    - ``.get()`` - zwraca pojedynczy rekord pasujący do zapytania lub wyjątek ``DoesNotExist``, jeżeli go brak;
    - ``.first()`` - zwróci z kolei pierwszy rekord ze wszystkich pasujących.

Metody SQLAlchemy:

    - ``.get(id)`` - zwraca pojedynczy rekord na podstawie podanego identyfikatora;
    - ``.one()`` - zwraca pojedynczy rekord pasujący do zapytania lub wyjątek ``DoesNotExist``, jeżeli go brak;
    - ``.scalar()`` - zwraca pierwszy element pierwszego zwróconego rekordu lub wyjątek ``MultipleResultsFound``;
    - ``.all()`` - zwraca pasujące rekordy w postaci listy.

.. _sesja:

.. note::

    Mechanizm sesji jest unikalny dla SQLAlchemy, pozwala m. in. zarządzać
    transakcjami i połączeniami z wieloma bazami. Stanowi "przechowalnię"
    dla tworzonych obiektów, zapamiętuje wykonywane na nich operacje,
    które mogą zostać zapisane w bazie lub w razie potrzeby odrzucone.
    W prostych aplikacjach wykorzystuje się jedną instancję sesji,
    w bardziej złożonych można korzystać z wielu.
    Instancja sesji (``sesja = BDSesja()``) tworzona jest na podstawie klasy, która z kolei
    powstaje przez wywołanie konstruktora z opcjonalnym parametrem
    wskazującym bazę: ``BDSesja = sessionmaker(bind=baza)``. Jak pokazano
    wyżej, obiekt sesji zawiera metody pozwalające komunikować się
    z bazą. Warto również zauważyć, że po wykonaniu wszystkich zamierzonych
    operacji w ramach sesji zapisujemy dane do bazy wywołując polecenie
    ``sesja.commit()``.

Modyfikowanie i usuwanie danych
=================================

Systemy ORM ułatwiają modyfikowanie i usuwanie danych z bazy, ponieważ
operacje te sprowadzają się do zmiany wartości pól klasy reprezentującej
tabelę lub do usunięcia instancji danej klasy.

.. raw:: html

    <div class="code_no">Peewee nr <script>var code_no2 = code_no2 || 1; document.write(code_no2++);</script></div>

.. literalinclude:: ormpw04.py
    :linenos:
    :lineno-start: 64
    :lines: 64-

.. raw:: html

    <div class="code_no">SQLAlchemy nr <script>var code_no3 = code_no3 || 1; document.write(code_no3++);</script></div>

.. literalinclude:: ormsa04.py
    :linenos:
    :lineno-start: 66
    :lines: 66-

Załóżmy, że chcemy zmienić przypisanie ucznia do klasy. W obydwu systemach
tworzymy więc obiekt reprezentujący ucznia o identyfikatorze "2". Stosujemy
omówione wyżej metody zapytań. W następnym kroku modyfikujemy odpowiednie
pole tworzące relację z tabelą "klasy", do którego przypisujemy
pobrany w zapytaniu obiekt (Peewee) lub identyfikator (SQLAlchemy).
Różnice, tzn. przypisywanie obiektu lub identyfikatora, wynikają ze sposobu
definiowania modeli w obu rozwiązanich.

Usuwanie jest jeszcze prostsze. W Peewee wystarczy do zapytania zwracającego
obiekt reprezentujący ucznia o podanym id "dokleić" odpowiednią metodę:
``Uczen.select().where(Uczen.id == 3).get().delete_instance()``.
W SQLAlchemy korzystamy jak zwykle z metody sesji, której przekazujemy
obiekt reprezentujący ucznia: ``sesja.delete(sesja.query(Uczen).get(3))``.

Po zakończeniu operacji wykonywanych na danych powinniśmy pamiętać o zamknięciu
połączenia, robimy to używając metody obiektu bazy ``baza.close()`` (Peewee)
lub sesji ``sesja.close()`` (SQLAlchemy). UWAGA: operacje dokonywane
podczas sesji w SQLAlchemy muszą zostać zapisane w bazie, dlatego przed
zamknięciem połączenia trzeba umieścić polecenie ``sesja.commit()``.

Zadania dodatkowe
******************

- Spróbuj dodać do bazy korzystając z systemu Peewee lub SQLAlchemy
  wiele rekordów na raz pobranych z pliku. Wykorzystaj i zmodyfikuj
  funkcję ``pobierz_dane()`` opisaną w materiale :ref:`Dane z pliku <dane_z_pliku>`.

- Postaraj się przedstawione aplikacje wyposażyć w konsolowy interfejs,
  który umożliwi operacje odczytu, zapisu, modyfikowania i usuwania rekordów.
  Dane powinny być pobierane z klawiatury od użytkownika.

- Przedstawione rozwiązania warto użyć w aplikacjach internetowych
  jako relatywnie szybki i łatwy sposób obsługi danych. Zobacz,
  jak to zrobić na przykładzie scenariusza aplikacji :ref:`Quiz ORM <quiz_orm>`.

- Przejrzyj scenariusz aplikacji internetowej :ref:`Czat <czat_app>`, zbudowanej z wykorzystaniem
  frameworku *Django*, korzystającego z własnego modelu ORM.

Źródła
*******************

* :download:`orm.zip <orm.zip>`

Kolejne wersje tworzenego kodu znajdziesz w katalogu ``~/python101/docs/bazy``.
Uruchamiamy je wydając polecenia:

.. code-block:: bash

    ~/python101$ cd docs/bazy/orm
    ~/python101/docs/bazy/orm$ python ormpw0x.py
    ~/python101/docs/bazy/orm$ python ormsa0x.py

\- gdzie *x* jest numerem kolejnej wersji kodu.

