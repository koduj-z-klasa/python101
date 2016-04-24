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
BLUE = (0, 0, 255)  # kolor paletki
PALETKA_1_POZ = (350, 360)  # początkowa pozycja zapisana w tupli
# utworzenie powierzchni paletki, wypełnienie jej kolorem,
paletka1 = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletka1.fill(BLUE)
# ustawienie prostokąta zawierającego paletkę w początkowej pozycji
paletka1_prost = paletka1.get_rect()
paletka1_prost.x = PALETKA_1_POZ[0]
paletka1_prost.y = PALETKA_1_POZ[1]

# piłka #################################################################
P_SZER = 20  # szerokość
P_WYS = 20  # wysokość
P_PREDKOSC_X = 6  # prędkość pozioma x
P_PREDKOSC_Y = 6  # prędkość pionowa y
GREEN = (0, 255, 0)  # kolor piłki
# utworzenie powierzchni piłki, narysowanie piłki i wypełnienie kolorem
pilka = pygame.Surface([P_SZER, P_WYS], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(pilka, GREEN, [0, 0, P_SZER, P_WYS])
# ustawienie prostokąta zawierającego piłkę w początkowej pozycji
pilka_prost = pilka.get_rect()
pilka_prost.x = OKNOGRY_SZER / 2
pilka_prost.y = OKNOGRY_WYS / 2

# ustawienia animacji ###################################################
FPS = 30  # liczba klatek na sekundę
fpsClock = pygame.time.Clock()  # zegar śledzący czas

# paletka ai ############################################################
RED = (255, 0, 0)
PALETKA_AI_POZ = (350, 20)  # początkowa pozycja zapisana w tupli
# utworzenie powierzchni paletki, wypełnienie jej kolorem,
paletkaAI = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
paletkaAI.fill(RED)
# ustawienie prostokąta zawierającego paletkę w początkowej pozycji
paletkaAI_prost = paletkaAI.get_rect()
paletkaAI_prost.x = PALETKA_AI_POZ[0]
paletkaAI_prost.y = PALETKA_AI_POZ[1]
# szybkość paletki AI
PREDKOSC_AI = 5

# komunikaty tekstowe ###################################################
# zmienne przechowujące punkty i funkcje wyświetlające punkty
PKT_1 = '0'
PKT_AI = '0'
fontObj = pygame.font.Font('freesansbold.ttf', 64)  # czcionka komunikatów


def drukuj_punkty1():
    tekst1 = fontObj.render(PKT_1, True, (0, 0, 0))
    tekst_prost1 = tekst1.get_rect()
    tekst_prost1.center = (OKNOGRY_SZER / 2, OKNOGRY_WYS * 0.75)
    oknogry.blit(tekst1, tekst_prost1)


def drukuj_punktyAI():
    tekstAI = fontObj.render(PKT_AI, True, (0, 0, 0))
    tekst_prostAI = tekstAI.get_rect()
    tekst_prostAI.center = (OKNOGRY_SZER / 2, OKNOGRY_WYS / 4)
    oknogry.blit(tekstAI, tekst_prostAI)

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
            myszaX, myszaY = event.pos  # współrzędne x, y kursora myszy

            # oblicz przesunięcie paletki gracza
            przesuniecie = myszaX - (PALETKA_SZER / 2)

            # jeżeli wykraczamy poza okno gry w prawo
            if przesuniecie > OKNOGRY_SZER - PALETKA_SZER:
                przesuniecie = OKNOGRY_SZER - PALETKA_SZER
            # jeżeli wykraczamy poza okno gry w lewo
            if przesuniecie < 0:
                przesuniecie = 0
            # zaktualizuj położenie paletki w poziomie
            paletka1_prost.x = przesuniecie

    # ruch piłki ########################################################
    # przesuń piłkę po obsłużeniu zdarzeń
    pilka_prost.move_ip(P_PREDKOSC_X, P_PREDKOSC_Y)

    # jeżeli piłka wykracza poza pole gry
    # z lewej/prawej – odwracamy kierunek ruchu poziomego piłki
    if pilka_prost.right >= OKNOGRY_SZER:
        P_PREDKOSC_X *= -1
    if pilka_prost.left <= 0:
        P_PREDKOSC_X *= -1

    if pilka_prost.top <= 0:  # piłka uciekła górą
        # P_PREDKOSC_Y *= -1  # odwracamy kierunek ruchu pionowego piłki
        pilka_prost.x = OKNOGRY_SZER / 2  # więc startuję ze środka
        pilka_prost.y = OKNOGRY_WYS / 2
        PKT_1 = str(int(PKT_1) + 1)

    if pilka_prost.bottom >= OKNOGRY_WYS:  # piłka uciekła dołem
        pilka_prost.x = OKNOGRY_SZER / 2  # więc startuję ze środka
        pilka_prost.y = OKNOGRY_WYS / 2
        PKT_AI = str(int(PKT_AI) + 1)

    # AI (jak gra komputer)
    # jeżeli piłka ucieka na prawo, przesuń za nią paletkę
    if pilka_prost.centerx > paletkaAI_prost.centerx:
        paletkaAI_prost.x += PREDKOSC_AI
    # w przeciwnym wypadku przesuń w lewo
    elif pilka_prost.centerx < paletkaAI_prost.centerx:
        paletkaAI_prost.x -= PREDKOSC_AI

    # jeżeli piłka dotknie paletki AI, skieruj ją w przeciwną stronę
    if pilka_prost.colliderect(paletkaAI_prost):
        P_PREDKOSC_Y *= -1
        # uwzględnij nachodzenie paletki na piłkę (przysłonięcie)
        pilka_prost.top = paletkaAI_prost.bottom

    # jeżeli piłka dotknie paletki gracza, skieruj ją w przeciwną stronę
    if pilka_prost.colliderect(paletka1_prost):
        P_PREDKOSC_Y *= -1
        # zapobiegaj przysłanianiu paletki przez piłkę
        pilka_prost.bottom = paletka1_prost.top

    # rysowanie obiektów ################################################
    oknogry.fill(LT_BLUE)  # wypełnienie okna gry kolorem

    drukuj_punkty1()  # wyświetl punkty gracza
    drukuj_punktyAI()  # wyświetl punkty AI

    # narysuj w oknie gry paletki
    oknogry.blit(paletka1, paletka1_prost)
    oknogry.blit(paletkaAI, paletkaAI_prost)

    # narysuj w oknie piłkę
    oknogry.blit(pilka, pilka_prost)

    # zaktualizuj okno i wyświetl
    pygame.display.update()

    # zaktualizuj zegar po narysowaniu obiektów
    fpsClock.tick(FPS)

# KONIEC
