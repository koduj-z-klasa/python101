# -*- coding: utf-8 -*-
# quiz-orm/models.py

from peewee import *
from app import baza


class BaseModel(Model):
    class Meta:
        database = baza


class Pytanie(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()

    def __str__(self):
        return self.pytanie


class Odpowiedz(BaseModel):
    pnr = ForeignKeyField(
        Pytanie, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()

    def __str__(self):
        return self.odpowiedz
