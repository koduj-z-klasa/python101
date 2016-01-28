.. _todopw:

ToDO
###########################

.. highlight:: python

Realizacja prostej listy ToDo (lista zadań do zrobienia) jako aplikacji okienkowej,
z wykorzystaniem biblioteki Qt5 i wiązań Pythona PyQt5.
Aplikacja umożliwia dodawanie, usuwanie, edycję i oznaczanie jako wykonane zadań,
zapisywanych w bazie SQLite obsługiwanej za pomocą systemu ORM `Peewee <http://docs.peewee-orm.com/en/latest/>`_.

Przykład ilustruje również techniki .

Przykład wykorzystuje `programowanie obiektowe <https://pl.wikipedia.org/wiki/Programowanie_obiektowe>`_ (ang. *Object Oriented Programing*) i ilustruje technikę `programowania model/widok <http://doc.qt.io/qt-5/model-view-programming.html>`_ (ang. *Model/View Programming*).

.. attention::

    **Wymagane oprogramowanie**:

      * Python v. 3.x
      * PyQt v. => 5.2.1

    **Wymagana wiedza**:

    	* Znajomość Pythona w stopniu średnim.
    	* Znajomość podstaw projektowania interfejsu z wykorzystaniem biblioteki Qt
    	  (zob. scenariusze :ref:`Kalkulator <kalkulator>` i :ref:`Widżety <widzety>`).
        * Znajomość podstaw wykorzystania systemów ORM (zob. scenariusz :ref:`Systemy ORM <systemy_orm>`).

.. contents::
    :depth: 1
    :local:

Interfejs
**********

Budowanie aplikacji zaczniemy od przygotowania podstawowego interfejsu. W dowolnym edytorze
otwieramy pusty plik, wklejamy poniższą zawrtość i zapisujemy pod nazwą :file:`gui.py`.

.. raw:: html

    <div class="code_no">Plik <i>gui.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: gui_z0.py
    :linenos:

Centralnym elementem aplikacji będzie komponent `QTableView <http://doc.qt.io/qt-5/qtableview.html>`_,
który potrafi wyświetlać dane w formie tabeli na podstawie zdefiniowanego modelu.
Użyjemy go po to, aby oddzielić dane od sposobu ich prezentacji (zob. `Model/View programming <http://doc.qt.io/qt-5/model-view-programming.html>`_). Taka architektura przydaje się zwłaszcza wtedy,
kiedy aplikacja okienkowa stanowi przede wszystkim interfejs służący prezentacji
i ewentualnie edycji danych, przechowywanych niezależnie, np. w bazie.

Pod kontrolką widoku umieszczamy obok siebie dwa przyciski, za pomocą których będzie się można
zalogować do aplikacji i ją zakończyć.

Główne okno i obiekt aplikacji utworzymy w pliku :file:`todopw.py`, którego zawartość
na początku będzie następująca:

.. raw:: html

    <div class="code_no">Plik <i>todopw.py</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: todopw_z0.py
    :linenos:

Okno logowania
***************

Podłączamy bazę
*****************

Model danych
**************

Dodawanie zadań
***************

Edycja i widok danych
*********************

Zapisywanie zmian
******************


Materiały
***************

1. `Model/View Programming <http://doc.qt.io/qt-5/model-view-programming.html>`_
2. `Model/View Tutorial <http://doc.qt.io/qt-5/modelview.html>`_
3. `Presenting Data in a Table View <http://doc.qt.io/qt-5/sql-presenting.html>`_
4. `Layout Management <http://doc.qt.io/qt-5/layout.html>`_

**Źródła:**

* :download:` <>`