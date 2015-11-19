.. _pylab:

Python kreśli
################

Jedną z potężniejszych bibliotek Pythona jest `matplotlib <http://pl.wikipedia.org/wiki/Matplotlib>`_,
która służy do tworzenia różnego rodzaju wykresów. *Pylab* to :term:`API` ułatwiające
korzystanie z omawianej biblioteki na wzór środowiska `Matlab <http://pl.wikipedia.org/wiki/MATLAB>`_.
Poniżej pokazujemy, jak łatwo przy użyciu Pythona wizualizować wykresy różnych
funkcji.

W systemach Linux instalacja biblioteki sprowadza się do użycia polecenia:

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: bash

    ~$ sudo pip install matplotlib

W systemach Windows bibliotekę instalujemy zgodnie z opisem :ref:`przygotowania środowiska <windows-env>`.

.. contents::
    :depth: 1
    :local:

Funkcja liniowa
***************

Zabawę zacznijmy w konsoli Pythona:

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

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

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

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
    :lines: 6-12

Dwie funkcje
*************

ZADANIE: wykonaj wykres funkcji:

* *f(x) = x/(-3) + a* dla *x* <= 0,
* *f(x) = x\*x/3* dla *x* >= 0,

– gdzie *x* = <-10;10> z krokiem 0.5. Współczynnik *a* podaje użytkownik.

Wykonanie zadania wymaga umieszczenia na wykresie dwóch funkcji.
Wykorzystamy funkcję ``arange()``, która zwraca listę wartości
zmiennoprzecinkowych (zob. typ :term:`typy danych`) z zakresu określonego przez
dwa pierwsze argumenty i z krokiem wyznaczonym przez argument trzeci.
Drugą przydatną konstrukcją będzie wyrażenie listowe uzupełnione o instrukcję
warunkową, która ogranicza wartości, dla których obliczane jest podane wyrażenie.

Ćwiczenie 3
============

Zanim zrealizujemy zadanie przećwiczmy w konsoli Pythona następujący kod:

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    >>> import pylab
    >>> x = pylab.arange(-10, 10.5, 0.5)
    >>> x
    >>> len(x)
    >>> a = 3
    >>> y1 = [i / -3 + a for i in x if i <= 0]
    >>> len(y1)

Uwaga: nie zamykaj tej sesji konsoli, zaraz się nam jeszcze przyda.

W pliku :file:`pylab02.py` umieszczamy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pylab03.py
    :linenos:

Uruchom program. Nie działa, dostajemy komunikat:
*ValueError: x and y must have same first dimension*,
czyli listy wartości *x* i *y1* nie zawierają tyle samo elementów.

Co należy z tym zrobić? Jak wynika z warunków zadania, wartości *y1* obliczane
są tylko dla argumentów mniejszych od zera. Zatem trzeba ograniczyć listę
*x*, tak aby zawierała tylko wartości z odpowiedniego przedziału.
Wróćmy do konsoli Pythona:

Ćwiczenie 4
============

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    >>> x
    >>> x[0]
    >>> x[0:5]
    >>> x[:5]
    >>> x[:len(y1)]
    >>> len(x[:len(y1)])

Uwaga: nie zamykaj tej sesji konsoli, zaraz się nam jeszcze przyda.

Z pomocą przychodzi nam wydobywanie z listy wartości wskazywanych przez
indeksy liczone od 0. Jednak prawdziwym ułatwieniem jest **notacja wycinania**
(ang. *slice*), która pozwala podać pierwszy i ostatni indeks interesującego
nas zakresu. Zmieniamy więc wywołanie funkcji ``plot()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    pylab.plot(x[:len(y1)], y1)

Uruchom i przetestuj działanie programu.

Udało się nam zrealizować pierwszą część zadania.
Spróbujmy zakodować część drugą. Dopisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pylab04.py
    :linenos:
    :lineno-start: 14
    :lines: 14-16

Wyrażenie listowe wylicza nam drugą dziedzinę wartości. Następnie do argumentów
funkcji ``plot()`` dodajemy drugę parę list. Spróbuj uruchomić program.
Nie działa, znowu dostajemy komunikat: *ValueError: x and y must have same first dimension*.
Teraz jednak wiemy już dlaczego...

Ćwiczenie 5
============

Przetestujmy kod w konsoli Pythona:

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    >>> len(x)
    >>> x[-10]
    >>> x[-10:]
    >>> len(y2)
    >>> x[-len(y2):]

Jak widać, w **notacji wycinania** możemy używać indeksów ujemnych wskazujących
elementy od końca listy. Jeżeli taki indeks umieścimy jako pierwszy przed
dwukropkiem, czyli separatorem przedziału, dostaniemy resztę elementów listy.

Na koniec musimy więc zmodyfikować funkcję ``plot()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    pylab.plot(x[:len(y1)], y1, x[-len(y2):], y2)

Ćwiczenie 6
============

Spróbuj dziedziny wartości *x* dla funkcji *y1* i *y2* wyznaczyć nie za pomocą
notacji wycinkowej, ale przy użyciu wyrażeń listowych, których wynik przypisz
do zmiennych *x1* i *x2*. Użyj ich jako argumentów funkcji ``plot()`` i przetestuj
program.

Ruchy Browna
***************

Napiszemy program, który symuluje `ruchy Browna <https://pl.wikipedia.org/wiki/Ruchy_Browna>`_. Jak wiadomo są to chaotyczne ruchy cząsteczek, które będziemy mogli zwizualizować w płaszczyźnie dwuwymiarowej.
Na początku przyjmujemy następujące założenia:

* cząsteczka, której ruch będziemy śledzić, znajduje się w początku układu współrzędnych (0, 0);
* w każdym ruchu cząsteczka przemieszcza się o stały wektor o wartości 1;
* kierunek ruchu wyznaczać będziemy losując kąt z zakresu <0; 2Pi>;
* współrzędne kolejnego położenia cząsteczki wyliczać będziemy ze wzorów:

.. math::

    x_n = x_{n-1} + r * cos(\phi)

    y_n = y_{n-1} + r * sin(\phi)


– gdzie: *r* – długość jednego kroku, :math:`\phi` – kąt wskazujący kierunek ruchu w odniesieniu do osi *OX*.

* końcowy wektor przesunięcia obliczymy ze wzoru: :math:`|s| = \sqrt{(x^2 * y^2)}`

Zacznijmy od wyliczenia współrzędnych opisujących ruch cząsteczki. Do pustego pliku o nazwie :file:`rbrowna.py` wpisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rbrowna01.py
    :linenos:

Funkcje trygonometryczne zawarte w module ``math`` wymagają kąta podanego w radianach,
dlatego wylosowany kąt po zamianie na liczbę zmiennoprzecinkową mnożymy przez wyrażenie
``math.pi / 180``. Uruchom i przetestuj kod.

Do przygotowania wykresu ilustrującego ruch cząsteczeki generowane współrzędne musimy
zapisać w listach. Dopiszmy więc następujący kod:



Zadania dodatkowe
*****************

Przygotuj wykres funkcji kwadratowej:
*f(x) = a*x^2 + b*x + c*, gdzie *x* = <-10;10> z krokiem 1, przyjmij następujące
wartości współczynników: *a = 1, b = -3, c = 1*.

Uzyskany wykres powinien wyglądać następująco:

.. figure:: img/pylab01.png

Źródła
*******************

* :download:`pylab.zip <pylab.zip>`

Kolejne wersje tworzonych skryptów znajdziesz w katalogu ``~/python101/pylab``.
Uruchamiamy je wydając polecenia:

.. code-block:: bash

    ~/python101$ cd pylab
    ~/python101/pylab$ python pylab0x.py

\- gdzie *x* jest numerem kolejnej wersji kodu.