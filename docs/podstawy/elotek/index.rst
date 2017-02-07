.. _toto-lotek:

Extra Lotek
###########

Kod Toto Lotka wypracowany w dwóch poprzednich częściach wprowadził podstawy programowania
w Pythonie: podstawowe typy danych (napisy, liczby, listy, zbiory), instrukcje sterujące (warunkową
i pętlę) oraz operacje wejścia-wyjścia w konsoli. Uzyskany skrypt wygląda następująco:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: toto29.py


Funkcje i moduły
*****************

Tam, gdzie w programie występują powtarzające się operacje lub zestaw poleceń
realizujący wyodrębnione zadanie, wskazane jest używanie funkcji.
Są to nazwane bloki kodu, które można grupować w ramach modułów (zob. :term:`funkcja`, :term:`moduł`).
Funkcje zawarte w modułach można importować do różnych programów.
Do tej pory korzystaliśmy np. z funkcji ``randit()`` zawartej w module ``random``.

Wyodrębnienie funkcji ułatwia sprawdzanie i poprawianie kodu, ponieważ
wymusza podział programu na logicznie uporządkowane kroki. Jeżeli
program korzysta z niewielu funkcji, można umieszczać je na początku pliku
programu głównego.

Tworzymy więc nowy plik :file:`totomodul.py` i umieszczamy w nim następujący kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: totomodul30.py
    :linenos:
    :emphasize-lines: 7, 10, 18, 24, 33, 36, 51


Funkcja w Pythonie składa się ze słowa kluczowego ``def``, nazwy, obowiązkowych nawiasów
okrągłych i opcjonalnych parametrów. Funkcje zazwyczaj zwracają jakieś dane
za pomocą instrukcji ``return``.

Warto zauważyć, że można zwracać więcej niż jedną wartość naraz,
np. w postaci tupli ``return (ile, maks, ilelos)``. **Tupla** to rodzaj listy,
w której nie możemy zmieniać wartości (zob. :term:`tupla`). Jest często stosowana
do przechowywania i przekazywania stałych danych.

Nazwy zmiennych lokalnych w funkcjach są niezależne od nazw zmiennych w programie
głównym, ponieważ definiowane są w różnych zasięgach, a więc w różnych przestrzeniach nazw.
Możliwe jest modyfikowanie zmiennych globalnych dostępnych w całym programie,
o ile wskażemy je instrukcją typu: ``global nazwa_zmiennej``.

Program główny po zmianach przedstawia się następująco:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: toto30.py
    :linenos:
    :emphasize-lines: 4, 7, 9, 12, 30-32

Na początku z modułu ``totomodul``, którego nazwa jest taka sama jak nazwa pliku,
importujemy potrzebne funkcje. Następnie w funkcji głównej ``main()``
wywołujemy je podając nazwę i ewentualne argumenty.
Zwracane przez nie wartości zostają przypisane podanym zmiennym.

Wiele wartości zwracanych w tupli można jednocześnie przypisać
kilku zmiennym dzięki operacji tzw. rozpakowania tupli:
``ileliczb, maksliczba, ilerazy = ustawienia()``. Należy jednak
pamiętać, aby ilość zmiennych z lewej strony wyrażenia odpowiadała ilości
elementów w tupli.

Konstrukcja ``while True`` oznacza nieskończoną pętlę. Stosujemy ją w funkcji
``ustawienia()``, aby wymusić na użytkowniku podanie poprawnych danych.

Funkcja główna ``main()`` zostaje wywołana, o ile warunek ``if __name__ == '__main__':`` jest prawdziwy.
Jest on prawdziwy wtedy, kiedy nasz skrypt zostanie uruchomiony
jako główny, wtedy nazwa specjalna ``__name__`` ustawiana jest na ``__main__``.
Jeżeli korzystamy ze skryptu jako modułu, importując go, ``__main__`` ustawiane jest na nazwę pliku.

.. note::

    W rozbudowanych programach dobrą praktyką ułatwiającą późniejsze przeglądanie
    i poprawianie kodu jest opatrywanie jego fragmentów **komentarzami**. Można je
    umieszczać po znaku ``#``. Z kolei funkcje opatruje się krótkim opisem
    działania i/lub wymaganych argumentów, ograniczanym **potrójnymi cudzysłowami**.
    Notacja ``"""..."""`` lub ``'''...'''`` pozwala zamieszczać teksty wielowierszowe.


Ćwiczenie
==========

* Przenieś kod powtarzany w pętli ``for`` (linie 17-24) do funkcji zapisanej w module
  programu i nazwanej np. ``wyniki()``. Zdefiniuj listę argumentów, zadbaj,
  aby funkcja zwracała ilość trafionych liczb. Wywołanie funkcji:
  ``iletraf = wyniki(set(liczby), typy)`` umieść w linii 17.

* Przy okazji popraw wyświetlanie listy trafionych liczb. Przed instrukcją
  ``print "Trafione liczby: %s" % trafione`` wstaw linię:
  ``trafione = ", ".join(map(str, trafione))``.

  Funkcja ``map()`` (zob. :ref:`mapowanie funkcji <map-fun>`) pozwala na zastosowanie
  jakiejś innej funkcji, w tym wypadku ``str`` (czyli konwersji na napis),
  do każdego elementu sekwencji, w tym wypadku zbioru ``trafione``.

  Metoda napisów ``join()`` pozwala połączyć elementy listy (muszą być typu *string*)
  podanymi znakami, np. przecinkami (``", "``).


Zapis/odczyt plików
*******************

Uruchamiając wielokrotnie program, musimy podawać wiele danych, aby zadziałał.
Dodamy więc możliwość zapamiętywania ustawień i ich zmiany. Dane zapisywać
będziemy w zwykłym pliku tekstowym. W pliku :file:`toto2.py` dodajemy
tylko jedną zmienną ``nick``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: toto32.py
    :linenos:
    :emphasize-lines: 2
    :lineno-start: 8
    :lines: 8-9

W pliku :file:`totomodul.py` zmieniamy funkcję ``ustawienia()`` oraz dodajemy
dwie nowe: ``czytaj_ust()`` i ``zapisz_ust()``.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: totomodul32.py
    :linenos:
    :emphasize-lines: 14, 23, 36-37, 42, 51
    :lineno-start: 1
    :lines: 1-55

W funkcji ``ustawienia()`` pobieramy nick użytkownika i tworzymy nazwę pliku
z ustawieniami, następnie próbujemy je odczytać wywołując funkcję ``czytaj_ust()``.
Funkcja ta sprawdza, czy podany plik istnieje na dysku i otwiera go do odczytu:
``plik = open(nazwapliku, "r")``. Plik powinien zawierać 1 linię, która przechowuje
ustawienia w formacie: ``nick;ile_liczb;maks_liczba;ile_prób``. Po jej
odczytaniu za pomocą metody ``.readline()`` i rozbiciu na elementy
zwracamy ją jako listę ``gracz``.

Jeżeli uda się odczytać zapisane ustawienia, drukujemy je, a następnie
pytamy, czy użytkownik chce je zmienić. Jeżeli nie znaleźliśmy zapisanych
ustawień lub użytkownik nacisnął klawisz "t" lub "T", wykonujemy poprzedni
kod. Na koniec zmiennej ``gracz`` przypisujemy listę ustawień przekazaną
do zapisu funkcji ``zapisz_ust()``. Funkcja ta zapisuje dane złączone za
pomocą średnika w jedną linię do pliku: ``plik.write(";".join(gracz))``.

W powyższym kodzie widać, jakie operacje można wykonywać na tekstach, tj.:

* operator ``+``: łączenie tekstów,
* ``linia.split(";")`` – rozbijanie tekstu wg podanego znaku na elementy listy,
* ``";".join(gracz)`` – wspomniane już złączanie elementów listy za pomocą podanego znaku,
* ``odp.lower()`` – zmiana wszystkich znaków na małe litery,
* ``str(arg)`` – przekształcanie podanego argumentu na typ tekstowy.

Zwróćmy uwagę na konstrukcję ``return gracz[0:1] + map(int, gracz[1:4])``,
której używamy, aby zwrócić odczytane/zapisane ustawienia do programu głównego.
Dane w pliku przechowujemy, a także pobieramy od użytkownika jako znaki.
Natomiast program główny oczekuje 4 wartości typu: znak, liczba, liczba, liczba.
Stosujemy więc **notację wycinkową** (ang. *slice*), aby wydobyć nick użytkownika:
``gracz[0:1]``. Pierwsza wartość mówi od którego elementu, a druga do którego
elementu wycinamy wartości z listy (przećwicz w konsoli Pythona!).
Wspominana już funkcja ``map()`` pozwala zastosować
do pozostałych 3 elementów (``gracz[1:4]``) funkcję ``int()``,
która zamienia je w wartości liczbowe.


Słowniki
******************

Skoro umiemy już zapamiętywać wstępne ustawienia programu, możemy również
zapamiętywać losowania użytkownika, tworząc rejestr do celów informacyjnych
i/lub statystycznych. Zadanie wymaga po pierwsze zdefiniowania jakieś struktury,
w której będziemy przechowywali dane, po drugie zapisu danych albo w plikach,
albo w bazie danych.

Na początku dopiszemy kod w programie głównym :file:`toto2.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: toto33.py
    :linenos:
    :emphasize-lines: 4-6, 19-31
    :lineno-start: 1
    :lines: 1-

Dane graczy zapisywać będziemy w plikach nazwanych nickiem użytkownika
z rozszerzeniem ".json": ``nazwapliku = nick + ".json"``.
Informacje o grach umieścimy w liście ``losowania``, którą na początku
zainicjujemy danymi o grach zapisanymi wcześniej: ``losowania = czytaj(nazwapliku)``.

Każda gra w liście ``losowania`` to :term:`słownik`. Struktura ta pozwala
przechowywać dane w parach "klucz: wartość", przy czym indeksami mogą być napisy:

* ``"czas"`` – będzie indeksem daty gry (potrzebny import modułu ``time``!),
* ``"dane"`` – będzie wskazywał tuplę z ustawieniami,
* ``"wylosowane"`` – listę wylosowanych liczb,
* ``"ile"`` – ilość trafień.

Na koniec dane ostatniej gry dopiszemy do listy (``losowania.append()``),
a całą listę zapiszemy do pliku: ``zapisz(nazwapliku, losowania)``.

Teraz zobaczmy, jak wyglądają funkcje ``czytaj_json()`` i ``zapisz_json()`` w module
:file:`totomodul.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: totomodul33.py
    :linenos:
    :lineno-start: 103
    :lines: 103-

Kiedy czytamy i zapisujemy dane, ważną sprawą staje się ich format. Najprościej
zapisywać dane jako znaki, tak jak zrobiliśmy to z ustawieniami, jednak często
programy użytkowe potrzebują zapisywać złożone struktury danych, np.
listy, zbiory czy słowniki. Znakowy zapis wymagałby wtedy wielu dodatkowych
manipulacji, aby możliwe było poprawne odtworzenie informacji. Prościej
jest skorzystać z *serializacji*, czyli zapisu danych obiektowych (zob. :term:`serializacja`).
Często stosowany jest prosty format tekstowy `JSON <https://pl.wikipedia.org/wiki/JSON>`_.

W funkcji ``czytaj()`` zawartość podanego pliki dekodujemy do listy: ``dane = json.load(plik)``.
Funkcja ``zapisz()`` oprócz nazwy pliku wymaga listy danych. Po otwarciu
pliku w trybie zapisu ``"w"``, co powoduje wyczyszczenie jego zawartości,
dane są serializowane i zapisywane formacie JSON: ``json.dump(dane, plik)``.

Dobrą praktyką jest zwalnianie uchwytu do otwartego pliku i przydzielonych mu zasobów
poprzez jego zamknięcie: ``plik.close()``. Tak robiliśmy w funkcjach
czytających i zapisujących ustawienia. Teraz jednak pliki otworzyliśmy przy
użyciu konstrukcji typu ``with open(nazwapliku, "r") as plik:``, która zadba
o ich właściwe zamknięcie.

Przetestuj, przynajmniej kilkukrotnie, działanie programu.

Ćwiczenie
==============

Załóżmy, że jednak chcielibyśmy zapisywać historię losowań w pliku tekstowym,
którego poszczególne linie zawierałyby dane jednego losowania, np.:
``wylosowane:[4, 5, 7];dane:(3, 10);ile:0;czas:1434482711.67``

Funkcja zapisująca dane mogłaby wyglądać np. tak:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    def zapisz_str(nazwapliku, dane):
        """Funkcja zapisuje dane w formacie txt do pliku"""
        with open(nazwapliku, "w") as plik:
            for slownik in dane:
                linia = [k + ":" + str(w) for k, w in slownik.iteritems()]
                linia = ";".join(linia)
                # plik.write(linia+"\n") – zamiast tak, można:
                print >>plik, linia

Napisz funkcję ``czytaj_str()`` odczytującą tak zapisane dane. Funkcja
powinna zwrócić listę słowników.

Materiały
**********

**Źródła:**

* :download:`Extra Lotek <elotek.zip>`