from PyQt6.QtWidgets import QTableView, QPushButton
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout


class UiWidget:
    """ Klasa definiująca GUI """

    def __init__(self):
        # tabelaryczny widok danych
        self.widok = QTableView()

        # przyciski Push ###
        self.loguj_btn = QPushButton("Za&loguj")
        self.koniec_btn = QPushButton("&Koniec")

        # układ przycisków Push ###
        uklad = QHBoxLayout()
        uklad.addWidget(self.loguj_btn)
        uklad.addWidget(self.koniec_btn)

        # główny układ okna ###
        ukladV = QVBoxLayout(self)
        ukladV.addWidget(self.widok)
        ukladV.addLayout(uklad)

        # właściwości widżetu ###
        self.setWindowTitle("Prosta lista zadań")
        self.resize(500, 300)
