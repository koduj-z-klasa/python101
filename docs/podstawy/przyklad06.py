from oceny_funkcje import wypisz, srednia, mediana, odchylenie


def main():
    przedmioty = {'polski', 'angielski'}  # definicja zbioru
    wypisz(przedmioty, 'Lista przedmiotów zawiera: ')

    while True:
        przedmiot = input('Podaj nazwę przedmiotu (min. 2 znaki) lub ENTER, żeby zakończyć: ').strip()
        if len(przedmiot) > 1:
            if przedmiot not in przedmioty:  # jeżeli przedmiotu nie ma w zbiorze
                przedmioty.add(przedmiot)  # dodaj przedmiot do zbioru
            else:
                print('Ten przedmiot już mamy :-)')
        else:
            wypisz(przedmioty, '\nTwoje przedmioty: ')
            przedmiot = input('\nZ którego przedmiotu wprowadzisz oceny? ')
            if przedmiot not in przedmioty:  # jeżeli przedmiotu nie ma w zbiorze
                print('Brak takiego przedmiotu, możesz go dodać.')
            else:
                break  # przerwanie pętli

    oceny = []  # pusta lista ocen
    ocena = None  # zmienna sterująca pętlą i do pobierania ocen
    while not ocena:
        try:
            ocena = int(input('Podaj ocenę (1-6) lub 0, aby zakończyć: '))
            if 0 < ocena < 7:
                oceny.append(ocena)
            elif ocena == 0:
                break
            else:
                print('Błędna ocena.')
            ocena = None
        except ValueError:
            print('Błędne dane!')

    wypisz(oceny, przedmiot.capitalize() + ' - wprowadzone oceny: ')
    s = srednia(oceny)
    m = mediana(oceny)
    o = odchylenie(oceny, s)
    print()
    print(f'Średnia: {s:8.2f}')
    print(f'Mediana: {m:8.2f}')
    print(f'Odchylenie: {o:5.2f}')
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
