# -*- coding: utf-8 -*-
# todo/todo.py

# wymagane importy
from flask import Flask, g
from flask import render_template
from datetime import datetime
from flask import flash, redirect, url_for, request

# import modułów do obsługi bazy sqlite
import os
import sqlite3

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    # klucz zabezpieczający sesje
    SECRET_KEY='bardzosekretnawartosc',
    # położenie pliku bazy
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    # nazwa aplikacji
    SITE_NAME='Moje zadania'
))


def get_db():
    """Funkcja tworzy połączenia z bazą przy pierwszym wywołaniu
    i umieszcza ją w kontekście aplikacji (obiekt g).
    W kolejnych wywołaniach zwraca połączenie z kontekstu."""

    if not hasattr(g, 'db'):  # jeżeli brak połączenia, to je tworzymy
        """Nawiazywanie połaczenia z bazą danych.
        Zob. http://flask.pocoo.org/docs/0.10/patterns/sqlite3/"""
        con = sqlite3.connect(app.config['DATABASE'])
        con.row_factory = sqlite3.Row
        g.db = con  # zapisujemy połączenie w kontekście aplikacji

    return g.db  # zwracamy połączenie z bazą


# dekorator wykonujący funkcje po wysłaniu odpowiedzi do klienta
@app.teardown_request
def close_db(error):
    """Zamykanie połączenia z bazą."""
    if hasattr(g, 'db'):
        g.db.close()


# dekorator łączący adres główny z widokiem index
# dodajemy obsługę żądań POST (domyślnie tyko GET)
@app.route('/', methods=['GET', 'POST'])
def index():
    """Główny widok strony. Obsługuje wyświetlanie i dodawanie zadań."""
    # return 'Cześć, tu Python!'

    error = None

    # jeżeli otrzymujemy dane POST z formularza, dodajemy nowe zadanie
    if request.method == 'POST':
        # sprawdzamy poprawność przesłanych danych
        if len(request.form['zadanie']) > 0:
            # pobieramy treść zadania z przesłanego formularza
            zadanie = request.form['zadanie']
            zrobione = '0'  # zadanie nie jest jeszcze wykonane
            data_pub = datetime.now()  # data dodania
            db = get_db()
            # zapytanie do bazy, które wstawia nowy wiersz z danymi
            db.execute('INSERT INTO zadania VALUES (?, ?, ?, ?);',
                       [None, zadanie, zrobione, data_pub])
            db.commit()  # wykonujemy zapytanie
            # informacja dla użytkownika o pomyślnym dodaniu nowego zadania
            flash('Dodano nowe zadanie!')
            # przekierowujemy użytkownika na stronę główną - żądanie GET!
            return redirect(url_for('index'))

        error = u'Nie możesz dodać pustego zadania!'  # komunikat o błędzie

    db = get_db()  # łaczymy sią z bazą
    # pobieramy wszystkie wpisy z bazy:
    kursor = db.execute('SELECT * FROM zadania ORDER BY data_pub DESC;')
    zadania = kursor.fetchall()
    # do szablonu przekazujemy pobrane zadania i zwracamy odpowiedź
    return render_template('zadania_lista.html', zadania=zadania, error=error)

# adres /zrobione wiążemy z widokiem zrobione(), obsługujemy tylko żądania POST


@app.route('/zrobione', methods=['POST'])
def zrobione():
    """Zmiana statusu zadania na wykonane."""
    # z przesłanego formularza pobieramy identyfikator zadania
    zadanie_id = request.form['id']
    db = get_db()
    # przygotowujemy zapytanie aktualizujące pole zrobione zadania o danym
    # identyfikatorze
    db.execute('UPDATE zadania SET zrobione=1 WHERE id=?', [zadanie_id, ])
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
