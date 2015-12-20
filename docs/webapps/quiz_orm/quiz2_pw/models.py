# -*- coding: utf-8 -*-
# quiz_pw/models.py

from app import baza
from peewee import *


class BaseModel(Model):

    class Meta:
        database = baza


class Pytanie(BaseModel):
    pytanie = CharField(unique=True)
    odpok = CharField()


class Odpowiedz(BaseModel):
    pnr = ForeignKeyField(
        Pytanie, related_name='odpowiedzi', on_delete='CASCADE')
    odpowiedz = CharField()
