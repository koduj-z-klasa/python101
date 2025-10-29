import random
import os
import json


def wczytaj_ustawienia(nick):
    nazwa_pliku = nick + '.txt'
    if os.path.isfile(nazwa_pliku):
        with open(nazwa_pliku) as plik:
            wiersz = plik.readline()
            dane = wiersz.strip().split(';')
            return dane
    return False


def pobierz_ustawienia(nick):
    error = False
    while True:
        try:
            n = int(input('Podaj liczbę losowanych liczb: '))
            maks = int(input('Podaj maksymalną losowaną liczbę: '))
            ile_typowan = int(input('Podaj liczbę typowań: '))
            if n >= maks or ile_typowan < 1:
                error = True
        except ValueError:
            error = True

        if error:
            print("Błędne dane!")
            continue  # dane niepoprawne
        else:
            break  # dane poprawne

    dane = [nick, n, maks, ile_typowan]
    return dane


def zapisz_ustawienia(nick, dane):
    nazwa_pliku = nick + '.txt'
    with open(nazwa_pliku, 'w') as plik:
        plik.write(';'.join(dane) + '\n')


def losuj_liczby(n, maks):
    """Funkcja losuje i zwraca listę n unikalnych liczb całkowitych w zakresie <0;maks>"""
    liczby = []
    while len(liczby) < n:
        liczba = random.randint(0, maks)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
    return liczby


def pobierz_typy(n, maks):
    """Funkcja pobiera od użytkownika typy wylosowanych liczb"""
    print(f'Wytypuj {n} z {maks} liczb: ')
    typy = set()
    error = False
    while len(typy) < n:
        try:
            typ = int(input('Podaj typ: '))
            if typ < 0 or typ > maks or typ in typy:
                error = True
        except ValueError:
            error = True

        if error:
            print('Błędne dane!')
            continue
        typy.add(typ)
    return typy

def wypisz_wyniki(liczby, typy):
    print()
    trafione = set(liczby) & typy
    if trafione:
        print(f'Trafione liczby: {trafione}')
        print(f'Liczba trafień {len(trafione)}')
    else:
        print('Brak trafień. Spróbuj jeszcze raz!')

    print()
    return len(trafione)


def wczytaj_dane(nick):
    """Funkcja odczytuje dane w formacie json z pliku"""
    nazwa_pliku = nick + '.json'
    dane = []
    if os.path.isfile(nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            dane = json.load(plik)
    return dane


def zapisz_dane(nick, dane):
    """Funkcja zapisuje dane w formacie json do pliku"""
    nazwa_pliku = nick + '.json'
    with open(nazwa_pliku, 'w') as plik:
        json.dump(dane, plik)
