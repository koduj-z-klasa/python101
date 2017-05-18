Trzy liczby
#############

**ZADANIE**: Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.

**POJĘCIA**: *pętla, obiekt, metoda, instrukcja warunkowa zagnieżdżona*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 02_if.py
    :linenos:

Pętla ``while warunek`` umożliwia powtarzanie bloku operacji, dopóki warunek
jest prawdziwy. W tym wypadku dopóki zmienna *op* ma wartość "t".

W Pythonie wszystko jest obiektem. Każdy obiekt przynależy do jakiegoś typu
i ma jakąś wartość. Typ determinuje, jakie operacje można wykonać na wartości danego obiektu.
Np. dane pobrane od użytkownika w funkcji ``input()`` zwracane są jako napis (typ *string*),
który rozbijamy na poszczególne składowe (w tym wypadku liczby) za pomocą metody ``split(separator)``.

Instrukcje warunkowe (``if``), jak i pętle, można zagnieżdżać stosując wcięcia.
Instrukcje o takich samych wcięciach tworzą bloki kodu.
W jednej złożonej instrukcji warunkowej można sprawdzać wiele warunków (``elif:``).

Zadania dodatkowe
*******************

Sprawdź, co się stanie, jeśli podasz liczby oddzielone przecinkiem lub podasz
za mało liczb. Zmień program tak, aby poprawnie interpretował dane oddzielane przecinkami.