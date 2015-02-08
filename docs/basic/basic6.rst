Nie znam Pythona... jeszcze
=================================

Python jest językiem wydajnym i zwartym dzięki wbudowanym mechanizmom
ułatwiającym wykonywanie typowych i częstych zadań programistycznych.
Podane niżej **przykłady należy przećwiczyć w konsoli Pythona**, którą
uruchamiamy poleceniem w terminalu:

.. code-block:: bash

    ~$ python
    
Operatory **\*** i **\*\***
----------------------------

Operator ``*`` służy rozpakowaniu listy zawierającej wiele argumentów, które chcemy
przekazać do funkcji:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:
    
    #wygeneruj liczby parzyste od 2 do 10
    lista = [2,11,2]
    range(*lista)

Operator ``**`` potrafi z kolei rozpakować słownik, dostarczając funkcji
nazwanych argumentów (ang. *keyword argument*):

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:
    
    def kalendarz(data, wydarzenie):
        print "Data:", data,"\nWydarzenie:", wydarzenie
    
    slownik = {"data" : "10.02.2015", "wydarzenie" : "szkolenie"}
    kalendarz(**slownik)

Iteratory
---------------

Iteratory to obiekty reprezentujące strumień danych, z którego zwracają
tylko jedną kolejną wartość na raz za pomocą metody ``__next()__``. Jeżeli
w strumieniu nie ma więcej danych wywoływany jest wyjątek ``StopIteration``.

Wbudowana funkcja ``iter()`` zwraca iterator utworzony z dowolnego iterowalnego
obiektu. Iteratory wykorzystujemy do przeglądania list, tupli, słowników czy plików
używając instrukcji ``for x in y``, w której *y* jest obiektem iterowalnym równoważnym
wyrażeniu ``iter(y)``. Np.:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    lista = [2, 4, 6]
    for x in lista:
        print x

    slownik = {'Adam':1, 'Bogdan':2 , 'Cezary':3}
    for x in slownik:
        print(x, slownik(x))

Listę (czyli obiekt iterowalny), zawierającą tuple (klucz, wartość) można wykorzystać
do utworzenia słownika, np.:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    lista = [('Polska','Warszawa'), ('Berlin','Niemcy'), ('Francja','Paryż')]
    dict(lista)

Generatory wyrażeń
-------------------

Jeżeli potrzebujemy wykonać jakąś operację na każdym elemencie sekwencji lub
chcemy wybrać podzespół elementów spełniający określone warunki, stosujemy
generatory wyrażeń (ang. *generator expressions*), które zwracają iteratory, np.:

.. code-block:: python
    :linenos:

    wyrazy = ['anna', 'ala', 'ela', 'wiola', 'ola']
    imiona = (imie.capitalize() for imie in wyrazy)
    for imie in imiona:
        print imie

Powyższy wydrukuje wszystkie imiona z dużej litery. Gdybyśmy chcieli wybrać
tylko imiona 3-literowe w wyrażeniu użylibyśmy opcjonalnej klauzuli ``if (warunek)``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    imiona = (imie.capitalize() for imie in wyrazy if len(imie) == 3)

Omawiane wyrażenia można zagnieżdzać. Przykłady podajemy niżej.

Wyrażenia listowe
-------------------

Jeżeli nawiasy okrągłe w generatorze wyrażeń zamienimy na kwadratowe dostaniemy
wyrażenie listowe (ang. *list comprehensions*), które – jak wskazuje nazwa –
zwracają listy:

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

Wyrażenia listowe w elegancki i wydajny sposób zastępują takie rozwiązania, jak:
    
    * :term:`pętle`
    * :term:`mapowanie funkcji`
    * :term:`wyrażenia lambda`
    * :term:`filtrowanie danych`

Pętle
^^^^^^^^^^^^^^^

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:
    
    kwadraty = []
    for x in range(10):
        kwadraty.append(x**2)


Mapowanie funkcji
^^^^^^^^^^^^^^^^^^^^

Funkcja ``map()`` funkcję podaną jako pierwszy argument stosuje do każdego elementu sekwencji
podanej jako argument drugi:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    def kwadrat(x):
        return x**2
    
    kwadraty = map(kwadrat, range(10))

Wyrażenia lambda
^^^^^^^^^^^^^^^^^^

Słowa kluczowe ``lambda`` pozwala utworzyć zwięzły odpowiednik prostej, jednowyrażeniowej
funkcji. Poniższy przykład należy rozumieć następująco: do każdej liczby wygenerowanej
przez funkcję ``range()`` zastosuj funkcję w postaci wyrażenia lambda podnoszącą
wartość do kwadratu, a uzyskane wartości zapisz w liście ``kwadraty``.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    kwadraty = map(lambda x: x**2, range(10))

Filtrowanie danych
^^^^^^^^^^^^^^^^^^^

Funkcja ``filter()`` jako pierwszy argument pobiera funkcję zwracającą ``True`` lub ``False``,
stosuje ją do każdego elementu sekwencji podanej jako argument drugi i zwraca tylko te,
które spełniają założony warunek:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    wyrazy = ['anna', 'ala', 'ela', 'wiola', 'ola']
    imiona = filter(lambda imie: len(imie) == 3, wyrazy)

Generatory
-------------------

    Objaśnienie mechanizmów generatorów.

Pliki
-----------------

Przećwicz alternatywne sposoby otwierania plików:

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

Słownik
^^^^^^^^

.. glossary::

    pętle
        podstawowa konstrukcja w programowania strukturalnego pozwalająca
        wielokrotnie wykonywać zawarte w niej instrukcje
        
    mapowanie funkcji
        w kontekście funkcji ``map()`` oznacza zastosowanie danej funkcji
        do wszystkich dostarczonych wartości
        
    wyrażenia lambda
        zwane czasem *funkcjami lambda*, mechanizm pozwalający zwięźle
        zapisywać proste funkcje w postaci pojedynczych wyrażeń
        
    filtrowanie danych
        selekcja danych na podstawie jakichś kryteriów

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
