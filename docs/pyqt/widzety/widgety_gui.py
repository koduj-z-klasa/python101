#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QGroupBox, QButtonGroup
from PyQt5.QtWidgets import QRadioButton, QComboBox, QSpinBox, QCheckBox
from PyQt5.QtWidgets import QSlider, QLCDNumber
from PyQt5.QtWidgets import QSplitter, QVBoxLayout
from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtWidgets import QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPolygon


class Ui_Widget(object):

    def setupUi(self, Widget):
        Widget.setObjectName("Widgety")

        self.kolory = ('R', 'G', 'B')

        # grupa przyciksów radio
        ukladR = QHBoxLayout()
        for kolor in self.kolory:
            self.radio = QRadioButton(kolor)
            if kolor == 'R':
                self.radio.setChecked(True)
            ukladR.addWidget(self.radio)
            self.radio.toggled.connect(self.ustawKanal)

        self.grupaRBtn = QGroupBox("Opcje RGB")
        self.grupaRBtn.setObjectName('Radio')
        self.grupaRBtn.setCheckable(True)
        self.grupaRBtn.setLayout(ukladR)

        # lista rozwijalna ComboBox
        self.komboRGB = QComboBox(self)
        for kolor in self.kolory:
            self.komboRGB.addItem(kolor)
        self.komboRGB.setEnabled(False)

        # SpinBox
        self.spinRGB = QSpinBox()
        self.spinRGB.setMinimum(0)
        self.spinRGB.setMaximum(255)
        self.spinRGB.setEnabled(False)

        # układ wertykalny: ComboBox + SpinBox
        ukladV1 = QVBoxLayout()
        ukladV1.addWidget(self.komboRGB)
        ukladV1.addWidget(self.spinRGB)

        # układ horyzontalny: grupa Radio + ComboBox i SpinBox
        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(self.grupaRBtn)
        ukladH1.addLayout(ukladV1)

        # slajder i lcd w spliterze
        self.slajder = QSlider(Qt.Horizontal)
        self.slajder.setMinimum(0)
        self.slajder.setMaximum(255)
        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        spliter = QSplitter(Qt.Horizontal, self)
        spliter.addWidget(self.slajder)
        spliter.addWidget(self.lcd)
        spliter.setSizes((125, 75))

        # grupa przycisków push
        self.btnR = QPushButton('R')
        self.btnR.setCheckable(True)
        self.btnG = QPushButton('G')
        self.btnG.setCheckable(True)
        self.btnB = QPushButton('B')
        self.btnB.setCheckable(True)

        ukladB = QHBoxLayout()
        ukladB.addWidget(self.btnR)
        ukladB.addWidget(self.btnG)
        ukladB.addWidget(self.btnB)

        self.grupaPBtn = QGroupBox("Przyciski RGB")
        self.grupaPBtn.setObjectName('Push')
        self.grupaPBtn.setCheckable(True)
        self.grupaPBtn.setChecked(False)
        self.grupaPBtn.setLayout(ukladB)

        # grupa przycisków CheckBox
        self.kwChk = QCheckBox("Kwadrat")
        self.kwChk.setChecked(True)
        self.koChk = QCheckBox("Koło")
        self.trChk = QCheckBox("Trójkąt")
        self.grupaChk = QButtonGroup()
        self.grupaChk.addButton(self.kwChk, 1)
        self.grupaChk.addButton(self.koChk, 2)
        self.grupaChk.addButton(self.trChk, 3)
        ukladChk = QVBoxLayout()
        ukladChk.addWidget(self.kwChk)
        ukladChk.addWidget(self.koChk)
        ukladChk.addWidget(self.trChk)

        # etykieta kanałów i kolorów
        self.kolorLbl = QLabel("R: 0  G: 0  B: 0")
        ukladChk.addWidget(self.kolorLbl)

        # widget rysujący kształty, instancja klasy Ksztalt
        self.ksztalt = Ksztalt(self)

        # układ horyzontalny: kształt + przyciski CheckBox
        ukladH2 = QHBoxLayout()
        ukladH2.addWidget(self.ksztalt)
        ukladH2.addLayout(ukladChk)

        # główny układ okna, wertykalny
        ukladV = QVBoxLayout()
        ukladV.addLayout(ukladH1)
        ukladV.addWidget(self.grupaPBtn)
        ukladV.addWidget(spliter)
        ukladV.addLayout(ukladH2)
        self.setLayout(ukladV)

        self.setWindowTitle("Widgety")


class Ksztalt(QWidget):

    def __init__(self, parent, ksztalt='Rect'):
        super(Ksztalt, self).__init__(parent)

        self.ksztalt = ksztalt
        self.kolorW = QColor(0, 0, 0)

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

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.rysujFigury(qp)
        qp.end()

    def rysujFigury(self, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.setBrush(self.kolorW)
        qp.setRenderHint(QPainter.Antialiasing)

        if self.ksztalt == 'Ellipse':
            qp.drawEllipse(0, 0, 100, 100)
        elif self.ksztalt == 'Triangle':
            punkty = QPolygon([
                QPoint(0, 100),
                QPoint(50, 0),
                QPoint(100, 100)])
            qp.drawPolygon(punkty)
        else:
            qp.drawRect(0, 0, 100, 100)
