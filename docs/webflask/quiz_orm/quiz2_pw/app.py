# -*- coding: utf-8 -*-
# quiz-orm/app.py

import os
from flask import Flask, g
from peewee import SqliteDatabase

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    TYTUL='Quiz ORM Peewee',
    DATABASE=os.path.join(app.root_path, 'quiz.db'),
))

# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = baza
    g.db.get_conn()


@app.after_request
def after_request(response):
    g.db.close()
    return response
