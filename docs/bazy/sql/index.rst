.. _sql_raw:

SQL
##################

.. contents::
    :depth: 1
    :local:

Do obsługi bazy danych wykorzystywany jest strukturalny i deklaratywny język zapytań `SQL`_.
Jest on m.in. przedmiotem nauki na lekcjach informatyki w szkołach ponadpodstawowych na poziomie rozszerzonym.
Korzystając z Pythona można łatwo i efektywnie pokazać używanie SQL-a, zarówno w skryptach,
jak również w aplikacjach desktopowych i internetowych. W poniższym materiale pokażemy,
jak wykorzystywać język SQL w skryptach wykonywanych w wierszu poleceń.

.. _SQL: http://pl.wikipedia.org/wiki/SQL

Połączenie z bazą
*****************

W ulubionym edytorze tworzymy plik :file:`sql_raw.py` i umieszczamy w nim poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sql_raw.py
    :linenos:
    :lineno-start: 1
    :lines: 1-9

Na początku importujemy moduł Pythona ``sqlite3`` do obsługi baz SQLite3. Następnie w zmiennej ``con``
tworzymy połączenie z bazą danych przechowywaną w pliku na dysku (``baza.db``, nazwa pliku
jest dowolna) lub w pamięci RAM, jeśli podamy wartość ``':memory:'``. Kolejna instrukcja ustawia właściwość
``row_factory`` na wartość ``sqlite3.Row``, aby możliwy był dostęp do pól zwracanych rekordów nie tylko
przez indeksy, ale również przez nazwy. Jest to bardzo przydatne podczas odczytu danych.

Do wykonywania operacji na bazie potrzebujemy obiektu tzw. kursora. Tworzymy go
poleceniem ``cur = con.cursor()``. Skrypt możemy uruchomić poleceniem podanym niżej,
co spowoduje utworzenie pustej bazy danych w podanym pliku (lub pamięci RAM).

.. code:: bash

    ~$ python sql_raw.py

Model bazy
***********

Zanim będziemy mogli wykonywać podstawowe operacje na bazie danych określane skrótem
:term:`CRUD` – *Create* (tworzenie), *Read* (odczyt), *Update* (aktualizacja), *Delete* (usuwanie) -
musimy utworzyć tabele i relacje między nimi według zaprojektowanego schematu.
Do naszego pliku dopisujemy więc następujący kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sql_raw.py
    :linenos:
    :lineno-start: 10
    :lines: 10-26

Proste polecenia SQL-a umieszczamy w cudzysłowach podwójnych
i wykonujemy za pomocą metody ``.execute()`` obiektu kursora. Bardziej skomplikowane
możemy zapisywać w cudzysłowach potrójnych. Jeżeli chcemy wykonać wiele poleceń na raz,
używmy metody ``.executescript()``. Metoda ta akceptuje również polecenia SQL odczytywane
z pliku tekstowego zapisanego np. na dysku.

Polecenia SQL-a umieszczone w naszym skrypcie tworzą dwie tabele. Tabela *klasa* przechowuje nazwę i profil klasy,
natomiast tabela *uczen* zawiera pola przechowujące imię i nazwisko ucznia oraz identyfikator
klasy (pole "klasa_id"), czyli tzw. klucz obcy, do której należy uczeń. Między tabelami zachodzi
relacja jeden-do-wielu, tzn. do jednej klasy może chodzić wielu uczniów.

Po wykonaniu skryptu w katalogu ze skryptem powinien pojawić się plik bazy danych :file:`baza.db`,
zawierający puste tabele *klasa* i *uczen*.
Możemy to sprawdzić np. przy użyciu interpretera :ref:`interpretera sqlite3 <sqlite3>` lub dowolnego
innego programu odczytującego bazy SQLite3.

Dodawanie danych (INSERT)
*************************

Do skryptu dopisujemy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sql_raw.py
    :linenos:
    :lineno-start: 27
    :lines: 27-42

Do dodania jednego rekordu używamy polecenia ``INSERT`` SQL-a jako argumentu wspominanej metody ``.execute()``.
Jeżeli chcemy dodać wiele rekordów na raz, posługujemy się metodą ``.executemany()``.
Zarówno w jednym, jak i drugim przypadku wartości pól nie należy umieszczać bezpośrednio w zapytaniu SQL
ze względu na możliwe błędy lub ataki typu `SQL injection <http://pl.wikipedia.org/wiki/SQL_injection>`_
("wstrzyknięcia" kodu SQL).
Zamiast tego używamy zastępników (ang. *placeholder*) w postaci znaków zapytania.
Wartości przekazujemy w tupli lub liście tupli jako drugi argument omawianych metod.

Warto zwrócić uwagę, na trudności wynikające z relacyjnej struktury bazy danych.
Aby dopisać informacje o uczniach do tabeli ``uczen``, musimy znać identyfikator
(klucz podstawowy) klasy. Bezpośrednio po zapisaniu danych klasy, możemy go uzyskać
dzięki funkcji ``.lastrowid()``, która zwraca ostatni *rowid* (unikalny identyfikator rekordu),
ale tylko po wykonaniu pojedynczego polecenia ``INSERT``. W innych przypadkach uzyskanie identyfikatora
wymaga wykonania kwerendy wybierającej SQL z odpowiednim warunkiem, np.:
``SELECT id FORM klasa WHERE nazwa = ? AND profil = ?`` (zob. poniżej).

.. note::

    Wartość ``NULL`` (czyli wartość pusta) w poleceniach SQL-a odpowiada kluczom głównym,
    które baza SQLite utworzy automatycznie. Można by je pominąć, ale wtedy w poleceniu
    musimy wymienić nazwy pól, np. ``INSERT INTO klasa (nazwa, profil) VALUES (?, ?), ('1C', 'biologiczny')``.

Metoda ``.commit()`` zatwierdza, tzn. zapisuje w bazie danych, operacje danej transakcji,
czyli grupy operacji, które albo powinny zostać wykonane razem, albo powinny
zostać odrzucone ze względu na naruszenie zasad `ACID`_ (Atomicity, Consistency,
Isolation, Durability – Atomowość, Spójność, Izolacja, Trwałość).

.. _ACID: http://pl.wikipedia.org/wiki/Transakcja_%28informatyka%29

Pobieranie danych (SELECT)
**************************

Pobieranie danych (czyli :term:`kwerenda`) wymaga polecenia ``SELECT`` języka SQL.
Dopisujemy więc do naszego skryptu funkcję, która wyświetli listę uczniów oraz
klas, do których należą:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sql_raw.py
    :linenos:
    :lineno-start: 43
    :lines: 43-60

Funkcja ``wypisz_liste_uczniow()`` na początku wykonuje zapytanie zliczające przy użyciu funkcji ``count()``
liczbę rekordów, czyli uczniów, zapisanych w tabeli ``uczen``. Następnie metoda ``.fetchone()`` kursora
zwraca listę zawierającą pola pierwszego (i jedynego w tym przypadku) wybranego rekordu.
Dlatego dopisujemy ``[0]``.

Jeżeli w bazie są zapisane dane jakichś uczniów, wykonujemy zapytanie SQL pobierające wszystkie dane z dwóch
powiązanych tabel: ``uczen`` i ``klasa``. Odczytujemy pola *id ucznia*, *imie* i *nazwisko*,
a także *nazwa* klasy na podstawie warunku w klauzuli ``WHERE``. Wynik, czyli wszystkie
pasujące rekordy zwrócone przez metodę ``.fetchall()`` w postaci krotki, zapisujemy w zmiennej ``uczniowie``.
Jej elementy, tzn. listy pól, odczytujemy w pętli ``for`` w zmiennej ``uczen``.
Dzięki ustawieniu właściwości ``.row_factory`` połączenia z bazą na ``sqlite3.Row``
odczytujemy poszczególne pola podając nazwy zamiast indeksów, np. ``uczen['imie']``.

.. note::

  Warto zwrócić uwagę na wykorzystanie w powyższym kodzie potrójnych cudzysłowów (``"""..."""``).
  Na początku funkcji można umieścić w nich opis jej działania, dalej wykorzystujemy je
  do zapisania rozbudowanego zapytania SQL.

Modyfikacja danych (UPDATE)
***************************

Do skryptu dodajemy kod, który przepisze ucznia do innej klasy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sql_raw.py
    :linenos:
    :lineno-start: 61
    :lines: 61-68

Na początku pobieramy identyfikator ucznia za pomocą polecenia SQL ``SELECT id FROM uczen WHERE nazwisko=?``
wykonywanego przez metodę ``.execute()``. Podobnie odczytujemy identyfikator nowej klasy.

.. note::

    Jeżeli polecenie SQL wymaga jednej wartości i podajemy ją w krotce jako argument metody ``execute()``,
    musimy pamiętać o umieszczeniu dodatkowego przecinka, np. ``('Nowak',)``, ponieważ
    w ten sposób tworzymy w Pythonie 1-elementowe krotkę. W przypadku wielu wartości przecinek nie jest wymagany.

Następnie konstruujemy zapytanie ``UPDATE uczen SET klasa_id=? WHERE id=?`` wykorzystując zastępniki,
dla których wartości podajemy w krotce.

Usuwanie danych (DELETE)
************************

Do skryptu dodamy jeszcze kod, który usunie wskazany rekord z tabeli ``uczen``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sql_raw.py
    :linenos:
    :lineno-start: 69
    :lines: 69-

Do usuwania rekordów używamy polecenie SQL ``DELETE``, które wymaga wskazania rekordów do usunięcia
w klauzuli ``WHERE``. W naszym przypadku podajemy w krotce imię i nazwisko ucznia, który ma być usunięty
z bazy.

.. note::

    Powyższy przykład jest bardzo uproszczony, ponieważ w codziennych zastosowaniach wskazywanie
    ucznia do usunięcia tylko po imieniu i nazwisku mogłoby spowodować usunięcie danych wielu uczniów,
    którzy mają takie same imiona i nazwiska jak podane.

Na koniec zamykamy połączenie z bazą, wywołując metodę ``.close()``, dzięki
czemu zapisujemy dokonane zmiany i zwalniamy zarezerwowane przez skrypt zasoby.

Zadania
********

- Przeczytaj :ref:`opis przykładowej funkcji pobierającej dane <dane_z_pliku>` z pliku tekstowego
  w formacie CSV. W skrypcie ``sql_raw.py`` zaimportuj tę funkcję i wykorzystaj
  do pobrania i wstawienia danych do bazy.

- Dodaj do skryptu konsolowy interfejs,
  który umożliwi operacje odczytu, zapisu, modyfikowania i usuwania rekordów.
  Dane powinny być pobierane z klawiatury od użytkownika.

- Zobacz, jak zintegrować obsługę bazy danych przy użyciu modułu *sqlite3*
  Pythona z aplikacją internetową na przykładzie scenariusza :ref:`ToDo <todo-app>`.
