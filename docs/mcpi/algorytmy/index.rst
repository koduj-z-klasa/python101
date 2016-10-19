.. _mcpialgorytmy:

Algorytmy
##############

W tym scenariuszu spróbujemy pokazać w Minecrafcie Pi algorytm symulujący
`ruchy Browna <https://pl.wikipedia.org/wiki/Ruchy_Browna>`_ oraz algorytmu
stosującego `metodę Monte Carlo <https://pl.wikipedia.org/wiki/Metoda_Monte_Carlo>`_
do wyliczenia liczby Pi.

Ruchy Browna
==============

Za pomocą wybranego edytora utwórz pusty plik, umieść w nim podany niżej kod i zapisz
w katalogu :file:`mcpi-sim` pod nazwą :file:`mcpi-rbrowna.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: mcpi-browna.py
    :linenos:
    :lineno-start: 1
    :lines: 1-


Większość kodu powinna być już zrozumiała, czyli importy bibliotek, nawiązywania połączenia
z serwerem MC Pi, czy funkcja ``plac()`` tworząca przestrzeń do testów.
Podobnie funkcja ``wykres()``, która pokazuje nam graficzną reprezentację funkcji
za pomocą biblioteki *matblotlib*. Na uwagę zasługuje w niej tylko parametr ``*extra``,
który pozwala przekazać argumenty i wartości dodatkowej funkcji.

