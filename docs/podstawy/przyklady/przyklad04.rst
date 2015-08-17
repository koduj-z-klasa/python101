.. _fibonacci:

Ciąg Fibonacciego
#################

**ZADANIE**: Wypisz ciąg Fibonacciego aż do *n*-tego wyrazu podanego przez użytkownika.
Ciąg Fibonacciego to ciąg liczb naturalnych, którego każdy wyraz poza dwoma
pierwszymi jest sumą dwóch wyrazów poprzednich. Początkowe wyrazy tego ciągu to: 0 1 1 2 3 5 8 13 21.

**POJĘCIA**: *funkcja, zwracanie wartości, tupla, rozpakowanie tupli, przypisanie wielokrotne*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 04_funkcja_02.py
    :linenos:

Definicja funkcji w Pythonie polega na użyciu słowa kluczowego ``def``,
podaniu nazwy funkcji i w nawiasach okrągłych ewentualnej listy parametrów.
Definicję kończymy znakiem dwukropka, po którym wpisujemy w następnych liniach,
pamiętając o wcięciach, ciało funkcji. Funkcja może, ale nie musi zwracać wartości.
Jeżeli chcemy zwrócić jakąś wartość używamy polecenia return wartość.

Zapis ``a, b = pwyrazy`` jest przykładem rozpakowania tupli, tzn. zmienne *a* i *b*
przyjmują wartości kolejnych elementów tupli ``pwyrazy``. Zapis równoważny, w którym nie
definiujemy tupli tylko wprost podajemy wartości, to ``a, b = 0, 1``; ten sposób
przypisania wielokrotnego stosujemy w kodzie ``a, b = b, b+a``. Jak widać, ilość
zmiennych z lewej strony musi odpowiadać liczbie wartości rozpakowywanych z tupli
lub liczbie wartości podawanych wprost z prawej strony.

Zadania dodatkowe
*****************

- Zmień funkcję ``fibonnacci()`` tak, aby zwracała wartość *n*-tego wyrazu. Wydrukuj tylko tę wartość w programie.
- Spróbuj napisać wersję rekurencyjną tej funkcji.