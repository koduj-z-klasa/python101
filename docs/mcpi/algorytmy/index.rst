.. _mcpialgorytmy:

Algorytmy
##############

W tym scenariuszu spróbujemy pokazać w Minecrafcie Pi algorytm symulujący
`ruchy Browna <https://pl.wikipedia.org/wiki/Ruchy_Browna>`_ oraz algorytm
stosujący `metodę Monte Carlo <https://pl.wikipedia.org/wiki/Metoda_Monte_Carlo>`_
do wyliczenia przybliżonej wartości liczby Pi.

Ruchy Browna
==============

Za pomocą wybranego edytora utwórz pusty plik, umieść w nim podany niżej kod i zapisz
w katalogu :file:`mcpi-sim` pod nazwą :file:`mcpi-rbrowna.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-rbrowna01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-


Większość kodu powinna być już zrozumiała. Importy bibliotek, nawiązywanie połączenia
z serwerem MC Pi, funkcje ``plac()``, ``wykres()`` i ``rysuj()`` omówione zostały w poprzednim
scenariuszu :ref:`Funkcje w mcpi <mcpi-funkcje>`.

W funkcji ``ruchyBrowna()`` na początku pobieramy od użytkownika ilość ruchów cząsteczki
do wygenerowania oraz ich długość, co ma znaczenie podczas ich odwzorowywania w świecie MC Pi.
Następnie w pętli:

* losujemy kąt wskazujący kierunek ruchu cząsteczki,
* wyliczamy współrzędne kolejnego punktu korzystając z funkcji *cos()* i *sin()* (np. ``x = x + r * np.cos(rad)``),
* zaokrąglamy wyniki do 2 miejsc po przecinku (np. ``x = int(round(x, 2))``) i drukujemy,
* na koniec dodajemy obliczone współrzędne do list odciętych i rzędnych (np. ``lx.append(x)``).

Po wyjściu z pętli obliczamy długość wektora przesunięcia, korzystając z twierdzenia Pitagorasa,
i drukujemy wynik z dokładnością do dwóch miejsc po przecinku (wyrażenie formatujące: ``{:.2f}``).

Po tych operacjach pozostaje wykreślenie ruchu cząsteczki w *matplotlib* i wyznaczenie go
w Minecrafcie.

.. figure:: img/rbrowna-matplot.png

.. tip::

    Przed uruchomieniem wizualizacji warto ustawić Steve'a w tryb lotu
    (dwukrotne naciśnięcie spacji).

(Nie)powtarzalność
==================

Kilkukrotne uruchomienie dotychczasowego kodu pokazuje, że za każdym razem generowany jest
inny tor ruchu cząsteczki. Z jednej strony to dobrze, bo to potwierdza przypadkowość symulowanych
ruchów, z drugiej strony przydatna byłaby możliwość zapamiętania wyjątkowo malowniczych
sekwencji.

Zmienimy więc funkcję ``ruchyBrowna()`` tak, aby zapisywała i ewentualnie
odczytywała wygenerowany i zapisany ruch cząsteczki. Musimy też dodać dwie funkcje narzędziowe
zapisujące i czytające dane.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-rbrowna02.py
    :linenos:
    :lineno-start: 68
    :lines: 68-129

Z powyższego kodu wynika, że jeżeli funkcja ``ruchyBrowna()`` otrzyma niepustą listę danych
(``if len(dane):``), wczyta z niej dane współrzędnych *x* i *y*. W przeciwnym wypadku
generowane będą nowe, które zostaną zapisane: ``zapisz_dane((lx, ly))``.

Funkcja ``zapisz_dane()``, pobiera tuplę zawierającą listę współrzędnych *x* i *y*,
otwiera plik o podanej nazwie do zapisu (``open('rbrowna.log', 'w')``) i zapisuje
w nim dane w formacie `json <https://pl.wikipedia.org/wiki/JSON>`_.

Funkcja ``czytaj_dane()`` prosi o podanie nazwy pliku z danymi, jeśli istnieje,
zwraca dane zapisane w formacie *json*, które w funkcji ``ruchyBrowna()``
rozpakowywane są jako listy wartości *x* i *y*: ``lx, ly = dane``.
Jeżeli podany plik z danymi nie istnieje, zwracana jest pusta lista,
a w funkcji ``ruchyBrowna()`` generowane są nowe dane.

W funkcji głównej zmieniamy wywołanie funkcji na ``ruchyBrowna(czytaj_dane())``
i testujemy zmieniony kod. Za pierwszym razem wciskamy :kbd:`Enter`, generujemy
i zapisujemy dane, za drugim razem podajemy nazwę pliku :file:`rbrowna.log`.

.. figure:: img/rbrowna0.png

Ruch cząsteczki
===============

Do tej pory ruch cząsteczki wizualizowane był jako pojedyncze punkty.
Możemy jednak pokazać pokonaną trasę liniowo, używając omawianej już
biblioteki :ref:`minecraftstaff <mcpifigury>`. Pod funkcją ``rysuj()`` umieszczamy
następującą funkcję:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-rbrowna03.py
    :linenos:
    :lineno-start: 68
    :lines: 68-103

Jak widać, jest to zmodyfikowana funkcja, której użyliśmy po raz pierwszy w scenariuszu
:ref:`Funkcje <mcpi-funkcje>`. Zmiany dotyczą dodatkowych instrukcji
typu ``mc.setBlock(x2, y2, z[0], block.GRASS)``, których zadaniem jest zaznaczenie
innymi blokami wylosowanych punktów reprezentujących ruch cząsteczki.
Instrukcja ``sleep(1)`` wstrzymując budowanie na 1 sekundę wywołuje wrażenie
animacji i pozwala śledzić na bieżąco budowany tor.
Końcowe instrukcje służą zaznaczeniu początku i końca ruchu blokami obsydianu.

**Eksperymenty**

Uruchmiamy kod i ekperymentujemy. Dla 100 ruchów z krokiem przesunięcia 5
możemy uzyskać np. takie rezultaty:

.. figure:: img/rbrowna1.png

.. figure:: img/rbrowna2.png

Nic nie stoina przeszkodzie, żeby cząsteczka "ruszała się" w pionie nad i...
pod wodą:

.. figure:: img/rbrowna3.png

.. figure:: img/rbrowna4.png
