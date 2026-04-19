from PyQt6.QtWidgets import QTableView, QPushButton
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QDialogButtonBox
from PyQt6.QtWidgets import QLabel, QLineEdit
from PyQt6.QtWidgets import QGridLayout


class UiWidget(object):
    """ Klasa definiująca GUI """

    def __init__(self):
        # tabelaryczny widok danych
        self.widok = QTableView()

        # przyciski Push ###
        self.loguj_btn = QPushButton("Za&loguj")
        self.koniec_btn = QPushButton("&Koniec")

        # układ przycisków Push ###
        uklad = QHBoxLayout()
        uklad.addWidget(self.loguj_btn)
        uklad.addWidget(self.koniec_btn)

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
        super().__init__()

        # etykiety, pola edycyjne i przyciski ###
        login_lbl = QLabel('Login')
        haslo_lbl = QLabel('Hasło')
        self.login = QLineEdit()
        self.haslo = QLineEdit()
        self.haslo.setEchoMode(QLineEdit.EchoMode.Password)
        self.przyciski = QDialogButtonBox(
            (QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel))

        # układ główny ###
        uklad = QGridLayout(self)
        uklad.addWidget(login_lbl, 0, 0)
        uklad.addWidget(self.login, 0, 1)
        uklad.addWidget(haslo_lbl, 1, 0)
        uklad.addWidget(self.haslo, 1, 1)
        uklad.addWidget(self.przyciski, 2, 0, 2, 0)

        # sygnały i sloty ###
        self.przyciski.accepted.connect(self.accept)
        self.przyciski.rejected.connect(self.reject)

        # właściwości widżetu ###
        self.setModal(True)
        self.setWindowTitle('Logowanie')

    def login_haslo(self):
        return (self.login.text().strip(),
                self.haslo.text().strip())

    # metoda statyczna, tworzy dialog i zwraca (login, haslo, ok)
    @staticmethod
    def get_login_haslo(self, parent=None):
        dialog = LoginDialog(parent)
        dialog.login.setFocus()
        ok = dialog.exec()
        login, haslo = dialog.login_haslo()
        return (login, haslo, ok == QDialog.accepted)
