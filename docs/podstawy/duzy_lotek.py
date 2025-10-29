import random

# dane wejściowe
error = False
try:
    n = int(input('Podaj liczbę losowanych liczb: '))
    maks = int(input('Podaj maksymalną losowaną liczbę: '))
    if n >= maks:
        error = True
except ValueError:
    error = True

if error:
    print('Błędne dane!')
    exit()

# losowanie liczb
liczby = []
while len(liczby) < n:
    liczba = random.randint(0, maks)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)

# pobieranie typów
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

# sprawdzanie typów i dane wyjściowe
print()
trafione = set(liczby) & typy
if trafione:
    print(f'Trafione liczby: {trafione}')
    print(f'Liczba trafień {len(trafione)}')
else:
    print('Brak trafień. Spróbuj jeszcze raz!')

print('Wylosowane liczby:', liczby)
