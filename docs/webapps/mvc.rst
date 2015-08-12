.. _mvc_wzorzec:

MVC
##############

W projektowaniu aplikacji internetowych odwołujemy się do wzorca M(odel)V(iew)C(ontroller),
czyli Model–Widok–Kontroler, co pozwala na oddzielenie danych od ich prezentacji oraz logiki aplikacji.
Funkcje kolejnych elementów są następujące:

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

**Widoki** – :term:`widok` w Django to funkcja lub klasa Pythona, która odpowiada
na żądania www, np. zwraca kod HTML generowany w szablonie (ang. *template*),
jakiś dokument, obrazek lub przekierowuje na inny adres.
Django zawiera wiele widoków wbudowanych. Widoki definiujemy w pliku :file:`views.py`.

Każda funkcja pełniąca rolę widoku jako pierwszy argument otrzymuje obiekt
``HttpRequest`` zawierający informacje o żądaniu, np. jego typ (GET lub POST)
czy nazwę użytkownika. Widok musi zwrócić obiekt typu ``HttpResponse``.

Dodawanie stron w Django polega na wykorzystywaniu widoków wbudowanych lub
tworzeniu nowych. Są to klasy lub funkcje Pythona wykonujące jakieś operacje
po stronie serwera w odpowiedzi na żądania klienta. Widoki powiązane są
z określonymi adresami url. Widoki najczęściej zwracają kod HTML
wyrenderowany na podstawie szablonów, do których możemy przekazywać dodatkowe dane,
np. z bazy.

Dane z bazy przekazywane są do szablonów za pomocą Pythonowego słownika.
Renderowanie polega na odszukaniu pliku szablonu, zastąpieniu przekazanych
zmiennych danymi i odesłaniu całości (HTML + dane) do użytkownika.

Szablony zapisywane są w podkatalogu ``templates/nazwa_aplikacji``.

.. _mvc_kontroler:

Kontroler
**********

**Kontroler** – :term:`kontroler` to mechanizm kierujący kolejne żądania
do odpowiednich widoków na podstawie wzorców adresów URL zawartych w pliku :file:`urls.py`.

Django
********

Twórcy Django traktują wzorzec MVC elastycznie, twierdząc że ich framework wykorzystuje
taczej wzorzec MTV, czyli model (Model), szablon (Template), widok (View).
Oznacza to, że powiązanie widoków z adresami URL oraz same widoki decydują o tym,
co zostanie zwrócone i pełnią w ten sposób rolę kontrolera.
Szablony natomiast decydują o tym, jak to zostanie zaprezentowane użytkownikowi,
a więc pełnią rolę widoków w sensie MVC.
