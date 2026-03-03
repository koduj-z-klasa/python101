from PyQt6.QtWidgets import QApplication, QWidget
from gui_z5 import UiWidget
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QRadioButton, QComboBox
from PyQt6.QtWidgets import QPushButton


class Widgety(QWidget, UiWidget):
    """ Główna klasa aplikacji """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Widżety')

        # Sygnały i sloty
        # przyciski CheckBox
        self.grupa_chk.buttonClicked.connect(self.ustaw_ksztalt)
        self.ksztalt_chk.clicked.connect(self.aktywuj_ksztalt)

        self.kanaly = {'R'}  # zbiór kanałów
        self.kolor_w = QColor(0, 0, 0)  # kolor RGB kształtu 1

        # Slider + przyciski RadioButton
        for i in range(self.uklad_r.count()):
            self.uklad_r.itemAt(i).widget().toggled.connect(self.ustaw_kanal)
        self.suwak.valueChanged.connect(self.zmien_kolor)

        # Lista ComboBox i SpinBox
        self.grupa_rbb.clicked.connect(self.ustaw_stan)
        self.lista_rgb.currentTextChanged.connect(self.ustaw_kanal)
        self.spin_rgb.valueChanged.connect(self.zmien_kolor)

        # przyciski PushButton
        for btn in self.grupa_pb.buttons():
            btn.clicked.connect(self.ustaw_kanal)
        self.grupa_pbb.clicked.connect(self.ustaw_stan)

    def ustaw_ksztalt(self):
        self.ksztalt_aktywny.ustaw_ksztalt(self.grupa_chk.checkedId())

    def aktywuj_ksztalt(self, wartosc):
        nadawca = self.sender()
        if wartosc:
            self.ksztalt_aktywny = self.ksztalt1
            nadawca.setText('<=')
        else:
            self.ksztalt_aktywny = self.ksztalt2
            nadawca.setText('=>')
        przyciski = self.grupa_chk.buttons()
        przyciski[self.ksztalt_aktywny.ksztalt].setChecked(True)

    def ustaw_kanal(self, wartosc):
        nadawca = self.sender()
        if isinstance(nadawca, QRadioButton) and wartosc:
            # nadawca to QRadioButton
            self.kanaly = set()  # resetujemy zbiór kanałów
            kanal = nadawca.text()
            self.kanaly.add(kanal)
            self.wypisz_kanal(kanal, self.suwak)
        elif isinstance(nadawca, QComboBox):
            # nadawca to QComboBox
            self.kanaly = set()  # resetujemy zbiór kanałów
            self.kanaly.add(wartosc)
            self.wypisz_kanal(wartosc, self.spin_rgb)
        elif isinstance(nadawca, QPushButton):
            if wartosc:
                self.kanaly.add(nadawca.text())
            elif nadawca.text() in self.kanaly:
                self.kanaly.remove(nadawca.text())

    def wypisz_kanal(self, kanal, obiekt):
        if kanal == 'R':
            obiekt.setValue(self.kolor_w.red())
        elif kanal == 'G':
            obiekt.setValue(self.kolor_w.green())
        else:
            obiekt.setValue(self.kolor_w.blue())

    def zmien_kolor(self, wartosc):
        self.lcd.display(wartosc)
        if 'R' in self.kanaly:
            self.kolor_w.setRed(wartosc)
        if 'G' in self.kanaly:
            self.kolor_w.setGreen(wartosc)
        if 'B' in self.kanaly:
            self.kolor_w.setBlue(wartosc)
        self.ksztalt_aktywny.ustaw_kolor_w(
            self.kolor_w.red(),
            self.kolor_w.green(),
            self.kolor_w.blue())

    def ustaw_stan(self, wartosc):
        if wartosc:
            # włączone przyciski RadioButton
            self.lista_rgb.setEnabled(False)
            self.spin_rgb.setEnabled(False)
        else:
            # włączona lista ComboBox
            self.lista_rgb.setEnabled(True)
            self.spin_rgb.setEnabled(True)
            self.kanaly = set()
            self.kanaly.add(self.lista_rgb.currentText())
            self.wypisz_kanal(wartosc, self.spin_rgb)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()
    sys.exit(app.exec())
