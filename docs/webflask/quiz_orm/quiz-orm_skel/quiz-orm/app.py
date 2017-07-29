# -*- coding: utf-8 -*-
# quiz-orm/app.py

from flask import Flask

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    TYTUL='Quiz ORM SQLAlchemy'
))
