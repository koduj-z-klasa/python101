.. _mcpi-rg:

Gra robotów
###########

Pole gry
========

Spróbujemy teraz pokazać rozgrywkę z :ref:`gry robotów <robot-game>`.
Zaczniemy od zbudowania areny wykorzystywanej w grze. W pliku :file:`mcsimrg.py` umieszczamy następujący kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsimrg01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-
    :emphasize-lines: 51-73

Początek pliku zawiera kod omówiony w :ref:`Podstawach <mcpipodstawy>`, nowa jest funkcja ``polegry()``.
Pole gry Robot Game wpisane jest w kwadrat o boku 19 jednostek, dlatego korzystamy z dwóch zagnieżdżonych pętli,
w których zmienne iteracyjne *i*, *j* przyjmują wartości od 0 do 18. Część pól kwadratu wyłączona jest
z rozgrywki, ich współrzędne zawiera lista ``obstacle``. Bloki trawy umieszczamy tylko wtedy, kiedy
para zmiennych iteracyjnych, służąca również do wyznaczania współrzędnych, znajduje się w liście.
Odpowiada za to instrukcja warunkowa ``if (i, j) in obstacle``.

Przed uruchomieniem skryptu trzeba jeszcze umieścić wywołanie funkcji ``polegry()`` w funkcji głównej
po instrukcji rysującej pole budowy ``plac()``.

.. figure:: img/mc04.png

Dane gry
========

W pliku :file:`lastgame.log` w katalogu :file:`mcpi-sim` (lub na końcu w "Źródłach") znajduje się zapis 100 rund przykładowej rozgrywki.

.. note::

	Gdybyś chciał wykorzystać zapis swojej rozgrywki, musisz zmodyfikować bibliotekę ``game.py``
	z pakietu ``rgkit``. Jeżeli korzystałeś z naszego :ref:`scenariusza <robot-game>` i zainstalowałeś ``rgkit``
	w :ref:`wirtualnym środowisku <rg-env>` :file:`~/robot/env`, plik ten znajdziesz w ścieżce
	:file:`~/robot/env/lib/python2.7/site-packages/rgkit/game.py`. Na końcu funkcji ``run_all_turns()``
	po linii nr 386 wstaw podany niżej kod:

	.. code-block:: python

	    # BEGIN DODANE na potrzeby Kzk
	    import json
	    plik = open('lastgame.log', 'w')
	    json.dump(self.history, plik)
	    plik.close()
	    # END OF DODANE

  Teraz po wywołaniu przykładowej walki: ``(env) root@kzk:~/robot$ rgrun bots/stupid26.py bots/Wall-E.py``
  w katalogu :file:`~/robot` znajdziesz plik :file:`lastgame.log`, który trzeba umieścić w katalogu
  ze skryptem :file:`mcsimrg.py`.

Każda runda to lista zawierająca słowniki określające właściwości poszczególnych robotów.
Do pliku :file:`mcsimrg.py` przed funkcją główną dodamy funkcję ``pokaz_gre()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsimrg02.py
    :linenos:
    :lineno-start: 76
    :lines: 76-87

Po otworzeniu pliku z danymi wczytujemy jego zawartość do listy za pomocą modułu *json*: ``dane = json.load(plik)``.
Następnie w pętli odczytujemy dane kolejnych rund i – na razie, poglądowo – drukujemy je w konsoli.
Aby przetestować kod, wpisz wywołanie funkcji ``pokaz_gre(5)`` zamiast ``polegry()`` w funkcji głównej.

.. figure:: img/mc05.png

Jak można zauważyć na zrzucie, słowniki opisujące roboty walczące w danej rundzie zawierają m.in.
identyfikatory gracza oraz położenie robota. Wykorzystamy te informacje w funkcji ``pokaz_runde()``,
którą dopisujemy w pliku :file:`mcsimrg.py` przed funkcją ``pokaz_gre()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsimrg03.py
    :linenos:
    :lineno-start: 76
    :lines: 77-88

Funkcja na początku rysuje pole gry, następnie w pętli odczytujemy dane kolejnych robotów.
Na podstawie identyfikatora gracza określamy typ bloku reprezentujący robota, pobieramy jego
położenie i wreszcie umieszczamy na planszy: ``mc.setBlock(loc[0], y, loc[1], blok)``.
Aby przetestować kod, wywołanie funkcji ``pokaz_runde(r)`` umieszczamy w funkcji ``pokaz_gre()``
po instrukcji ``print(r)``, którą można zakomentować.

.. figure:: img/mc06.png

Kolory i  animacja
==================

W trakcie starć w kolejnych rundach maleje siła robotów wskazywana przez właściwość *hp*.
Spróbujemy zróżnicować kolorystycznie typ bloków wykorzystywany do wyświetlania robotów.
Przed funkcją ``pokaz_runde()`` dopisujemy funkcję ``wybierz_blok()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcsimrg04.py
    :linenos:
    :lineno-start: 76
    :lines: 76-84

Siła robotów (*hp*) przyjmuje wartości od 0 do 50, dzieląc tę wartość całkowicie przez 10,
otrzymamy liczby od 0 do 5, które posłużą nam jako indeksy wskazujące typ bloku służący
do wyświetlenia robota danego zawodnika. Dobór typów w tuplach jest oczywiście
czysto umowny.

Pozostaje jeszcze zastąpienie instrukcji warunkowej w funkcji ``pokaz_runde()`` wywołaniem
naszej funkcji: ``blok = wybierz_blok(robot['player_id'], robot['hp'])``. Przykładowy efekt
przedstawia się tak:

.. figure:: img/mc07.png

**Ćwiczenie 3**

Przekształć kod uruchamiany na symulatorze tak, aby można go było uruchomić na serwerze
Minecrafta Pi Edition.

**Źródła:**

* :download:`Skrypty mcsimrg <mcsimrg.zip>`
* :download:`Log RG <lastgame.zip>`