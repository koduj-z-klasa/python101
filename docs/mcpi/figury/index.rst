.. _mcpifigury:

Figury 2D i 3D
###############

Możliwość programowego umieszczania różnych bloków w Minecraft Pi Edition
można wykorzystać jako atrakcyjny sposób wizualizacji różnych figur. Jednak
o ile budowanie prostych kształtów, jak np. kwadrat czy sześcian, nie stanowi
raczej problemu, o tyle trójkąty, koła i bardziej skomplikowane budowle
nie są trywialnym zadaniem. Tworzenie 2- i 3-wymiarowych konstrukcji ułatwi
nam biblioteka `minecraftstuff <http://www.stuffaboutcode.com/2013/11/coding-shapes-in-minecraft.html>`_.

**Instalacja**

Symulator ``mcpi-sim`` domyślnie nie działa z omawianą biblioteką i wymaga modyfikacji.
Zmienione pliki oraz omawianą bibliotekę umieściliśmy w archiwum
:download:`mcpi-sim-fix.zip <../mcpi-sim-fix.zip>`, które po ściągnięciu
należy rozpakować do katalogu :file:`~/mcpi-sim/local` nadpisując oryginalne pliki.


Linia
===========

W pustym pliku :file:`mcsim-fig.py` umieszczamy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsim-fig01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-
    :emphasize-lines: 41-59

Większość kodu omówiona została w :ref:`Podstawach <mcpiplac>`. W nowym kodzie, który został podświetlony,
importujemy bibliotekę *minecraftstuff* oraz klasę *Vec3*. Reprezentuje ona pozycję o podanych
współrzędnych w trójwymiarowym świecie MC. Polecenie ``figura = mcstuff.MinecraftDrawing(mc)`` tworzy instancję
głównej klasy biblioteki, która udostępni jej metody.

Do rysowania linii wykorzystujemy metodę ``drawLine()``, której przekazujemy jako argumenty
współrzędne punktu początkowego i końcowego, a także typ bloku i ewentualnie podtyp.
Współrzędne punktów końcowych zostały zapisane w dwóch tuplach (niemodyfikowalnej liście) jako tuple.
Rozpakowujemy je w pętlach (``x, y, z = punkt``) i przekazujemy do konstruktora klasy ``Vec3``
(``p2 = Vec3(x, y, z)``).

Koło
=====

Na końcu funkcji ``main()`` dodaj kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsim-fig.py
    :linenos:
    :lineno-start: 61
    :lines: 61-63

Metoda ``drawCircle()`` pozwala na rysowanie koła. Pierwsze trzy argumenty to współrzędne
środka, kolejne to: promień, typ i ewentualny podtyp bloku.

Kula
====

Do funkcji ``main()`` dopisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsim-fig.py
    :linenos:
    :lineno-start: 65
    :lines: 65-67

Metoda ``drawSphere()`` buduje kulę. Pierwsze trzy argumenty to współrzędne
środka, kolejne to: promień, typ i ewentualny podtyp bloku.

Kształt
=======

Do funkcji ``main()`` dodajemy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsim-fig.py
    :linenos:
    :lineno-start: 69
    :lines: 69-74

Powyżej do listy ``ksztalt`` dodajemy kolejne punkty w instrukcjach typu ``ksztalt.append(Vec3(-11, 0, 11))``.
Na koniec wywołujemy metodę ``drawFace()``, która punkty przekazane w liście łączy
liniami budowanymi z podanego bloku. Drugi argument, logiczny, decyduje o tym, czy figura
ma zostać wypełniona (``True``), czy nie (``False``).

.. figure:: img/mcsim-fig.png

**Ćwiczenie 1**

Wykorzystując odpowiednią metodę biblioteki *minecraftstuff*,
spróbuj zbudować napis "KzK" podobny do pokazanego poniżej.
Przetestuj swój kod w symulatorze i w Minecrafcie Pi.

.. figure:: img/mcsim-KzK.png

