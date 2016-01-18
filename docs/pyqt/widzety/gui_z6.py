#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ksztalty import Ksztalty, Ksztalt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QCheckBox, QButtonGroup, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider, QLCDNumber, QSplitter
from PyQt5.QtWidgets import QRadioButton, QGroupBox
from PyQt5.QtWidgets import QComboBox, QSpinBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Ui_Widget(object):
    """ Klasa definiująca GUI """

    kolory = ('R', 'G', 'B')
    kanaly = {'R'}  # zbiór kanałów
    kolorW = QColor(0, 0, 0)  # kolor RGB kształtu

    def setupUi(self, Widget):

        # widgety rysujące kształty, instancje klasy Ksztalt
        self.ksztalt1 = Ksztalt(self, Ksztalty.Polygon)
        self.ksztalt2 = Ksztalt(self, Ksztalty.Ellipse)
        self.ksztalt = self.ksztalt1  # kształt aktywny

        # przyciski CheckBox ###
        uklad = QVBoxLayout()  # układ pionowy
        self.grupaChk = QButtonGroup()
        for i, v in enumerate(('Kwadrat', 'Koło', 'Trójkąt', 'Linia')):
            self.chk = QCheckBox(v)
            self.grupaChk.addButton(self.chk, i)
            uklad.addWidget(self.chk)
        # CheckBox do wyboru aktywnego kształtu
        self.ksztaltChk = QCheckBox("<=")
        self.ksztaltChk.setChecked(True)
        uklad.addWidget(self.ksztaltChk)

        # układ poziomy dla kształtów oraz przycisków Chk
        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(self.ksztalt1)
        ukladH1.addLayout(uklad)
        ukladH1.addWidget(self.ksztalt2)

        # slajder i lcd ###
        self.slajder = QSlider(Qt.Horizontal)
        self.slajder.setMinimum(0)
        self.slajder.setMaximum(255)
        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        # układ poziomy (splitter) dla slajdera i lcd
        ukladH2 = QSplitter(Qt.Horizontal, self)
        ukladH2.addWidget(self.slajder)
        ukladH2.addWidget(self.lcd)
        ukladH2.setSizes((125, 75))

        # przyciski RadioButton ###
        uklad = QHBoxLayout()
        for kolor in self.kolory:
            self.radio = QRadioButton(kolor)
            if kolor == 'R':
                self.radio.setChecked(True)
            uklad.addWidget(self.radio)
            self.radio.toggled.connect(self.ustawKanal)
        # grupujemy przyciski
        self.grupaRBtn = QGroupBox("Opcje RGB")
        self.grupaRBtn.setObjectName('Radio')
        self.grupaRBtn.setCheckable(True)
        self.grupaRBtn.setLayout(uklad)

        # Lista ComboBox i SpinBox ###
        self.listaRGB = QComboBox(self)
        for kolor in self.kolory:
            self.listaRGB.addItem(kolor)
        self.listaRGB.setEnabled(False)

        self.spinRGB = QSpinBox()
        self.spinRGB.setMinimum(0)
        self.spinRGB.setMaximum(255)
        self.spinRGB.setEnabled(False)

        # układ pionowy dla ComboBox i SpinBox
        uklad = QVBoxLayout()
        uklad.addWidget(self.listaRGB)
        uklad.addWidget(self.spinRGB)

        # układ poziomy dla grupy Radio, ComboBox i SpinBox
        ukladH3 = QHBoxLayout()
        ukladH3.addWidget(self.grupaRBtn)
        ukladH3.insertSpacing(1, 25)
        ukladH3.addLayout(uklad)

        # przyciski PushButton ###
        uklad = QHBoxLayout()
        self.grupaP = QButtonGroup()
        self.grupaP.setExclusive(False)
        for kolor in self.kolory:
            self.btn = QPushButton(kolor)
            self.btn.setCheckable(True)
            uklad.addWidget(self.btn)
            self.grupaP.addButton(self.btn)
            self.btn.clicked[bool].connect(self.ustawKanal2)

        self.grupaPBtn = QGroupBox("Przyciski RGB")
        self.grupaPBtn.setObjectName('Push')
        self.grupaPBtn.setCheckable(True)
        self.grupaPBtn.setChecked(False)
        self.grupaPBtn.setLayout(uklad)

        # QLabel - QLineEdit ###
        ukladH4 = QHBoxLayout()
        self.labelR = QLabel("R", self)
        self.kolorR = QLineEdit("0")
        self.labelG = QLabel("G")
        self.kolorG = QLineEdit("0")
        self.labelB = QLabel("B")
        self.kolorB = QLineEdit("0")
        for k in self.kolory:
            label = getattr(self, 'label'+k)
            kolor = getattr(self, 'kolor'+k)
            ukladH4.addWidget(label)
            ukladH4.addWidget(kolor)
            kolor.setMaxLength(3)

        # główny układ okna, wertykalny ###
        ukladOkna = QVBoxLayout()
        ukladOkna.addLayout(ukladH1)
        ukladOkna.addWidget(ukladH2)
        ukladOkna.addLayout(ukladH3)
        ukladOkna.addWidget(self.grupaPBtn)
        ukladOkna.addLayout(ukladH4)

        self.setLayout(ukladOkna)  # przypisanie układu do okna głównego
        self.setWindowTitle("Widżety")
        self.resize(200, 250)
