Wykorzystanie Python 3
######################

Podstawą szkolenia jest, jak zaznaczono na początku, interpreter Pythona w wersji 2.7.x,
który standardowo dostępny jest w dystrybucjach linuksowych. Można jednak korzystać
z interpretera w wersji 3.x, pamiętając że:

* funkcja wejścia ``input_raw()`` została zastąpiona przez funkcję ``input()``,
  zachowanie poprzednie można emulować używając ``eval(input())``, co nie
  jest jednak zalecane;

* wyrażenie wyjścia ``print`` zostało zastąpione funkcją ``print()``, a więc
  wystarczy dodać nawiasy...

* dodatkowe moduły trzeba zainstalować osobno dla wersji 3.x używając odpowiedniej
  wersji narzędzia pip.

Instalacja Windows
==================

Ściągamy *interpreter Pythona* w wersji 3.x i instalujemy ręcznie.

Instalacja Linux
================

Python 3 jest podstawowym składnikiem wszystkich głównych dystrybucji Linuksa.

W systemach opartych na *Debianie* instalacja bibliotek dla interpretera
w wersji 3.x wymaga użycia polecenia ``pip3``.

W *Arch Linuksie* i pochodnych jest odwrotnie, domyślną wersją jest Python 3
i polecenie ``pip``. Jeżeli chcemy używać wersji 2.x używamy polecenia ``pip2``.
