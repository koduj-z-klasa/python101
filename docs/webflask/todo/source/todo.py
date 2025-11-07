from flask import (
    Blueprint, flash, g, render_template, request, redirect, url_for
)
from db import get_db, query_db
from users import login_required

bp = Blueprint('todo', __name__, template_folder='templates', url_prefix='/todo')

@bp.route('/')
@login_required
def index():
    sql = 'SELECT * FROM zadanie WHERE user_id=? ORDER BY data_pub DESC'
    zadania = query_db(sql, [g.user['id']])
    return render_template('todo/index.html', zadania=zadania)

@bp.route('/dodaj', methods=['GET', 'POST'])
@login_required
def dodaj():
    """Dodawanie nowego zadania"""
    error = None
    if request.method == 'POST':
        zadanie = request.form['zadanie'].strip()
        if len(zadanie):
            db = get_db()
            db.execute('INSERT INTO zadanie (user_id, zadanie, zrobione) VALUES (?, ?, ?)',
                       [g.user['id'], zadanie, 0])
            db.commit()
            flash('Dodano nowe zadanie.')
            return redirect(url_for('todo.index'))
        else:
            flash('Nie możesz dodać pustego zadania!')  # komunikat o błędzie

    return render_template('todo/zadanie_dodaj.html')

@bp.route('/zrobione', methods=['POST'])
def zrobione():
    """Zmiana statusu zadania na wykonane."""
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('UPDATE zadanie SET zrobione=1 WHERE id=? AND user_id=?',
               [zadanie_id, g.user['id']])
    db.commit()
    flash('Zmieniono status zadania.')
    return redirect(url_for('todo.index'))

@bp.route('/usun', methods=['POST'])
def usun():
    """Usuwanie zadania"""
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('DELETE FROM zadanie WHERE id=? AND user_id=?',
               [zadanie_id, g.user['id']])
    db.commit()
    flash('Usunięto zadanie.')
    return redirect(url_for('todo.index'))
