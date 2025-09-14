Warsztaty 4 godz.
#################

**Mów mi Python!** – czyli programowanie w języku Python w ramach projektu "Koduj z klasą" organizowanego przez Centrum Edukacji Obywatelskiej. Szczegóły pod adresem: `http://www.ceo.org.pl/pl/koduj <http://www.ceo.org.pl/pl/koduj>`_.

Dla kogo, czyli co musi wiedzieć uczestnik
******************************************

Dla każdego nauczyciela i ucznia, co oznacza, że materiał zawiera moduły o różnym stopniu trudności. Scenariusze zajęć oraz zakres przykładów można dostosować do poziomu uczestników.

Cele, treści i metody
*********************

Cele projektu, spis wszystkich materiałów oraz zalecane metody ich realizacji dostępne są w dokumencie :ref:`Cele, materiały i metody <materialy>` . Umieszczono tam również *listę oprogramowania* wymaganego do realizacji wszystkich materiałów. Podstawą szkoleń jest `wersja HTML <http://python101.readthedocs.org>`_ . Wersje źródłowe dostępne są w repozytorium `Python101 <https://github.com/koduj-z-klasa/python101>`_ .

Materiał zajęć
**************

Podstawy Pythona
================

	**Czas realizacji**: 1 * 45 min.

	**Metody**: kodowanie programu w edytorze od podstaw, wprowadzanie elementów języka w konsoli interpretera, ćwiczenia samodzielne w zależności od poziomu grupy.

	**Materiały i środki**: Python 2.7.x, edytor kodu, terminal, zalecany system :ref:`Linux Live LxPupTahr <linux-live>`, wersja HTML scenariusza *Mały Lotek*, punkty *1.2.1 – 1.2.5*, kod pełnego programu oraz ewentualne wersje pośrednie. Projektor, dostęp do internetu nie jest konieczny.

	**Realizacja**:: Na początku zapoznajemy użytkowników ze środowiskiem i narzędziami, tj. menedżer plików, edytor i jego konfiguracja, terminal znakowy, konsola Pythona, uruchamianie skryptu w terminalu, uruchamianie z edytora.

	Omawiamy założenia aplikacji *Mały lotek*: losowanie pojedynczej liczby i próba jej odgadnięcia przez użytkownika. Następnie rozpoczynamy wspólne kodowanie wg materiału.

	Po ukończeniu pierwszej części można urządzić mini-konkurs: zgadnij wylosowaną liczbę.

	Budując program *można* reżyserować podstawowe błędy składniowe i logiczne, aby uczestnicy nauczyli się je dostrzegać i usuwać. Np.:  próba użycia liczby pobranej od użytkownika bez przekształcenia jej na typ całkowity, niewłaściwe wcięcia, brak inkrementacji zmiennej iteracyjnej (nieskończona pętla), itp. Uczymy dobrych praktyk programowania: przejrzystość kodu (odstępy) i komentarze.

Wykresy w Pythonie
==================

	**Czas realizacji**: 1 * 45 min.1

	**Metody**: ćwiczenia w konsoli Pythona, wspólnie tworzenie i rozwijanie skryptów generujących wykresy, ćwiczenie samodzielne.

	**Materiały i środki**: Python 2.7.x, biblioteka Matplotlib, edytor kodu, terminal, zalecany system :ref:`Linux Live LxPupTahr <linux-live>`, wersja HTML scenariusza :ref:`Python kreśli <pylab>`. Projektor, dostęp do internetu nie jest konieczny.

	**Realizacja**:: Zaczynamy od prostego przykładu w konsoli Pythona, z której cały czas korzystamy. Stopniowo kodujemy przykłady wykorzystując je do praktycznego (!) wprowadzenia *wyrażeń listowych* zastępujących pętle *for*. Pokazujemy również mechanizmy związane z indeksowaniem list, m. in. *notację wycinkową* (ang. *slice*). Nie ma potrzeby ani czasu na dokładne wyjaśnienia tych technik. Celem ich użycia jest zaprezentowanie jednej z zalet Pythona: zwięzłości. Jeżeli wystarczy czasu, zachęcamy do samodzielnego sporządzenia wykresu funkcji kwadratowej.

Gra robotów
===========

	**Czas realizacji**: 2 * 45 min.

	**Metody**: omówienie zasad gry, pokaz rozgrywki między przykładowymi robotami, kodowanie klasy robota z wykorzystaniem "klocków" (gotowego kodu), uruchamianie kolejnych walk.

	**Materiały i środki**: Python 2.7.x, biblioteka rgkit, przykładowe roboty z repozytorium robotgame-bots oraz skrypt rgsimulator, edytor kodu, terminal, zalecany system :ref:`Linux Live LxPupTahr <linux-live>`, wersja HTML scenariusza :ref:`Gra robotów <robot-game>`, końcowy kod przykładowego robota w wersji *A* i *B*, koniecznie (!) kody wersji pośrednich. Projektor, dostęp do internetu lub scenariusz offline w wersji HTML dla każdego uczestnika.

	**Realizacja**:: Na początku omawiamy przygotowanie środowiska testowego, czyli użycie *virtualenv*, instalację biblioteki *rgkit, rgbots* i *rgsimulator*, polecenie *rgrun*. Uwaga: jeżeli korzystamy z *LxPupTahr*, w katalogu :file:`~/robot`  mamy kompletne wirtualne środowisko pracy.

	Podstawą jest zrozumienie reguł. Po wyjaśnieniu najważniejszych zasad gry, konstruujemy robota podstawowego w oparciu o materiał :ref:`Klocki 1 <klocki01>` . Kolejne implementowane zasady działania robota sprawdzamy w symulatorze, ucząc jednocześnie jego wykorzystania. W symulatorze reżyserujemy również przykładowe układy, wyjaśniając szczegółowe zasady rozgrywki. Później uruchomiamy "prawdziwe" walki, w tym z robotami open source (np. :file:`stupid26.py` ).

	Dalej rozwijamy strategię działania robota w oparciu o funkcje – :ref:`Klocki 2A <klocki02a>`  i/lub zbiory – :ref:`Klocki 2B <klocki02b>` . W zależności od poziomu grupy można przećwiczyć wersje: tylko *A*, *A* + *B*, *A* + *B* równolegle z porównywaniem kodu. Uwaga: nie mamy czasu na wgłębianie się w szczegóły implementacji.

	Wprowadzając kolejne zasady, wyjaśniamy odwołania do API biblioteki *rg* w dodawanych "klockach". Kolejne wersje robota zapisujemy w osobnych plikach, aby można je było konfrontować ze sobą.

	Zachęcamy uczestników do analizy kodu i zachowań robotów: co nam dało wprowadzenie danej zasady? jak można zmienić kolejność ich stosowania w kodzie? jak zachowują się roboty open source? jak można ulepszyć działanie robota?