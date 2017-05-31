Realizacja scenariuszy
######################

Katalog użytkownika
===================

Scenariusze zakładają, że pracujemy w **katalogu domowym** użytkownika.
W systemach Linux jest to podfolder katalogu ``/home`` o nazwie zalogowanego użytkownika,
np. ``/home/uczen``. W poleceniach wydawanych w terminalu (zob. :term:`terminal`)
ścieżkę do tego katalogu symbolizuje znak ``~``.

Skrócony zapis typu ``~/quiz2$`` oznacza, że dane polecenie należy wykonać w podkatalogu ``quiz2``
katalogu domowego użytkownika. Znak ``$`` oznacza, że komendy wydajemy
jako zwykły użytkownik, natomiast ``#`` – jako root, czyli administrator.

.. note::

    W przygotowanym przez nas systemie *LxPup KzkBox* wyjątkowo pracujemy jako użytkownik
    *root* w katalogu domowym :file:`/root`.

Kodu źródłowy
=============

W materiałach znajdziesz przykłady kodu źródłowego, które pokazują,
jak rozwija się program. Warto je wpisywać w wybranym edytorze samodzielnie,
aby nauczyć się składni języka i lepiej poznać środowisko programistyczne.

W przypadku braku czasu kod można zaznaczać, kopiować i wklejać, pamiętając
o zachowaniu wcięć. Podczas przepisywania można pominąć komentarze, czyli
teksty zaczynające się od znaku ``#`` lub zamknięte pomiędzy potrójnymi
cudzysłowami ``"""``.

Większość fragmentów kodu jest numerowana, ale jeśli Twój kod różni się nieznacznie
numeracją linii, nie musi to oznaczać błędu.

Dla przykładu kod poniżej powinien zostać wklejony w linii ``51`` omawianego pliku:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:
    :lineno-start: 51

    def run(self):
        """
        Główna pętla programu
        """
        while not self.handle_events():
            self.ball.move(self.board)
            self.board.draw(
                self.ball,
            )
            self.fps_clock.tick(30)


Wykorzystanie Git-a
=====================

Materiały szkoleniowe zostały umieszczone w repozytorium w serwisie GitHub
dzięki temu każdy może w łatwy sposób pobrać, zmieniać, a także zsynchronizować
swoją lokalną kopię.

W katalogu domowym użytkownika uruchamiamy komendę:

.. code-block:: bash

    ~$ git clone --recursive https://github.com/koduj-z-klasa/python101.git

W efekcie otrzymamy katalog ``python101`` z kodami źródłowymi materiałów.


Synchronizacja kodu
*******************

.. note::

    Poniższe instrukcje nie są wymagane w ramach przygotowania, ale warto
    się z nimi zapoznać w przypadku gdybyśmy chcieli skorzystać z możliwości
    pozbycia się lokalnych zmian wprowadzonych podczas ćwiczeń i przywrócenia
    stanu do punktu wyjścia.

Materiały zostały podzielone w repozytorium na części, które w kolejnych krokach
są rozbudowywane. Dzięki temu na początku szkolenia mamy niewielki zbiór plików,
natomiast w kolejnych krokach szkolenia możemy aktualizować wersję roboczą o nowe treści.

Uczestnicy mogą spokojnie edytować i zmieniać materiały bez obaw
o późniejsze różnice względem reszty grupy.

Zmiany możemy szybko wyczyścić i powrócić do stanu z początku ćwiczenia:

.. code-block:: bash

    $ git reset --hard

Możemy także skakać pomiędzy punktami kontrolnymi np. skoczyć do następnego
lub skoczyć do następnego punktu kontrolnego i zsynchronizować kody źródłowe grupy
bez zachowania zmian poszczególnych uczestników:

.. code-block:: bash

    $ git checkout -f pong/z1

Jeśli uczestnicy chcą wcześniej zachować swoje modyfikacje, mogą je zapisać
w swoim lokalnym repozytorium (wykonują tzw. commit).
