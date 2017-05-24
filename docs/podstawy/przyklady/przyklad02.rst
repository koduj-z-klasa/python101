Wydrukuj alfabet
##################

**ZADANIE**: Wydrukuj alfabet w porządku naturalnym, a następnie odwróconym w formacie:
"mała => duża litera". W jednym wierszu trzeba wydrukować po pięć takich grup.

**POJĘCIA**: *iteracja, pętla, kod ASCII, lista, inkrementacja, operatory arytmetyczne, logiczne, przypisania i zawierania*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 02_petle.py
    :linenos:

Pętla ``for`` wykorzystuje zmienną iteracyjną ``i``, która przybiera kolejne
wartości zwracane przez funkcję ``range()``. Parametry tej funkcji określają
wartość początkową i końcową, przy czym wartość końcowa nie jest zwracana.
Kod ``range(122,96,-1)`` generuje wartości malejące od 122 do 97(!) z krokiem -1.
Sprawdź w interpreterze:

.. code-block:: bash

    >>> list(range(0, 100))
    >>> list(range(122,96,-1))

Operacje na znakach:


* ``chr(kod_ascii)`` – zwraca znak odpowiadający podanemu kodowi `ASCII <https://pl.wikipedia.org/wiki/ASCII>`_;
* ``lower()`` – zwraca napis zamieniony na małe litery;
* ``upper()`` – zwraca napis zamieniony na duże litery;
* ``+`` – operator łączenia (konkatenacji) naspisów.

Operatory arytmetyczne i logiczne:

* ``x += 1`` – dodanie do zmiennej *x* wartości po prawej stronie – *1*;
* ``%`` – dzielenie modulo, zwraca resztę z dzielenia;
* ``==`` – operator porównania, nie mylić z operatorem przypisania (``=``);
* ``and`` – operator logicznej koniunkcji, obydwa warunki muszą być prawdziwe.

Zob.: :term:`operatory` dostępne w Pythonie.

Zadania
*******

- Uprość warunek w pierwszej pętli ``for`` drukującej alfabet w porządku
  naturalnym tak, aby nie używać operatora modulo.
- Wydrukuj co n-tą grupę liter alfabetu, przy czym wartość *n* podaje użytkownik.
  Wskazówka: użyj opcjonalnego, trzeciego argumentu funkcji ``range()``.
- Sprawdź działanie różnych operatorów Pythona w konsoli.
