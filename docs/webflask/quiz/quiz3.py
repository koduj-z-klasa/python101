# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return 'Cześć, tu Python!'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
