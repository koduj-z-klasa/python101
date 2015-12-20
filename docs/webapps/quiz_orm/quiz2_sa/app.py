# -*- coding: utf-8 -*-
# quiz_sa/app.py

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# konfiguracja aplikacji, m.in. klucz do obsługi sesji HTTP wymaganej
# przez funkcję flash
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    SQLALCHEMY_DATABASE_URI='sqlite:///quiz.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    TYTUL='Quiz 2 SQLAlchemy'
))

# tworzymy instancję bazy używanej przez modele
baza = SQLAlchemy(app)
