# -*- coding: utf-8 -*-
# quiz/quiz2.py

from flask import Flask

app = Flask(__name__)

# dekorator łączący adres główny z widokiem index
@app.route('/')
def index():
    return 'Cześć, tu Python!'

if __name__ == '__main__':
    app.run(debug=True)
