Znam Pythona?
#######################

.. contents::
    :depth: 1
    :local:

Trójkąt
***********************

    **ZADANIE**: Napisz program, który na podstawie danych pobranych od użytkownika, czyli długości boków, sprawdza, czy da się zbudować trójkąt
    i czy jest to trójkąt prostokątny. Jeżeli da się zbudować trójkąt, należy wydrukować jego obwód i pole, w przeciwnym wypadku
    komunikat, że nie da się utworzyć trójkąta.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 07_trojkat_01.py
    :linenos:

Jak to działa
===================

Pętla ``while`` wykonuje się dopóki warunek jest prawdziwy, czyli zmienna kontrolna "op" różna jest od "n". Dzięki temu użytkownik może wielokrotnie wprowadzać wartości boków tworzące trójkąt.
	
Są dwie metody pobierania kilku wartości z wejścia (np. klawiatury) na raz. 
Funkcja ``raw_input()`` zwraca wprowadzone dane zakończone nową linią jako napis.
Funkcja ``input()`` wartości pobrane z wejścia (np. klawiatury) traktuje jak kod Pythona.
Konstrukcja ``int(x) for x in raw_input().split()`` (przykład tzw. wyrażenia listowego) wywołuje funkcję ``int()``, która
usiłuje przekształcić podaną wartość na liczbę całkowitą dla każdej
wartości wyodrębnionej z ciągu wejściowego przez funkcję ``split()``. Separatorem
kolejnych wartości są dla funkcji ``split()`` białe znaki (spacje, tabulatory).
Funkcja ``input()`` pobiera wejście w postaci napisu, ale próbuje zinterpretować go
jakby był częścią kodu w Pythonie. Dlatego dane oddzielone przecinkami w postaci
np. "1, 2, 3" przypisywane są podanym zmiennym.

Funkcje ``if`` sprawdzają warunki złożone oparte na koniunkcji (``and``) i alternatywie (``or``).
Wyrażenie ``x**y`` oznacza podnoszenie podstawy ``x`` do potęgi ``y``.
Funkcja ``sqrt()`` (pierwiastek kwadratowy) zawarta jest w module ``math``, który na początku
programu trzeba zaimportować.

Zadania dodatkowe
===================

    Zmień program tak, aby użytkownik w przypadku podania boków, z których trójkąta zbudować się nie da, mógł spróbować kolejny raz.

Szyfr Cezara
***********************

    **ZADANIE**: Napisz program, który podany przez użytkownika ciąg znaków szyfruje przy użyciu szyfru Cezara i wyświetla zaszyfrowany tekst.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 07_szyfr_02.py
    :linenos:

Jak to działa
===================

W programie możemy wykorzystywać zmienne globalne, np. KLUCZ.
``def nazwa_funkcji(argumenty)`` - tak definiujemy funkcje, które
mogą lub nie zwracać jakieś wartości.
``nazwa_funkcji(argumenty)`` - tak wywołujemy funkcje.
Napisy mogą być indeksowane (od 0), co daje dostęp do pojedynczych znaków.
Funkcja ``len(str)`` zwraca długość napisu, wykorzystana jako argument funkcji
``range()`` pozwala iterować po znakach napisu.
Operator ``+=`` oznacza dodanie argumentu z prawej strony do wartości z lewej.

Zadania dodatkowe
===================

    Napisz funkcję deszyfrującą ``deszyfruj(txt)``. Dodaj do funkcji ``szyfruj(), deszyfruj()`` drugi parametr w postaci długości klucza podawanej przez użytkownika. Dodaj poprawne szyfrowanie dużych liter, obsługę białych znaków i znaków interpunkcyjnych.

Przykład funkcji deszyfrującej:

.. code-block:: python
    :linenos:

    def deszyfruj(txt):
        dtxt = ""
        KLUCZM = KLUCZ % 26
        for i in range(len(txt)):
            if (ord(txt[i]) - KLUCZM < 97):
                dtxt += chr(ord(txt[i]) - KLUCZM + 26)
            else:
                dtxt += chr(ord(txt[i]) - KLUCZM)
        return dtxt

