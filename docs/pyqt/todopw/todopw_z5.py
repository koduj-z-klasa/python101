#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from gui_z5 import Ui_Widget, LoginDialog
import baza_z5 as baza
from tabmodel_z5 import TabModel


class Zadania(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Zadania, self).__init__(parent)
        self.setupUi(self)

        self.logujBtn.clicked.connect(self.loguj)
        self.koniecBtn.clicked.connect(self.koniec)
        self.dodajBtn.clicked.connect(self.dodaj)

    def dodaj(self):
        """ Dodawanie nowego zadania """
        zadanie, ok = QInputDialog.getMultiLineText(self,
                                                    'Zadanie',
                                                    'Co jest do zrobienia?')
        if not ok or not zadanie.strip():
            QMessageBox.critical(self,
                                 'Błąd',
                                 'Zadanie nie może być puste.',
                                 QMessageBox.Ok)
            return

        zadanie = baza.dodajZadanie(self.osoba, zadanie)
        model.tabela.append(zadanie)
        model.layoutChanged.emit()  # wyemituj sygnał: zaszła zmiana!
        if len(model.tabela) == 1:  # jeżeli to pierwsze zadanie
            self.odswiezWidok()     # trzeba przekazać model do widoku

    def loguj(self):
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
        self.dodajBtn.setEnabled(True)

    def odswiezWidok(self):
        self.widok.setModel(model)  # przekazanie modelu do widoku
        self.widok.hideColumn(0)  # ukrywamy kolumnę id
        # ograniczenie szerokości ostatniej kolumny
        self.widok.horizontalHeader().setStretchLastSection(True)
        # dopasowanie szerokości kolumn do zawartości
        self.widok.resizeColumnsToContents()

    def koniec(self):
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    baza.polacz()
    model = TabModel(baza.pola)
    okno = Zadania()
    okno.show()
    okno.move(350, 200)
    sys.exit(app.exec_())
