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

Kod źródłowy
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
