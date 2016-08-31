#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget


class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super(Kalkulator, self).__init__(parent)

        self.interfejs()

    def interfejs(self):

        self.resize(300, 100)
        self.setWindowTitle("Prosty kalkulator")
        self.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())
