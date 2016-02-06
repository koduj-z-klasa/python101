#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from gui import Ui_Widget


class Zadania(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Zadania, self).__init__(parent)
        self.setupUi(self)

        self.logujBtn.clicked.connect(self.loguj)
        self.koniecBtn.clicked.connect(self.koniec)

    def loguj(self):
        login, ok = QInputDialog.getText(self, 'Logowanie', 'Podaj login:')
        if ok:
            haslo, ok = QInputDialog.getText(self, 'Logowanie', 'Podaj haslo:')
            if ok:
                if not login or not haslo:
                    QMessageBox.warning(
                        self, 'Błąd', 'Pusty login lub hasło!', QMessageBox.Ok)
                    return
                QMessageBox.information(
                    self, 'Dane logowania',
                    'Podano: ' + login + ' ' + haslo, QMessageBox.Ok)

    def koniec(self):
        self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Zadania()
    okno.show()
    okno.move(350, 200)
    sys.exit(app.exec_())
