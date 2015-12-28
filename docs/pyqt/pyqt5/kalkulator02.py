#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout


class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        # etykiety
        self.label1 = QLabel("Liczba 1:")
        self.label2 = QLabel("Liczba 2:")
        self.label3 = QLabel("Wynik:")

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(self.label1, 0, 0)
        ukladT.addWidget(self.label2, 0, 1)
        ukladT.addWidget(self.label3, 0, 2)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Prosty kalkulator")
        self.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())
