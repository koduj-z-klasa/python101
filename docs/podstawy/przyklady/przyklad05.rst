.. _oceny:

Oceny z przedmiotów
###################

**ZADANIE**: Napisz program, który umożliwi wprowadzanie ocen z podanego
przedmiotu ścisłego (np. fizyki), następnie policzy i wyświetla średnią,
medianę i odchylenie standardowe wprowadzonych ocen.
Funkcje pomocnicze i statystyczne umieść w osobnym module.

**POJĘCIA**: *import, moduł, zbiór, przechwytywanie wyjątków,
formatowanie napisów i danych na wyjściu, argumenty funkcji, zwracanie wartości*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 05_oceny_03.py
    :linenos:

Jak to działa
===================

Klauza ``from moduł import funkcja`` umożliwia wykorzystanie w programie
funkcji zdefiniowanych w innych modułach i zapisanych w osobnych plikach.
Dzięki temu utrzymujemy przejrzystość programu głównego, a jednocześnie
możemy funkcje z modułów wykorzystywać, importując je w innych programach.
Nazwa modułu to nazwa pliku z kodem pozbawiona jednak rozszerzenia *.py*.
Moduł musi być dostępny w ścieżce przeszukiwania, aby można go było poprawnie dołączyć.

.. note::
	W przypadku prostych programów zapisuj moduły w tym samym katalogu co program główny.

Instrukcja ``set()`` tworzy zbiór, czyli nieuporządkowany zestaw niepowtarzalnych (!) elementów. Instrukcje ``if przedmiot in przedmioty`` i ``if przedmiot not in przedmioty`` za pomocą operatorów zawierania ``(not) in`` sprawdzają, czy podany przedmiot już jest lub nie w zbiorze. Polecenie ``przedmioty.add()`` pozwala dodawać elementy do zbioru, przy czym jeżeli element jest już w zbiorze, nie zostanie dodany. Polecenie ``przedmioty.remove()`` usunnie podany jako argument element ze zbioru.

Oceny z wybranego przedmiotu pobieramy w pętli dopóty, dopóki użytkownik nie wprowadzi 0 (zera). Blok ``try...except`` pozwala przechwycić wyjątki, czyli w naszym przypadku niemożność przekształcenia wprowadzonej wartości na liczbę całkowitą. Jeżeli funkcja ``int()`` zwróci wyjątek, wykonywane są instrukcje w bloku ``except ValueError:``, w przeciwnym razie po sprawdzeniu poprawności oceny dodajemy ją jako liczbę zmiennoprzecinkową (typ *float*) do listy: ``oceny.append(float(ocena))``.

Metoda ``.capitalize()`` pozwala wydrukować podany napis dużą literą.

W funkcji ``print(...).format(s,m,o)`` zastosowano formatowanie drukowanych wartości, do których odwołujemy się w specyfikacji ``{0:5.2f}``. Pierwsza cyfra wskazuje, którą wartość z numerowanej od 0 (zera) listy, umieszczonej w funkcji ``format()``, wydrukować; np. aby wydrukować drugą wartość, trzeba by użyć kodu ``{1:}``.Po dwukropku podajemy szerokość pola przeznaczonego na wydruk, po kropce ilość miejsc po przecinku, symbol *f* oznacza natomiast liczbę zmiennoprzecinkową stałej precyzji.

Więcej informacji nt. formatowania danych wyjściowych: `PyFormat <https://pyformat.info/>`_.


.. raw:: html

    <hr />

**Funkcje** wykorzystywane w programie **oceny**, umieszczamy w osobnym pliku :file:`ocenyfun.py`.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: ocenyfun.py
    :linenos:

Klauzula ``import math`` udostępnia w pliku wszystkie metody z modułu
matematycznego, dlatego musimy odwoływać się do nich za pomocą notacji
moduł.funkcja, np.: ``math.sqrt()`` – zwraca pierwiastek kwadratowy.

Funkcja ``drukuj(co, kom="...")`` przyjmuje dwa argumenty, *co* – listę
lub zbiór, który drukujemy w pętli for, oraz *kom* – komunikat,
który wyświetlamy przed wydrukiem. Argument *kom* jest opcjonalny,
przypisano mu bowiem wartość domyślną, która zostanie użyta,
jeżeli użytkownik nie poda innej w wywołaniu funkcji.

Funkcja ``srednia()`` do zsumowania wartości ocen wykorzystuje funkcję ``sum()``.

Funkcja ``mediana()`` sortuje otrzymaną listę "w miejscu" (``oceny.sort()``), tzn. trwale zmienia porządek elementów.
W zależności od długości listy zwraca wartość środkową (długość nieparzysta)
lub średnią arytmetyczną dwóch środkowych wartości (długość).
Zapis ``oceny[half-1:half+1]`` wycina i zwraca dwa środkowe elementy
z listy, przy czym wyrażenie ``half = len(oceny)/2`` wylicza nam indeks drugiego ze środkowych elementów.

.. note::
    Przypomnijmy: alternatywna funkcja ``sorted(lista)`` zwraca uporządkowaną rosnąco kopię listy.

W funkcja ``wariancja()`` pętla for odczytuje kolejne oceny i w kodzie ``sigma += (ocena-srednia)**2`` korzysta z operatorów skróconego dodawania (+=) i potęgowania (**), aby wyliczyć sumę kwadratów różnic kolejnych ocen i średniej.

Zadania dodatkowe
*****************

- W konsoli Pythona utwórz listę ``wyrazy`` zawierającą elementy: *abrakadabra* i *kordoba*. Utwórz zbiór *w1* poleceniem ``set(wyrazy[0])``. Oraz zbiór *w2* poleceniem ``set(wyrazy[1])``. Wykonaj kolejno polecenia: ``print w1 – w2; print w1 | w2; print w1 & w2; print w1 ^ w2``. Przykłady te ilustrują użycie klasycznych operatorów na zbiorach, czyli: różnica (-) , suma (|), przecięcie (część wspólna, &) i elementy unikalne (^).
- W pliku :file:`ocenyfun.py` dopisz funkcję, która wyświetli wszystkie oceny oraz ich odchylenia od wartości średniej.
