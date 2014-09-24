Gra w życie Conwaya
===================

`Gra w życie`_ zrealizowana z użyciem biblioteki `PyGame`_.

.. _PyGame: http://www.pygame.org/wiki/tutorials
.. _Gra w życie: http://pl.wikipedia.org/wiki/Gra_w_życie

.. figure:: screen1.png

Przygotowanie
-------------

Do rozpoczęcia pracy z przykładem pobieramy szczątkowy kod źródłowy:

.. code-block:: bash

    ~/python101$ git checkout -f tags/life/z1

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

Na wstępie w pliku ``~/python101/life/life.py`` otrzymujemy kod który przygotuje okienko naszej gry:

.. tip::

    Podczas przepisywania kodu, można pominąć kawałki dokumentujące kod, to jest teksty zaczynające się od
    znaku ``#`` oraz teksty zamknięte pomiędzy potrójnymi cudzysłowami ``"""``.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: code1.py
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

    ~/python101$ python life/life.py

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>


.. code-block:: python
    :linenos:
    :lineno-start: 45

    import time
    time.sleep(5)


Jednak zamiast tego, dla lepszej kontroli powinniśmy zadeklarować klasę kontrolera gry,
usuńmy kod o linii 37 do końca i dodajmy klasę kontrolera:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: code1.py
    :linenos:
    :lineno-start: 45
    :lines: 45-

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

    ~/python101$ git checkout -f tags/pong/z2

Piłeczka
--------


Zadania dodatkowe i rzeczy które można poprawić
-----------------------------------------------

#. TODO

Słowniczek
----------

.. glossary::

    dziedziczenie
        w programowaniu obiektowym nazywamy mechanizm współdzielenia funkcjonalności
        między klasami. Klasa może dziedziczyć po innej klasie, co oznacza,
        że oprócz swoich własnych atrybutów oraz zachowań, uzyskuje także te pochodzące
        z klasy, z której dziedziczy.

    przesłanianie
        w programowaniu obiektowym możemy w klasie dziedziczącej przesłonić metody
        z klasy nadrzędnej rozszerzając lub całkowicie zmieniając jej działanie

Metryka
^^^^^^^

:Autorzy: Janusz Skonieczny <js@bravelabs.pl>,
          Robert Bednarz

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>
