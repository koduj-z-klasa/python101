from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QLabel, QGridLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt


class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):

        # etykiety
        etykieta_1 = QLabel("Liczba 1:", self)
        etykieta_2 = QLabel("Liczba 2:", self)
        etykieta_3 = QLabel("Wynik:", self)

        # przypisanie widgetów do układu tabelarycznego
        uklad_t = QGridLayout()
        uklad_t.addWidget(etykieta_1, 0, 0)
        uklad_t.addWidget(etykieta_2, 0, 1)
        uklad_t.addWidget(etykieta_3, 0, 2)

        # 1-liniowe pola edycyjne
        self.liczba_1 = QLineEdit()
        self.liczba_2 = QLineEdit()
        self.wynik = QLineEdit()

        # właściwości dodawanych pól
        self.wynik.readonly = True
        self.wynik.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')

        uklad_t.addWidget(self.liczba_1, 1, 0)
        uklad_t.addWidget(self.liczba_2, 1, 1)
        uklad_t.addWidget(self.wynik, 1, 2)

        # przyciski
        prz_dodaj = QPushButton("&Dodaj", self)
        prz_odejmij = QPushButton("&Odejmij", self)
        prz_dziel = QPushButton("&Mnóż", self)
        prz_mnoz = QPushButton("D&ziel", self)
        prz_koniec = QPushButton("&Koniec", self)

        uklad_h = QHBoxLayout()
        uklad_h.addWidget(prz_dodaj)
        uklad_h.addWidget(prz_odejmij)
        uklad_h.addWidget(prz_dziel)
        uklad_h.addWidget(prz_mnoz)

        uklad_t.addLayout(uklad_h, 2, 0, 1, 3)
        uklad_t.addWidget(prz_koniec, 3, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(uklad_t)

        prz_koniec.clicked.connect(self.koniec)
        prz_dodaj.clicked.connect(self.dzialanie)
        prz_odejmij.clicked.connect(self.dzialanie)
        prz_mnoz.clicked.connect(self.dzialanie)
        prz_dziel.clicked.connect(self.dzialanie)

        self.liczba_1.setFocus()
        # ustawienia rozmiaru, ikony i tytułu okna
        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Prosty kalkulator")
        self.show()

    def koniec(self):
        self.close()

    def dzialanie(self):

        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba_1.text())
            liczba2 = float(self.liczba_2.text())

            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + liczba2
            elif nadawca.text() == "&Odejmij":
                wynik = liczba1 - liczba2
            elif nadawca.text() == "&Mnóż":
                wynik = liczba1 * liczba2
            else:  # dzielenie
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return

            self.wynik.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.StandardButton.Ok)

    def closeEvent(self, event):
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Komunikat')
        msg_box.setText('Czy na pewno koniec?')
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        odp = msg_box.exec()

        if odp == QMessageBox.StandardButton.Yes.value:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape:
            self.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec())
