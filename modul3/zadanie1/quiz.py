# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import flash

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    # nieznany nikomu sekret
    SECRET_KEY='bradzosekretnawartosc',
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


@app.route('/', methods=['GET', 'POST'])
def index():
    # jezeli zadanie jest typu POST, to znaczy, ze ktos przeslal odpowiedzi do sprawdzenia
    if request.method == 'POST':
        score = 0 # liczba poprawnych odpowiedzi
        answers = request.form # zapamietujemy slownik z odpowiedziami
        # sprawdzamy odpowiedzi
        for question_number, user_answer in answers.items():
            # wyciagamy informacje o poprawnej odpowiedzi
            correct_answer = QUESTIONS[int(question_number)]['correct_answer']
            # porownujemy odpowiedzi
            if user_answer == correct_answer:
                # zwiekszamy wynik
                score += 1
        # zapamietujemy informacje o wyniku
        flash(u'Liczba poprawnych odpowiedzi, to: {0}'.format(score))
        # po POST przekierowujemy na strone glowna
        return redirect(url_for('index'))

    # jezeli zadanie jest typu GET, to renderujemy index.html
    return render_template('index.html', questions=QUESTIONS)


if __name__ == '__main__':
    app.run(debug=True)
