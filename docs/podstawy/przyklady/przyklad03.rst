Pobierz *n* liczb
#################

**ZADANIE**: Pobierz od użytkownika *n* liczb i zapisz je w liście.
Wydrukuj: elementy listy i ich indeksy, elementy w odwrotnej kolejności,
posortowane elementy. Usuń z listy pierwsze wystąpienie elementu podanego
przez użytkownika. Usuń z listy element o podanym indeksie.
Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.
Wybierz z listy elementy od indeksu *i* do *j*.

**POJĘCIA**: *lista, metoda, notacja wycinkowa, tupla*.

Wszystkie poniższe przykłady warto wykonać w konsoli Pythona.
Treść komunikatów w funkcjach ``print()`` można skrócić.
Można również wpisywać kolejne polecenia do pliku i sukcesywnie go uruchomiać.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 04_listy_01.py
    :linenos:

Na początku z modułu ``random`` importujemy funkcję ``randint(a, b)``,
która służy do generowania liczb z przedziału [a, b]. Wylosowane liczby
dodajemy do listy.

Lista (zob. :term:`lista`) to sekwencja indeksowanych danych, zazwyczaj tego samego typu.
Listę tworzymy ujmując wartości oddzielone przecinkami w nawiasy kwadratowe,
np. ``lista = [1, 'a']``. Dostęp do elementów sekwencji uzyskujemy podając
nazwę i indeks, np. ``lista[0]``. Elementy indeksowane są od 0 (zera!).
Z każdej sekwencji możemy wydobywać fragmenty dzięki notacji wycinkowej
(ang. *slice*, zob. :term:`notacja wycinkowa`), np.: ``lista[1:4]``.

.. note::

    Sekwencjami w Pythonie są również napisy i tuple.

Funkcje działające na sekwencjach:

* ``len()`` – zwraca ilość elementów;
* ``enumerate()`` – zwraca obiekt zawierający indeksy i elementy sekwencji;
* ``reversed()`` – zwraca obiekt zawierający odwróconą sekwencję;
* ``sorted(lista)`` – zwraca kopię listy posortowanej rosnąco;
* ``sorted(lista, reverse=True)`` – zwraca kopię listy w odwrotnym porządku;

Lista ma wiele użytecznych metod:

* ``.append(x)`` – dodaje x do listy;
* ``.remove(x)`` – usuwa pierwszy x z listy;
* ``.insert(i, x)`` – wstawia x przed indeksem i;
* ``.count(x)`` – zwraca ilość wystąpień x;
* ``.index(x)`` – zwraca indeks pierwszego wystąpienia x;
* ``.pop()`` – usuwa i zwraca ostatni element listy;
* ``.sort()`` – sortuje listę rosnąco;
* ``.reverse()`` – sortuje listę w odwróconym porządku.

Tupla to niemodyfikowalna lista. Wykorzystywana jest do zapamiętywania
i przekazywania wartości, których nie powinno się zmieniać.
Tuple tworzymy podając wartości w nawiasach okrągłych, np. ``tupla = (1, 'a')``
lub z listy za pomocą funkcji: ``tuple(lista)``. Tupla może powstać
również poprzez spakowanie wartości oddzielonych przecinkami,
np. ``tupla = 1, 'a'``. Próba zmiany wartości w tupli generuje błąd.

Funkcja ``eval()`` interpretuje swój argument jako kod Pythona.
W instrukcji ``a, i = eval(input("Podaj element i indeks oddzielone przecinkiem: "))``
podane przez użytkownika liczby oddzielone przecinkiem interpretowane są jako tupla,
która następnie zostaje rozpakowana, czyli jej elementy zostają przypisane
do zmiennych z lewej strony. Przetestuj w konsoli Pythona:

.. code-block:: bash

	>>> tupla = 2, 6
	>>> a, b = tupla
	>>> print(a, b)

Zadania dodatkowe
*****************

Utwórz w konsoli Pythona dowolną listę i przećwicz notację wycinkową.
Sprawdź działanie indeksów pustych i ujemnych, np. ``lista[2:], lista[:4], lista[-2], lista[-2:]``.
Posortuj trwale dowolną listę malejąco. Utwórz kopię listy posortowaną rosnąco.
