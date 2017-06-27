# -*- coding: utf-8 -*-
# czat/czat/models.py

from django.db import models
from django.contrib.auth.models import User


class Wiadomosc(models.Model):

    """Klasa reprezentująca wiadomość w systemie"""
    tekst = models.CharField(u'wiadomość', max_length=250)
    data_pub = models.DateTimeField(u'data publikacji')
    autor = models.ForeignKey(User)

    class Meta:  # ustawienia dodatkowe
        verbose_name = u'wiadomość'  # nazwa obiektu w języku polskim
        verbose_name_plural = u'wiadomości'  # nazwa obiektów w l.m.
        ordering = ['data_pub']  # domyślne porządkowanie danych

    def __unicode__(self):
        return self.tekst  # "autoprezentacja"
