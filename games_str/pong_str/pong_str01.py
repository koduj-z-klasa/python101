#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

# inicjacja modułu pygame
pygame.init()

# szerokość i wysokość okna gry
OKNOGRY_SZER = 800
OKNOGRY_WYS = 400
# kolor okna gry, składowe RGB zapisane w tupli
LT_BLUE = (230, 255, 255)

# powierzchnia do rysowania, czyli inicjacja pola gry
oknogry = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)
# tytuł okna gry
pygame.display.set_caption('Prosty Pong')

# pętla główna programu
while True:
    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # rysowanie obiektów
    oknogry.fill(LT_BLUE)  # kolor okna gry

    # zaktualizuj okno i wyświetl
    pygame.display.update()

# KONIEC
