#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from widgety_gui import Ui_Widget
from PyQt5.QtGui import QColor


class Widgety(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Widgety, self).__init__(parent)
        self.setupUi(self)

        self.kanaly = {'R'}  # zbiór kanałów
        self.kolor = QColor(0, 0, 0)  # kolor RGB

        self.grupaRBtn.clicked.connect(self.ustawStan)
        self.grupaPBtn.clicked.connect(self.ustawStan)

        self.slajder.valueChanged.connect(self.zmienKolor)
        self.spinRGB.valueChanged[int].connect(self.zmienKolor)

        self.komboRGB.activated[str].connect(self.ustawKanal)
        self.grupaChk.buttonClicked[int].connect(self.ustawKsztalt)

        self.btnR.clicked[bool].connect(self.ustawKanal)
        self.btnG.clicked[bool].connect(self.ustawKanal)
        self.btnB.clicked[bool].connect(self.ustawKanal)

    def ustawKanal(self, wartosc):
        self.kanaly = set()
        try:
            # ComboBox
            if len(wartosc) == 1:
                self.kanaly.add(wartosc)
        except TypeError:
            # RadioButton
            nadawca = self.sender()
            if wartosc:
                self.kanaly.add(nadawca.text())
            print(self.kanaly)

    def ustawKanal2(self, pressed):
        nadawca = self.sender()
        if pressed:
            self.kanaly.add(nadawca.text())
        else:
            self.kanaly.remove(nadawca.text())

    def zmienKolor(self, wartosc):
        self.lcd.display(wartosc)
        if 'R' in self.kanaly:
            self.kolor.setRed(wartosc)
        if 'G' in self.kanaly:
            self.kolor.setGreen(wartosc)
        if 'B' in self.kanaly:
            self.kolor.setBlue(wartosc)

        kolorTxt = 'R: ' + str(self.kolor.red())
        kolorTxt += '  G: ' + str(self.kolor.green())
        kolorTxt += '  B: ' + str(self.kolor.blue())
        self.kolorLbl.setText(kolorTxt)

        self.ksztalt.ustawKolorW(self.kolor)

    def ustawStan(self, wartosc):
        if wartosc:
            self.komboRGB.setEnabled(False)
            self.spinRGB.setEnabled(False)
            nadawca = self.sender()
            if nadawca.objectName() == 'Radio':
                self.grupaPBtn.setChecked(False)
                self.btnR.setChecked(False)
                self.btnG.setChecked(False)
                self.btnB.setChecked(False)
            if nadawca.objectName() == 'Push':
                self.grupaRBtn.setChecked(False)
                if 'R' in self.kanaly:
                    self.btnR.setChecked(True)
                elif 'G' in self.kanaly:
                    self.btnG.setChecked(True)
                elif 'B' in self.kanaly:
                    self.btnB.setChecked(True)
        else:
            self.komboRGB.setEnabled(True)
            self.spinRGB.setEnabled(True)




    def ustawKsztalt(self, id):
        if id == 2:
            self.ksztalt.ustawKsztalt('Ellipse')
        elif id == 3:
            self.ksztalt.ustawKsztalt('Triangle')
        else:
            self.ksztalt.ustawKsztalt('Rect')

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()

    sys.exit(app.exec_())
