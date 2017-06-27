# -*- coding: utf-8 -*-
# quiz_sa/models.py

from app import baza


class Pytanie(baza.Model):
    id = baza.Column(baza.Integer, primary_key=True)
    pytanie = baza.Column(baza.String(255), unique=True)
    odpok = baza.Column(baza.String(100))
    odpowiedzi = baza.relationship(
        'Odpowiedz', backref=baza.backref('pytanie'),
        cascade="all, delete, delete-orphan")


class Odpowiedz(baza.Model):
    id = baza.Column(baza.Integer, primary_key=True)
    pnr = baza.Column(baza.Integer, baza.ForeignKey('pytanie.id'))
    odpowiedz = baza.Column(baza.String(100))
