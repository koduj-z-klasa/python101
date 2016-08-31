#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from ksztalty import Ksztalty, Ksztalt
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

    def setupUi(self, Widget):

        # widgety rysujące kształty, instancje klasy Ksztalt
        self.ksztalt1 = Ksztalt(self, Ksztalty.Polygon)
        self.ksztalt2 = Ksztalt(self, Ksztalty.Ellipse)
        self.ksztaltAktywny = self.ksztalt1

        # przyciski CheckBox ###
        uklad = QVBoxLayout()  # układ pionowy
        self.grupaChk = QButtonGroup()
        for i, v in enumerate(('Kwadrat', 'Koło', 'Trójkąt', 'Linia')):
            self.chk = QCheckBox(v)
            self.grupaChk.addButton(self.chk, i)
            uklad.addWidget(self.chk)
        self.grupaChk.buttons()[self.ksztaltAktywny.ksztalt].setChecked(True)
        # CheckBox do wyboru aktywnego kształtu
        self.ksztaltChk = QCheckBox('<=')
        self.ksztaltChk.setChecked(True)
        uklad.addWidget(self.ksztaltChk)

        # układ poziomy dla kształtów oraz przycisków CheckBox
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

        # przyciski RadioButton ###
        self.ukladR = QHBoxLayout()
        for v in ('R', 'G', 'B'):
            self.radio = QRadioButton(v)
            self.ukladR.addWidget(self.radio)
        self.ukladR.itemAt(0).widget().setChecked(True)
        # grupujemy przyciski
        self.grupaRBtn = QGroupBox('Opcje RGB')
        self.grupaRBtn.setLayout(self.ukladR)
        self.grupaRBtn.setObjectName('Radio')
        self.grupaRBtn.setCheckable(True)
        # układ poziomy dla grupy Radio
        ukladH3 = QHBoxLayout()
        ukladH3.addWidget(self.grupaRBtn)
        # koniec RadioButton ###

        # Lista ComboBox i SpinBox ###
        self.listaRGB = QComboBox(self)
        for v in ('R', 'G', 'B'):
            self.listaRGB.addItem(v)
        self.listaRGB.setEnabled(False)
        # SpinBox
        self.spinRGB = QSpinBox()
        self.spinRGB.setMinimum(0)
        self.spinRGB.setMaximum(255)
        self.spinRGB.setEnabled(False)
        # układ pionowy dla ComboBox i SpinBox
        uklad = QVBoxLayout()
        uklad.addWidget(self.listaRGB)
        uklad.addWidget(self.spinRGB)
        # do układu poziomego grupy Radio dodajemy układ ComboBox i SpinBox
        ukladH3.insertSpacing(1, 25)
        ukladH3.addLayout(uklad)
        # koniec ComboBox i SpinBox ###

        # przyciski PushButton ###
        uklad = QHBoxLayout()
        self.grupaP = QButtonGroup()
        self.grupaP.setExclusive(False)
        for v in ('R', 'G', 'B'):
            self.btn = QPushButton(v)
            self.btn.setCheckable(True)
            self.grupaP.addButton(self.btn)
            uklad.addWidget(self.btn)
        # grupujemy przyciski
        self.grupaPBtn = QGroupBox('Przyciski RGB')
        self.grupaPBtn.setLayout(uklad)
        self.grupaPBtn.setObjectName('Push')
        self.grupaPBtn.setCheckable(True)
        self.grupaPBtn.setChecked(False)
        # koniec PushButton ###

        # etykiety QLabel i pola QLineEdit ###
        ukladH4 = QHBoxLayout()
        self.labelR = QLabel('R')
        self.labelG = QLabel('G')
        self.labelB = QLabel('B')
        self.kolorR = QLineEdit('0')
        self.kolorG = QLineEdit('0')
        self.kolorB = QLineEdit('0')
        self.kolorG.setEnabled(False)
        self.kolorB.setEnabled(False)
        for v in ('R', 'G', 'B'):
            label = getattr(self, 'label'+v)
            kolor = getattr(self, 'kolor'+v)
            ukladH4.addWidget(label)
            ukladH4.addWidget(kolor)
            kolor.setMaxLength(3)
        # koniec QLabel i QLineEdit ###

        # główny układ okna, wertykalny ###
        ukladOkna = QVBoxLayout()
        ukladOkna.addLayout(ukladH1)
        ukladOkna.addWidget(ukladH2)
        ukladOkna.addLayout(ukladH3)
        ukladOkna.addWidget(self.grupaPBtn)
        ukladOkna.addLayout(ukladH4)

        self.setLayout(ukladOkna)  # przypisanie układu do okna głównego
        self.setWindowTitle('Widżety')
        self.resize(200, 250)
