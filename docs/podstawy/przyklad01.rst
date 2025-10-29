.. _przyklad1:

Mów mi Python!
##############

.. note::

    W tym przykładzie poznasz instrukcje wejścia i wyjścia oraz podstawowe typy danych,
    użyjesz zmiennych i wykonasz proste operacje arytmetyczne.

Zadanie
*************

Napisz program :file:`witaj.py`, który pobiera od użytkownika imię oraz rok urodzenia i wypisuje podane niżej komunikaty.

**Dane**:

* ``akt_rok`` – liczba całkowita, aktualny rok,
* ``py_rok`` – liczba całkowita, rok powstania języka Python,
* ``imie`` – ciąg znaków pobierany z klawiatury, imię użytkownika,
* ``rok_urodzenia`` – liczba całkowita pobierana z klawiatury, rok urodzenia użytkownika.

**Wynik**:

* komunikaty wypisane na ekranie:

.. code::

    Witaj *imie*! Mów mi Python.
    Mam *wiek_py* lat*, ty masz wiek_u*.

.. tip::

    Język Python powstał w 1989 roku.
    Wiek użytkownika i wiek Pythona należy wyliczyć. Można użyć zmiennych pomocniczych, np. ``wiek_u`` i ``wiek_py``.
    
.. raw:: html

    <div class="code_no">Plik <i>witaj.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: przyklad01.py
    :linenos:

**Zmienne** służą do zapamiętywania używanych w programie wartości, np. napisów lub liczb.
Tworzymy je poprzez **przypisanie wartości** określonego typu za pomocą operatora `=`.
Przypisywane wartości mogą być wyrażeniami, np. działaniami arytmetycznymi lub logicznymi.

Do **pobierania danych** z klawiatury (domyślne wejście) i **wypisywania komunikatów** na ekranie (domyślne wyjście)
służą wbudowane funkcje:

* ``input()`` – zwraca pobrane z klawiatury znaki jako napis (ciąg znaków, ang. *string*).
* ``print()`` – wypisuje podane argumenty oddzielone przecinkami.

Do **przekształcania typów danych** na inne korzystamy z funkcji:

* ``int()`` – przekształca ciąg znaków na **liczbę całkowitą** (ang. *integer*),
* ``str()`` – przekształca liczbę całkowitą (lub inny typ danych) na **ciąg znaków** (ang. *string*).

Ciągi znaków można łączyć ze sobą za pomocą operatora ``+``.

Składnia
********

* **Nazwy zmiennych** nie powinny zawierać znaków narodowych.
  W Pythonie preferuje się małe litery oraz łączenie członów nazwy znakiem podkreślenia ``_``.
* **Napisy** w kodzie źródłowym, czyli stałe znakowe, ujmujemy w cudzysłowy podwójne lub pojedyncze.
* Znak ``#`` oznacza 1-liniowy komentarz, tj. objaśnienie kodu, które jest pomijane przez interpreter.

Ćwiczenia
*********

1) Zmień program tak, aby wartość zmiennej ``akt_rok`` (aktualny rok) była podawana przez użytkownika na początku programu.

.. tip::

    Użyj funkcji ``input()`` oraz ``int()``.

.. admonition:: Pojęcia
    
    :term:`zmienna`, wartość, :term:`typ danych`, wyrażenie, :term:`wejście` i :term:`wyjście`, komentarz
