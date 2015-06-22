.. _klocki01:

*RG* – klocki 1
################

.. tip::

    * Każdy "klocek" można testować osobno, a później w połączeniu z innymi.
      Warto i trzeba zmieniać kolejność stosowanych reguł!

Idź do środka
**************

To będzie nasza domyślna reguła. Umieszczamy ją w pliku :file:`robot01.py`
zawierającym niezbędne minimum działającego bota:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rgkod01.py
   :linenos:

**Metody i właściwości biblioteki** *rg*:

* ``rg.toward(poz_wyj, poz_cel)`` – zwraca następne położenie na drodze z bieżącego miejsca do podanego.
* ``self.location`` – pozycja robota, który podejmuje działanie (``self``).
* ``rg.CENTER_POINT`` – środek areny.

W środku broń się lub giń
**************************

Co powinien robić robot, kiedy dojdzie do środka? Może się bronić lub
popełnić samobójstwo:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rgkod02.py
    :linenos:

Atakuj wrogów obok
*******************

Wersja wykorzystująca pętlę.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rgkod03.py
    :linenos:

**Metody i właściwości biblioteki** *rg*:

* Słownik ``game.robots`` zawiera dane wszystkich robotów na planszy.
  Metoda  ``.iteritems()`` zwraca indeks ``poz``, czyli położenie *(x,y)*
  robota, oraz słownik ``robot`` opisujący jego właściwości, czyli:

    * *player_id* – identyfikator gracza, do którego należy robot;
    * *hp* – ilość punktów HP robota;
    * *location* – tupla (x, y) oznaczająca położenie robota na planszy;
    * *robot_id* – identyfikator robota w Twojej drużynie.

* ``rg.dist(poz1, poz1)`` – zwraca matematyczną odległość między dwoma położeniami.

Robot podstawowy
*****************

Łącząc omówione wyżej trzy podstawowe reguły, otrzymujemy robota podstawowego:

.. raw:: html

    <div class="code_no">Plik <em>robot04a.py</em>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rgkod04a.py
    :linenos:

Wybrane działanie robota zwracamy za pomocą instrukcji ``return``.
Zwróć uwagę, jak ważna jest w tej wersji kodu **kolejność umieszczenia reguł**,
pierwszy spełniony warunek powoduje wyjście z funkcji, więc pozostałe
możliwości nie są już sprawdzane!

.. raw:: html

    <hr />

Powyższy kod można przekształcić wykorzystując zmienną pomocniczą ``ruch``,
inicjowaną działaniem domyślnym, które może zostać zmienione przez kolejne reguły.
Dopiero na końcu zwracamy ustaloną akcję:

.. raw:: html

    <div class="code_no">Plik <em>robot04b.py</em>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rgkod04b.py
    :linenos:
    :emphasize-lines: 10, 13, 18, 20
    :lineno-start: 1
    :lines: 1-

Ćwiczenie 1
=============

Przetestuj działanie robota podstawowego wystawiając go do gry z samym sobą
w symulatorze. Zaobserwuj zachowanie się robotów tworząc różne układy początkowe:

.. code-block:: bash

    (env)~/robot$ python ./symuluj robot04a.py robot04b.py

Możliwe ulepszenia
*******************

Robota podstawowego można rozbudowywać na różne sposoby przy użyciu różnych
technik kodowania. Proponujemy więc :ref:`wersję **A** <klocki02a>` opartą na funkcjach
i listach oraz :ref:`wersję **B** <klocki02b>` opartą na zbiorach. Obie wersje implementują
te same reguły, jednak efekt końcowy nie wcale nie musi być identyczny.
Przetestuj i przekonaj się sam.

.. raw:: html

    <hr />
