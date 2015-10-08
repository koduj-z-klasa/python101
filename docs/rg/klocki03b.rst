.. _klocki03b:

*RG* – klocki 3B
################

Robot dotychczasowy
*******************

Na podstawie reguł i klocków z części pierwszej mogliśmy stworzyć następującego
robota:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: robot_b.py
    :linenos:

Jego działanie opiera się na wyznaczeniu zbiorów pól określonego typu
zastosowaniu następujących reguł:

#. jeżeli nie ma nic lepszego, broń się,
#. z punktu wejścia idź bezpiecznie do środka;
#. atakuj wrogów wokół siebie, o ile to bezpieczne, jeżeli nie,
   idź bezpiecznie do środka;
#. atakuj wrogów dwa pola obok;
#. idź bezpiecznie na najbliższego wroga.

Spróbujemy go ulepszyć dodając, ale i prezycując reguły.

Śledź wybrane miejsca
**********************

Aby unikać niepotrzebnych kolizji, nie należy wchodzić na wybrane wcześniej pola.
Trzeba więc zapamiętywać pola wybrane w danej rundzie.

Przed klasą ``Robot`` definiujemy dwie zmienne globalne, następnie na początku
metody ``.act()`` inicjujemy dane:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # zmienne globalne
    runda_numer = 0 # numer rundy
    wybrane_pola = set() # zbiór wybranych w rundzie pól

    # inicjacja danych
    # wyzeruj zbiór wybrane_pola przy pierwszym robocie w rundzie
    global runda_numer, wybrane_pola
    if game.turn != runda_numer:
        runda_numer = game.turn
        wybrane_pola = set()

Do zapamiętywania wybranych w rundzie pól posłużą funkcje ``ruszaj()``
i ``stoj()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # jeżeli się ruszamy, zapisujemy docelowe pole
    def ruszaj(poz):
        wybrane_pola.add(poz)
        return ['move', poz]

    # jeżeli stoimy, zapisujemy zajmowane miejsce
    def stoj(act, poz=None):
        wybrane_pola.add(self.location)
        return [act, poz]

Ze zbioru ``bezpieczne`` wyłączamy wybrane pola i stosujemy nowe funkcje:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # ze zbioru bezpieczne wyłączamy wybrane_pola
    bezpieczne = sasiednie - wrogowie_obok - wrogowie_obok2 - \
                 wejscia - przyjaciele - wybrane_pola

    # stosujemy nowy kod w regule "atakuj wroga dwa pola obok"
    elif wrogowie_obok2 and self.location not in wybrane_pola:

    # stosujemy funkcje "ruszaj()" i "stoj()"

    # zamiast: ruch = ['move', mindist(bezpieczne, rg.CENTER_POINT)]
    ruch = ruszaj(mindist(bezpieczne, rg.CENTER_POINT))

    # zamiast: ruch = ['attack', wrogowie_obok.pop()]
    ruch = stoj('attack', wrogowie_obok.pop())

    # zamiast: ruch = ['move', mindist(bezpieczne, najblizszy_wrog)]
    ruch = ruszaj(mindist(bezpieczne, najblizszy_wrog))

.. tip::

    Można zapamiętywać wszystkie wybrane ruchy lub tylko niektóre. Przetestuj,
    czy ma to wpływ na skuteczność AI.

Atakuj najsłabszego
********************

Do tej pory atakowaliśmy przypadkowego robota wokół nas,
lepiej wybrać najsłabszego.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # funkcja znajdująca najsłabszego wroga obok
    def minhp(bots):
        return min(bots, key=lambda x: game.robots[x].hp)

    elif wrogowie_obok:
        ...
        else:
            ruch = stoj('attack', minhp(wrogowie_obok))

Funkcja ``minhp()`` poda nam położenie najsłabszego wroga. Argument
parametru ``key``, czyli wyrażenie :ref:`lambda <lambda>` zwraca właściwość
robotów, czyli punkty HP, wg której są porównywane.

Samobójstwo lepsze niż śmierć?
******************************

Jeżeli grozi nam śmierć, a nie ma bezpiecznego miejsca, aby uciec, lepiej
popełnić samobójstwo:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # samobójstwo lepsze niż śmierć
    elif wrogowie_obok:
        if bezpieczne:
            ...
        else:
            ruch = stoj('suicide')

Unikaj nierównych starć
************************

Nie warto walczyć z przeważającą liczbą wrogów.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    elif wrogowie_obok:
        if 9*len(wrogowie_obok) >= self.hp:
            ...
        elif len(wrogowie_obok) > 1:
            if bezpieczne:
                ruch = ruszaj(mindist(bezpieczne, rg.CENTER_POINT))
        else:
            ruch = stoj('attack', minhp(wrogowie_obok))

Goń najsłabszych
*****************

Zamiast atakować słabego uciekającego robota, lepiej go gonić, może
trafi w gorsze miejsce...

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    elif wrogowie_obok:
        ...
        else:
            cel = minhp(wrogowie_obok)
            if game.robots[cel].hp <= 5:
                ruch = ruszaj(cel)
            else:
                ruch = stoj('attack', minhp(wrogowie_obok))

Robot zaawansowany
*******************

Po dodaniu/zmodyfikowaniu omwionych powyej reguł kod naszego robota może
wyglądać tak:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rgkod30b.py
    :linenos:

Na koniec trzeba przetestować robota. Czy rzeczywiście jest lepszy od poprzednich wersji?

Podsumowanie
***************

Nie myśl, że zastosowanie wszystkich powyższych reguł automatycznie ulepszy
robota. Weź pod uwagę fakt, że roboty pojawiają się w losowych punktach,
oraz to, że strategia przeciwnika może być inna od zakładanej. Zaproponowane
połączenie klocków nie musi być optymalne. Przetestuj kolejne wersje robotów,
ustal ich zalety i wady, eksperymentuj, aby znaleźć lepsze rozwiązania.
