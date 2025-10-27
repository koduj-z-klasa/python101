from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QLabel, QGridLayout


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

        # przypisanie utworzonego układu do okna
        self.setLayout(uklad_t)

        # ustawienia rozmiaru, ikony i tytułu okna
        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Prosty kalkulator")
        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec())
