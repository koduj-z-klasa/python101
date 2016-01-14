#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from gui_z6 import Ui_Widget
from PyQt5.QtGui import QColor


class Widgety(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Widgety, self).__init__(parent)
        self.setupUi(self)

        # sygnały i sloty
        self.grupaChk.buttonClicked[int].connect(self.ustawKsztalt)
        self.ksztaltChk.clicked.connect(self.aktywujKsztalt)
        self.slajder.valueChanged.connect(self.zmienKolor)
        self.grupaRBtn.clicked.connect(self.ustawStan)
        self.listaRGB.activated[str].connect(self.ustawKanal)
        self.spinRGB.valueChanged[int].connect(self.zmienKolor)
        self.grupaPBtn.clicked.connect(self.ustawStan)
        self.kolorR.textEdited.connect(self.zmienKolor)
        self.kolorG.textEdited.connect(self.zmienKolor)
        self.kolorB.textEdited.connect(self.zmienKolor)

        # ustawienia
        self.ksztalt1.ustawKolorW(QColor(200, 30, 40))
        self.ksztalt2.ustawKolorW(QColor(34, 76, 189))
        self.grupaChk.buttons()[self.ksztalt.ksztalt].setChecked(True)

    def ustawKsztalt(self, ksztalt):
        self.ksztalt.ustawKsztalt(ksztalt)

    def aktywujKsztalt(self, wartosc):
        nadawca = self.sender()
        if wartosc:
            self.ksztalt = self.ksztalt1
            nadawca.setText("<=")
        else:
            self.ksztalt = self.ksztalt2
            nadawca.setText("=>")
        self.grupaChk.buttons()[self.ksztalt.ksztalt].setChecked(True)

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

        self.ksztalt.ustawKolorW(self.kolorW)
        self.info()

    def ustawKanal(self, wartosc):
        self.kanaly = set()  # resetujemy zbiór kanałów
        try:  # ComboBox
            if len(wartosc) == 1:
                self.kanaly.add(wartosc)
        except TypeError:  # RadioButton
            nadawca = self.sender()
            if wartosc:
                self.kanaly.add(nadawca.text())
        self.info()

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
        self.info()

    def ustawKanal2(self, wartosc):
        nadawca = self.sender()
        if wartosc:
            self.kanaly.add(nadawca.text())
        else:
            self.kanaly.remove(nadawca.text())
        self.info()

    def info(self):
        fontB = "QWidget { font-weight: bold }"
        fontN = "QWidget { font-weight: normal }"

        for k in ('R', 'G', 'B'):
            label = getattr(self, 'label'+k)
            kolor = getattr(self, 'kolor'+k)
            if k in self.kanaly:
                label.setStyleSheet(fontB)
                kolor.setEnabled(True)
            else:
                label.setStyleSheet(fontN)
                kolor.setEnabled(False)
  
        self.kolorR.setText(str(self.kolorW.red()))
        self.kolorG.setText(str(self.kolorW.green()))
        self.kolorB.setText(str(self.kolorW.blue()))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()

    sys.exit(app.exec_())
