from PyQt6.QtWidgets import QApplication, QWidget
from gui_z2 import UiWidget


class Widgety(QWidget, UiWidget):
    """ Główna klasa aplikacji """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Widżety')

        # Sygnały i sloty
        # przyciski CheckBox
        self.grupa_chk.buttonClicked.connect(self.ustaw_ksztalt)
        self.ksztalt_chk.clicked.connect(self.aktywuj_ksztalt)

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


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()
    sys.exit(app.exec())
