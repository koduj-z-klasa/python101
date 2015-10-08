#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg

class Robot:

    def act(self, game):

        def czy_wejscie(poz):
            if 'spawn' in rg.loc_types(poz):
                return True
            return False

        def czy_wrog(poz):
            if game.robots.get(poz) != None:
                if game.robots[poz].player_id != self.player_id:
                    return True
            return False
        
        # lista wrogów obok
        wrogowie_obok = []
        for poz in rg.locs_around(self.location):
            if czy_wrog(poz):
                wrogowie_obok.append(poz)

        # jeżeli jesteś w punkcie wejścia, opuść go
        if czy_wejscie(self.location):
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        # jeżeli obok są przeciwnicy, atakuj
        if len(wrogowie_obok):
            return ['attack', wrogowie_obok.pop()]

        # jeżeli jesteś w środku, broń się
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # idź do środka planszy
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
