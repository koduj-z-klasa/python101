Python w przykładach
**************************************

Jestem Python
================

Python jest dynamicznie typowanym językiem interpretowanym wysokiego poziomu. Cechuje się czytelnością i zwięzłością kodu. Stworzony został w latach 90. przez Guido van Rossuma, nazwa zaś pochodzi od tytułu serialu komediowego emitowanego w BBC pt. "Latający cyrk Monty Pythona".

W systemach opartych na Linuksie interpreter Pythona jest standardowo zainstalowany, ponieważ duża część oprogramowania na nim bazuje. W systemach Microsoft Windows Pythona należy doinstalować. Funkcjonalność Pythona może być dowolnie rozszerzana dzięki licznym bibliotekom pozwalającym tworzyć aplikacje okienkowe (PyQt, PyGTK, wxPython), internetowe (Flask, Django) czy multimedialne i gry (Pygame). Istnieją również kompleksowe projekty oparte na Pythonie wspomagające naukową analizę, obliczenia i przetwarzanie danych (Anaconda, Canopy).

Kodować można w dowolnym edytorze tekstowym, jednak ze względów praktycznych warto korzystać z programów ułatwiających pisanie kodu. Polecić można np. lekkie, szybkie i obsługujące wiele języków środowisko Geany, a także profesjonalne rozwiązanie, jakim jest aplikacja PyCharm. Obydwa programy działają na platformie Linux i Windows.

Zanim przystąpimy do pracy w katalogu domowym utworzymy podkatalog ``python``, w którym będziemy zapisywali nasze skrypty:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: bash

    ~ $ mkdir python

Poznawanie Pythona zrealizujemy poprzez rozwiązywanie prostych zadań, które pozwolą zaprezentować elastyczność i łatwość tego języka. Nazwy kolejnych skryptów umieszczone są jako komentarz zawsze w czwartej linii kodu. Pliki zawierające skrypty Pythona mają zazwyczaj rozszerzenie **.py**. Bardzo przydatnym narzędziem podczas kodowania w Pythonie jest konsola interpretera, którą uruchomimy wydając w terminalu polecenie ``python`` lub ``ipython``. Można w niej testować i debugować wszystkie wyrażenia, warunki, polecenia itd., z których korzystamy w skryptach.

.. note::

    **Ipython** to rozszerzona konsola Pythona przeznaczona do wszelkiego rodzaju interaktywnych obliczeń.

Źródła
--------------------

Jeżeli chcesz, pobierz wszystkie kody wykorzystywane we wprowadzeniu: :download:`basic.zip <basic.zip>`

Przywitaj się
=================

Mów mi Python!
-----------------------

    **ZADANIE**: Pobierz od użytkownika *imię*, *wiek* i powitaj go komunikatem:
    "Mów mi Python, mam *x* lat.
    Witaj w moim świecie *imie*.
    Jesteś starszy(młodszy) ode mnie."

    **POJĘCIA**: *zmienna, wartość, wyrażenie, wejście i wyjście danych, instrukcja warunkowa, komentarz*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 01_hello.py
    :linenos:

JAK TO DZIAŁA
^^^^^^^^^^^^^^

Deklaracja zmiennej w Pythonie nie jest wymagana, wystarczy podanej nazwie przypisać jakąś wartość
za pomocą operatora przypisania "=". Zmiennym często przypisujemy wartości za pomocą wyrażeń,
czyli działań arytmetycznych lub logicznych.

.. note::
    Niekiedy mówi się, że w Pythonie zmiennych nie ma, są natomiast wartości określonego typu.

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
^^^^^^^^^^^^^^

    Zmień program tak, aby zmienna *aktRok* (aktualny rok) była podawana przez użytkownika na początku programu.

Metryka
^^^^^^^

:Autor: Robert Bednarz <ecg@ecg.vot.pl>

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>


.. include:: ../copyright.rst
