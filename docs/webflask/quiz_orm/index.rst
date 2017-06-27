.. _quiz-orm:

Quiz ORM
#####################

.. highlight:: python

Realizacja aplikacji internetowej Quiz w oparciu o :term:`framework` `Flask`_
i bazę danych `SQLite`_ zarządzaną systemem ORM `Peewee`_ lub `SQLAlchemy`_.

.. _Flask: http://flask.pocoo.org
.. _SQLite: http://www.sqlite.org
.. _Peewee: http://peewee.readthedocs.org/en/latest
.. _SQLAlchemy: http://www.sqlalchemy.org

.. contents::
    :depth: 1
    :local:

Wymagania
*******************

Dobre zrozumienie omawianych tu zagadnień wymaga przyswojenia podstaw Pythona
omówionych w scenariuszu "Python w przykładach" (tematy 2-6), obsługi bazy
danych przedstawionej w scenariuszu "Bazy danych w Pythonie" oraz scenariusza
wprowadzającego do użycia frameworka Flask w aplikacjach internetowych
pt. "Quiz". Zalecamy również zapoznanie się ze scenariuszem "ToDo", który
ilustruje użycie bazy danych obsługiwanej za pomocą wbudowanego modułu ``sqlite3``
z aplikacją internetową.

Wykorzystywane biblioteki instalujemy przy użyciu instalatora ``pip``:

.. code-block:: bash

    ~$ sudo pip install peewee sqlalchemy flask-sqlalchemy

Modularyzacja
*******************

Scenariusze "Quiz" i "ToDo" pokazują możliwość umieszczenia całego kodu
aplikacji obsługiwanej przez Flaska w jednym pliku. O ile dla celów
szkoleniowych jest to dobre rozwiązanie, o tyle w praktycznych realizacjach
wygodniej logicznie rozdzielić poszczególne części aplikacji i umieścić
je w osobnych plikach, których nazwy określają ich przeznaczenie.
Podejście takie usprawnia rozwijanie aplikacji, ale również ułatwia
poznawanie bardziej rozbudowanych systemów, takich jak Django, przedstawione
w scenariuszu "Czat".

Tak więc kod rozmieścimy następująco:

    - ``app.py`` – konfiguracja aplikacji Flaska i obiektu służącego do łączenia się z bazą;
    - ``models.py`` – klasy opisujące tabele, pola i relacje w bazie;
    - ``views.py`` – widoki obsługujące udostępnione użytkownikowi akcje, typu "rozwiąż quiz", "dodaj pytanie", "edytuj pytania" itp.
    - ``main.py`` – główny plik naszej aplikacji wiążący wszystkie powyższe, odpowiada za utworzenie tabel w bazie, wypełnienie ich danymi początkowymi i uruchomienie aplikacji, czyli serwera www;
    - ``dane.py`` – moduł opcjonalny, którego zadaniem jest odczytanie wstępnych danych z pliku *csv* i dodanie ich do bazy.

Wszystkie powyższe pliki muszą znajdować się w katalogu aplikacji ``quiz2``.
W podkatalogach ``templates`` umieścimy wszystkie szablony, czyli pliki
z rozszerzeniem *html*, arkusz stylów o nazwie ``style.css`` znajdzie się
w podkatalogu ``static``. Potrzebną strukturę katalogów można utworzyć poleceniami:

.. code-block:: bash

    ~$ mkdir quiz2
    ~$ cd quiz2
    ~$ mkdir templates; mkdir static
    ~$ touch app.py

Komendę z ostatniej linii, która tworzy pusty plik o podanej nazwie,
wydajemy w miarę rozbudowywania aplikacji. Można oczywiście korzystać
z wybranego edytora.

Aplikacja i baza
*******************

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: quiz2_pw/app.py
    :linenos:

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: quiz2_sa/app.py
    :linenos:

Moduł ``app.py``, jak wskazuje sama nazwa, służy zainicjowaniu aplikacji
Flaska (``app = Flask(__name__)``).
Jej ustawienia przechowywane są w słowniku ``.config``. Oprócz klucza
używanego do obsługi sesji (``SECRET_KEY``), a także nazwy wykorzystywanej
w szablonach (``TYTUL``), w przypadku SQLAlchemy definiujemy tu nazwę pliku
bazy danych (``SQLALCHEMY_DATABASE_URI='sqlite:///quiz.db'``)
i wyłączamy śledzenie modyfikacji (``SQLALCHEMY_TRACK_MODIFICATIONS=False``).
Następnie tworzymy instancję obiektu reprezentującego bazę.

Peewee wykorzystuje specjalną zmienną ``g``, w której możemy przechowywać
różne zasoby składające się na kontekst aplikacji, np. instancję bazy.
Tworzymy ją przekazując konstruktorowi nazwę pliku (``SqliteDatabase('quiz.db')``).
Następnie przy użyciu odpowiednich dekoratorów Flaska definiujemy funkcje
otwierające i zamykające połączenie w ramach każdego cyklu żądanie-odpowiedź,
co stanowi specyficzny wymóg bazy SQLite.

SQLAlchemy będziemy obsługiwać za pomocą rozszerzenia ``flask_sqlalchemy``,
które ułatwia używanie tego systemu ORM. Dzięki niemu tworzymy instancję
bazy powiązaną z konkretną aplikacją Flaska dzięki prostemu wywołaniu
odpowiedniego konstruktora (``baza = SQLAlchemy(app)``).

Modele
*******************

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: quiz2_pw/models.py
    :linenos:

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: quiz2_sa/models.py
    :linenos:

Modele to miejsce, w którym opisujemy strukturę naszej bazy danych,
a więc definiujemy klasy – odpowiadające tabelom i ich właściwości -
odpowiadające kolumnom. Jak widać, wykorzystamy tabelę ``Pytanie``,
zawierającą treść pytania i poprawną odpowiedź, oraz tabelę ``Odpowiedź``,
która przechowywać będzie wszystkie możliwe odpowiedzi. Relację
*jeden-do-wielu* między tabelami tworzyć będzie pole ``pnr``, czyli klucz obcy (``ForeignKey``),
przechowujący identyfikator pytania. W obu systemach nieco inaczej definiujemy
to powiązanie, w Peewee podajemy nazwę klasy (``Pytanie``), w SQLAlchemy
nazwę konkretnego pola (``pytani.id``). W obu przypadkach inaczej też określamy
relacje zwrotne w postaci pola ``odpowiedzi``, za pomocą którego w obiekcie
``Pytanie`` będziemy mieli dostęp do przypisanych mu odpowiedzi.

Na uwagę zasługują atrybuty dodatkowe, dzięki którym po usunięciu pytania,
usunięte również zostaną wszystkie przypisane mu odpowiedzi. W Peewee
podajemy: ``on_delete = 'CASCADE'``; w SQLAlchemy: ``cascade="all, delete, delete-orphan"``.

Warto zauważyć również, że w SQLAlchemy dzięki rozszerzeniu ``flask.ext.sqlalchemy``
jedyny import, którego potrzebujemy, to obiekt ``baza``, który udostępnia
wszystkie klasy i metody SQLAlchemy. Druga rzecz to miejsce, w którym określamy
relację zwrotną. Inaczej niż w Peewee robimy to w klasie ``Pytanie``.

Widoki
*******************

Przypomnijmy, że widoki to funkcje obsługujące przypisane im adresy url.
Najczęściej po wykonaniu określonych operacji zawierają również wywołanie
szablonu html, który uzupełniony o ewentualne dane zostaje odesłany użytkownikowi.
Zawartość tych funkcji jest w dużej mierze niezależna od obsługi bazy,
dlatego poniżej prezentować będziemy kompletny kod dla Peewee,
a potrzebne zmiany dla SQLAlchemy będziemy wskazywać w komentarzu lub
przywoływać we fragmentach. Warto również zaznaczyć,
że wykorzystywane szablony dla obu systemów są takie same.

Strona główna i szablony
============================

Widok obsługujący stronę główną w obu przypadkach jest prawie taki sam,
w *Peewee* linia ``from app import baza`` nie jest potrzebna:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: quiz2_sa/views.py
    :linenos:
    :lineno-start: 1
    :lines: 1-13

Zadaniem funkcji ``index()`` jest tylko wywołanie renderowania szablonu
``index.html``, który zostanie zwrócony użytkownikowi. W omówionych
do tej pory scenariuszach aplikacji internetowych (*Quiz*, *ToDo*) opartych
na Flasku każdy szablon zawierał kompletny kod strony. W praktyce jednak
spora część kodu HTML powtarza się na każdej stronie w ramach danego serwisu.
W związku z tym nasze szablony będą oparte o wzorzec zawierający stałe
elementy i bloki oznaczające fragmenty, które będzie można dostosować
do danego widoku. Wzorzec umieszczamy w katalogu ``templates`` pod nazwą
``szkielet.html``.

.. raw:: html

    <div class="code_no">Szablon <i>szkielet.html</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: quiz2_pw/templates/szkielet.html
    :linenos:

Przypomnijmy i uzupełnijmy składnię. Instrukcje sterujące otoczone znacznikami
``{% %}`` wymagają otwarcia i zamknięcia, np.: ``{% for %} {% endfor %}``.
Nowy znacznik ``{% block nazwa_bloku %}`` pozwala definiować nazwane miejsca,
w których szablony dziedziczące mogą wstawiać swój kod. Jeżeli chcemy
umieścić w kodzie konkretne wartości używamy znaczników ``{{ zmienna }}``.

We wzorcu szablonów zawarliśmy więc elementy stałe, takie jak dołączane style css
w nagłówku strony, menu nawigacyjne wyświetlane na każdej stronie
(``<div id="menu" class="cb">...</div>``) oraz wyświetlanie komunikatów
(``<div id="komunikaty" class="cb">``). W każdym szablonie zwracanym przez
zdefiniowane widoki możemy natomiast zmienić tytuł strony
(``{% block tytul %}{% endblock %}``), nagłówek strony
(``{% block h1 %}{% endblock %}``) i przede wszystkim treść
(``{% block tresc %}{% endblock %}``). Tak właśnie robimy w szablonie
``index.html``:


.. raw:: html

    <div class="code_no">Szablon <i>index.html</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: quiz2_pw/templates/index.html
    :linenos:

Każdy szablon dziedziczący z wzorca musi zawierać znacznik ``{% extends "szkielet.html" %}``,
a jeżeli coś zmienia, umieszcza odpowiednią treść w znaczniku typu
``{% block tresc %} treść {% endblock %}``.

Dla porządku spójrzmy jeszcze na zawartość pliku ``style.css`` zapisanego
w katalogu ``static`` i określającego wygląd naszej aplikacji.

.. raw:: html

    <div class="code_no">Arkusz stylów <i>style.css</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: css
.. literalinclude:: quiz2_pw/static/style.css
    :linenos:

Powiązanie modułów
***********************

Po zdefiniowaniu aplikacji, bazy, modelu, widoków i wykorzystywanych
przez nie szablonów, trzeba wszystkie moduły połączyć w całość.
Posłuży nam do tego plik ``main.py``:

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: quiz2_pw/main.py
    :emphasize-lines: 12
    :linenos:

Żeby zrozumieć rolę tego modułu, wystarczy prześledzić źródła importów,
które w Pythonie odpowiadają nazwom plików. Tak więc z pliku (modułu)
``app.py`` importujemy instancję aplikacji i bazy, z ``models.py``
klasy opisujące schemat bazy, a z ``views.py`` zdefiniowane widoki.
W podanym kodzie najważniejsze jest polecenie tworzące bazę i tabele:
``baza.create_tables([Pytanie, Odpowiedz],True)``; w SQLAlchemy
trzeba zastąpić je wywołaniem ``baza.create_all()``. Zostanie ono wykonane,
o ile na dysku nie istnieje już plik bazy ``quiz.db``.

Ostatnie polecenie ``app.run(debug=True)`` ma uruchomić naszą aplikację
w trybie debugowania. Czas więc uruchomić nasz testowy serwer:

.. code-block:: bash

    ~/quiz2$ python main.py

.. figure:: quiz2_1.png

Po wpisaniu w przeglądarce adresu 127.0.0.1:5000 powinniśmy zobaczyć:

.. figure:: quiz2_2.png

Widoki CRUD
*********************

Skrót :term:`CRUD` (*Create* (tworzenie), *Read* (odczyt), *Update* (aktualizacja), *Delete* (usuwanie))
oznacza, jak wyjaśniono, podstawowe operacje wykonywane na bazie danych.

Dane początkowe
====================

Moduł ``dane.py``:

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: quiz2_sa/dane.py
    :linenos:
    :lineno-start: 1
    :lines: 1-22

W *Peewee* linia ``from app import baza`` nie jest potrzebna.

Plik z danymi:

.. raw:: html

    <div class="code_no">Plik <i>pytania.csv</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: quiz2_pw/pytania.csv
    :linenos:

Pierwsza funkcja ``pobierz_dane('pytania.csv')`` odczytuje z podanego pliku kolejne
linie zawierające pytanie, odpowiedzi i odpowiedź prawidłową oddzielone znakiem
"#". Z odczytanych linii usuwamy znaki końca linii, następnie ustawiamy
kodowanie znaków, a na koniec rozbijamy je na trzy elementy (``line.split("#")``),
z których tworzymy tuple i dodajemy ją do listy ``dane.append(tuple(...))``.
Na koniec listę tupli zwracamy jako tuplę, która trafia do wywołania
drugiej funkcji ``dodaj_pytania()``.

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: quiz2_pw/dane.py
    :linenos:
    :lineno-start: 24
    :lines: 24-

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: quiz2_sa/dane.py
    :linenos:
    :lineno-start: 25
    :lines: 25-

Pętla ``for pytanie,odpowiedzi,odpok in dane:`` do oddzielonych przecinkami
zmiennych odczytuje z przekazanych tupli kolejne dane. Następnie
tworzymy obiekty reprezentujące rekordy w tablicy *pytanie*
(``pyt = Pytanie(pytanie = pytanie, odpok = odpok)``) i wywołujemy
odpowiednie dla danego ORM-u polecenia zapisujące je w bazie. Podobnie
postępujemy w pętli wewnętrznej, przy czym tworząc obiekty odpowiedzi
wykorzystujemy identyfikatory zapisanych wcześniej pytań
(``odp = Odpowiedz(pnr = pyt.id, odpowiedz = o.strip())``).

Odczyt
====================

Zaczniemy od widoku wyświetlającego pobrane z bazy dane w formie quizu
i sprawdzającego udzielone przez użytkownika odpowiedzi.

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: quiz2_pw/views.py
    :emphasize-lines: 18,23
    :linenos:
    :lineno-start: 15
    :lines: 15-37

Wyświetlenie pytań wymaga odczytania ich wraz z możliwymi odpowiedziami z bazy.
W Peewee korzystamy z kodu: ``Pytanie().select().annotate(Odpowiedz)``,
w SQLAlchemy: ``Pytanie.query.join(Odpowiedz)`` (metoda ``.join()``
zwiększa efektywność, bo wymusza pobranie możliwych odpowiedzi
w jednym zapytaniu). Po sprawdzeniu, czy mamy jakiekolwiek pytania za pomocą
metody ``.count()``, zwracamy użytkownikowi szablon ``quiz.html``, któremu
przekazujemy w zmiennej ``pytania`` dane w odpowiedniej formie. W SQLALchemy
korzystamy z metody ``.all()`` zwracającej pasujące rekordy jako listę.

Szablon ``quiz.html`` – oparty na omówionym wcześniej wzorcu – wyświetla pytania
i możliwe odpowiedzi jako pola opcji typu radio button:

.. raw:: html

    <div class="code_no">Szablon <i>quiz.html</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: quiz2_pw/templates/quiz.html
    :linenos:

Użytkownik po wybraniu odpowiedzi naciska przycisk *Sprawdź...* i przesyła
do naszego widoku dane w żądaniu typu :term:`POST`. W funkcji ``quiz()``
uwzględniamy taką sytuację i w pętli ``for pid, odp in request.form.items():``
odczytujemy identyfikator pytania i udzieloną odpowiedź. Następnie
pobieramy odpowiedź prawidłową w Peewee za pomocą kodu
``odpok = Pytanie.select(Pytanie.odpok).where(Pytanie.id == int(pid)).scalar()``,
a w SQLALchemy ``odpok = baza.session.query(Pytanie.odpok).filter(Pytanie.id == int(pid)).scalar()``.
W obu przypadkach metody ``.scalar()`` zwracają pojedyncze wartości, które
porównujemy z odpowiedziami użytkownika (``if odp == odpok:``) i w przypadku
poprawności zwiększamy wynik.

.. figure:: quiz2_3.png

Dodawanie i aktualizacja
=============================

Możliwość dodawania nowych pytań i odpowiedzi wymaga stworzenia nowego
widoku powiązanego z określonym adresem url, jak i szablonu, który
wyświetli użytkownikowi właściwy formularz. Na początku zajmiemy się
właśnie nim.

.. raw:: html

    <div class="code_no">Szablon <i>dodaj.html</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: quiz2_pw/templates/dodaj.html
    :linenos:

Powyższy kod umieszczamy w pliku ``dodaj.html`` w katalogu szablonów, czyli
``templates``. Jak widać najważniejszym elementem jest tu formularz.
Zawiera on pola tekstowe przeznaczone na pytanie, trzy odpowiedzi
i numer odpowiedzi poprawnej. Takiego formularza możemy użyć zarówno do dodawania nowych,
jak i edycji istniejących już pytań. Jedyna różnica będzie taka, że
przy edycji musimy w formularzu wyświetlić dane wybranego pytania.
Dlatego w kodzie szablonu stosujemy instrukcję warunkową ``{% if pytanie %}``,
która decyduje o tym, czy wyświetlamy puste pola, czy wypełniamy je
przekazanymi danymi. W tym ostatnim przypadku umieszczamy w
formularzu dodatkowe ukryte pole, w którym zapisujemy *id* edytowanego pytania.

Załóżmy, że użytkownik wpisał lub zmienił pytanie i nacisnął przycisk
typu *submit*, czyli wysłał dane do serwera. Co dzieje się dalej? Takie
żądanie :term:`POST` trafi do widoku ``dodaj()``, co określone zostało
w atrybucie formularza: ``action="{{ url_for('dodaj') }}"``. Zobaczmy, jak
wygląda ten widok:

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: quiz2_pw/views.py
    :emphasize-lines: 21-38
    :linenos:
    :lineno-start: 40
    :lines: 40-87

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: quiz2_sa/views.py
    :linenos:
    :lineno-start: 61
    :lines: 61-78

Po otworzeniu adresu ``/dodaj`` otrzymujemy żądanie :term:`GET`,
na które odpowiadamy zwróceniem omówionego wyżej szablonu ``dodaj.html``.
Jeżeli jednak otrzymujemy dane z formularza, na początku dokonujemy prostej
walidacji, tj. sprawdzamy, czy użytkownik nie przesyła pustego pytania lub odpowiedzi,
dodatkowo, czy podał odpowiedni numer odpowiedzi poprawnej.

Obiekt ``request.form`` zawiera wszystkie dane przesłane w ramach
żądania. Jeżeli wśród nich nie ma identyfikatora pytania, co oznaczałoby
edycję, generowany jest wyjątek, który przechwytujemy za pomocą konstrukcji
``try: ... except KeyError:`` i dodajemy nowe pytanie.
Tworzymy więc nowy obiekt pytania
(``p = Pytanie(pytanie = pytanie.strip(), odpok = odpok.strip())``) i używając
odpowiednich metod zapisujemy. Podobnie dalej odczytujemy w pętli przesłane odpowiedzi,
dla każdej tworzymy nowy obiekt (``o = Odpowiedz(pnr = p, odpowiedz = odp.strip())``)
i zapisujemy.

Trochę więcej zachodu wymaga aktualizacja danych. Na początku pobieramy
obiekt reprezentujemy edytowane pytanie i odpowiedzi na nie. W Peewee kod jest cokolwiek
rozbudowany: ``p = Pytanie.select(Pytanie,Odpowiedz).join(Odpowiedz).where(Pytanie.id == int(request.form['id'])).get()``,
w SQLAlchemy jest krócej: ``p = Pytanie.query.get(request.form['id'])``.
Później odpowiednim polom przypisujemy nowe dane. Więcej różnic występuje
dalej. W Peewee przeglądamy listę obiektów reprezentujących odpowiedzi,
w każdym zmieniamy odpowiednią właściwość (``o.odpowiedz = odpowiedzi[i].strip()``)
i zapisujemy zmiany. w SQLAlchemy iterujemy po przesłanych odpowiedziach,
które zapisujemy w obiektach odpowiedzi odczytywanych bezpośrednio
z obiektu reprezentującego pytanie (``p.odpowiedzi[i].odpowiedz = odp.strip()``).

Zapisywanie lub aktualizacja danych kończy się wygenerowaniem odpowiedniego
komunikatu dla użytkownika, np. ``flash(u'Dodano pytanie:','sukces')``.
Podobnie wcześniej, jeżeli podczas walidacji otrzymanych danych pojawi
się błąd, komunikat o nim zostanie zapisany w liście ``error[]``,
a później przekazany użytkownikowi w kodzie: ``for e in error: flash(e, 'blad')``.
Warto zwrócić tu uwagę na dodatkowe argumenty w funkcji ``flash``, wskazują
one rodzaj przekazywanych informacji, co wykorzystujemy we wzorcu
``szkielet.html``. Pętla ``{% for kategoria, komunikat in get_flashed_messages(with_categories=true) %}``
w zmiennej ``kategoria`` odczytuje omawiane dodatkowe argumenty
i używa jej do oznaczenia klasy CSS decydującej o sposobie wyświetlenia
danej informacji: ``<span class="{{ kategoria }}">{{ komunikat }}</span>``.

.. figure:: quiz2_4.png

Widok edycji i usuwanie
==========================

Można zadać pytanie, jak do szablonu ``dodaj.html`` trafiają pytania, które
chcemy edytować. Odpowiada za to widok ``edytuj()``

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: quiz2_pw/views.py
    :emphasize-lines: 9,12
    :linenos:
    :lineno-start: 90
    :lines: 90-103

Na początku pobieramy wszystkie pytania przy użyciu takiego samego kodu
jak w widoku ``quiz()`` i sprawdzamy, czy w ogóle jakieś są. Jeżeli tak,
przekazujemy pytania do szablonu ``edytuj.html``.

.. raw:: html

    <div class="code_no">Szablon <i>edytuj.html</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: html
.. literalinclude:: quiz2_pw/templates/edytuj.html
    :linenos:

Zadaniem szablonu jest wyświetlenie treści pytań i dwóch przycisków typu
*submit*, umożliwiających edycję lub usunięcie pytania. Przyciski te
są częścią formularzy, które zawierają tylko jedno ukryte pole przechowujące
*id* pytania. O tym, gdzie trafia identyfikator decyduje atrybutu *action*
w formularzu: ``{{ url_for('edytuj') }}`` lub ``{{ url_for('usun') }}``.
Używamy tu funkcji ``url_for``, która na podstawie podanego widoku generuje
odpowiadający mu adres url.

Jeżeli użytkownik wybierze edycję, do omawianego widoku ``edytuj()`` trafia
żądanie :term:`POST`, które obsługujemy w ten sposób, że na podstawie
odebranego identyfikatora tworzymy obiekt z żądanym pytaniem i odpowiedziami
(w SQLAlchemy stosujemy tu polecenie: ``Pytanie.query.get(pid)``), a następnie
każemy go wyrenderować w szablonie ``dodaj.html``. Działanie tego szablonu
omówiono wyżej. Jeżeli użytkownik kliknie przycisk *Usuń* jego żądanie
trafia do widoku ``usun()``. Funkcja ta przedstawia się następująco:

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: quiz2_pw/views.py
    :emphasize-lines: 5-6
    :linenos:
    :lineno-start: 106
    :lines: 106-

Działanie jest proste. Tworzymy obiekt reprezentujący pytanie o przesłanym
identyfikatorze i wywołujemy metodę, która go usuwa.. W Peewee korzystamy z polecenia:
``Pytanie.get(Pytanie.id == int(pid))`` i metody ``delete_instance(recursive = True)``;
dodatkowy argument ``recursive`` zapewnia kaskadowe usunięcie wszystkich odpowiedzi.
W SQLAlchemy pozyskany obiekt ``p = Pytanie.query.get(pid)`` usuwamy za pomocą
metody sesji ``baza.session.delete(p)``, którą finalnie zapisujemy ``baza.session.commit()``.
Na koniec wywołujemy za pomocą tzw. przekierowania widok strony głównej
(``return redirect(url_for('index'))``), który wyświetli przygotowane dla użytkownika komunikaty.
*Nota bene*, podobnie postąpiliśmy również w innych omówionych wyżej widokach.

.. figure:: quiz2_5.png

Poćwicz sam
===============

    Spróbuj napisać wersję omówionej w innym scenariuszu aplikacji :ref:`ToDo <todo>`
    przy wykorzystaniu wybranego systemu ORM, tj. Peewee lub SQLAlchemy.

Źródła
*************************

* :download:`quiz2.zip <quiz2.zip>`

Kompletne wersje kodu znajdziesz w powyższym archiwum w podkatalogach :file:`quiz2_pw`
i :file:`quiz2_sa`. Uruchamiamy je poleceniami:

.. code-block:: bash

    ~/quiz2/quiz2_orm$ python main.py

\- gdzie *orm* jest oznaczeniem modułu obsługi bazy danych, *pw* dla Peewee,
*sa* dla SQLALchemy.
