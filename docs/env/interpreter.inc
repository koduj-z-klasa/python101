Interpreter Pythona
####################

Python to język interpretowany. Kod źródłowy Pythona zapisujemy w plikach tekstowych
z rozszerzeniem ``.py``.

**Uruchamianie programów**

Programy Pythona uruchamiamy w terminalu przy użyciu interpretera:

.. code-block:: bash

    ~$ python3 nazwa_skryptu.py

– lub z poziomu edytora kodu, który oferuje taką możliwość.


**Testowanie kodu**

Tryb interaktywny interpretera Pythona jest podstawowym narzędziem nauki
i testowania kodu. Uruchamiamy go, wydając w terminalu używanego systemu
polecenie:

.. code-block:: bash

    ~$ python3

Proponujemy korzystanie z rozszerzonych powłok, oferujących dodatkowe podpowiedzi,
dopełanianie i formatowanie kodu itp. ułatwienia. W terminalu polecamy ``ipython``
uruchamiany poleceniem:

.. code-block:: bash

    ~$ ipython3

Najwięcej możliwości oferuje wersja graficzna ``qtconsole`` wykorzystująca bibliotekę
`Qt <https://pl.wikipedia.org/wiki/Qt>`_, pozwala m.in. na wygodne wklejanie kodu
i osadzanie obiektów `matplotlib <https://matplotlib.org>`_.
Uruchomimy ją poleceniem w terminalu:

.. code-block:: bash

    ~$ jupyter-qtconsole

– lub z menu start systemu naszego systemu.

Po uruchomieniu interpreter wyświetli swoją wersję, opcojonalie wersję kompilatora C++,
informację o sposobie uzyskania pomocy (polecenie ``help``), na końcu zaś
znak zachęty ``>>>`` lub ``In[1]``. Jeżeli będziemy testować instrukcje złożone, np.
warunkowe lub pętle, w interpreterze zobaczymy znaki ``...`` oznaczające,
że wprowadzany kod wymaga wcięć.

**Kodowanie**

Ze względów praktycznych warto korzystać z programów ułatwiających pisanie kodu
(obsługa wcięć, podświetlenia itd.), tzw. IDE,
czyli `Integrated Development Environment <http://pl.wikipedia.org/wiki/Zintegrowane_%C5%9Brodowisko_programistyczne>`_,
np. :ref:`Geany <geany-python>`, :ref:`Sublime-Text <st3-python>` lub :ref:`PyCharm <pycharm-python>`.
Wymienione programy działają na platformie Linux i Windows.

.. note::

    Do terminala polecenia kopiujemy i wklejamy bez znaku zachęty ``$``
    i poprzedzającego tekstu za pomocą środkowego klawisza myszki
    lub skrótów :kbd:`CTRL+SHIFT+V`, :kbd:`CTRL+SHIFT+Insert`.

Narzędzia i biblioteki
======================

**Omówienie narzędzi:**

* `pip <https://pip.pypa.io/en/stable/>`_  – instalator pakietów Pythona,
  podstawowe narzędzie służące do zarządzania pakietami Pythona zgromadzonymi
  w repozytorium `PyPI <https://pypi.python.org/pypi>`_  (Python Package Index);
* `virtualenv <https://virtualenv.readthedocs.org/en/latest/>`_  –
  menedżer wirtualnych środowisk Pythona, pozwala tworzyć katalogi zawierające
  izolowane wersje Pythona umożliwiające instalowanie wybranych wersji pakietów
  przez zwykłych użytkowników;
* `klient git <https://git-scm.com/downloads>`_  – narzędzie wersjonowania kodu
  umożliwiające korzystanie z repozytoriów w serwisie `Github <https://github.com/>`_;
* `sqlite3 <https://www.sqlite.org/>`_ – konsolowa powłoka dla baz SQLite3,
  umożliwia przeglądanie schematów tabel oraz zarządzanie bazą za pomocą języka SQL;
* `ipython <http://ipython.org/>`_ i `qtconsole <http://jupyter.org/qtconsole/stable/>`_
  – rozszerzone interaktywna konsola Pythona.


Pip
-------

Przydatne polecenia:

.. code-block:: bash

    ~$ pip -V  # wersja narzędzia pip
    ~$ pip list  # lista zainstalowanych pakietów
    ~$ sudo pip install nazwa_pakietu  # instalacja pakietu
    ~$ sudo pip install nazwa_pakietu -U  # aktualizacja pakietu
    ~$ sudo pip uninstall  # usunięcie pakietu

