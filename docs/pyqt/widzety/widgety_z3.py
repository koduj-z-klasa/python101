#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from gui_z3 import Ui_Widget
from PyQt5.QtGui import QColor


class Widgety(QWidget, Ui_Widget):
    """ Główna klasa aplikacji """

    kanaly = {'R'}  # zbiór kanałów
    kolorW = QColor(0, 0, 0)  # kolor RGB kształtu 1

    def __init__(self, parent=None):
        super(Widgety, self).__init__(parent)
        self.setupUi(self)  # tworzenie interfejsu

        # ustawienia, sygnały i sloty
        # przyciski CheckBox ###
        self.ksztaltChk.setChecked(True)
        self.ksztaltAktywny = self.ksztalt1
        self.grupaChk.buttons()[self.ksztaltAktywny.ksztalt].setChecked(True)
        self.grupaChk.buttonClicked[int].connect(self.ustawKsztalt)
        self.ksztaltChk.clicked.connect(self.aktywujKsztalt)
        # Slider + Radio Buttons ###
        self.grupaRBtn.setCheckable(True)
        self.ukladR.itemAt(0).widget().setChecked(True)
        self.suwak.valueChanged.connect(self.zmienKolor)
        for i in range(self.ukladR.count()):
            self.ukladR.itemAt(i).widget().toggled.connect(self.ustawKanal)

    def zmienKolor(self, wartosc):
        self.lcd.display(wartosc)
        if 'R' in self.kanaly:
            self.kolorW.setRed(wartosc)
        if 'G' in self.kanaly:
            self.kolorW.setGreen(wartosc)
        if 'B' in self.kanaly:
            self.kolorW.setBlue(wartosc)

        self.ksztaltAktywny.ustawKolorW(
            self.kolorW.red(),
            self.kolorW.green(),
            self.kolorW.blue())

    def ustawKanal(self, wartosc):
        self.kanaly = set()  # resetujemy zbiór kanałów
        nadawca = self.sender()
        if wartosc:
            self.kanaly.add(nadawca.text())

    def ustawKsztalt(self, wartosc):
        self.ksztaltAktywny.ustawKsztalt(wartosc)

    def aktywujKsztalt(self, wartosc):
        nadawca = self.sender()
        if wartosc:
            self.ksztaltAktywny = self.ksztalt1
            nadawca.setText("<=")
        else:
            self.ksztaltAktywny = self.ksztalt2
            nadawca.setText("=>")

        self.grupaChk.buttons()[self.ksztaltAktywny.ksztalt].setChecked(True)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()

    sys.exit(app.exec_())
