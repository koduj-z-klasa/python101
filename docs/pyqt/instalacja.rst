.. _pyqt5ins:

Instalacja
############

W systemach opartych na Debianie ((X)Ubuntu, Linux Mint itp.)
i w systemach opartych na Arch Linuksie (Manjaro itp.):

.. code-block:: bash

    ~$ sudo apt-get install python3-pyqt5
    ~# pacman -S python-pyqt5

W systemach Windows ze strony `Python Releases for Windows <https://www.python.org/downloads/windows/>`_
pobieramy instalator Pythona 3 w 32- lub 64-bitowej wersji i instalujemy.
Następnie pobieramy ze strony `PyQt5 Download <https://riverbankcomputing.com/software/pyqt/download5>`_
instalator PyQt5 w wersji 32- lub 64-bitowej i również instalujemy.

PyQt5 vs PyQt4
**************

Wszystkie przykłady aplikacji z naszych scenariuszy można kodować
i uruchamiać za pomocą bibliotek Qt4, PyQt4 i Pythona 2.
Zmiany w kodzie są niewielkie i dotyczą kodowania napisów, obiektów *QString* oraz importów.
Tak więc:

* w importach ``PyQt5.QtWidgets`` zamieniamy na ``PyQt4.QtGui``;
* na początku każdego pliku źródłowego dodajemy import ``from __future__ import unicode_literals`` –
  dzięki temu napisów w unikodzie nie musimy poprzedzać symbolem ``u``;
* tekst zwracany przez obiekty Qt4 jako typ *QString* konwertujemy w razie potrzeby na napisy
  Pythona za pomocą funkcji ``str()``.

Dokładne informacje nt. różnic pomiędzy kolejnymi wersjami bibblioteki PyQt
dostępne są na stronie `Differences Between PyQt4 and PyQt5 <http://pyqt.sourceforge.net/Docs/PyQt5/pyqt4_differences.html>`_.