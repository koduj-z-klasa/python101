#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from gui_z3 import Ui_Widget, LoginDialog
import baza_z3 as baza
from tabmodel_z3 import TabModel


class Zadania(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Zadania, self).__init__(parent)
        self.setupUi(self)

        self.logujBtn.clicked.connect(self.loguj)
        self.koniecBtn.clicked.connect(self.koniec)

    def loguj(self):
        """ Logowanie użytkownika """
        login, haslo, ok = LoginDialog.getLoginHaslo(self)
        if not ok:
            return

        if not login or not haslo:
            QMessageBox.warning(self, 'Błąd',
                                'Pusty login lub hasło!', QMessageBox.Ok)
            return

        self.osoba = baza.loguj(login, haslo)
        if self.osoba is None:
            QMessageBox.critical(self, 'Błąd', 'Błędne hasło!', QMessageBox.Ok)
            return

        zadania = baza.czytajDane(self.osoba)
        model.aktualizuj(zadania)
        model.layoutChanged.emit()
        self.odswiezWidok()

    def odswiezWidok(self):
        self.widok.setModel(model)  # przekazanie modelu do widoku

    def koniec(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    baza.polacz()
    model = TabModel()
    okno = Zadania()
    okno.show()
    okno.move(350, 200)
    sys.exit(app.exec_())
