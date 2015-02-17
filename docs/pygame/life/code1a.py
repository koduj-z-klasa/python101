# coding=utf-8

import pygame
import pygame.locals


class Board(object):
    """
    Plansza do gry. Odpowiada za rysowanie okna gry.
    """

    def __init__(self, width, height):
        """
        Konstruktor planszy do gry. Przygotowuje okienko gry.

        :param width: szerokość w pikselach
        :param height: wysokość w pikselach
        """
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Game of life')

    def draw(self, *args):
        """
        Rysuje okno gry

        :param args: lista obiektów do narysowania
        """
        background = (0, 0, 0)
        self.surface.fill(background)
        for drawable in args:
            drawable.draw_on(self.surface)

        # dopiero w tym miejscu następuje fatyczne rysowanie
        # w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać narysowane
        pygame.display.update()


class GameOfLife(object):
    """
    Łączy wszystkie elementy gry w całość.
    """

    def __init__(self, width, height, cell_size=10):
        """
        Przygotowanie ustawień gry
        :param width: szerokość planszy mierzona liczbą komórek
        :param height: wysokość planszy mierzona liczbą komórek
        :param cell_size: bok komórki w pikselach
        """
        pygame.init()
        self.board = Board(width * cell_size, height * cell_size)
        # zegar którego użyjemy do kontrolowania szybkości rysowania
        # kolejnych klatek gry
        self.fps_clock = pygame.time.Clock()

    def run(self):
        """
        Główna pętla gry
        """
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.board.draw()
            self.fps_clock.tick(15)

    def handle_events(self):
        """
        Obsługa zdarzeń systemowych, tutaj zinterpretujemy np. ruchy myszką

        :return True jeżeli pygame przekazał zdarzenie wyjścia z gry
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True


# magiczne liczby używane do określenia czy komórka jest żywa
DEAD = 0
ALIVE = 1


class Population(object):
    """
    Populacja komórek
    """

    def __init__(self, width, height, cell_size=10):
        """
        Przygotowuje ustawienia populacji

        :param width: szerokość planszy mierzona liczbą komórek
        :param height: wysokość planszy mierzona liczbą komórek
        :param cell_size: bok komórki w pikselach
        """
        self.box_size = cell_size
        self.height = height
        self.width = width
        self.generation = self.reset_generation()

    def reset_generation(self):
        """
        Tworzy i zwraca macierz pustej populacji
        """
        # w pętli wypełnij listę kolumnami
        # które także w pętli zostają wypełnione wartością 0 (DEAD)
        return [[DEAD for y in xrange(self.height)] for x in xrange(self.width)]

def handle_mouse(self):
    # pobierz stan guzików myszki z wykorzystaniem funcji pygame
    buttons = pygame.mouse.get_pressed()
    if not any(buttons):
        # ignoruj zdarzenie jeśli żaden z guzików nie jest wciśnięty
        return

    # dodaj żywą komórką jeśli wciśnięty jest pierwszy guzik myszki
    # będziemy mogli nie tylko dodawać żywe komórki ale także je usuwać
    alive = True if buttons[0] else False

    # pobierz pozycję kursora na planszy mierzoną w pikselach
    x, y = pygame.mouse.get_pos()

    # przeliczamy współrzędne komórki z pikseli na współrzędne komórki w macierz
    # gracz może kliknąć w kwadracie o szerokości box_size by wybrać komórkę
    x /= self.box_size
    y /= self.box_size

    # ustaw stan komórki na macierzy
    self.generation[x][y] = ALIVE if alive else DEAD

def draw_on(self, surface):
    """
    Rysuje komórki na planszy
    """
    for x, y in self.alive_cells():
        size = (self.box_size, self.box_size)
        position = (x * self.box_size, y * self.box_size)
        color = (255, 255, 255)
        thickness = 1
        pygame.draw.rect(surface, color, pygame.locals.Rect(position, size), thickness)

def alive_cells(self):
    """
    Generator zwracający współrzędne żywych komórek.
    """
    for x in range(len(self.generation)):
        column = self.generation[x]
        for y in range(len(column)):
            if column[y] == ALIVE:
                # jeśli komórka jest żywa zwrócimy jej współrzędne
                yield x, y


# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = GameOfLife(80, 40)
    game.run()
