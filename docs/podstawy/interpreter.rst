Interpreter Pythona
####################

Każdy kod można testować w interpreterze Pythona, jednak do tworzenia skryptów wykorzystujemy
dowolny edytor tekstowy. Ze względów praktycznych warto korzystać z programów
ułatwiających pisanie kodu (obsługa wcięć, podświetlenia itd.) tzw. IDE,
czyli `Integrated Development Environment <http://pl.wikipedia.org/wiki/Zintegrowane_%C5%9Brodowisko_programistyczne>`_
np. lekkie i szybkie :ref:`Geany <geany-python>` lub profesjonalne środowisko
:ref:`PyCharm <pycharm-python>`. Obydwa programy działają na platformie Linux i Windows.

Zanim przystąpimy do pracy w katalogu domowym tworzymy podkatalog ``python``,
w którym będziemy zapisywali nasze skrypty:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: bash

    ~$ mkdir python
    ~$ cd python

Tryb interaktywny intrpretera Pythona jest podstawowym narzędziem nauki
i testowania kodu. Uruchamiamy go, wydając w terminalu używanego systemu
polecenie:

.. code:: bash

    ~$ python

Po uruchomieniu interpreter wyświetli swoją wersję, wersję kompilatora C++ (``GCC``),
informację o sposobie uzyskania pomocy (polecenie ``help``), na końcu zaś
znak zachęty ``>>>``. Jeżeli będziemy testować instrukcje złożone, np.
warunkowe lub pętle, w interpreterze zobaczymy znaki ``...`` oznaczające,
że wprowadzany kod wymaga wcięć.

.. note::

    Można równierz korzystać z rozszerzonej konsoli Pythona uruchamianej poleceniem
    ``ipython``. Oferuje ona kolorowane wyjście, ułatwia wszelkiego rodzaju interaktywne obliczenia.

    Przykłady zawierające znak zachęty ``$`` oznaczają komendy
    do wykonania w terminalu systemu operacyjnego (w Xubuntu uruchom przez :kbd:`Win+T`).

    Komendy kopiujemy i wklejamy do terminala bez znaku zachęty ``$``
    i poprzedzającego tekstu za pomocą środkowego klawisza myszki
    lub skrótu :kbd:`CTRL+SHIFT+V`.
