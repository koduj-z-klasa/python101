#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys
import os
from random import randint
from time import sleep
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

mc = minecraft.Minecraft.create("192.168.1.10")  # połączenie z symulatorem


class GraWZycie(object):
    """
    Główna klasa gry, łączy wszystkie elementy.
    """

    def __init__(self, mc, szer, wys, ile=40):
        """
        Przygotowanie ustawień gry
        :param szer: szerokość planszy mierzona liczbą komórek
        :param wys: wysokość planszy mierzona liczbą komórek
        """
        self.mc = mc
        mc.postToChat('Gra o zycie')
        self.szer = szer
        self.wys = wys
        self.populacja = Populacja(mc, szer, wys)  # instancja klasy Populacja
        if ile:
            self.populacja.losuj(ile)

    def uruchom(self):
        """
        Główna pętla gry
        """
        i = 0
        while True:  # działaj w pętli do momentu otrzymania sygnału do wyjścia
            print("Generacja: " + str(i))
            self.plac(0, 0, 0, self.szer, self.wys)  # narysuj pole gry
            self.populacja.rysuj()
            self.populacja.nast_generacja()
            i += 1
            sleep(1)

    def plac(self, x, y, z, szer=20, wys=10):
        """
        Funkcja tworzy plac gry
        """
        podloga = block.STONE
        wypelniacz = block.AIR
        granica = block.OBSIDIAN

        # granica, podłoże, czyszczenie
        self.mc.setBlocks(
            x - 1, y - 1, z - 1, x + szer + 1, y - 1, z + wys + 1, granica)
        self.mc.setBlocks(x, y - 1, z, x + szer, y - 1, z + wys, podloga)
        self.mc.setBlocks(
            x, y, z, x + szer, y + max(szer, wys), z + wys, wypelniacz)


# magiczne liczby używane do określenia czy komórka jest żywa
DEAD = 0
ALIVE = 1
BLOK_ALIVE = 35  # block.WOOL


class Populacja(object):
    """
    Populacja komórek
    """

    def __init__(self, mc, ilex, iley):
        """
        Przygotowuje ustawienia populacji
        :param mc: obiekt Minecrafta
        :param ilex: rozmiar x macierzy komórek (wiersze)
        :param iley: rozmiar y macierzy komórek (kolumny)
        """
        self.mc = mc
        self.iley = iley
        self.ilex = ilex
        self.generacja = self.reset_generacja()

    def reset_generacja(self):
        """
        Tworzy i zwraca macierz pustej populacji
        """
        # wyrażenie listowe tworzy x kolumn o y komórkach
        # wypełnionych wartością 0 (DEAD)
        return [[DEAD for y in xrange(self.iley)] for x in xrange(self.ilex)]

    def losuj(self, ile=50):
        """
        Losowo wypełnia macierz żywymi komórkami, czyli wartością 1 (ALIVE)
        """
        for i in range(ile):
            x = randint(0, self.ilex - 1)
            y = randint(0, self.iley - 1)
            self.generacja[x][y] = ALIVE
        print self.generacja

    def rysuj(self):
        """
        Rysuje komórki na planszy, czyli umieszcza odpowiednie bloki
        """
        print "Rysowanie macierzy..."
        for x, z in self.zywe_komorki():
            podtyp = randint(0, 15)
            mc.setBlock(x, 0, z, BLOK_ALIVE, podtyp)

    def zywe_komorki(self):
        """
        Generator zwracający współrzędne żywych komórek.
        """
        for x in range(len(self.generacja)):
            kolumna = self.generacja[x]
            for y in range(len(kolumna)):
                if kolumna[y] == ALIVE:
                    yield x, y  # zwracamy współrzędne, jeśli komórka jest żywa

    def sasiedzi(self, x, y):
        """
        Generator zwracający wszystkich okolicznych sąsiadów
        """
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if nx == x and ny == y:
                    continue  # pomiń współrzędne centrum
                if nx >= self.ilex:
                    # sąsiad poza końcem planszy, bierzemy pierwszego w danym
                    # rzędzie
                    nx = 0
                elif nx < 0:
                    # sąsiad przed początkiem planszy, bierzemy ostatniego w
                    # danym rzędzie
                    nx = self.ilex - 1
                if ny >= self.iley:
                    # sąsiad poza końcem planszy, bierzemy pierwszego w danej
                    # kolumnie
                    ny = 0
                elif ny < 0:
                    # sąsiad przed początkiem planszy, bierzemy ostatniego w
                    # danej kolumnie
                    ny = self.iley - 1

                # dla każdego nie pominiętego powyżej
                # przejścia pętli zwróć komórkę w tych współrzędnych
                yield self.generacja[nx][ny]

    def nast_generacja(self):
        """
        Generuje następną generację populacji komórek
        """
        print "Obliczanie generacji..."
        nast_gen = self.reset_generacja()
        for x in range(len(self.generacja)):
            kolumna = self.generacja[x]
            for y in range(len(kolumna)):
                # pobieramy wartości sąsiadów
                # dla żywej komórki dostaniemy wartość 1 (ALIVE)
                # dla martwej otrzymamy wartość 0 (DEAD)
                # zwykła suma pozwala nam określić liczbę żywych sąsiadów
                count = sum(self.sasiedzi(x, y))
                if count == 3:
                    # rozmnażamy się
                    nast_gen[x][y] = ALIVE
                elif count == 2:
                    # przechodzi do kolejnej generacji bez zmian
                    nast_gen[x][y] = kolumna[y]
                else:
                    # za dużo lub za mało sąsiadów by przeżyć
                    nast_gen[x][y] = DEAD

        # nowa generacja staje się aktualną generacją
        self.generacja = nast_gen


if __name__ == "__main__":
    gra = GraWZycie(mc, 30, 20, 40)  # instancja klasy GraWZycie
    mc.player.setPos(20, 1, 10)
    gra.uruchom()  # wywołanie metody uruchom()
