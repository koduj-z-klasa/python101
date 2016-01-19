# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import QPoint, QRect, QSize


class Ksztalty:
    """ Klasa pomocnicza, symuluje typ wyliczeniowy """
    Rect, Ellipse, Polygon, Line = range(4)


class Ksztalt(QWidget):
    """ Klasa definiująca widget do rysowania kształtów """
    # współrzędne prostokąta i trójkąta
    prost = QRect(1, 1, 101, 101)
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
        self.rysujFigury(e, qp)
        qp.end()

    def rysujFigury(self, e, qp):
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

    def ustawKolorW(self, r=0, g=0, b=0):
        self.kolorW = QColor(r, g, b)
        self.update()
