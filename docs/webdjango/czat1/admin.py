# -*- coding: utf-8 -*-
# czatpro/czat/admin.py

from django.contrib import admin
from czat import models  # importujemy nasz model

# rejestrujemy model Wiadomosc w panelu administracyjnym
admin.site.register(models.Wiadomosc)
