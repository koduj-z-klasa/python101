.. _dane_z_pliku:

Dane z pliku
##################

Dane z tabel w bazach MS Accessa lub LibreOffice Base'a możemy eksportować
do formatu *csv*, czyli pliku tekstowego, w którym każda linia reprezentuje
pojedynczy rekord, a wartości pól oddzielone są jakimś separatorem, najczęściej
przecinkiem.

Załóżmy więc, że mamy plik ``uczniowie.csv`` zawierający dane uczniów
w formacie: ``Jan,Nowak,2``. Poniżej podajemy przykład funkcji, która
odczyta dane i zwróci je w użytecznej postaci:



.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: dane.py
    :linenos:

Na początku funkcji ``pobierz_dane()`` sprawdzamy, czy istnieje plik
podany jako argumet. Wykorzystujemy metodę ``isfile()`` z modułu ``os``,
który należy wcześniej zaimportować. Następnie w konstrukci ``with``
otwieramy plik i wczytujemy jego treść do zmiennej ``zawartosc``.
Pętla ``for`` pobiera kolejne linie, które oczyszczamy ze znaków końca linii
(``.replace('\n','')``, ``.replace('\r','')``) i dekodujemy jako zapisane w standardzie *utf-8*.
Poszczególne wartości oddzielone przecinkiem wyodrębniamy (``.split(',')``)
do tupli, którą dodajemy do zdefiniowanej wcześniej tablicy (``dane.append()``).

Na koniec funkcja zwraca listę przekształconą na tuplę (a więc zagnieżdzone tuple),
która po przypisaniu do zmiennej ``uczniowie`` użyta zostanie, dokładnie
tak jak robiliśmy to już wczesniej, jako argument metody ``.executemany()``.

.. attention::

    Znaki w pliku wejściowym powinny być zakodowane w standardzie ``utf-8``.

Przykład użycia
****************

W skrypcie omówionym w materiale :ref:`SQL <sql_raw>` można wykorzystać poniższy kod:

.. code-block:: python

    from dane import pobierz_dane

    # ...

    uczniowie = pobierz_dane('uczniowie.csv')
    cur.executemany(
    'INSERT INTO uczen (imie,nazwisko,klasa_id) VALUES(?,?,?)', uczniowie)