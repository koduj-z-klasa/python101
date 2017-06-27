# -*- coding: utf-8 -*-
# czat/models.py

from django.db import models
from django.contrib.auth.models import User


class Wiadomosc(models.Model):

    """Klasa reprezentująca wiadomość w systemie"""
    tekst = models.CharField('treść wiadomości', max_length=250)
    data_pub = models.DateTimeField('data publikacji', auto_now_add=True)
    autor = models.ForeignKey(User)

    class Meta:  # ustawienia dodatkowe
        verbose_name = u'wiadomość'  # nazwa obiektu w języku polskim
        verbose_name_plural = u'wiadomości'  # nazwa obiektów w l.m.
        ordering = ['data_pub']  # domyślne porządkowanie danych

    def __str__(self):
        return self.tekst  # "autoprezentacja"
