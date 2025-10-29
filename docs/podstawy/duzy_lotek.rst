.. _duzy-lotek:

Duży Lotek
##########

Przykład :ref:`Mały Lotek <maly-lotek>` pokazuje, jak wylosować jedną liczbę z zakresu ``<1; 10>``
i dać użytkownikowi trzy szanse jej odgadnięcia. Zasady większości gier wymagają typowania
wielu liczb z większego zakresu. Napiszemy więc program, w którym poziom trudności odgadywania liczb będzie
można dostosować.

.. note::

    Przykład "Duży Lotek" pokazuje, jak używać pętli warunkowej do pobierania danych z klawiatury,
    jak sprawdzać poprawność wprowadzanych danych
    oraz jak używać list i zbiorów jako złożonych struktur danych.

Zadanie
********

Napisz program :file:`duzy_lotek.py`, który losuje ``n`` liczb naturalnych
z podanego zakresu ``maks``, a następnie pobiera z klawiatury ``n`` typów, sprawdza i wypisuje,
ile z nich zostało trafionych. Program powinien sprawdzać poprawność podawanych
danych wejściowych.

**Dane**:

* ``n`` – liczba całkowita pobierana z klawiatury,
* ``maks`` – liczba naturalna pobierana z klawiatury większa od ``n``,
* ``typ`` – liczba całkowita pobierana z klawiatury z zakresu ``<0; maks>``.

**Wynik** – przykładowe komunikaty:

.. code::

    Podaj liczbę losowanych liczb: 4
    Podaj maksymalną losowaną liczbę: 10
    Wytypuj 4 z 10 liczb:
    Podaj liczbę 1: 2
    Podaj liczbę 2: 5
    Podaj liczbę 3: 7
    Podaj liczbę 4: 1

    Trafione liczby: {1}
    Liczba trafień 1
    Wylosowane liczby: [1, 6, 8, 3]

Poprawność danych
******************

.. raw:: html

    <div class="code_no">Plik <i>duzy_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: duzy_lotek.py
    :linenos:
    :lineno-start: 1
    :lines: 1-16

Podczas pobierania danych z klawiatury lub pliku możemy otrzymać dane niewłaściwego typu, np.
ciąg znaków kiedy oczekujemy liczby. Do obsługi tego typu błędów możemy użyć przechwytywania
wyjątków (zob. :term:`wyjątki`). Służy do tego instrukcja ``try: ... except wyjątek: ...``,
czyli: spróbuj wykonać kod w bloku ``try``, a w razie błędów przechwyć wyjątek – ``except wyjątek``
i wykonaj podporządkowane instrukcje.

W naszym programie jeżeli użytkownik poda łańcuch znaków, którego nie da się zamienić na liczbę
całkowitą, instrukcja ``int()`` wypisze komunikat ``invalid literal for int() with base 10``
i zgłosi wyjątek ``ValueError``. Wyjątek przechwytujemy i obsługujemy,
tj. ustawiamy zmienną pomocniczą ``error`` na wartość ``True`` (prawda).

Jeżeli typy danych są poprawne możemy sprawdzać, czy otrzymane wartości mieszczą się w odpowiednim
zakresie albo zawierają oczekiwane wartości. Korzystamy z instrukcji warunkowej, która w przypadku błędu
również zmienia wartość zmiennej ``error``.

Na końcu sprawdzamy, czy zmienna ``error`` ma wartość ``True``, co oznacza błąd typu danych lub zakresu wartości.
Wypisujemy wtedy odpowiedni komunikat i kończymy program instrukcją ``exit()``.

Losowanie liczb
***************

W programie "Mały lotek" losowaliśmy jedną liczbę, którą zapamiętywaliśmy w jednej zmiennej.
Tym razem mamy wylosować wiele liczb, które nie powinny się powtarzać. Uzupełniamy więc program:

.. raw:: html

    <div class="code_no">Plik <i>duzy_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: duzy_lotek.py
    :linenos:
    :lineno-start: 17
    :lines: 17-23

Do zapamiętania losowanych liczb używamy listy o nazwie ``liczby``. Losowanie odbywa się
w pętli warunkowej dopóki liczba elementów listy jest mniejsza od liczby liczb do wylosowania:
``while len(liczby) < n:``. Wewnątrz pętli wylosowana liczba dodawana jest do listy tylko
wtedy, jeżeli w liście nie występuje. Liczbę wystąpień elementu w liście zwraca metoda ``.count()``.

.. note::

    * Pętla ``for`` nie nadaje się do losowania unikalnych liczb, ponieważ wykonuje się określoną ilość razy,
      a nie możemy zagwarantować, że losowane liczby będą za każdym razem inne.
    * Ponieważ lista jest sekwencją, warunek ``liczby.count(liczba) == 0`` można zastąpić
      wyrażeniem ``liczba not in liczby``, w którym korzystamy z zaprzeczonego operatora zawierania
      ``not in``.

Pobieranie typów
****************

Do pobierania typów z klawiatury użyjemy takiej samej pętli, jak podczas losowania,
tzn. wykonuje się ona dopóty użytkownik nie poda tylu poprawnych typów, ile liczb zostało wylosowanych.
Uzupełniamy program:

.. raw:: html

    <div class="code_no">Plik <i>duzy_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: duzy_lotek.py
    :linenos:
    :lineno-start: 24
    :lines: 24-41

W pętli ``while`` kontrolujemy typ pobieranych danych i sprawdzamy:

* ``typ < 0 or typ > maks`` – alternatywa warunków badających czy podany typ jest mniejszy od zera
  lub większy od wartości maksymalnej,
* ``typ in typy`` – operator zawierania ``in`` zwróci prawdę, jeżeli badany typ
  znajduje się w zbiorze ``typy``.

Jeżeli zmienna ``error`` ma wartość ``True``, oznacza to błąd typu danych, zakresu lub powtórzenie typu.
Wypisujemy wtedy odpowiedni komunikat i wznawiamy działanie pętli za pomocą instrukcji ``continue``.
W przeciwnym razie dodajemy podaną liczbę (typ) do zbioru.

Zbiory
******

Zbiory (zob. :term:`zbiór`) to złożone struktury danych, które tym różnią się od list,
że zawarte w nich elementy nie mogą się powtarzać i są nieuporządkowane, tzn. nie są indeksowane.

**Operacje na zbiorach**

* ``typy = []`` lub ``typy = set()`` – utworzenie pustego zbioru,
* ``typy.add(element)`` – dodanie elementu do zbioru,
* ``trafione = set(liczby)`` – utworzenie zbioru z listy,
* ``|``, ``-``, ``&`` – operatory sumy, różnicy i iloczynu (części wspólnej) zabiorów,
* ``len(trafione)`` – zwraca liczbę elementów zbioru.

Liczba trafień
**************

Do programu dopisujemy kod ustalający liczbę trafień i wypisujący dane wyjściowe:

.. raw:: html

    <div class="code_no">Plik <i>duzy_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: duzy_lotek.py
    :linenos:
    :lineno-start: 42
    :lines: 42-51

Ustalenie liczby trafień w większości języków programowania wymagałoby przeszukiwania listy wylosowanych
liczb dla każdego podanego typu. W Pythonie możemy użyć arytmetyki zbiorów, tj. wyznaczamy
część wspólną: ``trafione = set(liczby) & typy``.

Jeżeli jakakolwiek liczba została odgadnięta, zbiór ``trafione`` jest niepusty i wyrażenie
``if trafione`` jest prawdziwe. Wypisujemy wtedy zbiór oraz liczbę jego elementów.

Ćwiczenia
**********

1) W interpreterze przetestuj poniższe instrukcje:

.. code-block:: bash

    ~$ python3
    >>> liczby = [1,3,5,7,9]
    >>> typy = set([2,3,4,5,6])
    >>> set(liczby) | typy
    >>> set(liczby) - typy
    >>> trafione = set(liczby) & typy
    >>> trafione
    >>> len(trafione)

2) Zmień program tak, aby użytkownik mógł 3 razy podawać typy, tj. odgadywać wylosowane liczby.

   .. tip::

       Wykorzystaj pętlę ``for``.

3) Przekształć powtarzający się kod sprawdzający poprawność typu danych na funkcję zwracającą
   wartość ``True`` lub ``False``. Użyj w funkcji w programie odpowiednio go modyfikując.

Poza tym sprawdzamy, czy użytkownik podaje sensowne typy. Warunek ``if 0 < typ <= maksliczba:``
to skrócony zapis wyrażenia logicznego z użyciem operatora koniunkcji:
``typ > 0 and typ <= maksliczba``. Sprawdzamy w ten sposób, czy wartość zmiennej
``typ`` jest większa od zera i mniejsza lub równa wartości zmiennej ``maksliczba``.

.. admonition:: Pojęcia

    :term:`pętla`, :term:`lista`, :term:`zbiór`
