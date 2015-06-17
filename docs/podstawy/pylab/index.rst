Python kreśli
################

Jedną z potężniejszych biliotek Pythona jest `matplotlib <http://pl.wikipedia.org/wiki/Matplotlib>`_,
która służy do tworzenia różnego rodzaju wykresów. *Pylab* to :term:`API` ułatwiające
korzystanie z omawianej biblioteki na wzór środowiska `Matlab <http://pl.wikipedia.org/wiki/MATLAB>`_.
Poniżej pokazujemy, jak łatwo przy użyciu Pythona wizualizować wykresy różnych
funkcji.

Najłatwiej zainstalować wymaganą bibliotekę wydając polecenie z uprawnieniami
roota w terminalu:

.. code-block:: bash

    ~# pip install matplotlib

.. contents::
    :depth: 1
    :local:

Funkcja liniowa
***************

Zabwę zacznijmy w konsoli Pythona:

.. code-block:: python

    import pylab
    x = [1,2,3]
    y = [4,6,5]
    pylab.plot(x,y)
    pylab.show()

Tworzenie wykresów jest proste. Musimy mieć zbiór wartości *x* i odpowiadający
im zbiór wartości *y*. Obie listy przekazujemy jako argumenty funkcji ``plot()``,
a następnie rysujemy funkcją ``show()``.

Spróbujmy zrealizować bardziej złożone zadanie.

ZADANIE: wykonaj wykres funkcji *f(x) = a*x + b*, gdzie *x* = <-10;10> z krokiem 1,
*a* = 1, *b* = 2.

W pliku :file:`pylab01.py` umieszczamy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pylab01.py
    :linenos:

Na początku dla ułatwienia importujemy interfejs ``pylab``. Następnie postępujemy
wg omówionego schematu: zdefiniuj dziedzinę argumentów funkcji, a następnie zbiór wyliczonych
wartości. W powyższym przypadku generujemy listę wartości *x* za pomocą funkcji
``range()`` – co warto przetestować w interaktywnej konsoli Pythona.
Wartości *y* wyliczamy w pętli i zapisujemy w liście.

Dodatkowe metody: ``title()`` ustawia tytuł wykresu, ``grid()`` włącza wyświetlanie
pomocniczej siatki. Uruchom program.

Ćwiczenie 1
============

Można ułatwić użytkownikowi testowanie funkcji, umożliwiając mu podawanie
współczynników *a* i *b*. Zastąp odpowiednie przypisania instrukcjami
pobierającymi dane od użytkownika. Nie zapomnij przekonwertować danych
tekstowych na liczby całkowite. Przetestuj zmodyfikowany kod.

Ćwiczenie 2
============

W konsoli Pythona wydajemy następujące polecenia:

.. code-block:: python

    >>> a = 2
    >>> x = range(11)
    >>> for i in x:
    ...   print a + i
    >>> y = [a + i for i in range(11)]
    >>> y

Powyższy przykład pokazuje kolejne ułatwienie dostępne w Pythonie, czyli
:term:`wyrażenie listowe`, które zwięźle zastępuje pętlę i zwraca listę
wartości. Jego działanie należy rozumieć następująco: dla każdej wartości
``i`` (nazwa zmiennej dowolna) w liście ``x`` wylicz wyrażenie ``a + i``
i umieść w liście ``y``.

Wykorzystajmy wyrażenie listowe w naszym programie:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pylab02.py
    :linenos:
    :emphasize-lines: 1, 2, 6
    :lineno-start: 6
    :lines: 6-11

Dwie funkcje
*************

ZADANIE: wykonaj wykres funkcji *f(x)*, gdzie *x* = <-10;10> z krokiem 0.5,
*f(x) = x*x/3 dla x < 1 i x > 0*, *f(x) = x/(-3) + a dla x <= 0*. Współczynnik
*a* podaje użytkownik.

Ćwiczenie 2
============

Zanim zrealizujemy zadanie przećwiczmy w konsoli Pythona następujący kod:

.. code-block:: python

    >>> import pylab
    >>> x = pylab.frange(-10, 11, 0.5)
    >>> x
    >>> y = [i**2 for i in x if i <= 0]
    >>> len(y)

Wykonanie zadania wymaga umieszczenia na wykresie dwóch funkcji.
Wykorzystamy funkcję ``frange``, która zwraca listę wartości
zmiennoprzecinkowych (zob. typ :term:`typy danych`) z zakresu określonego przez
dwa pierwsze argumenty i z krokiem wyznaczonym przez argument trzeci.
Drugą przydatną konstrukcją będzie wyrażenie listowe uzupełnione o instrukcję
warunkową, która ogranicza wartości, dla których obliczane jest podane wyrażenie.

W pliku :file:`pylab02.py` umieszczamy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pylab03.py
    :linenos:

Uruchom program. Udało się nam zrealizować pierwszą część zadania.
Spróbujmy zakodować część drugą. Dopisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pylab04.py
    :linenos:
    :lineno-start: 13
    :lines: 13-16

Po pobraniu współczynnika ``a`` od użytkownika tworzymy wyrażenie listowe
wyliczające drugą dziedzinę wartości. Następnie do argumentów przekazywanych
funkcji ``plot()`` dodajemy drugę parę list. Spróbuj uruchomić program.

Nie działa, dostajemy komunikat *ValueError: x and y must have same first dimension*,
czyli listy wartości *x* i *y* w którejś z par nie zawierają tyle samo elementów.

Ćwiczenie 3
============

Przetestujmy kod w konsoli Pythona:

.. code-block:: python

    >>> import pylab
    >>> x = pylab.frange(-10, 11, 0.5)
    >>> y1 = [i**2/3 for i in x if i < 1 or i > 0]
    >>> len(x) == len(y1)
    >>> a = 2
    >>> y2 = [i/-3 + a for i in x if i <= 0]
    >>> len(x) == len(y2)
    >>> len(x)
    >>> len(y2)

Uwaga: nie zamykaj tej sesji konsoli, zaraz się nam jeszcze przyda.

Szybko zauważymy, że lista ``y2`` zawiera mniej wartości niż dziedzina ``x``.
Co należy z tym zrobić? Jak wynika z warunków zadania, wartości *y2* obliczane
są tylko dla argumentów mniejszych od zera. Zatem trzeba ograniczyć listę
*x*, tak aby zawierała tylko wartości z odpowiedniego przedziału.
Wróćmy do konsoli Pythona:

Ćwiczenie 4
============

.. code-block:: python

    >>> x
    >>> x[0]
    >>> x[0:5]
    >>> x[:5]
    >>> x[:len(y2)]
    >>> len(x[:len(y2)])

Z pomocą przychodzi nam wydobywanie z listy wartości wskazywanych przez
indeksy liczone od 0. Jednak prawdziwym ułatwieniem jest notacja wycinania
(ang. *slice*), która pozwala podać pierwszy i ostatni indeks interesującego
nas zakresu. Zmieniamy więc wywołanie funkcji ``plot()``:

.. code-block:: python

    pylab.plot(x,y1,x[:len(y2)],y2)

Uruchom i przetestuj działanie programu.

Ćwiczenie 5
============

Spróbuj samodzielnie przygotować wykres funkcji kwadratowej:
*f(x) = a*x^2 + b*x + c*, gdzie *x* = <-10;10> z krokiem 1, przyjmij następujące
wartości współczynników: *a = 1, b = -3, c = 1*.

Uzyskany wykres powinien wyglądać następująco:

.. figure:: img/pylab01.png

.. raw:: html

    <hr />

Jeżli masz ochotę na więcej, daj znać!
