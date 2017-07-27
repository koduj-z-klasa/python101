# -*- coding: utf-8 -*-
# quiz-orm/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# konfiguracja aplikacji, m.in. klucz do obsługi sesji HTTP wymaganej
# przez funkcję flash
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'quiz.db'),
    SQLALCHEMY_DATABASE_URI='sqlite:///' +
                            os.path.join(app.root_path, 'quiz.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    TYTUL='Quiz ORM SQLAlchemy'
))

# tworzymy instancję bazy używanej przez modele
baza = SQLAlchemy(app)
