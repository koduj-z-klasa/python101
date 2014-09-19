Przygotowanie katalogu projektu
===============================

Poszczególne zadania zakładają wykorzystanie wspólnego katalogu projektu
``python101`` znajdującego się w katalogu domowym użytkownika.

Pobieranie materiałów
---------------------

Materiały szkoleniowe zostały umieszczone w repozytorium GIT w serwisie GitHub
dzięki temu każdy może w łatwy sposób pobrać, zmieniać a także zsynchronizować
swoją lokalną kopię.

Wystarczy uruchomić komendę:

.. code-block:: bash

    $ git clone https://github.com/koduj-z-klasa/python101.git

Synchronizacja kodu pomiędzy krokami

.. note::

    Poniższe przykłady nie są wymagane w ramach przygotowania, ale warto
    się z nimi zapoznać w przypadku gdybyśmy chcieli skorzystać z możliwości
    jakie daje git.

Materiały zostały podzielone w repozytorium na kilka gałęzi (branch). Dzięki temu
na początku szkolenia mamy niewielki zbiór plików, natomiast w kolejnych krokach
szkolenia możemy aktualizować wersję roboczą o nowe treści.

Uczestnicy mogą spokojnie edytować i zmieniać materiały bez obaw
o późniejsze różnice względem reszty grupy. Możemy je szybko wyczyścić:

.. code-block:: bash

    $ git reset --hard

Lub skoczyć do następnego punktu kontrolnego i zsynchronizować kody źródłowe grupy
bez zachowania zmian poszczególnych uczestników:

.. code-block:: bash

    $ git checkout -f --track origin/pong/z1

Jeśli uczestnicy chą wcześniej zachować swoje modyfikacje mogą je zapisać
w swoim lokalnym repozytorium (wykonują tzw. commit).

Jeśli otrzymamy komunikat ``fatal: A branch named 'pong/z1' already exists.``
to znaczy, że ta komenda została już raz wykonana (został stworzony lokalny branch
``pong/z1``, wtedy możemy wykonać:

.. code-block:: bash

    $ git checkout -f pong/z1
