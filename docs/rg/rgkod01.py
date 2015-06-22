#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg

class Robot:

    def act(self, game):

        # idź do środka planszy, ruch domyślny
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
