# coding=utf-8
# Copyright 2014 Janusz Skonieczny

"""
Gra w życie

http://pl.wikipedia.org/wiki/Gra_w_życie
"""

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
        pygame.display.set_caption('Simple Pong')

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
        self.population = Population(width, height, cell_size)

    def run(self):
        """
        Główna pętla gry
        """
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.board.draw(
                self.population,
            )
            if getattr(self, "started", None):
                self.population.cycle_generation()
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

            if event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_RETURN:
                self.started = True

            if event.type == pygame.locals.MOUSEMOTION or event.type == pygame.locals.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                if not any(buttons):
                    # ignoruj zdarzenie jeśli żaden z guzików nie jest wciśnięty
                    continue
                # pobierz pozycję kursora na planszy mierzoną w pikselach
                x, y = pygame.mouse.get_pos()
                # przeliczamy współrzędne komórki z pikseli
                x, y = x / self.population.box_size, y / self.population.box_size
                # dodaj żywą komórką jeśli wciśnięty jest pierwszy guzik
                alive = True if buttons[0] else False
                self.population.set_cell(x, y, alive)


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
        Tworzy i zwraca index pustej populacji
        """
        return [[DEAD for y in xrange(self.height)] for x in xrange(self.width)]

    def draw_on(self, surface):
        """
        Rysuje komórki na planszy
        """
        for x, y in self.alive_cells():
            size = (self.box_size, self.box_size)
            position = (x * self.box_size, y * self.box_size)
            pygame.draw.rect(surface, (255, 255, 255), pygame.locals.Rect(position, size), 1)

    def set_cell(self, x, y, alive):
        self.generation[x][y] = ALIVE if alive else DEAD

    def alive_cells(self):
        """
        Generator zwracający współrzędne żywych komórek.
        """
        for x in range(len(self.generation)):
            column = self.generation[x]
            for y in range(len(column)):
                if column[y] == ALIVE:
                    yield x, y

    def neighbours(self, x, y):
        """
        Generator zwracający wszystkich okolicznych sąsiadów
        """
        for nx in range(x-1, x+2):
            for ny in range(y-1, y+2):
                if nx == x and ny == y:
                    continue
                try:
                    yield self.generation[nx][ny]
                except IndexError:
                    # ignorujemy indeksy poza zakresem
                    pass


    def cycle_generation(self):
        """
        Generuje następną generację populacji komórek
        """
        next_gen = self.reset_generation()
        for x in range(len(self.generation)):
            column = self.generation[x]
            for y in range(len(column)):
                neighbours = sum(self.neighbours(x, y))
                if neighbours == 3:
                    # rozmnażamy się
                    next_gen[x][y] = ALIVE
                elif neighbours == 2:
                    # przechodzi do kolejnej generacji bez zmian
                    next_gen[x][y] = column[y]
                else:
                    # za dużo lub za mało sąsiadów by przeżyć
                    next_gen[x][y] = DEAD
        self.generation = next_gen


# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = GameOfLife(80, 40)
    game.run()


