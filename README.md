Szkolenie Python 101
====================

Niniejsze materiały to dokumentacja i kody źródłowe do szkolenia z
języka Python realizowanego w ramach projektu [Koduj z Klasą][1]
prowadzonego przez Fundację [Centrum Edukacji Obywatelskiej][2].

Pełna dokumentacja szkolenia znajduje się tutaj:

http://koduj-z-klasa.github.io/python101/

Pobieranie tego repozytorium
----------------------------

Gorąco zalecamy do klonowania tego repozytorium lokanie:

    $ git clone https://github.com/koduj-z-klasa/python101/

Wszystkie kody źródłowe można też pobrać jako archiwum ZIP bezpośrednio z tego repozytorium 
bez wykorzystania narzędzia GIT, jednak stracimy wtedy możliwość wykonywania
skoków pomiędzy etapami które zostały wskazane w materiałach szkoleniowych.

https://github.com/koduj-z-klasa/python101/archive/master.zip

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
wersji 1.3][3]. Jeżeli chcemy lokalnie generować dokumentację, instalujemy Sphinksa z kodów źródlowych.

    ~/python101$ sudo apt-get install python mercurial git python-dev python-pip python-virtualenv
    ~/python101$ virtualenv .pve
    ~/python101$ source .pve/bin/activate
    ~/python101$ pip install sphinx_rtd_theme hg+https://bitbucket.org/birkenfeld/sphinx#sphinx
        
Po instalacji możemy w folderze dokumentacji możemy uruchomić make:
  
    ~/python101/docs$ make html

Autorzy
-------

- Robert Bednarz <ecg@ecg.vot.pl>
- Dorota Rybicka <rybicka.dorota@gmail.com>
- Adam Jurkiewicz <biuro@cyfrowaszkola.waw.pl>
- Grzegorz Wilczek <grzegorz.wilczek@ceo.org.pl>
- [Janusz Skonieczny][4]

  [1]: http://www.ceo.org.pl/koduj
  [2]: http://www.ceo.org.pl/
  [3]: http://sphinx-doc.org/latest/
  [4]: http://plus.google.com/+JanuszSkonieczny/
