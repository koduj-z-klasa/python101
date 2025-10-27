.. _kalkulator-qt6:

Kalkulator
###########################

.. highlight:: python

Prosta 1-okienkowa aplikacja ilustrująca podstawy tworzenia interfejsu graficznego
i obsługi działań użytkownika za pomocą Pythona 3 i PyQt6.
Przykład wprowadza również podstawy `programowania obiektowego <https://pl.wikipedia.org/wiki/Programowanie_obiektowe>`_
(ang. Object Oriented Programing).

.. figure:: img/kalkulator05.png

Bibliotekę Pyqt6 instalujemy w :ref:`środowisku wirtualnym Pythona <venv>` za pomocą polecenia:

.. code-block:: bash

    (.venv) pip install pyqt6

Pokaż okno
***********

Zaczynamy od utworzenia pliku o nazwie :file:`kalkulator.py` i wstawiamy do niego poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator01.py
    :linenos:

Podstawą naszego programu będzie moduł ``PyQt6.QtWidgets``, z którego importujemy
klasy ``QApplication`` – obsługa aplikacji, i ``QWidget`` – podstawową klasę wszystkich elementów interfejsu graficznego.

Wygląd okna naszej aplikacji definiować będziemy za pomocą klasy ``Kalkulator``
dziedziczącej (zob. :term:`dziedziczenie`) właściwości i metody z klasy ``QWidget``.
Konstruktor naszej klasy na początku wywołuje :term:`konstruktor` klasy bazowej: ``super(self).__init__(parent)``.
Następnie wywołujemy metodę ``interfejs()``, w której tworzyć będziemy :term:`GUI` naszej aplikacji.
Ustawiamy właściwości okna aplikacji i jego zachowanie:

* ``self.resize(300, 100)`` – szerokość i wysokość okna;
* ``setWindowTitle("Prosty kalkulator")``) – tytuł okna;
* ``self.show()`` – wyświetlenie okna na ekranie.

.. note::

    Słowo ``self`` to konwencjonalna nazwa używana wtedy, kiedy odnosimy się do właściwości lub metod obiektu
    utworzonego jako instancja jakiejś klasy. Słowo to zawsze występuje jako pierwszy parametr metod definiowanych
    jako funkcje klasy. Zob. `What is self? <https://docs.python.org/3/faq/programming.html#what-is-self>`_

Instrukcja ``app = QApplication(sys.argv)`` – tworzy obiekt aplikacji.
Argument ``sys.argv`` wskazuje, że aplikacja może otrzymywać parametry z linii poleceń.
W instrukcji ``okno = Kalkulator()`` tworzymy okno aplikacji, czyli obiekt będący instancją klasy ``Kalkulator``.

Na koniec uruchamiamy **główną pętlę programu** (``app.exec()``), która rozpoczyna obsługę
zdarzeń (zob. :term:`główna pętla programu`). Zdarzenia (np. kliknięcia) generowane są przez
system lub użytkownika i przekazywane są do aplikacji, która może je obsługiwać.

Poprawne zakończenie aplikacji zapewniające zwrócenie informacji o jej stanie do systemu,
co zapewnia wywołanie ``sys.exit()``.

Przetestujmy kod. Program uruchamiamy poleceniem wydanym w terminalu z aktywnym środowiskiem wirtualnym
w katalogu ze skryptem:

.. code-block:: bash

    ~$ python3 kalkulator.py

.. figure:: img/kalkulator01.png

Etykiety
**********

Puste okno być może nie robi wrażenia, zobaczymy więc, jak tworzyć widżety (zob. :term:`widżet`).
Najprostszym przykładem będą etykiety.

Dodajemy wymagane importy i rozbudowujemy metodę ``interfejs()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator02.py
    :linenos:
    :lineno-start: 1
    :lines: 1-3

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator02.py
    :linenos:
    :lineno-start: 12
    :lines: 12-31

Dodawanie widżetów zaczynamy od utworzenia obiektów na podstawie odpowiedniej klasy,
w tym wypadku `QtLabel <http://doc.qt.io/qt-6/qlabel.html>`_. Do jej konstruktora
przekazujemy tekst, który ma się wyświetlać na etykiecie, np.: ``etykieta_1 = QLabel("Liczba 1:", self)``.
Opcjonalny drugi argument, omówione wyżej słowo ``self``, wskazuje obiekt rodzica, w tym przypadku okno,
w którym ją umieszczamy.

.. note::

    Tworzenie widżetów z argumentem ``self`` umożliwia dostęp do ich właściwości
    w zasięgu całej klasy, czyli w innych metodach.

Do rozmieszczania widżetów w oknie służą tzw. układy (ang. *layout*). Tworzymy więc
układ tabelaryczny: ``uklad_t = QGridLayout()`` – i dodajemy do niego obiekty (etykiety) za
pomocą metody ``addWidget()``. Jako argumenty podajemy nazwę obiektu oraz numer wiersza i kolumny
definiujących komórkę, w której znaleźć się ma obiekt. Numeracja wierszy i kolumn zaczyna się od zera.
Zdefiniowany układ przypisujemy do okna nadrzędnego: ``self.setLayout(uklad_t)``.

Na koniec używamy metody ``setGeometry()`` do określenia położenia okna aplikacji
(początek układu jest w lewym górnym rogu ekranu) i jego rozmiaru (szerokość, wysokość).
Dodajemy również ikonę pokazywaną w pasku tytułowym lub w miniaturze na pasku zadań:
``self.setWindowIcon(QIcon('kalkulator.png'))``.

.. note::

    Plik graficzny z ikoną musimy :download:`pobrać <kalkulator.png>` i umieścić w katalogu
    ze skryptem :file:`kalkulator.py`.

Przetestuj wprowadzone zmiany.

.. figure:: img/kalkulator02.png

Pola edycyjne i przyciski
**************************

Dodamy teraz pozostałe widżety tworzące graficzny interfejs naszej aplikacji,
czyli pola edycyjne (zob. `QLineEdit <http://doc.qt.io/qt-6/qlineedit.html>`_)
i przyciski (zob. `QPushButton <http://doc.qt.io/qt-6/qpushbutton.html>`_).
Jak zwykle zaczynamy od zaimportowania potrzebnych klas:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator03.py
    :linenos:
    :lineno-start: 4
    :lines: 4

Dodatkowa klasa ``QHBoxLayout`` umożliwi nam rozmieszczenie przycisków w układzie poziomym.

Następnie przed instrukcją ``self.setLayout(uklad_t)`` w metodzie ``interfejs()`` wstawiamy następujący kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator03.py
    :linenos:
    :lineno-start: 28
    :lines: 28 -57

Jak widać, dodawanie widżetów polega zazwyczaj na:

* **utworzeniu obiektu** na podstawie klasy opisującej potrzebny element interfejsu,
  np. ``liczba_1 = QLineEdit(self)`` lub ``prz_dodaj = QPushButton("&Dodaj", self)``;
* **ustawieniu właściwości** obiektu, np. ``self.wynik.readonly = True`` umożliwia tylko odczyt tekstu pola,
  ``self.wynik.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')`` – definiuje podpowiedź,
  która pojawia się po najechaniu kursorem na widżet;
* **przypisaniu obiektu do układu** – ponieważ mamy 4 przyciski działań, tworzymy układ horyzontalny
  (zob. `QHBoxLayout <http://doc.qt.io/qt-6/qhboxlayout.html>`_): ``uklad_h = QHBoxLayout()``,
  dodajemy do niego przyciski za pomocą metody ``addWidget()`` i dodajemy go do układu tabelarycznego:
  ``uklad_t.addLayout(uklad_h, 2, 0, 1, 3)``.
  Argumenty liczbowe w metodzie ``addLayout()`` oznaczają odpowiednio wiersz i kolumnę,
  tj. komórkę, do której wstawiamy obiekt, oraz liczbę wierszy i kolumn, które chcemy wykorzystać.

.. note::

    Znak ``&`` przed jakąś literą w opisie przycisków tworzy skrót klawiaturowy dostępny po naciśnięciu
    :kbd:`ALT + litera`.

Po uruchomieniu programu powinniśmy zobaczyć okno podobne do poniższego:

.. figure:: img/kalkulator03.png

Obsługa zdarzeń
***************

Mamy okno z polami edycyjnymi i przyciskami, ale kontrolki te na nic nie reagują.
Nauczymy się więc obsługiwać poszczególne zdarzenia.

Na początku skryptu importujemy klasę `QMessageBox <http://doc.qt.io/qt-6/qmessagebox.html>`_
pozwalającą tworzyć okna z komunikatami oraz przestrzeń nazw `Qt <http://doc.qt.io/qt-6/qt.html>`_
zawierającą różne stałe:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator03.py
    :linenos:
    :lineno-start: 5
    :lines: 5-6

Dalej w metodzie ``interfejs()`` po instrukcji ``self.setLayout(uklad_t)`` dopisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator03.py
    :linenos:
    :lineno-start: 60
    :lines: 60-65

Jednym ze zdarzeń jest kliknięcie przycisku (``clicked``), które wiążemy za pomocą metody
``conect()`` z metodami ``koniec()`` i ``dzialanie()``.
Metody te dodajemy na końcu klasy ``Kalkulator()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator03.py
    :linenos:
    :lineno-start: 73
    :lines: 73-102

Metoda ``koniec()`` wywołana po kliknięciu przycisku "Koniec" wywołuje metodę ``close()`` okna głównego,
co powoduje jego zamknięcie.

.. note::

    Omówiony fragment kodu ilustruje mechanizm zwany w bibliotece Qt :term:`sygnały i sloty` (ang. *signals & slots*).
    Zapewnia on komunikację między obiektami. Sygnał powstaje w momencie wystąpienia jakiegoś wydarzenia,
    np. kliknięcia. Slot może z kolei być wbudowaną w Qt funkcją lub Pythonowym wywołaniem (ang. *callable*),
    np. klasą lub metodą.

Działania
*********

Ze zdarzeniem kliknięcia przycisków działań powiązana została metoda ``działania()``.
Ponieważ jedna metoda ma obsłużyć cztery sygnały, musimy znać źródło sygnału (ang. *source*),
czyli nadawcę (ang. *sender*): ``nadawca = self.sender()``.

W bloku ``try:`` przekształcamy wprowadzone w polach tekstowych liczby na typ zmiennoprzecinkowy.
Operacja ta z powodu błędnych danych może zwrócić wyjątek, który przechwytujemy w klauzuli
``except ValueError`` i wyświetlamy ostrzeżenie: ``QMessageBox.warning()``.

Jeżeli dane są poprawne, w złożonej instrukcji warunkowej sprawdzamy nadawcę
(np. ``if nadawca.text() == "&Dodaj":``) i wykonujemy odpowiednie działanie.

Podczas dzielenia ponownie korzystamy z przechwytywania wyjątków, tym razem do obsługi
ewentualnego błędu dzielenia przez zero (``ZeroDivisionError``).

.. figure:: img/kalkulator06.png

Instrukcja ``round(liczba1 / liczba2, 9)`` zaokrągla wynik dzielenia do 9 miejsc po przecinku.

Na koniec zamieniamy uzyskany wynik na ciąg znaków i wypisujemy w polu tekstowym za pomocą
metody ``setText()``: ``self.wynikEdt.setText(str(wynik))``.

Sprawdź działanie programu.

.. figure:: img/kalkulator05.png

.. tip::

    Jeżeli po zaimplementowaniu działań, aplikacja po uruchomieniu nie aktywuje kursora
    w pierwszym polu edycyjnym, należy tuż przed ustawianiem właściwości okna głównego
    (``self.setGeometry()``) umieścić wywołanie ``self.liczba_1.setFocus()``,
    które ustawia focus na wybranym elemencie.

Zamykanie aplikacji
********************

Zamknięcie okna również jest rodzajem wydarzenia (`QCloseEvent <http://doc.qt.io/qt-6/qcloseevent.html>`_),
które można przechwycić. Np. po to, aby zapobiec utracie niezapisanych danych.
Do klasy ``Kalkulator()`` dopiszmy kolejna metodę:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator03.py
    :linenos:
    :lineno-start: 103
    :lines: 103-115

W nadpisanej metodzie `closeEvent() <http://doc.qt.io/qt-6/qwidget.html#closeEvent>`_
wyświetlamy użytkownikowi prośbę o potwierdzenie zamknięcia za pomocą okna dialogowego
utworzonego za pomocą klasy ``QMessageBox``.

.. figure:: img//kalkulator04.png

Używamy następujących metod:

* ``setWindowTitle()`` – do ustawienia tytuł okna,
* ``setText()`` – do podania komunikatu dla użytkownika, w tym przypadku pytania,
* ``setStandardButtons`` – do zdefiniowania dostępnych przycisków,
* ``setDefaultButton`` – do wskazania przycisku domyślnego.

Jeżeli użytkownik kliknie przycisk "Yes" (``if odp == QMessageBox.StandardButton.Yes.value:``),
zezwalamy na dalszą obsługę zdarzenia ``event.accept()``, w przeciwnym razie odrzucamy je ``event.ignore()``.

Naciśnięcie klawisza
********************

Może wygodnie byłoby zamykać aplikację naciśnięciem klawisza :kbd:`ESC`?
Dopiszmy jeszcze jedną metodę w klasie ``Kalkulator``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: kalkulator03.py
    :linenos:
    :lineno-start: 116
    :lines: 116-119

Podobnie jak w przypadku ``closeEvent()`` tworzymy własną wersję funkcji
`keyPressEvent <http://doc.qt.io/qt-6/qwidget.html#keyPressEvent>`_ obsługującej
naciśnięcia klawiszy `QKeyEvent <http://doc.qt.io/qt-6/qkeyevent.html>`_.
Sprawdzamy naciśnięty klawisz ``if e.key() == Qt.Key_Escape:`` i jeżeli jest to :kbd:`ESC`,
zamykamy okno.

Materiały
***************

1. Strona główna `dokumentacji Qt6 <http://doc.qt.io/qt-6/>`_
2. `Lista klas Qt6 <http://doc.qt.io/qt-6/classes.html>`_
3. `PyQt6 Reference Guide <http://pyqt.sourceforge.net/Docs/PyQt6/>`_
4. `Przykłady PyQt6 <https://github.com/baoboa/pyqt6/tree/master/examples>`_
5. `Signals and slots <http://doc.qt.io/qt-6/signalsandslots.html>`_
6. `Kody klawiszy <http://doc.qt.io/qt-6/qt.html#Key-enum>`_
