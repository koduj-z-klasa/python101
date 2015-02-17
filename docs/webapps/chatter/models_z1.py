# -*- coding: utf-8 -*-

# chatter/chatter/models.py

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """Klasa reprezentujaca wiadomosc w systemie."""
    text = models.CharField(u'wiadomość', max_length=250)
    pub_date = models.DateTimeField(u'data publikacji')
    user = models.ForeignKey(User)

    class Meta: # to jest klasa w klasie
        verbose_name = u'wiadomość' # nazwa modelu w jezyku polskim
        verbose_name_plural = u'wiadomości' #  nazwe modelu w l. mnogiej
        ordering = ['pub_date'] # porzadkowanie danych wzgledem daty
