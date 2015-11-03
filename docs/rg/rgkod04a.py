#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg


class Robot:

    def act(self, game):
        # jeżeli jesteś w środku, broń się
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # jeżeli wokół są przeciwnicy, atakuj
        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                if rg.dist(poz, self.location) <= 1:
                    return ['attack', poz]

        # idź do środka planszy
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
