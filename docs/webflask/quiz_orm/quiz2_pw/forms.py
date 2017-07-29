# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'
blad2 = 'Brak zaznaczonej poprawnej odpowiedzi'


class DodajForm(FlaskForm):
    pytanie = StringField('Treść pytania:',
                          validators=[Required(message=blad1)])
    odpowiedzi = FieldList(StringField(
                           'Odpowiedź',
                           validators=[Required(message=blad1)]),
                           min_entries=3,
                           max_entries=3)
    odpok = RadioField(
        'Poprawna odpowiedź',
        validators=[Required(message=blad2)],
        choices=[('0', 'o0'), ('1', 'o1'), ('2', 'o2')]
    )
    pid = HiddenField("Pytanie id")
