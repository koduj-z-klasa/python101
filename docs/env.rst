Środowisko systemowe i wymagane oprogramowanie
==============================================

Postaraliśmy się by każdy z uczestników szkolenia `Koduj z Klasą`_ otrzymał
gotowe środowisko, dzięki unifikacji minimalizujemy liczbę problemów
konfiguracyjnych. Jednak przygotowanie swojego środowiska nie wymaga
dużych nakładów pracy, wystarczy wykonać kilka krótkich instrukcji by
dostosować swój komputer na potrzeby tego szkolenia.

.. _Koduj z Klasą: http://kodujzklasa.pl

Szkolny Remix Ucznia (SRU)
-------------------------

Nasze materiały zakładają wykorzystanie Szkolnego Remixu Ucznia (SRU)
ze względu na jego gotowość do realizacji celów szkoleniowych niemal z pudełka.

http://sru.e-swoi.pl

Przykłady zakładają jednakową ścieżkę do katalogu domowego użytkownika,
w przypadku innych instalacji należy uwzględniać własną ścieżkę:

.. code-block:: bash

    /home/sru


LiveCD lub uruchomienie z Pendrive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   

Środowisko SRU jest przygotowane do uruchomienia bez instalacji na komputerach
z wykorzystaniem tzw. Live CD. W ramach programu Koduj z Klasą przekazujemy
pamięci USB zawierające SRU i umożliwiające uruchomienie systemu bez instalacji.

.. note::
    Pamięci USB zwykle są tak przygotowane że pomiędzy uruchomieniami
    zapamiętywane są tylko zmiany w katalogu domowym. Dzięki temu użytkownicy
    nie mogą popsuć konfiguracji systemu, ale też nie są wstanie instalować
    nowego oprogramowania.

Dla komputerów z systemem Windows 8 i BIOS UEFI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Przepraszamy, ale Microsoft bardzo się stara, aby utrudnić używanie innych systemów
niż ich własny w nowych komputerach. Dlatego też w nowych laptopach czasami nawet nie ma
możliwości startu systemu z pamięci USB, nie ma też napędu DVD.
Nieważne. Dajemy Wam do dyspozycji narzędzie, które pozwoli używać system w okienku.
Aby używać Szkolny Remiks Ucznia jako maszynę wirtualną bez konieczności startu z USB,
zainstalujcie Virtualbox, a następnie pobierzcie plik OVA i po prostu kliknijcie na niego dwa razy.
Następnie postępujcie wg wskazówek wyświetlanych przez VirtualBox. Po wykonanym imporcie, 
będziecie mogli po prostu uruchomić maszynę w Virtualbox. 
Po imporcie plik OVA można skasować, aby nie zabierał już miejsca. Nie będzie więcej potrzebny.
pamięci USB zawierające SRU i umożliwiające uruchomienie systemu bez instalacji.

Niezbędne pakiety:

Virtualbox - wersja dla Windows: http://www.cyfrowaszkola.waw.pl/_pliki/Virtualbox_abix.exe

OVA ze Szkolnym Remiksem: http://www.cyfrowaszkola.waw.pl/_python/SRU_FWIOO.ova

.. note::
    Dosyć szczegółowy opis instalacji znajdziecie na stronie
    http://cyfrowaszkola.waw.pl/free_desktop-uruchomienie-wewnatrz-ms-windows-macos-osx/
    Nie jest to opis dla Szkolnego Remiksu, który używamy tu na szkoleniach, 
    ale jest analogiczny i możecie spokojnie się nim posiłkować.

Brakujące komponenty
^^^^^^^^^^^^^^^^^^^^

Na starszych wersjach SRU może brakować oprogramowania przydatnego podczas szkolenia
warto je do instalować

Pobranie przykładów na komputerze uruchomionego z pomocą LiveCD lub Pendrive SRU
wymaga wcześniejszego instalacji narzędzia GIT, w terminalu (Win+T) uruchamiamy:

.. code-block:: bash

    $ sudo apt-get install git

Inne systemy Linux
^^^^^^^^^^^^^^^^^^

Wykorzystanie innych systemów Linux do celów szkoleniowych nie powinno
sprawiać większych problemów pod warunkiem, że uzupełnimy brakujące oprogramowanie.

Do instalacji wykorzystujemy systemowy package manager,
przykładowo dla Ubuntu i Debiana:

.. code-block:: bash

    $ sudo apt-get build-dep python-pygame
    $ sudo apt-get install python-dev python-pip python-virtualenv

Środowisko Windows
------------------

Nie zalecamy wykorzystania Windows ze względu na kompatybilność poleceń
i ścieżek do plików używanych w scenariuszach. Jednak użycie Windows jako
środowiska szkoleniowego nie jest wykluczone.

.. note::
    Pamiętaj by zmieniać znaki `/` (slash) na `\\` (backslash) w ścieżkach,
    natomiast w miejscu komend systemu Linux użyj bliskich zamienników z Windows.


Instalacja Python 2.7 pod windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Możemy szybko zainstalować Python z pomocą konsoli PowerShell (taka niebieska)

.. code-block:: powershell

    (new-object System.Net.WebClient).DownloadFile("https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi", "$pwd\python-2.7.8.msi")
    msiexec /i python-2.7.8.msi TARGETDIR=C:\Python27
    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
    (new-object System.Net.WebClient).DownloadFile("https://raw.github.com/pypa/pip/master/contrib/get-pip.py", "$pwd\get-pip.py")
    C:\Python27\python.exe get-pip.py virtualenv

Pozostałe biblioteki dystrybuowane w wersjach binarnych musimy zainstalować
z katalogu /arch/ w repo, pozostałe instalujemy za pomocą pip:

.. code-block:: bash

    pip install -r requirements.txt

Jak nie ma PowerShell
^^^^^^^^^^^^^^^^^^^^^

Jeśli nie mamy PowerShella to pozostaje ręcznie sciągnąć plik instalacyjny

https://www.python.org/downloads/

A następnie zainstalować pip przy użyciu świeżo zainstalowanego Pythona :)

.. code-block:: bash

    python -c "exec('try: from urllib2 import urlopen \nexcept: from urllib.request import urlopen');f=urlopen('https://raw.github.com/pypa/pip/master/contrib/get-pip.py').read();exec(f)"

Ponadto możemy ustawić zmienną systemową by za każdym razerm nie używać pełnej ścieżki.

.. code-block:: batch

    set PATH=%PATH%;c:\Python27\;c:\Python27\Scripts\

Środowisko programistyczne PyCharm
----------------------------------

PyCharm to profesjonalne, komercyjne środowisko programistyczne dostępne za darmo
do celów szkoleniowych.

To IDE doskonale wspiera proces uczenia się. Dzięki nawigacji po kodzie,
podpowiedziom oraz wykrywaniu błędów niemal na bieżąco uczniowie mniej
czasu będą spędzać na szukaniu problemów a więcej na poznawaniu tajników
programowania.

Szybka instalacja na systemach linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instalacja wersji testowej na systemach Linux wymaga pobrania i rozpakowania archiwum:

.. code-block:: bash

    wget http://download.jetbrains.com/python/pycharm-professional-3.4.1.tar.gz -O - | tar -xz
    ./pycharm-3.4.1/bin/pycharm.sh

Ręczna instalacja
^^^^^^^^^^^^^^^^^

Na systemach Windows możemy zainstalować PyCharm po `pobraniu pliku instalacyjnego
ze strony producenta z pomocą przeglądarki <http://www.jetbrains.com/pycharm/download/>`_.


Jak zdobyć bezpłatną licencję
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Każdy nauczyciel może wystąpić o klucz licencyjny przy pomocy `formularza
dostępnego na stronie producenta <http://www.jetbrains.com/eforms/classroomRequest.action?licenseRequest=PCP04LS#>`_

Polski słownik ortograficzny
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

W programie możemy włączyć sprawdzanie polskiej pisowni, jednak potrzebne
jest wskazanie pliku słownika. W ustawieniach :kbd:`Ctrl+Alt+S` szukamy `spell` i dodajemy
``custom dictionaries folder`` wskazując na ``/usr/share/hunspell/`` (lokalizacja w SRU).
