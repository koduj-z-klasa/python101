.. glossary::

    Klatki na sekundę (FPS)
        liczba klatek wyświetlanych w ciągu sekundy, czyli częstotliwość, z jaką statyczne obrazy pojawiają się na ekranie. Jest ona miarą płynności wyświetlania ruchomych obrazów.

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

    pygame.draw.rect()
        rysuje prostokąt na wskazanej powierzchni, parametry: powierzchnia, kolor, obiekt Rect, grubość obramowania.

    pygame.font.Font()
        tworzy obiekt czcionki z podanego pliku; ``.render()`` – tworzy nową powierzchnię z podanym tekstem, parametry: tekst, antyalias, kolor, tło.

    pygame.event.get()
        pobiera zdarzenia z kolejki zdarzeń; ``event.type()`` – zwraca identyfikator SDL typu zdarzenia, np. KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONDOWN, QUIT.

    SDL (Simple DirectMedia Layer)
        międzyplatformowa biblioteka ułatwiająca tworzenie gier i programów multimedialnych.

    Rect
        obiekt pygame.Rect przechowujący współrzędne prostokąta; ``.centerx, .x, .y, .top, .bottom, .left, .right`` – wirtualne własności obiektu prostokąta określające jego położenie; ``.colliderect()`` – metoda sprawdza czy dwa prostokąty nachodzą na siebie.
