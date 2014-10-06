Mów mi Python – wprowadzenie do języka Python
*********************************************

Słowniki
============

ZADANIE
-------

    Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia. Pobierz od użytkownika dane w formacie: *wyraz obcy: znaczenie1, znaczenie2, ...* itd. Pobieranie danych kończy wpisanie słowa "koniec". Podane dane zapisz w pliku. Użytkownik powinien mieć możliwość dodawania nowych i zmieniania zapisanych danych.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

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
