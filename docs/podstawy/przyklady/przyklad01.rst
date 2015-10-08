Trzy liczby
#############

**ZADANIE**: Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.

**POJĘCIA**: *pętla, obiekt, metoda, instrukcja warunkowa zagnieżdżona*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 02_if.py
    :linenos:

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
*******************

Sprawdź, co się stanie, jeśli podasz liczby oddzielone przecinkiem lub podasz
za mało liczb. Zmień program tak, aby poprawnie interpretował dane oddzielane przecinkami.
