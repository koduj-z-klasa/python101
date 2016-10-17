.. _mcpifunkcje:

Funkcje w mcpi
##############

O Minecrafcie w wersji na Raspberry Pi myśleć można jak o atrakcyjnej formie
wizualizacji tego co można przedstawić w grafice dwu- lub trójwymiarowej.
Zobaczmy zatem jakie budowle otrzymamy, wyliczając współrzędne bloków
za pomocą funkcji matematycznych. Przy okazji niejako przypomnimy sobie
użycie opisywanej już w naszych scenariuszach biblioteki :ref:`matplotlib <pylab>`,
która jest dedykowanym dla Pythona środowiskiem tworzenia wykresów 2D.

Funkcja liniowa
===============

Za pomocą wybranego edytora utwórz pusty plik, umieść w nim podany niżej kod i zapisz
w katalogu :file:`mcpi-sim` pod nazwą :file:`mcpi-funkcje.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-funkcje01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-


Większość kodu powinna być już zrozumiała, czyli importy bibliotek, nawiązywania połączenia
z serwerem MC Pi, czy funkcja ``plac()`` tworząca przestrzeń do testów.
Podobnie funkcja ``wykres()``, która pokazuje nam graficzną reprezentację funkcji
za pomocą biblioteki *matblotlib*. Na uwagę zasługuje w niej tylko parametr ``*extra``,
który pozwala przekazać argumenty i wartości dodatkowej funkcji.

Funkcja ``fun1()`` pobiera od użytkownika dwa współczynniki i odwzorowuje argumenty
z dziedziny <-10;10> na wartości wg liniowego równania: ``f(x) = a * x + b``.
Przeciwdziedzinę można byłoby uzyskać "na piechotę" za pomocą kodu:

.. code-block:: python

    y = []
    for i in x:
        y.append(a * i + b)

– ale efektywniejsze jest :term:`wyrażenie listowe`: ``y = [a * i + b for i in x]``.
Po zobrazowaniu wykresu za pomocą funkcji funkcji ``wykres()`` i biblioteki *matplotlib*
"budujemy" ją w MC Pi w pętli odczytującej wyliczone pary argumentów i wartości funkcji,
stanowiących współrzędne kolejnych bloków umieszczanych poziomo.

Uruchom i przetestuj omówiony kod podając współczynniki np. *4* i *6*.


Układ współrzędnych
===================

Spróbujmy pokazać w Mc Pi układ współrzędnych oraz ułatwić "budowanie" wykresów
za pomocą osobnej funkcji. Po funkcji ``plac()`` umieszczamy w pliku :file:`mcpi-funkcje.py` nowy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-funkcje02.py
    :linenos:
    :lineno-start: 37
    :lines: 37-59

– a kod tworzący wykres funkcji liniowej w MC Pi zmieniamy na:

.. code-block:: python

    rysuj(x, y, [1], blok)

Funkcja ``rysuj()`` potrafi zbudować bloki zarówno w poziomie, jak i w pionie w zależności
od tego, czy lista wartości funkcji przekazana zostanie jako parametr *y* czy też *z*.
Do rozpoznania tego wykorzystujemy zmienną sterującą ustawianą w instrukcji: ``czylista = True if len(y) > 1 else False``.

Zawartość funkcji ``main()`` zmieniamy na:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-funkcje02.py
    :linenos:
    :lineno-start: 91
    :lines: 91-98

Po uruchomieniu zmienionego kodu powinniśmy zobaczyć wykres naszej funkcji w pionie.

.. figure:: img/mcpi-funkcje02.png

Kod "budujący" wykresy funkcji możemy urozmaicić wykorzystując poznaną wcześniej
bibliotekę :ref:`minecraftstuff <mcpifigury>`. Poniżej funkcji ``rysuj()`` dodajemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-funkcje03.py
    :linenos:
    :lineno-start: 62
    :lines: 62-83

– a wywołanie ``rysuj()`` w funkcji ``fun1()`` zmieniamy na ``rysuj_linie()``.
Sprawdź rezultat.

Kolejne funkcje
===============

W pliku :file:`mcpi-funkcje.py` tuż nad funkcją główną ``main()`` umieszczamy kod
wyliczający dziedziny i przeciwdziedziny dwóch kolejnych funkcji:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-funkcje04.py
    :linenos:
    :lineno-start: 115
    :lines: 115-159

W funkcji ``fun2()`` wartości dziedziny uzyskujemy dzięki metodzie ``arange(start, stop, step)`` z biblioteki *numpy*. Potrafi ona generować listę wartości zmiennopozycyjnych w podanym zakresie <*start;stop*) z określonym krokiem *step*.

Przeciwdziedzinę wyliczamy w pętli w zależności od przedziałów, w których znajdują się argumenty,
za pomocą złożonej instrukcji warunkowej. Następnie wartości zarówno dziedziny, jak i przeciwdziedziny
przeskalowujemy w wyrażeniach listowych, mnożąc przez stały współczynnik,
aby wykres w MC Pi był większy i wyraźniejszy. Przy okazji współrzędne zaokrąglamy
do dwóch miejsc po przecinku, np.: ``x = [round(i * 20, 2) for i in x]``.

Zmieniamy też nieco wywołania w funkcji głównej. Przetestuj podany kod.

.. figure:: img/mcpi-funkcje04.png

[todo]