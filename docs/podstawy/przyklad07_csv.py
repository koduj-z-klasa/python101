import os  # moduł udostępniający funkcję isfile()
import csv  # moduł do obsługi formatu csv

slownik = {}  # pusty słownik
nazwa_pliku = "slownik.csv"  # nazwa pliku zawierającego wyrazy i ich tłumaczenia


def otworz():
    if os.path.isfile(nazwa_pliku):  # czy istnieje plik słownika?
        with open(nazwa_pliku, newline='') as plik_csv:  # otwórz plik do odczytu
            tresc = csv.reader(plik_csv)
            for wiersz in tresc:  # przeglądamy kolejne linie
                slownik[wiersz[0]] = wiersz[1:]
    return len(slownik)  # zwracamy liczbę elementów w słowniku


def zapisz():
    # otwieramy plik do zapisu, istniejący plik zostanie nadpisany(!)
    with open(nazwa_pliku, "w", newline='') as plik_csv:
        tresc = csv.writer(plik_csv)
        for w_obcy in slownik:
            lista = slownik[w_obcy]
            lista.insert(0, w_obcy)
            tresc.writerow(lista)


def oczysc(tekst):
    """Funkcja usuwa początkowe i końcowe białe znaki oraz znaki końca linii
       i zwraca tekst zamieniony na małe litery"""
    return tekst.strip().lower()


def main(args):
    print('''Wprowadzaj dane w formacie:
    wyraz obcy: znaczenie1, znaczenie2
    Aby zakończyć wprowadzanie danych, naciśnij ENTER.
    ''')

    # zmienna oznaczająca, że użytkownik uzupełnił lub zmienił słownik
    czy_zastapic = False
    czy_nowy = False
    ile_wyrazow = otworz()
    print('Słów w bazie:', ile_wyrazow)

    # główna pętla programu
    while True:
        dane = input('Podaj wyraz obcy i jego znaczenia: ')
        t = dane.split(':')
        w_obcy = t[0].strip().lower()
        if not w_obcy:
            break
        elif dane.count(':') == 1:  # sprawdzamy poprawność danych
            if w_obcy in slownik:
                print('Wyraz', w_obcy, ' i jego znaczenia są już w słowniku.')
                czy_zastapic = input('Zastąpić wpis (t/n)? ')
            # czy wyrazu nie ma w słowniku? a może chcemy go zastąpić?
            if w_obcy not in slownik or czy_zastapic == 't':
                znaczenia = t[1].split(',')  # znaczenia zapisujemy w liście
                znaczenia = list(map(oczysc, znaczenia))  # oczyszczamy listę
                slownik[w_obcy] = znaczenia
                print(f'Dodano: {w_obcy}:{znaczenia}')
                czy_nowy = True
        else:
            print('Błędny format!')

    if czy_nowy:
        zapisz()

    print(slownik)

    print('=' * 50)
    print('{0: <15}{1: <40}'.format('Wyraz obcy', 'Znaczenia'))
    print('=' * 50)
    for w_obcy in slownik:
        print('{0: <15}{1: <40}'.format(w_obcy, ','.join(slownik[w_obcy])))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
