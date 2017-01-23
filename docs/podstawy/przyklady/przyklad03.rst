Pobierz *n* liczb
#################

**ZADANIE**: Pobierz od użytkownika *n* liczb i zapisz je w liście.
Wydrukuj: elementy listy i ich indeksy, elementy w odwrotnej kolejności,
posortowane elementy. Usuń z listy pierwsze wystąpienie elementu podanego
przez użytkownika. Usuń z listy element o podanym indeksie.
Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.
Wybierz z listy elementy od indeksu *i* do *j*.

**POJĘCIA**: *tupla, lista, metoda*.

Wszystkie poniższe przykłady warto wykonać w konsoli Pythona.
Treść komunikatów w funkcjach ``print`` można skrócić.
Można również wpisywać kolejne polecenia do pliku i sukcesywanie go uruchomiać.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 04_listy_01.py
    :linenos:

Funkcja ``input()`` pobiera dane wprowadzone przez użytkownika podobnie jak
jak ``raw_input()``, ale próbuje zinterpretować je jako kod Pythona.
Podane na wejściu liczby oddzielone przecinkami zostają spakowane jako
:term:`tupla` (krotka). Jest to uporządkowana sekwencja poindeksowanych danych,
przypominająca tablicę, której wartości nie można zmieniać. Zainicjowanie
tupli wartościami od razu w kodzie jest proste: ``tupla = (4, 3, 5)``.

Lista to również uporządkowane sekwencje indeksowanych danych, zazwyczaj
tego samego typu, które jednak możemy zmieniać.

.. note::

    W definicji tupli nawiasy są opcjonalne, można więc pisać tak: ``tupla = 3, 2, 5, 8``
    Oprócz tupli i list sekwencjami są w Pythonie również napisy.

Dostęp do elementów sekwencji uzyskujemy podając nazwę i indeks, np. ``lista[0]``.
Elementy indeksowane są od 0 (zera!). Z każdej sekwencji możemy wydobywać fragmenty
dzięki notacji wycinkowej (ang. *slice*), np.: ``lista[1:4]``.

Funkcje działające na sekwencjach:

* ``len()`` – zwraca ilość elementów;
* ``enumerate()`` – zwraca obiekt zawierający indeksy i elementy sekwencji;
* ``reversed()`` – zwraca obiekt zawierający odwróconą sekwencję.
* ``sorted(lista)`` – zwraca kopię listy posortowanej rosnąco;
* ``sorted(lista, reverse=True)`` – zwraca kopię listy w odwrotnym porządku;
*

Lista ma wiele użytecznych metod:

* ``.append(x)`` – dodaje x do listy;
* ``.remove(x)`` – usuwa pierwszy x z listy;
* ``.insert(i, x)`` – wstawia x przed indeksem i;
* ``.count(x)`` – zwraca ilość wystąpień x;
* ``.index(x)`` – zwraca indeks pierwszego wystąpienia x;
* ``.pop()`` – usuwa i zwraca ostatni element listy;
* ``.sort()`` – sortuje listę rosnąco;
* ``.reverse()`` – sortuje listę w odwróconym porządku.


Zadania dodatkowe
*****************

Utwórz w konsoli Pythona dowolną listę i przećwicz notację wycinkową.
Sprawdź działanie indeksów pustych i ujemnych, np. ``lista[2:], lista[:4], lista[-2], lista[-2:]``.
Posortuj trwale dowolną listę malejąco. Utwórz kopię listy posortowaną rosnąco.
