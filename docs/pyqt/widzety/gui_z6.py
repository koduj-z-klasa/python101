from ksztalty import Ksztalty, Ksztalt
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QCheckBox, QButtonGroup, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider, QLCDNumber, QSplitter
from PyQt6.QtWidgets import QRadioButton, QGroupBox
from PyQt6.QtWidgets import QComboBox, QSpinBox
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QLabel, QLineEdit


class UiWidget:
    """ Klasa definiująca GUI """

    def __init__(self):

        # widget definiujący kształt, instancja klasy Ksztalt
        self.ksztalt1 = Ksztalt(None, Ksztalty.RECT)
        self.ksztalt2 = Ksztalt(None, Ksztalty.ELLIPSE)
        self.ksztalt_aktywny = self.ksztalt1

        # przyciski CheckBox
        uklad_chk = QVBoxLayout()  # układ pionowy
        self.grupa_chk = QButtonGroup()
        for i, v in enumerate(('Kwadrat', 'Koło', 'Trójkąt', 'Linia')):
            self.chk = QCheckBox(v)
            self.grupa_chk.addButton(self.chk, i)
            uklad_chk.addWidget(self.chk)
        przyciski = self.grupa_chk.buttons()
        przyciski[self.ksztalt_aktywny.ksztalt].setChecked(True)

        # przycisk CheckBox do wyboru aktywnego kształtu
        self.ksztalt_chk = QCheckBox('<=')
        self.ksztalt_chk.setChecked(True)
        uklad_chk.addWidget(self.ksztalt_chk)

        # układ poziomy dla kształtów oraz przycisków CheckBox
        uklad_h1 = QHBoxLayout()
        uklad_h1.addWidget(self.ksztalt1)
        uklad_h1.addLayout(uklad_chk)
        uklad_h1.addWidget(self.ksztalt2)
        # koniec CheckBox

        # Slider i LCDNumber
        self.suwak = QSlider(Qt.Orientation.Horizontal)
        self.suwak.setMinimum(0)
        self.suwak.setMaximum(255)
        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        # układ poziomy (splitter) dla slajdera i lcd
        uklad_h2 = QSplitter(Qt.Orientation.Horizontal, self)
        uklad_h2.addWidget(self.suwak)
        uklad_h2.addWidget(self.lcd)
        uklad_h2.setSizes((125, 75))

        # przyciski RadioButton
        self.uklad_r = QHBoxLayout()
        for v in 'RGB':
            self.radio = QRadioButton(v)
            self.uklad_r.addWidget(self.radio)
        self.uklad_r.itemAt(0).widget().setChecked(True)

        # grupujemy przyciski
        self.grupa_rbb = QGroupBox('Opcje RGB')
        self.grupa_rbb.setLayout(self.uklad_r)
        self.grupa_rbb.setObjectName('Radio')
        self.grupa_rbb.setCheckable(True)

        # układ poziomy dla grupy Radio
        uklad_h3 = QHBoxLayout()
        uklad_h3.addWidget(self.grupa_rbb)
        # koniec RadioButton

        # Lista ComboBox i SpinBox
        self.lista_rgb = QComboBox()
        for v in 'RGB':
            self.lista_rgb.addItem(v)
        self.lista_rgb.setEnabled(False)
        # SpinBox
        self.spin_rgb = QSpinBox()
        self.spin_rgb.setMinimum(0)
        self.spin_rgb.setMaximum(255)
        self.spin_rgb.setEnabled(False)
        # układ pionowy dla ComboBox i SpinBox
        uklad_v1 = QVBoxLayout()
        uklad_v1.addWidget(self.lista_rgb)
        uklad_v1.addWidget(self.spin_rgb)
        # do układu poziomego grupy Radio dodajemy układ ComboBox i SpinBox
        uklad_h3.insertSpacing(1, 25)
        uklad_h3.addLayout(uklad_v1)
        # koniec ComboBox i SpinBox

        # przyciski PushButton
        uklad_pb = QHBoxLayout()
        self.grupa_pb = QButtonGroup()
        for v in 'RGB':
            self.btn = QPushButton(v)
            self.btn.setCheckable(True)
            self.grupa_pb.addButton(self.btn)
            uklad_pb.addWidget(self.btn)
        self.grupa_pb.setExclusive(False)
        # grupujemy przyciski
        self.grupa_pbb = QGroupBox('Przyciski RGB')
        self.grupa_pbb.setLayout(uklad_pb)
        self.grupa_pbb.setObjectName('Push')
        self.grupa_pbb.setCheckable(True)
        self.grupa_pbb.setChecked(False)
        # koniec PushButton

        # etykiety QLabel i pola QLineEdit
        uklad_h4 = QHBoxLayout()
        self.label_r = QLabel('R')
        self.label_g = QLabel('G')
        self.label_b = QLabel('B')
        self.edit_r = QLineEdit('0')
        self.edit_g = QLineEdit('0')
        self.edit_b = QLineEdit('0')
        for v in 'rgb':
            label = getattr(self, 'label_' + v)
            edit = getattr(self, 'edit_' + v)
            edit.setObjectName('edit_' + v)
            edit.setMaxLength(3)
            uklad_h4.addWidget(label)
            uklad_h4.addWidget(edit)
        # koniec QLabel i QLineEdit

        # główny układ okna, pionowy
        uklad_okna = QVBoxLayout()
        uklad_okna.addLayout(uklad_h1)
        uklad_okna.addWidget(uklad_h2)
        uklad_okna.addLayout(uklad_h3)
        uklad_okna.addWidget(self.grupa_pbb)
        uklad_okna.addLayout(uklad_h4)

        # ustawienie głównego układu okna
        self.setLayout(uklad_okna)
