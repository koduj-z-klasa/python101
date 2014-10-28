Gra w Ponga (str)
=================

.. highlight:: python

Klasyczna gra w odbijanie piłeczki zrealizowana z użyciem biblioteki `PyGame`_. Wersja strukturalna.
Biblioteka PyGame ułatwia tworzenie aplikacji multimedialnych, w tym gier.

.. _PyGame: http://www.pygame.org/wiki/tutorials

Zmienne i plansza gry
---------------------

Tworzymy plik ``pong_str.py`` w terminalu lub w wybranym edytorze, zapisujemy na dysku i zaczynamy od zdefiniowania zmiennych określających właściwości obiektów w naszej grze.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str1.py
    :linenos:

W instrukcji ``pygame.display.set_mode()`` inicjalizujemy okno (powierzchnię główną) o rozmiarach 800x400 pikseli i 32 bitowej głębi kolorów. Tworzy w ten sposób powierzchnię do rysowania zapisaną w zmiennej OKNOGRY. Definujemy również kolory w formacie RGB (Red, Green, Blue) podając składowe poszczegónych kanałów w tuplach, np. (0, 0, 255).

Obiekty graficzne
---------------------

W dalszej kolejności zamiemy się określeniem właściwości i inicjalizacją paletek i piłki.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str2.py
    :linenos:
    :lineno-start: 34
    :lines: 34-

Schemat dodawania obiektów jest prosty. Po określeniu wymiarów obiektu (szerokości i wysokości), tworzymy powierzchnię (``pygame.Surface``), którą wypełniamy odpowiednim kolorem (``.fill()``). W przypadku piłki do metody ``Surface()`` przekazujemy dodatkowe argumenty (``pygame.SRCALPHA``) umożliwiające uzyskanie powierzchni z przezroczystymi pikselami (z kanałem alpha), na której rysujemy koło (``pygame.draw.ellipse()``) o podanym kolorze, środku i rozmiarach. W kolejnym kroku pobieramy powierzchnię prostokąta zajmowanego przez obiekt (``.get_rect()``), za pomocą której łatwiej ustawić wstępne położenie obiektu, a później nim manipulować (właściwości ``.x`` i ``.y``).

Wyświetlanie tekstu
---------------------

W grze chcemy wyświetlać punkty zdobywane przez graczy. Dopisujemy więc poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str3.py
    :linenos:
    :lineno-start: 72
    :lines: 72-

Po zdefiniowaniu zmiennych przechowujących punkty graczy, tworzymy obiekt czcionki z podanego pliku (``pygame.font.Font()``)[1]_. Następnie definujemy funkcje, których zadaniem jest rysowanie punktacji graczy. Na początku tworzą one nową powierzchnię z punktacją gracza (``.render()``), pobierają jej powierzchnię prostokątną (``.get_rect()``), pozycjonują ją (``.center()``) i rysują na głównej powierzchni gry (``.blit()``).

.. [1] Plik wykorzystywany do wyświetlania tekstu (``freesansbold.ttf``) musi znaleźć się w katalogu ze skryptem.

Główna pętla programu
---------------------

Programy interaktywne, w tym gry, reagujące na działania użytkownika, takie jak ruchy czy kliknięcia myszą, działają w pętli, której zadaniem jest:

* przechwycenie i obsługa działań użytkownika, czyli tzw. zdarzeń (ruchy, kliknięcia myszą, naciśnięcie klawiszy),
* aktualizacja stanu gry (przesunięcia elementów, aktualizacja planszy),
* aktualizacja wyświetlanego okna (narysowanie nowego stanu gry).

Dopisujemy więc do kodu głównę pętlę wraz z obsługą zdarzeń:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str4.py
    :linenos:
    :lineno-start: 95
    :lines: 95-

W obrębie głównej pętli programu pętla ``for`` odczytuje kolejne zdarzenia zwracane przez metodę ``pygame.event.get()``. Jak widać, obsługujemy wydarzenie typu (właściwość ``.type``) QUIT, czyli zakończenie aplikacji, oraz MOUSEMOTION, a więc ruch myszy. W tym drugim przypadku pobieramy współrzędne kursora (``.pos``) i obliczamy przesunięcie myszy w poziomie. Kolejne instrukcje uniemożliwiają wyjście paletki gracza poza okno gry.
Do pętli głównej musimy dopisać jeszcze kod kontrolujący paletkę komputera, piłkę i jej interakcje ze ścianami okna gry oraz paletkami, a także rysujący poszczególne obiekty:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str5.py
    :linenos:
    :lineno-start: 119
    :lines: 119-

Komentarze w kodzie wyjaśniają kolejne czynności. Warto zwrócić uwagę na sposób odczytywania pozycji obiektów klasy ``Rect`` (prostokątów), czyli właściwości ``.x, .y, .centerx, .right, .left, .top, .bottom``; oraz na sprawdzanie kolizji piłki z paletkami, czyli metodę ``.colliderect()``. Ostatnie linie kodu rysują okno gry i obiekty (tekst z wynikami graczy, paletki i piłkę) ze zmienionymi właściwościami (liczba punktów, położenie). Funkcja ``pygame.display.update()``, która musi być wykonywana na końcu rysowania, aktualizuje obraz gry. Ostatnia linia natomiast (``fpsClock.tick()``) pozwala blokuje grę na 30 klatek na sekundę, aby nie działała tak szybko jak pozwala sprzęt, lecz ze stałą prędkością.

Grę możemy uruchomić poleceniem wpisanym w terminalu:

.. code:: bash

    $ python pong_str.py

Słownik
---------

Klatki na sekundę (FPS) – liczba klatek wyświetlanych w ciągu sekundy, czyli częstotliwość, z jaką statyczne obrazy pojawiają się na ekranie. Jest ona miarą płynności wyświetlania ruchomych obrazów.
Kanał alfa (ang. alpha channel) – w grafice komputerowej jest kanałem, który definiuje przezroczyste obszary grafiki. Jest on zapisywany dodatkowo wewnątrz grafiki razem z trzema wartościami barw składowych RGB.
Inicjalizacja – proces wstępnego przypisania wartości zmiennym i obiektom. Każdy obiekt jest inicjalizowany różnymi sposobami zależnie od swojego typu.
Iteracja – czynność powtarzania (najczęściej wielokrotnego) tej samej instrukcji (albo wielu instrukcji) w pętli. Mianem iteracji określa się także operacje wykonywane wewnątrz takiej pętli.
Zdarzenie (ang. event) – zapis zajścia w systemie komputerowym określonej sytuacji, np. poruszenie myszką, kliknięcie, naciśnięcie klawisza.
pygame.time.Clock() – tworzy obiekt do śledzenia czasu; .tick() – kontroluje ile milisekund upłynęło od poprzedniego wywołania.
pygame.display.set_mode() – inicjuje okno lub ekran do wyświetlania, parametry: rozdzielczość w pikselach = (x,y), flagi, głębia koloru.
pygame.display.set_caption() – ustawia tytuł okna, parametr: tekst tytułu.
pygame.Surface() – obiekt reprezentujący dowolny obrazek (grafikę), który ma określoną rozdzielczość (szerokość i wysokość) oraz format pikseli (głębokość, przezroczystość); SRCALPHA – oznacza, że format pikseli będzie zawierać ustawienie alfa (przezroczystości); .fill() – wypełnia obrazek kolorem; .get_rect() – zwraca prostokąt zawierający obrazek; .convert_alpha() – zmienia format pikseli, w tym przezroczystość; .blit() – rysuje jeden obrazek na drugim, parametry: źródło, cel.
pygame.draw.ellipse() – rysuje okrągły kształt wewnątrz prostokąta, parametry: przestrzeń, kolor, prostokąt.
pygame.font.Font() – tworzy obiekt czcionki z podanego pliku; .render() – tworzy nową powierzchnię z podanym tekstem, parametry: tekst, antyalias, kolor, tło.
pygame.event.get() – pobiera zdarzenia z kolejki zdarzeń; event.type() – zwraca identyfikator SDL typu zdarzenia, np. KEYDOWN, KEYUP, MOUSEMOTION, QUIT.
SDL (Simple DirectMedia Layer) – międzyplatformowa bilioteka ułatwiająca tworzenie gier i programów multimedialnych.
pygame.Rect – obiekt pygame przechowujący współrzędne prostokąta; .centerx, .x, .y, .top, .bottom, .left, .right – wirtualne własności obiektu prostokąta określające jego położenie; .colliderect() – metoda sprawdza czy dwa prostokąty nachodzą na siebie.

POĆWICZ SAM
-----------
Zmodyfikuj właściwości obiektów (paletek, piłki) takie jak rozmiar, kolor, początkowa pozycja.
Zmień położenie paletek tak aby znalazły przy lewej i prawej krawędzi okna, wprowadź potrzebne zmiany w kodzie, aby umożliwić rozgrywkę.
Dodaj trzecią paletkę, która co jakiś czas będzie "przelatywać" przez środek planszy i zmieniać w przypadku kolizji tor i kolor piłki.

Metryka
^^^^^^^

:Autorzy: Łukasz Zarzecki, Robert Bednarz <rob@lo1.sandomierz.pl>

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>


.. include:: ../copyright.rst
