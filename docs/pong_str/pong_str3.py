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

# szerokość, wysokość i pozycja paletek
PALETKA_SZER = 100
PALETKA_WYS = 20

# Inicjacja PALETEK:
# utworzenie powierzchni dla obrazka, wypełnienie jej kolorem,
# pobranie prostokątnego obszaru obrazka i ustawienie go na wstępnej pozycji

PALETKA_1_POZ = (350, 360) # początkowa pozycja paletki gracza
paletka1_obr = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka1_obr.fill(BLUE)
paletka1_prost = paletka1_obr.get_rect()
paletka1_prost.x = PALETKA_1_POZ[0]
paletka1_prost.y = PALETKA_1_POZ[1]

PALETKA_2_POZ = (350, 20) # początkowa pozycja paletki komputera
paletka2_obr = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka2_obr.fill(RED)
paletka2_prost = paletka2_obr.get_rect()
paletka2_prost.x = PALETKA_2_POZ[0]
paletka2_prost.y = PALETKA_2_POZ[1]

# szybkość paletki 1 (AI - ang. artificial inteligence, sztuczna inteligencja), czyli komputera
AI_PREDKOSC = 3

# Inicjacja PIŁKI
# szerokość, wysokość, prędkość pozioma (x) i pionowa (y) PIŁKI
# utworzenie powierzchni dla piłki, narysowanie na niej koła, ustawienie pozycji początkowej
PILKA_SZER = 20
PILKA_WYS = 20
PILKA_PREDKOSC_X = 6
PILKA_PREDKOSC_Y = 6
pilka_obr = pygame.Surface([PILKA_SZER, PILKA_WYS], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(pilka_obr, GREEN, [0, 0, PILKA_SZER, PILKA_WYS])
pilka_prost = pilka_obr.get_rect()
pilka_prost.x = OKNOGRY_SZER/2
pilka_prost.y = OKNOGRY_WYS/2

# Rysowanie komunikatów tekstowych
# ustawienie początkowych wartości liczników punktów
# utworzenie obiektu czcionki z podanego pliku o podanym rozmiarze
GRACZ_1_PKT = '0'
GRACZ_2_PKT = '0'
fontObj = pygame.font.Font('freesansbold.ttf', 64)

# funkcje wyświetlające punkty gracza
# tworzą nowy obrazek z tekstem, pobierają prostokątny obszar obrazka,
# pozycjonują go i rysują w oknie gry

def drukuj_punkty_p1():
    tekst_obr1 = fontObj.render(GRACZ_1_PKT, True, (0,0,0))
    tekst_prost1 = tekst_obr1.get_rect()
    tekst_prost1.center = (OKNOGRY_SZER/2, OKNOGRY_WYS*0.75)
    OKNOGRY.blit(tekst_obr1, tekst_prost1)

def drukuj_punkty_p2():
    tekst_obr2 = fontObj.render(GRACZ_2_PKT, True, (0,0,0))
    tekst_prost2 = tekst_obr2.get_rect()
    tekst_prost2.center = (OKNOGRY_SZER/2, OKNOGRY_WYS/4)
    OKNOGRY.blit(tekst_obr2, tekst_prost2)
