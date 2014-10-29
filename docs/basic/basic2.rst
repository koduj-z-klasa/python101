Warunki i pętle
=================

Trzy liczby
-------------

    **ZADANIE**: Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.
    
    **POJĘCIA**: *pętla, obiekt, metoda, instrukcja warunkowa zagnieżdżona, formatowanie kodu*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 02_if.py
    :linenos:

JAK TO DZIAŁA
^^^^^^^^^^^^^^

Pętla ``while`` umożliwia powtarzanie określonych operacji, czyli pozwala użytkownikowi wprowadzać
kolejne serie liczb. Definiując pętle określamy warunek powtarzania kodu. Dopóki jest prawdziwy,
czyli dopóki zmienna *op* ma wartość "t" pętla działa. Do wydzielania kodu przynależnego do pętli
i innych instrukcji (np. ``if``) stosujemy wcięcia. Formatując kod, możemy używać zarówno tabulatorów,
jak i spacji, ważne aby w obrębie pliku było to konsekwentne.

.. note::
    Dobry styl programowania sugeruje używanie do wcięć 4 spacji.

W Pythonie wszystko jest obiektem, czyli typy wbudowane, np. napisy, posiadają metody (funkcje)
wykonujące określone operacje na wartościach. W podanym kodzie funkcja ``raw_input()`` zwraca
ciąg znaków wprowadzony przez użytkownika, z którego wydobywamy poszczególne słowa za pomocą
metody ``split()`` typu string.
Instrukcje warunkowe (``if``), jak i pętle, można zagnieżdżać stosując wcięcia.
W jednej złożonej instrukcji warunkowej można sprawdzać wiele warunków (``elif:``).

POĆWICZ SAM
^^^^^^^^^^^^^^

    Sprawdź, co się stanie, jeśli podasz liczby oddzielone przecinkiem lub podasz
    za mało liczb. Zmień program tak, aby poprawnie interpretował dane oddzielane przecinkami.

Wydrukuj alfabet
-----------------

    **ZADANIE**: Wydrukuj alfabet w porządku naturalnym, a następnie odwróconym w formacie:
    "mała => duża litera". W jednym wierszu trzeba wydrukować po pięć takich grup.
    
    **POJĘCIA**: *iteracja, pętla, kod ASCII, lista, inkrementacja, operatory arytmetyczne, logiczne, przypisania i zawierania*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 03_petle_02.py
    :linenos:

JAK TO DZIAŁA
^^^^^^^^^^^^^^

Pętla for wykorzystuje zmienną i, która przybiera wartości z listy liczb całkowitych zwróconej przez funkcję ``range()``. Parametry tej funkcji określają wartość początkową i końcową listy, przy czym wartość końcowa nie wchodzi do listy. Kod ``range(122,96,-1)`` generuje listę wartości malejących od 122 do 97(!) z krokiem -1.

Funkcja ``chr()`` zwraca znak, którego kod ASCII, czyli liczbę całkowitą, przyjmuje jako argument. Metoda ``lower()`` typu string (napisu) zwraca małą literę, ``upper()`` – dużą. Wyrażenie przypisywane zmiennej *tmp* pokazuje, jak można łączyć napisy (konkatenacja).

Zmienna pomocnicza ``x`` jest zwiększana (inkrementacja) w pętlach o 1. Wyrażenie ``x += 1`` odpowiada wyrażeniu ``x = x + 1``. Pierwszy warunek wykorzystuje operator logiczny ``and`` (koniunkcję) i operator modulo ``%`` (zwraca resztę z dzielenia), aby do ciągu znaków w zmiennej ``tmp`` dodać znak końca linii (``\n``) za pomocą operatora ``+=``. W drugim warunku używamy operatora porównania ``==``.

Poniżej podano wybrane operatory dostępne w Pythonie.

* **Arytmetyczne**: +, -, \*, /, //, %, \*\* (potęgowanie); znak + znak (konkatenacja napisów); znak * 10 (powielenie znaków)
* **Przypisania**: =, +=, -=, \*=, /=, %=, \*\*=, //=
* **Logiczne**: and, or, not
    Fałszem logicznym są: liczby zero (0, 0.0), False, None (null), puste kolekcje ([], (), {}, set()), puste napisy. Wszystko inne jest prawdą logiczną.
* **Zawierania**: in, not in
* **Porównania**: ==, >, <, <>, <=, >= != (jest różne)

POĆWICZ SAM
^^^^^^^^^^^^^^

    Uprość warunek w pierwszej pętli ``for`` drukującej alfabet w porządku naturalnym tak, aby nie używać operatora modulo.
    Wydrukuj co n-tą grupę liter alfabetu, przy czym wartość *n* podaje użytkownik. Wskazówka: użyj opcjonalnego, trzeciego argumentu funkcji ``range()``.
    Sprawdź działanie różnych operatorów Pythona w konsoli.

Metryka
^^^^^^^

:Autor: Robert Bednarz <ecg@ecg.vot.pl>

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>


.. include:: ../copyright.rst
