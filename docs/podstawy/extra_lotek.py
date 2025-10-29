from modul_lotek import wczytaj_ustawienia, pobierz_ustawienia, zapisz_ustawienia
from modul_lotek import losuj_liczby, pobierz_typy, wypisz_wyniki
from modul_lotek import wczytaj_dane, zapisz_dane
from datetime import datetime


def main(args):
    nick = input('Podaj nick: ')
    dane = wczytaj_ustawienia(nick)
    print(dane)  # tę instrukcję można zakomentować
    if dane:
        print(f'Ustawienia:\nLiczb: {dane[1]}\nMaks: {dane[2]}\nTypowań: {dane[3]}')

    if not dane or input('Zmieniasz (t/n)? ').lower() == 't':
        dane = pobierz_ustawienia(nick)
        zapisz_ustawienia(nick, dane)

    mick, n, maks, ile_typowan = dane[0:1] + [int(x) for x in dane[1:4]]
    print(mick, n, maks, ile_typowan)  # tę instrukcję można zakomentować

    liczby = losuj_liczby(n, maks)

    for i in range(ile_typowan):
        typy = pobierz_typy(n, maks)
        ile_trafionych = wypisz_wyniki(liczby, typy)
        if ile_trafionych == n:
            break

    print('Wylosowane liczby:', liczby)

    losowania = wczytaj_dane(nick)
    losowanie = {
        'czas': datetime.strftime(datetime.now(), '%d.%m.%Y %H:%M:%S'),
        'n': n,
        'maks': maks,
        'ile_typowan': ile_typowan,
        'wylosowane': tuple(liczby),
        'trafionych': ile_trafionych
    }
    losowania.append(losowanie)
    zapisz_dane(nick, losowania)
    print(losowania)  # tę instrukcję można zakomentować

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
