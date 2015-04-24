Podstawy Pythona
#########################

`Python <http://www.python.org>`_ jest dynamicznie typowanym `językiem interpretowanym <http://pl.wikipedia.org/wiki/J%C4%99zyk_interpretowany>`_
`wysokiego poziomu <http://pl.wikipedia.org/wiki/J%C4%99zyk_wysokiego_poziomu>`_. Cechuje się czytelnością i zwięzłością kodu. Stworzony został w latach 90.
przez `Guido van Rossuma <https://www.python.org/~guido/>`_, nazwa zaś pochodzi od tytułu serialu komediowego
emitowanego w BBC pt. `"Latający cyrk Monty Pythona" <http://pl.wikipedia.org/wiki/Lataj%C4%85cy_cyrk_Monty_Pythona>`_.

W systemach opartych na Linuksie :term:`interpreter` Pythona jest standardowo zainstalowany,
ponieważ duża część oprogramowania na nim bazuje. W systemach Microsoft Windows interpreter Pythona
należy :ref:`doinstalować <ins-python>`. Interpreter tłumaczy (kompiluje w locie) kod i od razu go wykonuje.
Interpreter Pythona może być używany w trybie interaktywnym do nauki i testowania
kodu.

Funkcjonalność Pythona może być dowolnie rozszerzana dzięki licznym
bibliotekom pozwalającym tworzyć aplikacje okienkowe (`PyQt <http://pl.wikipedia.org/wiki/PyQt>`_, `PyGTK <http://pl.wikipedia.org/wiki/PyGTK>`_, `wxPython <http://pl.wikipedia.org/wiki/WxPython>`_),
internetowe (`Flask <http://flask.pocoo.org/>`_, `Django <http://django.pl/>`_) czy multimedialne i gry (`Pygame <http://pl.wikipedia.org/wiki/Pygame>`_). Istnieją również
kompleksowe projekty oparte na Pythonie wspomagające naukową analizę, obliczenia
i przetwarzanie danych, np.: `Anaconda <https://store.continuum.io/cshop/anaconda/>`_ czy `Enthought Canopy <https://www.enthought.com/products/canopy/>`_.

Interpreter Pythona
===================

Siła Pythona tkwi m. in. w standardowej bibliotece udostępniającej wiele
funkcjonalności, a także w wielu rozszerzeniach zapewnianych przez instalację
dodatkowych modułów. W Pythonie łatwo stworzymy aplikacje konsolowe, wyposażone
w interfejs graficzny, sieciowe, bazodanowe, multimedialne itd.

W systemach opartych na Linuksie :term:`interpreter` Pythona jest standardowo zainstalowany,
ponieważ duża część oprogramowania na nim bazuje. W systemach Microsoft Windows Pythona
należy :ref:`doinstalować <ins-python>`. Interpreter tłumaczy (kompiluje w locie) kod i od razu go wykonuje.
Interpreter Pythona może być używany w trybie interaktywnym do nauki i testowania
kodu.

Prosty kod można testować w interpreterze, do tworzenia bardziej rozbudowanych
skryptów wykorzystać możemy dowolny edytor tekstowy. Ze względów praktycznych
warto korzystać z programów ułatwiających pisanie kodu (obsługa wcięć,
podświetlenia itd.) tzw. IDE czyli `Integrated Development Environment <http://pl.wikipedia.org/wiki/Zintegrowane_%C5%9Brodowisko_programistyczne>`_
np. lekkie i szybkie :ref:`Geany <geany-python>` lub profesjonalne środowisko
:ref:`PyCharm <pycharm-python>`. Obydwa programy działają na platformie Linux i Windows.

Zanim przystąpimy do pracy w katalogu domowym utworzymy podkatalog ``python``,
w którym będziemy zapisywali nasze skrypty:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: bash

    ~$ mkdir python
    ~$ cd python

Interpreter Pythona uruchamiamy poleceniem:

.. code:: bash

    ~$ python

Po uruchomieniu interpreter wyświetli swoją wersję, wersję kompilatora C++ (``GCC``),
informację o sposobie uzyskania pomocy (polecenie ``help``), na końcu zaś
znak zachęty ``>>>``.

.. note::

    Można równierz korzystać z rozszerzonej konsoli Pythona uruchamianej poleceniem
    ``ipython``. Oferuje ona kolorowane wyjście, ułatwia wszelkiego rodzaju interaktywne obliczenia.

    Przykłady zawierające znak zachęty ``$`` oznaczają komendy
    do wykonania w terminalu systemu operacyjnego (w Xubuntu uruchom przez :kbd:`Win+T`).

    Komendy kopiujemy i wklejamy do terminala bez znaku zachęty ``$`` i poprzedzającego tekstu
    za pomocą środkowego klawisza myszki lub skrótu :kbd:`CTRL+SHIFT+V`.

.. toctree::
    :maxdepth: 2

    podstawy/index.rst
    przyklady/index.rst
    przyklady/index1.rst
    przyklady/index2.rst
    przyklady/index3.rst
    przyklady/index4.rst
    przyklady/index5.rst

Materiały
***************

#. `Python`_

.. Python_: https://www.python.org/

Słownik
====================

.. glossary::

    język interpretowany
        język, który jest tłumaczony i wykonywany "w locie". Tłumaczeniem i
        wykonywaniem programu zajmuje się specjalny program nazwany interpreterem języka.

    interpreter
        program, który analizuje kod źródłowy, a następnie go wykonuje. Interpretery są
        podstawowym składnikiem języków wykorzystywanych do pisania skryptów wykonywanych
        po stronie klienta WWW (JavaScript) lub serwera (np. Python, PHP).

Źródła
====================

Wersje "Podstaw Pythona" w formacie *odt* lub *pdf*:

- :download:`T1.odt <T1.odt>`
- :download:`T1.pdf <T1.pdf>`

Kody "Python w przykładach":

- :download:`basic.zip <basic.zip>`
