# -*- coding: utf-8 -*-
# czat/czat/views.py

#from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Strona główna aplikacji."""
    #return HttpResponse("Witaj w aplikacji Czat!")
    return render(request, 'czat/index.html')
