Mów mi Python – wprowadzenie do języka Python
*********************************************

Znam Pythona
=================

ZADANIE
-------

    Przeanalizuj podane kody dwóch programów i spróbuj sam zrozumieć, jak działają i wprowadź sugerowane zmiany.

Pierwszy program na podstawie danych pobranych od użytkownika sprawdza m. in., czy da się zbudować trójkąt.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

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

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

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
