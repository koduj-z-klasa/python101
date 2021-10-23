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

# pętla główna programu
while True:
    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # przechwyć ruch myszy
        if event.type == MOUSEMOTION: 
            # pobierz współrzędne x, y kursora myszy
            myszaX, myszaY = event.pos
            
            # przesunięcie paletki gracza
            przesuniecie = myszaX-(PALETKA_SZER/2)
            
            # jeżeli wykraczamy poza okno gry w prawo
            if przesuniecie > OKNOGRY_SZER-PALETKA_SZER:
                przesuniecie = OKNOGRY_SZER-PALETKA_SZER
            # jeżeli wykraczamy poza okno gry w lewo
            if przesuniecie < 0:
                przesuniecie = 0
            paletka1_prost.x = przesuniecie
    
    # AI (jak gra komputer)
    # jeżeli środek piłki jest większy niż środek paletki AI
    # przesuń w prawo paletkę z ustawioną prędkością
    if pilka_prost.centerx > paletka2_prost.centerx:
        paletka2_prost.x += AI_PREDKOSC
    # w przeciwnym wypadku przesuń w lewo
    elif pilka_prost.centerx < paletka2_prost.centerx:
        paletka2_prost.x -= AI_PREDKOSC

    # przesuń piłkę po zdarzeniu
    pilka_prost.x += PILKA_PREDKOSC_X
    pilka_prost.y += PILKA_PREDKOSC_Y
    
    # Sprawdzamy kolizje piłki z obiektami
    # Ściany: jeżeli piłka wykracza poza okn0 z lewej lub prawej strony odbij ją od ściany
    if pilka_prost.right >= OKNOGRY_SZER:
        PILKA_PREDKOSC_X *= -1
    if pilka_prost.left <= 0:
        PILKA_PREDKOSC_X *= -1
        
    # Piłka i paletki

    # Jeżeli piłka dotknie paletki, skieruj ją w przeciwną stronę
    if pilka_prost.colliderect(paletka1_prost):
        PILKA_PREDKOSC_Y *= -1
        # uwzględnij nachodzenie paletki na piłkę (przysłonięcie)
        pilka_prost.bottom = paletka1_prost.top
        
    if pilka_prost.colliderect(paletka2_prost):
        PILKA_PREDKOSC_Y *= -1
        # uwzględnij nachodzenie paletki na piłkę (przysłonięcie)
        pilka_prost.top = paletka2_prost.bottom
        
    # jeżeli piłka wyszła poza pole gry u góry lub z dołu ustaw domyślną pozycję piłki
    # i przypisz punkt odpowiedniemu graczowi
    if pilka_prost.top <= 0:
        pilka_prost.x = OKNOGRY_SZER/2
        pilka_prost.y = OKNOGRY_WYS/2
        GRACZ_1_PKT = str(int(GRACZ_1_PKT)+1)
        
    if pilka_prost.bottom >= OKNOGRY_WYS:
        pilka_prost.x = OKNOGRY_SZER/2
        pilka_prost.y = OKNOGRY_WYS/2
        GRACZ_2_PKT = str(int(GRACZ_2_PKT)+1)
            
    # Rysowanie obiektów
    OKNOGRY.fill(LT_BLUE) # kolor okna gry
    
    drukuj_punkty_p1() # wyświetl punkty komputera
    drukuj_punkty_p2() # wyświetl punkty gracza
    
    # narysuj w oknie gry paletki
    OKNOGRY.blit(paletka1_obr, paletka1_prost)
    OKNOGRY.blit(paletka2_obr, paletka2_prost)

    # narysuj w oknie piłkę
    OKNOGRY.blit(pilka_obr, pilka_prost)

    # zaktualizuj okno i wyświetl
    pygame.display.update()

    # zaktualizuj zegar po narysowaniu obiektów
    fpsClock.tick(FPS)

#KONIEC
