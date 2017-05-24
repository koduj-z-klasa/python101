Instrukcje warunkowe
####################

Trzy liczby
===========

**ZADANIE**: Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.

**POJĘCIA**: *pętla while, obiekt, typ danych, metoda, instrukcja warunkowa zagnieżdżona*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 01_if.py
    :linenos:

Pętla ``while warunek`` umożliwia powtarzanie bloku operacji, dopóki warunek
jest prawdziwy. W tym wypadku dopóki zmienna *op* ma wartość "t".
Zwróć uwagę na operator porównania: ``==``.

W Pythonie wszystko jest obiektem. Każdy obiekt przynależy do jakiegoś typu
i ma jakąś wartość. Typ determinuje, jakie operacje można wykonać na wartości danego obiektu.
Funkcja ``input()`` zwraca pobrane dane jako napis (typ *string*).
Metoda ``split(separator)`` pozwala rozbić napis na składowe (w tym wypadku liczby).

Instrukcje warunkowe (``if``), jak i pętle, można zagnieżdżać stosując wcięcia.
Instrukcje o takich samych wcięciach tworzą bloki kodu.
W jednej złożonej instrukcji warunkowej można sprawdzać wiele warunków (``elif:``).

Zadania
-------

Sprawdź, co się stanie, jeśli podasz liczby oddzielone przecinkiem lub podasz
za mało liczb. Zmień program tak, aby poprawnie interpretował dane oddzielane przecinkami.

Trójkąt
=======

**ZADANIE**: Napisz program, który na podstawie danych pobranych od użytkownika,
czyli długości boków, sprawdza, czy da się zbudować trójkąt i czy jest to trójkąt prostokątny.
Jeżeli da się zbudować trójkąt, należy wydrukować jego obwód i pole, w przeciwnym wypadku
komunikat, że nie da się utworzyć trójkąta.

**POJĘCIA**: *pętla for, obiekt, typ danych, metoda, lista, instrukcja warunkowa zagnieżdżona*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 01_trojkat.py
    :linenos:

Pętla ``while`` działa podobnie jak w poprzednim przykładzie, ale wykorzystuje
warunek sformułowany przy wykorzystaniu operatora "różne od": ``!=``.

Metoda ``split(",")`` zwraca listę napisów wyodrębnionych z podanego ciągu.
Lista (zob. :term:`lista`) to sekwencja uporządkowanych danych,
np. ['3', '4', '5']. Do przeglądania takich sekwencji używa się pętli ``for``.

Pętla ``for zmienna in sekwencja`` odczytuje kolejne elementy *sekwencji*
i udostępnia je w *zmiennej*. W ciele pętli zmienną skonwertowaną na liczbę
całkowitą dodajemy do nowej listy za pomocą metody ``append()``.

Zapis ``a, b, c = lista`` jest przykładem rozpakowania listy, co polega
na przypisaniu zmiennym z lewej strony kolejnych wartości z listy.

.. note::

	Pętle, które wykonują jakieś operacje na sekwencjach i zapisują je w listach
	zastępuje się w Pythonie tzw. wyrażeniami listowymi. Zostaną one omówione
	w kolejnych przykładach.

Operatory logiczne:

* ``and`` – koniunkcja ("i"), wskazuje, że obydwa warunki muszą być prawdziwe;
* ``or`` – alternatywa ("lub"), przynajmniej jeden z podanych warunków powinien
  być prawdziwy.

Działania matematyczne:

* ``x**y`` – podnoszenie podstawy ``x`` do potęgi ``y``;
* ``sqrt()`` – funkcja z modułu ``math``, oblicza pierwiastek kwadratowy.
