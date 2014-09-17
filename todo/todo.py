# -*- coding: utf-8 -*-

# todo/todo.py

import os
import sqlite3
from datetime import datetime
from flask import Flask, g
from flask import render_template
from flask import flash, redirect, url_for, request

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    # nieznany nikomu sekret
    SECRET_KEY='bradzosekretnawartosc',
    # polozenie naszej bazy
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    # nazwa aplikacji
    SITE_NAME = 'Moja lista ToDo'
))

def connect_db():
    """Nawiazaywanie polaczenia z baza danych okreslona w konfiguracji."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Funkcja pomocnicza, ktora tworzy polaczenia z baza przy pierwszym
    wywolaniu i umieszcza ja w kontekscie aplikacji (obiekt g). W kolejnych
    wywolaniach zwraca polaczenie z kontekstu."""
    if not hasattr(g, 'db'):
        # jezeli kontekst nie zawiera informacji o polaczeniu to je tworzymy
        g.db = connect_db()
    # zwracamy polaczenie z baza
    return g.db

# dekorator sprawiajacy, ze dana funkcja zostaje wykonana po wyslaniu
# odpowiedzi do klienta
@app.teardown_request
def close_db(error):
    """Zamykanie polaczenia z baza."""
    if hasattr(g, 'db'):
        g.db.close()


# poza powiazaniem adresu / z funkcja index, dodajemy mozliwosc akcpetacji
# zadan HTTP GET i POST (domyslnie dozwolone sa tyko zadania GET)
@app.route('/', methods=['GET', 'POST'])
def index():
    """Glowny widok strony. Obsluguje wyswietlanie i dodawanie zadan."""
    # zmienna przechowujaca informacje o ewentualnych bledach
    error = None

    # sprawdzamy, czy zadanie jest POSTem, jezeli tak to dodajemy nowe zadanie
    if request.method == 'POST':
        # sprawdzamy poprawnosc przeslanych danych
        if len(request.form['entry']) > 0:
            # nawiazujemy polazcenie z baza danych
            db = get_db()
            # wyciagamy tresc zadania z przeslanego formularza
            new_entry = request.form['entry']
            # ustalamy, ze nowo dodane zadanie nie jest jeszcze wykonane
            is_done = '0'
            # data dodania
            created_at = datetime.now()
            # konfigurujemy zapytanie do bazy, ktyore wstawi nowy wiersz z danymi
            db.execute('insert into entries (title, is_done, created_at) values (?, ?, ?);',
                        [new_entry, is_done, created_at])
            # wykonujemy zapytanie
            db.commit()
            # ustawiamy informacje o pomyslnym dodaniu nowego zadnaia
            flash('Dodano nowe zadanie')
            # po udanym zapisie zawsze przekierowujemy na strone glowna
            return redirect(url_for('index'))
        # ustawiamy tresc komunikatu o bledzie
        error = u'Nie możesz dodać pustego zadania'

    # przygotowanie danych do wyswietlenia
    db = get_db()
    # wyciagniecie wszystkich wpisow
    cur = db.execute('select id, title, is_done, created_at from entries order by created_at desc;')
    entries = cur.fetchall()
    # zwracamy wyrenderowana tempaltke
    return render_template('show_entries.html', entries=entries, error=error)

# nadajemy osobny adres, oraz zezwalamy jedynie na zadania typu POST
@app.route('/mark_as_done', methods=['POST'])
def mark_as_done():
    """Zmiana statusu zadania na wykonane."""
    # z przeslanego formularza pobieramy indentyfikator zadania
    entry_id = request.form['id']
    # laczymy sie z baza danych
    db = get_db()
    # przygotowujeym zapytanie aktualizujace pole is_done zadania o danym identyfikatorze
    db.execute('update entries set is_done=1 where id=?', [entry_id,])
    # zapisujemy nowe dane
    db.commit()
    # na koniec przekierowujemy na liste wszystkich zadan
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

