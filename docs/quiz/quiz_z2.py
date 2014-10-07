# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template

app = Flask(__name__)

# konfiguracja aplikacji, sekret potrzebny do obsługi sesji HTTP wymaganej przez funkcję flash
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
))

# lista pytan
QUESTIONS = [
    {
        'question': u'Stolica Hiszpani, to:',# pytanie
        'answers': [u'Madryt', u'Warszawa', u'Barcelona'], # mozliwe odpowiedzi
        'correct_answer': u'Madryt', # poprawna odpowiedz
    },
    {
        'question': u'Objętość sześcianu o boku 6 cm, wynosi:', # pytanie
        'answers': [u'36', u'216', u'18'], # mozliwe odpowiedzi
        'correct_answer': u'216', # poprawna odpowiedz
    },
    {
        'question': u'Symbol pierwiastka Helu, to:', # pytanie
        'answers': [u'Fe', u'H', u'He'], # mozlowe odpowiedzi
        'correct_answer': u'He', # poprawna odpowiedz
    }
]


@app.route('/')
def index():
    # do templatki index.html przekazujemy liste pytan jako zmienna questions
    return render_template('index.html', questions=QUESTIONS)


if __name__ == '__main__':
    app.run(debug=True)
