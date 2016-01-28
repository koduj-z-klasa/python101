# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout


class Ui_Widget(object):

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")

        # tabelaryczny widok danych
        self.widok = QTableView()

        # przyciski Push ###
        self.logujBtn = QPushButton("Za&loguj")
        self.koniecBtn = QPushButton("&Koniec")

        # układ przycisków Push ###
        uklad = QHBoxLayout()
        uklad.addWidget(self.logujBtn)
        uklad.addWidget(self.koniecBtn)

        # główny układ okna ###
        ukladV = QVBoxLayout(self)
        ukladV.addWidget(self.widok)
        ukladV.addLayout(uklad)

        # właściwości widżetu ###
        self.setWindowTitle("Prosta lista zadań")
        self.resize(500, 300)
