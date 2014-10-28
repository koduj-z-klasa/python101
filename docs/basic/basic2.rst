Witaj Python!
=================

ZADANIE
------------
    Pobierz od użytkownika imię, wiek i powitaj go komunikatem:
    "Mów mi Python, mam x lat.
    Witaj w moim świecie imie.
    Jesteś starszy(młodszy) ode mnie."

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 01_hello.py
    :linenos:

JAK TO DZIAŁA
-------------

**Pojęcia**: *zmienna, wartość, wyrażenie, wejście i wyjście danych, instrukcja warunkowa, komentarz*.

Deklaracja zmiennej w Pythonie nie jest wymagana, wystarczy podanej nazwie przypisać jakąś wartość
za pomocą operatora przypisania "=" [2]_. Zmiennym często przypisujemy wartości za pomocą wyrażeń,
czyli działań arytmetycznych lub logicznych.

.. [2] Dlatego niekiedy mówi się, że w Pythonie zmiennych nie ma, są natomiast wartości określonego typu.

Funkcja ``raw_input()`` zwraca pobrane z klawiatury znaki jako napis, czyli typ **string**.

Funkcja ``int()`` umożliwia konwersję napisu na liczbę całkowitą, czyli typ **integer**.

Funkcja ``print`` drukuje podane argumenty oddzielone przecinkami. Komunikaty tekstowe ujmujemy
w cudzysłowy podwójne lub pojedyncze. Przecinek oddziela kolejne argumenty spacjami.

Instrukcja ``if`` (jeżeli) pozwala na warunkowe wykonanie kodu. Jeżeli podane wyrażenie
jest prawdziwe (przyjmuje wartość ``True``) wykonywana jest pierwsza instrukcja,
w przeciwnym wypadku (``else``), kiedy wyrażenie jest fałszywe (wartość ``False``),
wykonywana jest instrukcja druga. Warto zauważyć, że polecenia instrukcji warunkowej kończymy dwukropkiem.

Charakterystyczną cechą Pythona jest używanie wcięć do zaznaczania bloków kodu.
Komentarze wprowadzamy po znaku ``#``.

POĆWICZ SAM
-----------

    Zmień program tak, aby zmienna *curYear* (aktualny rok) była podawana przez użytkownika na początku programu.

