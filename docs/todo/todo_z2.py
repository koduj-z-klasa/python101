# -*- coding: utf-8 -*-
# todo/todo.py

from flask import Flask
app = Flask(__name__)

# dekorator laczacy adres glowny z widokiem index
@app.route('/')
def index():
    return 'Witaj na moim serwerze!'

if __name__ == '__main__':
    app.run(debug=True)
