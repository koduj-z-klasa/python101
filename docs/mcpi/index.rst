.. _mcpi-app:

Minecraft Pi
#############

`Minecraft Pi Edition <http://pi.minecraft.net/>`_ to specjalna wersja gry
`Minecraft <https://pl.wikipedia.org/wiki/Minecraft>`_ uruchamianej jako serwer
na minikomputerze `Raspberry Pi <https://pl.wikipedia.org/wiki/Raspberry_Pi>`_
z systemem `Raspbian <https://www.raspbian.org/>`_.
Wyjątkową cechą tej wersji jest możliwość kontrolowanie niektórych elementów gry za pomocą
`Minecraft API <http://www.stuffaboutcode.com/p/minecraft-api-reference.html>`_
zawartych w bibliotekach **mcpi** napisanych w języku `Python <https://www.python.org/>`_
i preinstalowanych w Raspbianie (w wersji dla Pythona 2 i 3).
Całość bardzo dobrze nadaje się do nauki programowania z wykorzystaniem języka Python.

**Wymagania wstępne**

1. Serwer Minecrafta Pi, czyli minikomputer Raspberry Pi w wersji B+, 2 lub 3
   z najnowszą wersją systemu Raspbian.
2. Klient, czyli dowolny komputer z systemem Linux lub Windows,
   zawierający interpreter Pythona 2, bibliotekę `mcpi <https://github.com/martinohanlon/mcpi>`_
   oraz symulator `mcpi-sim <https://github.com/pddring/mcpi-sim>`_.
3. Adresy IP serwera i klienta muszą należeć do tej samej sieci lokalnej.

**Instalacja bibliotek**

Wszystkie biblioteki oraz symulator umieściliśmy w archiwum :download:`mcpi-sim.zip <mcpi-sim.zip>`,
które należy pobrać i rozpakować w katalogu użytkownika. W kolejnych scenariuszach zakładamy,
że tworzone skrypty zapisujemy w katalogu ``~/mcpi-sim``.


.. note::

  * Do działania symulatora potrzebna jest biblioteka *PyGame*.
    Zobacz, jak ją zainstalować w systemie :ref:`Linux <linux-pakiety>` lub :ref:`Windows <pygame-win>`.
    Symulator działa tylko w Pythonie 2.
  * Dystrybucje :ref:`Linux Live <linux-live>` przygotowane na potrzeby naszego projektu
    zawierają już symulator.
  * Opisane poniżej scenariusze można realizować bezpośrednio na Raspberry Pi.
  * Symulator dostępny jest w repozytorium ``https://github.com/pddring/mcpi-sim.git``.
  * Biblioteki *mcpi* dostępne są w repozytorium ``https://github.com/martinohanlon/mcpi.git``.


.. toctree::
    :maxdepth: 2

    podstawy/index
    figury/index
    turtle/index
    funkcje/index
    algorytmy/index
    glife/index
    rgame/index
    gloss_mcpi

**Materiały**

1. Minecraft `Pi Edition <http://minecraft.gamepedia.com/Pi_Edition>`_
2. Dokumentacja `Minecraft API <http://www.stuffaboutcode.com/p/minecraft-api-reference.html>`_
3. `Getting started with Minecraft Pi <https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/>`_
