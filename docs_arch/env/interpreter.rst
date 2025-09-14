Podstawy Pythona
################

Python to język interpretowany. Kod źródłowy Pythona zapisujemy w plikach tekstowych
z rozszerzeniem ``.py``. Skrypty Pythona **uruchamiamy** w terminalu przy użyciu interpretera:

.. code-block:: bash

    ~$ python3 nazwa_skryptu.py

– lub z poziomu edytora kodu, który oferuje taką możliwość.

Ze względów praktycznych warto korzystać z programów ułatwiających pisanie kodu
(obsługa wcięć, podświetlenia itd.), tzw. IDE,
czyli `Integrated Development Environment <http://pl.wikipedia.org/wiki/Zintegrowane_%C5%9Brodowisko_programistyczne>`_.
Zobacz `Edytory kodu <https://linetc.readthedocs.io/pl/latest/tools/edytory/index.html>`_.

**Tryb interaktywny** interpretera Pythona jest podstawowym narzędziem nauki
i testowania kodu. Uruchamiamy go, wydając w terminalu używanego systemu
polecenie:

.. code-block:: bash

    ~$ python3

Po uruchomieniu interpreter wyświetla swoją wersję, opcjonalnie wersję kompilatora C++,
a także znak zachęty ``>>>``. Przydatne polecenia:

.. code-block:: bash

    >>> help()         # uruchomienie interaktywnej pomocy
    help> quit         # wyjście z trybu interaktywnej pomocy
    >>> help(obiekt)   # wyświetla pomoc dotyczącą dowolnego obiektu
    >>> import math    # zaimportowanie przykładowego modułu math
    >>> dir(math)      # przegląd dostępnych w module stałych i funkcji
    >>> help(math.pow) # wyświetla pomoc nt. stałej lub funkcji dostępnej w module
    >>> exit()         # wyjście z trybu iteraktywnego interpretera

Znaki ``...`` oznaczają, że testujemy instrukcję złożoną, np. warunkową lub pętlę,
i dalszy kod wymaga wcięć.

.. _pve:

Środowisko wirtualne
====================

Wirtualne środowisko Pythona (ang. *Python virtual environment*) pozwala instalować dodatkowe pakiety
w wybranych wersjach, a także dodatkowe narzędzia bez uprawnień administratora. W praktyce to katalog
zawierający niezbędne pliki potrzebne do działania interpretera oraz menedżer *pip*.
Po utworzeniu środowiska przed każdym użyciem należy go aktywować.

Utworzenie i korzystanie ze środowiska:

.. code-block:: bash

    ~$ python3 -m venv pve           # utworzenie środowiska katalogu pve
    ~$ source pve/bin/activate       # aktywacja w Linuksie
    > pve\\Scripts\\activate.bat     # aktywacja w Windowsie
    (pve) ~$ python skrypt.py        # uruchamianie skryptu w wirtualnym środowisku
    (pve) ~$ deactivate              # deaktywacja

Przydatne polecenia instalatora pakietów *pip*:

.. code-block:: bash

    (pve) ~$ pip install biblioteka==1.4   # instalacja biblioteki we wskazanej wersji
    (pve) ~$ pip -V                        # wersja narzędzia pip
    (pve) ~$ pip list                      # lista zainstalowanych pakietów
    (pve) ~$ pip install nazwa_pakietu     # instalacja pakietu
    (pve) ~$ pip install nazwa_pakietu -U  # aktualizacja pakietu
    (pve) ~$ pip uninstall nazwa_pakietu   # usunięcie pakietu

Przykład instalacji pakietów wykorzystywanych w materiałach:

.. code-block:: bash

    ~$ sudo pip3 install matplotlib
    ~$ sudo pip3 install pygame
    ~$ sudo pip3 install flask flask-wtf peewee sqlalchemy flask-sqlalchemy django

Rozszerzone powłoki
===================

Zchęcamy do korzystania z powłok rozszerzonych *IPython* i/lub *Jupyter QtConsole*,
oferujących podpowiedzi, dopełnianie, formatowanie kodu itp. ułatwienia.
Najłatwiej zainstalować je w środowisku wirtualnym:

.. code-block:: bash

    (pve) ~$ pip install ipython3
    (pve) ~$ pip install qtconsole pyqt5

Uruchamiamy je poleceniami:

.. code-block:: bash

    ~$ ipython3
    ~$ jupyter-qtconsole

.. tip::

    Do terminala skopiowane polecenia wklejamy bez znaku zachęty ``$``
    i poprzedzającego tekstu za pomocą środkowego klawisza myszki
    lub skrótów :kbd:`CTRL+SHIFT+V`, :kbd:`CTRL+SHIFT+Insert`.
