Quiz – aplikacja internetowa
============================

Realizacja aplikacji internetowej Quiz w oparciu o mikro-framework Flask.

Struktura katalogów
-------------------

W katalogu użytkownika tworzymy nowy katalog dla aplikacji :file:`quiz`, a w nim plik główny :file:`quiz.py`:

.. raw:: html

    <div class="code_no">Terminal nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: bash

    ~$ mkdir quiz; cd quiz; touch quiz.py

Aplikacja na przykładzie quizu – użytkownik zaznacza w formularzu poprawne odpowiedzi na pytania i otrzymuje ocenę – ma pokazać podstawową strukturę frameworka Flask.

Szkielet aplikacji
------------------

Utworzenie minimalnej aplikacji Flask pozwoli na uruchomienie serwera deweloperskiego, umożliwiającego wygodne rozwijanie kodu. W pliku :file:`quiz.py` wpisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    # -*- coding: utf-8 -*-
    # todo/todo.py

    from flask import Flask

    app = Flask(__name__)

    if __name__ == '__main__':
        app.run(debug=True)

Serwer uruchamiamy komendą:

.. raw:: html

    <div class="code_no">Terminal nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: bash

    ~/python101/modul3/zadanie1$ python todo.py

.. figure:: img/start_serwera.png

Domyślnie serwer uruchamia się pod adresem *http://127.0.0.1:5000*. Po wpisaniu adresu do przeglądarki internetowej otrzymamy stronę z błędem HTTP 404, co wynika z faktu, że nasza aplikacja nie ma jeszcze zdefiniowanego żadnego zachowania (widoku) dla tego adresu. W
uproszczeniu możemy widok utożsamiać z pojedynczą stroną w ramach aplikacji internetowej.

Definiowanie widoków – strona główna
------------------------------------

:term:`Widoki` to funkcje Pythona powiązane z określonymi adresami URL za pomocą tzw. dekoratorów. Widoki pozwalają nam obsługiwać żądania GET i POST, a także, przy wykorzystaniu szablonów, generować i zwracać żądane przez klienta strony WWW. W szablonach oprócz znaczników HTML możemy umieszczać różne dane. Flask renderuje (łączy) kod HTML z danymi i odsyła do przeglądarki.

W pliku :file:`todo.py` umieścimy funkcję ``index()``, widok naszej strony głównej:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:
    :emphasize-lines: 9-15

    # -*- coding: utf-8 -*-
    # todo/todo.py

    from flask import Flask
    from flask import render_template

    app = Flask(__name__)

    # dekorator laczacy adres glowny z widokiem index
    @app.route('/')
    def index():
        # gdybyśmy chcieli wyświetlić prosty tekst, użyjemy funkcji poniżej
        #return 'Hello, SWOI'
        # zwracamy wyrenderowany szablon index.html:
        return render_templpate('index.html')

    if __name__ == '__main__':
        app.run(debug=True)
        

Zauważmy, że widok ``index()`` za pomocą dekoratora ``@app.route('/')`` związaliśmy z adresem głównym (/). Dalej w katalogu :file:`quiz` tworzymy podkatalog :file:`templates`, a w nim szablon :file:`index.html`, wydajemy polecenia w terminalu:

.. raw:: html

    <div class="code_no">Terminal nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: bash

    ~/python101/modul3/zadanie1$ mkdir templates; cd templates; touch index.html

Do pliku :file:`index.html` wstawiamy przykładowy kod HTML:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: templates/index_z1.html
    :linenos:

Po odwiedzeniu adresu *http://127.0.0.1:5000*, otrzymamy stronę HTML.

.. figure:: img/h1.png

Pokaż dane aplikacji – pytania i odpowiedzi
-------------------------------------------

Dane naszej aplikacji, a więc pytania i odpowiedzi, umieścimy w liście ``QUESTIONS`` w postaci słowników zawierających: treść pytania, listę
możliwych odpowiedzi oraz poprawną odpowiedź. W pliku :file:`quiz.py` wstawiamy listę pytań, aktualizujemy widok ``index()``, przekazując do szablonu pytania w zmiennej ``questions``.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: quiz_z2.py
    :linenos:
    :emphasize-lines: 9-37

Dodatkowo dodaliśmy konfigurację aplikacji, ustalając sekretny klucz, który przyda nam się w późniejszej części. Aktualizujemy szablon :file:`index.html`, aby wyświetlić listę pytań w postaci formularza HTML.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: templates/index_z2.html
    :linenos:

Wewnątrz szablonu przeglądamy pytania zawarte w zmiennej questions za pomocą instrukcji ``{% for entry in questions %}``, tworzymy formularz
HTML składający się z treści pytania ``{{ entry.question }}`` i listy odpowiedzi (kolejna pętla ``{% for answer in entry.answers %}``) w
postaci grupy opcji nazywanych dla odróżnienia kolejnymi indeksami pytań liczonymi od 0 (``{% set question_number = loop.index0 %}``).

W efekcie powinniśmy otrzymać następującą stronę internetową:

.. figure:: img/quiz.png

Oceniamy odpowiedzi
-------------------

Mechanizm sprawdzana liczby poprawnych odpowiedzi umieścimy w pliku :file:`quiz.py`, modyfikując widok ``index()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:

    # uzupelniamy importy
    from flask import request
    from flask import redirect, url_for
    from flask import flash


    # rozszerzamy widok
    @app.route('/', methods=['GET', 'POST'])
    def index():
        # jezeli zadanie jest typu POST, to znaczy, ze ktos przeslal odpowiedzi do sprawdzenia
        if request.method == 'POST':
            score = 0 # liczba poprawnych odpowiedzi
            answers = request.form # zapamietujemy slownik z odpowiedziami
            # sprawdzamy odpowiedzi:
            for question_number, user_answer in answers.items():
                # pobieramy z listy informacje o poprawnej odpowiedzi
                correct_answer = QUESTIONS[int(question_number)]['correct_answer']
                if user_answer == correct_answer: # porownujemy odpowiedzi
                    score += 1 # zwiekszamy wynik
            # przygotowujemy informacje o wyniku
            flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(score))
            # po POST przekierowujemy na strone glowna
            return redirect(url_for('index'))

        # jezeli zadanie jest typu GET, renderujemy index.html
        return render_template('index.html', questions=QUESTIONS)
        

W szablonie :file:`index.html` po znaczniku ``<h1>`` wstawiamy instrukcje wyświetlające wynik:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: html
    :linenos:

    <!-- umieszczamy informacje ustawiona za pomoca funkcji flash -->
    <p>
        {% for message in get_flashed_messages() %}
            <strong class="success">{{ message }}</strong>
        {% endfor %}
    </p>

Jak to działa
^^^^^^^^^^^^^

Uzupełniliśmy dekorator app.route, aby obsługiwał zarówno żądania :term:`GET` (wejście na stronę główną po wpisaniu adresu => pokazujemy
pytania), jak i :term:`POST` (przesłanie odpowiedzi z formularza pytań => oceniamy odpowiedzi).

W widoku ``index()`` dodaliśmy instrukcję warunkową ``if request.method == 'POST':``, która wykrywa żądania POST i wykonuje blok kodu zliczający poprawne odpowiedzi. Zliczanie wykonywane jest w pętli ``for question_number, user_answer in answers.items()``.

W tym celu iterujemy po przesłanych odpowiedziach i sprawdzamy, czy nadesłana odpowiedź jest zgodna z tą, którą przechowujemy w polu ``correct_answer`` konkretnego pytania. Dzięki temu, że w szablonie dodaliśmy do każdego pytania jego numer (zmienna ``question_number``), to możemy teraz po tym numerze odwołać się do konkretnego pytania na naszej liście.

Jeżeli nadesłana odpowiedź jest zgodna z tym, co mamy zapisane w pytaniu, to naliczamy punkt. Informacje o wyniku przekazujemy do użytkownika za pomocą funkcji ``flash``, która korzysta z sesji HTTP (właśnie dlatego musieliśmy ustalić ``SECRET_KEY`` dla naszej aplikacji).

W efekcie otrzymujemy aplikację Quiz.

Materiały
^^^^^^^^^^^^^

1. Strona projektu Flask http://flask.pocoo.org/
2. Co to jest framework? http://pl.wikipedia.org/wiki/Framework
3. Co nieco o HTTP i żądaniach GET i POST
   http://pl.wikipedia.org/wiki/Http

Pojęcia
^^^^^^^^^^^^^

.. glossary::

    Aplikacja
        program komputerowy.

    Framework
        zestaw komponentów i bibliotek wykorzystywany do budowy aplikacji.

    GET
        typ żądania HTTP, służący do pobierania zasobów z serwera WWW.

    HTML
        język znaczników wykorzystywany do formatowania dokumentów, zwłaszcza stron WWW.

    HTTP
        protokół przesyłania dokumentów WWW.

    POST
        typ żądania HTTP, służący do umieszczania zasobów na serwerze WWW.

    Serwer deweloperski
        serwer używany w czasie prac nad oprogramowaniem.

    Serwer WWW
        serwer obsługujący protokół HTTP.

    Templatka
        szablon strony WWW wykorzystywany przez Flask do renderowania widoków.

    URL
        ustandaryzowany format adresowania zasobów w internecie (przykład: http://pl.wikipedia.org/wiki/Uniform_Resource_Locator).

    Widok
        fragment danych, który jest reprezentowany użytkownikowi.

Metryka
^^^^^^^

:Autorzy: Tomasz Nowacki,
          Robert Bednarz,
          Janusz Skonieczny

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>


.. include:: ../copyright.rst
