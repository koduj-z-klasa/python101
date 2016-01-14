#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from gui_z2 import Ui_Widget
from PyQt5.QtGui import QColor


class Widgety(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Widgety, self).__init__(parent)
        self.setupUi(self)

        # sygnały i sloty
        self.grupaChk.buttonClicked[int].connect(self.ustawKsztalt)
        self.ksztaltChk.clicked.connect(self.aktywujKsztalt)

        # ustawienia
        self.ksztalt1.ustawKolorW(QColor(200, 30, 40))
        self.ksztalt2.ustawKolorW(QColor(34, 76, 189))
        self.grupaChk.buttons()[self.ksztalt.ksztalt].setChecked(True)

    def ustawKsztalt(self, wartosc):
        self.ksztalt.ustawKsztalt(wartosc)

    def aktywujKsztalt(self, wartosc):
        nadawca = self.sender()
        if wartosc:
            self.ksztalt = self.ksztalt1
            nadawca.setText("<=")
        else:
            self.ksztalt = self.ksztalt2
            nadawca.setText("=>")
        self.grupaChk.buttons()[self.ksztalt.ksztalt].setChecked(True)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()

    sys.exit(app.exec_())
