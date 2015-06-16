Pythonizmy
###########

.. contents::
    :depth: 1
    :local:

Python jest językiem wydajnym i zwartym dzięki wbudowanym mechanizmom
ułatwiającym wykonywanie typowych i częstych zadań programistycznych.
Podane niżej **przykłady należy przećwiczyć w konsoli Pythona**, którą
uruchamiamy poleceniem w terminalu:

.. code-block:: bash

    ~$ python

Operatory **\*** i **\*\***
********************************

Operator ``*`` służy rozpakowaniu listy zawierającej wiele argumentów, które chcemy
przekazać do funkcji:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    # wygeneruj liczby parzyste od 2 do 10
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

Pętle
************************

Pętla to podstawowa konstrukcja wykorzystywana w językach programowania.
Python oferuje różne sposoby powtarzania wykonywania określonych operacji,
niekiedy wygodniejsze lub zwięźlejsze niż pętle. Są to przede wszystkim
generatory wyrażeń i wyrażenia listowe, a także funkcje ``map()`` i ``filter()``.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    kwadraty = []
    for x in range(10):
        kwadraty.append(x**2)

Iteratory
***************

Obiekty, z których pętle odczytują kolejne dane to :term:`iteratory` (ang. *iterators*)
Reprezentują one strumień danych, z którego zwracają tylko jedną kolejną
wartość na raz za pomocą metody ``__next()__``. Jeżeli w strumieniu nie ma
więcej danych, wywoływany jest wyjątek ``StopIteration``.

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
************************

Jeżeli chcemy wykonać jakąś operację na każdym elemencie sekwencji lub
wybrać podzespół elementów spełniający określone warunki, stosujemy
:term:`generatory wyrażeń` (ang. *generator expressions*), które zwracają iteratory.
Poniższy przykład wydrukuje wszystkie imiona z dużej litery:

.. code-block:: python
    :linenos:

    wyrazy = ['anna', 'ala', 'ela', 'wiola', 'ola']
    imiona = (imie.capitalize() for imie in wyrazy)
    for imie in imiona:
        print imie

Schemat składniowy generatora jest następujący:
``( wyrażenie for wyr in sekwencja if warunek )`` – przy czym:

- ``wyrażenie`` – powinno zawierać zmienną z pętli for
- ``if warunek`` – klauzula ta jest opcjonalna i działa jak filtr eliminujący
  wartości nie spełniające warunku

Gdybyśmy chcieli wybrać tylko imiona 3-literowe w wyrażeniu, użyjemy wspomnianej
opcjonalnej klauzuli ``if warunek``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    imiona = (imie.capitalize() for imie in wyrazy if len(imie) == 3)

Omawiane wyrażenia można zagnieżdzać. Przykłady podajemy niżej.

Wyrażenia listowe
***********************

Jeżeli nawiasy okrągłe w generatorze wyrażeń zamienimy na kwadratowe dostaniemy
:term:`wyrażenie listowe` (ang. *list comprehensions*), które – jak wskazuje nazwa –
zwraca listę:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    # wszystkie poniższe wyrażenia listowe możemy przypisać do zmiennych,
    # aby móc później korzystać z utworzonych list

    # lista kwadratów liczb od 0 do 9
    [x**2 for x in range(10)]

    # lista dwuwymiarowa [20,40] o wartościach a
    a = int(raw_input("Podaj liczbę całkowtią: "))
    [[a for y in xrange(20)] for x in xrange(40)]

    # lista krotek (x, y), przy czym x != y
    [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

    # utworzenie listy 3-literowych imion i ich pierwszych liter
    wyrazy = ['anna', 'ala', 'ela', 'wiola', 'ola']
    [ [imie, imie[0]] for imie in wyrazy if len(imie) == 3 ]

    # zagnieżdzone wyrażenie listowe tworzące listę współrzędnych
    # opisujących tabelę
    [ (x,y) for x in range(5) for y in range(3) ]

    # zagnieżdzone wyrażenie listowe wykorzystujące filtrowanie danych
    # lista kwadratów z zakresu {5;50}
    [ y for y in [ x**2 for x in range(10) ] if y > 5 and y < 50 ]

Wyrażenia listowe w elegancki i wydajny sposób zastępują takie rozwiązania, jak:

    * :term:`pętla`
    * :term:`mapowanie funkcji`
    * :term:`wyrażenia lambda`
    * :term:`filtrowanie danych`

.. _map-fun:

Mapowanie funkcji
==========================

Funkcja ``map()`` funkcję podaną jako pierwszy argument stosuje do każdego elementu sekwencji
podanej jako argument drugi:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    def kwadrat(x):
        return x**2

    kwadraty = map(kwadrat, range(10))

.. _lambda:

Wyrażenia lambda
==========================

Słowo kluczowe ``lambda`` pozwala utworzyć zwięzły odpowiednik prostej, jednowyrażeniowej
funkcji. Poniższy przykład należy rozumieć następująco: do każdej liczby wygenerowanej
przez funkcję ``range()`` zastosuj funkcję w postaci wyrażenia lambda podnoszącą
wartość do kwadratu, a uzyskane wartości zapisz w liście ``kwadraty``.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    kwadraty = map(lambda x: x**2, range(10))

Funkcje *lambda* często stosowane są w poleceniach sortowania jako wyrażenie
zwracające klucz (wartość), wg którego mają zostać posortowane elementy.
Jeżeli np. mamy listę tupli opisującą uczniów:

.. code-block:: python
    :linenos:

    uczniowie = [
        ('jan','Nowak','1A',15),
        ('ola','Kujawiak','3B',17),
        ('andrzej','bilski','2F',16),
        ('kamil','czuja','1B',14)
    ]

–  wywołanie ``sorted(uczniowie)`` zwróci nam listę posortowaną wg pierwszego elementu
każdej tupli, czyli imienia. Jeżeli jednak chcemy sortować wg np. klasy,
użyjemy parametru ``key``, który przyjmuje jednoargumentową funkcję zwracającą
odpowiedni klucz do sortowania, np.: ``sorted(uczniowie, key=lambda x: x[2])``.

W funkcjach ``min()``, ``max()`` podobnie używamy wyrażeń *lambda* jako argumentu
parametru ``key``, aby wskazać wartości, dla których wyszukujemy minimum i maksimum, np.:
``max(uczniowie, key=lambda x: x[3])`` – zwróci najstarszego ucznia.

Filtrowanie danych
==========================

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
**************************

Generatory (ang. *generators*) to funkcje ułatwiające tworzenie iteratorów.
Od zwykłych funkcji różnią się tym, że:

    - zwracają iterator za pomocą słowa kluczowego ``yield``,
    - zapamiętują swój stan z momentu ostatniego wywołania, są więc wznawialne (ang. *resumable*),
    - zwracają następną wartość ze strumienia danych podczas kolejnych wywołań
      metody ``next()``.

Najprostszy przykład generatora zwracającego kolejne liczby parzyste:

.. code-block:: python

    def gen_parzyste(N):
        for i in range(N):
            if i % 2 == 0
                yield i

    gen = gen_parzyste(10)
    gen.next()
    gen.next()
    ...

Pliki
**************************

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


Materiały
**************************

1. http://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie
2. http://brain.fuw.edu.pl/edu/TI:Programowanie_z_Pythonem
3. http://pl.python.org/docs/tut/
4. http://en.wikibooks.org/wiki/Python_Programming/Input_and_Output
5. https://wiki.python.org/moin/HandlingExceptions
6. http://learnpython.org/pl
7. http://www.checkio.org
8. http://www.codecademy.com
9. https://www.coursera.org
