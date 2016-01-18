#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ksztalty import Ksztalty, Ksztalt
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QCheckBox, QButtonGroup, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider, QLCDNumber, QSplitter
from PyQt5.QtWidgets import QRadioButton, QGroupBox


class Ui_Widget(object):
    """ Klasa definiująca GUI """

    def setupUi(self, Widget):

        # widgety rysujące kształty, instancje klasy Ksztalt
        self.ksztalt1 = Ksztalt(self, Ksztalty.Polygon)
        self.ksztalt2 = Ksztalt(self, Ksztalty.Ellipse)

        # przyciski CheckBox ###
        uklad = QVBoxLayout()  # układ pionowy
        self.grupaChk = QButtonGroup()
        for i, v in enumerate(('Kwadrat', 'Koło', 'Trójkąt', 'Linia')):
            self.chk = QCheckBox(v)
            self.grupaChk.addButton(self.chk, i)
            uklad.addWidget(self.chk)
        # CheckBox do wyboru aktywnego kształtu
        self.ksztaltChk = QCheckBox("<=")
        uklad.addWidget(self.ksztaltChk)

        # układ poziomy dla kształtów oraz przycisków Chk
        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(self.ksztalt1)
        ukladH1.addLayout(uklad)
        ukladH1.addWidget(self.ksztalt2)
        # koniec CheckBox ###

        # Slider i LCDNumber ###
        self.suwak = QSlider(Qt.Horizontal)
        self.suwak.setMinimum(0)
        self.suwak.setMaximum(255)
        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        # układ poziomy (splitter) dla slajdera i lcd
        ukladH2 = QSplitter(Qt.Horizontal, self)
        ukladH2.addWidget(self.suwak)
        ukladH2.addWidget(self.lcd)
        ukladH2.setSizes((125, 75))

        # pomocnicza tupla z oznaczeniami kolorów
        self.kolory = ('R', 'G', 'B')

        # przyciski RadioButton ###
        self.ukladR = QHBoxLayout()
        for v in self.kolory:
            self.radio = QRadioButton(v)
            self.ukladR.addWidget(self.radio)
        # grupujemy przyciski
        self.grupaRBtn = QGroupBox("Opcje RGB")
        self.grupaRBtn.setLayout(self.ukladR)
        self.grupaRBtn.setObjectName("Radio")
        # układ poziomy dla grupy Radio
        ukladH3 = QHBoxLayout()
        ukladH3.addWidget(self.grupaRBtn)
        # koniec RadioButton ###

        # główny układ okna, pionowy ###
        ukladOkna = QVBoxLayout()
        ukladOkna.addLayout(ukladH1)
        ukladOkna.addWidget(ukladH2)
        ukladOkna.addLayout(ukladH3)

        self.setLayout(ukladOkna)  # przypisanie układu do okna głównego
        self.setWindowTitle("Widgety")
