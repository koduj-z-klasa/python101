# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
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
    #return 'Cześć, tu Python!'
    return render_template('index.html', pytania=PYTANIA)

if __name__ == '__main__':
    app.run(debug=True)
