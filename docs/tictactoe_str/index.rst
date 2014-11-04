Gra w Kółko i Krzyżyk (str)
===========================

.. highlight:: python

Biblioteka `PyGame`_ ułatwia tworzenie aplikacji multimedialnych, w tym gier. Poniższy scenariusz prezentuje implementację prostej gry Kółko i krzyżyk.

.. _PyGame: http://www.pygame.org/wiki/tutorials

Zmienne i plansza gry
---------------------

Tworzymy plik ``tictactoe.py`` w terminalu lub w wybranym edytorze i zaczynamy od zdefiniowania zmiennych określających właściwości obiektów w naszej grze.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: tictactoe_str1.py
    :linenos:

W instrukcji ``pygame.display.set_mode()`` inicjalizujemy okno gry o rozmiarach 150x150 pikseli i 32 bitowej głębi kolorów. Tworzymy w ten sposób powierzchnię główną do rysowania zapisaną w zmiennej ``OKNOGRY``. ``POLE_GRY`` to lista elementów reprezentujących pola planszy, które mogą być puste (wartość 0), zawierać kółka gracza (wartość 1) lub komputera (wartość 2). Pozostałe zmienne określają, do kogo należy następny ruch, kto wygrał i czy nastąpił koniec gry.

Rysuj planszę gry
---------------------

Planszę można narysować na wiele sposobów, np. tak:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: tictactoe_str2.py
    :linenos:
    :lineno-start: 24
    :lines: 24-

Pierwsza funkcja, ``rysuj_plansze()``, wykorzystując zagnieżdżone pętle, rysuje nam 9 kwadratów o białym obramowaniu i szerokości 50 pikseli (formalnie są to obiekty :term:`Rect` zwracane przez metodę ``pygame.draw.rect()``). Zadaniem funkcji ``rysuj_pole_gry()`` jest narysowanie w zależności od stanu planszy gry zapisanego w liście ``POLE_GRY`` kółek o niebieskim (gracz) lub czerwonym (komputer) kolorze za pomocą metody ``pygame.draw.circle()``.

Sztuczna inteligencja
---------------------

Decydującą rolę w grze odgrywa komputer, od którego inteligencji zależy, czy rozgrywka przyniesie jakąś satysfakcję. Dopisujemy więc funkcje obsługujące sztuczną inteligencję:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: tictactoe_str3.py
    :linenos:
    :lineno-start: 46
    :lines: 46-

Za sposób gry komputera odpowiada funkcja ``ai_ruch()`` (*ai* – ang. *artificial intelligence*, sztuczna inteligencja). Na początku zawiera ona definicje dwóch list (``uklady_wygrywam, uklady_blokuje``), zawierających układy wartości, dla których komputer wygrywa oraz które powinien zablokować, aby nie wygrał gracz. O tym, które pole należy zaznaczyć, decyduje funkcja ``sprawdz_pola()`` przyjmująca jako argument najpierw układy wygrywające, później blokujące.

Podstawą działania funkcji ``sprawdz_pola()`` jest lista ``POLA_INDEKSY`` zawierająca jako elementy listy indeksów pól tworzących wiersze, kolumny i przekątne ``POLA_GRY`` (czyli planszy). Pętla ``for lista in POLA_INDEKSY:`` pobiera kolejne listy, tworzy w liście pomocniczej kol trójkę wartości odczytanych z ``POLA_GRY`` i próbuje ją dopasować do przekazanego jako argument układu wygrywającego lub blokującego. Jeżeli znajdzie dopasowanie zwraca liczbę oznaczającą gracza lub komputer, o ile opcjonalny argument ``WYGRANY`` ma wartość inną niż ``None``, w przeciwnym razie zwracany jest indeks ``POLA_GRY``, na którym komputer powinien postawić swój znak.

Jeżeli indeks zwrócony przez funkcję ``sprawdz_pola()`` jest pozytywny, przekazywany jest do funkcji ``postaw_znak()``, której zadaniem jest zapisanie w ``POLU_GRY`` pod otrzymanym indeksem wartości symbolizującej znak komputera (czyli 2) oraz nadanie i zwrócenie zmiennej RUCH wskazującej na gracza (wartość 1).

O ile na planszy nie ma układu wygrywającego lub nie ma konieczności blokowania gracza, komputer w pętli losuje przypadkowe pole (``random.randrange(0,9)``), dopóki nie znajdzie pustego, i przekazuje jego indeks do funkcji ``postaw_znak()``.

Główna pętla programu
---------------------

Programy interaktywne, w tym gry, reagujące na działania użytkownika, takie jak ruchy czy kliknięcia myszą, działają w pętli, której zadaniem jest:

1. przechwycenie i obsługa działań użytkownika, czyli tzw. zdarzeń (ruchy, kliknięcia myszą, naciśnięcie klawiszy),
2. aktualizacja stanu gry (przesunięcia elementów, aktualizacja planszy),
3. aktualizacja wyświetlanego okna (narysowanie nowego stanu gry).

Dopisujemy więc do kodu główną pętlę wraz z obsługą zdarzeń oraz dwie funkcje pomocnicze w niej wywoływane:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: tictactoe_str4.py
    :linenos:
    :lineno-start: 105
    :lines: 105-

W obrębie głównej pętli programu pętla ``for`` odczytuje kolejne zdarzenia zwracane przez metodę ``pygame.event.get()``. Jak widać, w pierwszej kolejności obsługujemy wydarzenie typu (właściwość ``.type``) QUIT, czyli zakończenie aplikacji. Później, o ile nikt nie wygrał (zmienna ``WYGRANA`` ma wartość ``False``), a kolej na ruch gracza (zmienna ``RUCH`` ma wartość 1), przechwytujemy wydarzenie ``MOUSEBUTTONDOWN``, tj. kliknięcie myszą. Sprawdzamy, czy naciśnięto pierwszy przycisk, pobieramy współrzędne kursora (``.pos``) i wyliczamy indeks klikniętego pola. Na koniec wywołujemy omówioną wcześniej ``funkcję postaw_znak()``. Jeżeli kolej na komputer, uruchamiamy sztuczną inteligencję (``ai_ruch()``).

Po wykonaniu ruchu przez komputer lub gracza trzeba sprawdzić, czy któryś z przeciwników nie wygrał. Korzystamy z funkcji ``kto_wygral()``, która definiuje dwa układy wygrywające (``uklad_gracz`` i ``uklad_komputer``) i za pomocą omówionej wcześniej funkcji ``sprawdz_pola()`` sprawdza, czy można je odnaleźć w ``POLU_GRY``. Na końcu sprawdza możliwość remisu i zwraca wartość symbolizującą wygranego (1, 2, 3) lub ``None``, o ile możliwe są kolejne ruchy. Wartość ta wpływa w pętli głównej na zmienną ``WYGRANA`` kontrolującą obsługę ruchów gracza i komputera.

Funkcja ``drukuj_wynik()`` ma za zadanie przygotowanie końcowego napisu. W tym celu tworzy obiekt czcionki z podanego pliku (``pygame.font.Font()``), następnie renderuje nowy obrazek z odpowiednim tekstem (``.render()``), pobiera jego powierzchnię prostokątną (``.get_rect()``), pozycjonują ją (``.center()``) i rysują na głównej powierzchni gry (``.blit()``).
Ostatnie linie kodu wypełniają okno gry kolorem (``.fill()``), wywołują funkcję rysujące planszę (``rysuj_plansze()``), stan gry (``rysuj_pole_gry()``, czyli znaki gracza i komputera), a także ewentualny komunikat końcowy (``drukuj_wynik()``). Funkcja ``pygame.display.update()``, która musi być wykonywana na końcu rysowania, aktualizuje obraz gry na ekranie.

.. note::
    Plik wykorzystywany do wyświetlania tekstu (``freesansbold.ttf``) musi znaleźć się w katalogu ze skryptem.

Grę możemy uruchomić poleceniem wpisanym w terminalu:

.. code:: bash

    $ python tictactoe.py

.. figure:: tictactoe.png

Poćwicz sam
-----------

    Zmień grę tak, aby zaczynał ją komputer.
    Dodaj do gry możliwość rozgrywki wielokrotnej bez konieczności ponownego uruchamiania skryptu.
    Zmodyfikuj funkcję rysującą pole gry tak, aby komputer rysował krzyżyki, a nie kółka.

Źródła
^^^^^^^^

Wszystkie kody możesz pobrać w formie archiwum: :download:`tictactoe_str.zip <tictactoe_str.zip>`

Słownik
^^^^^^^^

.. glossary::

    Kanał alfa (ang. alpha channel)
        w grafice komputerowej jest kanałem, który definiuje przezroczyste obszary grafiki. Jest on zapisywany dodatkowo wewnątrz grafiki razem z trzema wartościami barw składowych RGB.

    Inicjalizacja
        proces wstępnego przypisania wartości zmiennym i obiektom. Każdy obiekt jest inicjalizowany różnymi sposobami zależnie od swojego typu.

    Iteracja
        czynność powtarzania (najczęściej wielokrotnego) tej samej instrukcji (albo wielu instrukcji) w pętli. Mianem iteracji określa się także operacje wykonywane wewnątrz takiej pętli.

    Zdarzenie (ang. event)
        zapis zajścia w systemie komputerowym określonej sytuacji, np. poruszenie myszką, kliknięcie, naciśnięcie klawisza.
    
    pygame.locals
        moduła zawierający różne stałe używane przez Pygame, np. typy zdarzeń, identyfikatory naciśniętych klawiszy itp.

    pygame.time.Clock()
        tworzy obiekt do śledzenia czasu; ``.tick()`` – kontroluje ile milisekund upłynęło od poprzedniego wywołania.

    pygame.display.set_mode()
        inicjuje okno lub ekran do wyświetlania, parametry: rozdzielczość w pikselach = (x,y), flagi, głębia koloru.

    pygame.display.set_caption()
        ustawia tytuł okna, parametr: tekst tytułu.

    pygame.Surface()
        obiekt reprezentujący dowolny obrazek (grafikę), który ma określoną rozdzielczość (szerokość i wysokość) oraz format pikseli (głębokość, przezroczystość); SRCALPHA – oznacza, że format pikseli będzie zawierać ustawienie alfa (przezroczystości); ``.fill()`` – wypełnia obrazek kolorem; ``.get_rect()`` – zwraca prostokąt zawierający obrazek, czyli obiekt **Rect**; ``.convert_alpha()`` – zmienia format pikseli, w tym przezroczystość; ``.blit()`` – rysuje jeden obrazek na drugim, parametry: źródło, cel.

    pygame.draw.ellipse()
        rysuje okrągły kształt wewnątrz prostokąta, parametry: przestrzeń, kolor, prostokąt.

    pygame.font.Font()
        tworzy obiekt czcionki z podanego pliku; ``.render()`` – tworzy nową powierzchnię z podanym tekstem, parametry: tekst, antyalias, kolor, tło.

    pygame.event.get()
        pobiera zdarzenia z kolejki zdarzeń; ``event.type()`` – zwraca identyfikator SDL typu zdarzenia, np. KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONDOWN, QUIT.

    SDL (Simple DirectMedia Layer)
        międzyplatformowa biblioteka ułatwiająca tworzenie gier i programów multimedialnych.

    Rect
        obiekt ``pygame.Rect`` przechowujący współrzędne prostokąta; ``.centerx, .x, .y, .top, .bottom, .left, .right`` – wirtualne własności obiektu prostokąta określające jego położenie; ``.colliderect()`` – metoda sprawdza czy dwa prostokąty nachodzą na siebie.

Metryka
^^^^^^^

:Autorzy: Robert Bednarz <ecg@ecg.vot.pl>, Łukasz Zarzecki

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>


.. include:: ../copyright.rst
