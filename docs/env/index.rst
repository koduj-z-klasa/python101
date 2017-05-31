System i oprogramowanie
#######################

Nasze materiały zakładają wykorzystanie języka :term:`Python` w wersji 3.x.
Mogą być realizowane w dowolnym systemie operacyjnym, jednak proponujemy systemy Linux,
w których Python jest domyślnie zainstalowany i łatwiej doinstalować
dodatkowe narzędzia i biblioteki.

Do realizacji materiałów przygotowaliśmy również specjalne wersje systemu
:ref:`Linux Live <linux-live>` przeznaczone do instalacji na pendrajwach.
Zawierają one wszystkie potrzebne narzędzia i biblioteki, uruchamiają się
z napędu USB na większości komputerów i zapamiętują wyniki naszej pracy.


Katalog użytkownika
*******************

Scenariusze zakładają, że pracujemy w **katalogu domowym** użytkownika.
W systemach Linux jest to podfolder katalogu ``/home`` o nazwie zalogowanego użytkownika,
np. ``/home/uczen``. W poleceniach wydawanych w terminalu (zob. :term:`terminal`)
ścieżkę do tego katalogu symbolizuje znak ``~``.

Skrócony zapis typu ``~/quiz2$`` oznacza, że dane polecenie należy wykonać w podkatalogu ``quiz2``
katalogu domowego użytkownika. Znak ``$`` oznacza, że komendy wydajemy
jako zwykły użytkownik, natomiast ``#`` – jako root, czyli administrator.

.. note::

    W przygotowanym przez nas systemie *LxPup KzkBox* wyjątkowo pracujemy jako użytkownik
    *root* w kalogu domowym :file:`/root`.


.. include:: linux.inc

.. include:: windows.inc

.. include:: interpreter.inc

.. include:: ide.inc

.. include:: live.inc

.. include:: gloss_env.inc
