# -*- coding: utf-8 -*-
# czat/models.py

from django.db import models
from django.contrib.auth.models import User


class Wiadomosc(models.Model):

    """Klasa reprezentująca wiadomość w systemie"""
    tekst = models.CharField('treść wiadomości', max_length=250)
    data_pub = models.DateTimeField('data publikacji', auto_now_add=True)
    autor = models.ForeignKey(User)
