# coding=utf-8
# Copyright 2014 Janusz Skonieczny

"""
Gra w kółko i krzyżyk
"""

import pygame
import pygame.locals
import logging

# Konfiguracja modułu logowania, element dla zaawansowanych
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-7s | %(module)s.%(funcName)s - %(message)s', datefmt='%H:%M:%S')
logging.getLogger().setLevel(logging.INFO)


class Board(object):
    """
    Plansza do gry. Odpowiada za rysowanie okna gry.
    """

    def __init__(self, width):
        """
        Konstruktor planszy do gry. Przygotowuje okienko gry.

        :param width: szerokość w pikselach
        """
        self.surface = pygame.display.set_mode((width, width), 0, 32)
        pygame.display.set_caption('Tic-tac-toe')

        # Przed pisaniem tekstów, musimy zainicjować mechanizmy wyboru fontów PyGame
        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 48)

        # tablica znaczników 3x3 w formie listy
        self.markers = [None] * 9

    def draw(self, *args):
        """
        Rysuje okno gry

        :param args: lista obiektów do narysowania
        """
        background = (0, 0, 0)
        self.surface.fill(background)
        self.draw_net()
        self.draw_markers()
        self.draw_score()
        for drawable in args:
            drawable.draw_on(self.surface)

        # dopiero w tym miejscu następuje fatyczne rysowanie
        # w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać narysowane
        pygame.display.update()

    def draw_net(self):
        """
        Rysuje siatkę linii na planszy
        """
        color = (255, 255, 255)
        width = self.surface.get_width()
        for i in range(1, 3):
            pos = width / 3 * i
            # linia pozioma
            pygame.draw.line(self.surface, color, (0, pos), (width, pos), 1)
            # linia pionowa
            pygame.draw.line(self.surface, color, (pos, 0), (pos, width), 1)

    def player_move(self, x, y):
        """
        Ustawia na planszy znacznik gracza X na podstawie współrzędnych w pikselach
        """
        cell_size = self.surface.get_width() / 3
        x /= cell_size
        y /= cell_size
        self.markers[x + y * 3] = player_marker(True)

    def draw_markers(self):
        """
        Rysuje znaczniki graczy
        """
        box_side = self.surface.get_width() / 3
        for x in range(3):
            for y in range(3):
                marker = self.markers[x + y * 3]
                if not marker:
                    continue
                # zmieniamy współrzędne znacznika
                # na współrzędne w pikselach dla centrum pola
                center_x = x * box_side + box_side / 2
                center_y = y * box_side + box_side / 2

                self.draw_text(self.surface, marker, (center_x, center_y))

    def draw_text(self, surface,  text, center, color=(180, 180, 180)):
        """
        Rysuje wskazany tekst we wskazanym miejscu
        """
        text = self.font.render(text, True, color)
        rect = text.get_rect()
        rect.center = center
        surface.blit(text, rect)

    def draw_score(self):
        """
        Sprawdza czy gra została skończona i rysuje właściwy komunikat
        """
        if check_win(self.markers, True):
            score = u"Wygrałeś(aś)"
        elif check_win(self.markers, True):
            score = u"Przegrałeś(aś)"
        elif None not in self.markers:
            score = u"Remis!"
        else:
            return

        i = self.surface.get_width() / 2
        self.draw_text(self.surface, score, center=(i, i), color=(255, 26, 26))


class TicTacToeGame(object):
    """
    Łączy wszystkie elementy gry w całość.
    """

    def __init__(self, width, ai_turn=False):
        """
        Przygotowanie ustawień gry
        :param width: szerokość planszy mierzona w pikselach
        """
        pygame.init()
        # zegar którego użyjemy do kontrolowania szybkości rysowania
        # kolejnych klatek gry
        self.fps_clock = pygame.time.Clock()

        self.board = Board(width)
        self.ai = Ai(self.board)
        self.ai_turn = ai_turn

    def run(self):
        """
        Główna pętla gry
        """
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.board.draw()
            if self.ai_turn:
                self.ai.make_turn()
                self.ai_turn = False
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

            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if self.ai_turn:
                    # jeśli jeszcze trwa ruch komputera to ignorujemy zdarzenia
                    continue
                # pobierz aktualną pozycję kursora na planszy mierzoną w pikselach
                x, y = pygame.mouse.get_pos()
                self.board.player_move(x, y)
                self.ai_turn = True


class Ai(object):
    """
    Kieruje ruchami komputera na podstawie analizy położenia znaczników
    """
    def __init__(self, board):
        self.board = board

    def make_turn(self):
        """
        Wykonuje ruch komputera
        """
        if not None in self.board.markers:
            # brak dostępnych ruchów
            return
        logging.debug("Plansza: %s" % self.board.markers)
        move = self.next_move(self.board.markers)
        self.board.markers[move] = player_marker(False)

    @classmethod
    def next_move(cls, markers):
        """
        Wybierz następny ruch komputera na podstawie wskazanej planszy
        :param markers: plansza gry
        :return: index tablicy jednowymiarowe w której należy ustawić znacznik kółka
        """
        # pobierz dostępne ruchy wraz z oceną
        moves = cls.score_moves(markers, False)
        # wybierz najlepiej oceniony ruch
        score, move = max(moves, key=lambda m: m[0])
        logging.info("Dostępne ruchy: %s", moves)
        logging.info("Wybrany ruch: %s %s", move, score)
        return move

    @classmethod
    def score_moves(cls, markers, x_player):
        """
        Ocenia rekurencyjne możliwe ruchy

        Jeśli ruch jest zwycięstwem otrzymuje +1, jeśli przegraną -1
        lub 0 jeśli nie nie ma zwycięscy. Dla ruchów bez zwycięscy rekreacyjnie
        analizowane są kolejne ruchy a suma ich punktów jest wynikiem aktualnego
        ruchu.

        :param markers: plansza na podstawie której analizowane są następne ruchy
        :param x_player: True jeśli ruch dotyczy gracza X, False dla gracza O
        """
        # wybieramy wszystkie możliwe ruchy na podstawie wolnych pól
        available_moves = (i for i, m in enumerate(markers) if m is None)
        for move in available_moves:
            from copy import copy
            # tworzymy kopię planszy która na której testowo zostanie
            # wykonany ruch w celu jego późniejszej oceny
            proposal = copy(markers)
            proposal[move] = player_marker(x_player)

            # sprawdzamy czy ktoś wygrywa gracz którego ruch testujemy
            if check_win(proposal, x_player):
                # dodajemy punkty jeśli to my wygrywamy
                # czyli nie x_player
                score = -1 if x_player else 1
                yield score, move
                continue

            # ruch jest neutralny,
            # sprawdzamy rekurencyjne kolejne ruchy zmieniając gracza
            next_moves = list(cls.score_moves(proposal, not x_player))
            if not next_moves:
                yield 0, move
                continue

            # rozdzielamy wyniki od ruchów
            scores, moves = zip(*next_moves)
            # sumujemy wyniki możliwych ruchów, to będzie nasz wynik
            yield sum(scores), move


def player_marker(x_player):
    """
    Funkcja pomocnicza zwracająca znaczniki graczy
    :param x_player: True dla gracza X False dla gracza O
    :return: odpowiedni znak gracza
    """
    return "X" if x_player else "O"


def check_win(markers, x_player):
    """
    Sprawdza czy przekazany zestaw znaczników gry oznacza zwycięstwo wskazanego gracza

    :param markers: jednowymiarowa sekwencja znaczników w
    :param x_player: True dla gracza X False dla gracza O
    """
    win = [player_marker(x_player)] * 3
    seq = range(3)

    # definiujemy funkcję pomocniczą pobierającą znacznik
    # na podstawie współrzędnych x i y
    def marker(xx, yy):
        return markers[xx + yy * 3]

    # sprawdzamy każdy rząd
    for x in seq:
        row = [marker(x, y) for y in seq]
        if row == win:
            return True

    # sprawdzamy każdą kolumnę
    for y in seq:
        col = [marker(x, y) for x in seq]
        if col == win:
            return True

    # sprawdzamy przekątne
    diagonal1 = [marker(i, i) for i in seq]
    diagonal2 = [marker(i, abs(i-2)) for i in seq]
    if diagonal1 == win or diagonal2 == win:
        return True


# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = TicTacToeGame(300)
    game.run()

