.. _mvc_wzorzec:

MVC
##############

W projektowaniu aplikacji internetowych odwołujemy się do wzorca M(odel)V(iew)C(ontroller),
czyli Model–Widok–Kontroler, co pozwala na oddzielenie danych od ich prezentacji oraz logiki aplikacji.
Frameworki takie jak Flask czy Django korzystają z tego wzorca

.. _mvc_model:

Model
*********

**Modele** – :term:`model` w Django reprezentuje źródło informacji;
są to klasy Pythona opisujące pojedyncze tabele w bazie danych (zob. :term:`ORM`);
atrybuty klasy odpowiadają polom tabeli, ewentualne funkcje wykonują operacje na danych.
Instancja klasy odpowiada rekordowi danych. Modele definiujemy w pliku :file:`models.py`.

.. _mvc_widok:

Widok
*************

**Widoki** – :term:`widok` we Flasku lub Django to funkcja lub klasa Pythona,
która odpowiada na żądania www, np. zwraca kod HTML generowany w szablonie (ang. *template*),
jakiś dokument, obrazek lub przekierowuje na inny adres.

W Django Widoki definiujemy w pliku :file:`views.py`. Django zawiera wiele widoków wbudowanych
(ang. *generic views*), w tym opartych na klasach opisujących modele,
umożliwiających przeglądanie (np. *ListView, DetailView*) i edycję danych (np. *CreateView, UpdateView*).

Każda funkcja pełniąca rolę widoku jako pierwszy argument otrzymuje obiekt
``HttpRequest`` zawierający informacje o żądaniu, np. jego typ (GET lub POST),
nazwę użytkownika, a zwłaszcza dane przesłane do serwera. Obiekt *request*
jest słownikiem. Widok musi zwrócić jakąś odpowiedź. W Django jest to obiekt
typu ``HttpResponse``.

Widoki wykonują jakieś operacje po stronie serwera w odpowiedzi na żądania klienta.
Widoki powiązane są z określonymi adresami url.

Dane z bazy przekazywane są do szablonów za pomocą Pythonowego słownika.
Renderowanie polega na odszukaniu pliku szablonu, zastąpieniu przekazanych
zmiennych danymi i odesłaniu całości (HTML + dane) do użytkownika.

W Django szablony zapisywane są w podkatalogu ``templates/nazwa_aplikacji``.

.. _mvc_kontroler:

Kontroler
**********

**Kontroler** – :term:`kontroler` to mechanizm kierujący kolejne żądania
do odpowiednich widoków na podstawie wzorców adresów URL. We Flasku adresy
powiązane z widokiem definiujemy w dekoratorach typu ``@app.route('/', methods=['GET', 'POST'])``.
W Django adresy wiążemy z widokami w pliku :file:`urls.py` np.: ``url(r'^loguj/$', views.loguj, name='loguj')``.

Wzorce dopasowania
===================

Fragment ``r'^loguj/$'`` to wyrażenie regularne, często określane w języku angielskim
skrótowo *regex*. Najczęściej będzie zawierać następujące symbole:

#. ``r`` – początek, ``$`` – koniec, ograniczniki granic wyrażenia
#. ``^`` – dopasowuje początek ciągu lub nowej linii
#. ``.`` – dowolny pojedynczy znak
#. ``\d`` lub ``[0-9]`` – pojedyncza cyfra dziesiętna
#. ``[a-z]``, ``[A-Z]``, ``[a-zA-Z]`` – małe i/lub duże litery
#. ``+``, np. ``\d+`` – jedno lub więcej wystąpień poprzedniego wyrażenia
#. ``?``, np. ``\d?`` – zero lub 1 wystąpienie poprzedniego wyrażenia
#. ``*``, np. ``\d*`` – zero lub więcej wystąpień poprzedniego wyrażenia
#. ``{1,3}``, np. ``\d{1,3}`` – od 1 do 3 wystąpień poprzedniego wyrażenia

Więcej nt wyrażeń regularnych w Pythonie znajdziesz w dokumentacji:
`Regular Expression Syntax <https://docs.python.org/2/library/re.html>`_.

Django
*******

Twórcy Django traktują wzorzec MVC elastycznie, twierdząc że ich framework wykorzystuje
taczej wzorzec MTV, czyli model (Model), szablon (Template), widok (View).
Oznacza to, że powiązanie widoków z adresami URL oraz same widoki decydują o tym,
co zostanie zwrócone i pełnią w ten sposób rolę kontrolera.
Szablony natomiast decydują o tym, jak to zostanie zaprezentowane użytkownikowi,
a więc pełnią rolę widoków w sensie MVC.
