.. _strategia2:

Strategia pośrednia
####################

Zacznijmy od znanego
*********************************
W poprzednim poradniku (:ref:`strategia1`) zaczęliśmy od bota realizującego następujące zasady:

* Broń się w środku planszy
* Atakuj wrogów obok
* Idź do środka

Zmieniliśmy lub dodaliśmy następujące reguły:

* Opuść wejście
* Uciekaj, jeśli masz zginąć
* Atakuj wrogów dwa kroki obok
* Wchodź na bezpieczne, niezajęte pola
* Idź na wroga, jeśli w pobliżu go nie ma

Do powyższych dodamy kolejne reguły w postaci fragmentów kodu, które trzeba
zintergrować z dotychczasową implementacją bota, aby go ulepszyć.


Śledź wybierane miejsca
************************

To raczej złożona funkcja, ale jest potrzebna, aby zmniejszyć ilość kolizji.
Dotychczasowe boty drużyny próbują wejść na to samo miejsce i atakują się nawzajem.
Co prawda nie tracimy wtedy pukntów życia, ale (prawie) zawsze mamy lepszy wybór.
Jeżeli będziemy śledzić wszystkie wybrane przez nas ruchy w ramach rundy, możemy
uniknąć niepotrzebnych kolizji. Niestety, to wymaga wielu fragementów kodu.

Na początku dodamy zmienną, która posłuży do sprawdzenia, czy dany robot
jest pierwszym wywoływanym w rundzie. Jeżeli tak, musimy wyczyścić listę
poprzednich ruchów i zaktualizować licznik rund. Odpowiedni kod trzeba
umieścić na początku metody ``Robot.act``:

.. attention::

    Trzeba zainicjować zmienną globalną ``runda_numer``.

.. code-block:: python

    global runda_numer, wybrane_pola
    if game.turn != runda_numer:
        runda_numer = game.turn
        wybrane_pola = set()

Kolejne fragmenty odpowiadać będą za zapamiętywanie wykonywanych ruchów.
Kod najwygodniej umieścić w pojedynczych funkcjach, które zanim zwrócą
wybrany ruch, zapiszą go na liście. Warto zauważyć, że zapisywane będą
współrzędne pól, na które wchodzimy lub na których pozostajemy (obrona, atak,
samobójstwo). Funkcje muszą znaleźć się w metodzie ``Robot.act``,
aby współdzieliły jej przestrzeń nazw.

.. code-block:: python

    # Jeżeli się ruszamy, zapisujemy docelowe pole

    def ruszaj(loc):
        wybrane_pola.add(loc)
        return ['move', loc]

    # Jeżeli pozostajemy w miejscu, zapisujemy aktualne położenie
    # przy użyciu self.location

    def stoj(act, loc=None):
        wybrane_pola.add(self.location)
        return [act, loc]

Następnym krokiem jest usunięcie listy ``wybrane_pola``
ze zbioru bezpiecznych pól, które są podstawą dalszych wyborów:

.. code-block:: python

    bezpieczne = sasiednie - wrogowie_obok - wrogowie_obok2 \
                 - wejscia - przyjaciele - wybrane_pola

Roboty atakujące przeciwnika o dwa kroki obok często go otaczają (to dobrze),
ale jednocześnie blokują innych członków drużyny.
Dlatego możemy wykluczać ataki na pola *wrogowie_obok2*, jeśli znajdują się
na liście wykonanych ruchów.

[Robots that attack two moves away often form a perimeter around the enemy
(a good thing) but it prevents your own bots from run across the line.
For that reason we can choose to not let a robot do an an adjacent_enemy2
attack if they are sitting in a taken spot.]

.. code-block:: python

    elif wrogowie_obok2 and self.location not in wybrane_pola:

Na koniec podmieniamy kod zwracający ruchy:

.. code-block:: python

    ruch = ['move', mindist(bezpieczne, najblizszy_wrog)]
    ruch = ['attack', wrogowie_obok.pop()]

– tak aby wykorzystywał nowe funkcje:

.. code-block:: python

    ruch = ruszaj(mindist(bezpieczne, najblizszy_wrog))
    ruch = stoj('attack', wrogowie_obok.pop())

Warto pamiętać, że roboty nie mogą zamieniać się miejscami. Wprawdzie
jest możliwe zakodowanie tego, ale zamiana nie dojdzie do skutku.

Atakuj najsłabszego wroga
**************************

Każdy udany atak zmniejsza punkty HP wrogów tak samo, ale wynik gry
zależy od liczby pozostałych przy życiu robotów, a nie od ich żywotności.
Dlatego korzystniejsze jest wyeliminowanie słabego bota niż atakowanie/osłabienie
silnego. Odpowiednią funkcję umieścimy w funkcji ``Robot.act`` i użyjemy do
wyboru robota z listy zamiast dotychczasowej funkcji ``.pop()``, która zwracała
losowe roboty.

.. code-block:: python

    # funkcja znajdująca najsłabszego robota

    def minhp(bots):
        return min(bots, key=lambda x: game.robots[x].hp)

    elif wrogowie_obok:
        ...
        else:
            ruch = stoj('attack', minhp(wrogowie_obok))

Samobójstwo lepsze niż śmierć
******************************

Na razie usiłujemy uciec, jeżeli grozi nam śmierć, ale czasami może się
nam nie udać, bo natkniemy się na atakującego wroga. Jeżeli brak bezpiecznego
ruchu, a grozi nam śmierć, o ile pozostaniemy  w miejscu, możemy
popełnić samobójstwo, co osłabi wrogów bardziej niż atak.

.. code-block:: python

    elif wrogowie_obok:
        if 9*len(wrogowie_obok) >= self.hp:
            if bezpieczne:
                ruch = ruszaj(mindist(safe, rg.CENTER_POINT))
            else:
                ruch = stoj('suicide')
        else:
            ruch = stoj('attack', minhp(wrogowie_obok))

Unikaj nierównych starć
************************

W walce jeden na jednego nikt nie ma przewagi, ponieważ wróg może odpowiadać
atakiem na każdy nasz atak, jeżeli jesteśmy obok. Ale gdy wróg ma liczebną
przewagę, atakując dwoma robotami naszego jednego, dostaniemy podwójnie
za każdy wyprowadzony atak. Dlatego należy uciekać, jeśli wrogów
jest więcej. Warto zauważyć, że jest to kluczowa zasada w dążeniu do zwycięstwa
w *Grze robotów*, nawet w rozgrywkach na najwyższym poziomie.
Walka z wykorzystaniem przewagi jest zresztą warunkiem wygranej w większości pojedynków.

.. code-block:: python

    elif wrogowie_obok:
        if 9*len(wrogowie_obok) >= self.hp:
            ...
        elif len(wrogowie_obok) > 1:
            if bezpieczne:
                ruch = ruszaj(mindist(safe, rg.CENTER_POINT))
        else:
            ruch = stoj('attack', minhp(wrogowie_obok))

Goń słabe roboty
******************

Możemy założyć, że słabe roboty będą uciekać. Zamiast atakować podczas
ucieczki, powinniśmy je gonić. W ten sposób możemy wymusić kolejny ruch
w następnej turze, dzięki czemu trafią być może w gorsze miejsce.
Bierzemy pod uwagę roboty, które mają maksymalnie 5 punktów HP,
nawet gdy zaatakują zamiast uciekać, zginą w wyniku uszkodzeń z powodu kolizji.

.. code-block:: python

    elif wrogowie_obok:
        ...
        else:
            cel = minhp(wrogowie_obok)
            if game.robots[cel].hp <= 5:
                ruch = ruszaj(cel)
            else:
                ruch = stoj('attack', minhp(wrogowie_obok))

Trzeba pamiętać, że startegia gonienia słabego robota ma jedną oczywistą
wadę. Jeżeli słaby robot wybierzez obronę, goniący odniesie uszkodzenia
z powodu kolizji, broniący nie. Można temu przeciwdziałać wybierając atak,
a nie pogoń – koło się zamyka.

Podsumowanie
*************

Poniżej zestawienie reguł, które dodaliśmy:

* Śledź wybierane miejsca
* Atakuj najsłabszego wroga
* Samobójstwo lepsze niż śmierć
* Unikaj nierównych starć
* Goń słabe roboty

Dodanie powyższych zmian umożliwi stworzenie robota podobnego do *simplebot*
z pakietu open-source. Sprawdź jego kod, aby ulepszyć swojego. Do tej pory
tworzyliśmy robota walczącego według zbioru kilku reguł, ale w następnym
materiale poznamy roboty inaczej decydujące o ruchach, dodatkowo wykorzystujące
kilka opartych na zasadach sztuczek.

Jeśli jesteś gotów, sprawdź "Zaawansowane strategie" (już wkrótce...)

.. raw:: html

    <hr />

.. note::

    Niniejsza dokumentacja jest swobodnym i nieautoryzowanym tłumaczeniem materiałów
    dostępnych na stonie `Robotgame Intermediate Strategy
    <https://github.com/ramk13/robotgame/blob/master/strategy_guide/robotgame_intermediate_strategy.md>`_.
