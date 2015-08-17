Szyfr Cezara
############

**ZADANIE**: Napisz program, który podany przez użytkownika ciąg znaków szyfruje przy użyciu szyfru Cezara i wyświetla zaszyfrowany tekst.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 07_szyfr_02.py
    :linenos:

W programie możemy wykorzystywać zmienne globalne, np. KLUCZ.
``def nazwa_funkcji(argumenty)`` - tak definiujemy funkcje, które
mogą lub nie zwracać jakieś wartości.
``nazwa_funkcji(argumenty)`` - tak wywołujemy funkcje.
Napisy mogą być indeksowane (od 0), co daje dostęp do pojedynczych znaków.
Funkcja ``len(str)`` zwraca długość napisu, wykorzystana jako argument funkcji
``range()`` pozwala iterować po znakach napisu.
Operator ``+=`` oznacza dodanie argumentu z prawej strony do wartości z lewej.

Zadania dodatkowe
*****************

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
