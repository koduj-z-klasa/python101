.. _klocki02a:

*RG* – klocki 2A
################

Wersja **A** oparta jest na funkcjach, czyli metodach klasy ``Robot``.

.. tip::

    * Każdy "klocek" można testować osobno, a później w połączeniu z innymi.
      Warto i trzeba zmieniać kolejność stosowanych reguł!

Typy pól
***********

Zobaczmy, w jaki sposób dowiedzieć się, w jakim miejscu się znajdujemy,
gdzie wokół mamy wrogów lub pola, na które można wejść. Dysponując takimi
informacjami, będziemy mogli podejmować bardziej przemyślane działania.
Wykorzystamy kilka pomocniczych funkcji.

Czy to wejście?
================

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # funkcja zwróci prawdę, jeżeli "poz" wskazuje punkt wejścia
    def czy_wejscie(poz):
        if 'spawn' in rg.loc_types(poz):
            return True
        return False

**Metody i właściwości biblioteki** *rg*:

* ``gr.loc_types(poz)`` – zwraca typ pola wskazywanego przez ``poz``:

    * ``invalid`` – poza granicami planszy(np. (-1, -5) lub (23, 66));
    * ``normal`` – w ramach planszy;
    * ``spawn`` – punkt wejścia robotów;
    * ``obstacle`` – pola zablokowane ograniczające arenę.

Czy obok jest wróg?
====================

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # funkcja zwróci prawdę, jeżeli "poz" wskazuje wroga
    def czy_wrog(poz):
        if game.robots.get(poz) != None:
            if game.robots[poz].player_id != self.player_id:
                return True
        return False

    # lista wrogów obok
    wrogowie_obok = []
    for poz in rg.locs_around(self.location):
        if czy_wrog(poz):
            wrogowie_obok.append(poz)

    # warunek sprawdzający, czy obok są wrogowie
    if len(wrogowie_obok):
        pass

W powyższym kodzie metoda ``.get(poz)`` pozwala pobrać dane robota, którego
kluczem w słowniku jest ``poz``.

**Metody i właściwości biblioteki** *rg*:

* ``rg.locs_around(poz, filter_out=None)`` – zwraca listę położeń sąsiadujących
  z ``poz``. Jako ``filter_out`` można podać typy położeń do wyeliminowania, np.:
  ``rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))``.

.. raw:: html

    <hr />

.. tip::

    Definicje funkcji i list należy wstawić na początku metody ``Robot.act()``
    – przed pierwszym użyciem.


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
.. literalinclude:: rgkod05a.py
    :linenos:

Metoda ``.pop()`` zastosowana do listy zwraca jej ostatni element.

Ćwiczenie 1
===============

Zapisz powyższą implementację w katalogu :file:`robot` i przetestuj
ją w symulatorze, a następnie wystaw ją do walki z robotem podstawowym.
Poeksperymentuj z kolejnością reguł, która określa ich priorytety!

Atakuj, jeśli nie umrzesz
**************************

Warto atakować, ale nie wtedy, gdy grozi nam śmierć. Można przyjąć zasadę,
że atakujemy tylko wtedy, kiedy suma potencjalnych uszkodzeń będzie mniejsza
niż zdrowie naszego robota. Zmień więc dotychczasowe reguły ataku wroga korzystając
z poniższych "klocków":

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # WERSJA A
    # jeżeli suma potencjalnych uszkodzeń jest mniejsza od naszego zdrowia
    # funkcja zwróci prawdę
    def czy_atak():
        if 9*len(wrogowie_obok) < self.hp:
            return True
        return False

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

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # WERSJA A
    # funkcja zwróci prawdę jeżeli pole poz będzie puste
    def czy_puste(poz):
        if ('normal' in rg.loc_types(poz)) and not ('obstacle' in rg.loc_types(poz)):
            if game.robots.get(poz) == None:
                return True
        return False

    puste = [] # lista pustych pól obok
    bezpieczne = [] # lista bezpiecznych pól obok

    for poz in rg.locs_around(self.location):
        if czy_puste(poz):
            puste.append(poz)
        if czy_puste(poz) and not czy_wejscie(poz):
            bezpieczne.append(poz)

Atakuj 2 kroki obok
*******************

Jeżeli w odległości 2 kroków jest przeciwnik, zamiast iść w jego kierunku
i narażać się na szkody, lepiej go zaatakuj, aby nie mógł bezkarnie się
do nas zbliżyć.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # funkcja zwróci prawdę, jeżeli w odległości 2 kroków z przodu jest wróg
    def zprzodu(l1, l2):
        if rg.wdist(l1, l2) == 2:
            if abs(l1[0] - l2[0]) == 1:
                return False
            else:
                return True
        return False

    # funkcja zwróci współrzędne pola środkowego między dwoma innymi
    # oddalonymi o 2 kroki
    def miedzypole(p1, p2):
        return (int((p1[0]+p2[0]) / 2), int((p1[1]+p2[1]) / 2))

    for poz, robot in game.get('robots').items():
        if czy_wrog(poz):
            if rg.wdist(poz, self.location) == 2:
                if zprzodu(poz, self.location):
                    return ['attack', miedzypole(poz, self.location)]
                if rg.wdist(rg.toward(loc, rg.CENTER_POINT), self.location) == 1:
                    return ['attack', rg.toward(poz, rg.CENTER_POINT)]
                else:
                    return ['attack', (self.location[0], poz[1])]

Składamy reguły
****************

Ćwiczenie 3
==============

Jeżeli czujesz się na siłach, spróbuj dokładać do robota w wersji **A**
(opartego na funkcjach) po jednej z przedstawionych reguł, czyli:
1) Atakuj, jeśli nie umrzesz; 2) Ruszaj się bezpiecznie; 3) Atakuj na 2 kroki.
Przetestuj w symulatorze każdą zmianę.

Omówione reguły można poskładać w różny sposób, np. tak:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rgkod09a.py
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

    # funkcja zwracająca atak na najsłabszego wroga obok
    def atakuj():
        r = wrogowie_obok[0]
        for poz in wrogowie_obok:
            if game.robots[poz]['hp'] > game.robots[r]['hp']:
                r = poz
        return ['attack', r]

Inne
=================

* Czy warto atakować, jeśli obok jest więcej niż 1 wróg?
* Czy warto atakować 1 wroga obok, ale mocniejszego od nas?
* Jeżeli nie można bezpiecznie się ruszyć, może lepiej się bronić?
* Jeśli jesteśmy otoczeni przez wrogów, może lepiej popełnić samobójstwo...

Proponujemy, żebyś sam zaczął wprowadzać i testować zasugerowane ulepszenia.
Możesz też zajrzeć do drugiego :ref:`drugiego <klocki02b>` i :ref:`trzeciego <klocki03b>`
zestawu klocków opartych na zbiorach.
