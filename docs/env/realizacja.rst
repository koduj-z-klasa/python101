Co musisz wiedzieć i umieć?
###########################

O Pythonie
==========

`Python <http://www.python.org>`_ jest dynamicznie typowanym językiem interpretowanym
(zob. :term:`język interpretowany`) `wysokiego poziomu <http://pl.wikipedia.org/wiki/J%C4%99zyk_wysokiego_poziomu>`_.
Cechuje się czytelnością i zwięzłością kodu. Stworzony został w latach 90.
przez `Guido van Rossuma <https://www.python.org/~guido/>`_,
nazwa zaś pochodzi od tytułu serialu komediowego emitowanego w BBC pt.
`"Latający cyrk Monty Pythona" <http://pl.wikipedia.org/wiki/Lataj%C4%85cy_cyrk_Monty_Pythona>`_.

Według zestawień serwisu `TIOBE <http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html>`_
Python jest w czołówce popularności języków programowania – 1 miejsce w sierpniu 2024 r.

Python ma zróżnicowane zastosowanie m. in. dzięki licznym dodatkowym bibliotekom,
które pozwalają tworzyć aplikacje matematyczne (`Matplotlib <http://pl.wikipedia.org/wiki/Matplotlib>`_),
okienkowe (np. `PyQt <http://pl.wikipedia.org/wiki/PyQt>`_, `PyGTK <http://pl.wikipedia.org/wiki/PyGTK>`_,
`wxPython <http://pl.wikipedia.org/wiki/WxPython>`_),
internetowe (`Flask <http://flask.pocoo.org/>`_, `Django <http://django.pl/>`_)
czy multimedialne i gry (`Pygame <http://pl.wikipedia.org/wiki/Pygame>`_).

Istnieją również kompleksowe projekty oparte na Pythonie wspomagające naukową
analizę, obliczenia i przetwarzanie danych, np.: `Anaconda <https://store.continuum.io/cshop/anaconda/>`_, `Enthought Deployment Manager <https://www.enthought.com/enthought-deployment-manager/>`_
czy `Enthought Tool Suite <https://docs.enthought.com/ets/>`_.

Tryb interaktywny
=================

Interpreter (inaczej: powłoka) Pythona może być używany w trybie interaktywnym do nauki i testowania kodu.
Uruchamiamy go, wydając w terminalu polecenie:

.. code-block:: bash

    python3  # system Linux
    py       # system Windows

.. note::

    Powłokę można również uruchomić w środowisku programistycznym, np. PyCharm lub VSCodium.

Po uruchomieniu powłoka wyświetli znak zachęty ``>>>``. Przydatne polecenia:

.. code-block:: bash

    >>> help()         # uruchomienie interaktywnej pomocy
    help> quit         # wyjście z trybu interaktywnej pomocy
    >>> help(obiekt)   # wyświetla pomoc dotyczącą dowolnego obiektu
    >>> import math    # zaimportowanie przykładowego pakietu math
    >>> dir(math)      # przegląd dostępnych w pakiecie stałych i funkcji
    >>> help(math.pow) # wyświetla pomoc nt. stałej lub funkcji dostępnej w pakiecie
    >>> exit()         # wyjście z trybu interaktywnego interpretera

Znaki ``...`` oznaczają, że wpisujemy instrukcję złożoną, np. warunkową lub pętlę, i dalszy kod wymaga wcięć.

Skrypty Pythona
=================

* Kod źródłowy Pythona zapisujemy w plikach tekstowych z rozszerzeniem ``.py``.
* Skrypty Pythona można uruchamiać w terminalu przy użyciu interpretera w katalogu, w którym zapisany jest skrypt:

  .. code-block:: bash

      python3 nazwa_skryptu.py  # system Linux
      py nazwa_skryptu.py       # system Windows

* Ze względów praktycznych warto korzystać z edytorów lub środowisk programistycznych ułatwiających pisanie i uruchamianie
  programów (m. in. kolorowanie kodu, sprawdzanie błędów itd.)
  Zobacz `Edytory kodu <https://linetc.readthedocs.io/pl/latest/tools/edytory/index.html>`_.
* Podczas przepisywania (kopiowanie) można pominąć komentarze, czyli teksty zaczynające się od znaku ``#``.
* Przepisując lub wklejając kod pamiętać trzeba o zachowywaniu wcięć, które służą w Pythonie do wyodrębniania bloków kodu.
* W niektórych materiałach znajdziesz fragmenty kodu źródłowego, które pokazują, jak rozwija się program.
* Większość fragmentów kodu jest numerowana, ale jeśli Twój kod różni się nieznacznie numeracją linii, nie musi to oznaczać błędu.

Dla przykładu poniższy kod powinien zostać wklejony w linii ``51`` skryptu:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:
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

Katalogi i pliki
==================

Terminal
---------

W scenariuszach często wykorzystujemy terminal, inaczej wiersz poleceń.

* Zarówno w Linuksie, jak i Windowsie terminal otwieramy wpisując i uruchamiając aplikację "Terminal" w Menu Start.
  W Linuskie można też użyć ikony na pasku zadań. W obydwu systemach można również w menedżerze plików kliknąć prawym
  klawiszem w otwartym katalogu i wybrać polecenie "Otwórz w terminalu".
* Przydatne polecenia:

  .. code-block:: bash

      ~$ mkdir nazwa_katalogu  # utworzenie katalogu
      ~$ cd nazwa_katalogu     # wejście do katalogu
      ~$ cd ..                 # przejście do katalogu nadrzędnego
      ~$ ls                    # wypisanie zawartości katalogu
      ~$ touch nazwa_pliku     # utworzenie pustego pliku w Linuskie
      ~$ ni nazwa_pliku        # utworzenie pustego pliku w Windowsie
      ~$ rm nazwa_pliku        # usunięcie pliku

.. note::

  Katalogi i pliki można tworzyć nie tylko w terminalu, ale również za pomocą menedżera plików,
  edytora lub środowiska programistycznego.

Linux
--------

* Katalogi dla realizowanych projektów można tworzyć w katalogu domowym lub
  w jednym nadrzędnym katalogu, np.: :file:`python101`.
* **Katalog domowy** w Linuksie jest podkatalogiem katalogu :file:`/home`
  i ma nazwę zalogowanego użytkownika, np. ``/home/uczen``. W poleceniach wydawanych
  w terminalu ścieżka do tego katalogu oznaczana jest przez znak tyldy: ``~``.
* Zapisy typu ``~/quiz$`` oznaczają, że dane polecenie należy wykonać w podkatalogu
  ``quiz`` w katalogu domowego użytkownika.
* Znak ``$`` oznacza, że komendy wydajemy jako zwykły użytkownik, natomiast ``#`` – jako
  użytkownik z uprawnieniami administratora lub administrator (root).

Windows
---------

* Katalog domowy użytkownika w Windows nie nadaje się do przechowywania w nim
  kodów programów lub repozytoriów, najlepiej utworzyć jakiś katalog na partycji
  innej niż systemowa (oznaczana literą *C:*), np. :file:`D:\\python101` i w nim
  tworzyć podfoldery dla poszczególnych scenariuszy.
* Terminal otwieramy uruchamiając z Menu Start aplikację "Terminal", tj, Windows PowerShell.
  Można również w Eksploratorze kliknąć prawym klawiszem w otwartym katalogu
  i wybrać polecenie "Otwórz w Terminalu".
* W systemie Windows znaki ``/`` (slash) w ścieżkach zmieniamy na ``\`` (backslash).
* Pamiętajmy, żeby skrypty zapisywać w plikach kodowanych jako UTF-8.

.. admonition:: Pojęcia

    :term:`interpreter`, :term:`terminal`, :term:`kod źródłowy`