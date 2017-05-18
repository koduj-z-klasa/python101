Mów mi Python!
###############

**ZADANIE**: Pobierz od użytkownika *imię*, *wiek* i powitaj go komunikatem:
"Mów mi Python, mam *x* lat.
Witaj w moim świecie *imie*.
Jesteś starszy(młodszy) ode mnie."

**POJĘCIA**: *zmienna, wartość, wyrażenie, wejście i wyjście danych, instrukcja warunkowa, komentarz*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 01_hello.py
    :linenos:

Deklaracja zmiennej w Pythonie nie jest wymagana, wystarczy podanej nazwie przypisać jakąś wartość
za pomocą operatora przypisania "=". Zmiennym często przypisujemy wartości za pomocą wyrażeń,
czyli działań arytmetycznych lub logicznych.

.. note::

    Niekiedy mówi się, że w Pythonie zmiennych nie ma, są natomiast wartości określonego typu.

Funkcje:

* ``input()`` zwraca pobrane z klawiatury znaki jako napis, czyli typ **string**.
* ``int()`` umożliwia konwersję napisu na liczbę całkowitą, czyli typ **integer**.
* ``print()`` drukuje podane argumenty oddzielone przecinkami.

Napisy ujmujemy w cudzysłowy podwójne lub pojedyncze.

Instrukcja ``if wyrażenie`` (jeżeli) steruje warunkowym wykonaniem kodu. Jeżeli podane wyrażenie
jest prawdziwe (przyjmuje wartość ``True``), wykonywana jest pierwsza instrukcja,
w przeciwnym wypadku (``else``), kiedy wyrażenie jest fałszywe (wartość ``False``),
wykonywana jest instrukcja druga. Części instrukcji warunkowej kończymy dwukropkiem.

Charakterystyczną cechą Pythona jest używanie wcięć do zaznaczania bloków kodu. Standardem są 4 spacje.
Komentarze wprowadzamy po znaku ``#``.

Zadania
********

Zmień program tak, aby zmienna *aktRok* (aktualny rok) była podawana przez użytkownika na początku programu.
