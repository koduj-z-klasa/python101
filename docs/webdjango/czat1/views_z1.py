# -*- coding: utf-8 -*-
# czat/views.py

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Strona główna aplikacji."""
    return HttpResponse("Witaj w aplikacji Czat!")
