# -*- coding: utf-8 -*-
# todo/todo.py

# importujemy biblioteki potrzebne do nawiązania połączenia z baza
import os
import sqlite3

from flask import Flask, g

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
    """Nawiazywanie połaczenia z bazą danych określoną w konfiguracji."""
    """http://flask.pocoo.org/docs/0.10/patterns/sqlite3/"""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Funkcja pomocnicza, ktora tworzy połączenia z bazą przy pierwszym
    wywołaniu i umieszcza ja w kontekście aplikacji (obiekt g). W kolejnych
    wywołaniach zwraca połączenie z kontekstu."""
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
    return 'Hello, SWOI'

if __name__ == '__main__':
    app.run(debug=True)
