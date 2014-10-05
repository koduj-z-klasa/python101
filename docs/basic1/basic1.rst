Mów mi Python – wprowadzenie do języka Python
*********************************************

Jestem Python
================

Python jest dynamicznie typowanym językiem interpretowanym wysokiego poziomu. Cechuje się czytelnością i zwięzłością kodu. Stworzony został w latach 90. przez Guido van Rossuma, nazwa zaś pochodzi od tytułu serialu komediowego emitowanego w BBC pt. "Latający cyrk Monty Pythona".

W systemach opartych na Linuksie interpreter Pythona jest standardowo zainstalowany, ponieważ duża część oprogramowania na nim bazuje. W systemach Microsoft Windows Pythona należy doinstalować. Funkcjonalność Pythona może być dowolnie rozszerzana dzięki licznym bibliotekom pozwalającym tworzyć aplikacje okienkowe (PyQt, PyGTK, wxPython), internetowe (Flask, Django) czy multimedialne i gry (Pygame). Istnieją również kompleksowe projekty oparte na Pythonie wspomagające naukową analizę, obliczenia i przetwarzanie danych (Anaconda, Canopy).

Kodować można w dowolnym edytorze tekstowym, jednak ze względów praktycznych warto korzystać z programów ułatwiających pisanie kodu. Polecić można np. lekkie, szybkie i obsługujące wiele języków środowisko Geany, a także profesjonalne rozwiązanie, jakim jest aplikacja PyCharm. Obydwa programy działają na platformie Linux i Windows.

Zanim przystąpimy do pracy w katalogu domowym utworzymy podkatalog python, w którym będziemy zapisywali nasze skrypty:

.. raw:: html

    <div class="code_no">Terminal nr 2.1</div>

.. code:: bash

    ~ $ mkdir python

Poznawanie Pythona zrealizujemy poprzez rozwiązywanie prostych zadań, które pozwolą zaprezentować elastyczność i łatwość tego języka. Nazwy kolejnych skryptów umieszczone są jako komentarz zawsze w czwartej linii kodu. Pliki zawierające skrypty Pythona mają zazwyczaj rozszerzenie .py. Bardzo przydatnym narzędziem podczas kodowania w Pythonie jest konsola interpretera, którą uruchomimy wydając w terminalu polecenie python lub ipython[#f1]_. Można w niej testować i debugować wszystkie wyrażenia, warunki, polecenia itd., z których korzystamy w skryptach.

.. [#f1]_ Ipython to rozszerzona konsola Pythona przeznaczona do wszelkiego rodzaju interaktywnych obliczeń.

Witaj Python!
=================

ZADANIE
------------
Pobierz od użytkownika imię, wiek i powitaj go komunikatem::
    "Mów mi Python, mam x lat.
    Witaj w moim świecie imie.
    Jesteś starszy(młodszy) ode mnie."

.. raw:: html

    <div class="code_no">Kod nr 2.2.1</div>

.. code-block:: python
    :linenos:

    #! /usr/bin/env python
    # -*- coding: UTF-8 -*-

    # ~/python/01_hello.py

    # inicjalizujemy zmienne (wartości)
    curYear = 2014
    pythonYear = 1989
    wiekPythona = curYear - pythonYear # ile lat ma Python

    # pobieramy dane
    imie = raw_input('Jak się nazywasz? ')
    wiek = int(raw_input('Ile masz lat? '))

    # wyprowadzamy dane
    print "Witaj w moim świecie ",imie
    print "Mów mi Python, mam", wiekPythona, "lat."

    # instrukcja warunkowa
    if wiek > wiekPythona:
        print 'Jesteś starszy ode mnie.'
    else:
        print 'Jesteś młodszy ode mnie.'


JAK TO DZIAŁA
-------------

**Pojęcia**: *zmienna, wartość, wyrażenie, wejście i wyjście danych, instrukcja warunkowa, komentarz*.

Deklaracja zmiennej w Pythonie nie jest wymagana, wystarczy podanej nazwie przypisać jakąś wartość
za pomocą operatora przypisania "=" [#f2]_. Zmiennym często przypisujemy wartości za pomocą wyrażeń,
czyli działań arytmetycznych lub logicznych.

.. [#f2] Dlatego niekiedy mówi się, że w Pythonie zmiennych nie ma, są natomiast wartości określonego typu.

Funkcja ``raw_input()`` zwraca pobrane z klawiatury znaki jako napis, czyli typ **string**.

Funkcja ``int()`` umożliwia konwersję napisu na liczbę całkowitą, czyli typ **integer**.

Funkcja ``print`` drukuje podane argumenty oddzielone przecinkami. Komunikaty tekstowe ujmujemy
w cudzysłowy podwójne lub pojedyncze. Przecinek oddziela kolejne argumenty spacjami.

Instrukcja ``if`` (jeżeli) pozwala na warunkowe wykonanie kodu. Jeżeli podane wyrażenie
jest prawdziwe (przyjmuje wartość ``True``) wykonywana jest pierwsza instrukcja,
w przeciwnym wypadku (``else``), kiedy wyrażenie jest fałszywe (wartość ``False``),
wykonywana jest instrukcja druga. Warto zauważyć, że polecenia instrukcji warunkowej kończymy dwukropkiem.

Charakterystyczną cechą Pythona jest używanie wcięć do zaznaczania bloków kodu.
Komentarze wprowadzamy po znaku ``#``.

POĆWICZ SAM
-----------

    Zmień program tak, aby zmienna curYear (aktualny rok) była podawana przez użytkownika na początku programu.

Warunki i pętle
====================

ZADANIE
-------------

    Pobierz od użytkownika trzy liczby, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.

.. raw:: html

    <div class="code_no">Kod nr 2.3.1</div>

.. code-block:: python
    :linenos:

    #! /usr/bin/env python
    # -*- coding: UTF-8 -*-

    # ~/python/02_if.py

    op = "t"
    while op == "t":
        a, b, c = raw_input("Podaj trzy liczby oddzielone spacjami: ").split(" ")
        
        print "Wprowadzono liczby:", a, b, c,
        print "\nNajmniejsza: ",

        if a < b:
            if a < c:
                print a
            else
                print c
        elif b < c:
            print b
        else:
            print c
            
        op = raw_input("Jeszcze raz (t/n)? ")

    print "Nie, to nie :-("

JAK TO DZIAŁA
-------------

**Pojęcia**: *pętla, obiekt, metoda, instrukcja warunkowa zagnieżdżona, formatowanie kodu*.

Pętla while umożliwia powtarzanie określonych operacji, czyli pozwala użytkownikowi wprowadzać
kolejne serie liczb. Definiując pętle określamy warunek powtarzania kodu. Dopóki jest prawdziwy,
czyli dopóki zmienna op ma wartość "t" pętla działa. Do wydzielania kodu przynależnego do pętli
i innych instrukcji (np. ``if``) stosujemy wcięcia. Formatując kod, możemy używać zarówno tabulatorów,
jak i spacji, ważne aby w obrębie pliku było to konsekwentne [#f3]_.

.. [#f3] Dobry styl programowania sugeruje używanie do wcięć 4 spacji.

W Pythonie wszystko jest obiektem, czyli typy wbudowane, np. napisy, posiadają metody (funkcje)
wykonujące określone operacje na wartościach. W podanym kodzie funkcja ``raw_input()`` zwraca
ciąg znaków wprowadzony przez użytkownika, z którego wydobywamy poszczególne słowa za pomocą
metody ``split()`` typu string.
Instrukcje warunkowe (``if``), jak i pętle, można zagnieżdżać stosując wcięcia.
W jednej złożonej instrukcji warunkowej można sprawdzać wiele warunków (``elif:``).

POĆWICZ SAM
-----------

    Sprawdź, co się stanie, jeśli podasz liczby oddzielone przecinkiem lub podasz
    za mało liczb. Zmień program tak, aby poprawnie interpretował dane oddzielane przecinkami.

ZADANIE
-------------

    Wydrukuj alfabet w porządku naturalnym, a następnie odwróconym w formacie:
     "mała => duża litera". W jednym wierszu trzeba wydrukować po pięć takich grup.

.. raw:: html

    <div class="code_no">Kod nr 2.3.4</div>

.. code-block :: python
    :linenos:

    #! /usr/bin/env python
    # -*- coding: UTF-8 -*-

    # ~/python/03_petle.py

    print "Alfabet w porządku naturalnym:"
    x = 0
    for i in range(65,91):
        litera = chr(i)
        tmp = litera + " => " + litera.lower()
        x += 1
        if i > 65 and x % 5 == 0: # warunek złożony
            x = 0
            tmp += "\n"
        print tmp,

    x = -1
    print "\nAlfabet w porządku odwróconym:"
    for i in range(122,96,-1):
        litera = chr(i)
        x += 1
        if x == 5:
            x = 0
            print "\n",
        print litera.upper(), "=>", litera,

JAK TO DZIAŁA
-------------

**Pojęcia**: *iteracja, pętla, kod ASCII, lista, inkrementacja, operatory arytmetyczne, logiczne, przypisania i zawierania*.

Pętla for wykorzystuje zmienną i, która przybiera wartości z listy liczb całkowitych zwróconej przez funkcję ``range()``. Parametry tej funkcji określają wartość początkową i końcową listy, przy czym wartość końcowa nie wchodzi do listy. Kod ``range(122,96,-1)`` generuje listę wartości malejących od 122 do 97(!) z krokiem -1.

Funkcja ``chr()`` zwraca znak, którego kod ASCII, czyli liczbę całkowitą, przyjmuje jako argument. Metoda ``lower()`` typu string (napisu) zwraca małą literę, ``upper()`` – dużą. Wyrażenie przypisywane zmiennej tmp pokazuje, jak można łączyć napisy (konkatenacja).

Zmienna pomocnicza ``x`` jest zwiększana (inkrementacja) w pętlach o 1. Wyrażenie ``x += 1`` odpowiada wyrażeniu ``x = x + 1``. Pierwszy warunek wykorzystuje operator logiczny and (koniunkcję) i operator modulo ``%`` (zwraca resztę z dzielenia), aby do ciągu znaków w zmiennej ``tmp`` dodać znak końca linii (``\n``) za pomocą operatora ``+=``. W drugim warunku używamy operatora porównania ``==``.

Poniżej podano wybrane operatory dostępne w Pythonie.

**Arytmetyczne**:

- +, -, \*, /, //, %, \*\* (potęgowanie)
- znak + znak (konkatenacja napisów)
- znak * 10 (powielenie znaków)

**Przypisania**:

- =, +=, -=, *=, /=, %=, **=, //=

**Logiczne**:

- and, or, not

Fałszem logicznym są: liczby zero (0, 0.0), False, None (null), puste kolekcje ([], (), {}, set()), puste napisy. Wszystko inne jest prawdą logiczną.

**Zawierania**:

- in, not in

**Porównania**:

- ==, >, <, <>, <=, >= != (jest różne)

POĆWICZ SAM
-----------

Uprość warunek w pierwszej pętli for drukującej alfabet w porządku naturalnym tak, aby nie używać operatora modulo.
Wydrukuj co n-tą grupę liter alfabetu, przy czym wartość n podaje użytkownik. Wskazówka: użyj opcjonalnego, trzeciego argumentu funkcji ``range()``.
Sprawdź działanie różnych operatorów Pythona w konsoli.

Listy, tuple i funkcje
==========================

ZADANIE
------------

    Pobierz od użytkownika n liczb i zapisz je w liście. Wydrukuj: elementy listy i ich indeksy, elementy w odwrotnej kolejności, posortowane elementy. Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika. Usuń z listy element o podanym indeksie. Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu. Wybierz z listy elementy od indeksu i do j.

Wszystkie poniższe przykłady proponujemy wykonać w konsoli Pythona. Nie umieszczaj w konsoli komentarzy, możesz też pominąć lub skrócić komunikaty funkcji print. Można również wpisać poniższy kod do pliku i go uruchomić.

.. raw:: html

    <div class="code_no">Kod nr 2.4.1</div>

.. code-block :: python
    :linenos:

    #! /usr/bin/env python
    # -*- coding: UTF-8 -*-

    # ~/python/04_1_listy.py

    tupla = input("Podaj liczby oddzielone przecinkami: ")
    lista = [] # deklaracja pustej listy
    for i in range(len(tupla)):
        lista.append(int(tupla[i]))

    print "Elementy i ich indeksy:"
    for i, v in enumerate(lista):
        print v, "[",i,"]"

    print "Elementy w odwróconym porządku:"
    for e in reversed(lista):
        print e,

    print ""
    print "Elementy posortowane rosnąco:"
    for e in sorted(lista):
        print e,

    print ""
    e = int(raw_input("Którą liczbę usunąć? "))
    lista.remove(e)
    print lista

    a, i = input("Podaj element do dodania i indeks, przed którym ma się on znaleźć: ")
    lista.insert(i, a)
    print lista

    e = int(raw_input("Podaj liczbę, której wystąpienia w liście chcesz zliczyć? "))
    print lista.count(e)
    print "Pierwszy indeks, pod którym zapisana jest podana liczba to: "
    print lista.index(e)

    print "Pobieramy ostatni element z listy: "
    print lista.pop()
    print lista

    i, j = input("Podaj indeks początkowy i końcowy, aby uzyskać frgament listy: ")
    print lista[i:j]

JAK TO DZIAŁA
-------------

**Pojęcia**: *tupla, lista, metoda.*

Funkcja ``input()`` pobiera dane wprowadzone przez użytkownika
(tak jak ``raw_input()``), ale próbuje zinterpretować je jako kod Pythona.
Podane na wejściu liczby oddzielone przecinkami zostają więc spakowane jako
**tupla** (krotka). Jest to uporządkowana sekwencja poindeksowanych danych,
przypominająca tablicę, której wartości nie można zmieniać. Gdybyśmy chcieli
wpisać do tupli wartości od razu w kodzie, napisalibyśmy: ``tupla = (4, 3, 5)`` [#f4]_.
Listy to również uporządkowane sekwencje indeksowanych danych, zazwyczaj tego samego typu, które jednak możemy zmieniać.

.. [#f4] W definicji tupli nawiasy są opcjonalne, można więc pisać tak: ``tupla = 3, 2, 5, 8.``

Dostęp do elementów tupli lub listy uzyskujemy podając nazwę i indeks, np. ``lista[0]``.
Elementy indeksowane są od 0 (zera!). Funkcja ``len()`` zwraca ilość elementów w tupli/liście.
Funkcja ``enumerate()`` zwraca obiekt zawierający indeksy i elementy sekwencji (np. tupli lub listy) podanej jako atrybut.
Funkcja ``reversed()`` zwraca odwróconą sekwencję.

Lista ma wiele użytecznych metod: ``.append(x)`` – dodaje x do listy; ``.remove(x)`` – usuwa pierwszy x z listy;
``.insert(i, x)`` – wstawia x przed indeksem i; ``.count(x)`` – zwraca ilość wystąpień x;
``.index(x)`` – zwraca indeks pierwszego wystąpienia x; ``.pop()``
– usuwa i zwraca ostatni element listy. Funkcja ``reversed(lista)`` zwraca kopię listy w odwróconym porządku,
natomiast ``sorted(lista)`` zwraca kopię listy posortowanej rosnąco.
Jeżeli chcemy trwale odwrócić lub posortować elementy listy stosujemy metody:
``.reverse()`` i ``.sort()``. Z każdej sekwencji (napisu, tupli czy listy) możemy
wydobywać fragmenty dzięki notacji *slice* (wycinek). W najprostszym przypadku polega
ona na podaniu początkowego i końcowego (wyłącznie) indeksu elementów, które chcemy
wydobyć, np. ``lista[1:4]``.

POĆWICZ SAM
-----------

    Utwórz w konsoli Pythona dowolną listę i przećwicz notację slice. Sprawdź działanie indeksów pustych
    i ujemnych, np. ``lista[2:], lista[:4], lista[-2], lista[-2:]``.
    Posortuj dowolną listę malejąco. Wskazówka: wykorzystaj metodę ``.sort(reverse=True)``.

ZADANIE
------------

    Wypisz ciąg Fibonacciego aż do n-ego wyrazu podanego przez użytkownika.
    Ciąg Fibonacciego to ciąg liczb naturalnych, którego każdy wyraz poza dwoma
    pierwszymi jest sumą dwóch wyrazów poprzednich. Początkowe wyrazy tego ciągu to: 0 1 1 2 3 5 8 13 21

.. raw:: html

    <div class="code_no">Kod nr 2.4.4</div>

.. code-block:: python
    :linenos:

    #! /usr/bin/env python
    # -*- coding: UTF-8 -*-

    # ~/python/04_2_fibonacci.py

    def fibonacci(n): #definicja funkcji
        pwyrazy = (0, 1) #dwa pierwsze wyrazy ciągu zapisane w tupli
        a, b = pwyrazy #przypisanie wielokrotne, rozpakowanie tupli
        while a < n:
            print b
            a, b = b, a+b #przypisanie wielokrotne

    n = int(raw_input("Podaj numer wyrazu: "))
    fibonacci(n) #wywołanie funkcji
    print "" #pusta linia
    print "=" * 25 #na koniec szlaczek

JAK TO DZIAŁA
-------------

**Pojęcia**: *funkcja, zwracanie wartości, tupla, rozpakowanie tupli, przypisanie wielokrotne*.

Definicja funkcji w Pythonie polega na użyciu słowa kluczowego ``def``,
podaniu nazwy funkcji i w nawiasach okrągłych ewentualnej listy argumentów.
Definicję kończymy znakiem dwukropka, po którym wpisujemy w następnych liniach,
pamiętając o wcięciach, ciało funkcji. Funkcja może, ale nie musi zwracać wartości.
Jeżeli chcemy zwrócić jakąś wartość używamy polecenia return wartość.

Zapis ``a, b = pwyrazy`` jest przykładem rozpakowania tupli, tzn. zmienne *a* i *b*
przyjmują wartości kolejnych elementów tupli pwyrazy. Zapis równoważny, w którym nie
definiujemy tupli tylko wprost podajemy wartości, to ``a, b = 0, 1``; ten sposób
przypisania wielokrotnego stosujemy w kodzie ``a, b = b, b+a``. Jak widać, ilość
zmiennych z lewej strony musi odpowiadać liczbie wartości rozpakowywanych z tupli
lub liczbie wartości podawanych wprost z prawej strony.

POĆWICZ SAM
-----------

    Zmień funkcję ``fibonnacci()`` tak, aby zwracała wartość n-tego wyrazu. Wydrukuj tylko tę wartość w programie.

Listy, zbiory, moduły i funkcje w praktyce
=============================================

ZADANIE
-------

    Napisz program, który umożliwi wprowadzanie ocen z podanego przedmiotu ścisłego (np. fizyki), następnie policzy i wyświetla średnią, medianę i odchylenie standardowe wprowadzonych ocen. Funkcje pomocnicze i statystyczne umieść w osobnym module.

.. raw:: html

    <div class="code_no">Kod nr 2.5.1</div>

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

Klauza from moduł import funkcja umożliwia wykorzystanie w programie funkcji
zdefiniowanych w innych modułach i zapisanych w osobnych plikach. Dzięki temu
utrzymujemy przejrzystość programu głównego, a jednocześnie możemy funkcje
z modułów wykorzystywać, importując je w innych programach. Nazwa modułu
to nazwa pliku z kodem pozbawiona jednak rozszerzenia *.py*. Moduł musi
być dostępny w ścieżce przeszukiwania [#f5]_, aby można go było poprawnie dołączyć.

.. [#f5] W przypadku prostych programów zapisuj moduły w tym samym katalogu co program główny.

Instrukcja ``set()`` tworzy zbiór, czyli nieuporządkowany zestaw niepowtarzalnych (!) elementów. Instrukcje ``if przedmiot in przedmioty`` i ``if przedmiot not in przedmioty`` za pomocą operatorów zawierania ``(not) in`` sprawdzają, czy podany przedmiot już jest lub nie w zbiorze. Polecenie ``przedmioty.add()`` pozwala dodawać elementy do zbioru, przy czym jeżeli element jest już w zbiorze, nie zostanie dodany. Polecenie ``przedmioty.remove()`` usunnie podany jako argument element ze zbioru.

Oceny z wybranego przedmiotu pobieramy w pętli dopóty, dopóki użytkownik nie wprowadzi 0 (zera). Blok ``try...except`` pozwala przechwycić wyjątki, czyli w naszym przypadku niemożność przekształcenia wprowadzonej wartości na liczbę całkowitą. Jeżeli funkcja ``int()`` zwróci wyjątek, wykonywane są instrukcje w bloku ``except ValueError:``, w przeciwnym razie po sprawdzeniu poprawności oceny dodajemy ją jako liczbę zmiennoprzecinkową (typ *float*) do listy: ``oceny.append(float(ocena))``.

Metoda ``.capitalize()`` pozwala wydrukować podany napis dużą literą.

W funkcji ``print(...).format(s,m,o)`` zastosowano formatowanie drukowanych wartości, do których odwołujemy się w specyfikacji ``{0:5.2f}``. Pierwsza cyfra wskazuje, którą wartość z numerowanej od 0 (zera) listy, umieszczonej w funkcji ``format()``, wydrukować; np. aby wydrukować drugą wartość, trzeba by użyć kodu ``{1:}``.Po dwukropku podajemy szerokość pola przeznaczonego na wydruk, po kropce ilość miejsc po przecinku, symbol *f* oznacza natomiast liczbę zmiennoprzecinkową stałej precyzji.

POĆWICZ SAM
-----------

    W konsoli Pythona utwórz listę wyrazy zawierającą elementy: *abrakadabra* i *kordoba*. Utwórz zbiór *w1* poleceniem ``set(wyrazy[0])``. Oraz zbiór *w2* poleceniem ``set(wyrazy[1])``. Wykonaj kolejno polecenia: ``print w1 – w2; print w1 | w2; print w1 & w2; print w1 ^ w2``. Przykłady te ilustrują użycie klasycznych operatorów na zbiorach, czyli: różnica (-) , suma (|), przecięcie (część wspólna, &) i elementy unikalne (^).

Funkcje wykorzystywane w programie umieszczamy w osobnym pliku.

.. raw:: html

    <div class="code_no">Kod nr 2.5.4</div>

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
który wyświetlamy przed wydrukiem. Argument kom jest opcjonalny,
przypisano mu bowiem wartość domyślną, która zostanie użyta,
jeżeli użytkownik nie poda innej w wywołaniu funkcji.

Funkcja ``srednia()`` do zsumowania wartości ocen wykorzystuje funkcję ``sum()``.

Funkcja ``mediana()`` sortuje otrzymaną listę "w miejscu" (``oceny.sort()``), tzn. trwale zmienia porządek elementów [#f6]_.
W zależności od długości listy zwraca wartość środkową (długość nieparzysta)
lub średnią arytmetyczną dwóch środkowych wartości (długość).
Zapis ``oceny[half-1:half+1]`` wycina i zwraca dwa środkowe elementy
z listy, przy czym wyrażenie ``half = len(oceny)/2`` wylicza nam indeks drugiego ze środkowych elementów.

.. [#f6] Przypomnijmy: alternatywna funkcja ``sorted(lista)`` zwraca uporządkowaną rosnąco kopię listy.

W funkcja ``wariancja()`` pętla for odczytuje kolejne oceny i w kodzie ``sigma += (ocena-srednia)**2`` korzysta z operatorów skróconego dodawania (+=) i potęgowania (**), aby wyliczyć sumę kwadratów różnic kolejnych ocen i średniej.

POĆWICZ SAM
-----------

    Dopisz funkcję, która wyświetli wszystkie oceny oraz ich odchylenia od wartości średniej.

Słowniki
============

ZADANIE
-------

    Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia. Pobierz od użytkownika dane w formacie: *wyraz obcy: znaczenie1, znaczenie2, ...* itd. Pobieranie danych kończy wpisanie słowa "koniec". Podane dane zapisz w pliku. Użytkownik powinien mieć możliwość dodawania nowych i zmieniania zapisanych danych.

.. raw:: html

    <div class="code_no">Kod nr 2.6.1</div>

.. code-block:: python
    :linenos:

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # ~/python/06_slownik_02.py

    import os.path # moduł udostępniający funkcję isfile()

    print """Podaj dane w formacie:
    wyraz obcy: znaczenie1, znaczenie2
    Aby zakończyć wprowadzanie danych, podaj 0.
    """

    sFile="slownik.txt" #nazwa pliku zawierającego wyrazy i ich tłumaczenia
    slownik = {} # pusty słownik

    def otworz(plik):
        if os.path.isfile(sFile): #czy istnieje plik słownika?
            with open(sFile, "r") as sTxt: #otwórz plik do odczytu
                for line in sTxt: #przeglądamy kolejne linie
                    t = line.split(":") #rozbijamy linię na wyraz obcy i tłumaczenia
                    wobcy = t[0]
                    znaczenia = t[1].replace("\n","") #usuwamy znaki nowych linii
                    znaczenia = znaczenia.split(",") #tworzymy listę znaczeń
                    slownik[wobcy] = znaczenia #dodajemy do słownika wyrazy obce i ich znaczenia
        return len(slownik) #zwracamy ilość elementów w słowniku

    def zapisz(slownik):
        file1 = open(sFile,"w") #otwieramy plik do zapisu, istniejący plik zostanie nadpisany(!)
        for wobcy in slownik:
            znaczenia=",".join(slownik[wobcy]) # "sklejamy" znaczenia przecinkami w jeden napis
            linia = ":".join([wobcy,znaczenia])# wyraz_obcy:znaczenie1,znaczenie2,...
            print >>file1, linia # zapisujemy w pliku kolejne linie
        file1.close() #zamykamy plik

    def oczysc(str):
        str = str.strip() # usuń początkowe lub końcowe białe znaki
        str = str.lower() # zmień na małe litery
        return str

    nowy = False #zmienna oznaczająca, że użytkownik uzupełnił lub zmienił słownik
    ileWyrazow = otworz(sFile)
    print "Wpisów w bazie:", ileWyrazow

    #główna pętla programu
    while True:
        dane = raw_input("Podaj dane: ")
        t = dane.split(":")
        wobcy = t[0].strip().lower() # robimy to samo, co funkcja oczysc()
        if wobcy == 'koniec':
            break
        elif dane.count(":") == 1: #sprawdzamy poprawność wprowadzonych danych
            if wobcy in slownik:
                print "Wyraz", wobcy, " i jego znaczenia są już w słowniku."
                op = raw_input("Zastąpić wpis (t/n)? ")
            #czy wyrazu nie ma w słowniku? a może chcemy go zastąpić?
            if wobcy not in slownik or op == "t":
                znaczenia = t[1].split(",") #podane znaczenia zapisujemy w liście
                znaczenia = map(oczysc, znaczenia) #oczyszczamy elementy listy
                slownik[wobcy] = znaczenia
                nowy = True
        else:
            print "Błędny format!"

    if nowy: zapisz(slownik)

    print "="*50
    print "{0: <15}{1: <40}".format("Wyraz obcy","Znaczenia")
    print "="*50
    for wobcy in slownik:
        print "{0: <15}{1: <40}".format(wobcy,",".join(slownik[wobcy]))

JAK TO DZIAŁA
-------------

**Pojęcia**: *słownik, odczyt i zapis plików, formatowanie napisów.*

Słownik to struktura nieposortowanych danych w formacie klucz:wartość. Kluczami są najczęściej napisy, które wskazują na wartości dowolnego typu, np. inne napisy, liczby, listy, tuple itd. Notacja ``oceny = { 'polski':'1,4,2', 'fizyka':'4,3,1' }`` utworzy nam słownik ocen z poszczególnych przedmiotów.  Aby zapisać coś w słowniku stosujemy notację oceny['biologia'] = 4,2,5. Aby odczytać wartość używamy po prostu: ``oceny['polski']``.

W programie wykorzystujemy słownik, którego kluczami są obce wyrazy, natomiast wartościami są listy możliwych znaczeń. Przykładowy element naszego słownika wygląda więc tak: ``{ 'go':'iść,pojechać' }``. Natomiast ten sam element zapisany w pliku będzie miał format: *wyraz_obcy:znaczenie1,znaczeni2,...*. Dlatego funkcja ``otworz()`` przekształca format pliku na słownik, a funkcja ``zapisz()`` słownik na format pliku.

Funkcja ``otworz(plik)`` sprawdza za pomocą funkcji ``isFile(plik)`` z modułu *os.path*, czy podany plik istnieje na dysku. Polecenie ``open("plik", "r")`` otwiera podany plik w trybie do odczytu. Wyrażenie ``with ... as sTxt`` zapewnia obsługę błędów podczas dostępu do pliku (m. in. zadba o jego zamknięcie) i udostępnia zawartość pliku w zmiennej *sTxt*. Pętla ``for line in sTxt:`` odczytuje kolejne linie (czyli napisy). Metoda ``.split()`` zwraca listę zawierającą wydzielone według podanego znaku części ciągu, np.: ``t = line.split(":")``. Operacją odwrotną jest "sklejanie" w jeden ciąg elementów listy za pomocą podanego znaku, np. ",".join(slownik[wobcy]). Metoda .replace("co","czym") pozwala zastąpić w ciągu wszystkie wystąpienia *co – czym*., np.: ``znaczenia = t[1].replace("\n","")``.

Funkcja ``zapisz()`` otrzymuje słownik zawierający dane odczytane z pliku na dysku i dopisane przez użytkownika. W pętli odczytujemy klucze słownika, następnie tworzymy znaczenia oddzielone przecinkami i sklejamy je z wyrazem obcym za pomocą dwukropka. Kolejne linie za pisujemy do pliku ``print >>file1, ":".join([wobcy,znaczenia])``, wykorzystując operator ``>>`` i nazwę uchwytu pliku (*file1*).

W pętli głównej programu pobrane dane rozbite na wyraz obcy i jego znaczenia zapisujemy w liście *t*. Oczyszczamy pierwszy element tej listy zawierający wyraz obcy (``t[0].strip().lower()``) i sprawdzamy czy nie jest to słowo "koniec", jeśli tak wychodzimy z pętli wprowadzanie danych (``break``). W przeciwnym wypadku sprawdzamy metodą ``.count(":")``, czy dwukropek występuje we wprowadzonym ciągu tylko raz. Jeśli nie, format jest nieprawidłowy, w przeciwnym razie, o ile wyrazu nie ma w słowniku lub gdy chcemy go przedefiniować, tworzymy listę znaczeń. Funkcja ``map(funkcja, lista)`` do każdego elementu listy stosuje podaną jako argument funkcję (mapowanie funkcji). W naszym przypadku każde znaczenie z listy zostaje oczyszczone przez funkcję ``oczysc()``.

Na końcu drukujemy nasz słownik. Specyfikacja ``{0: <15}{1: <40}`` oznacza, że pierwszy argument umieszczony w funkcji ``format()``, drukowany ma być wyrównany do lewej (<) w polu o szerokości 15 znaków, drugi argument, również wyrównany do lewej, w polu o szerokości 40 znaków.

POĆWICZ SAM
-----------

    Kod drukujący słownik zamień w funkcję. Wykorzystaj ją do wydrukowania słownika odczytanego z dysku i słownika uzupełnionego przez użytkownika.

    Spróbuj zmienić program tak, aby umożliwiał usuwanie wpisów.

    Dodaj do programu możliwość uczenia się zapisanych w słowniku słówek. Niech program wyświetla kolejne słowa obce i pobiera od użytkownika możliwe znaczenia. Następnie powinien wyświetlać, które z nich są poprawne.

Znam Pythona
=================

ZADANIE
-------

    Przeanalizuj podane kody dwóch programów i spróbuj sam zrozumieć, jak działają i wprowadź sugerowane zmiany.

Pierwszy program na podstawie danych pobranych od użytkownika sprawdza m. in., czy da się zbudować trójkąt.

.. raw:: html

    <div class="code_no">Kod nr 2.7.1</div>

.. code-block:: python
    :linenos:

    #! /usr/bin/env python
    # -*- coding: UTF-8 -*-

    # ~/python/07_1_trojkat.py

    import math

    #a, b, c = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")
    # można też tak:
    #a, b, c = [int(x) for x in raw_input("Podaj 3 boki trójkąta (oddzielone spacjami): ").split()]
    if a+b > c and a+c > b and b+c > a:
        print "Z podanych boków można zbudować trójkąt."
        if ((a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2):
            print "Do tego prostokątny!"
        
        print "Obwód wynosi:", (a+b+c)
        p = 0.5 * (a + b + c) #współczynnik wzoru Herona
        P = math.sqrt(p*(p-a)*(p-b)*(p-c)) #pole ze wzoru Herona
        print "Pole wynosi:", P
    else:
        print "Z podanych odcinków nie można utworzyć trójkąta prostokątnego."


POĆWICZ SAM
-----------

    Zmień program tak, aby użytkownik w przypadku podania boków, z których trójkąta zbudować się nie da, mógł spróbować kolejny raz.

Drugi program jest przykładem implementacji szyfru Cezara.

.. raw:: html

    <div class="code_no">Kod nr 2.7.3</div>

.. code-block:: python
    :linenos:

    #! /usr/bin/env python
    # -*- coding: UTF-8 -*-

    # ~/python/07_2_szyfr_cezara.py

    KLUCZ = 3

    def szyfruj(txt):
        stxt = ""
        for i in range(len(txt)):
            if ord(txt[i]) > 122 - KLUCZ:
                stxt += chr(ord(txt[i]) + KLUCZ - 26)
            else:
                stxt += chr(ord(txt[i]) + KLUCZ)
        return stxt;

    utxt = raw_input("Podaj ciąg do zaszyfrowania:\n")
    stxt = szyfruj(utxt)
    print "Ciąg zaszyfrowany:\n", stxt

POĆWICZ SAM
-----------

    Napisz funkcję deszyfrującą ``deszyfruj(txt)``. Dodaj do funkcji ``szyfruj(), deszyfruj()`` drugi parametr w postaci długości klucza podawanej przez użytkownika. Dodaj poprawne szyfrowanie dużych liter, obsługę białych znaków i znaków interpunkcyjnych.

Nie znam Pythona... jeszcze
=================================

ZADANIE
-------

Wypróbuj w konsoli podane przykłady ułatwień (ang. comprehensions) Pythona:

.. raw:: html

    <div class="code_no">Kod nr 2.8.1</div>

.. code-block:: python
    :linenos:

    # Przykład tzw. list comprehensions
    # lista kwadratów liczb od 0 do 9
    [x**2 for x in range(10)]
    # lista dwuwymiarowa [20,40] o wartościach a
    a = int(raw_input("Podaj liczbę całkowtią: "))
    [[a for y in xrange(20)] for x in xrange(40)]
    # lista krotek (x, y), przy czym x != y
    [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

Lista pojęć
-----------
- *zmienna, wartość, wyrażenie, wejście i wyjście danych, instrukcja warunkowa, komentarz*;
- *pętla, obiekt, metoda, instrukcja warunkowa zagnieżdżona, formatowanie kodu*;
- *iteracja, kod ASCII, lista, inkrementacja, operatory arytmetyczne, logiczne, przypisania, porównania i zawierania*;
- *tupla, lista, metoda, funkcja, zwracanie wartości, pakowanie i rozpakowanie tupli, przypisanie wielokrotne*;
- *import, moduł, zbiór, przechwytywanie wyjątków, formatowanie napisów i danych na wyjściu*;
- *funkcja, argumenty funkcji, zwracanie wartości*;
- *słownik, odczyt i zapis plików*.

Materiały pomocnicze
--------------------

1. http://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie
2. http://brain.fuw.edu.pl/edu/TI:Programowanie_z_Pythonem
3. http://pl.python.org/docs/tut/
4. http://en.wikibooks.org/wiki/Python_Programming/Input_and_Output
5. https://wiki.python.org/moin/HandlingExceptions
6. http://learnpython.org/pl
7. http://www.checkio.org
8. http://www.codecademy.com
9. https://www.coursera.org

Metryka
^^^^^^^

:Autorzy: Robert Bednarz <rob@lo1.sandomierz.pl>,
          Janusz Skonieczny <js@bravelabs.pl>

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>
