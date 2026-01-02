.. _dane_z_pliku:

Dane z pliku
##################

Dane z tabel w bazach MS Accessa lub LibreOffice Base'a możemy eksportować
do formatu `CSV (comma-separated values) <https://pl.wikipedia.org/wiki/CSV_(format_pliku)>`_,
czyli pliku tekstowego, w którym każda linia reprezentuje pojedynczy rekord,
a wartości pól oddzielone są jakimś separatorem, najczęściej przecinkiem lub średnikiem.

Załóżmy więc, że mamy plik :download:`uczniowie.csv` w formacie CSV z danymi uczniów. Każda linia zawiera
dane jednego rekordu, np: ``Jan,Nowak,2``. Poniżej podamy przykłady dwóch funkcji,
które odczytują dane i zwracają je w postaci listy, której elementami są listy zawierające poszczególne wartości pól
jednego rekordu.

.. attention::

    Znaki w pliku wejściowym powinny być zakodowane w standardzie ``UTF-8``.

Użycie metod ciągów znaków
**************************

Do pliku :file:`dane.py` dodajemy pierwszą funkcję, która wykorzystuje metody ciągów znaków
do oczyszczenia i odczytywania danych.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: dane.py
    :linenos:
    :lineno-start: 1
    :lines: 1-15

Na początku funkcji za pomocą metody ``isfile()`` modułu ``os`` sprawdzamy, czy na dysku istnieje plik
podany jako argument. Jeżeli tak, w konstrukcji ``with`` otwieramy plik w trybie do odczytu,
a jego zawartość udostępniamy w zmiennej ``plik``.

Ponieważ plik można traktować jako sekwencję linii używamy pętli ``for`` do ich odczytywania.
Każda odczytana linia za pomocą metody ``strip()`` oczyszczana jest z ewentualnych znaków spacji
na początku i końcu oraz ze znaków końca linii. Następnie metoda ``split()`` rozbija linię
na podciągi znaków, tj. wartości poszczególnych pól, wydzielając je za pomocą znaku przecinka
podanego jako argument metody. Omawiana metoda zwraca listę, którą dopisujemy do listy ``dane``.

.. tip::

    Jeżeli znak oddzielający wartości poszczególnych pól rekordu jest inny niż przecinek,
    należy podać go jako argument metody ``split()``.

Użycie modułu csv
*****************

Język Python dostarcza gotowy moduł do wykonywania operacji na plikach w formacie CSV.
Poniżej pokazujemy funkcję, która korzysta z tego modułu do odczytywania danych:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: dane.py
    :linenos:
    :lineno-start: 17
    :lines: 17-28

Na początku w pliku zawierającym funkcję umieszczamy import modułu ``csv``.
Następnie początek funkcji jest taki sam, jak w przykładzie omówionym wcześniej.
Różnica występuje w pętli ``for``, w której do odczytania kolejnych linii z pliku
wykorzystujemy metodę ``reader()``, która jako argumenty otrzymuje zmienną udostępniającą zawartość pliku
oraz znak rozdzielający wartości poszczególnych pól rekordu.

.. tip::

    Jeżeli znak oddzielający wartości poszczególnych pól rekordu jest inny niż przecinek,
    należy podać go jako wartość argumentu ``delimiter``.

Przykłady użycia
****************

Plik ``dane.py`` zawierający jedną z omówionych wyżej funkcji nazwaną ``pobierz_dane()``
oraz plik z danymi w formacie CSV powinny znajdować się w katalogu ze skryptem obsługującym bazę danych.
Jeżeli tak jest, to:

W skrypcie omówionym w materiale :ref:`SQL <sql_raw>` można wykorzystać poniższy kod:

.. code-block:: python

    from dane import pobierz_dane

    # ...

    uczniowie = pobierz_dane('uczniowie.csv')
    cur.executemany('INSERT INTO uczen (imie,nazwisko,klasa_id) VALUES(?,?,?)', uczniowie)

.. tip::

    Kod przedstawionych funkcji można zmodyfikować, aby zwracał dane w strukturze wykorzystywanej przez system ORM,
    np. listy słowników zawierających dane w formacie "klucz":"wartość"
    (zob. :ref:`System ORM Peewee <orm_peewee>`, :ref:`System ORM SQLAlchemy <orm_sqlalchemy>`).

Materiały
==========

1. `CSV File Reading and Writing <https://docs.python.org/3/library/csv.html>`_
