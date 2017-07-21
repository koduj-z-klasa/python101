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
DANE = [{
    'pytanie': 'Stolica Hiszpani, to:',  # pytanie
    'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],  # możliwe odpowiedzi
    'odpok': 'Madryt'},  # poprawna odpowiedź
    {
    'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
    'odpowiedzi': ['36', '216', '18'],
    'odpok': '216'},
    {
    'pytanie': 'Symbol pierwiastka Helu, to:',
    'odpowiedzi': ['Fe', 'H', 'He'],
    'odpok': 'He'},
]


@app.route('/')
def index():
    # return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)


if __name__ == '__main__':
    app.run(debug=True)
