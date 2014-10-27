Nie znam Pythona... jeszcze
=================================

POĆWICZ SAM
-----------

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
