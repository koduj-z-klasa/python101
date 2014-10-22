Szkolenie Python 101
====================

Niniejsze materiały to dokumentacja i kody źródłowe do szkolenia z
języka Python realizowanego w ramach projektu [Koduj z Klasą][1]
prowadzonego przez Fundację [Centrum Edukacji Obywatelskiej][2].

Pełna dokumentacja szkolenia znajduje się tutaj:

[bit.ly/kzk-py](http://bit.ly/kzk-py)

Pobieranie tego repozytorium
----------------------------

Gorąco zalecamy do klonowania tego repozytorium lokanie:

    $ git clone git@github.com:koduj-z-klasa/python101.git

Wszystkie kody źródłowe można też pobrać jako archiwum ZIP bezpośrednio z tego repozytorium 
bez wykorzystania narzędzia GIT, jednak stracimy wtedy możliwość wykonywania
skoków pomiędzy etapami które zostały wskazane w materiałach szkoleniowych.

https://github.com/koduj-z-klasa/python101/archive/master.zip

Dodatkowe materiały 
-------------------

1. [Folder z materiałami Roberta Bednarza](https://www.dropbox.com/sh/mvvz59by7buh2oz/AAAFC-rYZHAOmjQmDCThi72Na?dl=0)
2. [Podstawy Python'a Doroty Rybickiej](https://drive.google.com/file/d/0B1hYVXsrSXCKY0hwZ3FHcHAwdDhpVDI2MmVIcVgybFV2UWZ3/view?usp=sharing)

Linki do zapamiętania dla uczestników
-------------------------------------

Polecamy do zajrzenia na poniższe strony jeśli będziecie szukać informacji po szkoleniu.

- GitHub: Bezpłatne publiczne repozytoria kodu źródłowego  
  https://github.com/

- BitBucket: Bezpłatne prywatne repozytoria kodu źródłowego dla małych zespołów  
  https://bitbucket.org/

- SourceTree: Okienkowa aplikacja dla GIT pod Windows  
  http://www.sourcetreeapp.com/

- PyCharm: Środowisko IDE dla Pythona bezpłatne na nauczycieli i uczniów  
  https://www.jetbrains.com/student/

- Python101: Nasze repozytorium materiałów szkoleniowych  
  https://github.com/koduj-z-klasa/python101

- Strona główna programu KZK dla Python  
  http://www.ceo.org.pl/pl/kodujzklasa/python

- Forum KZK  
  http://forum.kodujzklasa.pl/

- Proste przykłady OEIiZK dla pythona  
  http://python.oeiizk.edu.pl/

- Darmowy soft i usługi dla uczniów (w tym 100$ na serwer w internecie, hosting na ~1,5 roku)  
  https://education.github.com/pack

- Dokumentacja Python'a i bibliotek standardowych  
  https://docs.python.org/2.7/

- PyPi: Python Package Index, miejsce w którym można poszukać biliotek instalowanych przy pomocy narzędzia PIP  
  https://pypi.python.org/pypi

- Django: Framework do robienia aplikacji WWW z bateryjkami i dużym ekosystemem dodatków  
  https://docs.djangoproject.com/en/1.7/ - polecam zrobienie tutoriala 

- Flask: Elastyczny Frameworkdo budowy aplikacji WWW. Pomimo tego że jest na początek jest prosty, to zbudowanie większych aplikacji wymaga doświadczeń.  
  http://flask.pocoo.org/

- PyGame: Framework do tworzenia gier  
  http://www.pygame.org/news.html


Modyfikacje i budowa dokumentacji offline
-----------------------------------------

Materiały szkoleniowe są przygotowywane z pomocą oprogramowania [Sphinx w
wersji 1.3][3]. Ponieważ wersja ta nie jest jeszcze opublikowana należy ją 
zainstalować ze źródeł. W tym celu pobieramy archiwum:

    wget -O sphinx-latest.zip https://bitbucket.org/birkenfeld/sphinx/get/default.zip 
    unzip sphinx-latest.zip

Po rozpakowaniu znajdziemy folder podobny do tego `birkenfeld-sphinx-10d9deb02fd5`,
w nim wykonujemy polecenie instalacji Sphinx'a w naszym środowisku Python.

    $ sudo python setup.py install
    $ sudo pip install sphinx_rtd_theme
        
Po instalacji możemy w folderze dokumentacji możemy uruchomić make:
  
    ~/python101/docs$ make html

  [1]: http://www.ceo.org.pl/koduj
  [2]: http://www.ceo.org.pl/
  [3]: http://sphinx-doc.org/latest/
