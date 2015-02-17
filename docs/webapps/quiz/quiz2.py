# -*- coding: utf-8 -*-

# niezbędne importy
from flask import Flask
from flask import render_template

app = Flask(__name__)

# dekorator łączący adres główny z widokiem index
@app.route('/')
def index():
    # gdybyśmy chcieli wyświetlić prosty tekst, użyjemy funkcji poniżej
    # return 'Cześć, tu Python!'
    # a teraz zwracamy wyrenderowany szablon index.html:
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
