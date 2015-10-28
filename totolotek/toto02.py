#! /usr/bin/env python
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy, wyniki
from totomodul import czytaj_json, zapisz_json
import time

# program główny

# ustalamy trudność gry
nick, ileliczb, maksliczba, ilerazy = ustawienia()

nazwapliku = nick + ".json"
losowania = czytaj_json(nazwapliku)

# losujemy liczby
liczby = losujliczby(ileliczb, maksliczba)

# pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
for i in range(ilerazy):
    typy = pobierztypy(ileliczb, maksliczba)
    trafione = wyniki(set(liczby), typy)

losowania.append({
    "czas": time.time(),
    "dane": (ileliczb, maksliczba),
    "wylosowane": liczby,
    "ile": trafione
})

zapisz_json(nazwapliku, losowania)

print "Wylosowane liczby:", liczby
print "\n", losowania
