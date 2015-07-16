Git - wersjonowanie kodów źródłowych
====================================

.. _git-howto:

Pokażemy tutaj, jak nauczyciele mogą wykorzystać profesjonalne i bezpłatne narzędzia do wersjonowania
kodów źródłowych i wszystkich innych plików.

Przybliżamy tutaj jak GIT jest wykorzystywany w naszych materiałach i pokważemy jak go wykorzystać go podczas zajęć w szkole.

Poniżej przeprowadzimy szybkie wprowadzenie po więcej informacji oraz pełne szczegółowe wprowadzenie i przykłady użycia znajdziecie
w dostępnej online i do pobrania polskiej wersji książki `Pro Git`_ .
Polecamy także `cheat sheet z podręcznymi komendami <https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf>`_.


Co to jest GIT?
===============

GIT to system kontroli wersji, pozwala zapemiętać i synchronizować pomiędzy uzytkownikami zmiany dokonywane na plikach.
Umożliwia przywołanie dowolnej wcześniejszej wersji, a co najważniejsze,
automatycznie łączy zmiany które ze sobą nie kolidują, np. dokonane w różnych miejscach w pliku.

Nauczyciele pracujący z plikami, które zmieniają się z przykładu na przykład,
z ćwiczenia na ćwiczenie mogą skorzystać z systemu kontroli wersji do
synchronizacji przykładów z uczniami na poszczególnych etapach swojej pracy.

.. figure:: git-scm.png

Dzięki takim narzędziom możemy porzucić przesyłanie i rozpakowywanie archiwów oraz
kopiowanie plików na rzecz komend które szybko
ujednolicą stan plików na komputerach naszych uczniów.

.. _Pro Git: http://git-scm.com/book/pl

Lokalne repozytoria z historią zmian
------------------------------------

Każdy z uczniów może meć lokalną kopię całej historii zmian w plikach,
będzie mógł modyfikować swoje przykłady, ale w kluczowym momencie nauczyciel
może poprosić by wszyscy zsynchronizowali swoje kopie do jednej sprawdzonej wersji,
tak by dalej prowadzić zajęcia na jednolitym fundamencie.

Okresowa synchronizacja przykładów, które uczniowie z założenia zmieniają
podczas zajęć pozwala wykluczyć pomyłki i wyeliminować problemy wynikające z różnic
we wprowadzonych zmianach.

Poniżej mamy przykład komendy która otworzy pliki w `wersji 5` dla `zadania 2` .
Nazwy `zadanie2` oraz `wersja5` sa tylko przykładem, mogą być dowolnie wybrane przez autora.

.. code-block:: bash

    $ git checkout -f zadanie2/wersja5


Przed porzuceniem swoich zmian uczeń może zapisać kopię swojej pracy w repozytorium.

.. code-block:: bash

    $ git commit -a -m "Moje zmiany w przykładzie 5"


Instalujemy narzędzie GIT
=========================

.. _git-install:

Do korzystania z naszego repozytorium lokalnie na naszym komputerze musimy doinstalować niezbędne oprogramowanie.

Pod linuksem
------------

W linuksie do instalacji użyjemy menadżera pakietów, np. apt-get:

.. code-block:: bash

    $ sudo apt-get install git

Pod windows
-----------

Pod windows polecamy zainstalować SourceTree_, aplikację okienkową i narzędzia konsolowe:

.. _SourceTree: http://www.sourcetreeapp.com/

.. code-block:: bat

    > @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
    > choco install sourcetree

Jeśli nie mamy PowerShell'a `możemy sciągnąć i zainstalować <http://www.sourcetreeapp.com/download>`_ narzędzie ręcznie.

Ewentualnie możemy zainstalować tylko GIT dla konsoli:

.. code-block:: bat

    > @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
    > choco install git


Konfiguracja i pierwsze uruchomienie
------------------------------------

Przed pierwszym użyciem warto jeszcze skonfigurować dwie informacje identyfikujące ciebie jako autora zmian.
W komendach poniżej wstaw swoje dane.

.. code-block:: bash

    $ git config --global user.name "Jan Nowak"
    $ git config --global user.email jannowak@example.com

Więcej `o konfiguracji przeczytacie tutaj <http://git-scm.com/book/pl/v1/Pierwsze-kroki-Wst%C4%99pna-konfiguracja-Git>`_.

Pierwsze kroki i podstawy GIT
=============================

Na początek utwórzmy sobie piaskownicę do zabawy z GIT.
Naszą piaskownicą będzie zwyczajny katalog, dla ułatwienia pracy z ćwiczeniami
zalecamy nazwać go tak samo jak my, ale ostatecznie jego nazwa i lokalizacja nie ma znaczenia.

.. code-block:: bash

    ~$ mkdir git101
    ~$ cd git101/

Tworzymy lokalną historię zmian
-------------------------------

Przed rozpoczęciem pracy z wersjami plików w nowym lub istniejącym projekcie (takim który jeszcze nie ma historii zmian),
inicjalizujemy GITa w katalogu tego projektu. Tworzymy lokalne repozytorium poleceniem :

.. code-block:: bash

    ~/git101$ git init
    Initialized empty Git repository in ~/git101/.git/

W wyniku w naszym katalogu projektu (na razie pustym) pojawi się katalog `.git`
w nim narzędzie będzie miało swój schowek.


Zaczynamy śledzić pliki
-----------------------

W każdym momencie możemy sprawdzić status naszego repozytorium:

.. code-block:: bash

    ~/git101$ git status
    On branch master

    Initial commit

    nothing to commit (create/copy files and use "git add" to track)

Kluczowe jest `nothing to commit`, oznacza to że narzędzie nie wykryło
zmian w stosunku do tego co jest zapisane w repozytorium.
Słusznie, bo katalog jest pusty. Dodajmy jakieś pliki:

.. code-block:: bash

    ~/git101$ touch README hello.py
    ~/git101$ git status
    On branch master

    Initial commit

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        README
        hello.py

    nothing added to commit but untracked files present (use "git add" to track)

W powyższym komunikacie kluczowe jest `untracked files present`,
narzędzie wykryło pliki które jeszcze nie są śledzone, możemy rozpocząć
ich śledzenie wykonując polecenie podane we wskazówce:

.. code-block:: bash

    ~/git101$ git add hello.py README
    ~/git101$ git status
    On branch master

    Initial commit

    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)

        new file:   README
        new file:   hello.py

W efekcie wyraźnie zaznaczyliśmy które pliki GIT ma śledzić.
Działa to także w druga stronę, jeśli jakieś pliki mają zostać
zignorowane to trzeba to wyraźnie zaznaczyć, narzędzie nie
nie decyduje o tym za nas.

.. note::

    Operacji dodawania nie musimy powtarzać za każdym razem gdy
    plik się zmieni, musimy ja wykonać tylko jak pojawiają się nowe pliki.


Zapamiętujemy wersję plików
---------------------------

Zamiany w plikach zapisujemy wykonując komendę `git commit`:

.. code-block:: bash

    ~/git101$ git commit -m "Moja pierwsza wersja plików"
    [master (root-commit) e9cffa4] Moja pierwsza wersja plików
     2 files changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 README
     create mode 100644 hello.py

Parametr `-m` pozwala wprowadzić komentarz który pojawi się w historii zmian.

.. note::

    Komentarz jest wymagany, bo to dobra praktyka. Jeśli jesteśmy leniwi możemy podać
    jedno słowo albo nawet literę, wtedy nie jest potrzebny cudzysłów.

Sprawdźmy status a następnie zmodyfikujmy jeden z plików:

.. code-block:: bash

    ~/git101$ git status
    On branch master
    nothing to commit, working directory clean
    ~/git101$ echo "To jest piaskownica Git101." > README
    ~/git101$ touch tanie_dranie.py
    ~/git101$ git status
    On branch master
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        tanie_dranie.py

    no changes added to commit (use "git add" and/or "git commit -a")

GIT poprawnie wskazał, że nie ma zmian, następnie wykrył zmianę w pliki `README`
oraz pojawienie się nowego jeszcze nie śledzonego pliku.

.. note::

    Wskazówka zawiera tekst: `no changes added to commit (use "git add" and/or "git commit -a")`,
    wskazując na użycie komendy `git add`. Wcześniej mówiliśmy że nie trzeba
    operacji dodawania powtarzać za każdym razem - otóż nie trzeba, ale można.

    Dzięki temu możemy wybierać pliki które wersje nie zostaną zapisane, tworząc
    tzw. staging (poczekalnia), w poczekalni przygotowujemy zestaw plików,
    który zostanie zapisany w historii zmian w monecie wykonania `git commit`.

    Na razie nie zawracajmy sobie tym głowy, a po więcej informacji zapraszamy
    `do rozdziału o poczekalni <http://git-scm.com/book/pl/v1/Podstawy-Gita-Rejestrowanie-zmian-w-repozytorium#Dodawanie-zmodyfikowanych-plików-do-poczekalni>`_


Zapamiętajmy zmiany pliku 'README' w repozytorium przy pomocy komendy `git commit -a` z wskazówki:

.. code-block:: bash

    ~/git101$ git commit -a -m zmiana1
    [master c22799b] zmiana1
     1 file changed, 1 insertion(+)
    ~/git101$ git status
    On branch master
    Untracked files:
      (use "git add <file>..." to include in what will be committed)

        tanie_dranie.py

    nothing added to commit but untracked files present (use "git add" to track)

GIT wskazał nam, że plik tanie_dranie.py wciąż nie jest śledzony.
To nowy plik w naszym katalogu a my zapomnieliśmy go wcześniej `dodać`:

.. code-block:: bash

    ~/git101$ git add tanie_dranie.py
    ~/git101$ git commit -am nowy1
    [master 226e556] nowy1
     1 file changed, 0 insertions(+), 0 deletions(-)
     create mode 100644 tanie_dranie.py
    ~/git101$ git status
    On branch master
    nothing to commit, working directory clean

Podgląd historii zmian i wyciąganie wersji archiwalnych
-------------------------------------------------------

W każdym momencie możemy wyciągnąć wersję archiwalną z repozytorium.
Sprawdźmy co sobie zapisaliśmy w repozytorium.

.. code-block:: bash

    ~/git101$ git log
    commit 226e556d93ab9df6f21574ecdd29ba6b38f6aaab
    Author: Janusz Skonieczny <js@br..labs.pl>
    Date:   Thu Jul 16 19:43:28 2015 +0200

        nowy1

    commit 1e2678f4190cbf78f3e67aafb0b896128298de03
    Author: Janusz Skonieczny <js@br..labs.pl>
    Date:   Thu Jul 16 19:29:37 2015 +0200

        zmiana1

    commit e9cffa4b65487f9c5291fa1b9607b1e75e394bc1
    Author: Janusz Skonieczny <js@br..labs.pl>
    Date:   Thu Jul 16 19:00:04 2015 +0200

        Moja pierwsza wersja plików

Teraz sprawdźmy co się kryje w naszym pliku `README` i wyciągnijmy jego pierwsza wersję:

.. code-block:: bash

    ~/git101$ cat README
    To jest piaskownica Git101.
    ~/git101$ git checkout e9cffa
    Note: checking out 'e9cffa'.

    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by performing another checkout.

    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -b with the checkout command again. Example:

      git checkout -b new_branch_name

    HEAD is now at e9cffa4... Moja pierwsza wersja plików
    ~/git101$ cat README
    ~/git101$ git checkout master
    Previous HEAD position was e9cffa4... Moja pierwsza wersja plików
    Switched to branch 'master'
    ~/git101$ cat README
    To jest piaskownica Git101.

Działo się! Zwróćmy uwagę jak wskazaliśmy wersję z historii zmian,
podaliśmy początek skrótu `e9cffa4b65487f9c5291fa1b9607b1e75e394bc1`,
czyli tego opisanego komentarzem `Moja pierwsza wersja plików` do komendy `git checkout`.

Następnie przywróciliśmy najnowsze wersje plików z gałęzi `master`.
Wyjaśnienia co są gałęzie, zostawmy na później, tymczasem wystarczy nam to,
że komenda `git checkout master` zapisze nasze pliki w najnowszych wersjach
zapamiętanych w repozytorium.

Na razie nie przejmujemy się także ostrzeżeniem `You are in 'detached HEAD' state.`,
to także zostawiamy na później.

Spróbujcie teraz poćwiczyć wprowadzanie zmian i zapisywanie ich w repozytorium.

Centrale repozytoria dostępne przez internet
============================================

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

Wykonajmy teraz forka naszego projektu z przykładami i tą dokumentacją (tą którą czytasz).

https://github.com/koduj-z-klasa/python101

.. figure:: fork.png

Oczywiście możemy sobie założyć nowy pusty projekt, ale łatwiej będzie
nam się pobawić narzędziami na istniejącym projekcie.

.. note::

    Forkując, klonujemy historię zmian w projekcie (więcej o klonowaniu za chwilę).

    Forkiem często określamy kopię projektu, która będzie rozwijana niezależnie od oryginału.
    Np. jeśli chcemy wprowadzić modyfikacje, które nam są potrzebne, ale które nie zostaną
    przekazane do oryginalnego repozytorium.



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
    Author: Janusz Skonieczny <...>
    Date:   Thu Dec 11 15:37:46 2014 +0100

        git > source_code

    commit f7019bc1f433eb4a6c2c88f8f48337c77e5e415e
    Author: Janusz Skonieczny <...>
    Date:   Thu Dec 11 15:26:16 2014 +0100

        req

    commit 302fb3a974954ad936a825ba37519e145c148290
    Author: wilku-ceo <...>
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

# Konfiguracja SSH pod windowsJesli korzystamy z narzedzia KeePass do przechowywania hasel i kluczy SSH, to dobrze jest polaczyć je z GITem przez narzedzie Plink, do tego celu musimy dodać zmienna systemowa podmieniajaca domyslne narzedzie SSH. 

Uruchamiamy konsole PowerShell z uprawnieniami administracyjnymi:

.. code-block:: ps

    [Environment]::SetEnvironmentVariable("GIT_SSH", "d:\usr\tools\PuTTY\plink.exe", "User")
