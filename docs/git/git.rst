Git - wersjonowanie kodów źródłowych
====================================

Pokażemy tutaj jak nauczyciele mogą wykorzystać profesjonalne i bezpłatne narzędzia do wersjonowania
kodów źródłowych i wszystkich innych plików.

System kontroli wersji śledzi wszystkie zmiany dokonywane na pliku (lub plikach)
i umożliwia przywołanie dowolnej wcześniejszej wersji.
Nauczyciele pracujący z plikami które zmieniają się z przykładu na przykład,
z ćwiczenia na ćwiczenie mogą np. skorzystać z systemu kontroli wersji do
synchronizacji przykładów na poszczególnych etapach swojej pracy.

.. figure:: http://git-scm.com/figures/18333fig0104-tn.png

Dzięki takim narzędziom możemy porzucić przesyłanie i rozpakowywanie archiwów,
kopiowanie plików na rzecz komend które szybko doprowadzą
ujednolicą stan plików naszych uczniów.

.. tip::

    Bardziej szczegółową dokumentację i przykłady użycia znajdziecie
    w dostępnej online i do pobrania polskiej wersji książki `Pro Git`_ .
    Polecamy także `cheat sheet z podręcznymi komendami <https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf>`_.

.. _Pro Git: http://git-scm.com/book/pl

Lokalne repozytoria z historią zmian
------------------------------------

Każdy z uczniów może meć lokalną kopię całej historii zmian w plikach,
będzie mógł modyfikować swoje przykłady, ale w kluczowym momencie nauczyciel
może poprosić by wszyscy zsynchronizowali swoje kopie do jednej sprawdzonej wersji.

Okresowa synchronizacja przykładów które uczniowie z założenia zmieniają
podczas zajęć pozwala wykluczyć pomyłki i wyeliminować problemy wynikające z różnic
we wprowadzonych zmianach.

.. code-block:: bash

    $ git checkout -f zadanie2/wersja5


Przed porzuceniem swoich zmian uczeń może zapisać kopię swojej pracy w repozytorium.

.. code-block:: bash

    $ git commit -a -m "Moje zmiany w przykładzie 5"

Centrale repozytoria dostępne przez internet
--------------------------------------------

Posługując się repozytoriami plików często mówimy o nich jako o „projektach“.
Projekty mogą mieć swoje centralne repozytoria dostępne publicznie lub
dla wybranych użytkowników.

W szczególności polecamy serwisy:

1. GitHub - https://github.com/ - bezpłatne repozytoria dla projektów widocznych publicznie
2. Bitbucket - https://bitbucket.org/ - bezpłatne repozytoria dla projektów bez wymogu ich upubliczniania

W każdym z nich możemy ograniczyć możliwość modyfikacji kodu do wybranych osób,
a wymienione serwisy różnią się tym, że GitHub_ jest większy i bardziej popularny w środowisku open source,
natomiast Bitbucket_ bezpłatnie umożliwia całkowite ukrycie projektów.

Dodatkowo te serwisy oferują rozszerzony bezpłatnych dostęp dla uczniów i nauczycieli,
a także oferują rozbudowane płatne funkcje.

.. _GitHub: https://github.com/
.. _Bitbucket: https://bitbucket.org/

Nowe konto GitHub
-----------------

Zakładamy, że nauczyciele nie muszą korzystać z prywatnych repozytoriów, a dostęp do większej liczby projektów
pomoże w nauce, dlatego początkującym proponujemy założenie konta w serwisie GitHub_.

.. figure:: github1.png


Forkujemy pierwszy projekt
--------------------------

Każdy może sobie skopiować (do własnego repozytorium) i modyfikować projekty publicznie dostępne w GitHub_.
Dzięki temu każdy może wykonać — na swojej kopii — poprawki i zaprezentować te poprawki światu i autorom projektu :)

Wykonajmy teraz forka naszego projektu z przykładami i tą dokumentacją.

https://github.com/koduj-z-klasa/python101

.. figure:: fork.png

Oczywiście możemy sobie założyć nowy pusty projekt, ale łatwiej będzie
nam się pobawić narzędziami na istniejącym projekcie.

.. note::

    Forkując, klonujemy historię zmian w projekcie (więcej o klonowaniu za chwilę).

    Forkiem często określamy kopię projektu, która będzie rozwijana niezależnie od oryginału.
    Np. jeśli chcemy wprowadzić modyfikacje, które nam są potrzebne, ale które nie zostaną
    przekazane do oryginalnego repozytorium.


Instalujemy narzędzie GIT
-------------------------

Do korzystania z naszego repozytorium lokalnie na naszym komputerze musimy doinstalować niezbędne oprogramowanie.

Pod linuksem:

.. code-block:: bash

    $ sudo apt-get install git

Pod windows polecamy zainstalować SourceTree_:

.. _SourceTree: http://www.sourcetreeapp.com/

.. code-block:: bat

    > @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
    > choco install sourcetree

Jeśli nie mamy PowerShell'a `możemy sciągnąć i zainstalować <http://www.sourcetreeapp.com/download>`_ narzędzie ręcznie.

Przed pierwszym użyciem warto jeszcze skonfigurować dwie informacje identyfikujące ciebie jako autora zmian.
W komendach poniżej wstaw swoje dane.

.. code-block:: bash

    $ git config --global user.name "Jan Nowak"
    $ git config --global user.email jannowak@example.com

Klonujemy nasz projekt lokalnie
-------------------------------

Klonowanie to proces tworzenia lokalnej kopii historii zmian.
Dzięki temu możemy wprowadzić zmiany i zapisać je lokalnej kopii historii zmian,
a następnie synchronizować historie zmian pomiędzy repozytoriami.

.. figure:: clone.png

.. code-block:: bash

    ~$ git clone https://github.com/<MOJA-NAZWA-UŻYTKOWNIKA>/python101.git

W efekcie uzyskamy katalog ``python101`` zawierający kopie plików, które będziemy zmieniać.

.. note::

    W podobny sposób uczniowie mogą wykonać lokalną kopię naszych materiałów.
    Dyskusję czy to jest fork czy klon zostawmy na później ;)


Skok do wybranej wersji z historii zmian
----------------------------------------

Klon repozytorium zawiera całą historię zmian projektu:

.. code-block:: bash

    ~$ cd python101
    ~/python101$ git log

    commit 510611a351c7c3ff60e2506d8704e3f786fcedb7
    Author: Janusz Skonieczny <js+sourcetree@bravelabs.pl>
    Date:   Thu Dec 11 15:37:46 2014 +0100

        git > source_code

    commit f7019bc1f433eb4a6c2c88f8f48337c77e5e415e
    Author: Janusz Skonieczny <js+sourcetree@bravelabs.pl>
    Date:   Thu Dec 11 15:26:16 2014 +0100

        req

    commit 302fb3a974954ad936a825ba37519e145c148290
    Author: wilku-ceo <grzegorz.wilczek@ceo.org.pl>
    Date:   Thu Dec 11 11:05:43 2014 +0100

        poprawiona nazwa CEO



Możemy skoczyć do dowolnej z nich ustawiając wersje plików w kopii roboczej
według jednej z wersji zapamiętanej w historii zmian.

.. code-block:: bash

    ~/python101$ git checkout 302fb3

    Previous HEAD position was 510611a... git > source_code
    HEAD is now at 302fb3a... poprawiona nazwa CEO


Zmiany można też oznaczyć czytelnym tag'iem tak by łatwiej było zapamiętać miejsca docelowe.
W przykładzie poniżej ``pong/z1`` jest przykładową etykietą wersji plików potrzebnej podczas pracy
z pierwszym zadaniem ćwiczenia z grą pong.

.. code-block:: bash

    ~/python101$ git checkout pong/z1

Tyle tytułem wprowadzenia. Wróćmy do ostatniej wersji i wprowadź jakieś zmiany.

.. code-block:: bash

    ~/python101$ git checkout master


Zmieniamy i zapisujemy zmiany w lokalnym repozytorium
-----------------------------------------------------

Dopiszmy coś co pliku ``README`` i zapiszmy go na dysku.
A następnie sprawdźmy pzy pomocy komendy ``git status`` czy nasza zmiana zostanie wykryta.


.. code-block:: bash

    ~/python101$ git status

    On branch master
    Your branch is up-to-date with 'origin/master'.

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")


Następnie dodajmy zmiany do repozytorium. Normalnie nie zajmuje to tylu operacji,
ale chcemy zobaczyć co się dzieje na każdym etapie.

.. code-block:: bash

    ~/python101$ git add README.md
    ~/python101$ git status
    On branch master
    Your branch is up-to-date with 'origin/master'.

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

        modified:   README.md


    ~/python101$ git commit -m "Moja pierwsza zmiana!"
    [master 87ec5f4] Moja pierwsza zmiana!
    1 file changed, 1 insertion(+), 1 deletion(-)

    ~/python101$ git status
    On branch master
    Your branch is ahead of 'origin/master' by 1 commit.
      (use "git push" to publish your local commits)

    nothing to commit, working directory clean

Zazwyczaj wszystkie operacje zapisania zmian w historii zawrzemy w jednej komendzie:

.. code-block:: bash

    ~/python101$ git commit -a -m "Moja pierwsza zmiana!"`

Wysyłamy zmiany do centralnego repozytorium
-------------------------------------------

Na razie historia naszych zmian została zapisana lokalnie. Możemy w ten sposób pracować
nad projektami jednak gdy chcemy podzielić swoim geniuszem ze światem, musimy go wysłać
do repozytorium dostępnego przez innych.

.. code-block:: bash

    ~/python101$ git push origin master

Komenda ``push`` przyjmuje dwa parametry alias `zdalnego repozytorium <http://git-scm.com/book/pl/v1/Podstawy-Gita-Praca-ze-zdalnym-repozytorium>`_
``origin`` oraz nazwę `gałęzi zmian <http://git-scm.com/book/pl/v1/Ga%C5%82%C4%99zie-Gita-Czym-jest-ga%C5%82%C4%85%C5%BA>`_ ``master``.

.. tip::

    Dla uproszczenia wystarczy, że zapamiętasz tą komendę tak jak jest, bez wnikania w znaczenie wartości parametrów.
    W większości przypadków jest ona wystarczająca do osiągnięcia celu.

Sprawdź teraz czy w twoim repozytorium w serwisie GitHub pojawiły się zmiany.

Przypisujemy tagi do konkretnych wersji w historii zmian
--------------------------------------------------------

Możemy etykietę przypisać do aktualnej wersji zmian:

.. code-block:: bash

    ~/python101$ git tag moja_zmiana

Lub wybrać i przypisać ją do wybranej wersji historycznej.

.. code-block:: bash

    ~/python101$ git log --pretty=oneline
    87ec5f4d8e639365f360bc11b9b51629b909ee9d Moja pierwsza zmiana!
    510611a351c7c3ff60e2506d8704e3f786fcedb7 git > source_code
    f7019bc1f433eb4a6c2c88f8f48337c77e5e415e req
    302fb3a974954ad936a825ba37519e145c148290 poprawiona nazwa CEO

    ~/python101$ git tag zmiana_ceo 302fb3a

    ~/python101$ git show zmiana_ceo
    commit 302fb3a974954ad936a825ba37519e145c148290
    Author: wilku-ceo <grzegorz.wilczek@ceo.org.pl>
    Date:   Thu Dec 11 11:05:43 2014 +0100

        poprawiona nazwa CEO

    diff --git a/docs/copyright.rst b/docs/copyright.rst
    index 85feb38..431eb81 100644
    --- a/docs/copyright.rst
    +++ b/docs/copyright.rst
    @@ -5,7 +5,7 @@
                 <img alt="Licencja Creative Commons" style="border-width:0" src="ht
             Materiały <span xmlns:dct="http://purl.org/dc/terms/" href="http://purl
             udostępniane przez <a xmlns:cc="http://creativecommons.org/ns#" href="h
    -        Centrum Edudkacji Europejsci</a> na licencji <a rel="license" href="htt
    +        Centrum Edukacji Obywatelskiej</a> na licencji <a rel="license" href="h
             Creative Commons Uznanie autorstwa-Na tych samych warunkach 4.0 Międzyn
         </p>


Wysyłamy tagi do centralnego repozytorium
-----------------------------------------

Etykiety które przypiszemy do wersji w historii zmian muszą zostać wypchnięte
do centralnego repozytorium przy pomocy specjalnej wersji komendy push.

.. code-block:: bash

    ~/python101$ git push origin --tags --force

Parametr ``--tags`` mowi komendzie by wypchnęła nasze etykiety,
natomiast ``--force`` wymusi zmiany w ew. istniejących etykietach — bez ``--force``
serwer może odrzucić nasze zmiany jeśli takie same etykiety już istnieją
w centralnym repozytorium i są przypisane do innych wersji zmian.

Pobieramy zmiany z centralnego repozytorium
-------------------------------------------

Jeśli już mamy klona repozytorium i chcemy upewnić się że mamy lokalnie najnowsze wersje plików
(np. gdy nauczyciel zaktualizował przykłady lub dodał nowe pliki), to ciągniemy zmiany
z centralnego repozytorium:

.. code-block:: bash

    ~/python101$ git pull

Ta komenda ściągnie historię zmian z centralnego repozytorium i zaktualizuje naszą kopię roboczą plików.

Metryka
^^^^^^^

:Autorzy: Janusz Skonieczny <js@bravelabs.pl>,

:Utworzony: |date| o |time|

.. |date| date::
.. |time| date:: %H:%M


.. raw:: html

    <style>
        div.code_no { text-align: right; background: #e3e3e3; padding: 6px 12px; }
        div.highlight, div.highlight-python { margin-top: 0px; }
    </style>

.. include:: ../copyright.rst
