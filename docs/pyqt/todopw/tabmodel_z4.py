# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
        else:
            return QVariant()
