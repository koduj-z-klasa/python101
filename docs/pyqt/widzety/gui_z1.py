#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ksztalty import Ksztalty, Ksztalt
from PyQt5.QtWidgets import QHBoxLayout


class Ui_Widget(object):
    """ Klasa definiująca GUI """

    def setupUi(self, Widget):

        # widget rysujący kształty, instancja klasy Ksztalt
        self.ksztalt = Ksztalt(self, Ksztalty.Polygon)
        self.ksztalt.ustawKolorW(200, 30, 40)

        # układ poziomy, zawiera: self.ksztalt
        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(self.ksztalt)

        self.setLayout(ukladH1)  # przypisanie układu do okna głównego
        self.setWindowTitle("Widżety")
