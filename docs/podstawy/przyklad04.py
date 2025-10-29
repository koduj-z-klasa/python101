from random import randint

n = int(input('Ile liczb podasz? '))
lista = []  # pusta lista
for i in range(n):
    liczba = int(input('Podaj liczbę: '))
    lista.append(liczba)
print('Elementy listy:', lista)
print()

print('Elementy i indeksy – sposób 1:')
for i in range(n):
    # wypisuje: element (indeks)
    print(f'{lista[i]} ({i})', end=' ')
print('\n')

print('Elementy i indeksy – sposób 2:')
for i, e in enumerate(lista):
    print(f'{e} ({i})', end=' ')
print('\n')

print('Elementy posortowane nierosnąco:')
for e in reversed(lista):
    print(e, end=' ')
print('\n')

print('Elementy posortowane niemalejąco:')
for e in sorted(lista):
    print(e, end=' ')
print('\n')

el = int(input('Podaj element, którego wystąpienia należy zliczyć: '))
if el in lista:
    print('Liczba wystąpień:', lista.count(el))
    print('Indeks pierwszego wystąpienia:', lista.index(el))
else:
    print('Brak elementu w liście!')
print()

el = int(input('Podaj element do usunięcia: '))
lista.remove(el)
print(f'Usunięto {el} z listy:', lista)
print()

ind = int(input('Podaj indeks elementu do usunięcia: '))
if 0 <= ind < len(lista):
    el = lista.pop(ind)
    print(f'Usunięto {el} z listy:', lista)
else:
    print('Indeks poza zakresem.')
print()

el = int(input('Podaj element do wstawienia: '))
ind = int(input('Podaj indeks: '))
lista.insert(ind, el)
print(lista, '\n')

i = int(input('Podaj indeks początkowy: '))
j = int(input('Podaj indeks końcowy: '))
print(lista[i:j])
