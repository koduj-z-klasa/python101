# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import render_template, request, redirect, url_for, abort, flash
from app import app
from models import Pytanie, Odpowiedz
from forms import *


@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')


@app.route('/lista')
def lista():
    """Pobranie wszystkich pytań z bazy i zwrócenie szablonu z listą pytań"""
    pytania = Pytanie().select().annotate(Odpowiedz)
    if not pytania.count():
        flash('Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('lista.html', pytania=pytania)


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Wyświetlenie pytań i odpowiedzi w formie quizu oraz ocena poprawności
    przesłanych odpowiedzi"""
    if request.method == 'POST':
        wynik = 0
        for pid, odp in request.form.items():
            odpok = Pytanie.select(Pytanie.odpok).where(
                Pytanie.id == int(pid)).scalar()
            if odp == odpok:
                wynik += 1

        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(wynik), 'sukces')
        return redirect(url_for('index'))

    # GET, wyświetl pytania
    pytania = Pytanie().select().annotate(Odpowiedz)
    if not pytania.count():
        flash('Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania)


def flash_errors(form):
    """Odczytanie wszystkich błędów formularza i przygotowanie komunikatów"""
    for field, errors in form.errors.items():
        for error in errors:
            if type(error) is list:
                error = error[0]
            flash("Błąd: {}. Pole: {}".format(
                error,
                getattr(form, field).label.text))


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    """Dodawanie pytań i odpowiedzi"""
    form = DodajForm()
    if form.validate_on_submit():
        odp = form.odpowiedzi.data
        p = Pytanie(pytanie=form.pytanie.data, odpok=odp[int(form.odpok.data)])
        p.save()
        for o in odp:
            inst = Odpowiedz(pnr=p.id, odpowiedz=o)
            inst.save()
        flash("Dodano pytanie: {}".format(form.pytanie.data))
        return redirect(url_for("lista"))
    elif request.method == 'POST':
        flash_errors(form)

    return render_template("dodaj.html", form=form, radio=list(form.odpok))


def get_or_404(pid):
    """Pobranie i zwrócenie obiektu z bazy lub wywołanie szablonu 404.html"""
    try:
        p = Pytanie.select().annotate(Odpowiedz).where(Pytanie.id == pid).get()
        return p
    except Pytanie.DoesNotExist:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    """Zwrócenie szablonu 404.html w przypadku nie odnalezienia strony"""
    return render_template('404.html'), 404


@app.route('/edytuj/<int:pid>', methods=['GET', 'POST'])
def edytuj(pid):
    """Edycja pytania o identyfikatorze pid i odpowiedzi"""
    p = get_or_404(pid)
    form = DodajForm()

    if form.validate_on_submit():
        odp = form.odpowiedzi.data
        p.pytanie = form.pytanie.data
        p.odpok = odp[int(form.odpok.data)]
        p.save()
        for i, o in enumerate(p.odpowiedzi):
            o.odpowiedz = odp[i]
            o.save()
        flash("Zaktualizowano pytanie: {}".format(form.pytanie.data))
        return redirect(url_for("lista"))
    elif request.method == 'POST':
        flash_errors(form)

    for i in range(3):
        if p.odpok == p.odpowiedzi[i].odpowiedz:
            p.odpok = i
            break
    form = DodajForm(obj=p)
    return render_template("edytuj.html", form=form, radio=list(form.odpok))


@app.route('/usun/<int:pid>', methods=['GET', 'POST'])
def usun(pid):
    """Usunięcie pytania o identyfikatorze pid"""
    p = get_or_404(pid)
    if request.method == 'POST':
        flash('Usunięto pytanie {0}'.format(p.pytanie), 'sukces')
        p.delete_instance(recursive=True)
        return redirect(url_for('index'))
    return render_template("pytanie_usun.html", pytanie=p)
