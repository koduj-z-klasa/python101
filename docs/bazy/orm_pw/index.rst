.. _orm_peewee:

System ORM Peewee
#################

Używanie systemów ORM, takich jak :term:`Peewee`, w prostych projektach
sprowadza się do schematu, który poglądowo można opisać w trzech krokach:

1. deklaracja modelu opisującego bazę
2. utworzenie na podstawie modelu tabel w bazie,
3. wykonywanie operacji :term:`CRUD`.

Przez model (zob. też: :term:`model bazy danych`) rozumiemy tutaj deklaracje klas i ich właściwości (atrybutów)
opisujące obiekty, które będą przechowywane w bazie. Systemy ORM na podstawie klas tworzą
odpowiednie tabele i pola, uwzględniając ich typy i powiązania. Odwzorowanie klas i ich właściwości
na tabele, kolumny i relacje w bazie stanowi istotę mapowania relacyjno-obiektowego.

Poniżej spróbujemy pokazać, jak wykonywać typowe operacje na bazie z wykorzystaniem biblioteki Peewee.

.. note::

    Wyjaśnienia podanego niżej kodu są uproszczone ze względu na przejrzystość i poglądowość instrukcji.
    Do używania systemów ORM wystarczające jest poznanie ich interfejsu API.

Środowisko pracy
================

Do tworzenia aplikacji możesz użyć dowolnych narzędzi, np. terminala i ulubionego edytora kodu.
Sugerujemy jednak wykorzystanie środowiska **PyCharm** lub innego, ponieważ w ułatwiają pracę nad projektami
w języku Python.

Przed rozpoczęciem pracy przygotuj w wybranym katalogu, np. :file:`baza_orm`` :ref:`wirtualne środowisko Pythona <venv>`
i w aktywnym środowisku zainstaluj pakiet *Peewee*:

.. code-block:: bash

    (.venv) ~/baza_orm$ pip install peewee

Klasa bazowa
************

W ulubionym edytorze utwórz plik o nazwie :file:`orm_pw.py` z następującym kodem:

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 1
    :lines: 1-16

Na początku importujemy potrzebne klasy. Dalej tworzymy zmienną ``plik_bazy``,
która będzie przechowywała nazwę pliku z bazą danych.
Jeżeli plik znajduje się na dysku (``if os.path.exists()``), usuwamy go (os.remove()),
aby zapewnić bezproblemowe działanie skryptu podczas wielokrotnego uruchamiania.

Następnie tworzymy obiekt ``baza`` do obsługi bazy SQlite3 przechowywanej w pliku :file:`baza_pw.db`.

.. tip::

    Jeżeli zamiast nazwy pliku, podamy argument ``:memory:``, baza utworzona zostanie w pamięci RAM,
    co może być przydatne podczas testowania.

Do utworzenia modeli danych potrzebna będzie **klasa bazowa**, którą tworzymy w oparciu o klasę ``Model``,
w podklasie ``Meta`` dodatkowo przypisujemy obiekt służący do komunikacji z bazą do atrybutu ``database``.

Model danych
*************

Dodajemy definicje klas opisujących dwa obiekty reprezentujące klasę i ucznia. Każda klasa ma swoją nazwę
i profil, każdy uczeń ma imię, nazwisko oraz przynależy do jakiejś klasy.

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 18
    :lines: 18-32

Deklarowanie modelu opiera się na dziedziczonej klasie podstawowej ``Base``.
Klasy o nazwach ``Klasa`` i ``Uczen`` reprezentują tabele w bazie. Właściwości tych klas odpowiadają polom.
Każde pole jest instancją klasy określającej typ danych i ma ograniczenia podawane jako dodatkowe argumenty
konstruktora:

- ``CharFiled()`` – klasa definiująca pole zawierające ciąg znaków,
- ``null=False`` – ograniczenie, pole nie może zawierać wartości ``NULL``,
- ``default=''`` – ograniczenie, wartość domyślna przechowywana w polu,
- ``ForeignKeyField()`` – klasa definiująca relację, konstruktor otrzymuje nazwę klasy powiązanej,
  z którą tworzymy relację, oraz nazwę atrybutu określającego relację zwrotną w powiązanej klasie;
  dzięki temu wywołanie w postaci ``Klasa.uczniowie`` da nam dostęp do obiektów reprezentujących
  uczniów przypisanych do danej klasy.

Po zdefiniowaniu modelu, co jest relatywnie najtrudniejsze, trzeba go przetestować,
czyli utworzyć tabele i kolumny w bazie. W Peewee łączymy się z bazą (``baza.connect()``)
i wywołujemy metodę ``create_tables()``, której podajemy w liście nazwy klas reprezentujących tabele.

Omówiony kod można już uruchomić, w katalogu, z którego uruchamiamy skrypt, powinien zostać utworzony
plik bazy :file:`baza_pw.db`.

Ćwiczenie
==========

1) Wykorzystaj :ref:`interpreter sqlite3 <sqlite3>` i sprawdź, czy zostały utworzone tabele,
   czyli jak wygląda kod SQL wygenerowany przez ORM. Przykładowy zrzut poniżej.

.. figure:: sqlite3_2.png

.. note::

    Nazwy utworzonych tabel to nazwy klas, które je opisują, podobnie nazwy pól odpowiadają nazwom atrybutów.
    Warto zauważyć, że *Peewee* nie wymaga definiowania kluczy głównych, są tworzone automatycznie
    jako pola o nazwie ``id`` zawierające liczby całkowite.

Dodawanie danych
****************

Dodawanie (ang. *create*) danych w Peewee wykonywane jest za pomocą obiektów
reprezentujących rekordy zdefiniowanych tabel oraz ich metod.

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 33
    :lines: 33-46

Metoda ``create()`` modelu służy do utworzenia jego instancji (obiektu) i zapisania odpowiedniego rekordu w bazie,
czyli wykonania klauzuli ``INSERT`` języka SQL. Nazwane argumenty metody odpowiadają atrybutom modelu:
``klasa = '1A', profil = 'matematyczny')``.

Innym sposobem jest utworzenie instancji modelu i zapisanie obiektu w bazie jako rekordu za pomocą metody ``.save()``.

Można również dodawać wiele rekordów na raz. Tworzymy listę słowników ``uczniowie``. Każdy słownik zawieraja dane
w formacie "klucz":"wartość", przy czym klucze są nazwami atrybutów klasy. Wartością klucza ``'klasa'`` jest
instancja modelu ``Klasa``.

Następnie za pomocą metody ``insert_many()``, której jako argument podajemy przygotowaną listę słowników,
dodajemy rekordy z danymi wielu uczniów do bazy.

Odczyt danych
*************

Odczyt danych może być realizowany na wiele sposobów. Zacznijmy od uzupełnienia kodu skryptu:

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 47
    :lines: 47-72

Do odczytywaniu wielu rekordów służy metoda ``select()`` modelu, która zwraca listę obiektów
zapisanych w bazie. Listę możemy odczytać za pomocą pętli, np.: ``for klasa in klasy:``.
Mamy również dostęp do atrybutów odczytywanych obiektów, możemy je wypisać dzięki notacji z kropką:
``print(klasa.id, klasa.nazwa, klasa.profil)``.

Do odczytania jednego rekordu (obiektu) z bazy danych na podstawie wartości któregoś z jego atrybutów,
możemy użyć metody ``where()``, która odpowiada klauzuli warunkowej ``WHERE`` języka SQL, np.:
``Klasa.select().where(Klasa.nazwa == '1A').get()``. Dopóki interesuje nas jeden rekord z jednej tabeli,
możemy też użyć skróconego zapytania: ``klasa = Klasa.get(Klasa.nazwa == '1A')``.

W funkcji ``wypisz_liste_uczniow()`` do sprawdzenia liczby obiektów zapisanych w bazie używamy metody ``count()``.
Jeżeli w bazie zapisano jakichś uczniów (``if Uczen().select().count():``),
pobieramy ich dane używając złączenia z modelem ``Klasa``.
Używamy metody ``join()``, która odpowiada klauzuli ``INNER JOIN`` języka SQL:
``Uczen.select().join(Klasa)``. Zwróconą listę rekordów odczytujemy za pomocą pętli ``for``.
Jeżeli w bazie nie ma żadnych uczniów, wypisujemy odpowiedni komunikat.

Modyfikowanie danych
********************

Systemy ORM ułatwiają modyfikowanie danych w bazie, ponieważ operacja ta polega
na zmianie wartości pól wybranego obiektu. W naszym skrypcie dopisujemy kod:

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 73
    :lines: 73-80

Na początku odczytujemy obiekt klasy ``Uczen`` o podanym identyfikatorze oraz obiekt klasy ``Klasa`` o podanej nazwie.
Następnie atrybutowi ``klasa`` obiektu reprezentującego ucznia przypisujemy obiekt klasy:
``uczen.klasa = nowa_klasa``. Na koniec zapisujemy zmiany w bazie za pomocą metody ``save()``.

Usuwanie danych
****************

Do skryptu dodajemy poniższy kod:

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 87
    :lines: 87-

Za pomocą kwerendy warunkowej odczytujemy obiekt ucznia o identyfikatorze "3",
a następnie wywołujemy metodę ``delete_instance()``, która usuwa obiekt z bazy.

Do usuwania wielu rekordów służy metoda ``delete()`` modelu połączona z metodą ``where()``,
która pozwala wskazać rekordy do usunięcia. Należy pamiętać, żeby po utworzeniu
zapytania wykonać go za pomocą metody ``execute()``.

Po zakończeniu operacji wykonywanych na danych powinniśmy pamiętać o zamknięciu połączenia.
Robimy to używając metody obiektu bazy ``baza.close()``.

Zadania
********

1) Spróbuj dodać do bazy korzystając z systemu Peewee wiele rekordów na raz pobranych z pliku
   :download:`uczniowie.csv <uczniowie.csv>`.
   Wykorzystaj i zmodyfikuj funkcję ``pobierz_dane()`` opisaną w materiale :ref:`Dane z pliku <dane_z_pliku>`.

2) Dodaj do aplikacji konsolowy interfejs, który umożliwi operacje
   odczytu, zapisu, modyfikowania i usuwania rekordów.
   Dane powinny być pobierane z klawiatury od użytkownika.

3) Przedstawione rozwiązania warto użyć w aplikacjach internetowych
   jako relatywnie szybki i łatwy sposób obsługi danych. Zobacz,
   jak to zrobić na przykładzie scenariusza aplikacji :ref:`Quiz ORM <quiz-orm>`.

4) Przejrzyj scenariusz aplikacji internetowej :ref:`Czat <czat1>`, zbudowanej z użyciem
   frameworku *Django*, korzystającego z własnego modelu ORM.
