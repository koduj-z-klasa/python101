.. _mcpialgorytmy:

Algorytmy
##############

W tym scenariuszu spróbujemy pokazać w Minecrafcie Pi algorytm symulujący
`ruchy Browna <https://pl.wikipedia.org/wiki/Ruchy_Browna>`_ oraz algorytm
stosujący `metodę Monte Carlo <https://pl.wikipedia.org/wiki/Metoda_Monte_Carlo>`_
do wyliczenia przybliżonej wartości liczby Pi.

Ruchy Browna
==============

Za pomocą wybranego edytora utwórz pusty plik, umieść w nim podany niżej kod i zapisz
w katalogu :file:`mcpi-sim` pod nazwą :file:`mcpi-rbrowna.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-rbrowna01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-


Większość kodu powinna być już zrozumiała. Importy bibliotek, nawiązywanie połączenia
z serwerem MC Pi, funkcje ``plac()``, ``wykres()`` i ``rysuj()`` omówione zostały w poprzednim
scenariuszu :ref:`Funkcje w mcpi <mcpi-funkcje>`.

W funkcji ``ruchyBrowna()`` na początku pobieramy od użytkownika ilość ruchów cząsteczki
do wygenerowania oraz ich długość, co ma znaczenie podczas ich odwzorowywania w świecie MC Pi.
Następnie w pętli:

* losujemy kąt wskazujący kierunek ruchu cząsteczki,
* wyliczamy współrzędne kolejnego punktu korzystając z funkcji *cos()* i *sin()* (np. ``x = x + r * np.cos(rad)``),
* zaokrąglamy wyniki do 2 miejsc po przecinku (np. ``x = int(round(x, 2))``) i drukujemy,
* na koniec dodajemy obliczone współrzędne do list odciętych i rzędnych (np. ``lx.append(x)``).

Po wyjściu z pętli obliczamy długość wektora przesunięcia, korzystając z twierdzenia Pitagorasa,
i drukujemy wynik z dokładnością do dwóch miejsc po przecinku (wyrażenie formatujące: ``{:.2f}``).

Po tych operacjach pozostaje wykreślenie ruchu cząsteczki w *matplotlib* i wyznaczenie go
w Minecrafcie.

(Nie)powtarzalność
==================

[todo]