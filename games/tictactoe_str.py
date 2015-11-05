#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, random
from pygame.locals import * #udostępnienie nazw metod z locals

# inicjacja modułu pygame
pygame.init()

# przygotowanie powierzchni do rysowania, czyli inicjacja okna gry
OKNOGRY = pygame.display.set_mode((150, 150), 0, 32)
# tytuł okna gry
pygame.display.set_caption('Kółko i krzyżyk')

# lista opisująca stan pola gry, 0 - pole puste, 1 - gracz, 2 - komputer
POLE_GRY = [0,0,0,
            0,0,0,
            0,0,0]

RUCH = 1 # do kogo należy ruch: 1 – gracz, 2 – komputer
WYGRANY = 0 # wynik gry: 0 - nikt, 1 - gracz, 2 - komputer, 3 - remis
WYGRANA = False

# rysowanie planszy gry, czyli linii oddzielających pola
def rysuj_plansze():
    for i in range(0,3):#x
        for j in range(0,3):#y
            # argumenty: powierzchnia, kolor, x,y, w,h, grubość linii
            pygame.draw.rect(OKNOGRY, (255,255,255), Rect((j*50,i*50),(50,50)), 1)

# narysuj kółka
def rysuj_pole_gry():
    for i in range(0,3):
        for j in range(0,3):
            pole = i*3+j #zmienna pole przyjmuje wartości od 0-8
            # x i y określają środki kolejnych pól,
            # a więc wartości: 25,25, 25,75 25,125 75,25 itd.
            x = j*50+25
            y = i*50+25

            if POLE_GRY[pole] == 1:
                pygame.draw.circle(OKNOGRY,(0,0,255), (x,y),10)#rysuj kółko gracza
            elif POLE_GRY[pole] == 2:
                pygame.draw.circle(OKNOGRY,(255,0,0), (x,y),10)#rysuj kółko komputera

# postaw kółko lub krzyżyk (w tej wersji też kółko, ale w innym kolorze :-))
def postaw_znak(pole, RUCH):
    if POLE_GRY[pole] == 0:
        if RUCH == 1: # ruch gracza
            POLE_GRY[pole] = 1
            return 2
        elif RUCH == 2: # ruch komputera
            POLE_GRY[pole] = 2
            return 1

    return RUCH

# funkcja pomocnicza sprawdzająca, czy komputer może wygrać, czy powinien
# blokować gracza, czy może wygrał komputer lub gracz
def sprawdz_pola(uklad, wygrany = None):
    wartosc = None;
    # lista wielowymiarowa, której elementami są inne listy zagnieżdżone
    POLA_INDEKSY = [ # trójki pól planszy do sprawdzania
        [0,1,2], [3,4,5], [6,7,8], # indeksy pól w poziomie (wiersze)
        [0,3,6], [1,4,7], [2,5,8], # indeksy pól w pionie (kolumny)
        [0,4,8], [2,4,6] # indeksy pól na skos (przekątne)
    ]

    for lista in POLA_INDEKSY:
        kol = [] # lista pomocnicza
        for ind in lista:
            kol.append(POLE_GRY[ind]) # zapisz wartość odczytaną z POLE_GRY
        if (kol in uklad): # jeżeli znalazłeś układ wygrywający lub blokujący
            # zwróć wygranego (1,2) lub indeks pola do zaznaczenia
            wartosc = wygrany if wygrany else lista[kol.index(0)]

    return wartosc

# ruchy komputera
def ai_ruch(RUCH):
    pole = None # które pole powinien zaznaczyć komputer

    # listy wielowymiarowe, których elementami są inne listy zagnieżdżone
    uklady_wygrywam = [[2, 2, 0], [2, 0, 2], [0, 2, 2]]
    uklady_blokuje = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]

    # sprawdź, czy komputer może wygrać
    pole = sprawdz_pola(uklady_wygrywam)
    if pole is not None:
        return postaw_znak(pole, RUCH)

    # jeżeli komputer nie może wygrać, blokuj gracza
    pole = sprawdz_pola(uklady_blokuje)
    if pole is not None:
        return postaw_znak(pole, RUCH)

    # jeżeli nie można wygrać i gracza nie trzeba blokować, wylosuj pole
    while pole == None:
        pos = random.randrange(0,9) #wylosuj wartość od 0 do 8
        if POLE_GRY[pos] == 0:
            pole = pos

    return postaw_znak(pole, RUCH)

# sprawdź, kto wygrał, a może jest remis?
def kto_wygral():
    # układy wygrywające dla gracza i komputera
    uklad_gracz = [[1,1,1]]
    uklad_komp = [[2,2,2]]

    WYGRANY = sprawdz_pola(uklad_gracz,1) # czy wygrał gracz?
    if not WYGRANY: # jeżeli gracz nie wygrywa
        WYGRANY = sprawdz_pola(uklad_komp,2) # czy wygrał komputer?

    # sprawdź remis
    if 0 not in POLE_GRY and WYGRANY not in [1,2]:
        WYGRANY = 3

    return WYGRANY

# funkcja wyświetlająca komunikat końcowy
# tworzy nowy obrazek z tekstem, pobiera jego prostokątny obszar
# pozycjonuje go i rysuje w oknie gry
def drukuj_wynik(WYGRANY):
    fontObj = pygame.font.Font('freesansbold.ttf', 16)
    if WYGRANY == 1:
        tekst = u'Wygrał gracz!'
    elif WYGRANY == 2:
        tekst = u'Wygrał komputer!'
    elif WYGRANY == 3:
        tekst = 'Remis!'
    tekst_obr = fontObj.render(tekst, True, (20,255,20))
    tekst_prost = tekst_obr.get_rect()
    tekst_prost.center = (75, 75)
    OKNOGRY.blit(tekst_obr, tekst_prost)

# pętla główna programu
while True:
    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if WYGRANA == False:
            if RUCH == 1:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1: # jeżeli naciśnięto pierwszy przycisk
                        mouseX, mouseY = event.pos # rozpakowanie tupli
                        pole = ((mouseY/50)*3)+(mouseX/50) # wylicz indeks klikniętego pola
                        RUCH = postaw_znak(pole, RUCH)
            elif RUCH == 2:
                RUCH = ai_ruch(RUCH)

            WYGRANY = kto_wygral()
            if WYGRANY != None:
                WYGRANA = True


    OKNOGRY.fill((0,0,0))# definicja koloru powierzchni w RGB
    rysuj_plansze()
    rysuj_pole_gry()
    if WYGRANA:
        drukuj_wynik(WYGRANY)
    pygame.display.update()
