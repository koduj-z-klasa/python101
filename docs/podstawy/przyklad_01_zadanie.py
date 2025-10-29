# inicjalizujemy zmienne
akt_rok = int(input('Podaj aktualny rok: '))
py_rok = 1989

# pobieramy dane
imie = input('Jak się nazywasz? ')
rok_urodzenia = int(input('Podaj rok urodzenia: '))

# wykonujemy obliczenia
wiek_py = akt_rok - py_rok
wiek_u = akt_rok - rok_urodzenia

# wypisujemy komunikaty
print('Witaj', imie + '!', 'Mów mi Python.')
print('Mam', wiek_py, 'lat, ty masz', str(wiek_u) + '.')

# kto jest starszy?
if wiek_py > wiek_u:
    print('Jestem starszy od ciebie!')

if wiek_u < wiek_py:
    print('Jestem młodszy od ciebie!')

if wiek_py == wiek_u:
    print('Mamy tyle samo lat!')
