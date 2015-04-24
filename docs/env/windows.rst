Przygotowanie systemu Windows
#############################

Przykłady zostały przygotowane myślą o systemie Linux, jednak bez większych problemów
powinniśmy móc je zaadaptować dla środowiska Windows.
Cały kod działa tak samo, jednak niektóre biblioteki trzeba ściągnąć i zainstalować ręcznie w wersjach binarnych.

.. note::

    Pamiętaj, by w systemie Windows zmieniać znaki ``/`` (slash) na ``\`` (backslash) w ścieżkach
    podawanych w scenariuszach, podobnie pozamieniaj komendy systemu Linux
    na odpowiedniki wiersza poleceń Windows.

.. contents:: Spis treści
    :backlinks: none

Instalacja przez PowerShell
===========================

Punktem wyjścia jest instalacja interpretera Pythona. Wersję 2.7.8 szybko zainstalujemy
za pomocą konsoli PowerShell (oznaczonej niebieską ikoną i niebieskim tłem). Wystarczy skopiować
poniższy kod linia po linii, wkleić i wykonać:

.. code-block:: posh

    (new-object System.Net.WebClient).DownloadFile("https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi", "$pwd\python-2.7.8.msi")
    msiexec /i python-2.7.8.msi TARGETDIR=C:\Python27
    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
    (new-object System.Net.WebClient).DownloadFile("https://raw.github.com/pypa/pip/master/contrib/get-pip.py", "$pwd\get-pip.py")
    C:\Python27\python.exe get-pip.py virtualenv


Instalacja ręczna
=================

Jeżeli w naszej wersji Windows nie ma PowerShella, ściągamy `interpreter Pythona`_ w wybranej
wersji (2.7.x lub 3.4.x) i instalujemy ręcznie.

.. tip::

Warto jest zaznaczyć opcję "Add Python.exe to Path", która domyślnie nie jest włączona.

.. _interpreter Pythona: https://www.python.org/downloads/

.. figure:: img/python_windows01.jpg

Instalacja PIP
--------------

Następnie instalujemy program ``pip`` do zarządzania dodatkowymi bibliotekami za pomocą polecenia:

.. code-block:: bash

    python -c "exec('try: from urllib2 import urlopen \nexcept: from urllib.request import urlopen');f=urlopen('https://raw.github.com/pypa/pip/master/contrib/get-pip.py').read();exec(f)"

Brak Pythona na ścieżce wywołań?
================================

Gdyby jakieś wywołania Pythona nie działały, warto do zmiennej ``PATH`` (użytkownika
lub systemowej) dodać ścieżki do interpretera i polecenia ``pip``. W oknie "Uruchamianie" (:kbd:`WIN+R`)
wpisujemy polecenie wywołujące okno "Zmienne środowiskowe" – można je również
uruchomić z okna właściwości komputera:

.. code-block:: bat

    rundll32 sysdm.cpl,EditEnvironmentVariables

.. figure:: img/winpath01.jpg
.. figure:: img/winpath02.jpg

.. note::

    Dla wersji Python 3.x trzeba odpowiednio dostosować ścieżkę instalacji Pythona.

Następnie klikamy przycisk "Nowa" i wpisujemy: ``PATH=%PATH%;c:\Python27\;c:\Python27\Scripts\``;
w przypadku zmiennej systemowej klikamy "Edytuj", a ścieżki ``c:\Python27\;c:\Python27\Scripts\``
dopisujemy po średniku. Dla pojedynczej sesji (do momentu przelogowania się) możemy użyć
polecenia w konsoli tekstowej:

.. code-block:: bat

    set PATH=%PATH%;c:\Python27\;c:\Python27\Scripts\

Instalacja bibliotek wymaganych przez scenariusze
=================================================

Biblioteki instalujemy za pomocą polecenia ``pip``:

.. code-block:: bash

    pip install flask django
    pip install peewee sqlalchemy flask-sqlalchemy

Pozostaje instalacja bibliotek wymaganych przez scenariusze.
Moduł wymagany przez gry pobieramy z katalogu `/arch/` zawartego w repozytorium
lub ze strony `PyGame`_ i instalujemy:

.. figure:: img/pygame_windows01.jpg

.. _PyGame: http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi


GIT i GitHub
============

Jeżeli chcemy pod Windowsem korzystać z mechanizmów oferowanych przez serwis
GitHub, musimy zainstalować odpowiedniego :ref:`klienta <git-install>`.
Zagadnienia te omówione zostały w osobnym :ref:`dokumencie <git-howto>`,
który warto przejrzeć.
Instalacja Git-a nie jest wymagana, aby pracować na przygotowanych scenariuszach.

