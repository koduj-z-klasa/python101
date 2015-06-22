#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg

# zmienne globalne
runda_numer = 0 # numer rundy
wybrane_pola = set() # zbiór wybranych w rundzie pól

class Robot:

    def act(self, game):

        # inicjacja danych
        # wyzeruj zbiór wybrane_pola przy pierwszym robocie w rundzie
        global runda_numer, wybrane_pola
        if game.turn != runda_numer:
            runda_numer = game.turn
            wybrane_pola = set()

        # jeżeli się ruszamy, zapisujemy docelowe pole
        def ruszaj(poz):
            wybrane_pola.add(poz)
            return ['move', poz]

        # jeżeli stoimy, zapisujemy zajmowane miejsce
        def stoj(act, poz=None):
            wybrane_pola.add(self.location)
            return [act, poz]

        # funkcja znajdująca najsłabszego wroga obok
        def minhp(bots):
            return min(bots, key=lambda x: game.robots[x].hp)

        def mindist(bots, poz):
            return min(bots, key=lambda x: rg.dist(x, poz))

        wszystkie = {(x, y) for x in xrange(19) for y in xrange(19)}
        wejscia = {poz for poz in wszystkie if 'spawn' in rg.loc_types(poz)}
        zablokowane = {poz for poz in wszystkie if 'obstacle' in rg.loc_types(poz)}
        przyjaciele = {poz for poz in game.robots if game.robots[poz].player_id == self.player_id}
        wrogowie = set(game.robots) - przyjaciele

        sasiednie = set(rg.locs_around(self.location)) - zablokowane
        wrogowie_obok = sasiednie & wrogowie
        wrogowie_obok2 = {poz for poz in sasiednie if (set(rg.locs_around(poz)) & wrogowie)} - przyjaciele
        # ze zbioru bezpieczne wyłączamy wybrane_pola
        bezpieczne = sasiednie - wrogowie_obok - wrogowie_obok2 - \
                     wejscia - przyjaciele - wybrane_pola

        if wrogowie:
            najblizszy_wrog = mindist(wrogowie, self.location)
        else:
            najblizszy_wrog = rg.CENTER_POINT

        # działanie domyślne:
        ruch = ['guard']

        if self.location in wejscia:
            if bezpieczne:
                ruch = ruszaj(mindist(bezpieczne, rg.CENTER_POINT))
        elif wrogowie_obok:
            if 9*len(wrogowie_obok) >= self.hp:
                if bezpieczne:
                    ruch = ruszaj(mindist(bezpieczne, rg.CENTER_POINT))
                else:
                    ruch = stoj('suicide')
            elif len(wrogowie_obok) > 1:
                if bezpieczne:
                    ruch = ruszaj(mindist(bezpieczne, rg.CENTER_POINT))
            else:
                cel = minhp(wrogowie_obok)
                if game.robots[cel].hp <= 5:
                    ruch = ruszaj(cel)
                else:
                    ruch = stoj('attack', minhp(wrogowie_obok))
        elif wrogowie_obok2 and self.location not in wybrane_pola:
            ruch = stoj('attack', wrogowie_obok2.pop())
        elif bezpieczne:
            ruch = ruszaj(mindist(bezpieczne, najblizszy_wrog))

        return ruch
