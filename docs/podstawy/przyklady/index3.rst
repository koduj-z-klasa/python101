Zbiory i słowniki
#######################

.. contents::
    :depth: 1
    :local:

Oceny z przedmiotów
***********************

    **ZADANIE**: Napisz program, który umożliwi wprowadzanie ocen z podanego przedmiotu ścisłego (np. fizyki), następnie policzy i wyświetla średnią, medianę i odchylenie standardowe wprowadzonych ocen. Funkcje pomocnicze i statystyczne umieść w osobnym module.
    
    **POJĘCIA**: *import, moduł, zbiór, przechwytywanie wyjątków, formatowanie napisów i danych na wyjściu, argumenty funkcji, zwracanie wartości*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 05_oceny_03.py
    :linenos:

Jak to działa
===================

Klauza ``from moduł import funkcja`` umożliwia wykorzystanie w programie funkcji zdefiniowanych w innych modułach i zapisanych w osobnych plikach. Dzięki temu utrzymujemy przejrzystość programu głównego, a jednocześnie możemy funkcje z modułów wykorzystywać, importując je w innych programach. Nazwa modułu to nazwa pliku z kodem pozbawiona jednak rozszerzenia *.py*. Moduł musi być dostępny w ścieżce przeszukiwania, aby można go było poprawnie dołączyć.

.. note::
    W przypadku prostych programów zapisuj moduły w tym samym katalogu co program główny.

Instrukcja ``set()`` tworzy zbiór, czyli nieuporządkowany zestaw niepowtarzalnych (!) elementów. Instrukcje ``if przedmiot in przedmioty`` i ``if przedmiot not in przedmioty`` za pomocą operatorów zawierania ``(not) in`` sprawdzają, czy podany przedmiot już jest lub nie w zbiorze. Polecenie ``przedmioty.add()`` pozwala dodawać elementy do zbioru, przy czym jeżeli element jest już w zbiorze, nie zostanie dodany. Polecenie ``przedmioty.remove()`` usunnie podany jako argument element ze zbioru.

Oceny z wybranego przedmiotu pobieramy w pętli dopóty, dopóki użytkownik nie wprowadzi 0 (zera). Blok ``try...except`` pozwala przechwycić wyjątki, czyli w naszym przypadku niemożność przekształcenia wprowadzonej wartości na liczbę całkowitą. Jeżeli funkcja ``int()`` zwróci wyjątek, wykonywane są instrukcje w bloku ``except ValueError:``, w przeciwnym razie po sprawdzeniu poprawności oceny dodajemy ją jako liczbę zmiennoprzecinkową (typ *float*) do listy: ``oceny.append(float(ocena))``.

Metoda ``.capitalize()`` pozwala wydrukować podany napis dużą literą.

W funkcji ``print(...).format(s,m,o)`` zastosowano formatowanie drukowanych wartości, do których odwołujemy się w specyfikacji ``{0:5.2f}``. Pierwsza cyfra wskazuje, którą wartość z numerowanej od 0 (zera) listy, umieszczonej w funkcji ``format()``, wydrukować; np. aby wydrukować drugą wartość, trzeba by użyć kodu ``{1:}``.Po dwukropku podajemy szerokość pola przeznaczonego na wydruk, po kropce ilość miejsc po przecinku, symbol *f* oznacza natomiast liczbę zmiennoprzecinkową stałej precyzji.

**FUNKCJE** wykorzystywane w programie **oceny**, umieszczamy w osobnym pliku ``ocenyfun.py``.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: ocenyfun.py
    :linenos:

Jak to działa
===================

Klauzula ``import math`` udostępnia w pliku wszystkie metody z modułu
matematycznego, dlatego musimy odwoływać się do nich za pomocą notacji
moduł.funkcja, np.: ``math.sqrt()`` – zwraca pierwiastek kwadratowy.

Funkcja ``drukuj(co, kom="...")`` przyjmuje dwa argumenty, *co* – listę
lub zbiór, który drukujemy w pętli for, oraz *kom* – komunikat,
który wyświetlamy przed wydrukiem. Argument *kom* jest opcjonalny,
przypisano mu bowiem wartość domyślną, która zostanie użyta,
jeżeli użytkownik nie poda innej w wywołaniu funkcji.

Funkcja ``srednia()`` do zsumowania wartości ocen wykorzystuje funkcję ``sum()``.

Funkcja ``mediana()`` sortuje otrzymaną listę "w miejscu" (``oceny.sort()``), tzn. trwale zmienia porządek elementów.
W zależności od długości listy zwraca wartość środkową (długość nieparzysta)
lub średnią arytmetyczną dwóch środkowych wartości (długość).
Zapis ``oceny[half-1:half+1]`` wycina i zwraca dwa środkowe elementy
z listy, przy czym wyrażenie ``half = len(oceny)/2`` wylicza nam indeks drugiego ze środkowych elementów.

.. note::
    Przypomnijmy: alternatywna funkcja ``sorted(lista)`` zwraca uporządkowaną rosnąco kopię listy.

W funkcja ``wariancja()`` pętla for odczytuje kolejne oceny i w kodzie ``sigma += (ocena-srednia)**2`` korzysta z operatorów skróconego dodawania (+=) i potęgowania (**), aby wyliczyć sumę kwadratów różnic kolejnych ocen i średniej.

Zadania dodatkowe
===================

    W konsoli Pythona utwórz listę ``wyrazy`` zawierającą elementy: *abrakadabra* i *kordoba*. Utwórz zbiór *w1* poleceniem ``set(wyrazy[0])``. Oraz zbiór *w2* poleceniem ``set(wyrazy[1])``. Wykonaj kolejno polecenia: ``print w1 – w2; print w1 | w2; print w1 & w2; print w1 ^ w2``. Przykłady te ilustrują użycie klasycznych operatorów na zbiorach, czyli: różnica (-) , suma (|), przecięcie (część wspólna, &) i elementy unikalne (^).
    W pliku ``ocenyfun.py`` dopisz funkcję, która wyświetli wszystkie oceny oraz ich odchylenia od wartości średniej.

Słownik słówek
***********************

    **ZADANIE**: Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia. Pobierz od użytkownika dane w formacie: *wyraz obcy: znaczenie1, znaczenie2, ...* itd. Pobieranie danych kończy wpisanie słowa "koniec". Podane dane zapisz w pliku. Użytkownik powinien mieć możliwość dodawania nowych i zmieniania zapisanych danych.
    
    **POJĘCIA**: *słownik, odczyt i zapis plików, formatowanie napisów.*

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 06_slownik_02.py
    :linenos:

Jak to działa
===================

Słownik to struktura nieposortowanych danych w formacie klucz:wartość. Kluczami są najczęściej napisy, które wskazują na wartości dowolnego typu, np. inne napisy, liczby, listy, tuple itd. Notacja ``oceny = { 'polski':'1,4,2', 'fizyka':'4,3,1' }`` utworzy nam słownik ocen z poszczególnych przedmiotów.  Aby zapisać coś w słowniku stosujemy notację ``oceny['biologia'] = 4,2,5``. Aby odczytać wartość używamy po prostu: ``oceny['polski']``.

W programie wykorzystujemy słownik, którego kluczami są obce wyrazy, natomiast wartościami są listy możliwych znaczeń. Przykładowy element naszego słownika wygląda więc tak: ``{ 'go':'iść,pojechać' }``. Natomiast ten sam element zapisany w pliku będzie miał format: *wyraz_obcy:znaczenie1,znaczeni2,...*. Dlatego funkcja ``otworz()`` przekształca format pliku na słownik, a funkcja ``zapisz()`` słownik na format pliku.

Funkcja ``otworz(plik)`` sprawdza za pomocą funkcji ``isFile(plik)`` z modułu *os.path*, czy podany plik istnieje na dysku. Polecenie ``open("plik", "r")`` otwiera podany plik w trybie do odczytu. Wyrażenie ``with ... as sTxt`` zapewnia obsługę błędów podczas dostępu do pliku (m. in. zadba o jego zamknięcie) i udostępnia zawartość pliku w zmiennej *sTxt*. Pętla ``for line in sTxt:`` odczytuje kolejne linie (czyli napisy). Metoda ``.split()`` zwraca listę zawierającą wydzielone według podanego znaku części ciągu, np.: ``t = line.split(":")``. Operacją odwrotną jest "sklejanie" w jeden ciąg elementów listy za pomocą podanego znaku, np. ``",".join(slownik[wobcy])``. Metoda ``.replace("co","czym")`` pozwala zastąpić w ciągu wszystkie wystąpienia *co – czym*., np.: ``znaczenia = t[1].replace("\n","")``.

Funkcja ``zapisz()`` otrzymuje słownik zawierający dane odczytane z pliku na dysku i dopisane przez użytkownika. W pętli odczytujemy klucze słownika, następnie tworzymy znaczenia oddzielone przecinkami i sklejamy je z wyrazem obcym za pomocą dwukropka. Kolejne linie za pisujemy do pliku ``print >>file1, ":".join([wobcy,znaczenia])``, wykorzystując operator ``>>`` i nazwę uchwytu pliku (*file1*).

W pętli głównej programu pobrane dane rozbite na wyraz obcy i jego znaczenia zapisujemy w liście *t*. Oczyszczamy pierwszy element tej listy zawierający wyraz obcy (``t[0].strip().lower()``) i sprawdzamy czy nie jest to słowo "koniec", jeśli tak wychodzimy z pętli wprowadzanie danych (``break``). W przeciwnym wypadku sprawdzamy metodą ``.count(":")``, czy dwukropek występuje we wprowadzonym ciągu tylko raz. Jeśli nie, format jest nieprawidłowy, w przeciwnym razie, o ile wyrazu nie ma w słowniku lub gdy chcemy go przedefiniować, tworzymy listę znaczeń. Funkcja ``map(funkcja, lista)`` do każdego elementu listy stosuje podaną jako argument funkcję (mapowanie funkcji). W naszym przypadku każde znaczenie z listy zostaje oczyszczone przez funkcję ``oczysc()``.

Na końcu drukujemy nasz słownik. Specyfikacja ``{0: <15}{1: <40}`` oznacza, że pierwszy argument umieszczony w funkcji ``format()``, drukowany ma być wyrównany do lewej (<) w polu o szerokości 15 znaków, drugi argument, również wyrównany do lewej, w polu o szerokości 40 znaków.

Zadania dodatkowe
===================

    Kod drukujący słownik zamień w funkcję. Wykorzystaj ją do wydrukowania słownika odczytanego z dysku i słownika uzupełnionego przez użytkownika.
    Spróbuj zmienić program tak, aby umożliwiał usuwanie wpisów.
    Dodaj do programu możliwość uczenia się zapisanych w słowniku słówek. Niech program wyświetla kolejne słowa obce i pobiera od użytkownika możliwe znaczenia. Następnie powinien wyświetlać, które z nich są poprawne.

Metryka
===================

:Autor: Robert Bednarz <ecg@ecg.vot.pl>

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>

.. include:: ../../copyright.rst
