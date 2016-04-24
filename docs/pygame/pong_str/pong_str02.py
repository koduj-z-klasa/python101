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

# powierzchnia do rysowania, czyli inicjacja okna gry
oknogry = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)
# tytuł okna gry
pygame.display.set_caption('Prosty Pong')

# paletka gracza #########################################################
PALETKA_SZER = 100  # szerokość
PALETKA_WYS = 20  # wysokość
BLUE = (0, 0, 255)  # kolor wypełnienia
PALETKA_1_POZ = (350, 360)  # początkowa pozycja zapisana w tupli
# utworzenie powierzchni paletki, wypełnienie jej kolorem,
paletka1 = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka1.fill(BLUE)
# ustawienie prostokąta zawierającego paletkę w początkowej pozycji
paletka1_prost = paletka1.get_rect()
paletka1_prost.x = PALETKA_1_POZ[0]
paletka1_prost.y = PALETKA_1_POZ[1]

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

    # narysuj w oknie gry paletki
    oknogry.blit(paletka1, paletka1_prost)

    # zaktualizuj okno i wyświetl
    pygame.display.update()

# KONIEC
