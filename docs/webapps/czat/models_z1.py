# -*- coding: utf-8 -*-
# czatpro/czat/models.py

from django.db import models
from django.contrib.auth.models import User


class Wiadomosc(models.Model):

    """Klasa reprezentująca wiadomość w systemie"""
    tekst = models.CharField(max_length=250)
    data_pub = models.DateTimeField()
    autor = models.ForeignKey(User)
