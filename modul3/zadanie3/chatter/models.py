# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """Klasa reprezentujaca wiadomosc w systemie."""
    text = models.CharField(u'wiadomość', max_length=250)
    pub_date = models.DateTimeField(u'data publikacji')
    user = models.ForeignKey(User)

    class Meta:
        # konfigurujemy nazwe modelu w jezyku polskim
        verbose_name = u'wiadomość'
        # konfigurujemy nazwe modelu w liczbie monogiej 
        verbose_name_plural = u'wiadomości'
        # konfigurujemy sposob porzadkowania danych modelu
        ordering = ['pub_date'] # porzadkowanie wzgledem daty
