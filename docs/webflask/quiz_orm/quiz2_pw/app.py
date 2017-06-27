# -*- coding: utf-8 -*-
# quiz_pw/app.py

from flask import Flask, g
from peewee import *

app = Flask(__name__)

# konfiguracja aplikacji, m.in. klucz do obsługi sesji HTTP wymaganej
# przez funkcję flash
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    TYTUL='Quiz 2 Peewee'
))

# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('quiz.db')


@app.before_request
def before_request():
    g.db = baza
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response
