#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, random
from pygame.locals import * #udostępnienie nazw metod z locals

# inicjacja modułu pygame
pygame.init()

# szerokość i wysokość okna gry
OKNOGRY_SZER = 800
OKNOGRY_WYS = 400

# przygotowanie powierzchni do rysowania, czyli inicjacja okna gry
OKNOGRY = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)
# tytuł okna gry
pygame.display.set_caption('Gra o życie')

# rozmiar komórki
ROZ_KOM = 10
# ilość komórek w poziomie i pionie
KOM_POZIOM = OKNOGRY_SZER/ROZ_KOM
KOM_PION = OKNOGRY_WYS/ROZ_KOM

# wartości oznaczające komórki "martwe" i "żywe"
KOM_MARTWA = 0
KOM_ZYWA = 1

# lista opisująca stan pola gry, 0 - komórki martwe, 1 - komórki żywe
# na początku tworzymy listę zawierającą KOM_POZIOM zer
POLE_GRY = [KOM_MARTWA] * KOM_POZIOM
# rozszerzamy listę o listy zagnieżdżone, otrzymujemy więc listę dwuwymiarową
for i in range(KOM_POZIOM):
    POLE_GRY[i] = [KOM_MARTWA] * KOM_PION

# przygotowanie następnej generacji komórek, czyli zaktualizowanego POLA_GRY
def przygotuj_populacje(polegry):
    # na początku tworzymy 2-wymiarową listę wypełnioną zerami
    nast_gen = [KOM_MARTWA] * KOM_POZIOM
    for i in range(KOM_POZIOM):
        nast_gen[i] = [KOM_MARTWA] * KOM_PION

    # iterujemy po wszystkich komórkach
    for y in range(KOM_PION):
        for x in range(KOM_POZIOM):

            # zlicz populację (żywych komórek) wokół komórki
            populacja = 0
            # wiersz 1
            try:
                if polegry[x-1][y-1] == KOM_ZYWA: populacja += 1
            except IndexError:pass
            try:
                if polegry[x][y-1] == KOM_ZYWA: populacja += 1
            except IndexError:pass
            try:
                if polegry[x+1][y-1] == KOM_ZYWA: populacja += 1
            except IndexError:pass

            # wiersz 2
            try:
                if polegry[x-1][y] == KOM_ZYWA: populacja += 1
            except IndexError:pass
            try:
                if polegry[x+1][y] == KOM_ZYWA: populacja += 1
            except IndexError:pass

            # wiersz 3
            try:
                if polegry[x-1][y+1] == KOM_ZYWA: populacja += 1
            except IndexError:pass
            try:
                if polegry[x][y+1] == KOM_ZYWA: populacja += 1
            except IndexError:pass
            try:
                if polegry[x+1][y+1] == KOM_ZYWA: populacja += 1
            except IndexError:pass

            # "niedoludnienie" lub przeludnienie = śmierć komórki
            if polegry[x][y] == KOM_ZYWA and (populacja < 2 or populacja > 3):
                nast_gen[x][y] = KOM_MARTWA
            # życie trwa
            elif polegry[x][y] == KOM_ZYWA and (populacja == 3 or populacja == 2):
                nast_gen[x][y] = KOM_ZYWA
            # nowe życie
            elif polegry[x][y] == KOM_MARTWA and populacja == 3:
                nast_gen[x][y] = KOM_ZYWA

    # zwróć nowe polegry z następną generacją komórek
    return nast_gen

# rysowanie komórek (kwadratów) żywych
def rysuj_populacje():
    for y in range(KOM_PION):
        for x in range(KOM_POZIOM):
            if POLE_GRY[x][y] == KOM_ZYWA:
                pygame.draw.rect(OKNOGRY, (255,255,255), Rect((x*ROZ_KOM,y*ROZ_KOM),(ROZ_KOM,ROZ_KOM)),1)

# zmienne sterujące wykorzystywane w pętli głównej
zycie_trwa = False
przycisk_wdol = False

# pętla główna programu
while True:
    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_RETURN:
            zycie_trwa = True

        if zycie_trwa == False:
            if event.type == MOUSEBUTTONDOWN:
                przycisk_wdol = True
                przycisk_typ = event.button

            if event.type == MOUSEBUTTONUP:
                przycisk_wdol = False

            if przycisk_wdol:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x = mouse_x / ROZ_KOM
                mouse_y = mouse_y / ROZ_KOM
                # lewy przycisk myszy ożywia
                if przycisk_typ == 1: POLE_GRY[mouse_x][mouse_y] = KOM_ZYWA
                # prawy przycisk myszy uśmierca
                if przycisk_typ == 3: POLE_GRY[mouse_x][mouse_y] = KOM_MARTWA

    if zycie_trwa == True:
        POLE_GRY = przygotuj_populacje(POLE_GRY)

    OKNOGRY.fill((0,0,0)) # ustaw kolor okna gry
    rysuj_populacje()
    pygame.display.update()
    pygame.time.delay(100)
