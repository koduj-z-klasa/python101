Interpreter Pythona
####################

**Uruchamianie programów**

Programy Pythona zapisane w plikach z rozszerzeniem ``.py`` uruchamiamy w terminalu
przy użyciu interpretera:

.. code-block:: bash

    ~$ python3 nazwa_skryptu.py

**Testowanie kodu**

Interpreter Pythona jest interaktywnym środowiskiem, w którym możemy testować dowolny
kod. Wersję podstawową uruchomimy poleceniem:

.. code-block:: bash

    ~$ python3

Warto jednak korzystać z rozszerzonych powłok, oferujących dodatkowe podpowiedzi,
dopełanianie i formatowanie kodu itp. ułatwienia. Polecamy program ``ipython``.
Jego wersję terminalową uruchomimy poleceniem:

.. code-block:: bash

    ~$ ipython3

– a wersję graficzną:

.. code-block:: bash

    ~$ ipython3
 ``qtconsole``.



ze względów praktycznych warto korzystać z programów ułatwiających pisanie kodu
(obsługa wcięć, podświetlenia itd.), tzw. IDE,
czyli `Integrated Development Environment <http://pl.wikipedia.org/wiki/Zintegrowane_%C5%9Brodowisko_programistyczne>`_, np. :ref:`Geany <geany-python>`, :ref:`Sublime-Text <st3-python>` lub :ref:`PyCharm <pycharm-python>`.
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

Narzędzia i biblioteki
======================

**Omówienie narzędzi:**

* `pip <https://pip.pypa.io/en/stable/>`_  – instalator pakietów Pythona,
  podstawowe narzędzie służące do zarządzania pakietami Pythona zgromadzonymi np.
  w repozytorium `PyPI <https://pypi.python.org/pypi>`_  (Python Package Index);
* `virtualenv <https://virtualenv.readthedocs.org/en/latest/>`_  –
  menedżer wirtualnych środowisk Pythona, pozwala tworzyć katalogi zawierające
  izolowane środowisko Pythona umożliwiające instalowanie wybranych wersji pakietów
  przez zwykłych użytkowników;
* `klient git <https://git-scm.com/downloads>`_  – narzędzie wersjonowania kodu
  umożliwiające korzystanie z repozytoriów i dokumentacji w serwisie `Github <https://github.com/>`_
* `sqlite3 <https://www.sqlite.org/>`_ – konsolowa powłoka dla baz SQLite3,
  umożliwia przeglądanie schematów tabel oraz zarządzanie bazą za pomocą języka SQL.
* `ipython <http://ipython.org/>`_ i `qtconsole <http://jupyter.org/qtconsole/stable/>`_ – rozszerzona interaktywna konsola Pythona;
*   – rozszerzona interaktywna konsola
  Pythona wykorzystująca bibliotekę Qt, umożliwia m. in. wyświetlanie wykresów utworzonych
  z wykorzystaniem *matplotlib*.



Pip
-------

Przydatne polecenia:

.. code-block:: bash

    ~$ pip -V  # wersja narzędzia pip
    ~$ pip list  # lista zainstalowanych pakietów
    ~$ sudo pip install nazwa_pakietu  # instalacja pakietu
    ~$ sudo pip install nazwa_pakietu -U  # aktualizacja pakietu
    ~$ sudo pip uninstall  # usunięcie pakietu

.. _XFCE: http://www.xfce.org/
