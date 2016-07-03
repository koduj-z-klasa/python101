.. _pyqt5ins:

Instalacja
############

W systemach opartych na Debianie ((X)Ubuntu, Linux Mint itp.)
i w systemach opartych na Arch Linuksie (Manjaro itp.):

.. code-block:: bash

    ~$ sudo apt-get install python3-pyqt5
    ~# pacman -S python-pyqt5

.. tip::

	Powyższe polecenia zainstalują bibliotekę PyQt5 dla Pythona 3.
	Jeżeli chcemy wersji dla Pythona 2, użyjemy pakietów: ``python-pyqt5``,
	a w Archu ``python2-pyqt5``.

W systemach Windows ze strony `Python Releases for Windows <https://www.python.org/downloads/windows/>`_
pobieramy instalator Pythona 3 w 32- lub 64-bitowej wersji i instalujemy.
Następnie pobieramy ze strony `PyQt5 Download <https://riverbankcomputing.com/software/pyqt/download5>`_
instalator PyQt5 w wersji 32- lub 64-bitowej i również instalujemy.
Autorzy PyQt5 na stronach Riverbank nie udostępniają wersji dla Pythona 2.

PyQt5 + Python2
****************

Przykłady w scenariuszach napisane są dla PyQt5+Pythona3, ale jeżeli zainstalowaliśmy
PyQt5+Python2, żeby zadziałały wystarczy:
* w pierwszej linii zmienić ``python3`` na ``python`` lub ``python2``;
* wywołanie ``super().__init__(parent)`` zmienić na ``super(nazwa_klasy, self).__init__(parent)``;
* na początku każdego pliku źródłowego dodać import ``from __future__ import unicode_literals``.

PyQt5 vs PyQt4
**************

Wszystkie przykłady aplikacji z naszych scenariuszy można kodować
i uruchamiać za pomocą bibliotek Qt4, PyQt4 i Pythona 2.
Zmiany w kodzie są niewielkie i dotyczą kodowania napisów, obiektów *QVariant* oraz importów.
Tak więc:

* w pierwszej linii zmienimy ``python3`` na ``python`` lub ``python2``;
* w importach ``PyQt5.QtWidgets`` zamieniamy na ``PyQt4.QtGui``;
* na początku każdego pliku źródłowego dodajemy import ``from __future__ import unicode_literals`` –
  dzięki temu napisów w unikodzie nie musimy poprzedzać symbolem ``u``;
* wartości zwracane przez obiekty Qt4 jako typ *QVariant* konwertujemy w razie potrzeby na odpowiednie
  typy. Napisy uzyskujemy za pomocą funkcji ``str()`` lub metody ``toString()`` obiektu ``QVariant``.
  Wartość logiczną otrzymamy wywołując metodę ``toBool()`` obiektu ``QVariant``.

Dokładne informacje nt. różnic pomiędzy kolejnymi wersjami bibblioteki PyQt
dostępne są na stronie `Differences Between PyQt4 and PyQt5 <http://pyqt.sourceforge.net/Docs/PyQt5/pyqt4_differences.html>`_.