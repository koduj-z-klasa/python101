.. _przyklad4:

Listy i krotki
###############

.. note::

    W tym przykładzie poznasz **listę** oraz **krotki**. Są to jedne z najczęściej używanych złożonych struktur danych,
    które pozwalają przechowywać wiele danych pod jedną nazwą.

Zadanie
********

Napisz program :file:`lista.py`, który pobiera z klawiatury ``n`` liczb całkowitych i zapisuje je w liście.
Następnie wykonuje podane niżej operacje:

- wypisuje elementy listy i ich indeksy w jednym wierszu,
- wypisuje elementy listy w odwrotnej kolejności
- wypisuje elementy listy posortowane w porządku niemalejącym,
- wypisuje liczbę wystąpień oraz indeks pierwszego wystąpienia podanego elementu,
- usuwa z listy podany element,
- usuwa z listy element o podanym indeksie,
- wstawia podany element na podanym indeksie,
- wypisuje z listy elementy od indeksu ``i`` do ``j``.

**Dane**:

Wszystkie dane to liczby całkowite pobierane z klawiatury, niektóre dane zapisywane są w tych samych zmiennych.
sam.

- ``n`` – liczba liczb pobieranych z klawiatury i zapisywanych w liście,
- ``el`` – liczba, którą należy z listy usunąć,
- ``el`` – liczba, której liczbę wystąpień i indeks pierwszego wystąpienia należy wypisać,
- ``ind`` – indeks elementu do usunięcia,
- ``ind, el`` – indeks i element, który należy wstawić do tabeli,
- ``i, j`` – indeksy pobierane z klawiatury, oznaczające wycinek listy do wypisania.

.. tip::

    Wszystkie poniższe przykłady operacji na listach warto wykonać w konsoli Pythona.
    Treść komunikatów w funkcjach ``print()`` można skrócić.
    Można również wpisywać kolejne polecenia do pliku i sukcesywnie go uruchomiać.

.. raw:: html

    <div class="code_no">Plik <i>lista.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. literalinclude:: przyklad04.py
    :linenos:

**Lista** to sekwencja indeksowanych danych, zazwyczaj tego samego typu, w kodzie łatwo ją rozpoznać
po nawiasach kwadratowych. Podstawowe operacje:

- ``lista = [3, 'III', 4, 'IV']`` – utworzenie listy poprzez podanie wartości,
- ``lista = []`` – utworzenie pustej listy,
- ``lista[0]`` – odczyt elementu o podanym indeksie, indeksy zaczynają się od 0 (zera),
- ``lista[1:4]`` – odczyt elementów od indeksu 1 do 3 przy użyciu notacji wycinkowej.

Funkcje działające na sekwencjach:

* ``len()`` – zwraca liczbę elementów;
* ``enumerate()`` – zwraca numer elementu i element sekwencji;
* ``sorted(lista)`` – zwraca kopię sekwencji posortowanej niemalejąco;
* ``sorted(lista, reverse=True)`` – zwraca kopię sekwencji w odwrotnym porządku;
* ``reversed()`` – zwraca kopię sekwencji w odwrotnym porządku.

.. note::

    Sekwencjami są w Pythonie również ciągi znaków i krotki (tuple).

Metody obiektów typu lista:

* ``.append(x)`` – dodaje x do listy;
* ``.remove(x)`` – usuwa pierwszy x z listy;
* ``.insert(i, x)`` – wstawia x na indeksie i;
* ``.count(x)`` – zwraca liczbę wystąpień x;
* ``.index(x)`` – zwraca indeks pierwszego wystąpienia x;
* ``.pop()`` – usuwa i zwraca ostatni element listy;
* ``.pop(i)`` – usuwa i zwraca element wskazany przez i;
* ``.sort()`` – sortuje listę rosnąco;
* ``.reverse()`` – sortuje listę w odwróconym porządku.

**Krotka** (tupla) to niemodyfikowalna lista. Wykorzystywana jest do zapamiętywania
i przekazywania wartości, których nie powinno się zmieniać.
Krotki tworzymy podając wartości w nawiasach okrągłych, np. ``krotka = (1, 'a')``
lub z listy za pomocą funkcji: ``tuple(sekwencja)``. Krotka może powstać
również poprzez spakowanie wartości oddzielonych przecinkami,
np. ``krotka = 1, 'a'``. Próba zmiany wartości w krotce generuje błąd.

Przetestuj w konsoli Pythona:

.. code-block:: bash

    >>> krotka = 2, 6
    >>> a, b = krotka
    >>> print(a, b)
    >>> krotka[0] = 1

Ćwiczenia
-----------

Utwórz w konsoli Pythona dowolną listę i przećwicz notację wycinkową:

* sprawdź działanie indeksów pustych i ujemnych, np. ``lista[2:], lista[:4], lista[-2], lista[-2:]``,
* posortuj trwale dowolną listę malejąco,
* utwórz kopię listy posortowaną rosnąco.

.. admonition:: Pojęcia

    :term:`lista`, :term:`metoda`, :term:`notacja wycinkowa`, :term:`krotka`
