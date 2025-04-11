Słownik Pythona
################

.. glossary::

    blok kodu
        ciąg kolejnych instrukcji wyodrębniany za pomocą wcięć, czyli należących do tego samego poziomu wcięcia;
        dobrym przykładem są bloki kodu w instrukcjach warunkowych lub iteracyjnych

    filtrowanie danych
        selekcja danych na podstawie jakichś kryteriów

    formatowanie kodu
        Python wymaga formatowania kodu za pomocą wcięć, podstawowym wymogiem
        jest stosowanie takich samych wcięć w obrębie pliku, np. 4 spacji
        i ich wielokrotności. Wcięcia odpowiadają nawiasom w innych językach,
        służą grupowaniu instrukcji i wydzielaniu bloków kodu.
        Błędy wcięć zgłaszane są jako wyjątki ``IndentationError``.

    funkcja
        blok często wykonywanego kodu wydzielony słowem kluczowym ``def``,
        opatrzony unikalną w danym zasięgu nazwą; może przyjmować dane
        i zwracać wartości za pomocą słowa kluczowego ``return``.

    generatory wyrażeń
        (ang. *generator expressions*) – zwięzły w notacji sposób tworzenia
        iteratorów według składni: ``( wyrażenie for wyraz in sekwencja if warunek )``


    instrukcja warunkowa
        podstawowa konstrukcja w programowaniu, wykorzystuje wyrażenie logiczne
        przyjmujące wartość ``True`` (prawda) lub ``False`` (fałsz) do wyboru
        odpowiedniego działania. Umożliwia rozgałęzianie kodu.
        W najprostszej postaci sprawdza, czy warunek jest prawdziwy i wykonuje działanie:

.. code-block:: python

    if wiek < 18:
        print("Treść zabroniona")

.. glossary::

        Klauzula ``else`` ("w przeciwnym razie") pozwala określić działanie, gdy warunek jest fałszywy:


.. code-block:: python

    if wiek < 18:
        print("Treść zabroniona")
    else:
        print("Zapraszamy")

.. glossary::

    interpreter
        program, który analizuje kod źródłowy, a następnie go wykonuje. Interpretery są
        podstawowym składnikiem języków wykorzystywanych do pisania skryptów wykonywanych
        po stronie klienta WWW (JavaScript) lub serwera (np. Python, PHP).

        Interpreter Pythona jest interaktywny, tzn. można w nim wydawać
        polecenia i obserwować ich działanie, co pozwala wygodnie uczyć się
        i testować oprogramowanie. Uruchamiany jest w terminalu, zazwyczaj
        za pomocą polecenia ``python``.

    iteratory
        (ang. *iterators*) – obiekt reprezentujący sekwencję danych,
        zwracający z niej po jednym elemencie na raz przy użyciu metody
        ``next()``; jeżeli nie ma następnego elementu, zwracany jest wyjątek
        ``StopIteration``. Funkcja ``iter()`` potrafi zwrócić iterator
        z podanego obiektu.

    język interpretowany
        język, który jest tłumaczony i wykonywany "w locie", np. Python lub PHP.
        Tłumaczeniem i wykonywaniem programu zajmuje się specjalny program
        nazwany interpreterem języka.

    lista
        jedna z podstawowych struktur danych, indeksowana sekwencja takich samych
        lub różnych elementów, które można zmieniać. Przypomina tabele z innych
        języków programowania. Np. ``imiona = ['Ala', 'Ola', 'Ela']``.
        Deklaracja pustej listy: ``lista = []``.

    mapowanie funkcji
        w kontekście funkcji ``map()`` oznacza zastosowanie danej funkcji
        do wszystkich dostarczonych wartości

    moduł
        plik zawierający wiele zazwyczaj często używanych w wielu programach
        funkcji lub klas; zanim skorzystamy z zawartych w nim fragmentów kodu,
        trzeba je lub cały moduł zaimportować za pomocą słowa kluczowego
        ``import``.

    notacja wycinkowa
        (ang. *slice notation*) pojedyncze elementy wszystkich sekwencji takich jak
        napisy, listy, tuple są indeksowane zaczynając od 0, odczytujemy je za pomocą indeksu,
        np.: ``napis[0]``; możliwe jest również odczytanie kilku elementów sekwencji
        naraz, w najprostszej postacji trzeba określić indeks pierwszego i ostatniego
        (niewliczanego) elementu, np. ``napis[1:5]``.

    operatory
        **Arytmetyczne**: +, -, \*, /, //, %, \*\* (potęgowanie); znak + znak (konkatenacja napisów); znak * 10 (powielenie znaków);
        **Przypisania**: =, +=, -=, \*=, /=, %=, \*\*=, //=;
        **Logiczne**: and, or, not; Fałszem logicznym są: liczby zero (0, 0.0), False, None (null), puste kolekcje ([], (), {}, set()), puste napisy. Wszystko inne jest prawdą logiczną.
        **Zawierania**: in, not in;
        **Porównania**: ==, >, <, <>, <=, >= != (jest różne).

        Operator * rozpakowuję listę paramterów przekazaną funkcji.
        Operator ** rozpakuje słownik.

    pętla
        podstawowa konstrukcja w programowaniu, umożliwia powtarzanie fragmentów
        kodu zadaną ilość razy (pętla ``for``) lub dopóki podane wyrażenie
        logiczne jest prawdziwe (pętla ``while``). Należy zadbać, aby pętla
        była skończona za pomocą odpowiedniego warunku lub instrukcji przeywającej
        powtarzanie. Np.:

.. code-block:: python

    for i in range(11):
        print i

.. glossary::

    serializacja
        proces przekształcania obiektów w strumień znaków lub bajtów,
        który można zapisać w pliku (bazie) lub przekazać do innego programu.

    słownik
        typ mapowania, zestaw par elementów w postaci "klucz: wartość". Kluczami mogą być
        liczby, ciągi znaków czy tuple. Wartości mogą być tego samego lub
        różnych typów. Np. ``osoby = {'Ala': 'Lipiec' , 'Ola': 'Maj', 'Ela': 'Styczeń'}``.
        Dane ze słownika łatwo wydobyć: ``slownik['klucz']``,
        lub zmienić: ``slownik['klucz'] = wartosc``.
        Deklaracja pustego słownika: ``slownik = dict()``.

    tupla
        podbnie jak lista, zawiera indeksowaną sekwencję takich samych lub
        różnych elementów, ale nie można ich zmieniać. Często służy do
        przechowywania lub przekazywania ustawień, stałych wartości itp.
        Np. ``imiona = ('Ala', 'Ola', 'Ela')``. 1-elementową tuplę należy
        zapisywać z dodatkowym przecinkiem: ``tupla1 = (1,)``.

    typ danych
        W Pythonie wszystkie dane, tj. przypisane do nazw wartości, są obiektami określonego typu.
        Typ definiuje m.in. operacje, które można wykonać na danych wartościach.
        W pewnym uproszczeniu podstawowe typy danych to:
        *string* – napis (łańcuch znaków), podtyp sekwencji;
        *integer* – dodatnie i ujemne liczby całkowite;
        *float* – liczby zmiennoprzecinkowe (separatorem jest kropka);
        *boolean* – wartości logiczne `True` (prawda, 1) lub `False` (fałsz, 0), podtyp
        typu całkowitego.

    wejście
        Domyślnym wejściem dla programów uruchamianych w terminalu jest klawiatura. Wszystkie dane wprowadzane z
        klawiatury traktowane są jako znaki.

    wyjście
        Domyślnym wyjściem dla programów uruchamianych w terminalu jest ekran, na którym wypisywane są komunikaty
        i wyniki działania programu.

    wyjątki
        to komunikaty zgłaszane przez interpreter Pythona, pozwalające ustalić
        przyczyny błędnego działania kodu.

    wyrażenia lambda
        zwane czasem *funkcjami lambda*, mechanizm pozwalający zwięźle
        zapisywać proste funkcje w postaci pojedynczych wyrażeń

    wyrażenie listowe
        (ang. *list comprehensions*) – efektywny sposób tworzenia list na podstawie
        elementów dowolnych sekwencji, na których wykonywane są te same operacje
        i które opcjonalnie spełniają określone warunki. Składnia:
        ``[ wyrażenie for wyraz in sekwencja if warunek ]``

    wyrażenie logiczne
        wyrażenie, którego obliczona wartość to prawda (``True``) lub fałsz (``False``)

    zbiór
        nieuporządkowany, nieindeksowany zestaw elementów tego samego lub
        różnych typów, nie może zawierać duplikatów, obsługuje charakterystyczne
        dla zbiorów operacje: sumę, iloczyn oraz różnicę.
        Np. ``imiona = set(['Ala', 'Ola', 'Ela'])``. Deklaracja pustego zbioru:
        ``zbior = set()``.

    zmienna
        nazwa powiązana z zapamiętaną i wykorzystywaną w programie wartością
        lub strukturą danych. Zmienna może przechowywać pojedyncze wartości
        określonego typu, np. ciąg znaków: ``imie = "Anna"``, jak i rozbudowane struktury
        danych, np. listę ciągów znaków: ``imiona = ['Ala', 'Ola', 'Ela']``.
        W nazwach zmiennych nie używamy znaków narodowych, nie rozpoczynamy ich od cyfr,
        w nazwach wielowyrazowych używamy znaku podkreślenia `_`, np. `moje_imie`.

    zmienna iteracyjna
        zmienna występująca w pętli, której wartość zmienia się, najczęściej
        jest zwiększana (inkremntacja) o 1, w każdym wykonaniu pętli.
        Może pełnić rolę "licznika" powtórzeń lub być elementem wyrażenia
        logicznego wyznaczającego koniec działania pętli.
