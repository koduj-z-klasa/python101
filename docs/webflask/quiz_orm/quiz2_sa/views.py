# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import render_template, request, redirect, url_for, abort, flash
from app import app, baza
from models import Pytanie, Odpowiedz
from forms import *
from sqlalchemy.orm.exc import NoResultFound


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lista')
def lista():
    pytania = Pytanie.query.join(Odpowiedz)
    if not pytania.count():
        flash('Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('lista.html', pytania=pytania.all())


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # POST, sprawdź odpowiedzi
    if request.method == 'POST':
        wynik = 0  # liczba poprawnych odpowiedzi
        # odczytujemy słownik z odpowiedziami
        for pid, odp in request.form.items():
            # pobieramy z bazy poprawną odpowiedź
            odpok = baza.session.query(Pytanie.odpok).filter(
                Pytanie.id == int(pid)).scalar()
            if odp == odpok:  # porównujemy odpowiedzi
                wynik += 1  # zwiększamy wynik
        # przygotowujemy informacje o wyniku
        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(wynik), 'sukces')
        return redirect(url_for('index'))

    # GET, wyświetl pytania
    pytania = Pytanie.query.join(Odpowiedz)
    if not pytania.count():
        flash('Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania.all())


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            if type(error) is list:
                error = error[0]
            flash("Błąd: {}. Pole: {}".format(
                error,
                getattr(form, field).label.text))


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    form = DodajForm()
    if form.validate_on_submit():
        odp = form.odpowiedzi.data
        p = Pytanie(pytanie=form.pytanie.data, odpok=odp[int(form.odpok.data)])
        baza.session.add(p)
        baza.session.commit()
        for o in odp:
            inst = Odpowiedz(pnr=p.id, odpowiedz=o)
            baza.session.add(inst)
        baza.session.commit()

        flash("Dodano pytanie: {}".format(form.pytanie.data))
        return redirect(url_for("lista"))
    elif request.method == 'POST':
        flash_errors(form)

    return render_template("dodaj.html", form=form, radio=list(form.odpok))


def get_or_404(pid):
    try:
        p = Pytanie.query.get(pid)
        return p
    except NoResultFound:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/edytuj/<int:pid>', methods=['GET', 'POST'])
def edytuj(pid):
    p = get_or_404(pid)
    form = DodajForm()

    if form.validate_on_submit():
        odp = form.odpowiedzi.data
        p.pytanie = form.pytanie.data
        p.odpok = odp[int(form.odpok.data)]
        for i, o in enumerate(p.odpowiedzi):
            o.odpowiedz = odp[i]
        baza.session.commit()

        flash("Zaktualizowano pytanie: {}".format(form.pytanie.data))
        return redirect(url_for("lista"))
    elif request.method == 'POST':
        flash_errors(form)

    for i in range(3):
        if p.odpok == p.odpowiedzi[i].odpowiedz:
            p.odpok = i
            break
    form = DodajForm(obj=p)
    odpok = list(form.odpok)
    return render_template("edytuj.html", form=form, radio=odpok)


@app.route('/usun/<int:pid>', methods=['GET', 'POST'])
def usun(pid):
    """Usunięcie pytania o identyfikatorze pid"""
    if request.method == 'POST':
        p = get_or_404(request.form['pid'])
        flash('Usunięto pytanie {0}'.format(p.pytanie), 'sukces')
        baza.session.delete(p)
        baza.session.commit()
        return redirect(url_for('lista'))
    p = get_or_404(pid)
    return render_template("pytanie_usun.html", pytanie=p)
