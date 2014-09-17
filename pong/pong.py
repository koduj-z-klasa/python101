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

board = Board(800, 400)
board.draw()



