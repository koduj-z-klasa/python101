# -*- coding: utf-8 -*-
# quiz-orm/models.py

from app import baza


class Pytanie(baza.Model):
    id = baza.Column(baza.Integer, primary_key=True)
    pytanie = baza.Column(baza.Unicode(255), unique=True)
    odpok = baza.Column(baza.Unicode(100))
    odpowiedzi = baza.relationship(
        'Odpowiedz', backref=baza.backref('pytanie'),
        cascade="all, delete, delete-orphan")

    def __str__(self):
        return self.pytanie


class Odpowiedz(baza.Model):
    id = baza.Column(baza.Integer, primary_key=True)
    pnr = baza.Column(baza.Integer, baza.ForeignKey('pytanie.id'))
    odpowiedz = baza.Column(baza.Unicode(100))

    def __str__(self):
        return self.odpowiedz
