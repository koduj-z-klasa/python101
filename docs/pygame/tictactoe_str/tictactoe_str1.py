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
