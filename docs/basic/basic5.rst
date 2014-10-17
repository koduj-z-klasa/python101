Listy, zbiory, moduły i funkcje
==================================

ZADANIE
-------

    Napisz program, który umożliwi wprowadzanie ocen z podanego przedmiotu ścisłego (np. fizyki), następnie policzy i wyświetla średnią, medianę i odchylenie standardowe wprowadzonych ocen. Funkcje pomocnicze i statystyczne umieść w osobnym module.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    #! /usr/bin/env python
    # -*- coding: UTF-8 -*-

    # ~/python/05_oceny_03.py

    # importujemy funkcje z modułu ocenyfun zapisanego w pliku ocenyfun.py
    from ocenyfun import drukuj
    from ocenyfun import srednia
    from ocenyfun import mediana
    from ocenyfun import odchylenie

    przedmioty = set(['polski','angielski']) #definicja zbioru
    drukuj(przedmioty, "Lista przedmiotów zawiera: ") #wywołanie funkcji z modułu ocenyfun

    print "\nAby przerwać wprowadzanie przedmiotów, naciśnij Enter."
    while True:
        przedmiot = raw_input("Podaj nazwę przedmiotu: ")
        if len(przedmiot):
            if przedmiot in przedmioty: #czy przedmiot jest w zbiorze?
                print "Ten przedmiot już mamy :-)"
            przedmioty.add(przedmiot) #dodaj przedmiot do zbioru
        else:
            drukuj(przedmioty,"\nTwoje przedmioty: ")
            przedmiot = raw_input("\nZ którego przedmiotu wprowadzisz oceny? ")
            if przedmiot not in przedmioty: #jeżeli przedmiotu nie ma w zbiorze
                print "Brak takiego przedmiotu, możesz go dodać."
            else:
                break # wyjście z pętli

    oceny = [] # pusta lista ocen
    ocena = None # zmienna sterująca pętlą i do pobierania ocen
    print "\nAby przerwać wprowadzanie ocen, podaj 0 (zero)."

    while not ocena:
        try: #mechanizm obsługi błędów
            ocena = int(raw_input("Podaj ocenę (1-6): "))
            if (ocena > 0 and ocena < 7):
                oceny.append(float(ocena))
            elif ocena == 0:
                break
            else:
                print "Błędna ocena."
            ocena = None
        except ValueError:
            print "Błędne dane!"

    drukuj(oceny,przedmiot.capitalize()+" - wprowadzone oceny: ")
    s = srednia(oceny) # wywołanie funkcji z modułu ocenyfun
    m = mediana(oceny) # wywołanie funkcji z modułu ocenyfun
    o = odchylenie(oceny,s) # wywołanie funkcji z modułu ocenyfun
    print "\nŚrednia: {0:5.2f}\nMediana: {1:5.2f}\nOdchylenie: {2:5.2f}".format(s,m,o)

JAK TO DZIAŁA
-------------

**Pojęcia**: *import, moduł, zbiór, przechwytywanie wyjątków, formatowanie napisów i danych na wyjściu*.

Klauza ``from moduł import funkcja`` umożliwia wykorzystanie w programie funkcji zdefiniowanych w innych modułach i zapisanych w osobnych plikach. Dzięki temu utrzymujemy przejrzystość programu głównego, a jednocześnie możemy funkcje z modułów wykorzystywać, importując je w innych programach. Nazwa modułu to nazwa pliku z kodem pozbawiona jednak rozszerzenia *.py*. Moduł musi być dostępny w ścieżce przeszukiwania [5]_, aby można go było poprawnie dołączyć.

.. [5] W przypadku prostych programów zapisuj moduły w tym samym katalogu co program główny.

Instrukcja ``set()`` tworzy zbiór, czyli nieuporządkowany zestaw niepowtarzalnych (!) elementów. Instrukcje ``if przedmiot in przedmioty`` i ``if przedmiot not in przedmioty`` za pomocą operatorów zawierania ``(not) in`` sprawdzają, czy podany przedmiot już jest lub nie w zbiorze. Polecenie ``przedmioty.add()`` pozwala dodawać elementy do zbioru, przy czym jeżeli element jest już w zbiorze, nie zostanie dodany. Polecenie ``przedmioty.remove()`` usunnie podany jako argument element ze zbioru.

Oceny z wybranego przedmiotu pobieramy w pętli dopóty, dopóki użytkownik nie wprowadzi 0 (zera). Blok ``try...except`` pozwala przechwycić wyjątki, czyli w naszym przypadku niemożność przekształcenia wprowadzonej wartości na liczbę całkowitą. Jeżeli funkcja ``int()`` zwróci wyjątek, wykonywane są instrukcje w bloku ``except ValueError:``, w przeciwnym razie po sprawdzeniu poprawności oceny dodajemy ją jako liczbę zmiennoprzecinkową (typ *float*) do listy: ``oceny.append(float(ocena))``.

Metoda ``.capitalize()`` pozwala wydrukować podany napis dużą literą.

W funkcji ``print(...).format(s,m,o)`` zastosowano formatowanie drukowanych wartości, do których odwołujemy się w specyfikacji ``{0:5.2f}``. Pierwsza cyfra wskazuje, którą wartość z numerowanej od 0 (zera) listy, umieszczonej w funkcji ``format()``, wydrukować; np. aby wydrukować drugą wartość, trzeba by użyć kodu ``{1:}``.Po dwukropku podajemy szerokość pola przeznaczonego na wydruk, po kropce ilość miejsc po przecinku, symbol *f* oznacza natomiast liczbę zmiennoprzecinkową stałej precyzji.

POĆWICZ SAM
-----------

    W konsoli Pythona utwórz listę wyrazy zawierającą elementy: *abrakadabra* i *kordoba*. Utwórz zbiór *w1* poleceniem ``set(wyrazy[0])``. Oraz zbiór *w2* poleceniem ``set(wyrazy[1])``. Wykonaj kolejno polecenia: ``print w1 – w2; print w1 | w2; print w1 & w2; print w1 ^ w2``. Przykłady te ilustrują użycie klasycznych operatorów na zbiorach, czyli: różnica (-) , suma (|), przecięcie (część wspólna, &) i elementy unikalne (^).

Funkcje wykorzystywane w programie umieszczamy w osobnym pliku.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    #! /usr/bin/env python
    # -*- coding: UTF-8 -*-

    # ~/python/ocenyfun.py

    """
        Moduł ocenyfun zawiera funkcje wykorzystywane w programie m01_oceny.
    """

    import math # zaimportuj moduł matematyczny

    def drukuj(co,kom="Sekwencja zawiera: "):
        print kom
        for i in co:
            print i,

    def srednia(oceny):
        suma = sum(oceny)
        return suma/float(len(oceny))

    def mediana(oceny):
        oceny.sort();
        if len(oceny) % 2 == 0: #parzysta ilość ocen
            half = len(oceny)/2
            #można tak:
            #return float(oceny[half-1]+oceny[half]) / 2.0
            #albo tak:
            return sum(oceny[half-1:half+1]) / 2.0
        else: #nieparzysta ilość ocen
            return oceny[len(oceny)/2]

    def wariancja(oceny,srednia):
        """
        Wariancja to suma kwadratów różnicy każdej oceny i średniej podzielona przez ilość ocen:
        sigma = (o1-s)+(o2-s)+...+(on-s) / n, gdzie:
        o1, o2, ..., on - kolejne oceny,
        s - średnia ocen,
        n - liczba ocen.
        """
        sigma = 0.0
        for ocena in oceny:
            sigma += (ocena-srednia)**2
        return sigma/len(oceny)

    def odchylenie(oceny,srednia): #pierwiastek kwadratowy z wariancji
        w = wariancja(oceny,srednia)
        return math.sqrt(w)

JAK TO DZIAŁA
-------------

**Pojęcia**: *funkcja, argumenty funkcji, zwracanie wartości, moduł*.

Klauzula ``import math`` udostępnia w pliku wszystkie metody z modułu
matematycznego, dlatego musimy odwoływać się do nich za pomocą notacji
moduł.funkcja, np.: ``math.sqrt()`` – zwraca pierwiastek kwadratowy.

Funkcja ``drukuj(co, kom="...")`` przyjmuje dwa argumenty, *co* – listę
lub zbiór, który drukujemy w pętli for, oraz *kom* – komunikat,
który wyświetlamy przed wydrukiem. Argument *kom* jest opcjonalny,
przypisano mu bowiem wartość domyślną, która zostanie użyta,
jeżeli użytkownik nie poda innej w wywołaniu funkcji.

Funkcja ``srednia()`` do zsumowania wartości ocen wykorzystuje funkcję ``sum()``.

Funkcja ``mediana()`` sortuje otrzymaną listę "w miejscu" (``oceny.sort()``), tzn. trwale zmienia porządek elementów [6]_.
W zależności od długości listy zwraca wartość środkową (długość nieparzysta)
lub średnią arytmetyczną dwóch środkowych wartości (długość).
Zapis ``oceny[half-1:half+1]`` wycina i zwraca dwa środkowe elementy
z listy, przy czym wyrażenie ``half = len(oceny)/2`` wylicza nam indeks drugiego ze środkowych elementów.

.. [6] Przypomnijmy: alternatywna funkcja ``sorted(lista)`` zwraca uporządkowaną rosnąco kopię listy.

W funkcja ``wariancja()`` pętla for odczytuje kolejne oceny i w kodzie ``sigma += (ocena-srednia)**2`` korzysta z operatorów skróconego dodawania (+=) i potęgowania (**), aby wyliczyć sumę kwadratów różnic kolejnych ocen i średniej.

POĆWICZ SAM
-----------

    Dopisz funkcję, która wyświetli wszystkie oceny oraz ich odchylenia od wartości średniej.
