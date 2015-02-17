# -*- coding: utf-8 -*-

# chatter/chatter/admin.py

from django.contrib import admin
from chatter.models import Message # importujemy nasz model

admin.site.register(Message) # rejestrujemy nasz model w panelu administracyjnym
