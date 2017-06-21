.. _pyqt5:

Aplikacje okienkowe Qt5
###########################

`PyQt <https://pl.wikipedia.org/wiki/PyQt>`_ to zbiór bibliotek `Pythona <https://www.python.org/>`_
tworzonych przez `Riverbank Computing <https://riverbankcomputing.com/software/pyqt/intro>`_
umożliwiających szybkie projektowanie interfejsów aplikacji okienkowych opartych o międzyplatformowy
framework `Qt <https://pl.wikipedia.org/wiki/Qt>`_
(zob. również oficjalną stronę `Qt Company <http://www.qt.io/>`_)
dostępny w wersji `Open Source <https://pl.wikipedia.org/wiki/Otwarte_oprogramowanie>`_  na licencji `GNU LGPL <https://pl.wikipedia.org/wiki/GNU_Lesser_General_Public_License>`_ .
Działa na wielu platformach i systemach operacyjnych.

Nasze scenariusze przygotowane zostały z wykorzystaniem Pythona 3 i bilioteki PyQt5.

**Instalacja**

W systemach Linux opartych na Debianie ((X)Ubuntu, Linux Mint itp.) lub na Arch Linuksie (Manjaro itp.):

.. code-block:: bash

    ~$ sudo apt-get install python3-pyqt5 python3-sip
    ~# pacman -S python-pyqt5 python-sip

W środowisku Windows 64-bitowym(!) (w systemach Linux również) najnowszą wersję zainstalujemy
zgodnie z `instrukcjami Riverbank <https://www.riverbankcomputing.com/software/pyqt/download5>`_
za pomocą menedżera pakietów:

.. code-block:: bash

    ~$ pip3 install PyQt5 SIP


.. toctree::
    :maxdepth: 2

    kalkulator/index
    widzety/index
    todopw/index
    gloss_pyqt


.. note::

	Aplikacje okienkowe w Pythonie można tworzyć z wykorzystaniem innych rozwiązań,
	takich jak:

		* `Tkinter <https://pl.wikipedia.org/wiki/Tkinter>`_ – wykorzystuje bibliotekę
		  `Tk <https://pl.wikipedia.org/wiki/Tk>`_;
		* `PyGTK <https://pl.wikipedia.org/wiki/PyGTK>`_ – wykorzytuje bibliotekę
		  `GTK+ <https://pl.wikipedia.org/wiki/GTK%2B>`_;
		* `wxPython <https://pl.wikipedia.org/wiki/WxPython>`_ – wykorzystuje bibliotekę
		  `wxWidgets <https://pl.wikipedia.org/wiki/WxWidgets>`_;
		* `PySide <https://srinikom.github.io/pyside-docs/>`_ – wykorzystuje bibliotekę Qt4, alternatywa dla PyQt4.
