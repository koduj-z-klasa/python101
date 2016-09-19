.. _mcpifigury:

Figury
#######

Możliwość programowego umieszczania różnych bloków w Minecraft Pi Edition
można wykorzystać jako atrakcyjny sposób wizualizacji różnych figur. Jednak
o ile budowanie prostych kształtów, jak np. kwadrat czy sześcian, nie stanowi
raczej problemu, o tyle trójkąty, koła i bardziej skomplikowane figury 3D
nie są trywialnym zadaniem. Dużym ułatwienim w konstruowaniu bardziej skomplikowanych
budowli będzie 2-wymiarowa biblioteka `minecraftstuff <http://www.stuffaboutcode.com/2013/11/coding-shapes-in-minecraft.html>`_ oraz 3-wymiarowa `minecraftturtle <http://www.stuffaboutcode.com/2014/05/minecraft-graphics-turtle.html>`_.

**Instalacja**

Symulator ``mcpi-sim`` domyślnie nie działa z omawianymi bibliotekami i wymaga modyfikacji.
Dla ułatwienia przygotowaliśmy więc archiwum :download:`mcpi-sim-fix.zip <mcpi-sim-fix.zip>`,
które po ściągnięciu należy rozpakować do katalogu :file:`~/mcpi-sim/local` nadpisując oryginalne pliki.
Archiwum zawiera również omawiane biblioteki.

.. note::

	Kod bibliotek znajdziemy w repozytoriach serwisu GitHub: `rep. minecraftstuff <https://github.com/martinohanlon/minecraft-stuff>`_ i `rep. minecraftturtle <https://github.com/martinohanlon/minecraft-turtle>`_ w serwisie GitHub.

Kształty 2D
===========

W pustym pliku :file:`mcsim2d.py` umieszczamy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsim2d01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-
    :emphasize-lines: 44-54

Większość kodu omówiona została w :ref:`Podstawach <mcpipodstawy>`, nowy kod został podświetlony.

Figury 3D
=========

Biblioteka ``minecraftturtle`` inspirowana jest wbudowaną w Pythona biblioteką
`turtle <https://docs.python.org/2/library/turtle.html>`_, często wykorzystywaną do
nauki programowania dzieci. Jednak tu "żółw" może poruszać się w przestrzeni.

W pustym pliku :file:`mcsim3d.py` umieszczamy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsim3d01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-
    :emphasize-lines: 44-86

Większość kodu omówiona została w :ref:`Podstawach <mcpipodstawy>`, nowy kod został podświetlony.

[cdn]

**Źródła:**

* :download:`Skrypty mcsimfig <mcsimfig.zip>`