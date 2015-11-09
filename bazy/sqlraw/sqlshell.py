#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Minimala powłoka SQLite
# https://docs.python.org/2/library/sqlite3.html

import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

buffer = ""

print "Podaj polecenie SQL do wykonania w sqlite3."
print "Naciśnij Enter, aby wyjść."

while True:
    line = raw_input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print cur.fetchall()
        except sqlite3.Error as e:
            print "Wystąpił błąd:", e.args[0]
        buffer = ""

con.close()
