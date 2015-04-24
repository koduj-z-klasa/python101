# -*- coding: utf-8 -*-
# quiz/quiz3.py

from flask import Flask
from flask import render_template

app = Flask(__name__)

# dekorator łączący adres główny z widokiem index
@app.route('/')
def index():
    #return 'Cześć, tu Python!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
