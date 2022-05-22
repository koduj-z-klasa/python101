Realizacja scenariuszy
######################

Katalog użytkownika
===================

Jeżeli w scenariuszu mowa o **katalogu domowym** użytkownika, w systemie Linux
należy przez to rozumieć podfolder katalogu ``/home`` o nazwie zalogowanego użytkownika,
np. ``/home/uczen``. W poleceniach wydawanych w terminalu (zob. :term:`terminal`)
ścieżkę do tego katalogu symbolizuje znak ``~``.

Zapis typu ``~/quiz2$`` oznacza więc, że dane polecenie należy wykonać w podkatalogu
``quiz2`` katalogu domowego użytkownika.

Znak ``$`` oznacza, że komendy wydajemy jako zwykły użytkownik,
natomiast ``#`` – jako root, czyli administrator.

.. note::

    W przygotowanym przez nas systemie *MX Linux Live* pracujesz jako użytkownik
    z loginem i hasłem *demo*.

W systemie Windows
==================

Jeżeli scenariusze będziemy wykonywać w MS Windows, musimy pamiętać o różnicach:

* Katalog domowy użytkownika w Windows nie nadaje się do przechowywania w nim
  kodów programów lub repozytoriów, najlepiej utworzyć jakiś katalog na partycji
  innej niż systemowa (oznaczana literą *C:*), np. :file:`D:\python` i w nim
  tworzyć foldery dla poszczególnych scenariuszy.
* Domyślnym terminalem jest program ``cmd``, czyli wiersz poleceń; jest on jednak
  ograniczony i niewygodny, warto używać konsoli PowerShell lub jeszcze lepiej
  konsoli instalowanych razem z Pythonem i klientem Git.
* W systemie Windows znaki ``/`` (slash) w ścieżkach zmieniamy na ``\`` (backslash).
* Zamieniamy również komendy systemu Linux na odpowiedniki wiersza poleceń Windows,
  np. ``mkdir`` na ``md``.
* Pamiętajmy, żeby skrypty zapisywać w plikach kodowanych jako UTF-8.


Kod źródłowy
=============

W materiałach znajdziesz przykłady kodu źródłowego, które pokazują,
jak rozwija się program. Warto je wpisywać w wybranym edytorze samodzielnie,
aby nauczyć się składni języka i lepiej poznać środowisko programistyczne.
Podczas przepisywania można pominąć komentarze, czyli
teksty zaczynające się od znaku ``#`` lub zamknięte pomiędzy potrójnymi
cudzysłowami ``"""``.

W przypadku braku czasu kod można zaznaczać, kopiować i wklejać, pamiętając
o zachowaniu wcięć.

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
