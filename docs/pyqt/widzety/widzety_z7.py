#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from gui_z7 import Ui_Widget
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
            self.ukladR.itemAt(i).widget().toggled.connect(self.ustawKanal)
        self.suwak.valueChanged.connect(self.zmienKolor)
        # Lista ComboBox i SpinBox ###
        self.grupaRBtn.clicked.connect(self.ustawStan)
        self.listaRGB.activated[str].connect(self.ustawKanal)
        self.spinRGB.valueChanged[int].connect(self.zmienKolor)
        # przyciski PushButton ###
        for btn in self.grupaP.buttons():
            btn.clicked[bool].connect(self.ustawKanalPBtn)
        self.grupaPBtn.clicked.connect(self.ustawStan)
        # etykiety QLabel i pola QEditLine ###
        for v in ('R', 'G', 'B'):
            kolor = getattr(self, 'kolor' + v)
            kolor.textEdited.connect(self.zmienKolor)

    def info(self):
        fontB = "QWidget { font-weight: bold }"
        fontN = "QWidget { font-weight: normal }"

        for v in ('R', 'G', 'B'):
            label = getattr(self, 'label' + v)
            kolor = getattr(self, 'kolor' + v)
            if v in self.kanaly:
                label.setStyleSheet(fontB)
                kolor.setEnabled(True)
            else:
                label.setStyleSheet(fontN)
                kolor.setEnabled(False)

        self.kolorR.setText(str(self.kolorW.red()))
        self.kolorG.setText(str(self.kolorW.green()))
        self.kolorB.setText(str(self.kolorW.blue()))

    def ustawKanalPBtn(self, wartosc):
        nadawca = self.sender()
        kolor = getattr(self, 'kolor' + nadawca.text())
        if wartosc:
            self.kanaly.add(nadawca.text())
            kolor.setEnabled(True)
        else:
            self.kanaly.remove(nadawca.text())
            kolor.setEnabled(False)

    def ustawStan(self, wartosc):
        if wartosc:
            self.listaRGB.setEnabled(False)
            self.spinRGB.setEnabled(False)
            nadawca = self.sender()
            if nadawca.objectName() == 'Radio':
                self.grupaPBtn.setChecked(False)
            if nadawca.objectName() == 'Push':
                self.grupaRBtn.setChecked(False)
                for btn in self.grupaP.buttons():
                    btn.setChecked(False)
                    if btn.text() in self.kanaly:
                        btn.setChecked(True)
        else:
            self.listaRGB.setEnabled(True)
            self.spinRGB.setEnabled(True)
            self.kanaly = set()
            self.kanaly.add(self.listaRGB.currentText())

    def ustawKanal(self, wartosc):
        self.kanaly = set()  # resetujemy zbiór kanałów
        try:  # ComboBox
            if len(wartosc) == 1:
                self.kanaly.add(wartosc)
        except TypeError:  # RadioButton
            nadawca = self.sender()
            if wartosc:
                self.kanaly.add(nadawca.text())

    def zmienKolor(self, wartosc):
        try:
            wartosc = int(wartosc)
        except ValueError:
            wartosc = 0
        if wartosc > 255:
            wartosc = 255

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
        self.info()

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
