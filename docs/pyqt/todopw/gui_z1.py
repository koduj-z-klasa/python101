# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QGridLayout


class Ui_Widget(object):

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")

        # tabelaryczny widok danych
        self.widok = QTableView()

        # przyciski Push ###
        self.logujBtn = QPushButton("Za&loguj")
        self.koniecBtn = QPushButton("&Koniec")

        # układ przycisków Push ###
        uklad = QHBoxLayout()
        uklad.addWidget(self.logujBtn)
        uklad.addWidget(self.koniecBtn)

        # główny układ okna ###
        ukladV = QVBoxLayout(self)
        ukladV.addWidget(self.widok)
        ukladV.addLayout(uklad)

        # właściwości widżetu ###
        self.setWindowTitle("Prosta lista zadań")
        self.resize(500, 300)


class LoginDialog(QDialog):
    """ Okno dialogowe logowania """
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        # etykiety, pola edycyjne i przyciski ###
        loginLbl = QLabel('Login')
        hasloLbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.przyciski = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)

        # układ główny ###
        uklad = QGridLayout(self)
        uklad.addWidget(loginLbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(hasloLbl, 1, 0)
        uklad.addWidget(self.haslo, 1, 1)
        uklad.addWidget(self.przyciski, 2, 0, 2, 0)

        # sygnały i sloty ###
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Logowanie')

    def loginHaslo(self):
        return (self.login.text().strip(),
                self.haslo.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def getLoginHaslo(parent=None):
        dialog = LoginDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec_()
        dane = dialog.loginHaslo()
        return (dane[0], dane[1], ok == QDialog.Accepted)
