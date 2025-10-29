.. _maly-lotek:

Mały Lotek
###########

.. note::

    Przykład pokazuje użycie instrukcji wejścia i wyjścia, instrukcji iteracyjnej oraz warunkowej,
    a także generatora liczb pseudolosowych. Program wymaga umiejętności wyodrębniania bloków
    kodu za pomocą wcięć.

Zadanie
********

Napisz program :file:`maly_lotek.py`, który losuje liczbę i daje użytkownikowi trzy szansy na jej odgadnięcie.

**Dane**:

* ``liczba`` – losowa liczba całkowita z zakresu <1; 10>, którą należy odgadnąć,
* ``typ`` – liczba całkowita pobierana z klawiatury,

**Wynik** – wypisane komunikaty:

* "Zgadłeś!" – jeżeli użytkownik odgadł wylosowaną liczbę,
* "Nie zgadłeś. Spróbuj jeszcze raz." – jeżeli użytkownik nie zgadł, ale ma jeszcze szanse,
* "Miałem na myśli liczbę: liczba" – jeżeli użytkownik nie odgadł wylosowanej liczby.

Losowanie liczby
****************

Korzystanie z generatora liczb pseudolosowych umożliwia moduł ``random``.
Zawiera on m.in. funkcję ``randint()``, która zwraca liczbę z obustronnie domkniętego zakresu ``<a; b>``:

.. raw:: html

    <div class="code_no">Plik <i>maly_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: maly_lotek.py
    :linenos:
    :lineno-start: 1
    :lines: 1-5

Pobieranie typów
****************

Trafienie za pierwszym razem wylosowanej liczby jest bardzo trudne, dajemy graczowi 3 szanse.
Uzupełniamy kod:

.. raw:: html

    <div class="code_no">Plik <i>maly_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: maly_lotek.py
    :linenos:
    :lineno-start: 6
    :lines: 6-9

Pobieranie i sprawdzanie kolejnych liczb wymaga powtórzeń, czyli **pętli** (zob. :term:`pętla`).
Ponieważ wiemy, że użytkownik ma trzy szanse, stosujemy pętlę ``for i in range(3):``.
W każdym powtórzeniu wypisujemy numer próby i pobieramy z klawiatury liczbę całkowitą,
którą zapisujemy w zmiennej: ``typ = int(input('Podaj liczbę od 1 do 10: '))``.

.. attention::

    Zakładamy na razie, że gracz wprowadza poprawne dane, czyli liczby całkowite!

Sprawdzanie typów
******************

Do sprawdzenia, czy użytkownik odgadł wylosowaną liczbę, musimy skorzystać ze złożonej instrukcji warunkowej:

.. raw:: html

    <div class="code_no">Plik <i>maly_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: maly_lotek.py
    :linenos:
    :lineno-start: 10
    :lines: 10-17

Jeżeli zmienne ``liczba `` i ``typ`` zawierają tę samą wartość, wypisujemy komunikat o sukcesie.
W przeciwnym razie jeżeli pobrano trzeci typ (``i == 2``) i nie był on trafny, wypisujemy wylosowaną liczbę.
W przeciwnym razie wypisujemy komunikat, żeby spróbować jeszcze raz.

Ćwiczenie
*********

1) Zgadywanie, gdy losowana liczba jest wypisywana, nie jest zabawne. Zakomentuj instrukcję wypisującą wylosowaną liczbę.
2) Dopisz odpowiednie polecenie, które wypisze liczbę podaną przez gracza.
3) W trybie interaktywnym interpretera Pythona sprawdź działanie funkcji ``randint()``:

   .. code-block:: bash

       ~$ python3
       >>> list(range(30))
       >>> for i in range(0, 100, 2)
       ...   print i
       ...
       >>> exit()

   Funkcja ``range()`` może przyjmować opcjonalne parametry określające początek, koniec
   oraz krok generowanej listy wartości.

.. admonition:: Pojęcia

    :term:`pętla`, :term:`instrukcja warunkowa`
