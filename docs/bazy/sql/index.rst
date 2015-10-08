.. _sql_raw:

SQL
##################

.. contents::
    :depth: 1
    :local:

Jak wiadomo, do obsługi bazy danych wykorzystywany jest strukturalny
język zapytań `SQL`_. Jest on m.in. przedmiotem nauki na lekcjach informatyki
na poziomie rozszerzonym w szkołach ponadgimnazjalnych. Używając Pythona
można łatwo i efektywnie pokazać używanie SQL-a, zarówno z poziomu wiersza
poleceń, jak również z poziomu aplikacji internetowych WWW. Na początku
zajmiemy się skryptem konsolowym, co pozwala przećwiczyć "surowe" polecenia SQL-a.

.. _SQL: http://pl.wikipedia.org/wiki/SQL

Połączenie z bazą
***********************

W ulubionym edytorze tworzymy plik :file:`sqlraw.py` i umieszczamy w nim poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw01.py
    :linenos:

Przede wszystkim importujemy moduł ``sqlite3`` do obsługi baz SQLite3. Następnie w zmiennej ``con``
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
***********************

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

Po wykonaniu wprowadzonego kodu w katalogu ze skryptem powinien pojawić się plik :file:`test.db`,
czyli nasza baza danych. Możemy sprawdzić jej zawartość przy użyciu interpretera :ref:`interpretera sqlite3 <sqlite3>`.

Wstawianie danych
***********************

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
***********************

Pobieranie danych (czyli :term:`kwerenda`) wymaga polecenia *SELECT* języka SQL.
Dopisujemy więc do naszego skryptu funkcję, która wyświetli listę uczniów oraz
klas, do których należą:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw04.py
    :linenos:
    :lineno-start: 58
    :lines: 58-

Funkcja ``czytajdane()`` wykonuje zapytanie SQL pobierające wszystkie dane z dwóch
powiązanych tabel: "uczen" i "klasa". Wydobywamy *id ucznia*, *imię* i *nazwisko*,
a także *nazwę* klasy na podstawie warunku w klauzuli *WHERE*. Wynik, czyli wszystkie
pasujące rekordy zwrócone przez metodę ``.fetchall()``, zapisujemy w zmiennej ``uczniowie``
w postaci tupli. Jej elementy odczytujemy w pętli ``for`` jako listę ``uczen``.
Dzięki ustawieniu właściwości ``.row_factory`` połączenia z bazą na ``sqlite3.Row``
odczytujemy poszczególne pola podając nazwy zamiast indeksów, np. ``uczen['imie']``.

Modyfikacja i usuwanie danych
=============================

Do skryptu dodajemy jeszcze kilka linii:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw05.py
    :linenos:
    :lineno-start: 71
    :lines: 71-

Aby zmienić przypisanie ucznia do klasy, pobieramy identyfikor klasy za pomocą
metody ``.execute()`` i polecenia *SELECT* SQL-a z odpowiednim warunkiem.
Póżniej konstruujemy zapytanie *UPDATE* wykorzystując zastępniki i wartości
przekazywane w tupli (zwróć uwagę na dodatkowy przecinek(!)) – w efekcie zmieniamy
przypisanie ucznia do klasy.

Następnie usuwamy dane ucznia o identyfikatorze 3, używając polecenia SQL
*DELETE*. Wywołanie funkcji ``czytajdane()`` wyświetla zawartość bazy po zmianach.

Na koniec zamykamy połącznie z bazą, wywołując metodę ``.close()``, dzięki
czemu zapisujemy dokonane zmiany i zwalniamy zarezerwowane przez skrypt zasoby.

Zadania dodatkowe
*******************

- Przeczytaj opis przykładowej funkcji pobierającej dane z pliku tekstowego
  w formacie *csv*. W skrypcie ``sqlraw.py`` zaimportuj tę funkcję i wykorzystaj
  do pobrania i wstawienia danych do bazy.

- Postaraj się przedstawioną aplikację wyposażyć w konsolowy interfejs,
  który umożliwi operacje odczytu, zapisu, modyfikowania i usuwania rekordów.
  Dane powinny być pobierane z klawiatury od użytkownika.

- Zobacz, jak zintegrować obsługę bazy danych przy użyciu modułu *sqlite3*
  Pythona z aplikacją internetową na przykładzie scenariusza "ToDo".

Źródła
*******************

* :download:`sqlraw.zip <sqlraw.zip>`

Kolejne wersje tworzenego kodu znajdziesz w katalogu ``~/python101/docs/bazy/sql``.
Uruchamiamy je wydając polecenia:

.. code-block:: bash

    ~/python101$ cd docs/bazy/sql
    ~/python101/docs/bazy/sql$ python sqlraw0x.py

\- gdzie *x* jest numerem kolejnej wersji kodu.
