# coding=utf-8
# Copyright 2013 Janusz Skonieczny

"""
Klasyczna gra w odbijanie piłeczki napisana z użyciem biblioteki PyGame.


Na co warto zwrócić uwagę
- wykorzystanie __init__ do utworzenie instancji obiektów (ich właściwości)
- dziedziczenie i implementacja metod "wirtualnych", a raczej brakujących
- wykorzystanie *args jako zamiast jednego parametru z kolekcją

Co można poprawić
- piłeczka wychodzi poza prawą krawędź planszy
- różne poziomy sprawności AI (aktualnie komputer zawsze wygrywa)
- zabezpieczenie by piłeczka nie zazębiała się z rakietką
- zmiana wektora prędkości w zależności od pędu rakietki
- dwie piłeczki

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

        :param width:
        :param height:
        """
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Simple Pong')

    def draw(self, *args):
        """
        Rysuje okno gry

        :param args: lista obiektów do narysowania
        """
        background = (230, 255, 255)
        self.surface.fill(background)
        for drawable in args:
            drawable.draw_on(self.surface)

        # dopiero w tym miejscu następuje fatyczne rysowanie
        # w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać narysowane
        pygame.display.update()


class PongGame(object):
    """
    Łączy wszystkie elementy gry w całość.
    """

    def __init__(self, width, height):
        pygame.init()
        self.board = Board(width, height)
        # zegar którego użyjemy do kontrolowania szybkości rysowania
        # kolejnych klatek gry
        self.fps_clock = pygame.time.Clock()
        self.ball = Ball(20, 20, width/2, height/2)
        self.player1 = Racket(80, 20, width/2 - 40, height - 40)
        self.player2 = Racket(80, 20, width/2 - 40, 20, color=(0, 0, 0))
        self.ai = Ai(self.player2, self.ball)
        self.judge = Judge(self.board, self.ball, self.player2, self.ball)

    def run(self):
        """
        Główna pętla programu
        """
        while not self.handle_events():
            self.ball.move(self.board, self.player1, self.player2)
            self.board.draw(
                self.ball,
                self.player1,
                self.player2,
                self.judge,
            )
            self.ai.move()
            self.fps_clock.tick(30)

    def handle_events(self):
        """
        Obsługa zdarzeń systemowych, tutaj zinterpretujemy np. ruchy myszką
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.locals.MOUSEMOTION:
                # myszka steruje ruchem pierwszego gracza
                x, y = event.pos
                self.player1.move(x)


class Drawable(object):
    """
    Klasa bazowa dla rysowanych obiektów
    """

    def __init__(self, width, height, x, y, color=(0, 255, 0)):
        self.width = width
        self.height = height
        self.color = color
        self.surface = pygame.Surface([width, height], pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.surface.get_rect(x=x, y=y)

    def draw_on(self, surface):
        surface.blit(self.surface, self.rect)


class Ball(Drawable):
    """
    Piłeczka, sama kontroluje swoją prędkość i kierunek poruszania się.
    """
    def __init__(self, width, height, x, y, color=(255, 0, 0), x_speed=3, y_speed=3):
        super(Ball, self).__init__(width, height, x, y, color)
        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.start_x = x
        self.start_y = y

    def bounce_y(self):
        """
        Odwraca wektor prędkości w osi Y
        """
        self.y_speed *= -1

    def bounce_x(self):
        """
        Odwraca wektor prędkości w osi X
        """
        self.x_speed *= -1

    def reset(self):
        """
        Ustawia piłeczkę w położeniu początkowym i odwraca wektor prędkości w osi Y
        """
        self.rect.x, self.rect.y = self.start_x, self.start_y
        self.bounce_y()

    def move(self, board, *args):
        """
        Przesuwa piłeczkę o wektor prędkości
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x < 0 or self.rect.x > board.surface.get_width():
            self.bounce_x()

        if self.rect.y < 0 or self.rect.y > board.surface.get_height():
            self.bounce_y()

        for racket in args:
            if self.rect.colliderect(racket.rect):
                self.bounce_y()


class Racket(Drawable):
    """
    Rakietka, porusza się w osi X z ograniczeniem prędkości.
    """

    def __init__(self, width, height, x, y, color=(0, 255, 0), max_speed=10):
        super(Racket, self).__init__(width, height, x, y, color)
        self.max_speed = max_speed
        self.surface.fill(color)

    def move(self, x):
        """
        Przesuwa rakietkę w wyznaczone miejsce.
        """
        delta = x - self.rect.x
        if abs(delta) > self.max_speed:
            delta = self.max_speed if delta > 0 else -self.max_speed
        self.rect.x += delta


class Ai(object):
    """
    Przeciwnik, steruje swoją rakietką na podstawie obserwacji piłeczki.
    """
    def __init__(self, racket, ball):
        self.ball = ball
        self.racket = racket

    def move(self):
        x = self.ball.rect.centerx
        self.racket.move(x)


class Judge(object):
    """
    Sędzia gry
    """

    def __init__(self, board, ball, *args):
        self.ball = ball
        self.board = board
        self.rackets = args
        self.score = [0, 0]

        # Przed pisaniem tekstów, musimy zainicjować mechanizmy wyboru fontów PyGame
        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 64)

    def update_score(self, board_height):
        """
        Jeśli trzeba przydziela punkty i ustawia piłeczkę w początkowym położeniu.
        """
        if self.ball.rect.y < 0:
            self.score[0] += 1
            self.ball.reset()
        elif self.ball.rect.y > board_height:
            self.score[1] += 1
            self.ball.reset()

    def draw_text(self, surface,  text, x, y):
        """
        Rysuje wskazany tekst we wskazanym miejscu
        """
        text = self.font.render(text, True, (150, 150, 150))
        rect = text.get_rect()
        rect.center = x, y
        surface.blit(text, rect)

    def draw_on(self, surface):
        """
        Aktualizuje i rysuje wyniki
        """
        height = self.board.surface.get_height()
        self.update_score(height)

        width = self.board.surface.get_width()
        self.draw_text(surface, "Player: {}".format(self.score[0]), width/2, height * 0.3)
        self.draw_text(surface, "Computer: {}".format(self.score[1]), width/2, height * 0.7)


# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = PongGame(800, 400)
    game.run()
