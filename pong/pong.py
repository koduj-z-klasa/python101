# coding=utf-8

import pygame
import pygame.locals
import sys


class Board(object):
    """
    Plansza do gry.
    """
    def __init__(self, width, height):
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Simple Pong')

    def draw(self, *args):
        background = (230, 255, 255)
        self.surface.fill(background)
        for surface, rect in args:
            self.surface.blit(surface, rect)
        pygame.display.update()


class PongGame(object):
    """
    Łączy wszystkie elementy gry w całość.
    """
    def __init__(self, width, height):
        super(PongGame, self).__init__()
        self.board = Board(width, height)
        self.clock = pygame.time.Clock()
        self.ball = Ball(10, 10, width/2, height/2)
        self.player1 = Racket(50, 10, width/2, height/2)

    def run(self):
        while True:
            self.handle_events()
            self.ball.move(self.board, (self.player1,))
            self.board.draw(
                (self.ball.surface, self.ball.rect),
                (self.player1.surface, self.player1.rect),
            )
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.locals.MOUSEMOTION:
                self.player1.move(self.board, event.pos)

class Drawable(object):
    def __init__(self, width, height, x, y, color=(0, 255, 0)):
        self.width = width
        self.height = height
        self.color = color
        self.surface = pygame.Surface([width, height], pygame.SRCALPHA, 32).convert_alpha()
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.draw()

    @property
    def center_x(self):
        return self.rect.x + self.surface.get_width() / 2


class Ball(Drawable):
    """
    Piłeczka, porusza się z wektorem prędkości,
    odbija się gdy uderzy w jakiś inny obiekt lub ściany boczne.
    """
    def __init__(self, width, height, x, y, color=(255, 0, 0), x_speed=3, y_speed=3):
        super(Ball, self).__init__(width, height, x, y, color)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.start_x = x
        self.start_y = y

    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])

    def move(self, board, rackets):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        for r in rackets:
            if self.rect.colliderect(r.rect):
                self.bounce_y()

        if self.rect.x < 0 or self.rect.x > board.surface.get_width():
            self.bounce_x()

        if self.rect.y < 0 or self.rect.y > board.surface.get_height():
            self.bounce_y()

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

    def reset(self):
        self.bounce_y()
        self.rect.x = self.start_x
        self.rect.y = self.start_y


class Racket(Drawable):
    """
    Rakietka, porusza się w osi X nie wychodząc poza brzegi planszy.
    """
    def __init__(self, width, height, x, y, color=(0, 255, 0)):
        super(Racket, self).__init__(width, height, x, y, color)

    def draw(self):
        self.surface.fill(self.color)

    def move(self, board, position):
        x, y = position
        x = x - self.width
        max_x = board.surface.get_width()
        if x < 0:
            x = 0
        elif x + self.width > max_x:
            x = max_x
        self.rect.x = x

game = PongGame(800, 400)
game.run()


