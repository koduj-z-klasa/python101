# -*- coding: utf-8 -*-
# todo/todo.py

# importujemy biblioteki potrzebne do nawiązania połączenia z baza
import os
import sqlite3

from flask import Flask, g
# dodajemy nowe importy do pozostalych
from flask import render_template

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    # nieznany nikomu sekret dla mechanizmu sesji
    SECRET_KEY = 'bardzosekretnawartosc',
    # polozenie naszej bazy
    DATABASE = os.path.join(app.root_path, 'db.sqlite'),
    # nazwa aplikacji
    SITE_NAME = 'Moja lista ToDo'
))

def connect_db():
    """Nawiazywanie polaczenia z baza danych okreslona w konfiguracji."""
    """http://flask.pocoo.org/docs/0.10/patterns/sqlite3/"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Funkcja pomocnicza, ktora tworzy polaczenia z baza przy pierwszym
    wywolaniu i umieszcza ja w kontekscie aplikacji (obiekt g). W kolejnych
    wywolaniach zwraca polaczenie z kontekstu."""
    if not hasattr(g, 'db'):
        g.db = connect_db() # jezeli kontekst nie zawiera informacji o polaczeniu to je tworzymy
    return g.db # zwracamy polaczenie z baza

# dekorator wykonujacy funkcje po wyslaniu odpowiedzi do klienta
@app.teardown_request
def close_db(error):
    """Zamykanie polaczenia z baza."""
    if hasattr(g, 'db'):
        g.db.close()

# dekorator laczacy adres glowny z widokiem index
@app.route('/')
def index():
    db = get_db() # laczymy sie z baza
    # pobieramy wszystkie wpisy z bazy:
    cur = db.execute('select id, title, is_done, created_at from entries order by created_at desc;')
    entries = cur.fetchall()
    # renderujemy tempaltke i zwracamy ja do klienta
    return render_template('show_entries.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
