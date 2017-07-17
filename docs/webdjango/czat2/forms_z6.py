# -*- coding: utf-8 -*-
# czat/forms.py

from django.forms import ModelForm, TextInput
from czat.models import Wiadomosc


class EdytujWiadomoscForm(ModelForm):
    class Meta:
        model = Wiadomosc
        fields = ['tekst', 'data_pub']
        exclude = ['autor']
        widgets = {'tekst': TextInput(attrs={'size': 60})}
