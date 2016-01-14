#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ksztalty import Ksztalty, Ksztalt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtWidgets import QCheckBox, QButtonGroup, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider, QLCDNumber, QSplitter
from PyQt5.QtWidgets import QRadioButton, QGroupBox
from PyQt5.QtWidgets import QComboBox, QSpinBox


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

        # główny układ okna, wertykalny ###
        ukladOkna = QVBoxLayout()
        ukladOkna.addLayout(ukladH1)
        ukladOkna.addWidget(ukladH2)
        ukladOkna.addLayout(ukladH3)

        self.setLayout(ukladOkna)  # przypisanie układu do okna głównego
        self.setWindowTitle("Widgety")


class Ksztalty:
    """ Klasa pomocnicza, symuluje typ wyliczeniowy """
    Rect, Ellipse, Polygon, Line = range(4)


class Ksztalt(QWidget):
    """ Klasa definiująca widget do rysowania kształtów """
    # współrzędne prostokąta i trójkąta
    prost = QRect(1, 1, 100, 100)
    punkty = QPolygon([
        QPoint(1, 101),  # punkt początkowy (x, y)
        QPoint(51, 1),
        QPoint(101, 101)])

    def __init__(self, parent, ksztalt=Ksztalty.Rect):
        super(Ksztalt, self).__init__(parent)

        # kształt do narysowania
        self.ksztalt = ksztalt
        # kolor obramowania i wypełnienia w formacie RGB
        self.kolorO = QColor(0, 0, 0)
        self.kolorW = QColor(255, 255, 255)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.rysujFigury(qp)
        qp.end()

    def rysujFigury(self, qp):
        qp.setPen(self.kolorO)  # kolor obramowania
        qp.setBrush(self.kolorW)  # kolor wypełnienia
        qp.setRenderHint(QPainter.Antialiasing)  # wygładzanie kształtu

        if self.ksztalt == Ksztalty.Rect:
            qp.drawRect(self.prost)
        elif self.ksztalt == Ksztalty.Ellipse:
            qp.drawEllipse(self.prost)
        elif self.ksztalt == Ksztalty.Polygon:
            qp.drawPolygon(self.punkty)
        elif self.ksztalt == Ksztalty.Line:
            qp.drawLine(self.prost.topLeft(), self.prost.bottomRight())
        else:  # kształt domyślny Rect
            qp.drawRect(self.prost)

    def sizeHint(self):
        return QSize(102, 102)

    def minimumSizeHint(self):
        return QSize(102, 102)

    def ustawKsztalt(self, ksztalt):
        self.ksztalt = ksztalt
        self.update()

    def ustawKolorW(self, kolor):
        self.kolorW = kolor
        self.update()
