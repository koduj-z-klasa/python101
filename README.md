Szkolenie Python 101
====================

Niniejsze materiały to dokumentacja i kody źródłowe do szkolenia z
języka Python realizowanego w ramach projektu [Koduj z Klasą][1]
prowadzonego przez Fundację [Centrum Edukacji Obywatelskiej][2].

Pełna dokumentacja szkolenia znajduje się tutaj:

<bit.ly/py-101>

Modyfikacje i budowa dokumentacji offline
-----------------------------------------

Materiały szkoleniowe są przygotowywane z pomocą oprogramowania [Sphinx w
wersji 1.3][3]. Ponieważ wersja ta jest jeszcze nie opublikowana należy ją 
zainstalować ze źródeł. W tym celu pobieramy archiwum:

    wget -O sphinx-latests.zip https://bitbucket.org/birkenfeld/sphinx/get/default.zip 
    unzip sphinx-latests.zip

Po rozpakowaniu znajdziemy folder podobny do tego `birkenfeld-sphinx-10d9deb02fd5`,
w nim wykonujemy polecenie instalacji Sphinxa w naszym środowisku Python.

    $ sudo python setup.py install 
        
Po instalacji możemy w folderze dokumentacji możemy uruchomić make:
  
    ~/python101/docs$ make html

  [1]: http://www.ceo.org.pl/koduj
  [2]: http://www.ceo.org.pl/
  [3]: http://sphinx-doc.org/latest/
