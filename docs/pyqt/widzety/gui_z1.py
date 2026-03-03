from ksztalty import Ksztalty, Ksztalt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout


class UiWidget:
    """ Klasa definiująca GUI """

    def __init__(self):

        # widget definiujący kształt, instancja klasy Ksztalt
        self.ksztalt1 = Ksztalt(None, Ksztalty.RECT)

        # układ poziomy dla kształtów oraz przycisków CheckBox
        uklad_h1 = QHBoxLayout()
        uklad_h1.addWidget(self.ksztalt1)

        # główny układ okna, pionowy
        uklad_okna = QVBoxLayout()
        uklad_okna.addLayout(uklad_h1)

        # ustawienie głównego układu okna
        self.setLayout(uklad_okna)
