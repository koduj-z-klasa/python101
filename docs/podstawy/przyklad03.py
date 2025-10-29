n = int(input('Podaj liczbę liter alfabetu do wypisania: '))

print("Alfabet w porządku naturalnym:")

print('Wersja 1 – for:')
for i in range(n):
    l_mala = chr(ord('a') + i)
    l_duza = chr(ord('A') + i)
    print(f'{l_mala} – {l_duza}', end=' ')
print()

print('Wersja 2 - for:')
for i in range(65, 65+n):
    l_duza = chr(i)
    l_mala = chr(i + 32)  # 32 to różnica między kodem ASCII litery dużej i małej
    print(f'{l_mala} – {l_duza}', end=' ')
print()

print('Wersja 3 – while:')
i = 0
while i < n:
    l_mala = chr(ord('a') + i)
    l_duza = chr(ord('A') + i)
    print(f'{l_mala} – {l_duza}', end=' ')
    i += 1
print()
