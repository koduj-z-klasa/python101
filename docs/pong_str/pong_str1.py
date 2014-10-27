#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

# Przygotowanie zmiennych opisujących okno gry oraz obiekty gry i ich właściwości (paletki, piłeczka)
# Inicjacja modułu i obiektów Pygame'a

# inicjacja modułu pygame
pygame.init()

# liczba klatek na sekundę
FPS = 30
# obiekt zegara, który pozwala śledzić czas
fpsClock = pygame.time.Clock()

# szerokość i wysokość okna gry
OKNOGRY_SZER = 800
OKNOGRY_WYS = 400

# przygotowanie powierzchni do rysowania, czyli inicjacja okna gry
OKNOGRY = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)
# tytuł okna gry
pygame.display.set_caption('Prosty Pong')

# kolory wykorzystywane w grze, których składowe RGB zapisane są w tuplach
LT_BLUE = (230, 255, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
