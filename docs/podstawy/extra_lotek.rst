.. _extra-lotek:

Extra Lotek
###########

Program "Duży Lotek" omówiony w poprzednim przykładzie można podzielić na części kodu realizujące
pojedyncze zadania, np. pobranie danych wejściowych, wylosowanie liczb, pobranie typów użytkownika,
sprawdzenie i wypisanie danych wyjściowych. Realizację takich zadań możemy umieścić w funkcjach,
których będzie można używać w innych programach.

.. note::

    Przykład "Extra Lotek" pokazuje, jak używać funkcji i modułów oraz
    jak zapisywać i odczytywać dane z plików tekstowych w różnych formatach.

Zadanie
*******

Napisz program :file:`extra_lotek.py`, który losuje ``n`` liczb naturalnych
z podanego zakresu ``maks``, a następnie pobiera z klawiatury ``n`` typów, sprawdza i wypisuje,
ile z nich zostało trafionych. Pobieranie typów, sprawdzanie i wypisywanie wyników
powtarza się tyle razy, ile poda użytkownik. Dodatkowo program powinien:

* sprawdzać poprawność podawanych danych wejściowych,
* zapisywać w pliku i odczytywać dane wejściowe: nick użytkownika, liczbę losowanych liczb,
  wartość maksymalną oraz liczbę typowań,
* pozwalać na zmianę danych wejściowych.

Realizację kolejnych zadań zakoduj w funkcjach umieszczonych w module.

**Dane**:

* ``nick`` – nick użytkownika, ciąg znaków pobierany z klawiatury,
* ``n`` – liczba naturalna pobierana z klawiatury większa od ``n``,
* ``maks`` – liczba całkowita pobierana z klawiatury,
* ``ile_typowan`` – liczba całkowita pobierana z klawiatury,
* ``typ`` – liczba całkowita pobierana z klawiatury z zakresu ``<0; maks>``.

**Wynik**

Komunikaty podczas pierwszego uruchomienia:

.. code::

    Podaj nick: adam
    Podaj liczbę losowanych liczb: 3
    Podaj maksymalną losowaną liczbę: 10
    Podaj liczbę typowań: 1
    Wytypuj 3 z 10 liczb:
    Podaj typ: 1
    Podaj typ: 3
    Podaj typ: 5

    Wylosowane liczby: [10, 3, 4]
    Trafione liczby: {3}
    Liczba trafień 1

Początkowe komunikaty po kolejnym uruchomieniu przez tego samego użytkownika:

.. code::

    Podaj nick: adam
    Ustawienia:
    Liczb: 3
    Maks: 10
    Typowań: 1
    Zmieniasz (t/n)? n
    Wytypuj 3 z 10 liczb:
    ...

Funkcja główna
***************

Tam, gdzie w programie występują powtarzające się operacje lub zestaw poleceń
realizujący wyodrębnione zadanie, wskazane jest używanie funkcji.
Wyodrębnienie funkcji poprawia czytelność działania programu, ułatwia sprawdzanie i poprawianie kodu.

Jeżeli zadania realizowane przez program umieszczamy w funkcjach, to jedną z nich trzeba wywołać na początku,
aby program zaczął działać. Taka funkcja zwyczajowo nazywana jest ``main()``
i zazwyczaj zawiera logikę działania programu, tj. wywołuje inne funkcje wykonujące osobne zadania.

W nowym pliku :file:`extra_lotek.py` umieszczamy początkowy kod:

.. raw:: html

    <div class="code_no">Plik <i>extra_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python

.. code::

    def main(args):
        nick = input('Podaj nick: ')

        pass

        return 0

    if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))

Funkcja w Pythonie to wyodrębniony i nazwany blok kodu.
Definicja funkcji ``def main(args):`` zawiera słowo kluczowe ``def``,
nazwę funkcji z okrągłymi nawiasami, np. ``main()``, opcjonalne parametry, np. ``args`` oraz dwukropek.

Instrukcja warunkowa ``if __name__ == '__main__':`` sprawdza, czy nasz plik został uruchomiony
bezpośrednio przez interpreter, który zmienną specjalną ``__name__`` ustawia wtedy na ``__main__``.
Jeżeli plik zostałby zaimportowany, zmienna ``__name__`` ustawiona zostałaby na nazwę pliku.

Jeżeli plik wykonywany jest bezpośrednio, uruchamiana jest funkcja główna ``main(args)`` jako argument metody
``sys.exit()``, która kończy wykonywanie programu. Wartość zwracana przez funkcję główną informuje
o tym, jak zakończył się program, np. zero (``0``) oznacza, że program zakończył się poprawnie.

.. note::

    W prostych programach pisanych na własny użytek można zrezygnować z bloku ``if __name__ == '__main__':``,
    a także usunąć argument ``args`` z definicji funkcji głównej. Trzeba jednak pamiętać o wywołaniu
    funkcji głównej, tj. umieszczeniu instrukcji ``main()`` bez wcięcia po definicji funkcji głównej.

    Instrukcja ``pass`` nie jest wykonywana, to informacja, że w danym miejscu zostanie wstawiony jakiś kod.
    Pozwala również uniknąć błędu w miejscach, w których brak kodu jest niedozwolony, np.
    po instrukcji warunkowej lub pętli.

Moduł
******

Często używane funkcje umieszczamy w osobnych modułach (zob. :term:`moduł`), z których
importujemy je do różnych programów za pomocą instrukcji ``import`` lub ``from ... import``.

.. note::

    Jeżeli program korzysta z niewielu i/lub unikalnych funkcji,
    możemy umieścić je na początku programu w jednym pliku.

Wczytywanie ustawień
--------------------

W katalogu ze skryptem naszego programu tworzymy nowy plik ``modul_lotek.py``,
dodajemy importy modułów wbudowanych oraz funkcji wczytującej zapisanie ustawienia:

.. raw:: html

    <div class="code_no">Plik <i>modul_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: modul_lotek.py
    :linenos:
    :lineno-start: 1
    :lines: 1-14

Funkcja ``wczytaj_ustawienia()`` otrzymuje parametr ``nick``, który wykorzystujemy do zdefiniowania nazwy pliku
z ustawieniami użytkownika. Za pomocą metody ``isfile()`` sprawdzamy, czy plik znajduje się
w ścieżce przeszukiwania, czyli w praktyce w katalogu naszego programu głównego. Jeżeli tak, otwieramy go
w domyślnym trybie "do odczytu" – ``with open(nazwa_pliku) as plik:`` – i udostępniamy w zmiennej ``plik``.

Plik zawiera jeden wiersz w formacie ``nick;liczba losowanych liczb;maksymalna liczba;liczba typowań``.
Do jego odczytania używamy metody ``readline()``. Z otrzymanego ciągu znaków usuwamy znaki końca wiersza
przy użyciu metody ``strip()``. Następnie dzielimy tekst za pomocą metody ``split()`` i znaku średnika na części,
które zwracane są w postaci listy ``dane``.

Pobieranie ustawień
--------------------

Do naszego modułu dodajemy kolejną funkcję o nazwie ``pobierz_ustawienia()``, której zadaniem
będzie pobieranie danych wejściowych z klawiatury:

.. raw:: html

    <div class="code_no">Plik <i>modul_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: modul_lotek.py
    :linenos:
    :lineno-start: 16
    :lines: 16-36

Funkcja ``pobierz_ustawienia()`` wykorzystuje nieskończoną pętlę warunkową ``while True``,
w której pobierane są kolejne dane wejściowe. W przypadku podania błędnych danych pętla zaczyna działanie od początku
dzięki instrukcji ``continue``, jeżeli dane są poprawne przerywamy działanie pętli instrukcją
``break`` i zwracamy je w postaci listy ``dane``.

.. note::

    Wyjaśnienie instrukcji ``try ... except`` znajdziesz w materiale :ref:`Duży lotek <duzy-lotek>`
    w sekcji "Poprawność danych".

Zapisywanie ustawień
--------------------

Dodajemy do modułu funkcję ``zapisz_ustawienia()``, która pobierać będzie dwa parametry
zawierające nick użytkownika i dane do zapisania.

.. raw:: html

    <div class="code_no">Plik <i>modul_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: modul_lotek.py
    :linenos:
    :lineno-start: 38
    :lines: 38-42

Początek funkcji jest prawie identyczny jak w funkcji ``wczytaj_ustawienia()`` z tą tylko różnicą,
że plik otwierany jest w trybie do zapisu, tj, podajemy drugi argument w funkcji ``open()`` – znak ``w``.
W efekcie, jeżeli pliku nie ma na dysku – zostanie zapisany, jeżeli jest – zostanie nadpisany.
Parametr ``dane`` jest 4-elementową listą zawierająca pobrane od użytkownika lub odczytane z dysku
dane wejściowe. Dane te łączymy za pomocą metody ``join()`` i znaku średnika. Otrzymany ciąg znaków
uzupełniamy znakiem końca wiersza ``\n`` i zapisujemy w pliku za pomocą metody ``.write()``.

Dane wejściowe
**************

Wykorzystajmy przygotowane funkcje w programie głównym. Na początku pliku :file:`extra_lotek.py`
importujemy dodane funkcje:

.. raw:: html

    <div class="code_no">Plik <i>extra_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: extra_lotek.py
    :linenos:
    :lineno-start: 1
    :lines: 1

Następnie instrukcję ``pass`` zastępujemy poniższym kodem:

.. raw:: html

    <div class="code_no">Plik <i>extra_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: extra_lotek.py
    :linenos:
    :lineno-start: 7
    :lines: 9-20

Po pobraniu nicka z klawiatury wywołujemy funkcję ``wczytaj_ustawienia()``, która zwróci listę
z odczytanymi danymi lub wartość ``False``. W instrukcji warunkowej, jeżeli lista nie jest pusta
(``if dane:``), wypisujemy dane oprócz nicka.

Jeżeli nie udało się odczytać danych (``if not dane``) lub jeżeli użytkownik chce zmienić odczytane dane
(``or input('Zmieniasz (t/n)? ').lower() == 't'``), wywołujemy funkcję ``pobierz_dane()``, a następnie
funkcję ``zapisz_ustawienia()``, która zapisuje listę ``dane`` zawierającą nick i pozostałe informacje.

W kolejnej instrukcji przypisujemy elementy listy ``dane`` do osobnych zmiennych.
Do wskazania poszczególnych elementów listy używamy notacji wycinkowej.
Instrukcja ``[int(x) for x in dane[1:4]]`` to :term:`wyrażenie listowe`. Można je rozumieć
jako skrócony zapis pętli ``for``, która odczytuje trzy ostatnie elementy listy ``dane[1:4]``,
zamienia je na liczby całkowite ``int(x)`` i tworzy nową listę. Jej elementy to liczby
przypisywane do zmiennych ``m, maks`` i ``ile_typowan``.

Losowanie i sprawdzanie
***********************

Funkcje, które losują liczby do odgadnięcia, pobierają typy użytkownika, sprawdzają i wypisują wyniki
umieszczamy w module :file:`modul_lotek.py`:

.. raw:: html

    <div class="code_no">Plik <i>modul_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: modul_lotek.py
    :linenos:
    :lineno-start: 44
    :lines: 44-84

Dodane instrukcje to kod omówiony w scenariuszu :ref:`Duży lotek <duzy-lotek>` przekształcony
na funkcje. Warto zwrócić uwagę, że zwracają one wartości, tj. listę wylosowanych liczb ``liczby``,
zbiór typów użytkownika ``typy`` oraz liczbę trafień ``len(trafione)``.

Następnie w programie głównym uzupełniamy importy na początku pliku:

.. raw:: html

    <div class="code_no">Plik <i>extra_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: extra_lotek.py
    :linenos:
    :lineno-start: 1
    :lines: 1-2
    :emphasize-lines: 2

Następnie dopisujemy kod w funkcji głównej przed instrukcją ``return 0``:

.. raw:: html

    <div class="code_no">Plik <i>extra_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: extra_lotek.py
    :linenos:
    :lineno-start: 21
    :lines: 21-30

Po wylosowaniu liczb wykorzystujemy pętlę ``for i in range(ile_typowan)``, aby użytkownik mógł kilka razy typować liczby.
Wewnątrz pętli pobieramy typy, sprawdzamy i wypisujemy wyniki. Jeżeli liczba odgadniętych liczb,
czyli wartość zwrócona przez funkcję ``wypisz_wyniki()`` równa jest liczbie losowanych liczb, kończymy
pętlę instrukcją ``break``.

Historia typowań
*******************

Skoro umiemy już zapamiętywać wstępne ustawienia programu, możemy również
zapamiętywać losowania i typowania użytkownika, tworząc rejestr do celów informacyjnych
i/lub statystycznych. Przyjmijmy, że będziemy zapisywali dane ostatniego typowania
i będą one zawierały:

* ``czas`` – data typowania,
* ``n`` – liczba losowanych liczb,
* ``maks`` – maksymalna losowana liczba,
* ``ile_typowan`` – liczba typowań,
* ``ustawienia`` – krotka z liczbą losowanych liczb, liczbą maksymalną i liczbą typowań,
* ``wylosowane`` – krotka z wylosowanymi liczbami,
* ``ile_trafionych`` – liczba trafionych liczb.

Do przechowywania tych informacji wykorzystamy słownik, w którym kluczami będą nazwy danych.

Zaczniemy od dodania dwóch funkcji w pliku modułu:

.. raw:: html

    <div class="code_no">Plik <i>modul_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: modul_lotek.py
    :linenos:
    :lineno-start: 86
    :lines: 86-100

Kiedy czytamy i zapisujemy dane w plikach, ważną sprawą staje się ich format. Najprościej
zapisywać dane jako znaki, tak jak zrobiliśmy to z ustawieniami, jednak często
programy użytkowe potrzebują zapisywać złożone struktury danych, np.
listy, zbiory czy słowniki. Znakowy zapis wymagałby wtedy wielu dodatkowych
manipulacji, aby możliwe było poprawne odtworzenie informacji. Prościej
jest skorzystać z *serializacji*, czyli zapisu danych obiektowych (zob. :term:`serializacja`).
Często stosowany jest wtedy prosty format tekstowy `JSON <https://pl.wikipedia.org/wiki/JSON>`_.

W funkcji ``wczytaj_dane()`` zawartość pliku o podanej nazwie dekoduje do listy: ``dane = json.load(plik)``,
która jest zwracana. Funkcja ``zapisz_dane()`` otwiera plik o podanej nazwie w trybie do zapisu
i zapisuje podaną listę danych w formacie JSON: ``json.dump(dane, plik)``. Ewentualne dane znajdujące się
w pliku są nadpisywane.

Pozostaje nam wykorzystać przygotowane funkcje w programie głównym. Na początku dodajemy importy:

.. raw:: html

    <div class="code_no">Plik <i>extra_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: extra_lotek.py
    :linenos:
    :lineno-start: 1
    :lines: 1-3
    :emphasize-lines: 3

Dalej na końcu funkcji ``main()``, ale przed instrukcją ``return 0`` dopisujemy:

.. raw:: html

    <div class="code_no">Plik <i>extra_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: extra_lotek.py
    :linenos:
    :lineno-start: 31
    :lines: 31-42

Do zmiennej ``losowania`` przypisujemy listę zwróconą przez funkcję ``wczytaj_dane()``.
Następnie tworzymy słownik ``losowanie``, zawierający wszystkie omówione wyżej dane aktualnej "gry".
Na uwagę zasługuje obsługa daty i czasu przy użyciu metod z podmodułu ``datetime``:

* ``now()`` – metoda zwraca obiekt reprezentujący aktualną datę i czas,
* ``strftime()`` – metoda pozwala przekształcić obiekt w ciąg znaków według ciągu formatującego
  ``%d.%m.%Y %H:%M:%S``, który oznacza zapis w postaci ``dzień.miesiąc.rok godzina:minuta:sekunda``,
  np.: ``21.10.2025 16:07:23``.

.. note::

    Serializacja JSON nie obsługuje obiektów typu ``datetime``, dlatego trzeba je zamieniać
    na ciąg znaków. Alternatywnie do pokazanego wyżej sposobu można użyć metody zwracającej
    datę w formacie ISO 8601, np. ``datetime.now().isoformat()``.

Przygotowany słownik dodajemy do listy słowników: ``losowania.append(losowanie)``,
którą wypisujemy w celach poglądowych ;-) i zapisujemy za pomocą funkcji ``zapisz_dane()``.

Ćwiczenia
*********

1) Przećwicz w trybie interaktywnym notację wycinkową, wyrażenia listowe i łączenie list:

.. code-block:: bash

    ~$ python3
    >>> dane = ['a', 'b', 'c', '1', '2', '3']
    >>> dane[0:3]
    >>> dane[3:6]
    >>> duze = [x.upper() for x in dane[0:3]]
    >>> kwadraty = [int(x)**2 for x in dane[3:6]]
    >>> duze + kwadraty

2) Sprawdź w trybie interaktywnym, jak wygląda znakowa reprezentacja aktualnej daty i czasu
   w formacie ISO 8601.

3) Załóżmy, że jednak chcielibyśmy zapisywać historię losowań w pliku tekstowym,
   którego poszczególne linie zawierałyby dane jednego losowania, np.:

   ``czas:2025-10-28T15:31:27.047438;n:2;maks:10;ile_typowan:2;wylosowane:(5, 7);trafionych:2``

   Funkcja zapisująca dane mogłaby wyglądać np. tak:

   .. raw:: html

      <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

   .. code:: python

       def zapisz_txt(nick, dane):
           """Funkcja zapisuje dane w formacie txt do pliku"""
           nazwa_pliku = nick + "_losowania.txt"
           with open(nazwapliku, "w") as plik:
               for slownik in dane:
                   wiersz = [k + ":" + str(w) for k, w in slownik.iteritems()]
                   wiersz = ";".join(wiersz)
                   print >>plik, wiersz + '\n'


   Napisz funkcję ``czytaj_txt()`` odczytującą tak zapisane dane, która zwraca listę słowników.

   Użyj obydwu funkcji w programie ``extra_lotek.py`` tak, aby wypisywane były dane zwracane
   przez funkcję ``zapisz_txt()``.

    .. tip::

        Nie musisz zastępować funkcji zapisujących dane w formacie JSON.

.. admonition:: Pojęcia

    :term:`funkcja`, :term:`moduł`, :term:`notacja wycinkowa`, :term:`serializacja`
