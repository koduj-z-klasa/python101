.. _mcpi-glife:

Gra w życie
##############

`Gra w życie <https://pl.wikipedia.org/wiki/Gra_w_%C5%BCycie>`_  jest najbardziej znaną implementacją
`automatu komórkowego <https://pl.wikipedia.org/wiki/Automat_kom%C3%B3rkowy>`_,
wymyśloną przez brytyjskiego matematyka Johna Conwaya. Cały pomysł polega na symulowaniu
rozwoju populacji komórek, które umieszczone w wyznaczonym obszarze tworzą różne
zaskakujące układy.

Grę zaimplementujemy przy użyciu programowania obiektowego, którego podstawowym
elementem są `klasy <https://pl.wikipedia.org/wiki/Klasa_%28programowanie_obiektowe%29>`_.
Można je rozumieć jako definicje
`obiektów <https://pl.wikipedia.org/wiki/Obiekt_%28programowanie_obiektowe%29>`_
odwzorowujących mniej lub bardziej dokładniej jakieś elementy rzeczywistości,
niekoniecznie materialne. Obiekty łączą dane, czy też właściwości,
oraz metody na nich operujące. Obiekt tworzymy na podstawie klas i nazywamy
je wtedy instancjami danej klasy.

Plansza gry
===========

Zaczniemy od przygotowania obszaru, w którym będziemy obserwować kolejne populacje
komórek. Tworzymy pusty plik w katalogu :file:`mcpi-sim` i zapisujemy pod nazwą :file:`mcpi-glife.py`.
Wstawiamy do niego poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-glife01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-

Główna klasa w programie nazywa się ``GraWZycie``, jej definicja rozpoczyna się słowem
kluczowym ``class``, a nazwa obowiązkową dużą literą. Pierwsza zdefiniowana metoda o nazwie ``__init__()``
to konstruktor klasy, wywoływany w momencie tworzenia jej instancji.
Dzieje się tak w głównej funkcji ``main()`` w instrukcji: ``gra = GraWZycie(mc, 20, 10, 40)``.
Tworząc instancję klasy, czyli obiekt ``gra``, przekazujemy do konstruktora
parametry: obiekt ``mc`` reprezentujący grę Minecraft, szerokość
i wysokość pola gry, a także ilość tworzonych na wstępie komórek.

Konstruktor z przekazanych parametrów tworzy właściwości klasy w instrukcjach
typu ``self.mc = mc``. Odwołujemy się do nich w innych metodach za pomocą
słowa ``self``, tak jak np. w wywołanej w funkcji głównej metodzie ``uruchom()``.
Jej zadaniem jest wykonanie kolejnej metody klasy – ``plac()``,
której przekazujemy współrzędne punktu początkowego, a także szerokość i wysokość
planszy gry.

.. note::

    Warto zauważyć i zapamiętać, że każda metoda w klasie jako pierwszy
    parametr przyjmuje zawsze wskaźnik do instancji obiektu, na którym
    będzie działać, czyli konwencjonalne słowo ``self``.

W wyniku uruchomienia i przetestowania kodu powinniśmy zobaczyć zbudowaną
planszę do gry, czyli prostokąt, o podanych w funkcji głównej wymiarach.

Populacja
=========

Utworzymy klasę ``Populacja``, a w niej strukturę danych reprezentującą
układ żywych i martwych komórek. Przed funkcją główną ``main()`` wstawiamy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-glife02.py
    :linenos:
    :lineno-start: 58
    :lines: 58-97

Konstruktor klasy ``Populacja`` pobiera obiekt Minecrafta (``mc``) oraz rozmiary
dwuwymiarowej macierzy (``ilex, iley``), czyli tablicy, która reprezentować będzie układy
komórek. Po przypisaniu wałsciwościom klasy przekazanych parametrów tworzymy
początkowy stan populacji, tj. macierz wypełnioną zerami. W metodzie ``reset_generacja()``
wykorzystujemy wyrażenie listowe, które – ujmując rzecz w terminologii Pythona –
zwraca listę *ilex* list zawierających *iley* komórek z wartościami zero.
To właśnie wspomniana wcześniej macierz dwuwymiarowa.

Komórki mogą być martwe (``DEAD``– wartość 0) i tak jest na początku, ale aby populacja mogła ewoluować,
trzeba niektóre z nich ożywić (``ALIVE`` – wartość 1).
Odpowiada za to metoda ``losuj()``, która przyjmuje jeden argument
określający, ile komórek ma być początkowo żywych. Następnie w pętli losowana
jest wymagana ilość par indeksów wskazujących wiersz i kolumnę, czyli komórkę,
która ma być żywa (``ALIVE``). Na końcu drukujemy w terminalu
początkowy układ komórek.

W konstruktorze klasy głównej tworzymy instancję klasy ``Populacja`` – to powoduje
wykonanie jej konstruktora. Potem wywołujemy metodę tworzącą układ początkowy.
Tak więc na końcu konstruktora klasy ``GraWZycie`` dodajemy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-glife02.py
    :linenos:
    :lineno-start: 32
    :lines: 32-34

Przetestuj kod.

Rysowanie macierzy
==================

Skoro mamy przygotowany plac gry oraz początkowy układ populacji, trzeba ją
narysować, czyli umieścić określone bloki we współrzędnych Minecrafta odpowiadającyh
indeksom ożywionych komórek macierzy. Na końcu klasy ``Populacja`` dodajemy dwie nowe
metody:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-glife03.py
    :linenos:
    :lineno-start: 100
    :lines: 100-117

– a rysowanie wywołujemy w metodzie ``uruchom()`` klasy głównej, dopisując:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-glife03.py
    :linenos:
    :lineno-start: 41
    :lines: 41

Wyjaśnienia wymaga funkcja ``rysuj()``. W pętli pobieramy współrzędne
żywych komórek, które rozpakowywane są z 2-elementowej listy do zmiennych:
``for x, z in self.zywe_komorki():``. Dalej losujemy podtyp bloku bawełny
i umiszczamy go we wskazanym mmiejscu.

Funkcja ``zywe_komorki()`` to tzw. :term:`generator`, co poznajemy po tym,
że zwraca wartości za pomocą słowa kluczowego ``yield``. Jej
działanie polega na przeglądaniu macierzy za pomocą zagnieżdżonych pętli
i zwracaniu współrzędnych "żywych"komórek.

Różnica pomiędzy generatorem a zwykłą funkcją polega na tym, że zwykła funkcja
po przeglądnięciu całej macierzy zwróciłaby od razu kompletną listę żywych
komórek, a `generator <https://wiki.python.org/moin/Generators>`_
robi to "na żądanie". Po napotkaniu żywej komórki
zwraca jej współrzędne, zapamiętuje stan lokalnych pętli i czeka na następne
wywołanie. Dzięki temu oszczędzamy pamięć, a dla dużych struktur także
zwiększamy wydajność.

Uruchom kod, oprócz pola gry, powinieneś zobaczyć bloki reprezentujące pierwszą
generację komórek.

Ewolucja – zasady gry
=====================

Jak można było zauważyć, rozgrywka toczy się na placu podzielonym na kwadratowe komórki,
którego reprezentacją algorytmiczną jest macierz. Każda komórka ma maksymalnie
ośmiu sąsiadów. To czy komórka przetrwa, zależy od ich ilości.
Reguły są następujące:

* Martwa komórka, która ma dokładnie 3 sąsiadów, staje się żywa w następnej generacji.
* Żywa komórka z 2 lub 3 sąsiadami zachowuje swój stan, w innym przypadku umiera
  z powodu "samotości" lub "zatłoczenia".

Kolejne generacje obliczamy w umownych jednostkach czasu.
Do kodu klasy ``Populacja`` dodajemy dwie metody zawierające logikę gry:

.. highlight:: python
.. literalinclude:: mcpi-glife04.py
    :linenos:
    :lineno-start: 125
    :lines: 125-180

[todo]
