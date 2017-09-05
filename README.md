Szkolenia Python 101
====================

Niniejsze materiały to dokumentacja i kody źródłowe do szkoleń z
języka Python realizowanych w ramach projektu [Koduj z Klasą][1]
prowadzonego przez Fundację [Centrum Edukacji Obywatelskiej][2].

Wersja HTML dokumentacji znajduje się pod adresem:

http://python101.rtfd.io

Nasze repozytorium
-------------------

Zachęcamy do sklonowania tego repozytorium lokalnie:

    $ git clone https://github.com/koduj-z-klasa/python101/

Można je również pobrać jako archiwum ZIP:

https://github.com/koduj-z-klasa/python101/archive/master.zip

Forum Koduj z Klasą
--------------------

Zachęcamy do dyskusji i zadawania pytań na forum:

http://discourse.kodujzklasa.pl/

Linki do zapamiętania
---------------------

Polecamy poniższe strony jako źródła dodatkowych materiałów dla uczestników szkoleń:

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

- Proste przykłady OEIiZK dla pythona
  http://python.oeiizk.edu.pl/

- Darmowy soft i usługi dla uczniów (w tym 100$ na serwer w internecie, hosting na ok. 1,5 roku)
  https://education.github.com/pack

- Dokumentacja Python'a i bibliotek standardowych
  https://docs.python.org/3/

- PyPi: Python Package Index, miejsce w którym można poszukać biliotek instalowanych przy pomocy narzędzia PIP
  https://pypi.python.org/pypi

- Django: Framework do robienia aplikacji WWW z bateryjkami i dużym ekosystemem dodatków
  https://docs.djangoproject.com/en/1.11/

  Polecamy tutorial w języku polskim:
  https://docs.djangoproject.com/pl/1.11/intro/tutorial01/

- Flask: Elastyczny Framework do budowy aplikacji WWW. Prosty do prostych aplikacji.
  http://flask.pocoo.org/

- PyGame: Framework do tworzenia gier
  http://www.pygame.org/news.html


Modyfikacje i budowa dokumentacji offline
-----------------------------------------

Dokumentacja szkoleń przygotowywana jest za pomocą oprogramowania [Sphinx][3].
Można je zainstalować lokalnie i wygenerować materiały w formacie html samodzielnie:

    ~/python101$ sudo apt install python-pip
    ~/python101$ sudo pip install virtualenv
    ~/python101$ virtualenv .pve
    ~/python101$ source .pve/bin/activate
    (.pve) ~/python101$ pip install sphinx sphinx-rtd-theme

Po instalacji w folderze dokumentacji wydajemy polecenie:

    (.pve) ~/python101/docs$ make html

Autorzy
-------

- Robert Bednarz <ecg@ecg.vot.pl>
- Adam Jurkiewicz <biuro@cyfrowaszkola.waw.pl>
- [Janusz Skonieczny][4]

  [1]: http://www.ceo.org.pl/koduj
  [2]: http://www.ceo.org.pl/
  [3]: http://sphinx-doc.org/latest/
  [4]: http://plus.google.com/+JanuszSkonieczny/
