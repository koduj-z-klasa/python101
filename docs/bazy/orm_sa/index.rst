.. _orm_sqlalchemy:

System ORM SQLAlchemy
#####################

Używanie systemów ORM, takich jak :term:`SQLAlchemy`, w prostych projektach
sprowadza się do schematu, który poglądowo można opisać w trzech krokach:

1. deklaracja modelu opisującego bazę
2. utworzenie na podstawie modelu tabel w bazie,
3. wykonywanie operacji :term:`CRUD`.

Przez model (zob. też: :term:`model bazy danych`) rozumiemy tutaj deklaracje klas i ich właściwości (atrybutów)
opisujące obiekty, które będą przechowywane w bazie. Systemy ORM na podstawie klas tworzą
odpowiednie tabele i pola, uwzględniając ich typy i powiązania. Odwzorowanie klas i ich właściwości
na tabele, kolumny i relacje w bazie stanowi istotę mapowania relacyjno-obiektowego.

Poniżej spróbujemy pokazać, jak wykonywać typowe operacje na bazie z wykorzystaniem biblioteki SQLAlchemy.

.. note::

    Wyjaśnienia podanego niżej kodu są uproszczone ze względu na przejrzystość i poglądowość instrukcji.
    Do używania systemów ORM wystarczające jest poznanie ich interfejsu API.

Środowisko pracy
================

Do tworzenia aplikacji możesz użyć dowolnych narzędzi, np. terminala i ulubionego edytora kodu.
Sugerujemy jednak wykorzystanie środowiska **PyCharm** lub innego, ponieważ w ułatwiają pracę nad projektami
w języku Python.

Przed rozpoczęciem pracy przygotuj w wybranym katalogu, np. :file:`baza_orm`` :ref:`wirtualne środowisko Pythona <venv>`
i w aktywnym środowisku zainstaluj pakiet *SQLAlchemy*:

.. code-block:: bash

    (.venv) ~/baza_orm$ pip install sqlalchemy

Klasa bazowa
************

W ulubionym edytorze utwórz dwa plik o nazwie :file:`orm_sa.py`.

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_sa.py
    :linenos:
    :lineno-start: 1
    :lines: 1-17

Na początku importujemy potrzebne klasy. Dalej tworzymy zmienną ``plik_bazy``,
która będzie przechowywała nazwę pliku z bazą danych.
Jeżeli plik znajduje się na dysku (``if os.path.exists()``), usuwamy go (os.remove()),
aby zapewnić bezproblemowe działanie skryptu podczas wielokrotnego uruchamiania.

Następnie tworzymy obiekt ``baza`` do obsługi bazy SQlite3 przechowywanej w pliku :file:`baza_sa.db`.

Do utworzenia modeli danych potrzebna będzie **klasa bazowa**, którą tworzymy w oparciu o klasę
``DeclarativeBase``.

Model danych
*************

Dodajemy definicje klas opisujących dwa obiekty reprezentujące klasę i ucznia. Każda klasa ma swoją nazwę
i profil, każdy uczeń ma imię, nazwisko oraz przynależy do jakiejś klasy.

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_sa.py
    :linenos:
    :lineno-start: 18
    :lines: 18-37

Tworzenie modelu opiera się na dziedziczonej klasie podstawowej ``Base`` i mapowaniu deklaratywnym
(ang. *Declarative Mapping*). Definicje klas o nazwach ``Klasa`` i ``Uczen`` z jednej strony opisują
obiekty Pythona, z drugiej strony zawierają metainformacje opisujące tabele SQL,
które utworzone zostaną w bazie. Definicje wykorzystują również wskazówki dotyczące typów danych
(ang. *type hinst*). Przeanalizujmy kilka fragmentów kodu:

- ``__tablename__`` – określa nazwę tabeli w bazie danych,
- ``id: Mapped[int]`` – nazwa pola z adnotacją typu danych,
- ``mapped_column()`` - funkcja pozwalająca definiować ograniczenia pól tworzonych w tabelach, np.:

  - ``Integer`` – pole przechowuje liczby całkowite,
  - ``String(100)`` – pole przechowuje maksymalnie 40 znaków,
  - ``primary_key=True`` – pole jest kluczem głównym,
  - ``nullable=False`` – pole nie może zawierać wartości null,
  - ``default=''`` – domyślna wartość pola,
  - ``ForeignKey()`` – definiuje klucz obcy, jako argument podajemy nazwę tabeli i klucza głównego,

- ``relationship()`` – funkcja, która tworzy relację zwrotną między dwoma zmapowanymi klasami podanymi
  w adnotacji typu, np.: ``Mapped[List["Uczen"]]``, ``Mapped["Klasa"]``; argument ``back_populates``
  pozwala wskazać nazwę relacji w powiązanej klasie.

Relacja zwrotna pozwala na dostęp do powiązanych obiektów, np. kod typu ``klasa.uczniowie``
da nam dostęp do uczniów należących do danej klasy, a kod ``uczen.klasa`` wskaże klasę,
do której należy uczeń.

Zdefiniowane model możemy sprawdzić za pomocą kodu tworzącego tabele: ``Base.metadata.create_all(baza)``.

Omówiony kod można uruchomić. W katalogu, z którego uruchamiamy skrypt, powinien zostać utworzony
plik bazy :file:`baza_sa.db`.

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

Do pliku :file:`orm_sa.py` dodajemy następujący kod:

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_sa.py
    :linenos:
    :lineno-start: 38
    :lines: 38-57

Wykonywanie operacji na bazie danych wymaga utworzenia obiektu sesji, tworzonego w kontekście:
``with Session(baza) as sesja`` – co ułatwia pracę z bazą.

Metoda ``add()`` pozwala na tworzenie nowych rekordów. Jako argument podajemy nazwę modelu
z wymaganymi argumentami.

W ramach sesji można wykonywać wiele operacji, jednak aby zostały odzwierciedlone w bazie danych,
trzeba wywołać metodę ``commit()``.

.. note::

    Dopiero po zatwierdzeniu zmian metodą ``commit()`` mamy dostęp do identyfikatorów nowo
    utworzonych obiektów.

Metoda ``add_all()`` pozwala dodać wiele rekordów na raz. Jako argument podajemy listę obiektów.
Zwróć uwagę, w jaki sposób wskazujemy klasę do której należy uczeń.


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
odczytu klasy, do której przypisano ucznia (``inst_uczen.klasa.nazwa``),
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

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 65
    :lines: 65-

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_sa.py
    :linenos:
    :lineno-start: 67
    :lines: 67-

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

Zadania
********

- Spróbuj dodać do bazy korzystając z systemu Peewee lub SQLAlchemy
  wiele rekordów na raz pobranych z pliku. Wykorzystaj i zmodyfikuj
  funkcję ``pobierz_dane()`` opisaną w materiale :ref:`Dane z pliku <dane_z_pliku>`.

- Postaraj się przedstawione aplikacje wyposażyć w konsolowy interfejs,
  który umożliwi operacje odczytu, zapisu, modyfikowania i usuwania rekordów.
  Dane powinny być pobierane z klawiatury od użytkownika.

- Przedstawione rozwiązania warto użyć w aplikacjach internetowych
  jako relatywnie szybki i łatwy sposób obsługi danych. Zobacz,
  jak to zrobić na przykładzie scenariusza aplikacji :ref:`Quiz ORM <quiz-orm>`.

- Przejrzyj scenariusz aplikacji internetowej :ref:`Czat <czat1>`, zbudowanej z użyciem
  frameworku *Django*, korzystającego z własnego modelu ORM.

Źródła
********

* :download:`orm.zip <orm.zip>`


