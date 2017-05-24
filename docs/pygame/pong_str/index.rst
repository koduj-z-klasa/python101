.. _pong-str:

Pong (str)
###################

.. highlight:: python

Wersja strukturalna klasycznej gry w odbijanie piłeczki zrealizowana z użyciem biblioteki `PyGame`_.

.. _PyGame: http://www.pygame.org/wiki/tutorials

.. contents::
    :depth: 1
    :local:

.. figure:: pong.png

Pole gry
***********************

Tworzymy plik ``pong_str.py`` w terminalu lub w wybranym edytorze, zapisujemy na dysku
i wprowadzamy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str01.py
    :linenos:

Na początku importujemy wymagane biblioteki i inicjujemy moduł ``pygame``.
Dużymi literami zapisujemy nazwy zmiennych określające właściwości pola gry,
które inicjalizujemy w instrukcji ``pygame.display.set_mode()``.
Tworzy ona powierzchnię o wymiarach 800x400 pikseli i 32 bitowej głębi kolorów,
na której umieszczać będziemy pozostałe obiekty. W kolejnej instrukcji ustawiamy tytuł okna gry.

Programy interaktywne, w tym gry, reagujące na działania użytkownika,
takie jak ruchy czy kliknięcia myszą, działają w tzw. **głównej pętli**,
której zadaniem jest:

a) przechwycenie i obsługa działań użytkownika, czyli tzw. zdarzeń (ruchy, kliknięcia myszą, naciśnięcie klawiszy),
b) aktualizacja stanu gry (np. obliczanie przesunięć elementów) i rysowanie go.

Zadanie z punktu *a)* realizuje pętla ``for``, która odczytuje kolejne zdarzenia
zwracane przez metodę ``pygame.event.get()``. Za pomocą instrukcji warunkowych
możemy przechwytywać zdarzenia, które chcemy obsłużyć, np. naciśnięcie przycisku
zamknięcia okna: ``if event.type == QUIT``.

Instrukcja ``oknogry.fill(BLUE)`` wypełnia okno zdefiniowanym kolorem.
Jego wyświetlenie następuje w poleceniu ``pygame.display.update()``.

Uruchom aplikację, wydając w terminalu polecenie:

.. code:: bash

    $ python pong_str.py

Paletka gracza
***************

Planszę gry już mamy, pora umieścić na niej paletkę gracza.
Poniższy kod wstawiamy **przed pętlą główną** programu:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str02.py
    :linenos:
    :lineno-start: 22
    :lines: 22-33

Elementy graficzne tworzymy za pomocą polecenia
``pygame.Surface((szerokosc, wysokosc), flagi, głębia)``.
Utworzony obiekt możemy wypełnić kolorem: ``.fill(kolor)``.
Położenie obiektu określimy pobierając na początku prostokątny obszar (:term:`Rect`),
który go reprezentuje, metodą ``get_rect()``. Następnie podajemy współrzędne
``x`` i ``y`` wyznaczające położenie w poziomie i pionie.

.. note::

    * Początek układu współrzędnych w *Pygame* to lewy górny róg okna głównego.
    * Położenie obiektu można ustawić również podając nazwane argumenty:
      ``obiekt_prost = obiekt.get_rect(x = 350, y =350)``.
    * Położenie obiektów klasy ``Rect`` (prostokątów) możemy odczytwyać
      wykorzystując właściwości, takie jak: ``.x, .y, .centerx, .right, .left, .top, .bottom``.

Omówiony kod utworzy obiekt reprezentujący paletkę gracza, ale trzeba ją jeszcze
umieścić na planszy gry. W tym celu użyjemy metody ``.blit()``, która służy
rysowaniu jednego obrazka na drugim. Poniższy kod musimy wstawić w pętli głównej
przed instrukcją wyświetlającą okno.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str02.py
    :linenos:
    :lineno-start: 47
    :lines: 47-48

Pozostaje uruchomienie kodu.

Ruch paletki
*************

W pętli przechwytującej zdarzenia dopisujemy zaznaczony poniżej kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str03.py
    :linenos:
    :lineno-start: 35
    :lines: 35-67
    :emphasize-lines: 10-24

Chcemy sterować paletką za pomocą myszy. Zadaniem powyższego kodu jest
przechwycenie jej ruchu (``MOUSEMOTION``), odczytanie współrzędnych kursora
z tupli ``event.pos`` i obliczenie przesunięcia określającego nowe położenie paletki.
Kolejne instrukcje warunkowe korygują nową pozycję paletki, jeśli wykraczamy
poza granice pola gry.

Przetestuj kod.

Piłka w grze
************

Piłkę tworzymy podobnie jak paletkę. Przed pętlą główną programu wstawiamy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str04.py
    :linenos:
    :lineno-start: 35
    :lines: 35-51

Przy tworzeniu powierzchni dla piłki używamy flagi ``SRCALPHA``, co oznacza,
że obiekt graficzny będzie zawierał przezroczyste piksele. Samą piłkę rysujemy
za pomocą instrukcji ``pygame.draw.ellipse(powierzchnia, kolor, prostokąt)``.
Ostatni argument to lista zawierająca współrzędne lewego górnego i prawego dolnego
rogu prostokąta, w który wpisujemy piłkę.

Ruch piłki, aby był płynny, wymaga użycia animacji. Ustawiamy więc liczbę
generowanych klatek na sekundę (``FPS = 30``) i przygotowujemy obiekt zegara,
który będzie kontrolował czas.

Teraz **pod pętlą** (nie w pętli!) ``for``, która przechwytuje zdarzenia, umieszczamy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str04.py
    :linenos:
    :lineno-start: 78
    :lines: 78-100

Na uwagę zasługuje metoda ``.move_ip(offset, offset)``, która przesuwa prostokąt
zawierający piłkę o podane jako ``offset`` wartości. Dalej decydujemy, co ma się dziać,
kiedy piłka wyjdzie poza pole gry. Metoda ``.colliderect(prostokąt)`` pozwala sprawdzić,
czy dwa obiekty nachodzą na siebie. Dzięki temu możemy odwrócić bieg piłeczki
po jej zetknięciu się z paletką gracza.

Piłkę trzeba umieścić na polu gry. Podaną niżej instrukcję umieszczamy poniżej
polecenia rysującego paletkę gracza:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str04.py
    :linenos:
    :lineno-start: 108
    :lines: 108-109

Na koniec ograniczamy prędkość animacji wywołując metodę ``.tick(fps)``,
która wstrzymuje wykonywanie programu na podaną jako argument liczbę klatek na sekundę.
Podany niżej kod trzeba dopisać na końcu w pętli głównej:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str04.py
    :linenos:
    :lineno-start: 114
    :lines: 114-115

Teraz możesz już zagrać sam ze sobą! Przetestuj działanie programu.

AI – przeciwnik
***************

Dodamy do gry przeciwnika AI (ang. *artificial inteligence*), czyli paletkę sterowaną programowo.

Przed główną pętlą programu dopisujemy kod tworzący paletkę AI:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str05.py
    :linenos:
    :lineno-start: 53
    :lines: 53-64

Tu nie ma nic nowego, więc od razu przed instrukcją wykrywającą kolizję piłki
z paletką gracza (``if pilka_prost.colliderect(paletka1_prost)``)
dopisujemy kod sterujący ruchem paletki AI:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str05.py
    :linenos:
    :lineno-start: 111
    :lines: 111-123

Samą paletkę AI trzeba umieścić na planszy, po instrukcji rysującej paletkę
gracza dopisujemy więc:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

.. literalinclude:: pong_str05.py
    :linenos:
    :lineno-start: 134
    :lines: 134-136
    :emphasize-lines: 3

Pozostaje zmienić kod odpowiedzialny za odbijanie piłki od górnej krawędzi
planszy (``if pilka_prost.top <= 0``), żeby przeciwnik AI mógł przegrywać.
W tym celu dokonujemy zmian wg poniższego kodu:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str05.py
    :linenos:
    :lineno-start: 102
    :lines: 102-105
    :emphasize-lines: 3-4

Teraz można już zagrać z komputerem :-).

Liczymy punkty
**************

Co to za gra, w której nie wiadomo, kto wygrywa...
Dodamy kod zliczający i wyświetlający punkty. Przed główną pętlą programu wstawiamy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str06.py
    :linenos:
    :lineno-start: 66
    :lines: 66-84

Po zdefiniowaniu zmiennych przechowujących punkty graczy, tworzymy obiekt czcionki
z podanego pliku (``pygame.font.Font()``). Następnie definiujemy funkcje,
których zadaniem jest rysowanie punktacji graczy. Na początku tworzą one nowe obrazki
z punktacją gracza (``.render()``), pobierają ich prostokąty (``.get_rect()``),
pozycjonują je (``.center()``) i rysują na głównej powierzchni gry (``.blit()``).

.. note::

    Plik wykorzystywany do wyświetlania tekstu (``freesansbold.ttf``)
    musi znaleźć się w katalogu ze skryptem.

W pętli głównej programu musimy umieścić wyrażenia zliczające punkty.
Jeżeli piłka ucieknie górą, punkty dostaje gracz, w przeciwnym wypadku AI.
Dopisz podświetlone instrukcje:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str06.py
    :linenos:
    :lineno-start: 122
    :lines: 122-131
    :emphasize-lines: 5, 10

Obie funkcje wyświetlające punkty również trzeba wywołać z pętli głównej,
a więc po instrukcji wypełniającej okno gry kolorem (``oknogry.fill(LT_BLUE)``)
dopisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str06.py
    :linenos:
    :lineno-start: 153
    :lines: 153-157
    :emphasize-lines: 4-5

Sterowanie klawiszami
*********************

Skoro możemy przechwytywać ruch myszy, nic nie stoi na przeszkodzie,
aby umożliwić poruszanie paletką za pomocą klawiszy.
W pętli ``for`` odczytującej zdarzenia dopisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str07.py
    :linenos:
    :lineno-start: 114
    :lines: 114-123

Naciśnięcie klawisza generuje zdarzenie ``pygame.KEYDOWN``.
Dalej w instrukcji warunkowej sprawdzamy, czy naciśnięto klawisz kursora
lewy lub prawy i przesuwamy paletkę o 5 pikseli.

.. tip::

    `Kody klawiszy <http://www.pygame.org/docs/ref/key.html>`_ możemy sprawdzić w dokumentacji *Pygame*.

Uruchom program i sprawdź, jak działa. Szybko zauważysz, że wciśnięcie strzałki
porusza paletką, ale żeby poruszyła się znowu, trzeba naciskanie powtarzać.
To niewygodne, paletka powinna ruszać się dopóki klawisz jest wciśnięty.
Przed pętlą główną dodamy więc poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: pong_str07.py
    :linenos:
    :lineno-start: 86
    :lines: 86-87

Dzięki tej instrukcji włączyliśmy powtarzalność wciśnięć klawiszy. Przetestuj, czy działa.

Zadania dodatkowe
***********************

* Zmodyfikuj właściwości obiektów (paletek, piłki) takie jak rozmiar, kolor, początkowa pozycja.
* Zmień położenie paletek tak, aby znalazły się przy lewej i prawej krawędzi okna,
  wprowadź potrzebne zmiany w kodzie, aby poruszały się w pionie.
* Dodaj trzecią paletkę, która co jakiś czas będzie "przelatywać" przez środek planszy
  i zmieniać w przypadku kolizji tor i kolor piłki.

Materiały
**************

**Źródła:**

* :download:`pong_str.zip <pong_str.zip>`
