#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from gui_z5 import Ui_Widget
from PyQt5.QtGui import QColor


class Widgety(QWidget, Ui_Widget):
    """ Główna klasa aplikacji """

    kanaly = {'R'}  # zbiór kanałów
    kolorW = QColor(0, 0, 0)  # kolor RGB kształtu 1

    def __init__(self, parent=None):
        super(Widgety, self).__init__(parent)
        self.setupUi(self)  # tworzenie interfejsu

        # Sygnały i sloty ###
        # przyciski CheckBox ###
        self.grupaChk.buttonClicked[int].connect(self.ustawKsztalt)
        self.ksztaltChk.clicked.connect(self.aktywujKsztalt)
        # Slider + przyciski RadioButton ###
        for i in range(self.ukladR.count()):
            self.ukladR.itemAt(i).widget().toggled.connect(self.ustawKanalRBtn)
        self.suwak.valueChanged.connect(self.zmienKolor)
        # Lista ComboBox i SpinBox ###
        self.grupaRBtn.clicked.connect(self.ustawStan)
        self.listaRGB.activated[str].connect(self.ustawKanalCBox)
        self.spinRGB.valueChanged[int].connect(self.zmienKolor)
        # przyciski PushButton ###
        for btn in self.grupaP.buttons():
            btn.clicked[bool].connect(self.ustawKanalPBtn)
        self.grupaPBtn.clicked.connect(self.ustawStan)

    def ustawKanalPBtn(self, wartosc):
        nadawca = self.sender()
        if wartosc:
            self.kanaly.add(nadawca.text())
        elif wartosc in self.kanaly:
            self.kanaly.remove(nadawca.text())

    def ustawStan(self, wartosc):
        if wartosc:
            self.listaRGB.setEnabled(False)
            self.spinRGB.setEnabled(False)
        else:
            self.listaRGB.setEnabled(True)
            self.spinRGB.setEnabled(True)
            self.kanaly = set()
            self.kanaly.add(self.listaRGB.currentText())

    def ustawKanalCBox(self, wartosc):
        self.kanaly = set()  # resetujemy zbiór kanałów
        self.kanaly.add(wartosc)

    def ustawKanalRBtn(self, wartosc):
        self.kanaly = set()  # resetujemy zbiór kanałów
        nadawca = self.sender()
        if wartosc:
            self.kanaly.add(nadawca.text())

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
