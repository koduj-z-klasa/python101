n = int(input('Podaj liczbę liter alfabetu do wypisania: '))
print("Alfabet w porządku odwróconym:")

for i in range(122, 122-n, -1):
    l_mala = chr(i)
    l_duza = l_mala.upper()
    print(f'{l_mala} – {l_duza}', end=' ')