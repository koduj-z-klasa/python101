from django.contrib import admin
from chatter.models import Message


# rejestrujeym nasz model w panelu administracyjnym
admin.site.register(Message)
