from ksztalty import Ksztalty, Ksztalt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QCheckBox, QButtonGroup


class UiWidget:
    """ Klasa definiująca GUI """

    def __init__(self):

        # widget definiujący kształt, instancja klasy Ksztalt
        self.ksztalt1 = Ksztalt(None, Ksztalty.RECT)
        self.ksztalt2 = Ksztalt(None, Ksztalty.ELLIPSE)
        self.ksztalt_aktywny = self.ksztalt1

        # przyciski CheckBox
        uklad_chk = QVBoxLayout()  # układ pionowy
        self.grupa_chk = QButtonGroup()
        for i, v in enumerate(('Kwadrat', 'Koło', 'Trójkąt', 'Linia')):
            self.chk = QCheckBox(v)
            self.grupa_chk.addButton(self.chk, i)
            uklad_chk.addWidget(self.chk)
        przyciski = self.grupa_chk.buttons()
        przyciski[self.ksztalt_aktywny.ksztalt].setChecked(True)

        # przycisk CheckBox do wyboru aktywnego kształtu
        self.ksztalt_chk = QCheckBox('<=')
        self.ksztalt_chk.setChecked(True)
        uklad_chk.addWidget(self.ksztalt_chk)

        # układ poziomy dla kształtów oraz przycisków CheckBox
        uklad_h1 = QHBoxLayout()
        uklad_h1.addWidget(self.ksztalt1)
        uklad_h1.addLayout(uklad_chk)
        uklad_h1.addWidget(self.ksztalt2)
        # koniec CheckBox

        # główny układ okna, pionowy
        uklad_okna = QVBoxLayout()
        uklad_okna.addLayout(uklad_h1)

        # ustawienie głównego układu okna
        self.setLayout(uklad_okna)
