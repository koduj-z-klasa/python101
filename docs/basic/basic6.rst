Nie znam Pythona... jeszcze
=================================

Wyrażenia listowe
-----------------

Wypróbuj w konsoli podane przykłady wyrażeń listowych (ang. *list comprehensions*) Pythona:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    # lista kwadratów liczb od 0 do 9
    [x**2 for x in range(10)]

    # lista dwuwymiarowa [20,40] o wartościach a
    a = int(raw_input("Podaj liczbę całkowtią: "))
    [[a for y in xrange(20)] for x in xrange(40)]

    # lista krotek (x, y), przy czym x != y
    [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

Pliki
-----------------

Przećwicz alternatywne spsoby otwierania plików:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    f = open('test.txt', 'r')
    for line in f:
        print line[0]
    f.close()

    with open("text.txt", "r") as txt:
        for line in txt:
            print line

    for line in open('test.txt', 'r'):
        print line[0]

Materiały w sieci
--------------------

Warto odwiedzić:

1. http://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie
2. http://brain.fuw.edu.pl/edu/TI:Programowanie_z_Pythonem
3. http://pl.python.org/docs/tut/
4. http://en.wikibooks.org/wiki/Python_Programming/Input_and_Output
5. https://wiki.python.org/moin/HandlingExceptions
6. http://learnpython.org/pl
7. http://www.checkio.org
8. http://www.codecademy.com
9. https://www.coursera.org

Metryka
^^^^^^^

:Autor: Robert Bednarz <ecg@ecg.vot.pl>

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>


.. include:: ../copyright.rst
