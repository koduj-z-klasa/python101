Interpreter Pythona
###################

Python to język interpretowany. Kod źródłowy Pythona zapisujemy w plikach tekstowych
z rozszerzeniem ``.py``.

**Uruchamianie programów**

Programy Pythona uruchamiamy w terminalu przy użyciu interpretera:

.. code-block:: bash

    ~$ python3 nazwa_skryptu.py

– lub z poziomu edytora kodu, który oferuje taką możliwość.


**Interaktywna konsola**

Tryb interaktywny interpretera Pythona jest podstawowym narzędziem nauki
i testowania kodu. Uruchamiamy go, wydając w terminalu używanego systemu
polecenie:

.. code-block:: bash

    ~$ python3

Zalecamy korzystanie z powłok rozszerzonych, oferujących podpowiedzi,
dopełnianie i formatowanie kodu itp. ułatwienia. W terminalu rozszerzoną powłokę
uruchamiany poleceniem:

.. code-block:: bash

    ~$ ipython3

Najwięcej możliwości oferuje wersja graficzna ``qtconsole`` (oparta na bibliotece
`Qt <https://pl.wikipedia.org/wiki/Qt>`_). Pozwala m.in. na wygodne wklejanie kodu
i osadzanie obiektów `matplotlib <https://matplotlib.org>`_.
Uruchomimy ją poleceniem w terminalu:

.. code-block:: bash

    ~$ jupyter-qtconsole
    lub
    ~$ ipython3 qtconsole

– lub z menu start naszego systemu.

Po uruchomieniu interpreter wyświetli swoją wersję, opcjonalnie wersję kompilatora C++,
informację o sposobie uzyskania pomocy (polecenie ``help``), na końcu zaś
znak zachęty ``>>>`` lub ``In[1]``. Jeżeli będziemy testować instrukcje złożone, np.
warunkowe lub pętle, w interpreterze zobaczymy znaki ``...`` oznaczające,
że wprowadzany kod wymaga wcięć.

.. tip::

  Python występuje w wersji 2.x i 3.x, które w systemach Linux są zazwyczaj preinstalowane.
  Domyślna wersja w danej dystrybucji uruchamiana jest poleceniem ``python``.
  Można precyzyjnie wybrać wersję interpretera za pomocą poleceń: ``python2`` lub ``python3``.


**Kodowanie**

Ze względów praktycznych warto korzystać z programów ułatwiających pisanie kodu
(obsługa wcięć, podświetlenia itd.), tzw. IDE,
czyli `Integrated Development Environment <http://pl.wikipedia.org/wiki/Zintegrowane_%C5%9Brodowisko_programistyczne>`_.
Zobacz :ref:`IDE – edytory kodu <ide>`

.. tip::

    Do terminala skopiowane polecenia wklejamy bez znaku zachęty ``$``
    i poprzedzającego tekstu za pomocą środkowego klawisza myszki
    lub skrótów :kbd:`CTRL+SHIFT+V`, :kbd:`CTRL+SHIFT+Insert`.

