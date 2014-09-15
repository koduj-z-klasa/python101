Python 101
=========+

Materiały dla nauczycieli do szkolenia z języka Python realizowanego w ramach
projektu Koduj z Klasą prowadzonego przez Fundację Centrum Edukacji Obywatelskiej

http://www.ceo.org.pl/koduj

## Założenia

Materiały zakładają wykorzystanie Szkolnego Remixu Ucznia (SRU)

http://sru.e-swoi.pl

Pobranie przykładów na komputerze uruchomionego z pomocą LiveCD lub Pendrive SRU
wymaga wcześniejszego instalacji narzędzia GIT, w terminalu (Win+T) uruchamiamy:

    sudo apt-get install git

Przykłady zakładają jednakową ścieżkę do katalogu domowego użytkownika,
w przypadku innych instalacji należy uwzględniać własną ścieżkę.

    /home/sru

## Pobranie materiałów

Materiały zostały podzielone w repozytorium na kilka gałęzi (branch). Dzięki temu
na początku szkolenia mamy niewielki zbiór plików, natomiast w kolejnych krokach
szkolenia możemy aktualizować wersję roboczą o nowe treści.

    git clone https://github.com/koduj-z-klasa/python101.git

Uczestnicy mogą spokojnie edytować i zmieniać materiały bez obaw
o późniejsze różnice względem reszty grupy. Możemy je szybko wyczyścić

    git reset --hard

Lub skoczyć do następnego punktu kontrolnego bez zachowania zmian

    git checkout --track origin/zadanie1b

Jeśli uczestnicy chą wcześniej zachować swoje modyfikacje mogą je zapisać
w swoim lokalnym repozytorium (wykonują tzw. commit).

## Inne systemy Linux

Na innych systemach z Linuksem musimy wyrzkostayć sysmewy package manager,
przykładowo dla Ubuntu i Debiana

    sudo apt-get build-dep python-pygame
    sudo apt-get install python-dev python-pip python-virtualenv

## Instalacja Python 2.7 pod windows

Możemy szybko zainstalować Python z pomocą konsoli PowerShell (taka niebieska)

    (new-object System.Net.WebClient).DownloadFile("https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi", "$pwd\python-2.7.8.msi")
    msiexec /i python-2.7.8.msi TARGETDIR=C:\Python27
    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
    (new-object System.Net.WebClient).DownloadFile("https://raw.github.com/pypa/pip/master/contrib/get-pip.py", "$pwd\get-pip.py")
    C:\Python27\python.exe get-pip.py virtualenv

Pozostałe biblioteki dystrybuowane w wersjach binarnych musimy zainstalować
z katalogu /arch/ w repo, pozostałe instalujemy za pomocą pip:

    pip install -r requirements.txt

### Jak nie ma PowerShell

Jeśli nie mamy PowerShella to pozostaje ręcznie sciągnąć plik instalacyjny

https://www.python.org/downloads/

A następnie zainstalować pip przy użyciu świeżo zainstalowanego Pythona :)

    python -c "exec('try: from urllib2 import urlopen \nexcept: from urllib.request import urlopen');f=urlopen('https://raw.github.com/pypa/pip/master/contrib/get-pip.py').read();exec(f)"

Ponadto możemy ustawić zmienną systemową by za każdym razerm nie używać pełnej ścieżki.

    set PATH=%PATH%;c:\Python27\;c:\Python27\Scripts\




