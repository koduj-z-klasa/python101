.. Python 101 documentation master file, created by
   sphinx-quickstart on Tue Sep 16 15:47:34 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Szkolenie Python 101
====================

Niniejsze materiały to dokumentacja do szkolenia z języka Python realizowanego
w ramach projektu `Koduj z Klasą`_ prowadzonego przez
Fundację `Centrum Edukacji Obywatelskiej`_.

Krótki link do tej strony: `bit.ly/kzk-py <http://bit.ly/kzk-py>`_


Pobieranie tej dokumentacji
---------------------------

Materiały można `pobrać do czytania w wersji offline
<http://koduj-z-klasa.github.io/python101/python-101-html.zip>`_.
Poniższa komendy pobiorą dokumentację i rozpakują pliki na pulpicie
w folderze ``~/Pulpit/python-101-html``:

.. code-block:: bash

    wget -O python-101-html.zip http://koduj-z-klasa.github.io/python101/python-101-html.zip
    unzip python-101-html.zip -d ~/Pulpit/

Te materiały można także pobrać i zmodyfikować i `przygotować według instrukcji w repozytorium`_

.. _Koduj z Klasą: http://www.ceo.org.pl/koduj
.. _Centrum Edukacji Obywatelskiej: http://www.ceo.org.pl/
.. _przygotować według instrukcji w repozytorium: https://github.com/koduj-z-klasa/python101


Przygotowanie do szkolenia
--------------------------

Przed szkoleniem warto przygotować sprawdzić i przygotować swój komputer.

..  toctree::
    :maxdepth: 1

    env
    git

Zaczynamy!
----------

.. toctree::
    :maxdepth: 2
    :numbered:

    basic/basic
    pong/index
    life/index
    tic-tac-toe/index
    quiz
    todo
    chatter



Indices and tables
~~~~~~~~~~~~~~~~~~

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. raw:: html

    <script>
      // dla http://koduj-z-klasa.github.io/python101/
      // w read the docs kod uzupełnia się w dashboardzie
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-55172998-1', 'auto');
      ga('send', 'pageview');
    </script>
