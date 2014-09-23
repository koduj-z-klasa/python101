Gra w Ponga
===========

.. highlight:: python

Klasyczna gry w odbijanie piłeczki zrealizowana z użyciem biblioteki `PyGame`_.

.. _PyGame: http://www.pygame.org/wiki/tutorials

.. figure:: pong_0.png

Przygotowanie
-------------

Do rozpoczęcia pracy z przykładem pobieramy szczątkowy kod źródłowy:

.. code-block:: bash

    ~/python101$ git checkout -f --track origin/pong/z1

.. note::

    Przykłady zawierające znak zachęty ``$`` oznaczają komendy
    do wykonania w terminalu systemu operacyjnego (uruchom przez :kbd:`Win+T`).

    Oprócz znaku zachęty ``$`` przykłady mogą zawierać informację o
    lokalizacji w jakiej należy wykonać komendę. Np. ``~/python101$`` oznacza
    że komendę wykonujemy w folderze ``python101`` w katalogu domowym
    użytkownika, czyli ``/home/sru/python101`` w środowisku SRU.
    Jeśli nie mamy tego katalogu należy :doc:`przygotować katalog projektu <../git>`.

    Komendy należy kopiować i wklejać bez znaku zachęty ``$`` i poprzedzającego tekstu.
    Komendy można wklejać do terminala środkowym klawiszem myszki.

Okienko gry
-----------

Na wstępie w pliku ``~/python101/pong/pong.py`` otrzymujemy kod który przygotuje okienko naszej gry:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_z1.py
    :linenos:


W powyższym kodzie zdefiniowaliśmy klasę ``Board`` z dwiema metodami:

#. konstruktorem ``__init__``, oraz
#. metodą ``draw`` posługującą się biblioteką ``PyGame`` do rysowania w oknie.

Na końcu utworzyliśmy instancję klasy ``Board`` i wywołaliśmy jej metodę ``draw`` na razie
bez żadnych elementów wymagających narysowania.

.. note::

    Każdy plik skryptu *Python* jest uruchamiany w momencie importu — plik/moduł główny
    jest importowany jako pierwszy.

    Deklaracje klas są faktycznie instrukcjami sterującymi mówiącymi by w aktualnym module
    utworzyć typy zawierające wskazane definicje.

    Możemy mieszać deklaracje klas ze zwykłymi instrukcjami sterującymi takimi jak ``print``,
    czy przypisaniem wartości zmiennej ``board = Board(800, 400)`` i następnie wywołaniem
    metody na obiekcie ``board.draw()``.


Nasz program możemy uruchomić komendą:

.. code-block:: bash

    ~/python101$ python pong/pong.py

Mrugnęło? Program się wykonał i zakończył działanie :). Żeby zobaczyć efekt na dłużej,
możemy na końcu chwilkę uśpić nasz program:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>


.. code-block:: python
    :linenos:
    :lineno-start: 39

    import time
    time.sleep(5)


Jednak zamiast tego, dla lepszej kontroli powinniśmy zadeklarować klasę kontrolera gry:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>


.. literalinclude:: pong_z2.py
    :linenos:
    :lineno-start: 37
    :lines: 37-

.. note::

    Prócz dodania kontrolera zmieniliśmy także sposób w jaki gra jest uruchamiana
    — nie mylić z uruchomieniem programu.

    Na końcu dodaliśmy instrukcję warunkową
    ``if __name__ == "__main__":``, w niej sprawdzamy czy nasz moduł jest modułem
    głównym programu, jeśli nim jest gra zostanie uruchomiona.

    Dzięki temu jeśli nasz moduł został zaimportowany gdzieś indziej instrukcją
    ``import pong``, deklaracje klas zostały by wykonane, ale sama gra nie będzie
    uruchomiona.

Gotowy kod możemy wyciągnąć komendą:

.. code-block:: bash

    ~/python101$ git checkout -f --track origin/pong/z2

Piłeczka
--------

Czas dodać piłkę do gry. *Piłeczką* będzie kolorowe kółko które z każdym przejściem
naszej pętli przesuniemy o kilka punktów w osi X i Y, zgodnie wektorem prędkości.

Wcześniej jednak zdefiniujemy wspólną klasę bazową dla obiektów które będziemy
rysować w oknie naszej gry:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>


.. literalinclude:: pong_z3.py
    :linenos:
    :lineno-start: 67
    :lines: 72-85

Następnie dodajmy klasę samej piłeczki dziedzicząc z ``Drawable``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>


.. literalinclude:: pong_z3.py
    :linenos:
    :lineno-start: 83
    :lines: 88-124

Teraz musimy naszą piłeczkę zintegrować z resztą gry:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>


.. literalinclude:: pong_z3.py
    :linenos:
    :lines: 38-60
    :emphasize-lines: 12, 19-22
    :lineno-start: 38

.. note::

    Metoda ``Board.draw`` oczekuje wielu opcjonalnych argumentów, na razie przekazujemy
    tylko jeden, by zwiększyć czytelność potencjalnie dużej listy argumentów — kto
    wie co jeszcze dodamy :) — podajemy każdy w swojej linii zakończonej przecinkiem ``,``

    Python nie traktuje takich osieroconych przecinków jako błąd, jest to ukłon w stronę
    programistów którzy często zmieniają kod, kopiują i wklejają kawałki.

    Dzięki temu możemy wstawiać nowe, i zmieniać kolejność bez zwracania uwagi czy na końcu
    jest przecinek, czy go brakuje, czy go należy usunąć. Zgodnie z konwencją powinien być
    tam zawsze.

Gotowy kod możemy wyciągnąć komendą:

.. code-block:: bash

    ~/python101$ git checkout -f --track origin/pong/z3


Odbijanie piłeczki
------------------

Uruchommy naszą "grę" ;)

.. code-block:: bash

    ~/python101$ python pong/pong.py

.. figure:: pong_3.png

Efekt nie jest powalający, ale mamy już jakiś ruch na planszy. Szkoda, że piłka spada z planszy.
Może mogła by się odbijać od krawędzi okienka?
Możemy wykorzystać wcześniej przygotowane metody do zmiany kierunku wektora
prędkości, musimy tylko wykryć moment w którym piłeczka będzie dotykać krawędzi.

W tym celu piłeczka musi być świadoma istnienia planszy i pozycji krawędzi, dlatego
zmodyfikujemy metodę ``Ball.move`` tak by przyjmowała ``board`` jako argument i na
jego podstawie sprawdzimy czy piłeczka powinna się odbijać:

.. code-block:: python
    :emphasize-lines: 1, 8-12
    :lineno-start: 119

    def move(self, board):
        """
        Przesuwa piłeczkę o wektor prędkości
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x < 0 or self.rect.x > board.surface.get_width():
            self.bounce_x()

        if self.rect.y < 0 or self.rect.y > board.surface.get_height():
            self.bounce_y()

Jeszcze zmodyfikujmy wywołanie metody ``move`` w naszej pętli głównej:

.. code-block:: python
    :emphasize-lines: 6
    :lineno-start: 51

    def run(self):
        """
        Główna pętla programu
        """
        while not self.handle_events():
            self.ball.move(self.board)
            self.board.draw(
                self.ball,
            )
            self.fps_clock.tick(30)

.. warning::

    Powyższe przykłady mają o jedno wcięcie za mało. Poprawnie wcięte przykłady
    straciłyby kolorowanie, dlatego należy lekko poprawić kod po ewentualnym wklejeniu.


Sprawdzamy piłka się odbija, uruchamiamy nasz program:

.. code-block:: bash

    ~/python101$ python pong/pong.py

Gotowy kod możemy wyciągnąć komendą:

.. code-block:: bash

    ~/python101$ git checkout -f --track origin/pong/z4


Odbijamy piłeczkę rakietką
--------------------------

Dodajmy "rakietkę" od przy pomocy której będziemy mogli odbijać piłeczkę.
Dodajmy zwykły prostokąt, który będziemy przesuwać przy pomocy myszki.

.. literalinclude:: pong_z5.py
    :linenos:
    :lines: 144-161
    :lineno-start: 133

Następnie "pokażemy" rakietkę piłeczce, tak by mogła się od niej odbijać.
Wiemy że rakietek będzie więcej dlatego od razu tak zmodyfikujemy metodę
``Ball.move`` by przyjmowała kolekcję rakietek:

.. code-block:: python
    :linenos:
    :emphasize-lines: 1, 14-16
    :lineno-start: 119

    def move(self, board, *args):
        """
        Przesuwa piłeczkę o wektor prędkości
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x < 0 or self.rect.x > board.surface.get_width():
            self.bounce_x()

        if self.rect.y < 0 or self.rect.y > board.surface.get_height():
            self.bounce_y()

        for racket in args:
            if self.rect.colliderect(racket.rect):
                self.bounce_y()


Tak jak w przypadku dodawania piłeczki, rakietkę też trzeba dodać do "gry",
dodatkowo musimy ją pokazać piłeczce:

.. literalinclude:: pong_z5.py
    :linenos:
    :lines: 38-76
    :emphasize-lines: 13, 23, 36-39
    :lineno-start: 38

Gotowy kod możemy wyciągnąć komendą:

.. code-block:: bash

    ~/python101$ git checkout -f --track origin/pong/z4

.. note::

    W tym miejscu można się pobawić naszą grą, zmodyfikuj ją według uznania
    i pochwal się rezultatem z innymi

    Jeśli kod przestanie działać, można szybko porzucić zmiany poniższą komendą.

    .. code-block:: bash

        ~/python101$ git reset --hard


Gramy przeciwko komputerowi
---------------------------

Dodajemy przeciwnika, nasz przeciwnik będzie mistrzem, będzie dokładnie
śledził piłeczkę i zawsze starał się utrzymać rakietkę gotową do odbicia piłeczki.

.. literalinclude:: pong_z6.py
    :linenos:
    :lines: 167-177
    :lineno-start: 164

Tak jak w przypadku piłeczki i rakietki dodajemy nasze ``Ai`` do gry,
a wraz nią wraz dodajemy drugą rakietkę.
Dwie rakietki ustawiamy na przeciwległych brzegach planszy.

Trzeba pamiętać by pokazać drugą rakietkę piłeczce, tak by mogła się
od niej odbijać.

.. literalinclude:: pong_z6.py
    :linenos:
    :lines: 38-66
    :emphasize-lines: 13-15, 22, 26, 28
    :lineno-start: 38


Pokazujemy punkty
-----------------

Dodajmy klasę sędziego, który patrząc na poszczególne elementy gry będzie
decydował czy graczom należą się punkty i będzie ustawiał piłkę w początkowym położeniu.

.. literalinclude:: pong_z7.py
    :linenos:
    :lines: 183-228
    :lineno-start: 183

Tradycyjnie dodajemy instancję nowej klasy do gry:

.. literalinclude:: pong_z7.py
    :linenos:
    :lines: 38-66
    :emphasize-lines: 16, 28
    :lineno-start: 38

Zadania dodatkowe i rzeczy które można poprawić
-----------------------------------------------

#. Piłeczka "odbija się" po zewnętrznej prawej i dolnej krawędzi. Można to poprawić.
#. Metoda ``Ball.move`` otrzymuje w argumentach planszę i rakietki. Te elementy można
   piłeczce przekazać tylko raz w konstruktorze.
#. Komputer nie odbija piłeczkę rogiem rakietki.
#. Rakietka gracza rusza się tylko gdy gracz rusza myszką, ruch w stronę myszki powinen
   być kontynuowany także gdy myszka jest bezczynna.
#. Gdy piłeczka odbija się od boków rakietki powinna odbijać się w osi X.
#. Gra dwuosobowa z użyciem komunikacji po sieci.


Metryka
^^^^^^^

:Autorzy: Janusz Skonieczny <js@bravelabs.pl>

Dokument wygenerowany |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>
