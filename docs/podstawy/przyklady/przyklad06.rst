.. _slownik-slowek:

Słownik słówek
##############

**ZADANIE**: Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia. Pobierz od użytkownika dane w formacie: *wyraz obcy: znaczenie1, znaczenie2, ...* itd. Pobieranie danych kończy wpisanie słowa "koniec".
Podane dane zapisz w pliku. Użytkownik powinien mieć możliwość dodawania nowych i zmieniania zapisanych danych.

**POJĘCIA**: *słownik, odczyt i zapis plików, formatowanie napisów.*

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 06_slownik_02.py
    :linenos:

Słownik (zob. :term:`slownik`) to struktura nieuporządkowanych danych w formacie *klucz:wartość*.
Kluczami są najczęściej napisy, które wskazują na wartości dowolnego typu,
np. inne napisy, liczby, listy, tuple itd. W programie wykorzystujemy słownik,
którego kluczami są wyrazy obce, natomiast wartościami są listy możliwych znaczeń.

Operacje na słowniku:

* ``slownik = { 'go':['iść','pojechać'] }`` – utworzenie 1-elementowego słownika;
* ``slownik['make'] = ['robić','marka']`` – dodanie nowego elementu;
* ``slownik['go']`` – odczyt elementu.

Aby zilustrować niektóre operacje na napisach i listach, elementy słownika zapisywać
będziemy do pliku w formacie *wyraz_obcy:znaczenie1,znaczeni2,...*.
Funkcja ``otworz()`` przekształca format pliku na słownik,
a funkcja ``zapisz()`` słownik na format pliku.

Operacje na plikach:

* ``os.path.isfile(plik)`` – sprawdzenie, czy istnieje podany plik;
* ``open(plik, "w")`` – otwarcie pliku w podanym trybie: *"r"* – odczyt(domyślny),
  *"w"* – zapis, *"a"* – dopisywanie;
* ``with open(plik) as zmienna:`` – otwarcie pliku w instrukcji ``with ... as ...`` zapewnia
  obsługę błędów, dba o zamknięcie pliku i udostępnia jego zawartość w *zmiennej*;
* ``for linia in zmienna:`` – pętla, która odczytuje kolejne linie pliku;
* ``plik.write(tresc)`` – zapisuje do pliku podaną treść;
* ``plik.close()`` – zamyka plik.

Operacje na napisach:

* ``.split(":")`` – zwraca listę części napisu wydzielone według podanego znaku;
* ``",".join(lista)`` – zwraca elementy listy połączone podanym znakiem (w tym wypadku przecinkiem);
*	``.lower()`` – zamienia znaki na małe litery;
*	``.strip()`` – usuwa początkowe i końcowe białe znaki (spacje, tabulatory);
* ``.replace("co","czym")`` – zastępuje w ciągu wszystkie wystąpienia *co – czym*;
* ``.count(znak)`` – zwraca ilość wystąpień znaku w napisie.

W pętli głównej programu dane pobrane w formacie *wyraz_obcy:znaczenie1,znaczeni2,...*
rozbijamy na wyraz obcy i jego znaczenia, które zapisujemy w liście *t*. Wszystkie elementy
oczyszczamy, tj. zamieniamy na małe litery i usuwamy białe znaki.
Funkcja ``map(oczysc, znaczenia)`` pozwala zastosować podaną jako pierwszy argument funkcję *oczysc*
do wszystkich elementów listy *znaczenia* podanej jako argument drugi.
Instrukcja ``list()`` przekształca zwrócony przez funkcję ``map()`` obiekt z powrotem na listę.

**Formatowanie napisów**

Metoda napisów ``format()`` pozwala na drukowanie przekazanych jej jako argumentów danych
zgodnie z ciągami formatującymi umieszczanymi w nawiasach klamrowych w napisie,
np. ``{0: <15}{1: <40}``. Pierwsza cyfra wskazuje, do którego argumentu metody ``format()``
odnosi się ciąg formatujący. Po dwukropku podajemy znak

, że pierwszy argument umieszczony w funkcji ``format()``, drukowany ma być wyrównany do lewej (<) w polu o szerokości 15 znaków, drugi argument, również wyrównany do lewej, w polu o szerokości 40 znaków.

`csv <https://pl.wikipedia.org/wiki/CSV_(format_pliku)>`_

Zadania dodatkowe
*****************

- Kod drukujący słownik zamień w funkcję. Wykorzystaj ją do wydrukowania słownika odczytanego z dysku i słownika uzupełnionego przez użytkownika.
- Spróbuj zmienić program tak, aby umożliwiał usuwanie wpisów.
- Dodaj do programu możliwość uczenia się zapisanych w słowniku słówek. Niech program wyświetla kolejne słowa obce i pobiera od użytkownika możliwe znaczenia. Następnie powinien wyświetlać, które z nich są poprawne.
