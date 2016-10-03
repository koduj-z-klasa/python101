Minecraft Pi
#############

`Minecraft Pi Edition <http://pi.minecraft.net/>`_ to zbiór bibliotek `Pythona <https://www.python.org/>`_
umożliwiających kontrolowanie niektórych elementów gry `Minecraft <https://pl.wikipedia.org/wiki/Minecraft>`_ uruchamianej jako serwer na minikomputerze `Raspberry Pi <https://pl.wikipedia.org/wiki/Raspberry_Pi>`_
z systemem `Raspbian <https://www.raspbian.org/>`_. Całość bardzo dobrze nadaje się do nauki programowania
z wykorzystaniem języka Python.

**Wymagania wstępne**

1. Serwer Minecrafta Pi, czyli minikomputer Raspberry Pi w wersji B+, 2 lub 3
   z najnowszą wersją systemu Raspbian
2. Klient, czyli dowolny komputer z systemem Linux [lub Windows?],
   zawierający interpreter Pythona 2 oraz bibliotekę *mcpi-sim*
3. Adresy IP serwera i klienta muszą należeć do tej samej sieci lokalnej

**Instalacja bibliotek**

Biblioteki *mcpi-sim*, czyli symulatora Minecrafta, instalujemy poleceniem:

.. code-block:: bash

    ~$ git clone https://github.com/pddring/mcpi-sim.git

**Symulator zawiera biblioteki ``mcpi``** w katalogu :file:`~/mcpi-sim/mcpi`.
*Mcpi* to pythonowe :term:`API` pozwalające na komunikację z serwerem Minecraft Pi.
Do działania symulatora potrzebna jest biblioteka *PyGame*. Zobacz, jak ją zainstalować
w systemie :ref:`Linux <linux-pakiety>` lub :ref:`Windows <pygame-win>`.

.. note::

	* Dystrybucja XenialPup KzkBox przygotowana na potrzeby naszego projektu zawiera już symulator.

	* Do zainstalowania tylko bibliotek *mcpi* użyć można polecenia:
	  ``git clone https://github.com/martinohanlon/mcpi.git``. Można też ściągnąć
	  i rozpakować archiwum `master.zip <https://github.com/martinohanlon/mcpi/archive/master.zip>`_.

.. toctree::
    :maxdepth: 2

    podstawy/index
    figury/index
    turtle/index
    rgame/index
    gloss_mcpi

**Materiały**

1. Minecraft `Pi Edition <http://minecraft.gamepedia.com/Pi_Edition>`_
2. Dokumentacja `Minecraft API <http://www.stuffaboutcode.com/p/minecraft-api-reference.html>`_
