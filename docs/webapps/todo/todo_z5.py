# -*- coding: utf-8 -*-
# todo/todo.py

from flask import Flask, g
from flask import render_template
from datetime import datetime
from flask import flash, redirect, url_for, request

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


@app.route('/', methods=['GET', 'POST'])
def index():
    """Główny widok strony. Obsługuje wyświetlanie i dodawanie zadań."""

    error = None

    if request.method == 'POST':
        if len(request.form['zadanie']) > 0:
            zadanie = request.form['zadanie']
            zrobione = '0'
            data_pub = datetime.now()
            db = get_db()
            db.execute('INSERT INTO zadania VALUES (?, ?, ?, ?);',
                       [None, zadanie, zrobione, data_pub])
            db.commit()
            flash('Dodano nowe zadanie.')
            return redirect(url_for('index'))

        error = u'Nie możesz dodać pustego zadania!'  # komunikat o błędzie

    db = get_db()
    kursor = db.execute('SELECT * FROM zadania ORDER BY data_pub DESC;')
    zadania = kursor.fetchall()
    return render_template('zadania_lista.html', zadania=zadania, error=error)

if __name__ == '__main__':
    app.run(debug=True)
