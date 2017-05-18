Interpreter Pythona
####################

Każdy kod można testować w interpreterze Pythona, jednak do tworzenia skryptów
ze względów praktycznych warto korzystać z programów ułatwiających pisanie kodu
(obsługa wcięć, podświetlenia itd.), tzw. IDE,
czyli `Integrated Development Environment <http://pl.wikipedia.org/wiki/Zintegrowane_%C5%9Brodowisko_programistyczne>`_, np. :ref:`Geany <geany-python>`, :ref:`Sublime-Text <_st3-python>` lub :ref:`PyCharm <pycharm-python>`.
Wymienione programy działają na platformie Linux i Windows.

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

    ~$ python3

Po uruchomieniu interpreter wyświetli swoją wersję, wersję kompilatora C++ (``GCC``),
informację o sposobie uzyskania pomocy (polecenie ``help``), na końcu zaś
znak zachęty ``>>>``. Jeżeli będziemy testować instrukcje złożone, np.
warunkowe lub pętle, w interpreterze zobaczymy znaki ``...`` oznaczające,
że wprowadzany kod wymaga wcięć.

.. note::

    Warto zainstalować i korzystać z rozszerzonych wersji konsoli Pythona uruchamianych najczęściej
    poleceniami ``ipython3`` lub ``ipython3 qtconsole``. Oferują ona kolorowane wyjście,
    rozbudowane podpowiedzi i ułatwienia interaktywnych obliczeń.

    Przykłady zawierające znak zachęty ``$`` oznaczają komendy do wykonania w terminalu systemu operacyjnego.

    Komendy kopiujemy i wklejamy do terminala bez znaku zachęty ``$``
    i poprzedzającego tekstu za pomocą środkowego klawisza myszki
    lub skrótów :kbd:`CTRL+SHIFT+V`, :kbd:`CTRL+SHIFT+Insert`.
