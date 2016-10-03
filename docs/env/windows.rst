.. _windows-env:

Przygotowanie systemu Windows
#############################

Przykłady zostały przygotowane z myślą o systemie Linux.
Przygotowana i polecana przez nas przenośna wersja Linuksa :ref:`LxPup <linux-live>`
zawiera wszystkie potrzebne narzędzia i biblioteki.
Można je również wykonywać w środowisku Windows. Cały kod działa tak samo,
jednak niektóre biblioteki w wersjach binarnych trzeba ściągnąć i zainstalować ręcznie.

.. note::

    Pamiętaj, by w systemie Windows zmieniać znaki ``/`` (slash) na ``\`` (backslash) w ścieżkach
    podawanych w scenariuszach, podobnie pozamieniaj komendy systemu Linux
    na odpowiedniki wiersza poleceń Windows.

.. contents:: Spis treści
    :backlinks: none

.. _ins-python:

Inerpreter Pythona
==================

Na stronie `Python Releases for Windows <https://www.python.org/downloads/windows/>`_ klikamy
link *Last Python 2 Release - ...* i pobieramy plik :file:`Windows x86 MSI installer` dla
Windowsa 32-bitowego lub :file:`Windows x86-64 MSI installer` dla edycji 64-bitowej.

.. tip::

    Podczas instalacji zaznaczamy opcję "Add Python.exe to Path".

.. figure:: img/python_windows01.jpg

Narzędzia i biblioteki
======================

Narzędzia wymagane:

* `pip <https://pip.pypa.io/en/stable/>`_  – instalator pakietów Pythona, podstawowe narzędzie
  służące do zarządzania pakietami Pythona zgromadzonymi np.
  w repozytorium `PyPI <https://pypi.python.org/pypi>`_  (Python Package Index);
* `virtualenv <https://virtualenv.readthedocs.org/en/latest/>`_  – menedżer wirtualnych środowisk Pythona,
  pozwala tworzyć katalogi zawierające izolowane środowisko Pythona umożliwiające instalowanie
  wybranych wersji pakietów przez zwykłych użytkowników;
* `klient git <https://git-scm.com/downloads>`_  – narzędzie umożliwiające korzystanie z repozytoriów
  kodu i dokumentacji w serwisie `Github <https://github.com/>`_
* `sqlite3 <https://www.sqlite.org/>`_ – konsolowa powłoka dla baz SQLite3, umożliwia przeglądanie
  schematów tabel oraz zarządzanie bazą za pomocą języka SQL.

Narzędzia dodatkowe:

* `ipython <http://ipython.org/>`_ – rozszerzona interaktywna konsola Pythona;
* `qtconsole <http://jupyter.org/qtconsole/stable/>`_  – rozszerzona interaktywna konsola
  Pythona wykorzystująca bibliotekę Qt, umożliwia m. in. wyświetlanie wykresów utworzonych
  z wykorzystaniem *matplotlib*.

Pip
----

Narzędzie uruchamiamy w wierszu poleceń (terminalu). Przydatne polecenia:

.. code-block:: bat

    pip -V  # wersja narzędzia pip
    pip list  # lista zainstalowanych pakietów
    pip install nazwa_pakietu  # instalacja pakietu
    pip install nazwa_pakietu -U  # aktualizacja pakietu
    pip uninstall  # usunięcie pakietu

Narzędzia ``pip`` użyjemy do instalacji pakietów *virtualenv*, *ipython* i *qtconsole*:

.. code-block:: bat

    pip install virtualenv
    pip install ipython qtconsole

.. _pyqt-win:

Biblioteki PyQt
----------------

*Qtconsole* wymaga bibliotek PyQt. W Windows 32-bitowym ze strony `PyQt4 Download <http://https://www.riverbankcomputing.com/software/pyqt/download>`_ pobieramy plik `PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x32.exe <http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.11.4/PyQt4-4.11.4-gpl-Py2.7-Qt4.8.7-x32.exe>`_
i instalujemy.

W wersji 64-bitowej Windowsa w terminalu wydajemy polecenie:

.. code-block:: bat

    pip install python-qt5

Git
----

Git to narzędzie do obsługi repozytoriów hostowanych w serwisie `GitHub <https://github.com/>`_.
Podstawowego klienta w wersji 32- lub 64-bitowej pobieramy ze strony `Downloading Git <https://git-scm.com/download/win>`_ i instalujemy, zaznaczając wszystkie opcje.

:ref:`Alternatywna metoda instalacji <git-install>`, jak również zasady pracy z repozytoriami
omówione zostały w osobnym :ref:`dokumencie <git-howto>`. Gorąco zachęcamy do jego przejrzenia.

.. _pygame-win:

PyGame
-------

Jest to moduł wymagany m.in. przez scenariusze gier. W przypadku Windows 32-bitowego ze strony
`PyGame <http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi>`_ pobieramy plik
`pygame-1.9.1.win32-py2.7.msi <http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi>`_
i instalujemy:

.. figure:: img/pygame_windows01.jpg

W przypadku wersji 64-bitowej ze strony `http://www.lfd.uci.edu/~gohlke/pythonlibs <http://www.lfd.uci.edu/~gohlke/pythonlibs>`_ pobieramy pakiet ``pygame-1.9.2b1-cp27-cp27m-win_amd64.whl``. Następnie
otwieramy terminal w katalogu z zapisanym pakietem i wydajemy polecenie:

.. code-block:: bat

    pip install pygame-1.9.2b1-cp27-cp27m-win_amd64.whl

.. _matplotlib-win:

Matplotlib
----------

Aby zainstalować **matplotlib**, wchodzimy na stronę `http://www.lfd.uci.edu/~gohlke/pythonlibs <http://www.lfd.uci.edu/~gohlke/pythonlibs>`_ i pobieramy pakiety ``numpy`` oraz ``matplotlib`` w formacie ``whl`` dostosowane do naszej wersji Pythona i Windows. Np. jeżeli zainstalowaliśmy *Pythona v. 2.7.12* i mamy *Windows 7 64-bit*, pobierzemy: ``numpy‑1.10.0b1+mkl‑cp27‑none‑win_amd64.whl``
i ``matplotlib‑1.4.3‑cp27‑none‑win_amd64.whl``. Następnie otwieramy terminal w katalogu z pobranymi pakietami
i instalujemy:

.. code-block:: bat

    pip install numpy‑1.10.0b1+mkl‑cp27‑none‑win_amd64.whl
    pip install matplotlib‑1.4.3‑cp27‑none‑win_amd64.whl

.. note::

    Oficjalne kompilacje **matplotlib** dla Windows dostępne są w serwisie
    `Sourceforge matplotlib <http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.5.0/windows/>`_.

.. _webapps-win:

Aplikacje internetowe
---------------------

Instalacja bibliotek wymaganych do scenariuszy:

.. code-block:: bat

    pip install flask django peewee sqlalchemy flask-sqlalchemy

.. _sqlite3-win:

SQLite3
-------

Ze strony `SQLite Download Page <http://>`_, z sekcji *Precompiled Binaries for Windows*
ściągamy skompilowany interpreter dla 32- lub 64-bitowej wersji Windows.
Przykładowe archiwum :file:`sqlite-dll-win64-x64-3140200.zip` należy rozpakować,
najlepiej do katalogu systemowego (:file:`C:\Windows\System32`),
żeby był dostępny z każdej lokalizacji.


Brak Pythona?
=============

Jeżeli nie możemy wywołać interpretera lub instalatora ``pip`` w terminalu,
oznacza to, że zapomnieliśmy zaznaczyć opcji "Add Python.exe to Path" podczas
instalacji interpretera. Najprościej zainstalować go jeszcze raz z zaznaczoną
opcją.

Można też samemu rozszerzyć zmienną systemową ``PATH`` swojego użytkownika
o ścieżkę do ``python.exe``. Najwygodniej wykorzystać konsolę PowerShell:

.. code-block:: posh

    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")

Ewentualnie, jeśli posiadamy uprawnienia administracyjne, możemy zmienić zmienną ``PATH`` wszystkim użytkownikom:

.. code-block:: posh

    $CurrentPath=[Environment]::GetEnvironmentVariable("Path", "Machine")
    [Environment]::SetEnvironmentVariable("Path", "$CurrentPath;C:\Python27\;C:\Python27\Scripts\", "Machine")

Jeżeli nie mamy dostępu do konsoli PowerShell, w oknie "Uruchamianie" (:kbd:`WIN+R`)
wpisujemy polecenie wywołujące okno "Zmienne środowiskowe" – można je również
uruchomić z okna właściwości komputera:

.. code-block:: bat

    rundll32 sysdm.cpl,EditEnvironmentVariables

.. figure:: img/winpath01.jpg
.. figure:: img/winpath02.jpg

Następnie klikamy przycisk "Nowa" i wpisujemy: ``PATH=%PATH%;c:\Python27\;c:\Python27\Scripts\``;
w przypadku zmiennej systemowej klikamy "Edytuj", a ścieżki ``c:\Python27\;c:\Python27\Scripts\``
dopisujemy po średniku. Dla pojedynczej sesji (do momentu przelogowania się) możemy użyć
polecenia w konsoli tekstowej:

.. code-block:: bat

    set PATH=%PATH%;c:\Python27\;c:\Python27\Scripts\