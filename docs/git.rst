Pobieranie materiałów i kody źródłowe
=====================================

Materiały szkoleniowe zostały umieszczone w repozytorium GIT w serwisie GitHub
dzięki temu każdy może w łatwy sposób pobrać, zmieniać a także zsynchronizować
swoją lokalną kopię.

Wystarczy uruchomić komendę:

.. code-block:: bash

    $ git clone https://github.com/koduj-z-klasa/python101.git

Spójność przykładów pomiędzy kolejnymi zadaniami
------------------------------------------------

Materiały zostały podzielone w repozytorium na kilka gałęzi (branch). Dzięki temu
na początku szkolenia mamy niewielki zbiór plików, natomiast w kolejnych krokach
szkolenia możemy aktualizować wersję roboczą o nowe treści.

Uczestnicy mogą spokojnie edytować i zmieniać materiały bez obaw
o późniejsze różnice względem reszty grupy. Możemy je szybko wyczyścić:

.. code-block:: bash

    $ git reset --hard

Lub skoczyć do następnego punktu kontrolnego bez zachowania zmian:

.. code-block:: bash

    $ git checkout --track origin/zadanie1b

Jeśli uczestnicy chą wcześniej zachować swoje modyfikacje mogą je zapisać
w swoim lokalnym repozytorium (wykonują tzw. commit).
