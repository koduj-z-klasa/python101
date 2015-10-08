Rozpoczynamy
##############

.. contents:: Spis treści
    :backlinks: none

Tworzenie robota
*****************

Podstawowa struktura klasy reprezentującej każdego robota jest następująca:

.. code-block:: python

    class Robot:

        def act(self, game):
            return [<some action>, <params>]

Na początku gry powstaje jedna instanacja klasy ``Robot``. Oznacza to,
że właściwości klasy oraz globalne zmienne modułu są współdzielone między
wywołaniami. W każdej rundzie system wywołuje metodę ``act`` tej instancji
dla każdego robota, aby określić jego działanie.
(Uwaga: na początku przeczytaj reguły.)

Metoda ``act`` musi zwrócić jedną z następujących odpowiedzi:

.. code-block:: python

    ['move', (x, y)]
    ['attack', (x, y)]
    ['guard']
    ['suicide']

Jeżeli metoda ``act`` zwróci wyjątek lub błędne polecenie, robot pozostaje
w obronie, ale jeżeli powtórzy się to zbyt wiele razy, gracz zostanie zmuszony
do kapitulacji. Szczegóły omówiono w dziale *Zabezbieczenia*.

Odczytywanie właściwości robota
********************************

Każdy robot, przy użyciu wskaźnika ``self``, udostępnia następujące
właściwości:

* ``location`` – położenie robota w formie tupli (x, y);
* ``hp`` – punkty zdrowia wyrażone liczbą całkowitą
* ``player_id`` – identyfikator gracza, do którego należy robot
  (czyli oznaczenie "drużyny")
* ``robot_id`` – unikalny identyfikator robota, ale tylko w obrębie
  "drużyny"

Dla przykładu: kod ``self.hp`` – zwróci aktualny stan zdrowia robota.

W każdej rundzie system wywołując metodę ``act`` udostępnia jej stan gry
w następującej strukturze ``game``:

.. code-block:: python

    {
        # słownik wszystkich robotów na polach wyznaczonych
        # przez {location: robot}
        'robots': {
            (x1, y1): {
                'location': (x1, y1),
                'hp': hp,
                'player_id': player_id,

                # jeżeli robot jest w twojej drużynie
                'robot_id': robot_id
            },

            # ...i pozostałe roboty
        },

        # ilość odbytych rund (wartość początkowa 0)
        'turn': turn
    }

Wszystkie roboty w strukturze ``game['robots']`` są instancjami specjalnego
słownika udostępniającego ich właściwości, co przyśpiesza kodowanie.
Tak więc następujące konstrukcje są tożsame:

.. code-block:: python

    game['robots'][location]['hp']
    game['robots'][location].hp
    game.robots[location].hp

Poniżej zwięzły przykład drukujący położenie wszystkich robotów z danej drużyny:

.. code-block:: python

    class Robot:
        def act(self, game):
            for loc, robot in game.robots.items():
                if robot.player_id == self.player_id:
                    print loc

Przykładowy robot
*****************

Poniżej mamy kod prostego robota, który można potraktować jako punkt wyjścia.
Robot, jeżeli znajdzie wokół siebie przeciwnka, atakuje go, w przeciwnym
razie przemieszcza się do środka planszy (``rg.CENTER_POINT``).

.. code-block:: python

    import rg

    class Robot:
        def act(self, game):
            # if we're in the center, stay put
            if self.location == rg.CENTER_POINT:
                return ['guard']

            # if there are enemies around, attack them
            for loc, bot in game.robots.iteritems():
                if bot.player_id != self.player_id:
                    if rg.dist(loc, self.location) <= 1:
                        return ['attack', loc]

            # move toward the center
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

Użyliśmy, jak widać modułu ``rg``, który zostanie omówiony dalej.

.. note::

    Podczas gry tworzona jest tylko jedna instancja robota, w której można
    zapisywać trwałe dane.

.. note::

    Niniejsza dokumentacja jest nieautoryzowanym tłumaczeniem oficjalnej dokumentacji
    dostępnej na stonie `RobotGame <https://robotgame.net>`_.
