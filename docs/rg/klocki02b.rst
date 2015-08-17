.. _klocki02b:

*RG* – klocki 2B
################

Wersja **B** oparta jest na zbiorach i operacjach na nich.

.. tip::

    * Każdy "klocek" można testować osobno, a później w połączeniu z innymi.
      Warto i trzeba zmieniać kolejność stosowanych reguł!

Typy pól
***********

Zobaczmy, w jaki sposób dowiedzieć się, w jakim miejscu się znajdujemy,
gdzie wokół mamy wrogów lub pola, na które można wejść. Dysponując takimi
informacjami, będziemy mogli podejmować bardziej przemyślane działania.
Wykorzystamy wyrażenia zbiorów (ang. *set comprehensions*) (zob. :term:`wyrażenie listowe`)
i operacje na zbiorach (zob. :term:`zbiór`).

Czy to wejście?
================

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # wszystkie pola na planszy jako współrzędne (x, y)
    wszystkie = {(x, y) for x in xrange(19) for y in xrange(19)}

    # punkty wejścia (spawn)
    wejscia = {poz for poz in wszystkie if 'spawn' in rg.loc_types(poz)}

    # warunek sprawdzający, czy "poz" jest w punkcie wejścia
    if poz in wejscia:
        pass

**Metody i właściwości biblioteki** *rg*:

* ``gr.loc_types(poz)`` – zwraca typ pola wskazywanego przez ``poz``:

    * ``invalid`` – poza granicami planszy(np. (-1, -5) lub (23, 66));
    * ``normal`` – w ramach planszy;
    * ``spawn`` – punkt wejścia robotów;
    * ``obstacle`` – pola zablokowane ograniczające arenę.

Czy obok jest wróg?
====================

Wersja oparta na zbiorach wykorzystuje różnicę i cześć wspólną zbiorów.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # pola zablokowane
    zablokowane = {poz for poz in wszystkie if 'obstacle' in rg.loc_types(poz)}

    # pola zajęte przez nasze roboty
    przyjaciele = {poz for poz in game.robots if game.robots[poz].player_id == self.player_id}

    # pola zajęte przez wrogów
    wrogowie = set(game.robots) - przyjaciele

    # pola sąsiednie
    sasiednie = set(rg.locs_around(self.location)) - zablokowane

    # pola obok zajęte przez wrogów
    wrogowie_obok = sasiednie & wrogowie

    # warunek sprawdzający, czy obok są wrogowie
    if wrogowie_obok:
        pass

**Metody i właściwości biblioteki** *rg*:

* ``rg.locs_around(poz, filter_out=None)`` – zwraca listę położeń sąsiadujących
  z ``poz``. Jako ``filter_out`` można podać typy położeń do wyeliminowania, np.:
  ``rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))``.

.. raw:: html

    <hr />

.. tip::

    Definicje zbiorów należy wstawić na początku
    metody ``Robot.act()`` – przed pierwszym użyciem.

Wykorzystując powyższe "klocki" możemy napisać robota realizującego następujące reguły:

#. Opuść jak najszybciej wejście;
#. Atakuj wrogów obok;
#. W środku broń się;
#. W ostateczności idź do środka.

Implementacja
==============

Przykładowa implementacja może wyglądać następująco:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rgkod05b.py
    :linenos:

Metoda ``.pop()`` zastosowana do zbioru zwraca element losowy.

Ćwiczenie 1
===============

Zapisz powyższą implementację w katalogu :file:`robot` i przetestuj
ją w symulatorze, a następnie wystaw ją do walki z robotem podstawowym.
Poeksperymentuj z kolejnością reguł, która określa ich priorytety!

.. tip::

    Do kontrolowania logiki działania robota zamiast rozłącznych instrukcji
    warunkowych: ``if war1: ... if war2: ...`` itd. można użyć instrukcji
    złożonej: ``if war1: ... elif war2: ... [elif war3: ...] else: ...``.

Atakuj, jeśli nie umrzesz
**************************

Warto atakować, ale nie wtedy, gdy grozi nam śmierć. Można przyjąć zasadę,
że atakujemy tylko wtedy, kiedy suma potencjalnych uszkodzeń będzie mniejsza
niż zdrowie naszego robota. Zmień więc dotychczasowe reguły ataku wroga korzystając
z poniższych "klocków":

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # WERSJA B
    # jeżeli obok są przeciwnicy, atakuj
    if wrogowie_obok:
        if 9*len(wrogowie_obok) >= self.hp:
            pass
        else:
            ruch = ['attack', wrogowie_obok.pop()]

**Metody i właściwości biblioteki** *rg*:

* ``self.hp`` – ilość punktów HP robota.

Ćwiczenie 2
===============

Dodaj powyższą regułę do poprzedniej wersji robota.

Ruszaj się bezpiecznie
***********************

Zamiast iść na oślep lepiej wchodzić czy uciekać na bezpieczne pola.
Za "bezpieczne" przyjmiemy na razie pole puste, niezablokowane i nie będące
punktem wejścia.

.. raw:: html

    <div class="code_no"><strong>Wersja <em>B</em>.</strong> Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # WERSJA B
    # zbiór bezpiecznych pól
    bezpieczne = sasiednie - wrogowie_obok - wejscia - przyjaciele


Atakuj 2 kroki obok
*******************

Jeżeli w odległości 2 kroków jest przeciwnik, zamiast iść w jego kierunku
i narażać się na szkody, lepiej go zaatakuj, aby nie mógł bezkarnie się
do nas zbliżyć.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # WERSJA B
    wrogowie_obok2 = {poz for poz in sasiednie if (set(rg.locs_around(poz)) & wrogowie)} - przyjaciele

    if wrogowie_obok2:
        ruch = ['attack', wrogowie_obok2.pop()]

Składamy reguły
****************

Ćwiczenie 3
==============

Jeżeli czujesz się na siłach, spróbuj dokładać do robota w wersji **B**
(opartego na zbiorach) po jednej z przedstawionych reguł, czyli:
1) Atakuj, jeśli nie umrzesz; 2) Ruszaj się bezpiecznie; 3) Atakuj na 2 kroki.
Przetestuj w symulatorze każdą zmianę.

Omówione reguły można poskładać w różny sposób, np. tak:

W wersji **B** opartej na zbiorach:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rgkod09b.py
    :linenos:

Możliwe ulepszenia
**********************

Poniżej pokazujemy "klocki", których możesz użyć, aby zoptymalizować robota.
Zamieszczamy również listę pytań do przemyślenia, aby zachęcić cię do
samodzielnego konstruowania najlepszego robota :-)

Atakuj najsłabszego
====================

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # wersja B
    # funkcja znajdująca najsłabszego wroga obok z podanego zbioru (bots)
    def minhp(bots):
        return min(bots, key=lambda x: game.robots[x].hp)

    if wrogowie_obok:
        ...
        else:
            ruch = ['attack', minhp(wrogowie_obok)]

Najkrócej do celu
==================

Funkcji ``mindist()`` można użyć do znalezienia najbliższego wroga,
aby iść w jego kierunku, kiedy opuścimy punkt wejścia:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # WERSJA B
    # funkcja zwraca ze zbioru pól (bots) pole najbliższe podanego celu (poz)
    def mindist(bots, poz):
        return min(bots, key=lambda x: rg.dist(x, poz))

    najblizszy_wrog = mindist(wrogowie,self.location)

Inne
=================

* Czy warto atakować, jeśli obok jest więcej niż 1 wróg?
* Czy warto atakować 1 wroga obok, ale mocniejszego od nas?
* Jeżeli nie można bezpiecznie się ruszyć, może lepiej się bronić?
* Jeśli jesteśmy otoczeni przez wrogów, może lepiej popełnić samobójstwo...
* Spróbuj zmienić akcję domyślną.
* Spróbuj użyć jednej złożonej instrukcji warunkowej!

Proponujemy, żebyś sam zaczął wprowadzać i testować zasugerowane ulepszenia.
Możesz też zajrzeć do :ref:`trzeciego <klocki03b>` zestawu klocków.

