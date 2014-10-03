Gra w Kółko i Krzyżyk
=====================

Klasyczna gra w kółko i krzyżyk zrealizowana przy pomocy  `PyGame`_.

.. _PyGame: http://www.pygame.org/wiki/tutorials

.. figure:: screen1.png

Przygotowanie
-------------

Do rozpoczęcia pracy z przykładem pobieramy szczątkowy kod źródłowy:

.. code-block:: bash

    ~/python101$ git checkout -f tic_tac_toe/z1


Okienko gry
-----------

Na wstępie w pliku ``~/python101/games/tic_tac_toe.py`` otrzymujemy kod który przygotuje okienko naszej gry:

.. note::

    Ten przykład zakłada wcześniejsze zrealizowanie przykładu: :doc:`../life/index`,
    opisy niektórych cech wspólnych zostały tutaj wyraźnie pominięte.
    W tym przykładzie wykorzystujemy np. podobne mechanizmy do tworzenia okna i
    zarządzania główną pętlą naszej gry.

.. warning::

    TODO: Wymaga rozbicia i uzupełnienia opisów

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: code0.py
    :linenos:


W powyższym kodzie mamy podstawy potrzebne do uruchomienia gry:

.. code-block:: bash

    ~/python101$ python games/life.py

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>

.. include:: ../copyright.rst
