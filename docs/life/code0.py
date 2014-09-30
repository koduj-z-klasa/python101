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

            if event.type == pygame.locals.MOUSEMOTION or event.type == pygame.locals.MOUSEBUTTONDOWN:
            if event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_RETURN:
                self.started = True




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
                    # jeśli komórka jest żywa zwrócimy jej współrzędne
                    yield x, y

    def draw_on(self, surface):
        """
        Rysuje komórki na planszy
        """
        for x, y in self.alive_cells():
            size = (self.box_size, self.box_size)
            position = (x * self.box_size, y * self.box_size)
        color = (255, 255, 255)
            pygame.draw.rect(surface, (255, 255, 255), pygame.locals.Rect(position, size), 1)

    def neighbours(self, x, y):
        """
        Generator zwracający wszystkich okolicznych sąsiadów
        """
        for nx in range(x-1, x+2):
            for ny in range(y-1, y+2):
                if nx == x and ny == y:
                    # pomiń te współrzędne
                    continue
                if nx > self.width:
                    # sąsiad poza końcem planszy, bierzemy pierwszego w danym rzędzie
                    nx = 0
                elif nx < 0:
                    # sąsiad przed początkiem planszy, bierzemy ostatniego w danym rzędzie
                    nx = self.width - 1
                if ny > self.height:
                    # sąsiad poza końcem planszy, bierzemy pierwszego w danej kolumnie
                    ny = 0
                elif ny < 0:
                    # sąsiad przed początkiem planszy, bierzemy ostatniego w danej kolumnie
                    ny = self.height - 1

                # dla każdego nie pominiętego powyżej
                # przejścia pętli zwróć komórkę w tych współrzędnych
                yield self.generation[nx][ny]

    def cycle_generation(self):
        """
        Generuje następną generację populacji komórek
        """
        next_gen = self.reset_generation()
        for x in range(len(self.generation)):
            column = self.generation[x]
            for y in range(len(column)):
                # pobieramy wartości sąsiadów
                # dla żywej komórki dostaniemy wartość 1 (ALIVE)
                # dla martwej otrzymamy wartość 0 (DEAD)
                # zwykła suma pozwala nam określić liczbę żywych sąsiadów
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

        # nowa generacja staje się aktualną generacją
        self.generation = next_gen


# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = GameOfLife(80, 40)
    game.run()


