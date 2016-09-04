.. _pyqt5ins:

Instalacja
############

PyQt5 + Python2
****************

W systemach Linux opartych na Debianie ((X)Ubuntu, Linux Mint itp.) lub na Arch Linuksie (Manjaro itp.):

.. code-block:: bash

    ~$ sudo apt-get install python-pyqt5
    ~# pacman -S python2-pyqt5

Ponieważ Riverbank nie udostępnia pakietów binarnych PyQt5 dla Pythona 2 pod systemem Windows,
ze strony `Python Releases for Windows <https://www.python.org/downloads/windows/>`_
pobieramy instalator Pythona 3 w 32- lub 64-bitowej wersji i instalujemy.
Następnie postępujemy wg instrukcji ze strony `PyQt5 Download <https://riverbankcomputing.com/software/pyqt/download5>`_. Gdybyśmy jednak chcieli skorzystać z połączenia Python2 + PyQt5,
postępujemy wg instrukcji ze strony `PyQt5 for Windows via PyPI <https://github.com/pyqt/python-qt5>`_.

PyQt5 + Python3
****************

Przykłady w scenariuszach napisane są dla PyQt5+Pythona2, ale bez żadnych zmian działają również
w środowisku PyQt5+Python3. Kod można opcjonalnie dostosować do Pythona 3:

* w pierwszej linii zmienić ``python`` na ``python3``;
* wywołanie ``super(nazwa_klasy, self).__init__(parent)`` uprościć na ``super().__init__(parent)``;
* na początku każdego pliku źródłowego usunąć import ``from __future__ import unicode_literals``.

PyQt4 + Python2
****************

Wszystkie przykłady aplikacji z naszych scenariuszy można także kodować
i uruchamiać za pomocą starszych bibliotek Qt4, PyQt4 i Pythona 2.
Zmiany w kodzie są niewielkie i dotyczą napisów, obiektów *QVariant* oraz importów.
Tak więc:

* w importach ``PyQt5.QtWidgets`` zamieniamy na ``PyQt4.QtGui``;
* na początku każdego pliku źródłowego dodajemy import ``from __future__ import unicode_literals`` –
  dzięki temu napisów zawierających polskie znaki nie musimy poprzedzać symbolem ``u``;
* wartości zwracane przez obiekty Qt4 jako typ *QVariant* konwertujemy w razie potrzeby na odpowiednie
  typy. Napisy uzyskujemy za pomocą funkcji ``str()`` lub metody ``toString()`` obiektu ``QVariant``.
  Wartość logiczną otrzymamy wywołując metodę ``toBool()`` obiektu ``QVariant``.

Dokładne informacje nt. różnic pomiędzy kolejnymi wersjami bibblioteki PyQt
dostępne są na stronie `Differences Between PyQt4 and PyQt5 <http://pyqt.sourceforge.net/Docs/PyQt5/pyqt4_differences.html>`_.