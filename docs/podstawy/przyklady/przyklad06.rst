.. _slownik-slowek:

Słownik słówek
##############

**ZADANIE**: Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia. Pobierz od użytkownika dane w formacie: *wyraz obcy: znaczenie1, znaczenie2, ...* itd. Pobieranie danych kończy wpisanie słowa "koniec". Podane dane zapisz w pliku. Użytkownik powinien mieć możliwość dodawania nowych i zmieniania zapisanych danych.

**POJĘCIA**: *słownik, odczyt i zapis plików, formatowanie napisów.*

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 06_slownik_02.py
    :linenos:

Słownik to struktura nieuporządkowanych danych w formacie klucz:wartość. Kluczami są najczęściej napisy, które wskazują na wartości dowolnego typu, np. inne napisy, liczby, listy, tuple itd. Notacja ``oceny = { 'polski':'1,4,2', 'fizyka':'4,3,1' }`` utworzy nam słownik ocen z poszczególnych przedmiotów.  Aby zapisać coś w słowniku stosujemy notację ``oceny['biologia'] = 4,2,5``. Aby odczytać wartość używamy po prostu: ``oceny['polski']``.

W programie wykorzystujemy słownik, którego kluczami są obce wyrazy, natomiast wartościami są listy możliwych znaczeń. Przykładowy element naszego słownika wygląda więc tak: ``{ 'go':'iść,pojechać' }``. Natomiast ten sam element zapisany w pliku będzie miał format: *wyraz_obcy:znaczenie1,znaczeni2,...*. Dlatego funkcja ``otworz()`` przekształca format pliku na słownik, a funkcja ``zapisz()`` słownik na format pliku.

Funkcja ``otworz(plik)`` sprawdza za pomocą funkcji ``isFile(plik)`` z modułu *os.path*, czy podany plik istnieje na dysku. Polecenie ``open("plik", "r")`` otwiera podany plik w trybie do odczytu. Wyrażenie ``with ... as sTxt`` zapewnia obsługę błędów podczas dostępu do pliku (m. in. zadba o jego zamknięcie) i udostępnia zawartość pliku w zmiennej *sTxt*. Pętla ``for line in sTxt:`` odczytuje kolejne linie (czyli napisy). Metoda ``.split()`` zwraca listę zawierającą wydzielone według podanego znaku części ciągu, np.: ``t = line.split(":")``. Operacją odwrotną jest "sklejanie" w jeden ciąg elementów listy za pomocą podanego znaku, np. ``",".join(slownik[wobcy])``. Metoda ``.replace("co","czym")`` pozwala zastąpić w ciągu wszystkie wystąpienia *co – czym*., np.: ``znaczenia = t[1].replace("\n","")``.

Funkcja ``zapisz()`` otrzymuje słownik zawierający dane odczytane z pliku na dysku i dopisane przez użytkownika. W pętli odczytujemy klucze słownika, następnie tworzymy znaczenia oddzielone przecinkami i sklejamy je z wyrazem obcym za pomocą dwukropka. Kolejne linie za pisujemy do pliku ``print >>file1, ":".join([wobcy,znaczenia])``, wykorzystując operator ``>>`` i nazwę uchwytu pliku (*file1*).

W pętli głównej programu pobrane dane rozbite na wyraz obcy i jego znaczenia zapisujemy w liście *t*. Oczyszczamy pierwszy element tej listy zawierający wyraz obcy (``t[0].strip().lower()``) i sprawdzamy czy nie jest to słowo "koniec", jeśli tak wychodzimy z pętli wprowadzanie danych (``break``). W przeciwnym wypadku sprawdzamy metodą ``.count(":")``, czy dwukropek występuje we wprowadzonym ciągu tylko raz. Jeśli nie, format jest nieprawidłowy, w przeciwnym razie, o ile wyrazu nie ma w słowniku lub gdy chcemy go przedefiniować, tworzymy listę znaczeń. Funkcja ``map(funkcja, lista)`` do każdego elementu listy stosuje podaną jako argument funkcję (mapowanie funkcji). W naszym przypadku każde znaczenie z listy zostaje oczyszczone przez funkcję ``oczysc()``.

Na końcu drukujemy nasz słownik. Specyfikacja ``{0: <15}{1: <40}`` oznacza, że pierwszy argument umieszczony w funkcji ``format()``, drukowany ma być wyrównany do lewej (<) w polu o szerokości 15 znaków, drugi argument, również wyrównany do lewej, w polu o szerokości 40 znaków.

Zadania dodatkowe
*****************

- Kod drukujący słownik zamień w funkcję. Wykorzystaj ją do wydrukowania słownika odczytanego z dysku i słownika uzupełnionego przez użytkownika.
- Spróbuj zmienić program tak, aby umożliwiał usuwanie wpisów.
- Dodaj do programu możliwość uczenia się zapisanych w słowniku słówek. Niech program wyświetla kolejne słowa obce i pobiera od użytkownika możliwe znaczenia. Następnie powinien wyświetlać, które z nich są poprawne.
