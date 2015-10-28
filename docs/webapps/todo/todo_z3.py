# -*- coding: utf-8 -*-
# todo/todo.py

from flask import Flask, g

import os
import sqlite3

app = Flask(__name__)


app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    SITE_NAME='Moje zadania'
))


def get_db():
    """Funkcja tworząca połączenie z bazą danych"""
    if not hasattr(g, 'db'):  # jeżeli brak połączenia, to je tworzymy
        con = sqlite3.connect(app.config['DATABASE'])
        con.row_factory = sqlite3.Row
        g.db = con  # zapisujemy połączenie w kontekście aplikacji
    return g.db  # zwracamy połączenie z bazą


@app.teardown_request
def close_db(error):
    """Zamykanie połączenia z bazą"""
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/')
def index():
    return 'Cześć, tu Python!'

if __name__ == '__main__':
    app.run(debug=True)
