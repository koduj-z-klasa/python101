import os


def pobierz_dane_1(plikcsv):
    dane = []  # deklarujemy pustą listę
    if os.path.isfile(plikcsv):
        # otwieramy plik do odczytu
        with open(plikcsv) as plik:
            for linia in plik:
                dane.append(linia.strip().split(","))
    else:
        print("Plik z danymi", plikcsv, "nie istnieje!")

    return dane


import csv


def pobierz_dane_2(plikcsv):
    dane = []  # deklarujemy pustą listę
    if os.path.isfile(plikcsv):
        # otwieramy plik do odczytu
        with open(plikcsv) as plik:
            for linia in csv.reader(plik, delimiter=','):
                dane.append(linia)
    return dane


print(pobierz_dane_1("uczniowie.csv"))
print(pobierz_dane_2("uczniowie.csv"))
