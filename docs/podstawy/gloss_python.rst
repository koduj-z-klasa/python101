
.. glossary::

    język interpretowany
        język, który jest tłumaczony i wykonywany "w locie", np. Python lub PHP.
        Tłumaczeniem i wykonywaniem programu zajmuje się specjalny program
        nazwany interpreterem języka.

    interpreter
        program, który analizuje kod źródłowy, a następnie go wykonuje. Interpretery są
        podstawowym składnikiem języków wykorzystywanych do pisania skryptów wykonywanych
        po stronie klienta WWW (JavaScript) lub serwera (np. Python, PHP).

        Interpreter Pythona jest interaktywny, tzn. można w nim wydawać
        polecenia i obserwować ich działanie, co pozwala wygodnie uczyć się
        i testować oprogramowanie. Uruchamiany jest w terminalu, zazwyczaj
        za pomocą polecenia ``python``.

    formatowanie kodu
        Python wymaga formatowania kodu za pomocą wcięć, podstawowym wymogiem
        jest stosowanie takich samych wcięć w obrębie pliku, np. 4 spacji
        i ich wielokrotności. Wcięcia odpowiadają nawiasom w innych językach,
        służą grupowaniu instrukcji i wydzielaniu bloków kodu.
        Błędy wcięć zgłaszane są jako ``IndentationError``.

    zmienna
        nazwa określająca jakąś zapamiętywaną i wykorzystywaną w programie wartość
        lub strukturę danych. Zmienna może przechowywać pojedyncze wartości
        określonego typu, np.: ``imie = "Anna"``, jak i rozbudowane struktury
        danych, np.: ``imiona = ('Ala', 'Ola', 'Ela')``. W nazwach zmiennych
        nie używamy znaków narodowych, nie rozpoczynamy ich od cyfr.

    lista
        jedna z podstawowych struktur danych, indeksowana sekwencja takich samych
        lub różnych elementów, które można zmieniać. Przypomina tabele z innych
        języków programowania. Np. ``imiona = ['Ala', 'Ola', 'Ela']``.

    tupla
        podbnie jak lista, zawiera indeksowaną sekwencję takich samych lub
        różnych elementów, ale nie można ich zmieniać. Często służy do
        przechowywania lub przekazywania ustawień, stałych wartości itp.
        Np. ``imiona = ('Ala', 'Ola', 'Ela')``. 1-elementową tuplę należy
        zapisywać z dodatkowym przecinkiem: ``tupla1 = (1,)``.

    zbiór
        nieuporządkowany, nieindeksowany zestaw elementów tego samego lub
        różnych typów, nie może zawierać duplikatów, obsługuje charakterystyczne
        dla zbiorów operacje: sumę, iloczyn oraz różnicę.
        Np. ``imiona = set(['Ala', 'Ola', 'Ela'])``.

    słownik
        zestaw par elementów w postaci klucz:wartość. Zarówno klucze,
        jak i wartości mogą być tego samego lub różnych typów. Największą
        zaletą słownika jest to, że klucze mogą być ciągami znaków.
        Np. ``osoby = {'Ala': 'Lipiec' , 'Ola': 'Maj', 'Ela': 'Styczeń'}``.

    instrukcja warunkowa
        podstawowa konstrukcja w programowaniu, wykorzystuje wyrażenie logiczne
        przyjmujące wartość True (prawda) lub False (fałsz) do wyboru
        odpowiedniego działania. Umożliwia rozgałezianie kodu.
        Np.:

.. code-block:: python

    if wiek < 18:
        print "Treść zabroniona"
    else:
        print "Zapraszamy"

    pętla
        podstawowa konstrukcja w programowaniu, umożliwia powtarzanie fragmentów
        kodu zadaną ilość razy (pętla ``for``) lub dopóki podane wyrażenie
        logiczne jest prawdziwe (pętla ``while``).

.. code-block:: python

    for i in range(11):
        print i
