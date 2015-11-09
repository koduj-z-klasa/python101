#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

# utworzenie połączenia z bazą przechowywaną w pamięci RAM
con = sqlite3.connect(':memory:')

# dostęp do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row

# utworzenie obiektu kursora
cur = con.cursor()
