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
układ żywych i martwych komórek.