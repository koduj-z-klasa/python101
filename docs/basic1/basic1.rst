Mów mi Python – wprowadzenie do języka
**************************************

Jestem Python
================

Python jest dynamicznie typowanym językiem interpretowanym wysokiego poziomu. Cechuje się czytelnością i zwięzłością kodu. Stworzony został w latach 90. przez Guido van Rossuma, nazwa zaś pochodzi od tytułu serialu komediowego emitowanego w BBC pt. "Latający cyrk Monty Pythona".

W systemach opartych na Linuksie interpreter Pythona jest standardowo zainstalowany, ponieważ duża część oprogramowania na nim bazuje. W systemach Microsoft Windows Pythona należy doinstalować. Funkcjonalność Pythona może być dowolnie rozszerzana dzięki licznym bibliotekom pozwalającym tworzyć aplikacje okienkowe (PyQt, PyGTK, wxPython), internetowe (Flask, Django) czy multimedialne i gry (Pygame). Istnieją również kompleksowe projekty oparte na Pythonie wspomagające naukową analizę, obliczenia i przetwarzanie danych (Anaconda, Canopy).

Kodować można w dowolnym edytorze tekstowym, jednak ze względów praktycznych warto korzystać z programów ułatwiających pisanie kodu. Polecić można np. lekkie, szybkie i obsługujące wiele języków środowisko Geany, a także profesjonalne rozwiązanie, jakim jest aplikacja PyCharm. Obydwa programy działają na platformie Linux i Windows.

Zanim przystąpimy do pracy w katalogu domowym utworzymy podkatalog python, w którym będziemy zapisywali nasze skrypty:

.. raw:: html

    <div class="code_no">Terminal nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code:: bash

    ~ $ mkdir python

Poznawanie Pythona zrealizujemy poprzez rozwiązywanie prostych zadań, które pozwolą zaprezentować elastyczność i łatwość tego języka. Nazwy kolejnych skryptów umieszczone są jako komentarz zawsze w czwartej linii kodu. Pliki zawierające skrypty Pythona mają zazwyczaj rozszerzenie .py. Bardzo przydatnym narzędziem podczas kodowania w Pythonie jest konsola interpretera, którą uruchomimy wydając w terminalu polecenie python lub ipython [1]_. Można w niej testować i debugować wszystkie wyrażenia, warunki, polecenia itd., z których korzystamy w skryptach.

.. [1] Ipython to rozszerzona konsola Pythona przeznaczona do wszelkiego rodzaju interaktywnych obliczeń.
