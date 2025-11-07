.. _quiz-app:

Quiz
#####

Realizacja aplikacji internetowej Quiz w oparciu o :term:`framework` Flask 3.1.x
Na stronie wyświetlamy pytania, użytkownik zaznacza poprawne odpowiedzi,
przesyła je na serwer i otrzymuje informację o wynikach.

Środowisko pracy
================

Do tworzenia aplikacji z użyciem Flaska możesz użyć dowolnych narzędzi, np. terminala i ulubionego edytora kodu.
Sugerujemy jednak wykorzystanie środowiska **PyCharm**, ponieważ w dużym stopniu ułatwia pracę nad projektami
w języku Python.

Przed rozpoczęciem pracy przygotuj w katalogu :file:`projekty_flask`` :ref:`wirtualne środowisko Pythona <venv>`
i w aktywnym środowisku zainstaluj pakiet *Flask*:

.. code-block:: bash

    (.venv) ~/projekty_flask$ pip install flask

Projekt i aplikacja
===================

W katalogu :file:`projekty_flask`` tworzymy nowy **katalog aplikacji** o nazwie :file:`quiz`:

.. raw:: html

    <div class="code_no">Terminal nr <script>var ter_t = ter_t || 1; document.write(ter_t++);</script></div>

.. highlight:: bash
.. code-block:: bash

    (.venv) ~/projekty_flask$ mkdir quiz
    (.venv) ~/projekty_flask$ cd quiz

Utworzymy szkielet aplikacji Flask, co pozwoli na uruchomienie testowego serwera www.
W katalogu aplikacji :file:`quiz` dodajemy plik o nazwie :file:`app.py` i umieszczamy w nim poniższy kod.

.. raw:: html

    <div class="code_no">Plik <i>app.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/app1.py
    :linenos:

Serwer uruchamiamy jednym z poleceń w terminalu w katalogu projektu:
``flask run --debug`` lub ``python3 app.py`` (``py app.py`` w systemie Windows):

.. raw:: html

    <div class="code_no">Terminal nr <script>var ter_t = ter_t || 1; document.write(ter_t++);</script></div>

.. code-block:: bash

    (.venv) ~/projekty_flask/quiz$ flask run --debug

.. figure:: img/flask_run_01.png

Domyślnie serwer uruchamia się pod adresem ``http://127.0.0.1:5000``.
Po otwarciu przeglądarki i wpisaniu tego adresu (można też kliknąć adres wyświetlony w terminalu
z wciśniętym klawiszem :kbd:`CTLR`) zobaczymy napis zwrócony przez aplikację: "Cześć, tu Python i Flask!".

.. figure:: img/flask_strona_01.png

.. tip::

    Działanie serwera zatrzymujemy w terminalu skrótem :kbd:`CTRL+C`.

Strona główna
=============

Nasza aplikacja zwraca użytkownikowi stronę główną za pomocą widoku ``index()``.
Jest to funkcja Pythona powiązana z określonym w dekoratorze ``route('/')``
adresem ``/`` oznaczającym domyślny zasób serwera.

Widoki obsługują podstawowe żądania protokołu :term:`HTTP` wysyłane przez przeglądarkę.

.. note::

    Żądania typu :term:`GET` występują wtedy, kiedy chcemy pobrać jakieś dane z serwera,
    np. stronę. Ewentualne dane przekazywane do serwera (np. parametry wyszukiwania)
    widoczne są w adresie URL, np.:

    ``www.google.com/search?client=firefox-b-lm&channel=entpr&q=żądania+GET+i+POST``

    Żądanie typu :term:`POST` służą natomiast do przesyłania na serwer danych niewidocznych w adresie URL,
    które mają zazwyczaj zmieniać stan aplikacji, np. dodać lub zalogować użytkownika.
    Do przesyłania danych metodą ``POST`` służą formularze.

W odpowiedzi na żądanie aplikacja może odsyłać różne dane, np. predefiniowany tekst, ale najczęściej
będzie to strona :term:`HTML` zawierająca różne w zależności od żądania informacje, np.
formularz z pytaniami albo wyniki quizu.

Flask ułatwia tworzenie takich stron za pomocą tzw. szablonów (zob. :term:`szablon`).
Szablony umieścimy w katalogu :file:`quiz/templates`, kóry należy utworzyć:

.. raw:: html

    <div class="code_no">Terminal nr <script>var ter_t = ter_t || 1; document.write(ter_t++);</script></div>

.. code-block:: bash

    (.venv) ~/projekty_flask/quiz$ mkdir templates

Następnie w utworzonym katalogu dodajemy plik :file:`index.html` i umieszczamy w nim kod:

.. raw:: html

    <div class="code_no">Plik <i>index.html</i>. <span class="right"><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></span></div>

.. highlight:: html
.. literalinclude:: source/index.html
    :linenos:

W miejsce oznaczone tagiem ``{{ config.SITE_NAME }}`` wstawiona zostanie nazwa serwisu, którą zdefiniujemy
w ustawieniach aplikacji.

Uzupełniamy i zmieniamy kod w pliku :file:`app.py`:

.. raw:: html

    <div class="code_no">Plik <i>app.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/app2.py
    :linenos:
    :emphasize-lines: 5-9, 14

Konfiguracja aplikacji przechowywana jest w słowniku ``config``, do którego dodajemy
sekretny klucz, wykorzystywany do obsługi sesji (zob :term:`sesja`) oraz nazwę serwisu.

Do renderowania szablonu (zob: :term:`renderowanie szablonu`) używamy
zaimportowanej na początku pliku funkcji ``render_template('index.html')``, która jako argument przyjmuje
nazwę pliku szablonu.

Po otworzeniu strony głównej (``http://127.0.0.1:5000``) zobaczymy stronę:

.. figure:: img/flask_strona_02.png

Pytania i odpowiedzi
====================

Dane aplikacji, a więc pytania i odpowiedzi, umieścimy w pliku :file:`app.py` – to najprostsze
rozwiązanie, żeby nie wprowadzać na razie obsługi bazy danych.
Nowy kod wstawiamy po instrukcji ``app = Flask(__name__)``:

.. raw:: html

    <div class="code_no">Plik <i>app.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/app3.py
    :linenos:
    :emphasize-lines: 5-28

Źródłem danych dla naszej aplikacji będzie lista ``dane``, która zawiera trzy słowniki.
W każdym słowniku umieszczamy treść pytania, możliwe odpowiedzi oraz odpowiedź poprawną.

Dalej definiujemy nowy adres URL ``/pytania``, który będzie obsługiwany przez
funkcję ``pytania()``. W funkcji zwracamy szablon ``pytania.html``,
do którego przekazujemy listę ``dane`` w zmiennej ``pytania``.

W katalogu :file:`templates` tworzymy nowy plik :file:`pytania.html` i wstawiamy
do niego poniższy kod:

.. raw:: html

    <div class="code_no">Plik <i>pytania.html</i> <span class="right"><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></span></div>

.. highlight:: html
.. literalinclude:: source/pytania.html
    :linenos:

W szablonie używamy specjalnych tagów:

* ``{% instrukcja %}`` – tak wstawiamy instrukcje sterujące typu ``for``, ``set`` czy ``if``;
* ``{{ zmienna }}`` – tak wstawiamy wartości danych przekazanych do szablonu.

Pętla ``{% for komunikat in get_flashed_messages() %}`` odpowiada za wstawienie komunikatów,
które przygotujemy dla użytkownika w widoku ``pytania()``.

Znacznik ``<form>`` tworzy formularz, który wysyłany będzie na adres URL zdefiniowany w atrybucie ``action``.
Adres ten generujemy przy użyciu funkcji ``url_for('pytania')``. Jako argument przyjmuje ona nazwę widoku.

W formularzu wstawiamy pytania i możliwe odpowiedzi: z przekazanej do szablonu zmiennej ``pytania``
odczytujemy w pętli ``{% for p in pytania %}`` kolejne słowniki. Dalej w znacznikach akapitu ``<p>``
wyświetlamy treść pytania ``{{ p.pytanie }}``, a w kolejnej pętli ``{% for o in p.odpowiedz %}``
– odpowiedzi jako grupy opcji typu radio ``<input type="radio">``.

Każda grupa odpowiedzi nazywana jest dla odróżnienia numerem pytania liczonym od 0.
Odpowiednią zmienną ustawiamy w instrukcji ``{% set pnr = loop.index0 %}``,
a używamy w postaci ``name="{{ pnr }}"``. Dzięki temu przyporządkujemy
przesłane odpowiedzi do kolejnych pytań podczas ich sprawdzania.

Na końcu w znaczniku ``<a>`` generujemy adres strony głównej za pomocą wspomnianej
funkcji ``url_for('index')``, której argumentem jest nazwa widoku,
czyli funkcji w tym przypadku obsługującej adres domyślny.

Po uruchomieniu serwera i wpisaniu w przeglądarce adresu ``http://127.0.0.1:5000/pytania``
powinniśmy zobaczyć:

.. figure:: img/flask_pytania_01.png

Oceniamy odpowiedzi
===================

Kod sprawdzający liczbę poprawnych odpowiedzi umieścimy w widoku ``pytania()``.
Na początku pliku :file:`app.py` dodajemy potrzebne importy:

.. raw:: html

    <div class="code_no">Plik <i>app.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/app4.py
    :linenos:
    :lineno-start: 3
    :lines: 3

– i uzupełniamy kod funkcji ``pytania()``:

.. raw:: html

    <div class="code_no">Plik <i>app.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/app4.py
    :linenos:
    :lineno-start: 27
    :lines: 27-39

* ``methods=['GET', 'POST']`` – dodajemy typy żądań, które chcemy obsługiwać,
  tj. :term:`GET` (odesłanie zażądanej strony), jak i :term:`POST`
  (przesłanie danych z formularza, tj. odpowiedzi, i odesłanie wyników);
* ``request`` – obiekt zawierający informacje związane z żądaniem, m. in. typ żądania
  i ewentualne dane z formularza;
* ``if request.method == 'POST':`` – instrukcja warunkowa, która wykrywa
  żądania POST i wykonuje blok kodu zliczający poprawne odpowiedzi;
* ``odpowiedzi = request.form`` – przesyłane dane z formularza zapisujemy w zmiennej ``odpowiedzi``;
* ``for pnr, odp in odpowiedzi.items()`` – w pętli odczytujemy
  kolejne pary danych, czyli numer pytania i udzieloną odpowiedź;
* ``if odp == dane[int(pnr)]['odpok']:`` – sprawdzamy, czy nadesłana odpowiedź
  jest zgodna z poprawną, którą odczytujemy z listy pytań.

Zwróćmy uwagę, że wartości zmiennej ``pnr``, czyli numery pytań liczone od zera,
ustaliliśmy wcześniej w szablonie.

Jeżeli nadesłana odpowiedź jest poprawna (``if odp == dane[int(pnr)]['odpok']:``), tzn. zgadza się
z poprawną odpowiedzią zawartą w liście słowników – doliczamy punkt (``punkty += 1``).

Informacje o wyniku przekazujemy użytkownikowi za pomocą funkcji ``flash()``.
W szablonie wyświetlamy je we wspominanej pętli ``{% for komunikat in get_flashed_messages() %}``.

Ćwiczenie
----------

1. Wstaw w szablonie strony głównej link do strony wyświetlającej pytania.

   .. figure:: img/flask_strona_03.png

2. Uruchom serwer, wejdź na stronę główną, a następnie na stronę z pytaniami.

   .. figure:: img/flask_pytania_01.png

3. Zaznacz odpowiedzi i prześlij dane na serwer.

   .. figure:: img/flask_pytania_02.png

Materiały
=========

* `Quickstart <https://flask.palletsprojects.com/en/stable/quickstart/>`_

.. admonition:: Pojęcia

    :term:`framework`, :term:`HTTP`, :term:`GET`, :term:`POST`, :term:`sesja`,
    :term:`dekorator`, :term:`widok`, :term:`szablon`, :term:`renderowanie szablonu`
