#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
import random
from pygame.locals import *  # udostępnienie nazw metod z locals

# inicjacja modułu pygame
pygame.init()

# przygotowanie powierzchni do rysowania, czyli inicjacja okna gry
OKNOGRY = pygame.display.set_mode((150, 150), 0, 32)
# tytuł okna gry
pygame.display.set_caption('Kółko i krzyżyk')

# lista opisująca stan pola gry, 0 - pole puste, 1 - gracz, 2 - komputer
POLE_GRY = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

RUCH = 1  # do kogo należy ruch: 1 – gracz, 2 – komputer
WYGRANY = 0  # wynik gry: 0 - nikt, 1 - gracz, 2 - komputer, 3 - remis
WYGRANA = False

# rysowanie planszy gry, czyli linii oddzielających pola


def rysuj_plansze():
    for i in range(0, 3):  # x
        for j in range(0, 3):  # y
            # argumenty: powierzchnia, kolor, x,y, w,h, grubość linii
            pygame.draw.rect(OKNOGRY, (255, 255, 255),
                             Rect((j * 50, i * 50), (50, 50)), 1)

# narysuj kółka


def rysuj_pole_gry():
    for i in range(0, 3):
        for j in range(0, 3):
            pole = i * 3 + j  # zmienna pole przyjmuje wartości od 0-8
            # x i y określają środki kolejnych pól,
            # a więc wartości: 25,25, 25,75 25,125 75,25 itd.
            x = j * 50 + 25
            y = i * 50 + 25

            if POLE_GRY[pole] == 1:
                # rysuj kółko gracza
                pygame.draw.circle(OKNOGRY, (0, 0, 255), (x, y), 10)
            elif POLE_GRY[pole] == 2:
                # rysuj kółko komputera
                pygame.draw.circle(OKNOGRY, (255, 0, 0), (x, y), 10)
