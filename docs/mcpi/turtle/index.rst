.. _mcpiturtle:

Żółw w przestrzeni
###################

Bilioteka `minecraftturtle <http://www.stuffaboutcode.com/2014/05/minecraft-graphics-turtle.html>`_
implementuje tzw. grafikę zółwia (ang. *turtle graphics*) w trzech wymiarach. W praktyce ułatwia więc
budowanie konstrukcji przestrzennych. Inspirowana jest wbudowaną w Pythona biblioteką
`turtle <https://docs.python.org/2/library/turtle.html>`_, często wykorzystywaną do
nauki programowania najmłodszych. Poniżej pokażemy, jak poruszać się "żółwiem" w przestrzeni.

**Instalacja**

Symulator ``mcpi-sim`` domyślnie nie działa z omawianą biblioteką i wymaga modyfikacji.
Zmienione pliki oraz omawianą bibliotekę umieściliśmy w archiwum
:download:`mcpi-sim-fix.zip <../mcpi-sim-fix.zip>`, które po ściągnięciu
należy rozpakować do katalogu :file:`~/mcpi-sim/local` nadpisując oryginalne pliki.

Kwadraty
=========

W pustym pliku :file:`mcsim-turtle.py` umieszczamy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsim-turtle01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-
    :emphasize-lines: 41-56

Początek kodu omawialiśmy już w :ref:`Podstawach <mcpipodstawy>`. W podświetlonym fragmencie
przede wszystkim importujemy omawianą bibliotekę oraz klasę *Vec3* reprezentującą położenie
w MC. Polecenie ``turtle = mcturtle.MinecraftTurtle(mc, start)`` tworzy obiekt "żółwia",
którym będziemy mogli sterować za pomocą kilku metod.

W powyższym kodzie używamy następujących metod:

- ``speed()`` – ustawia prędkość budowania: 0 – brak animacji, 1 – b. wolno, 10 – najszybciej;
- ``penblock()`` – ustawienie bloku, którym budujemy ślad;
- ``forward(x)`` – idź do przodu o *x* "kroków";
-  ``right(x)``, ``left(x)`` – obróć się w prawo/lewo o *x* stopni;

Okna
======

Do funkcji ``main()`` dopisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsim-turtle.py
    :linenos:
    :lineno-start: 58
    :lines: 58-76

W podanym kodzie mamy kilka nowych metod:

- ``setposition(x, y, z)`` – ustawia "żółwia" na podanej pozycji;
- ``up(x)`` – obróć się do góry o *x* stopni;
- ``down(x)`` – obróć się w dół o *x* stopni;

Szlaczek
========

Dopisz do funkcji ``main()`` podany kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsim-turtle.py
    :linenos:
    :lineno-start: 78
    :lines: 78-92

Nowe metody to:

- ``setx(x)``, ``setx(y)``, ``setx(z)`` – metody ustawiają składowe pozycji,
  jest też metoda ``position()``, która zwraca pozycję;
- ``penup()``, ``pendown()`` – podniesienie/opuszczenie "pędzla", dodatkowo funkcja ``isdown()``
  sprawdza, czy pędzel jest opuszczony;

.. figure:: img/mcsim-turtle.png

**Ćwiczenia**

1. Napisz kod, który zbuduje napis "KzK" podobny do pokazanego niżej.

	.. figure:: img/mcsim-turtKzK.png

2. Napisz kod, który zbuduje sześcian. Przekształć go w funkcję, która
buduje sześcian o podanej długości boku z podanego punktu.