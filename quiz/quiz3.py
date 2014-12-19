# -*- coding: utf-8 -*-

# niezbędne importy
from flask import Flask
from flask import render_template, request, redirect, url_for, flash

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    # nieznany nikomu sekret
    SECRET_KEY='bradzosekretnawartosc',
))

# lista pytań
PYTANIA = [
    {
        'pytanie': u'Stolica Hiszpani, to:',# pytanie
        'odpowiedzi': [u'Madryt', u'Warszawa', u'Barcelona'], # możliwe odpowiedzi
        'odpok': u'Madryt', # poprawna odpowiedź
    },
    {
        'pytanie': u'Objętość sześcianu o boku 6 cm, wynosi:',
        'odpowiedzi': [u'36', u'216', u'18'],
        'odpok': u'216',
    },
    {
        'pytanie': u'Symbol pierwiastka Helu, to:',
        'odpowiedzi': [u'Fe', u'H', u'He'],
        'odpok': u'He',
    }
]


@app.route('/')
def index():
    # jeżeli zadanie jest typu GET, to renderujemy szablon index.html,
    # do którego przekazujemy tablicę pytań w zmiennej "pytania"
    return render_template('index.html', pytania=PYTANIA)


if __name__ == '__main__':
    app.run(debug=True)
