.. _rgkit:

Testowanie robotów
###################

Pakiet **rgkit**
******************

Do budowania i testowania robotów używamy pakietu *rgkit*. W tym celu przygotowujemy
środowisko deweloperskie, zawierające bibliotekę ``rg``:

.. code-block:: bash

    ~$ mkdir robot; cd robot
    ~robot/$ virtualenv env
    ~robot/$ source env/bin/activate
    (env):~robot$ pip install rgkit

Po wykonaniu powyższych poleceń i zapisaniu implementacji klasy ``Robot``
np. w pliku :file:`~/robot/robot01.py` możemy uruchamiać grę przeciwko
samemu sobie:

.. code-block:: bash

    (env)~/robot$ rgrun robot01.py robot01.py

Jeżeli utworzymy inne implementacje robotów, np. w pliku :file:`~/robot/robot02.py`
skonfrontujemy je poleceniem:

.. code-block:: bash

    (env)~/robot$ rgrun robot01.py robot02.py

Przydatne opcje polecenia ``rgrun``:

* ``-H`` – symulacja bez UI
* ``-r`` – roboty wprowadzane losowo zamiast symetrycznie.

.. attention::

    Pokazana powyżej instalacja zakłada użycie środowiska wirtualnego tworzonego
    przez pakiet *virtualenv*, dlatego przed uruchomieniem symulacji,
    a także przed użyciem omówionego niżej pakietu *robotgame-bots* trzeba
    pamiętać o wydaniu w katalogu :file:`robot` polecenia:

.. code-block:: bash

    ~/robot$ source env/bin/activate

Roboty open-source
*******************

Swoje roboty warto wystawić do gry przeciwko przykładowym robotom
dostarczanym przez projekt `robotgame-bots <https://github.com/mpeterv/robotgame-bots>`_:
Instalacja sprowadza się do wykonania polecenia w utworzonym wcześniej katalogu :file:`robot`:

.. code-block:: bash

    ~/robot$ git clone https://github.com/mpeterv/robotgame-bots bots

Wynikiem polecenia będzie utworzenia podkatalogu :file:`~/robot/bots` zawierającego
kod przykładowych robotów.

Listę dostępnych robotów najłatwiej użyskać wydając polecenie:

.. code-block:: bash

    (env)~/robot$ ls bots

Aby zmierzyć się z wybranym robotem – na początek sugerujemy *stupid26.py* –
wydajemy polecenie:

.. code-block:: bash

    (env)~/robot$ rgrun mojrobot.py bots/stupid26.py

Od czasu do czasu można zaktualizować dostępne roboty poleceniem:

.. code-block:: bash

    ~/robot/bots$ git pull --rebase origin master

Symulator rg
*************

Bardzo przydatny jest symulator zachowania robotów. Instalacja
w katalogu :file:`robot`:

.. code-block:: bash

    ~/robot$ git clone https://github.com/mpeterv/rgsimulator.git

Następnie uruchamiamy symulator podając jako parametr nazwę przynajmniej
jednego robota (można dwóch):

.. code-block:: bash

    (env)~/robot$ rgsimulator/rgsimulator.py robot01.py [robot02.py]

Symulatorem sterujemy za pomocą klawiszy:

* Klawisze kursora lub WASD do zaznaczania pól.
* Klawisz F: utworzenie robota-przyjaciela w zaznaczonym polu.
* Klawisz E: utworzenie robota-wroga w zaznaczonym polu.
* Klawisze Delete or Backspace: usunięcie robota z zaznaczonego pola.
* Klawisz H: zmiana punktów HP robota.
* Klawisz T: zmiana rundy.
* Klawisz C: wyczyszczenie planszy gry.
* Klawisz Spacja: pokazuje planowane ruchy robotów.
* Klawisz Enter: uruchomienie rundy.
* Klawisz L: załadowanie meczu z robotgame.net. Należy podać tylko numer meczu.
* Klawisz K: załadowanie podanej rundy z załadowanego meczu. Also updates the simulator turn counter.
* Klawisz P: zamienia kod robotów gracza 1 z 2.
* Klawisz O: ponowne załadowanie kodu obydwu robotów.
* Klawisz N: zmienia działanie robota, wyznacza "następne działanie".
* Klawisz G: tworzy i usuwa roboty w punktach wejścia (ang. *spawn locations*), "generowanie robotów".

.. tip::

    W Linuksie warto utworzyć sobie przyjazny link do wywoływania symulatora.
    W katalogu :file:`robot` wydajemy polecenia:

.. code-block:: bash

    (env)~/robot$ ln -s rgsimulator/rgsimulator.py symuluj
    (env)~/robot$ symuluj robot01.py [robot02.py]

.. note::

    Niniejsza dokumentacja jest nieautoryzowanym tłumaczeniem oficjalnej dokumentacji
    dostępnej na stonie `RobotGame <https://robotgame.net>`_, a także `RobotGame – rgkit <https://github.com/RobotGame/rgkit>`_.
    Opis działania symulatora robotów przetłumaczono na podstawie strony
    projektu `Rgsimulator <https://github.com/mpeterv/rgsimulator>`_.
