#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ~/python/06_slownik.py

"""
	ZADANIE
	Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia.
	Pobierz od użytkownika dane w formacie: wyraz obcy: znaczenie1, znaczenie2, ... itd.
    Pobieranie danych kończy wpisanie słowa "koniec".
	Podane dane zapisz w pliku.
    Użytkownik powinien mieć możliwość dodawania nowych i zmieniania zapisanych danych.
"""

import os.path # moduł udostępniający funkcję isfile()

print """Podaj dane w formacie:
wyraz obcy: znaczenie1, znaczenie2
Aby zakończyć wprowadzanie danych, podaj 0.
"""

sFile="slownik.txt" #nazwa pliku zawierającego wyrazy i ich tłumaczenia
slownik = {} # pusty słownik
#wobce = set() # pusty zbiór wyrazów obcych

def otworz(plik):
    if os.path.isfile(sFile): #czy istnieje plik słownika?
        with open(sFile, "r") as sTxt: #otwórz plik do odczytu
            for line in sTxt: #przeglądamy kolejne linie
                t = line.split(":") #rozbijamy linię na wyraz obcy i tłumaczenia
                wobcy = t[0]
                znaczenia = t[1].replace("\n","") #usuwamy znaki nowych linii
                znaczenia = znaczenia.split(",") #tworzymy listę znaczeń
                slownik[wobcy] = znaczenia #dodajemy do słownika wyrazy obce i ich znaczenia
    return len(slownik) #zwracamy ilość elementów w słowniku

def zapisz(slownik):
    file1 = open(sFile,"w") #otwieramy plik do zapisu, istniejący plik zostanie nadpisany(!)
    for wobcy in slownik:
        znaczenia=",".join(slownik[wobcy]) # "sklejamy" znaczenia przecinkami w jeden napis
        linia = ":".join([wobcy,znaczenia]) # wyraz_obcy:znaczenie1,znaczenie2,...
        print >>file1, linia # zapisujemy w pliku kolejne linie
    file1.close() #zamykamy plik

def oczysc(str):
    str = str.strip() # usuń początkowe lub końcowe białe znaki
    str = str.lower() # zmień na małe litery 
    return str

nowy = False #zmienna oznaczająca, że użytkownik uzupełnił lub zmienił słownik
ileWyrazow = otworz(sFile)
print "Wpisów w bazie:", ileWyrazow

#główna pętla programu
while True:
    dane = raw_input("Podaj dane: ")
    t = dane.split(":")
    wobcy = t[0].strip().lower() # robimy to samo, co funkcja oczysc()
    if wobcy == 'koniec':
        break
    elif dane.count(":") == 1: #sprawdzamy poprawność wprowadzonych danych
        if wobcy in slownik:
            print "Wyraz", wobcy, " i jego znaczenia są już w słowniku."
            op = raw_input("Zastąpić wpis (t/n)? ")
        #czy wyrazu nie ma w słowniku? a może chcemy go zastąpić?
        if wobcy not in slownik or op == "t":
            znaczenia = t[1].split(",") #podane znaczenia zapisujemy w liście
            znaczenia = map(oczysc, znaczenia) #oczyszczamy elementy listy
            slownik[wobcy] = znaczenia
            nowy = True
    else:
        print "Błędny format!"

if nowy: zapisz(slownik)

print "="*50
print "{0: <15}{1: <40}".format("Wyraz obcy","Znaczenia")
print "="*50
for wobcy in slownik:
    print "{0: <15}{1: <40}".format(wobcy,",".join(slownik[wobcy]))


"""
Alternatywne sposoby otwierania pliku:
f = open('test.txt', 'r')
for line in f:
    print line[0]
f.close()

with open("text.txt", "r") as txt:
    for line in txt:
        print line

for line in open('test.txt', 'r'):
    print line[0]
"""
