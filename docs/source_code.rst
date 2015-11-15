Przygotowanie katalogu projektu
###############################

Poszczególne zadania zakładają wykorzystanie wspólnego katalogu projektu
``python101`` znajdującego się w katalogu domowym użytkownika.

Pobieranie materiałów
*********************

Materiały szkoleniowe zostały umieszczone w repozytorium **Git** w serwisie GitHub
dzięki temu każdy może w łatwy sposób pobrać, zmieniać, a także zsynchronizować
swoją lokalną kopię.

W katalogu domowym użytkownika uruchamiamy komendę:

.. code-block:: bash

    ~$ git clone --recursive https://github.com/koduj-z-klasa/python101.git

W efekcie otrzymamy katalog ``python101`` z kodami źródłowymi materiałów.

Znak zachęty i miejsce uruchomienia 
***********************************

Przykłady zawierające znak zachęty ``$`` oznaczają komendy
do wykonania w terminalu systemu operacyjnego (w Linux uruchom przez :kbd:`Win+T`).

Oprócz znaku zachęty ``$`` przykłady mogą zawierać informację o
lokalizacji w jakiej należy wykonać komendę. Np. ``~/python101$`` oznacza
że komendę wykonujemy w folderze ``python101`` w katalogu domowym
użytkownika, czyli ``/home/sru/python101`` w środowisku linux (dla windows nie mamy domyśnej lokalizacji).

Komendy należy kopiować i wklejać bez znaku zachęty ``$`` i poprzedzającego tekstu.
Komendy można wklejać do terminala w systemie linux środkowym klawiszem myszki.


Korzystanie z kodu źródłowego
*****************************

W materiałach będą pojawiać się przykłady kodu źródłowego jak ten poniżej.
Te przykłady pokazują jak nasz kod może się rozwijać.

By wspierać uczenie się na błędach i zwracanie uwagi na niuanse składni
języka programowania, warto by część przykładów uczestnicy próbowali odtworzyć
samodzielnie.

Jednak dla większego tempa i w przypadku jasnych przykładów
warto je zwyczajnie kopiować, omawiać ich działanie i ewentualnie modyfikować
w ramach eksperymentów.

Niektóre przykłady starają się zachować numerację linii zgodną z oczekiwanym rezultatem.
Przykładowo kod poniżej powinien zostać wklejony w linii ``51`` omawianego pliku.

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


Podczas przepisywania kodu można pominąć kawałki dokumentujące kod,
to znaczy tzw. *komentarze*. Komentarzem są teksty zaczynające się od
znaku ``#`` oraz teksty zamknięte pomiędzy potrójnymi cudzysłowami ``"""``.

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
