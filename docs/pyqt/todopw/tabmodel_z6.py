# -*- coding: utf-8 -*-

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant


class TabModel(QAbstractTableModel):
    """ Tabelaryczny model danych """

    def __init__(self, pola=[], dane=[], parent=None):
        super(TabModel, self).__init__()
        self.pola = pola
        self.tabela = dane

    def aktualizuj(self, dane):
        """ Przypisuje źródło danych do modelu """
        print(dane)
        self.tabela = dane

    def rowCount(self, parent=QModelIndex()):
        """ Zwraca ilość wierszy """
        return len(self.tabela)

    def columnCount(self, parent=QModelIndex()):
        """ Zwraca ilość kolumn """
        if self.tabela:
            return len(self.tabela[0])
        else:
            return 0

    def data(self, index, rola=Qt.DisplayRole):
        """ Wyświetlanie danych """
        i = index.row()
        j = index.column()

        if rola == Qt.DisplayRole:
            return '{0}'.format(self.tabela[i][j])
        elif rola == Qt.CheckStateRole and (j == 3 or j == 4):
            if self.tabela[i][j]:
                return Qt.Checked
            else:
                return Qt.Unchecked
        elif rola == Qt.EditRole and j == 1:
            return self.tabela[i][j]
        else:
            return QVariant()

    def flags(self, index):
        """ Zwraca właściwości kolumn tabeli """
        flags = super(TabModel, self).flags(index)
        j = index.column()
        if j == 1:
            flags |= Qt.ItemIsEditable
        elif j == 3 or j == 4:
            flags |= Qt.ItemIsUserCheckable

        return flags

    def setData(self, index, value, rola=Qt.DisplayRole):
        """ Zmiana danych """
        i = index.row()
        j = index.column()
        if rola == Qt.EditRole and j == 1:
            self.tabela[i][j] = value
        elif rola == Qt.CheckStateRole and (j == 3 or j == 4):
            if value:
                self.tabela[i][j] = True
            else:
                self.tabela[i][j] = False

        return True

    def headerData(self, sekcja, kierunek, rola=Qt.DisplayRole):
        """ Zwraca nagłówki kolumn """
        if rola == Qt.DisplayRole and kierunek == Qt.Horizontal:
            return self.pola[sekcja]
        elif rola == Qt.DisplayRole and kierunek == Qt.Vertical:
            return sekcja+1
        else:
            return QVariant()
