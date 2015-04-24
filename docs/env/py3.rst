Wykorzystanie Python 3
######################

Podstawą szkolenia jest, jak zaznaczono na początku, interpreter Pythona w wersji 2.7.x,
który standardowo dostępny jest w dystrybucjach linuksowych. Można jednak korzystać
z interpretera w wersji 3.4.x, czyli najnowszej stabilnej, pamiętając że:

* funkcja wejścia ``input_raw()`` została zastąpiona przez funkcję ``input()``,
  zachowanie poprzednie można emulować używając ``eval(input())``, co nie
  jest jednak zalecane;

* wyrażenie wyjścia ``print`` zostało zastąpione funkcją ``print()``, a więc
  wystarczy dodać nawiasy...

* dodatkowe moduły trzeba zainstalować osobno dla wersji 3.4.x

Instalacja w systemie Linux
===========================

W systemach opartych na Debianie instalacja modułów dla interpretera
w wersji 3.x wymaga dodania do nazw cyfry 3, np. ``python3 -pip`` itd.
W Arch Linuksie i pochodnych jest odwrotnie, domyślną wersją jest Python 3,
jeżeli chcemy używać wersji 2.x dodajemy odpowiednią cyfrę.
Warto również zauważyć, że systemy oparte na Archu mogą nie wykorzystywać
mechanizmu podnoszenia uprawnień zwykłego użytkownika ``sudo``,
wtedy instalujemy z konta ``roota``, stąd znak ``~#`` w kodzie.
