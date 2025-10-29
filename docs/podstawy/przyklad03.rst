.. _przyklad3:

Pętle
#####

.. note::

    W tym przykładzie poznasz instrukcje iteracyjne, tzw. pętle,
    pozwalające powtarzać określone operacje.

Zadanie
********

Napisz program :file:`alfabet.py`, który wypisze ``n`` początkowych małych i dużych liter alfabetu
w jednym wierszu w formacie: "mała_litera–duża_litera".

**Dane**:

* ``n`` – liczba całkowita oznaczająca liczbę liter do wypisania.

**Wynik**:

* wypisane pary małych i dużych liter na ekranie, np. dla ``n = 5``:

.. code::

    a–A b–B c–C d–D e–E

.. raw:: html

    <div class="code_no">Plik <i>alfabet.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: przyklad03.py
    :linenos:

Pętla ``for``
*************

Liczba wykonań pętli ``for`` zależy od liczby elementów sekwencji znajdującej się po słowie kluczowym ``in``.
Kolejne elementy sekwencji dostępne są w zmiennej iteracyjnej, w naszym przykładzie ma ona nazwę``i``.

**Funkcja** ``range()`` generuje sekwencje liczb całkowitych, np.:

- ``range(n)`` – zwraca kolejne liczby z zakresu ``<0, n-1>``, pętla wykona się ``n`` razy,
- ``range(a, b)`` – zwraca kolejne liczby z zakresu ``<a, b-1>``, pętla wykona się ``b-a`` razy,
- ``range(a, b, -1)`` – zwraca malejące liczby z zakresu ``<a, b>``, pętla wykona się ``a-b`` razy.

.. note::

    Jeżeli chcesz sprawdzić działanie funkcji ``range()`` w trybie interaktywnym interpretera, warto tę funkcję
    wywołać jako argument funkcji ``list()``, która zamienia generowaną sekwencję na listę, np.:
    ``list(range(65, 91))``.

Inne przykłady sekwencji, których można użyć w pętli ``for``:

- ciąg znaków, np. ``abcdefg``,
- lista elementów, np. ``[2, 4, 6, 8]``.

Pętla ``while``
***************

Pętla ``while warunek`` umożliwia powtarzanie bloku operacji, dopóki warunek jest prawdziwy,
w tym przypadku dopóki ``i < n``. Zwróć uwagę, że początkowa wartość 0 zmiennej ``i``
jest w pętli zwiększana o 1: ``i += 1`` – aby pętla nie działała w nieskończoność.

Operacje na znakach
*******************

Wszystkim znakom przypisane są kody liczbowe, w przypadku 25 liter alfabetu łacińskiego są to kody
`ASCII <https://pl.wikipedia.org/wiki/ASCII>`_. Duże litery mają kody w zakresie ``<65, 90>``,
natomiast małe litery w zakresie ``<97, 122>``.

Do wykonywania operacji na znakach służą funkcje i metody typu ``string``:

- ``ord(znak)`` – zwraca kod ASCII podanego znaku,
- ``char(kod)`` – zwraca znak o podanym kodzie.
- ``znak(i).upper()`` – metoda zwraca znak(i) zamienione na duże litery,
- ``znak(i).lower()`` – metoda zwraca znak(i) zamienione na małe litery.

Formatowane wyjście
********************

Jeżeli w wpisywanym komunikacie chcemy umieścić wartości zmiennych lub wyrażeń, najwygodniej używać
formatowanych ciągów znakowych (ang. *f-strings*). Przed cudzysłowami dajemy małą literą ``f``,
zmienne lub wyrażenia otaczamy nawiasami klamrowymi, np.:

- ``print(f'{l_mala} – {l_duza}', end=' ')`` – dodatkowy argument ``end`` pozwala określić znak wstawiany
  na końcu wypisywanego komunikatu zamiast domyślnego znaku nowego wiersza.

Ćw. 1 – odwrócony porządek
--------------------------

Dodaj do programu :file:`alfabet.py` kod, który wypisze w jednym wierszu ``n`` małych i dużych liter
zaczynając od końca alfabetu.

.. tip::

    Użyj funkcji ``range()``, która wygeneruje sekwencje malejących kodów ASCII. Możesz również użyć metod
    ``.upper()`` lub ``.lower()``.

.. admonition:: Pojęcia

    :term:`pętla`, :term:`metoda`
