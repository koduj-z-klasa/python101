Chatter – aplikacja internetowa
==========================================

.. highlight:: python

Zastosowanie Pythona i frameworka Django (wersja 1.6.5) do stworzenia aplikacji internetowej Chatter; prostego czata, w którym zarejestrowani użytkownicy będą mogli wymieniać się krótkimi wiadomościami.

Projekt i aplikacja
---------------------------------------

Tworzymy nowy projekt Django, a następnie uruchamiamy lokalny serwer, który pozwoli śledzić postęp pracy. W katalogu domowym wydajemy polecenia w terminalu:

.. raw:: html

    <div class="code_no">Terminal nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: bash

    ~ $ django-admin.py startproject chatter
    ~ $ cd chatter
    ~/chatter $ python manage.py runserver 127.0.0.1:8080

Powstanie katalog projektu chatter i aplikacja o nazwie chatter. Pod adresem *127.0.0.1:8080* w przeglądarce zobaczymy stronę powitalną.

.. note::

    Jeden projekt może zawierać wiele aplikacji zapisywanych w osobnych podkatalogach katalogu projektu.
    Lokalny serwer deweloperski można zatrzymać za pomocą skrótu Ctrl+C.

Teraz zmodyfikujemy ustawienia projektu, aby korzystał z polskiej wersji językowej oraz lokalnych ustawień daty i czasu. Musimy również zarejestrować naszą aplikację w projekcie. W pliku setting.py zmieniamy następujące linie:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # chatter/chatter/settnigs.py

    # rejestrujemy aplikacje
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'chatter', # nasza aplikacja
    )

    LANGUAGE_CODE = 'pl' # ustawienia jezyka

    TIME_ZONE = 'Europe/Warsaw' # ustawienia daty i czasu

Model – Widok – Kontroler
---------------------------------------

W projektowaniu aplikacji internetowych za pomocą Django odwołujemy się do wzorca M(odel)V(iew)C(ontroller), czyli Model–Widok–Kontroler [#]_, co pozwala na oddzielenie danych od ich prezentacji oraz logiki aplikacji. Funkcje kolejnych elementów są następujące:

:term:`Modele` – w Django reprezentują źródło informacji, są to klasy Pythona, które zawierają pola, właściwości i zachowania danych, odwzorowują pojedyncze tabele w bazie danych [#]_. Definiowane są w pliku :file:`models.py`.
:term:`Widoki` – w Django są to funkcje Pythona, które na podstawie żądań www (dla danych adresów URL) zwracają odpowiedź w postaci kodu HTML generowanego w szablonach (templates), przekierowania, dokumentu XML czy obrazka. Definiowane są w pliku :file:`views.py`.
:term:`Kontroler` – to mechanizm kierujący kolejne żądania do odpowiednich widoków na podstawie konfiguracji adresów URL zawartej w pliku :file:`urls.py`.

.. [#] Twórcy Django traktują jednak ten wzorzec elastycznie, mówiąc że ich framework wykorzystuje wzorzec MTV, czyli model (model), szablon (template), widok (view).
.. [#] Takie odwzorowanie nosi nazwę mapowania obiektowo-relacyjnego (ORM). ORM odwzorowuje strukturę bazy na obiekty Pythona.

Model danych i baza
---------------------------------------

Model, jak zostało powiedziane, jest klasą Pythona opisującą dane naszej aplikacji, czyli wiadomości. Instancje tej klasy będą konkretnymi wiadomościami napisanymi przez użytkowników systemu. Każda wiadomość  będzie zwierała treść, datę dodania oraz autora wiadomości (użytkownika).

W katalogu :file:`chatter/chatter` w pliku :file:`models.py` wpisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: models_z1.py
    :linenos:

Po skonfigurowaniu projektu i zdefiniowaniu modelu danych możemy utworzyć bazę danych [#]_ dla naszej aplikacji, czyli wszystkie potrzebne tabele. Podczas tworzenia bazy Django pyta o nazwę, email i hasło administratora. Podajemy te dane po wydaniu w katalogu projektu w terminalu polecenia:

.. raw:: html

    <div class="code_no">Terminal nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: bash

    ~/chatter $ python manage.py syncdb

.. [#] Domyślnie Django korzysta z bazy SQLite, która przechowywana jest w jednym pliku :file:`db.sqlite3` w katalogu aplikacji.

Panel administracyjny
---------------------------------------

Django pozwala szybko utworzyć panel administratora dla naszego projektu. Rejestrujemy więc model danych jako element panelu w nowo utworzonym pliku :file:`admin.py` w katalogu :file:`chatter/chatter`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: admin_z1.py
    :linenos:

Po ewentualnym ponownum uruchomieniu serwera wchodzimy na adres *127.0.0.1:8080/admin/*. Otrzymamy dostęp do panelu administracyjnego, w którym możemy dodawać nowych użytkowników i wiadomości [#]_.

.. [#] Bezpieczna aplikacja powinna dysponować osobnym mechanizmem rejestracji użytkowników i dodawania wiadomości, tak by nie trzeba było udostępniać panelu administracyjnego osobom postronnym.

Strona główna – widoki i szablony
---------------------------------------

Dodawanie stron w Django polega na tworzeniu widoków, czyli funkcji Pythona powiązanych z określonymi adresami url. Widoki najczęściej zwracały będą kod HTML wyrenderowany na podstawie szablonów, do których możemy przekazywać dodatkowe dane [#]_, np. z bazy. Dla przejrzystości przyjęto, że w katalogu aplikacji (:file:`chatter/chatter`):

1. plik :file:`views.py` zawiera definicję widoków, w tym wywołania szablonów,
2. plik :file:`url.py` zawiera reguły łączące widoki z adresami url,
3. w katalogu :file:`chatter/chatter/templates/chatter` zapisujemy szablony (templatki) pod nazwami określonymi w wywołujących je widokach, np. :file:`index.html`.

.. [#] Danych z bazy przekazywane są do szablonów za pomocą Pythonowego słownika. Renderowanie polega na odszukaniu pliku szablonu, zastąpieniu przekazanych zmiennych danymi i odesłaniu całości (HTML + dane) do użytkownika.

Aby utworzyć stronę główną, stworzymy pierwszy widok, czyli funkcję ``index()`` [#]_, którą powiążemy z adres URL głównej strony (/). Widok zwracał będzie kod wyrenderowany na podsatwie szablonu :file:`index.html`. W pliku :file:`views.py` umieszczamy:

.. [#] Nazwa ``index()`` jest przykładowa, funkcja mogłaby się nazywać inaczej.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: views_z1.py
    :linenos:

Widok :file:`index()` łączymy z adresem URL strony głównej: *127.0.0.1:8000/* w pliku :file:`urls.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: urls_z1.py
    :linenos:

Tworzymy katalog dla szablonów wydając polecenie:

.. raw:: html

    <div class="code_no">Terminal nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: bash

    ~/chatter/chatter $ mkdir -p templates/chatter

Tworzymy szablon, plik :file:`chatter/chatter/templates/chatter/index.html`, który zawiera:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: index_z1.html
    :linenos:

Po wpisaniu adresu *127.0.0.1:8080/* zobaczymy tekst, który zwróciliśmy z widoku, czyli "Witaj w systemie Chatter".

Logowanie użytkowników
---------------------------------------

Dodanie formularza logowania dla użytkowników polega na:

1. dodaniu w pliku :file:`views.py` nowego widoku ``my_login()``, który wywoływać będzie szablon zapisany w pliku :file:`templates/chatter/login.html`,
2. powiązaniu w pliku urls.py nowego widoku z adresem :file:`/login`.

Django upraszcza zadanie, ponieważ zawiera odpowiednie formularze i model reprezentujący użytkowników w systemie, z którego – nota bene – skorzystaliśmy już podczas tworzenia bazy danych.

Widok ``my_login()`` wyświetli formularz logowania i obsłuży żądania typu POST (wysłanie danych z formularza na serwer), sprawdzi więc poprawność przesłanych danych (nazwa użytkownika i hasło). Jeżeli dane będą poprawne, zaloguje użytkownika i wyświetli spersonalizowaną stronę główną (:file:`index.html`), w przeciwnym wypadku zwrócona zostanie informacja o błędzie.

Importujemy potrzebne moduły, tworzymy widok ``my_login()`` i uzupełniamy widok ``index()`` w pliku :file:`views.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: views_z2.py
    :linenos:


W pliku :file:`urls.py` dopisujemy regułę łączącą url */login* z widokiem ``my_login()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # adres logowania (/login) o nazwie login powiazany z widokiem my_login
    url(r'^login/$', views.my_login, name='login'),

Tworzymy nowy szablon :file:`login.html` w katalogu :file:`templates/chatter/`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: login_z1.html
    :linenos:

Zmieniamy również szablon :file:`index.html` głównego widoku, aby uwzględniał status użytkownika (zalogowany/niezalogowany):

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: index_z2.html
    :linenos:

Zwróćmy uwagę, jak umieszczamy linki w szablonach. Mianowicie kod ``{% url 'login' %}`` wykorzystuje wbudowaną funkcję ``url()``, która na podstawie nazwy adresu określanej w regułach pliku :file:`urls.py` (parametr ``name``) generuje skojarzony z nią adres.

JAK TO DZIAŁA:  Po przejściu pod adres *127.0.0.1:8080/login/*, powiązany z widokiem ``my_login()``, przeglądarka wysyła żądanie GET do serwera. Widok ``my_login()`` przygotowuje formularz autoryzacji (AuthenticationForm), przekazuje go do szablonu :file:`login.html` i zwraca do klienta. Efekt jest taki:

Po wypełnieniu formularza danymi i kliknięciu przycisku "Zaloguj", do serwera zostanie wysłane żądanie typu POST. W widoku ``my_login()`` obsługujemy taki przypadek za pomocą instrukcji ``if``. Sprawdzamy poprawność przesłanych danych (walidacja), logujemy użytkownika w systemie i zwracamy przekierowanie na stronę główną, która wyświetla nazwę zalogowanego użytkownika. Jeżeli dane nie są poprawne, zwracana jest informacja o błędach. Przetestuj!

Dodawanie i wyświetlanie wiadomości
---------------------------------------

Chcemy, by zalogowani użytkownicy mogli przeglądać wiadomości od innych użytkowników i dodawać własne. Utworzymy widok ``messages()``, który wyświetli wszystkie wiadomości (żądanie GET) i ewentualnie zapisze nową wiadomość nadesłaną przez użytkownika (żądanie POST). Widok skorzysta z nowego szablonu :file:`messages.html` i powiązany zostanie z adresem */messages*. Zaczynamy od zmian w :file:`views.py`.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # -*- coding: utf 8 -*-

    # chatter/chatter/views.py

    # dodajemy nowe importy
    from chatter.models import Message
    from django.utils import timezone
    from django.contrib.auth.decorators import login_required


    # pozostale widoki

    # dekorator, ktory "chroni" nasz widok przed dostepem przez osoby niezalogowane, jezeli uzytkownik niezalogowany
    # bedzie probowal odwiedzic ten widok, to zostanie przekierowany na strone logowania
    @login_required(login_url='/login')
    def messages(request):
        """Widok wiadomosci."""
        error = None

        # zadanie POST oznacza, ze ktos probuje dodac nowa wiadomosc w systemie
        if request.method == 'POST':
            text = request.POST.get('text', '') # pobieramy tresc przeslanej wiadomosci
            # sprawdzamy, czy nie jest ona dluzsza od 250 znakow:
            # – jezeli jest dluzsza, to zwracamy blad, jezeli jest krotsza lub rowna, to zapisujemy ja w systemie
            if not 0 < len(text) <= 250:
                error = u'Wiadomość nie może być pusta i musi mieć co najwyżej 250 znaków'
            else:
                # ustawiamy dane dla modelu Message
                msg = Message(text=text, pub_date=timezone.now(), user=request.user)
                msg.save() # zapisujemy nowa widomosc
                return redirect(reverse('messages')) # przekierowujemy na strone wiadomosci

        user = request.user # informacje o aktualnie zalogowanym uzytkowniku
        messages = Message.objects.all() # pobieramy wszystkie wiadomosci
        # ustawiamy zmienne przekazywane do szablonu
        context = {'user': user, 'messages': messages, 'error': error}
        # renderujemy templatke wiadomosci
        return render(request, 'chatter/messages.html', context)

Teraz tworzymy nową templatkę messages.html w katalogu :file:`templates/chatter/`.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: messages_z1.html
    :linenos:

Uzupełniamy szablon widoku głównego, aby zalogowanym użytkownikom wyświetlał się link prowadzący do strony z wiadomościami. W pliku index.html po klauzuli ``{% else %}``, poniżej znacznika ``<h1>`` wstawiamy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: html

    <p><a href="{% url 'messages' %}">Zobacz wiadomości</a></p>

Na koniec dodajemy nową regułę do :file:`urls.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: html

    url(r'^messages/$', views.messages, name='messages'),

Jeżeli uruchomimy serwer deweloperski, zalogujemy się do aplikacji i odwiedzimy adres *127.0.0.1:8080/messages/*, zobaczymy listę wiadomości dodanych przez użytkowników [#]_.

.. [#] Jeżeli w panelu administracyjnym nie dodałeś żadnej wiadomości, lista będzie pusta.

JAK TO DZIAŁA: W widoku ``messages()``, podobnie jak w widoku ``login()``, mamy dwie ścieżki postępowania, w zależności od użytej metody HTTP. GET pobiera wszystkie wiadomości (``messages = Message.objects.all()``), przekazuje je do szablonu i renderuje. Django konstruuje odpowiednie zapytanie i mapuje dane z bazy na obiekty klasy Message (mapowanie obiektowo-relacyjne (ORM)).

POST zawiera z kolei treść nowej wiadomości, której długość sprawdzamy i jeżeli wszystko jest w porządku, tworzymy nową wiadomość (instancję klasy *Message*, czyli obiekt ``msg``) i zapisujemy ją w bazie danych (wywołujemy metodę obiektu: ``msg.save()``).

Rejestrowanie użytkowników
---------------------------------------

Utworzymy nowy widok ``my_register()``, szablon :file:`register.html` i nowy adres URL */register*, który skieruje użytkownika do formularza rejestracji, wymagającego podania nazwy i hasła. Zaczynamy od dodania widoku w pliku :file:`views.py`.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    # chatter/chatter/views.py

    # pozostale widoki

    def my_register(request):
        """Rejestracja nowego uzytkownika."""
        form = forms.UserCreationForm() # ustawiamy formularz rejestracji

        # POST oznacza, ze ktos probuje utworzyc nowego uzytkownika
        if request.method == 'POST':
            # przypisujemy nadeslane dane do formularza tworzenia uzytkownika
            form = forms.UserCreationForm(request.POST)
            # sprawdzamy poprawnosc nadeslanych danych:
            # – jezeli wszystko jest wporzadku to tworzymy uzytkownika
            # – w przeciwnym razie zwracamy formularz wraz z informacja o bledach
            if form.is_valid():
                # zapamietujemy podana nazwe uzytkownika i haslo
                username = form.data['username']
                password = form.data['password1']
                # zapisujemy formularz tworzac nowego uzytkownika
                form.save()
                # uwierzytelniamy uzytkownika
                user = authenticate(username=username, password=password)
                login(request, user)
                # po udanej rejestracji, przekierowujemy go na strone glowna
                return redirect(reverse('index'))

        # ustawiamy zmienne przekazywane do szablonu
        context = {'form': form}
        # renderujemy templatke rejestracji
        return render(request, 'chatter/register.html', context)

Tworzymy nowy szablon :file:`register.html` w katalogu :file:`templates/chatter`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: register_z1.html
    :linenos:

W szablonie widoku głównego :file:`index.html` po linku "Zaloguj się" wstawiamy kolejny:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: html

    <p><a href="{% url 'register' %}">Zarejestruj się</a></p>

Na koniec uzupełniamy plik :file:`urls.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    url(r'^register/$', views.my_register, name='register'),

JAK TO DZIAŁA: Zasada działania jest taka sama jak w przypadku pozostałych widoków. Po wpisaniu adresu *127.0.0.1:8080/register/* otrzymujemy formularz rejestracji nowego użytkownika, który podobnie jak formularz logowania, jest wbudowany w Django, więc wystarczy przekazać go do szablonu. Po wypełnieniu i zatwierdzeniu formularza wysyłamy żądanie POST, widok ``my_register()`` odbiera przekazane dane (nazwę użytkownika, hasło i powtórzone hasło), sprawdza ich poprawność (poprawność i unikalność nazwy użytkownika oraz hasło) oraz tworzy i zapisuje nowego użytkownika. Po rejestracji użytkownik przekierowywany jest na stronę główną.

Wylogowywanie użytkowników
---------------------------------------

Django ma wbudowaną również funkcję wylogowującą. Utworzymy zatem nowy widok ``my_logut()`` i powiążemy go z adresem :file:`/logout`. Do pliku :file:`views.py` dodajemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    def my_logout(request):
        """Wylogowywanie uzytkownika z systemu"""
        logout(request)
        # przekierowujemy na strone glowna
        return redirect(reverse('index'))

POĆWICZ SAM
---------------------------------------
    Powiąż widok ``my_logut`` z adresem *logout/* dopisując regułę w odpowiednim pliku. Powiązanie nazwij "logout".
    Wylogowywanie nie wymaga osobnego szablonu, dodaj jednak link wylogowujący do 1) szablonu :file:`index.html` po linku "Zobacz wiadomości" oraz do 2) szablonu :file:`messages.html` po nagłówku ``<h1>``.

Pojęcia
^^^^^^^^^^^^^^^^^^^

.. glossary::

    Aplikacja
        program komputerowy.

    Framework
        zestaw komponentów i bibliotek wykorzystywany do budowy aplikacji.

    GET
        typ żądania HTTP, służący do pobierania zasobów z serwera WWW.

    HTML
        język znaczników wykorzystywany do formatowania dokumentów,
        zwłaszcza stron WWW.

    HTTP
        protokół przesyłania dokumentów WWW.
        
    Kontroler
        logika aplikacji, w Django zawarta w funkcji obsługującej widok.

    Logowanie
        proces autoryzacji i uwierzytelniania użytkownika w systemie.

    Model
        schematy i źródła danych aplikacji.

    ORM
        mapowanie obiektowo-relacyjne, oprogramowanie służące do przekształcania struktur bazy danych na obiekty klasy danego języka oprogramowania.

    POST
        typ żądania HTTP, służący do umieszczania zasobów na serwerze WWW.

    Serwer deweloperski
        serwer używany w czasie prac nad oprogramowaniem.

    Serwer WWW
        serwer obsługujący protokół HTTP.

    Templatka
        szablon strony WWW wykorzystywany przez Django do renderowania widoków.

    URL
        ustandaryzowany format adresowania zasobów w internecie (przykład: http://pl.wikipedia.org/wiki/Uniform_Resource_Locator).

    Widok
        funkcja obsługująca żądania przychodzące na powiązany z nią adres, zazwyczaj zwraca użytkownikowi żądaną stronę html wyrenderowaną ze wskazanego szablonu.

Materiały
^^^^^^^^^^^^^^^^^^^

1. O Django http://pl.wikipedia.org/wiki/Django_(informatyka)
2. Strona projektu Django https://www.djangoproject.com/
3. Co to jest framework? http://pl.wikipedia.org/wiki/Framework
4. Co nieco o HTTP i żądaniach GET i POST http://pl.wikipedia.org/wiki/Http

Metryka
^^^^^^^

:Autorzy: Tomasz Nowacki,
          Robert Bednarz

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M

.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>


.. include:: ../copyright.rst
