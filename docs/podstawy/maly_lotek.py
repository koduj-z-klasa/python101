import random

liczba = random.randint(1, 10)
print('Wylosowana liczba:', liczba)

for i in range(3):
    print('Próba ', i + 1)
    typ = int(input('Jaką liczbę od 1 do 10 mam na myśli? '))

    if liczba == typ:
        print('Zgadłeś!')
        break
    elif i == 2:
        print('Wylosowano liczbę: ', liczba)
    else:
        print('Spróbuj jeszcze raz.')
    print()
