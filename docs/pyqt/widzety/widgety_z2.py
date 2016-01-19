#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from gui_z2 import Ui_Widget


class Widgety(QWidget, Ui_Widget):
    """ Główna klasa aplikacji """

    def __init__(self, parent=None):
        super(Widgety, self).__init__(parent)
        self.setupUi(self)  # tworzenie interfejsu

        # Sygnały i sloty ###
        # przyciski CheckBox ###
        self.grupaChk.buttonClicked[int].connect(self.ustawKsztalt)
        self.ksztaltChk.clicked.connect(self.aktywujKsztalt)

    def ustawKsztalt(self, wartosc):
        self.ksztaltAktywny.ustawKsztalt(wartosc)

    def aktywujKsztalt(self, wartosc):
        nadawca = self.sender()
        if wartosc:
            self.ksztaltAktywny = self.ksztalt1
            nadawca.setText('<=')
        else:
            self.ksztaltAktywny = self.ksztalt2
            nadawca.setText('=>')
        self.grupaChk.buttons()[self.ksztaltAktywny.ksztalt].setChecked(True)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()

    sys.exit(app.exec_())
