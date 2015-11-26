# -*- coding: utf-8 -*-
# czatpro/czat/views.py

from django.http import HttpResponse


def index(request):
    """Strona główna aplikacji."""
    return HttpResponse("Witaj w aplikacji Czat!")
