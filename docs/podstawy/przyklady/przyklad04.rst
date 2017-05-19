.. _fibonacci:

Ciąg Fibonacciego
#################

**ZADANIE**: Wypisz ciąg Fibonacciego aż do *n*-tego wyrazu podanego przez użytkownika.
Ciąg Fibonacciego to ciąg liczb naturalnych, którego każdy wyraz poza dwoma
pierwszymi jest sumą dwóch wyrazów poprzednich. Początkowe wyrazy tego ciągu to: 0 1 1 2 3 5 8 13 21. Przyjmujemy, że 0 wchodzi w skład ciągu.

**POJĘCIA**: *funkcja, zwracanie wartości, tupla, rozpakowanie tupli, przypisanie wielokrotne*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 04_funkcja_02.py
    :linenos:

Instrukcje realizujące jedno zadanie zazwyczaj grupujemy w funkcje,
które można później wielokrotnie wywoływać.
Funkcję definiujemy za pomocą słowa kluczowego ``def`` wg schematu
``def nazwa_funkcji(parametry):``. Przy czym parametry są opcjonalne.
Po dwukropku od nowego wiersza umieszczamy odpowiednio wcięte instrukcje,
które tworzą ciało funkcji. Funkcja może zwrócać jakąś wartość za pomocą
polecenia ``return wartość``.

Zapis ``a, b = pwyrazy`` jest przykładem rozpakowania tupli, tzn. zmienne *a* i *b*
przyjmują wartości kolejnych elementów tupli ``pwyrazy``. Zapis równoważny, w którym nie
definiujemy tupli tylko wprost podajemy wartości, to ``a, b = 0, 1``; ten sposób
przypisania wielokrotnego stosujemy w kodzie ``a, b = b, b + a``. Jak widać, ilość
zmiennych z lewej strony musi odpowiadać liczbie wartości rozpakowywanych z tupli
lub liczbie wartości podawanych wprost z prawej strony.

Podane przykłady pokazują, że algorytmy iteracyjne można implementować za pomocą różnych
instrukcji sterujących, w tym wypadku pętli ``while`` i ``for``, a także z wykorzystaniem
podejścia rekurencyjnego. W tym ostatnim wypadku zwróć uwagę na argument wywołania funkcji.

Zadania dodatkowe
*****************

Zmień funkcje tak, aby zwracały poprawne wartości przy założeniu,
że dwa pierwsze wyrazy ciągu równe są 1 (bez zera).
