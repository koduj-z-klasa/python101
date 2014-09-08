# coding=utf-8
# Copyright 2013 Janusz Skonieczny

import pygame
import pygame.locals
import sys


class Movable(object):
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


class Ball(Movable):

    def __init__(self, width, height, x, y, color=(255, 0, 0), x_speed=3, y_speed=3):
        super(Ball, self).__init__(width, height, x, y, color)
        self.x_speed = x_speed
        self.y_speed = y_speed

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

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1


class Paddle(Movable):

    def __init__(self, width, height, x, y, color=(0, 255, 0), ball=None):
        super(Paddle, self).__init__(width, height, x, y, color)
        self.ball = ball

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


class Ai(object):

    def __init__(self, paddle, ball, speed=4):
        self.speed = speed
        self.ball = ball
        self.paddle = paddle

    def move(self):
        x = self.ball.rect.x
        if self.paddle.center_x > x:
            self.paddle.rect.x -= self.speed
        else:
            self.paddle.rect.x += self.speed


class Board(object):

    def __init__(self, width, height):
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Simple Pong')

    def draw(self, *args):
        self.surface.fill((230, 255, 255))
        for surface, rect in args:
            self.surface.blit(surface, rect)
        pygame.display.update()


class PongGame(object):

    def __init__(self, width, height):
        super(PongGame, self).__init__()
        self.board = Board(width, height)
        self.ball = Ball(10, 10, width/2, height/2)
        self.player1 = Paddle(50, 10, 350, 20)
        self.player2 = Paddle(50, 10, 350, 360)
        self.ai = Ai(self.player2, self.ball)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.handle_events()
            self.ai.move()
            self.ball.move(self.board, (self.player1, self.ai.paddle))
            self.board.draw(
                (self.player1.surface, self.player1.rect),
                (self.player2.surface, self.player2.rect),
                (self.ball.surface, self.ball.rect),
            )

            self.board.surface.blit(self.player2.surface, self.player2.rect)
            self.board.surface.blit(self.ball.surface, self.ball.rect)
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.locals.MOUSEMOTION:
                self.player1.move(self.board, event.pos)

if __name__ == "__main__":
    game = PongGame(800, 400)
    game.run()
