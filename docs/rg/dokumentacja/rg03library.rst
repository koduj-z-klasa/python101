Biblioteka rg
##############

*Gra robotów* udostępnia bibliotekę ułatwiającą programowanie. Zawarta jest
w module ``rg``, który importujemy na początku pliku instrukcją ``import rg``.

.. attention::

    Położenie robota (``loc``) reprezentowane jest przez tuplę (x, y).

.. raw:: html

    <hr />

**rg.dist(loc1, loc2)**
*******************************

Zwraca matematyczną odległość między dwoma położeniami.

.. raw:: html

    <hr />

**rg.wdist(loc1, loc2)**
********************************

Zwraca różnicę w ruchach między dwoma położeniami. Ponieważ robot nie może
poruszać się na ukos, jest to suma ``dx + dy``.

.. raw:: html

    <hr />

**rg.loc_types(loc)**
*******************************

Zwraca listę typów położeń wskazywanych przez ``loc``. Możliwe wartości to:

* ``invalid`` – poza granicami planszy(np. (-1, -5) lub (23, 66));
* ``normal`` – w ramach planszy;
* ``spawn`` – punkt wejścia robotów;
* ``obstacle`` – pola, na które nie można się ruszyć (szare kwadraty).

Metoda nie ma dostępu do kontekstu gry, np. wartość ``obstacle`` nie oznacza,
że na sprawdzanym kwadracie nie ma wrogiego robota; wiemy tylko, że dany
kwadrat jest przeszkodą na mapie.

Zwrócona lista może zawierać kombinacje wartości typu: ``['normal', 'obstacle']``.

.. raw:: html

    <hr />

**rg.locs_around(loc, filter_out=None)**
*************************************************

Zwraca listę położeń sąsiadujących z ``loc``. Jako drugi argument
``filter_out`` można podać listę typów położeń do wyeliminowania.
Dla przykładu: ``rg.locs_around(self.location, filter_out=('invalid', 'obstacle'))``
– poda listę kwadratów, na które można wejść.

.. raw:: html

    <hr />

**rg.toward(current_loc, dest_loc)**
********************************************

Zwraca następne położenie na drodze z bieżącego miejsca do podanego.
Np. poniższy kod:

.. code-block:: python

    import rg

    class Robot:
        def act(self, game):
            if self.location == rg.CENTER_POINT:
                return ['suicide']
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

– skieruje robota do środka planszy, gdzie popełni on samobójstwo.

.. raw:: html

    <hr />

**rg.CENTER_POINT**
*****************************

Stała (ang. *constant*) definiująca położenie środkowego punktu planszy.

.. raw:: html

    <hr />

**rg.settings**
*****************************

Specjalny typ słownika (AttrDict) zawierający ustawienia gry.

* ``rg.settings.spawn_every`` – ilość rozegranych rund od wejścia robota do gry;
* ``rg.settings.spawn_per_player`` - ilość robotów wprowadzonych przez gracza;
* ``rg.settings.robot_hp`` – domyślna ilość punktów HP robota;
* ``rg.settings.attack_range`` – tupla (minimum, maksimum) przechowująca
  zakres uszkodzeń wyrządzonych przez atak;
* ``rg.settings.collision_damage`` – uszkodzenia wyrządzone przez kolizję;
* ``rg.settings.suicide_damage`` – uszkodzenia wyrządzone przez samobójstwo;
* ``rg.settings.max_turns`` – liczba rund w grze.

.. raw:: html

    <hr />

Czy w danym położeniu jest robot
*********************************

Ponieważ struktura ``game.robots`` jest słownikiem robotów, w którym kluczami
są położenia, a wartościami roboty, można użyć testu ``(x, y) in game.robots``,
który zwróci ``True``, jeśli w danym położeniu jest robot, lub ``Flase``
w przeciwnym razie.

.. note::

    Niniejsza dokumentacja jest nieautoryzowanym tłumaczeniem oficjalnej dokumentacji
    dostępnej na stonie `RobotGame <https://robotgame.net>`_.
