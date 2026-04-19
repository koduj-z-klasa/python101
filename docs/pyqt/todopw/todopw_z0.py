from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QMessageBox, QInputDialog
from gui_z0 import UiWidget


class Zadania(QWidget, UiWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.loguj_btn.clicked.connect(self.loguj)
        self.koniec_btn.clicked.connect(self.koniec)

    def loguj(self):
        login, ok = QInputDialog.getText(self, 'Logowanie', 'Podaj login:')
        if ok:
            haslo, ok = QInputDialog.getText(self, 'Logowanie', 'Podaj haslo:')
            if ok:
                if not login or not haslo:
                    QMessageBox.warning(
                        self, 'Błąd', 'Pusty login lub hasło!', QMessageBox.StandardButton.Ok)
                    return
                QMessageBox.information(
                    self, 'Dane logowania',
                    'Podano: ' + login + ' ' + haslo, QMessageBox.StandardButton.Ok)

    def koniec(self):
        self.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Zadania()
    okno.show()
    okno.move(350, 200)
    sys.exit(app.exec())
