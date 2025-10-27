.. _pyqt6:

Aplikacje okienkowe Qt
######################

`PyQt <https://pl.wikipedia.org/wiki/PyQt>`_ to zbiór bibliotek `Pythona <https://www.python.org/>`_
tworzonych przez `Riverbank Computing <https://riverbankcomputing.com/software/pyqt/intro>`_
umożliwiających szybkie projektowanie interfejsów aplikacji okienkowych opartych o międzyplatformowy
framework `Qt <https://pl.wikipedia.org/wiki/Qt>`_
(zob. również oficjalną stronę `Qt Company <http://www.qt.io/>`_)
dostępny w wersji `Open Source <https://pl.wikipedia.org/wiki/Otwarte_oprogramowanie>`_  na licencji `GNU LGPL <https://pl.wikipedia.org/wiki/GNU_Lesser_General_Public_License>`_ .
Działa w wielu systemach operacyjnych.

**Instalacja**

Bibliotekę instalujemy w :ref:`środowisku wirtualnym Pythona <venv>` za pomocą polecenia:

.. code-block:: bash

    ~$ (.venv) pip install pyqt6

.. toctree::
    :maxdepth: 2

    kalkulator/index
    widzety/index
    todopw/index

.. note::

    Aplikacje okienkowe w Pythonie można tworzyć z wykorzystaniem innych rozwiązań,
    takich jak:

        * `PySide6 <https://doc.qt.io/qtforpython-6/index.html>`_ – oficjalna implementacja biblioteki Qt6 dla Pythona;
        * `Tkinter <https://pl.wikipedia.org/wiki/Tkinter>`_ – wykorzystuje bibliotekę
          `Tk <https://pl.wikipedia.org/wiki/Tk>`_;
        * `PyGTK <https://pl.wikipedia.org/wiki/PyGTK>`_ – wykorzystuje bibliotekę
          `GTK+ <https://pl.wikipedia.org/wiki/GTK%2B>`_;
        * `wxPython <https://pl.wikipedia.org/wiki/WxPython>`_ – wykorzystuje bibliotekę
          `wxWidgets <https://pl.wikipedia.org/wiki/WxWidgets>`_;
        * `PySimpleGUI <https://www.pysimplegui.com/>`_ – biblioteka napisana od podstaw.
