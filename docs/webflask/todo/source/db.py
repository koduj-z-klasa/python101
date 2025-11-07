import sqlite3
from flask import g, current_app

def get_db():
    """Funkcja tworzy połączenie z bazą"""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """Funkcja zamyka połączenia z bazą"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    """Funkcja rejestruje funkcję close_db() w aplikacji"""
    app.teardown_appcontext(close_db)

def query_db(query, args=(), one=False):
    """Funkcja wykonuje zapytania SQL i zwraca rezultaty"""
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db():
    """Funkcja tworzy bazę i tabele"""
    from werkzeug.security import generate_password_hash
    db = get_db()
    with current_app.open_resource('modele.sql') as f:
        db.executescript(f.read().decode('utf8'))
