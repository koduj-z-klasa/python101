# -*- coding: utf-8 -*-
# quiz_sa/views.py

from flask import render_template, request, redirect, url_for, flash

from app import app
from app import baza
from models import Pytanie, Odpowiedz


@app.route('/')
def index():
    return render_template('index.html')


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
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(wynik), 'sukces')
        return redirect(url_for('index'))

    # GET, wyświetl pytania
    pytania = Pytanie.query.join(Odpowiedz)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('quiz.html', pytania=pytania.all())


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    error = []
    # POST, zapisz pytanie
    if request.method == 'POST':
        # sprawdzanie poprawności przesłanych danych
        if len(request.form['pytanie']) == 0:
            error.append(u'Błąd: pytanie nie może być puste!')
        odpowiedzi = list(request.form.getlist('odp[]'))
        for odp in odpowiedzi:
            if len(odp) == 0:
                error.append(u'Odpowiedź nie może być pusta!')
        if len(request.form['odpok']) == 0:
            error.append(u'Brak numeru poprawnej odpowiedzi!')
        elif int(request.form['odpok']) > len(odpowiedzi):
            error.append(u'Błędny numer poprawnej odpowiedzi!')

        if not error:  # jeżeli nie ma błędów dodajemy pytanie
            pytanie = request.form['pytanie'].strip()
            odpok = odpowiedzi[(int(request.form['odpok']) - 1)]
            try:
                if request.form['id']:  # aktualizujemy pytanie
                    p = Pytanie.query.get(request.form['id'])
                    p.pytanie = pytanie.strip()
                    p.odpok = odpok.strip()
                    for i, odp in enumerate(odpowiedzi):
                        p.odpowiedzi[i].odpowiedz = odp.strip()
                    baza.session.commit()
                    flash(u'Zmieniono pytanie:', 'sukces')
            except KeyError:  # dodajemy nowe pytanie, brak id pytania!
                p = Pytanie(pytanie=pytanie.strip(), odpok=odpok.strip())
                baza.session.add(p)
                baza.session.commit()
                for odp in odpowiedzi:
                    o = Odpowiedz(pnr=p.id, odpowiedz=odp.strip())
                    baza.session.add(o)
                baza.session.commit()
                flash(u'Dodano pytanie:', 'sukces')

            flash("\n" + pytanie + " " + odpok.strip() +
                  " (" + ", ".join(odpowiedzi) + ")", 'kom')
            return redirect(url_for('index'))
        else:
            for e in error:
                flash(e, 'blad')

    # GET, wyświetl formularz
    return render_template('dodaj.html')


@app.route('/edytuj', methods=['GET', 'POST'])
def edytuj():
    pytania = Pytanie.query.join(Odpowiedz)
    if not pytania.count():
        flash(u'Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    if request.method == 'POST':
        pid = request.form['id']
        pytanie = Pytanie.query.get(pid)
        return render_template('dodaj.html', pytanie=pytanie)

    return render_template('edytuj.html', pytania=pytania.all())


@app.route('/usun', methods=['POST'])
def usun():
    """Usunięcie pytania o identyfikatorze pid"""
    pid = request.form['id']
    p = Pytanie.query.get(pid)
    baza.session.delete(p)
    baza.session.commit()
    flash(u'Usunięto pytanie {0}'.format(pid), 'sukces')
    return redirect(url_for('index'))
