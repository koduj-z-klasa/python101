.. _sql-orm:

SQL v. ORM
##################

.. contents::
    :depth: 1
    :local:

Bazy danych są niezbędnym składnikiem większości aplikacji. Poniżej
zwięźle pokażemy, w jaki sposób z wykorzystaniem Pythona można je obsługiwać
przy użyiu języka :term:`SQL`, jak i systemów :term:`ORM` na przykładzie rozwiązania
*Peewee*.

.. note::

    Niniejszy materiał koncentruje się na poglądowym wyeksponowaniu różnic w kodowaniu,
    komentarz ograniczono do minimum. Dokładne wyjaśnienia poszczególnych instrukcji
    znajdziesz w materiale :ref:`SQL <sql_raw>` oraz :ref:`Systemy ORM <systemy_orm>`.
    W tym ostatnim omówiono również ORM SQLAlchemy.

Połączenie z bazą
***********************

Na początku pliku :file:`sqlraw.py` umieszczamy kod, który importuje moduł do obsługi bazy *SQLite3*
i przygotowuje obiekt kursora, który posłuży nam do wydawania poleceń SQL:

.. raw:: html

    <div class="code_no">Plik <i>sqlraw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw.py
    :linenos:
    :lineno-start: 1
    :lines: 1-13

System ORM Peewee inicjujemy w pliku :file:`ormpw.py` tworząc klasę bazową, która zapewni połączenie z bazą:

.. raw:: html

    <div class="code_no">Plik <i>ormpw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: ormpw.py
    :linenos:
    :lineno-start: 1
    :lines: 1-18

.. note::

    Parametr ``:memory:`` powduje utworzenie bazy danych w pamięci operacyjnej,
    która istnieje tylko w czasie wykonywania programu. Aby utworzyć trwałą bazę,
    zastąp omawiany prametr nazwę pliku, np. :file:`test.db`.

Model bazy
***********************

Dane w bazie zorganizowane są w tabelach, połączonych najczęściej relacjami.
Aby utworzyć tabele ``klasa`` i ``uczen`` powiązane relacją jeden-do-wielu,
musimy wydać następujące polecenia SQL:

.. raw:: html

    <div class="code_no">Plik <i>sqlraw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw.py
    :linenos:
    :lineno-start: 15
    :lines: 15-30

Wydawanie poleceń SQL-a wymaga koncentracji na poprawności użycia tego języka,
systemy ORM izolują nas od takich szczegółów pozwalając skupić się na logice danych.
Tworzymy więc klasy opisujące nasze obiekty, tj. klasy i uczniów. Na podstawie
Właściwości tych obieków system ORM utworzy odpowiednie pola tabel. Konkretna klasa
lub uczeń, czyli instancje klasy, reprezentować będą rekordy w tabelach.

.. raw:: html

    <div class="code_no">Plik <i>ormpw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: ormpw.py
    :linenos:
    :lineno-start: 21
    :lines: 21-32

Ćwiczenie 1
============

Utwórz za pomocą tworzonych skryptów bazy w plikach o nazwach :file:`sqlraw.db` oraz
:file:`peewee.db`. Następnie otwórz te bazy w `interpreterze Sqlite <sqlite3>`_  i wykonaj
podane niżej polecenia. Porównaj struktury utworzonych tabel.

.. code-block:: bash

    sqlite> .tables
    sqlite> .schema klasa
    sqlite> .schema uczen

Wstawianie danych
***********************

Chcemy wstawić do naszych tabel dane dwóch klas oraz dwóch uczniów.
Korzystając z języka SQL użyjemy następujących poleceń:

.. raw:: html

    <div class="code_no">Plik <i>sqlraw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw.py
    :linenos:
    :lineno-start: 32
    :lines: 32-47

W systemie ORM pracujemy z instancjami ``inst_klasa`` i ``inst_uczen``. Nadajemy wartości ich
atrybutom i korzystamy z ich metod:

.. raw:: html

    <div class="code_no">Plik <i>ormpw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: ormpw.py
    :linenos:
    :lineno-start: 34
    :lines: 34-47

Pobieranie danych
***********************

Pobieranie danych (czyli :term:`kwerenda`) wymaga polecenia *SELECT* języka SQL.
Aby wyświetlić dane wszystkich uczniów zapisane w bazie użyjemy kodu:

.. raw:: html

    <div class="code_no">Plik <i>sqlraw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw.py
    :linenos:
    :lineno-start: 50
    :lines: 50-62

W systemie ORM korzystamy z metody ``select()`` instancji reprezentującej ucznia.
Dostęp do danych przechowywanych w innych tabelach uzyskujemy dzięki wyrażeniom
typu ``inst_uczen.klasa.nazwa``, które generuje podzapytanie zwracające obiekt
klasy przypisanej uczniowi.

.. raw:: html

    <div class="code_no">Plik <i>ormpw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: ormpw.py
    :linenos:
    :lineno-start: 50
    :lines: 50-56

.. tip::

    Ze względów wydajnościowych pobieranie danych z innych tabel możemy
    zasygnalizować już w głównej kwerendzie, używając metody ``join()``,
    np.: ``Uczen.select().join(Klasa)``.

Modyfikacja i usuwanie danych
*****************************

Edycja danych zapisanych już w bazie to kolejna częsta operacja. Jeżeli chcemy
przepisać ucznia z klasy do klasy, w przypadku czystego SQL-a musimy pobrać
identyfikator ucznia (``uczen_id = cur.fetchone()[0]``),
identyfikator klasy (``klasa_id = cur.fetchone()[0]``) i użyć ich w klauzuli ``UPDATE``.
Usuwany rekord z kolei musimy wskazać w klauzuli ``WHERE``.

.. raw:: html

    <div class="code_no">Plik <i>sqlraw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: sqlraw.py
    :linenos:
    :lineno-start: 64
    :lines: 64-

W systemie ORM tworzymy instancję reprezentującą ucznia i zmieniamy jej właściwości (``inst_uczen.klasa = Klasa.select().where(Klasa.nazwa == '1B').get()``). Usuwając dane w przypadku systemu ORM, usuwamy instancję wskazanego obiektu:

.. raw:: html

    <div class="code_no">Plik <i>ormpw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: ormpw.py
    :linenos:
    :lineno-start: 58
    :lines: 58-

.. note::

    Po wykonaniu wszystkich założonych operacji na danych połączenie z bazą należy
    zamknąć, zwalniając w ten sposób zarezerwowane zasoby. W przypadku modułu ``sqlite3``
    wywołujemy polecenie ``con.close()``, w Peewee ``baza.close()``.

Podsumowanie
***********************

Bazę danych można obsługiwać za pomocą języka SQL na niskim poziomie. Zyskujemy wtedy na szybkości
działania, ale tracimy przejrzystość kodu, łatwość jego przeglądania i rozwijania.
O ile w prostych zastosowaniach można to zaakceptować, o tyle w bardziej rozbudowanych
projektach używa się systemów ORM, które pozwalają zarządzać danymi nie w formie tabel, pól i rekordów,
ale w formie obiektów reprezentujących logicznie spójne dane. Takie podejście
lepiej odpowiada obiektowemu wzorcowi projektowania aplikacji.

Dodatkową zaletą systemów ORM, nie do przecenienia, jest większa odporność na błędy i ewentualne
ataki na dane w bazie.

Systemy ORM można łatwo integrować z programami desktopowymi i frameworkami przeznaczonymi do tworzenia
aplikacji sieciowych. Wśród tych ostatnich znajdziemy również takie, w których system ORM jest
podstawowym składnikiem, np. *Django*.

Zadania dodatkowe
*******************

- Wykonaj scenariusz aplikacji :ref:`Quiz ORM <quiz-orm>`, aby zobaczyć przykład wykorzystania systemów ORM
  w aplikacjach internetowych.

- Wykonaj scenariusz aplikacji internetowej :ref:`Czat (cz. 1) <czat-app>`, zbudowanej z wykorzystaniem
  frameworku *Django*, korzystającego z własnego modelu ORM.

Źródła
*******************

* :download:`sqlorm.zip <sqlorm.zip>`

Kolejne wersje tworzonych skryptów znajdziesz w katalogu ``~/python101/bazy/sqlorm``.
Uruchamiamy je wydając polecenia:

.. code-block:: bash

    ~/python101$ cd bazy/sqlorm
    ~/python101/bazy/sqlorm$ python sqlraw0x.py
    ~/python101/bazy/sqlorm$ python ormpw0x.py

\- gdzie *x* jest numerem kolejnej wersji kodu.