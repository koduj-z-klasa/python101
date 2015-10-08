#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg

runda_numer = 0 # numer rundy
wybrane_pola = set() # zbiór wybranych w rundzie pól

class Robot:

    def act(self, game):

        global runda_numer, wybrane_pola
        if game.turn != runda_numer:
            runda_numer = game.turn
            wybrane_pola = set()

        # jeżeli się ruszamy, zapisujemy docelowe pole
        def ruszaj(loc):
            wybrane_pola.add(loc)
            return ['move', loc]

        # jeżeli stoimy, zapisujemy zajmowane miejsce
        def stoj(act, loc=None):
            wybrane_pola.add(self.location)
            return [act, loc]

        # wszystkie pola
        wszystkie = {(x, y) for x in xrange(19) for y in xrange(19)}
        # punkty wejścia
        wejscia = {poz for poz in wszystkie if 'spawn' in rg.loc_types(poz)}
        # pola zablokowane
        zablokowane = {poz for poz in wszystkie if 'obstacle' in rg.loc_types(poz)}
        # pola zajęte przez nasze roboty
        przyjaciele = {poz for poz in game.robots if game.robots[poz].player_id == self.player_id}
        # pola zajęte przez wrogów
        wrogowie = set(game.robots) - przyjaciele
        # pola sąsiednie
        sasiednie = set(rg.locs_around(self.location)) - zablokowane
        # pola sąsiednie zajęte przez wrogów
        wrogowie_obok = sasiednie & wrogowie
        wrogowie_obok2 = {poz for poz in sasiednie if (set(rg.locs_around(poz)) & wrogowie)} - przyjaciele
        # pola bezpieczne
        bezpieczne = sasiednie - wrogowie_obok - wrogowie_obok2 - wejscia - przyjaciele - wybrane_pola

        # funkcja znajdująca najsłabszego wroga obok z podanego zbioru (bots)
        def mindist(bots, loc):
            return min(bots, key=lambda x: rg.dist(x, loc))

        if wrogowie:
            najblizszy_wrog = mindist(wrogowie,self.location)
        else:
            najblizszy_wrog = rg.CENTER_POINT

        # działanie domyślne:
        ruch = ['guard']

        # jeżeli jesteś w punkcie wejścia, opuść go
        if self.location in wejscia:
            ruch = ruszaj(mindist(bezpieczne, rg.CENTER_POINT))

        # jeżeli jesteś w środku, broń się
        if self.location == rg.CENTER_POINT:
            ruch = ['guard']

        # jeżeli obok są przeciwnicy, atakuj, o ile to bezpieczne,
        # najsłabszego wroga
        if wrogowie_obok:
            if 9*len(wrogowie_obok) >= self.hp:
                if bezpieczne:
                    ruch = ruszaj(mindist(bezpieczne, rg.CENTER_POINT))
            else:
                ruch = ['attack', minhp(wrogowie_obok)]

        if wrogowie_obok2 and self.location not in wybrane_pola:
            ruch = ['attack', wrogowie_obok2.pop()]

        return ruch
