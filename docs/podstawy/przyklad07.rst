.. _przyklad07:

Słownik i obsługa plików
########################

.. note::

    W tym przykładzie zobaczysz, na czym polega **zapis i odczyt plików** tekstowych w różnych formatach,
    poznasz kolejną złożoną strukturę danych – **słownik** oraz nauczysz się wykonywać kolejne operacje na napisach.

Zadanie
********

Napisz program :file:`slownik.py`, który pozwoli zapisywać w pliku tekstowym obce wyrazy oraz ich możliwe znaczenia.
Program powinien pobierać dane z klawiatury w formacie: ``wyraz obcy: znaczenie1, znaczenie2, ...`` itd.
Pobieranie danych kończy naciśnięcie klawisze :kbd:`ENTER`.
Podane dane powinny być zapisywane w pliku :file:`slownik.txt` i/lub :file:`slownik.csv`.
Program powinien odczytywać wcześniej zapisane dane, a użytkownik powinien mieć możliwość
dodawania nowych i zmieniania zapisanych danych.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python

.. literalinclude:: przyklad07_txt.py
    :linenos:

Słownik
-------

Słownik (zob. :term:`słownik`) to struktura nieuporządkowanych danych w formacie *klucz:wartość*.
Kluczami mogą być m.in. napisy i liczby, które wskazują na wartości dowolnego typu,
np. inne napisy, liczby, listy, krotki itd. W programie wykorzystujemy słownik,
którego kluczami są wyrazy obce, natomiast wartościami są listy możliwych znaczeń, np.:

.. code::

    slownik = {'go': ['iść', 'pojechać', 'chodzić'], 'look': ['patrzeć', 'poszukać'], 'see' : ['widzieć', 'zrozumieć']}

**Operacje na słowniku**:

* ``slownik = {}`` – utworzenie pustego słownika,
* ``slownik = { 'go':['iść','pojechać'] }`` – utworzenie 1-elementowego słownika,
* ``slownik['make'] = ['robić','tworzyć']`` – dodanie nowego elementu,
* ``slownik['go']`` – odczyt elementu wskazanego przez klucz.

Pliki tekstowe
---------------

Aby zilustrować niektóre operacje na napisach i listach, elementy słownika zapisywać
będziemy do pliku w formacie *wyraz_obcy:znaczenie1,znaczeni2,...*.
Funkcja ``otworz()`` przekształca format pliku na słownik,
a funkcja ``zapisz()`` słownik na format pliku.

**Operacje na plikach tekstowych**:

* ``os.path.isfile(plik)`` – zwraca prawdę, jeżeli podany plik istnieje,
* ``open(plik, "w")`` – otwarcie pliku w podanym trybie: ``"r"`` – odczyt(domyślny),
  ``"w"`` – zapis, ``"a"`` – dopisywanie,
* ``with open(nazwa_pliku) as plik:`` – otwarcie pliku w instrukcji ``with ... as ...`` zapewnia
  obsługę błędów, dba o zamknięcie pliku i udostępnia go w zmiennej ``plik``,
* ``for wiersz in plik:`` – plik tekstowy można rozumieć jako sekwencję wierszy, pętla ``for`` pozwala więc na odczyt
  kolejnych wierszy,
* ``plik.write(tresc)`` – zapisuje do pliku podaną treść,
* ``plik.close()`` – zamyka plik, ale lepiej używać konstrukcji z ``with``.

**Operacje na napisach**:

* ``.split(':')`` – dzieli tekst na części oddzielane podanym znakiem, zwraca je w postaci listy,
* ``','.join(lista)`` – łączy elementy listy podanym znakiem (w tym wypadku przecinkiem), zwraca tekst,
*	``.lower()`` – zamienia znaki na małe litery,
*	``.strip()`` – usuwa początkowe i końcowe białe znaki (spacje, tabulatory) oraz znaki końca wiersza,
* ``.replace('co','czym')`` – zastępuje w ciągu wszystkie wystąpienia *co – czym*,
* ``.count(znak)`` – zwraca liczbę wystąpień znaku w napisie.

W pętli głównej programu dane pobrane w formacie *wyraz_obcy:znaczenie1,znaczeni2,...*
rozbijamy na wyraz obcy i jego znaczenia, które zapisujemy w liście ``t``. Wszystkie elementy
oczyszczamy, tj. zamieniamy na małe litery i usuwamy białe znaki.
Funkcja ``map(oczysc, znaczenia)`` pozwala zastosować podaną jako pierwszy argument funkcję ``oczysc()``
do wszystkich elementów listy ``znaczenia`` podanej jako argument drugi.
Instrukcja ``list()`` przekształca zwrócony przez funkcję ``map()`` obiekt z powrotem na listę.

Format csv
----------

Dane tekstowe często zapisuje się w formacie `csv <https://pl.wikipedia.org/wiki/CSV_(format_pliku)>`_.
Jest to rozwiązanie wygodniejsze, ponieważ zwalnia nas od konieczności ręcznego przekształcania
odczytywanych z pliku linii na struktury danych.

Na początku pliku dodajemy import modułu: ``import csv``. Następnie zmieniamy nazwę pliku oraz funkcje
``otworz()`` i ``zapisz()`` na podane niżej:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: przyklad07_csv.py
    :linenos:
    :lineno-start: 5
    :lines: 5-24

Format CSV polega na zapisywaniu wartości oddzielonych separatorem, czyli domyślnie przecinkiem.
Jeżeli wartość zawiera znak separatora, jest cytowana domyślnie za pomocą cudzysłowu.
W naszym wypadku przykładowa linia pliku przyjmie postać: ``wyraz obcy,znaczenie1,znaczenie2,...``

**Operacje na plikach CSV**

- ``csv.reader(plik)`` – metoda interpretuje podany plik jako format CSV i każdą linię zwraca w postaci listy elementów,
  wyodrębnionych za pomocą separatora,
- ``csv.writer(plik)`` – metoda tworzy obiekt reprezentujący treść pliku w formacie CSV,
- ``.writerow(lista)`` – metoda umożliwia zapis listy elementów w formacie CSV w obiekcie zwróconym przez metodę
  ``.writer()``.

Instrukcja ``slownik[linia[0]] = linia[1:]`` zapisuje dane w słowniku, kluczem jest wyraz obcy (1 element listy),
wartościami lista znaczeń odczytana za pomocą notacji indeksowej.

Ćwiczenia
*********

1) Kod wypisujący słownik zamień na funkcję ``wypisz_slownik()`` i wykorzystaj ją do wypisywania słownika.
2) Rozszerz program tak, aby umożliwiał usuwanie elementów słownika.
3) Dodaj do programu możliwość uczenia się zapisanych w słowniku słówek, np. niech program wypisuje kolejne
   słowa obce i pobiera od użytkownika możliwe znaczenie i sprawdza, czy jest poprawne.

.. admonition:: Pojęcia

    :term:`słownik`, :term:`notacja wycinkowa`
