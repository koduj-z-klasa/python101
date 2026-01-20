import numpy as np
import random
import matplotlib.pyplot as plt
import csv
import os

def zapisz_csv(nazwa_pliku, x, y):
    dane = list(zip(x, y))
    dane.insert(0, ('x', 'y'))
    print(dane)
    with open(nazwa_pliku, 'w') as plik:
        writer = csv.writer(plik)
        writer.writerows(list(dane))

def czytaj_csv(nazwa_pliku):
    lx = []
    ly = []
    if os.path.isfile(nazwa_pliku):
        with open(nazwa_pliku) as plik:
            dane = list(csv.reader(plik))
            dane.pop(0)
            for wiersz in dane:
                print(wiersz)
                lx.append(float(wiersz[0]))
                ly.append(float(wiersz[1]))
    return lx, ly

def generuj_ruchy():
    n = int(input('Ile ruchów? '))
    x = y = 0
    lx = [0]
    ly = [0]

    for i in range(0, n):
        # wylosuj kąt i zamień go na radiany
        rad = random.randint(0, 360) * np.pi / 180
        x = x + np.cos(rad)  # wylicz współrzędną x
        y = y + np.sin(rad)  # wylicz współrzędną y
        print(f'x = {x:.2f}, y = {y:.2f}')
        lx.append(float(x))
        ly.append(float(y))

    # oblicz i wypisz wektor końcowego przesunięcia
    s = np.fabs(np.sqrt(x ** 2 + y ** 2))
    print(f'Wektor przesunięcia: {s:.2f}')
    return lx, ly

def rysuj_ruchy(lx, ly):
    s = np.fabs(np.sqrt(lx[-1] ** 2 + ly[-1] ** 2))
    fig, ax = plt.subplots()
    ax.plot((0, lx[-1]), (0, ly[-1]), color='blue')
    ax.plot(lx, ly, 'o:g', linewidth=2, alpha=0.5)
    ax.legend([f'Dane x, y\nPrzemieszczenie: {s:.2f}'], loc='upper left')
    ax.set_xlabel('lx')
    ax.set_ylabel('ly')
    ax.set_title('Ruchy Browna')
    ax.grid(True)
    plt.show()

lx, ly = czytaj_csv('r_browna.csv')
if lx == []:
    lx, ly = generuj_ruchy()
    zapisz_csv('r_browna.csv', lx, ly)
rysuj_ruchy(lx, ly)
