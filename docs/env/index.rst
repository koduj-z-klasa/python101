System i oprogramowanie
#######################

Nasze materiały zakładają wykorzystanie systemu :term:`Linux` i języka :term:`Python` w wersji 2.7.x,
który jest częścią wszystkich desktopowych dystrybucji. Oprócz interpretera języka
potrzebne są biblioteki wykorzystywane w bardziej zaawansowanych przykładach,
takich jak gry, aplikacje internetowe czy obsługa baz danych za pomocą systemów ORM.

Przygotowaliśmy również specjalną wersję systemu :ref:`Linux Live <linux-live>`
o nazwie *LxPup KzkBox* przeznaczoną do instalacji na kluczu USB.
Zawiera ona wszystkie potrzebne narzędzia i biblioteki, uruchamia się z napędu USB
na większości komputerów i zapamiętuje wyniki naszej pracy.

.. note::

    Do realizacji scenariuszy dostosować można praktycznie każdy system, w tym MS Windows.
    Na końcu tego dokumentu znajdziesz wskazówki, jak to zrobić.

Katalog użytkownika
*******************

Scenariusze zakładają również, że pracujemy w **katalogu domowym** użytkownika.
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

.. include:: ide.inc

.. include:: live.inc

.. include:: py3.inc

.. include:: gloss_env.inc
