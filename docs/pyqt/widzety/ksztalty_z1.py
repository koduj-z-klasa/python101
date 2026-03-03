from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPolygon
from PyQt6.QtCore import QRect, QPoint, QSize
from enum import Enum


class Ksztalty(Enum):
    """ Klasa pomocnicza, symuluje typ wyliczeniowy """
    RECT, ELLIPSE, POLYGON, LINE = range(4)


class Ksztalt(QWidget):
    """ Klasa definiująca widget do rysowania kształtów """
    # współrzędne prostokąta i trójkąta
    prost = QRect(1, 1, 101, 101)
    punkty = QPolygon([
        QPoint(1, 101),  # punkt początkowy (x, y)
        QPoint(51, 1),
        QPoint(101, 101)])

    def __init__(self, parent, ksztalt=Ksztalty.RECT):
        super().__init__(parent)

        # kształt do narysowania
        self.ksztalt = ksztalt

        # kolor obramowania i wypełnienia w formacie RGB
        self.kolor_o = QColor(0, 0, 0)
        self.kolor_w = QColor(255, 255, 255)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.rysuj_figury(qp)
        qp.end()

    def rysuj_figury(self, qp):
        qp.setPen(self.kolor_o)  # kolor obramowania
        qp.setBrush(self.kolor_w)  # kolor wypełnienia
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)  # wygładzanie kształtu

        if self.ksztalt == Ksztalty.RECT:
            qp.drawRect(self.prost)
        elif self.ksztalt == Ksztalty.ELLIPSE:
            qp.drawEllipse(self.prost)
        elif self.ksztalt == Ksztalty.LINE:
            qp.drawLine(self.prost.topLeft(), self.prost.bottomRight())
        elif self.ksztalt == Ksztalty.POLYGON:
            qp.drawPolygon(self.punkty)

    def minimumSizeHint(self):
        return QSize(102, 102)

    def ustaw_ksztalt(self, ksztalt):
        self.ksztalt = ksztalt
        self.update()

    def ustaw_kolor_w(self, r=0, g=0, b=0):
        self.kolorW = QColor(r, g, b)
        self.update()
