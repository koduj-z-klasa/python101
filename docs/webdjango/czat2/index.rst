.. _czat2:

Czat 2
######

Dodawanie, edycja, usuwanie czy przeglądanie danych zgromadzonych w bazie
są typowymi czynnościami w aplikacjach internetowych określanymi angielskim skrótem :term:`CRUD`.
Utworzony w scenariuszu :ref:`Czat 1 <czat1>` kod ilustruje krok po korku obsługę żądań GET i POST
oraz niektórych operacji CRUD (odczyt i dodawanie danych).

Django zawiera gotowe rozwiązania, które skracają realizację typowych zadań eliminując również potencjalne błędy.
W tym scenariuszu poznasz m. in. widoki wbudowane oparte na klasach służące zarządzaniu użytkownikami oraz
odczytywaniu, dodawaniu, edytowaniu i usuwaniu danych.

.. attention::

    **Wymagane oprogramowanie**:

      * Środowisko wirtualne Pythona v. 3.x
      * Django v. 5.1.x
      * Opcjonalnie: interpreter bazy SQLite3

    **Zalecana wiedza i umiejętności**:

      Zrealizowany scenariusz :ref:`Czat 1 <czat1>`.

.. contents::
    :depth: 1
    :local:

Środowisko pracy
=================

Do pracy potrzebujemy katalogu z utworzonym środowiskiem wirtualnym Pythona, w którym zainstalowano
pakiet Django. Możemy wykorzystać katalog :file:`projekty_django` ze scenariusza :ref:`Czat 1 <czat1>`
lub przygotować ten katalog od początku zgodnie z instrukcjami (zob. :ref:`Czat 1 – Środowisko pracy <czat1-env>`

Następnie w katalogu :file:`projekty_django` tworzymy nowy projekt o nazwie **czat2**:

.. raw:: html

    <div class="code_no">Terminal nr <script>var ter_no = ter_no || 1; document.write(ter_no++);</script></span></div>

.. code-block:: bash

    (.venv) ~/projekty_django$ django-admin startproject czat2
    (.venv) ~/projekty_django$ cd czat2

Lista użytkowników
==================

Na początku zajmiemy się obsługą użytkowników, która realizowana będzie przez osobną aplikację.

W katalogu :file:`projekty_django/czat2` tworzymy aplikację o nazwie **users**:

.. raw:: html

    <div class="code_no">Terminal nr <script>var ter_no = ter_no || 1; document.write(ter_no++);</script></span></div>

.. code-block:: bash

    (.venv) ~/projekty_django/czat2$ python manage.py startapp users

Następnie tworzymy plik :file:`czat2/users/urls.py`, w którym umieszczamy poniższy kod:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/users_urls_01.py
    :linenos:
    :lineno-start: 1
    :lines: 1-7

W liście ``urlpatterns`` definiujemy powiązanie między domyślnym adresem URL aplikacji i widokiem ``index``.

Dalej w pliku :file:`czat2/users/views.py` umieszczamy kod widoku, czyli funkcję ``index()``:

.. raw:: html

    <div class="code_no">Plik <i>views.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/users_views.py
    :linenos:
    :lineno-start: 1
    :lines: 1-7

Zadaniem widoku jest pobranie z bazy danych wszystkich użytkowników i przekazanie ich do szablonu.

Kolejnym krokiem jest utworzenie odpowiednich podkatalogów i umieszczenie kodu szablonu
w pliku :file:`czat2/users/templates/users/index.html`:

.. raw:: html

    <div class="code_no">Plik <i>index.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: HTML
.. literalinclude:: source/users_index_01.html
    :linenos:
    :lineno-start: 1

W pierwszym tagu warunkowym ``{% if users %}`` sprawdzamy, czy lista ``users`` zawiera jakichś użytkowników.
Jeżeli tak, za pomocą tagu ``for`` wypiszemy ich nazwy, w przeciwnym razie komunikat "Brak użytkowników".

W drugim tagu warunkowym ``{% if user.is_authenticated %}`` sprawdzamy, czy jakiś użytkownik jest zalogowany.
Jeżeli tak, wypiszemy komunikat "Jesteś już zalogowany jako ...", w przeciwnym razie wypisany zostanie
link do utworzenia konta.

Dodawanie użytkowników
======================

Użytkownicy będą mogli samodzielnie zakładać konta, logować i wylogowywać się.
Inaczej niż w aplikacji *Czat 1* zadania te zrealizujemy za pomocą tzw. widoków wbudowanych opartych na klasach
(ang. `class-based generic views <https://docs.djangoproject.com/en/5.2/topics/class-based-views/>`_).

W pliku :file:`czat2/users/urls.py` importujemy formularz tworzenia użytkownika (``UserCreationForm``)
oraz wbudowany widok przeznaczony do dodawania danych (``CreateView``):

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/users_urls_02.py
    :linenos:
    :lineno-start: 1
    :lines: 1-4
    :emphasize-lines: 3, 4

W tym samym pliku :file:`czat2/users/urls.py` w liście ``urlpatterns`` definiujemy adres URL */rejestruj*,
który obsługiwany będzie przez zaimportowany wyżej widok wywołany jako funkcja.

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/users_urls_02.py
    :linenos:
    :lineno-start: 10
    :lines: 10-14

Widok ``CreateView`` otrzymuje trzy argumenty, które przekazujemy do metody ``as_view()``:

    * ``template_name`` – nazwa pliku szablonu, w którym umieścimy formularz tworzenia użytkownika,
    * ``form_class`` – nazwa klasy definiującej formularz tworzenia użytkownika,
    * ``success_url`` – adres, na który nastąpi przekierowanie w przypadku braku błędów, np. po udanej rejestracji.

Zawartość szablonu umieszczamy w pliku :file:`templates/users/rejestruj.html`:

.. raw:: html

    <div class="code_no">Plik <i>rejestruj.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: HTML
.. literalinclude:: source/rejestruj.html
    :linenos:

Jeżeli zalogowany użytkownik wejdzie na stronę, zobaczy komunikat "Jesteś już zalogowany jako ...", natomiast
użytkownik niezalogowany zobaczy formularz zakładania konta.

Ćwiczenie
---------

1) W ustawieniach projektu *czat2*:

    - zarejestruj aplikację *users*,
    - ustaw polską wersję językową,
    - zlokalizuj datę i czas.

2) W konfiguracji adresów URL projektu powiąż adres URL ``users/`` z adresami URL aplikacji *users*.
3) Uruchom serwer deweloperski i w przeglądarce wejdź na adres *127.0.0.1:8000/users/*.
4) Dodaj użytkowników *adam* i *ewa* z hasłem *zaq1@WSX*.

.. figure:: img/django_rejestracja.png

.. figure:: img/django_lista_uzytkownikow.png

Wy(logowanie)
=============

Na początku pliku :file:`czat2/users/urls.py` aplikacji dopisujemy wymagany import:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/users_urls_02.py
    :linenos:
    :lineno-start: 5
    :lines: 5

– a następnie uzupełniamy listę ``urlpatterns``:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/users_urls_02.py
    :linenos:
    :lineno-start: 15
    :lines: 15-21

Z adresami */loguj* i */wyloguj* wiążemy wbudowane w Django widoki ``LoginView`` i ``LogoutView``
zaimportowane z modułu ``django.contrib.auth.views``. Widoki wywołujemy jako funkcje za pomocą metody ``as_view()``,
która otrzymuje argumenty:

    * ``template_name`` – nazwę pliku szablonu, w którym umieścimy formularz logowania użytkownika,
    * ``next_page`` – nazwa adresu URL, na który przekierowujemy użytkownika po zalogowaniu lub wylogowaniu się.

.. note::

    Adresy, na które zostaje przekierowany użytkownik po zalogowaniu lub wylogowaniu za pomocą widoków wbudowanych,
    mogą być określane również za pomocą stałych ``LOGIN_REDIRECT_URL`` i ``LOGOUT_REDIRECT_URL`` zdefiniowanych w pliku
    ustawień projektu. W naszym przypadku na końcu pliku :file:`czat2/settings.py` moglibyśmy umieścić kod:

.. raw:: html

    <div class="code_no">Plik <i>settings.py</i>. <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. code-block:: python

    LOGIN_REDIRECT_URL = '/users/'
    LOGOUT_REDIRECT_URL = '/users/'

Logowanie wymaga szablonu, który tworzymy i zapisujemy w pliku :file:`templates/users/loguj.html`:

.. raw:: html

    <div class="code_no">Plik <i>loguj.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: HTML
.. literalinclude:: source/loguj.html
    :linenos:

Ćwiczenie
---------

1) W szablonie :file:`users/index.html` umieść linki służące do logowania i wylogowania. Użyj metody POST.

.. figure:: img/django_zaloguj.png

2) Zaloguj się jako użytkownik.

.. figure:: img/django_logowanie.png

3) Wyloguj się.

.. figure:: img/django_wyloguj.png

Wiadomości
===========

Chcemy, by zalogowani użytkownicy mogli przeglądać wiadomości wszystkich użytkowników,
zmieniać, usuwać i dodawać własne. Podobnie jak w przypadku obsługi użytkowników,
w realizacji tych zadań również użyjemy widoków wbudowanych opartych na klasach.

.. note::

    Django oferuje wbudowane widoki przeznaczone do typowych operacji:

    * *DetailView* i *ListView* – (ang. *generic display view*) widoki przeznaczone
      do prezentowania szczegółów i listy danych;
    * *FormView*, *CreateView*, *UpdateView* i *DeleteView* – (ang. *generic editing views*)
      widoki przeznaczone do wyświetlania formularzy ogólnych, w szczególności
      służących dodawaniu, uaktualnianiu, usuwaniu obiektów (danych).

Początek pracy będzie podobny jak w przypadku aplikacji "Czat 1":

1) W katalogu :file:`projekty_django/czat2` tworzymy aplikację *czat*.
2) Rejestrujemy aplikację w projekcie.
3) Dodajemy model danych, tj. klasę ``Wiadomości`` w pliku :file:`models.py`:

.. raw:: html

    <div class="code_no">Plik <i>models.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/models.py
    :linenos:

.. warning::

    W porównaniu do modelu użytego w aplikacji *Czat 1* w definicji pola ``data_pub`` argument ``auto_now_add=True``
    zastępujemy ``default=timezone.now``, aby użytkownik mógł modyfikować datę dodania wiadomości w formularzu.

4) Przygotowujemy migrację dla aplikacji "czat" i ją wykonujemy.

.. tip::

    Dla przypomnienia poniżej kolejne polecenia wydawane w aktywnym środowisku wirtualnym
    w katalogu :file:`projekty_django/czat2`:

    .. code-block:: bash

        (.venv) ~/projekty_django/czat2$ python manage.py startapp czat
        (.venv) ~/projekty_django/czat2$ python manage.py makemigrations czat
        (.venv) ~/projekty_django/czat2$ python manage.py migrate
        (.venv) ~/projekty_django/czat2$ python manage.py check

    Ostatnie wydane polecenie sprawdza poprawność wykonanych czynności i powinno zwrócić komunikat
    *System check identified no issues (0 silenced)*.

    Jeżeli masz problem z wykonaniem powyższych czynności, zajrzyj do punktów 8.1.2 – 8.1.3 ze scenariusza
    :ref:`Czat 1 <czat1>`.

Strona główna
=============

Chcemy, żeby aplikacja *czat* obsługiwała żądanie wyświetlenia strony głównej. W tym celu tworzymy nowy
plik :file:`projekty_django/czat/urls.py` i uzupełniamy go kodem:

.. raw:: html

    <div class="code_no">Plik <i>czat/urls.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_urls_01.py
    :linenos:

Jak widać adres domyślny aplikacji ``''`` obsługiwany ma być przez widok ``index``. Zatem w pliku :file:`czat/views.py`
umieszczamy kod:

.. raw:: html

    <div class="code_no">Plik <i>czat/views.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_views_01.py
    :linenos:

Następnie musimy dodać szablon, który umieszczamy w pliku :file:`templates/czat/index.html`:

.. raw:: html

    <div class="code_no">Plik <i>czat/index.html</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: HTML
.. literalinclude:: source/czat_index_01.html
    :linenos:

Na koniec włączamy konfigurację URL aplikacji do konfiguracji projektu, czyli w pliku
:file:`projekty_django/czat2/urls.py` lista ``urlpatterns`` powinna wyglądać następująco:

.. raw:: html

    <div class="code_no">Plik <i>czat2/urls.py</i>. <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. code-block:: python

    urlpatterns = [
        path('', include('czat.urls')),
        path('czat/', include('czat.urls')),
        path('users/', include('users.urls')),
        path('admin/', admin.site.urls),
    ]

Ćwiczenie
----------

1) Uruchamiamy serwer deweloperski i otwieramy w przeglądarce adres domyślny ``127.0.0.1:8000``,
   powinniśmy zobaczyć stronę wygenerowaną na podstawie dodanego szablonu:

.. figure:: img/czat2_strona_glowna.png

Lista wiadomości
================

W pliku :file:`projekty_django/czat/urls.py` uzupełniamy importy i dodajemy definicję adresu URL:

.. raw:: html

    <div class="code_no">Plik <i>czat/urls.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_urls_02.py
    :linenos:
    :lineno-start: 1
    :lines: 1-9
    :emphasize-lines: 2-4, 9

Adres ``lista/`` będzie obsługiwany przez klasę zdefiniowaną w pliku ``views.py``, którą wywołujemy jako funkcję:
``views.ListaWiadomosci.as_view()``. Wywołanie umieszczamy w funkcji ``login_required()``, aby wiadomości mogli
oglądać tylko zalogowani użytkownicy.

Adres, na który przekierowany zostanie użytkownik, jeżeli nie będzie zalogowany, definiujemy
na końcu pliku :file:`czat2/settings.py` w stałej ``LOGIN_URL``:

.. raw:: html

    <div class="code_no">Plik <i>czat2/settings.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. code-block:: python

    LOGIN_URL = '/users/loguj'

Do pliku :file:`czat/views.py` dodajemy wymagane do wszystkich operacji :term:`CRUD` importy
oraz kod klasy ``ListaWiadomosci``:

.. raw:: html

    <div class="code_no">Plik <i>czat/views.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_views_02.py
    :linenos:
    :lineno-start: 1
    :lines: 1-17
    :emphasize-lines: 2-6, 13-16

Klasę ``ListaWiadomosci`` tworzymy na podstawie wbudowanej wbudowanej klasy ``ListView``
i dostosowujemy jej właściwości:

* ``model`` – podajemy model, którego dane zostaną pobrane z bazy;
* ``context_object_name`` – zmieniamy domyślną nazwę (object_list) listy obiektów przekazanych do szablonu;
* ``paginate_by``– określamy ilość obiektów wyświetlanych na stronie.

Szablon
-------

Potrzebujemy szablonu, którego klasa ``ListView`` szuka pod domyślną nazwą *<nazwa modelu>_list.html*,
czyli w naszym przypadku tworzymy plik :file:`templates/czat/wiadomosc_list.html`:

.. raw:: html

    <div class="code_no">Plik <i>wiadomosc_list.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: source/wiadomosc_list_01.html
    :linenos:

Kolejne wiadomości odczytujemy i wyświetlamy w pętli przy użyciu tagu ``{% for %}``.
Dostęp do właściwości obiektów umożliwia operator kropki, np.: ``{{ wiadomosc.autor.username }}``.

Linki nawigacyjne tworzymy w instrukcji warunkowej ``{% if is_paginated %}``.
Obiekt ``page_obj`` zawiera następujące właściwości:

* ``has_previous`` – zwraca ``True``, jeżeli jest poprzednia strona;
* ``previous_page_number`` – numer poprzedniej strony;
* ``next_page_number`` – numer następnej strony;
* ``number`` – numer aktualnej strony;
* ``paginator.num_pages`` – ilość wszystkich stron.

Numer strony do wyświetlenia przekazujemy w zmiennej ``page`` adresu URL.

Dodawanie wiadomości
====================

Zadanie to zrealizujemy wykorzystując widok ``CreateView``. Aby ułatwić dodawanie wiadomości
dostosujemy klasę widoku tak, aby użytkownik nie musiał wprowadzać pola autor.

Na początek dopiszemy w pliku :file:`czat/urls.py` skojarzenie adresu URL ``dodaj/``
z wywołaniem zaimportowanej z pliku :file:`views.py` klasy ``DodajWiadomosc`` jako funkcji:

.. raw:: html

    <div class="code_no">Plik <i>czat/urls.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_urls_02.py
    :linenos:
    :lineno-start: 10
    :lines: 10

Dalej w pliku :file:`czat/views.py` umieszczamy kod:

.. raw:: html

    <div class="code_no">Plik <i>czat/views.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. literalinclude:: source/czat_views_02.py
    :linenos:
    :lineno-start: 19
    :lines: 19-36

Klasa ``DodajWiadomosc`` dziedziczy z klasy ``CreateView``. Określamy jej właściwości i nadpisujemy wybrane metody:

* ``fields`` – pozwala wskazać pola, które mają znaleźć się na formularzu;
* ``get_initial()`` – metoda pozwala ustawić domyślne wartości dla wybranych pól.
  Wykorzystujemy ją do zainicjowania pola ``data_pub`` aktualna datą: ``initial['data_pub'] = timezone.now()``.
* ``form_valid()`` – metoda, która sprawdza poprawność przesłanych danych i zapisuje je w bazie:

    - ``wiadomosc = form.save(commit=False)`` – tworzymy obiekt wiadomości, ale go nie zapisujemy;
    - ``wiadomosc.autor = self.request.user`` – uzupełniamy dane autora;
    - ``wiadomosc.save()`` – zapisujemy obiekt;
    - ``messages.success(self.request, "Dodano wiadomość!")`` – przygotowujemy komunikat,
      który wyświetlony zostanie po dodaniu wiadomości.

Szablon
--------

Domyślny szablon dodawania danych dla klasy ``CreateView`` nazywa się *<nazwa modelu>_form.html*.
W nowym pliku wstawiamy poniższą treść i zapisujemy pod nazwą :file:`templates/czat/wiadomosc_form.html`:

.. raw:: html

    <div class="code_no">Plik <i>wiadomosc_form.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: source/wiadomosc_form.html
    :linenos:

W szablonie :file:`templates/czat/index.html` wstawiamy jeszcze po nagłówku ``<h1>`` kod wyświetlający komunikaty:

.. raw:: html

    <div class="code_no">Plik <i>index.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. code:: HTML

        {% if messages %}
          <ul>
            {% for komunikat in messages %}
              <li>{{ komunikat|capfirst }}</li>
              {% endfor %}
          </ul>
        {% endif %}

Ćwiczenie
----------

1) Umieść link do dodawania wiadomości na końcu strony *Lista wiadomości*.

.. figure:: img/django_dodawanie.png

2) Dodaj jakąś wiadomość:

.. figure:: img/django_dodawanie2.png

Edycja wiadomości
=================

Widok pozwalający na edycję wiadomości i jej aktualizację dostępny będzie
pod adresem **/edytuj/<pk>**, gdzie **<pk>** będzie identyfikatorem
obiektu do zaktualizowania. Zaczniemy od uzupełnienia pliku :file:`urls.py`:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_urls_02.py
    :linenos:
    :lineno-start: 11
    :lines: 11

Nowością w powyższym kodzie jest definicja adresu z dodatkowym parametrem ``<pk>`` – nazwa jest tu skrótem
od ang. *primary key*, co znaczy "klucz główny". Zmienna ta zawierać będzie identyfikator wiadomości
i dostępna będzie w klasie widoku, który obsłuży edycję wiadomości.

Do pliku :file:`views.py` dopisujemy kod klasy ``EdytujWiadomosc``, która dostosowuje wbudowany widok ``UpdateView``:

.. raw:: html

    <div class="code_no">Plik <i>views.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_views_02.py
    :linenos:
    :lineno-start: 38
    :lines: 38-55

Nowe metody to:

- ``get_object()`` – pobiera i zwraca wskazaną przez identyfikator w zmiennej *pk* wiadomość:
  ``wiadomosc = Wiadomosc.objects.get(id=self.kwargs['pk'])``.
- ``get_context_data()`` – pozwala przekazać do szablonu dodatkowe dane,
  w tym przypadku listę wiadomości, ale tylko zalogowanego użytkownika:
  (``context['wiadomosci'] = Wiadomosc.objects.filter(autor=self.request.user)``).

Pozostałe właściwości ``model``, ``context_object_name``, ``template_name`` i ``success_url``
wyjaśniliśmy wcześniej. Jak widać, do edycji wiadomości wykorzystamy ten sam szablon,
którego użyliśmy podczas dodawania.

Formularz jednak dostosujemy. Wykorzystamy właściwość ``form_class``,
której przypisujemy utworzoną w nowym pliku :file:`czat/forms.py` klasę zmieniającą domyślne ustawienia:

.. raw:: html

    <div class="code_no">Plik <i>forms.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_forms.py
    :linenos:

Klasa ``EdytujWiadomoscForm`` oparta jest na wbudowanej klasie ``ModelForm``.
Właściwości formularza określamy w podklasie ``Meta``:

* ``model`` – oznacza to samo co w widokach, czyli model, dla którego tworzony jest formularz;
* ``fields`` – to samo co w widokach, lista pól do wyświetlenia;
* ``exclude`` – opcjonalnie lista pól do pominięcia;
* ``widgets`` – słownik, którego klucze oznaczają pola danych, a ich wartości
  odpowiadające im w formularzach HTML typy pól i ich właściwości, np. rozmiar.

Teraz w szablonie :file:`wiadomosc_list.html` musimy dodać link, aby zalogowany użytkownik mógł
edytować swoje wiadomości. Kod wypisujący wiadomości w znaczniku ``<li>`` przyjmie następującą postać:

.. raw:: html

    <div class="code_no">Plik <i>wiadomosc_lista.html</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: source/wiadomosc_list_02.html
    :linenos:
    :lineno-start: 21
    :lines: 21-27
    :emphasize-lines: 4-6

Ćwiczenie
----------

1) Wejdź na stronę "Lista wiadomości" i kliknij link *Edytuj*:

.. figure:: img/django_edycja_01.png

2) Zmień treść wiadomości i kliknij przycisk *Zapisz*:

.. figure:: img/django_edycja_02.png

Usuwanie wiadomości
===================

Do usuwania wiadomości wykorzystamy – podobnie jak w przypadku edycji – adres zawierający jej identyfikator:
**/edytuj/<pk>**. Uzupełniamy więc plik :file:`urls.py`:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_urls_02.py
    :linenos:
    :lineno-start: 12
    :lines: 12

Na końcu pliku :file:`views.py` umieszczamy kod klasy ``UsunWiadomosc``, która wykorzystuje wbudowany widok ``DeleteView``:

.. raw:: html

    <div class="code_no">Plik <i>views.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/czat_views_02.py
    :linenos:
    :lineno-start: 57
    :lines: 57-60

Domyślny szablon dla tego widoku przyjmuje nazwę *<nazwa-modelu>_confirm_delete.html*,
dlatego uprościliśmy jego nazwę we właściwości ``template_name``. Tworzymy więc plik :file:`wiadomosc_usun.html`:

.. raw:: html

    <div class="code_no">Plik <i>wiadomosc_usun.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: source/wiadomosc_usun.html
    :linenos:

Tag ``{{ object }}`` zostanie zastąpiony treścią wiadomości zwróconą przez funkcję ``__str__()`` modelu.

Ćwiczenie
----------

1) W szablonie :file:`wiadomosc_list.html` za linkiem *Edytuj* wstaw podobny link *Usuń*:
   ``&bull; <a href="{% url 'czat:usun' wiadomosc.id %}">Usuń</a>``, aby zalogowany użytkownik mógł
   usunąć wiadomość.

2) Wejdź na stronę "Lista wiadomości" i kliknij link *Usuń*:

.. figure:: img/django_usun_01.png

3) Potwierdź usunięcie wiadomości:

.. figure:: img/django_usun_02.png

Materiały
=========

1. `Built-in class-based generic views <https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-display/>`_
2. Strona projektu Django https://www.djangoproject.com/
3. Co to jest framework? http://pl.wikipedia.org/wiki/Framework
4. Co nieco o HTTP i żądaniach GET i POST http://pl.wikipedia.org/wiki/Http

