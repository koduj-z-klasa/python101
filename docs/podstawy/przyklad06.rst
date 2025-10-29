.. _przyklad6:

Moduły i zbiory
###############

.. note::

    W tym przykładzie zobaczysz, jak korzystać z **modułów**, a także
    poznasz i wykorzystasz **zbiór**, kolejną obok list i krotek złożoną strukturę danych.

Zadanie
*******

Napisz program :file:`oceny.py`, który umożliwi wprowadzanie ocen z wybranego / wprowadzonego przedmiotu,
następnie policzy i wyświetla średnią, medianę i odchylenie standardowe wprowadzonych ocen.
Funkcje pomocnicze i statystyczne umieść w osobnym module.

**Dane**:

- ``przedmiot`` – nazwa dodawanego przedmiotu i/lub przedmiotu, z którego będą wprowadzane oceny,
  ciąg znaków pobierany z klawiatury,
- ``ocena`` – ocena pobierana z klawiatury, liczba całkowita.

**Wynik**:

– wypisana na ekranie średnia, mediana i odchylenie podanych ocen, np.:

.. code::

    Średnia:     3.62
    Mediana:     3.50
    Odchylenie:  1.58

.. raw:: html

    <div class="code_no">Plik <i>oceny.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. literalinclude:: przyklad06.py
    :linenos:

**Moduły**

Moduły to pliki zawierające często wykorzystywane stałe, funkcje i klasy. Wiele modułów, tzw. wbudowanych,
jest częścią standardowej instalacji Pythona, programista może również tworzyć własne moduły.
Dostęp do zawartości modułu uzyskujemy dzięki **importom**. Nazwa modułu to nazwa pliku z kodem bez rozszerzenia ``.py``.
Moduł musi znajdować się w ścieżce przeszukiwania, aby import był udany. Przykłady:

- ``import math`` – import całego modułu, dostęp do zawartości uzyskujemy dzięki notacji z kropką,
  np. ``math.pi`` lub ``math.sqrt()``,
- ``from math import pi, sqrt`` – import tylko wybranych elementów, których nazw używamy bezpośrednio, np.:
  ``pole = pi * r**2``, ``c = sqrt(a**2 + b**2)``.

.. note::

    W przypadku prostych programów zapisuj moduły w tym samym katalogu co program główny.

**Zbiór**

Do przechowywania nazw przedmiotów wykorzystujemy :term:`zbiór`, czyli nieuporządkowany zestaw niepowtarzalnych (!)
elementów. Operacje na zbiorach:

- ``przedmioty = {'polski', 'angielski'}`` – tworzy zbiór, można również używać funkcji ``set(sekwencja)``;
- ``.add(x)`` – dodaje element x do zbioru, jeżeli go w zbiorze nie ma;
- ``element (not) in kolekcji`` – operator zawierania ``(not) in`` sprawdza, czy podany element
  jest lub nie w kolekcji, tj. liście, zbiorze, krotce (tupli) lub innej sekwencji; wynikiem jest prawda
  lub fałsz.

.. note::

    Porządek elementów w zbiorach, inaczej niż w listach i krotkach, jest nieokreślony.

Przedmioty pobieramy w nieskończonej pętli warunkowej ``while True``. Jeżeli użytkownik poda przynajmniej 2-znakową
nazwę przedmiotu (``if len(przedmiot) > 1:``) i przedmiotu nie ma w zbiorze (``if przedmiot not in przedmioty:``),
zostanie on dodany. W przeciwnym razie wypisujemy przedmioty zawarte w zbiorze i pobieramy nazwę przedmiotu, z którego
użytkownik chce wprowadzić oceny. Jeżeli podanej nazwy nie ma w zbiorze, wypisujemy odpowiedni komunikat,
jeżeli jest, przerywamy pętlę instrukcją ``break`` i przechodzimy do wprowadzania ocen.

W drugiej pętli warunkowej pobieramy oceny, dopóki użytkownik nie wprowadzi 0 (zera).
Blok ``try...except`` pozwala przechwycić wyjątki, czyli w tym przypadku błąd przekształcenia
wartości na liczbę całkowitą. Jeżeli funkcja ``int()`` zwróci wyjątek, wykonywane są instrukcje
w bloku ``except ValueError:``, w przeciwnym razie po sprawdzeniu poprawności oceny dodajemy ją
do listy: ``oceny.append(ocena)``.

Metoda ``.capitalize()`` zmienia pierwszy znak napisu na wielką literę.

Do wypisania komunikatów używamy sformatowanych ciągów znaków (:term:`f-strings`) i specyfikatorów formatu.
Zapis ``{s:8.2f}`` oznacza, że wartość zmiennej ``s`` ma zostać wypisana w polu o szerokości 8 znaków
jako liczba zmiennoprzecinkowa z dokładnością do dwóch miejsc po przecinku.

Więcej informacji nt. formatowania danych wyjściowych: `PyFormat <https://pyformat.info/>`_.

.. raw:: html

    <hr />

**Funkcje** wykorzystywane w programie **oceny**, umieszczamy w osobnym pliku :file:`ocenyfun.py`.

.. raw:: html

    <div class="code_no">Plik <i>oceny_funkcje.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. literalinclude:: oceny_funkcje.py
    :linenos:

Instrukcja ``import math`` udostępnia wszystkie metody z modułu matematycznego, wykorzystujemy
funkcję obliczającą pierwiastek kwadratowy: ``math.sqrt()``.

Funkcja ``wypisz(sekwencja, kom='...')`` wypisuje podany komunikat, a następnie za pomocą pętli
``for e in sekwencja`` odczytuje i wypisuje elementy podanej sekwencji (zbioru, listy ip.) w jednym wierszu.
Argument ``kom`` jest opcjonalny, ponieważ przypisujemy mu wartość domyślną, która zostanie użyta,
jeżeli użytkownik nie poda innej w wywołaniu funkcji.

Funkcja ``srednia()`` do zsumowania wartości ocen wykorzystuje funkcję ``sum()``.

Funkcja ``mediana()`` sortuje niemalejąco otrzymaną listę "w miejscu" (``oceny.sort()``),
tzn. trwale zmienia porządek elementów listy. Jeżeli liczba ocen jest parzysta ``if len(oceny) % 2 == 0:``,
zwraca średnią arytmetyczną dwóch środkowych wartości. Indeks drugiego ze środkowych elementów
obliczamy w wyrażeniu ``half = len(oceny) // 2``. Operator ``//`` oznacza dzielenie całkowite.
Notacja wycinkowa ``oceny[half-1:half+1]`` zwraca dwa środkowe elementy z listy.
Jeżeli liczba ocen jest nieparzysta, zwracamy wartość środkową: ``oceny[len(oceny) // 2]``.

W funkcji ``wariancja()`` pętla ``for`` odczytuje kolejne oceny i korzysta z operatorów skróconego dodawania (``+=``)
i potęgowania (``**``), aby wyliczyć sumę kwadratów różnic kolejnych ocen i średniej: ``suma += (ocena - srednia)**2``.
Funkcja zwraca średnią arytmetyczną obliczonej sumy: ``suma / len(oceny)``.

Ćwiczenia
----------

W konsoli Pythona utwórz listę ``wyrazy`` zawierającą elementy: *abrakadabra* i *kordoba*.

- utwórz zbiór ``w1`` za pomocą polecenia ``set(wyrazy[0])`` oraz zbiór ``w2`` za pomocą polecenia ``set(wyrazy[1])``,
- wykonaj kolejno polecenia ilustrujące użycie klasycznych operatorów na zbiorach, czyli:
  różnica (-) , suma (|), przecięcie (część wspólna, &) i elementy unikalne (^):

.. code-block:: bash

  >>> print(w1 – w2)
  >>> print(w1 | w2)
  >>> print(w1 & w2)
  >>> print(w1 ^ w2)

- w pliku :file:`oceny_funkcje.py` dopisz funkcję, która wyświetli wszystkie oceny oraz ich odchylenia
  od wartości średniej; wywołanie funkcji umieść w pliku :file:`oceny.py`.

.. admonition:: Pojęcia

    :term:`moduł`, :term:`importowanie`, :term:`zbiór`, :term:`f-strings`, :term:`notacja wycinkowa`
