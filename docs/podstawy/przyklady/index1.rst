Warunki i pętle
##################

.. contents::
    :depth: 1
    :local:

Trzy liczby
**************

    **ZADANIE**: Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.

    **POJĘCIA**: *pętla, obiekt, metoda, instrukcja warunkowa zagnieżdżona*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 02_if.py
    :linenos:

Jak to działa
==============

Pętla ``while`` umożliwia powtarzanie określonych operacji, np. pozwala użytkownikowi wprowadzać
kolejne serie liczb. Definiując pętlę określamy warunek powtarzania kodu. Dopóki jest prawdziwy,
czyli dopóki zmienna *op* ma wartość "t" pętla działa.

W Pythonie wszystko jest obiektem. Każdy obiekt przynależy do jakiego typu
i ma jakąś wartość. Typ determinuje, jakie operacje można wykonać na wartości danego obiektu.
Np. w podanym kodzie zmienna ``op`` jest napisem (typ string), z którego
możemy wyłuskać poszczególne słowa za pomocą metody ``split()``.

Instrukcje warunkowe (``if``), jak i pętle, można zagnieżdżać stosując wcięcia.
W jednej złożonej instrukcji warunkowej można sprawdzać wiele warunków (``elif:``).

Zadania dodatkowe
==================

    Sprawdź, co się stanie, jeśli podasz liczby oddzielone przecinkiem lub podasz
    za mało liczb. Zmień program tak, aby poprawnie interpretował dane oddzielane przecinkami.

Wydrukuj alfabet
********************

    **ZADANIE**: Wydrukuj alfabet w porządku naturalnym, a następnie odwróconym w formacie:
    "mała => duża litera". W jednym wierszu trzeba wydrukować po pięć takich grup.

    **POJĘCIA**: *iteracja, pętla, kod ASCII, lista, inkrementacja, operatory arytmetyczne, logiczne, przypisania i zawierania*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 03_petle_02.py
    :linenos:

Jak to działa
==============

Pętla ``for`` wykorzystuje zmienną iteracyjną ``i``, która przybiera wartości
z listy liczb całkowitych zwróconej przez funkcję ``range()``. Parametry
tej funkcji określają wartość początkową i końcową listy, przy czym wartość
końcowa nie wchodzi do listy. Kod ``range(122,96,-1)`` generuje listę wartości
malejących od 122 do 97(!) z krokiem -1.

Funkcja ``chr()`` zwraca znak, którego kod ASCII, czyli liczbę całkowitą,
przyjmuje jako argument. Metoda ``lower()`` typu string (napisu) zwraca
małą literę, ``upper()`` – dużą. Wyrażenie przypisywane zmiennej ``tmp``
pokazuje, jak można łączyć napisy (konkatenacja).

Zmienna pomocnicza ``x`` jest zwiększana (inkrementacja) w pętlach o 1.
Wyrażenie ``x += 1`` odpowiada wyrażeniu ``x = x + 1``. Pierwszy warunek
wykorzystuje operator logiczny ``and`` (koniunkcję) i operator modulo ``%``
(zwraca resztę z dzielenia), aby do ciągu znaków w zmiennej ``tmp`` dodać
znak końca linii (``\n``) za pomocą operatora ``+=``.
W drugim warunku używamy operatora porównania ``==``.

Zob.: :term:`operatory` dostępne w Pythonie.

Zadania dodatkowe
==================

    Uprość warunek w pierwszej pętli ``for`` drukującej alfabet w porządku
    naturalnym tak, aby nie używać operatora modulo. Wydrukuj co n-tą grupę
    liter alfabetu, przy czym wartość *n* podaje użytkownik.
    Wskazówka: użyj opcjonalnego, trzeciego argumentu funkcji ``range()``.
    Sprawdź działanie różnych operatorów Pythona w konsoli.
