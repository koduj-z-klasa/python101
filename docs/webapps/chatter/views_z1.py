# -*- coding: utf-8 -*-
# czat/czat/views.py

# HttpResponse pozwala zwracac proste wiadomości tekstowe
from django.http import HttpResponse
from django.shortcuts import render # render pozwala zwracac szablony

def index(request):
    """Strona glowna aplikacji."""
    # aby wyświetlić (zwrócić) prosta wiadomosc tekstowa wystarczyłaby instrukcja poniżej:
    #return HttpResponse("Hello, SWOI")
    # my zwrócimy szablon index.html, uwaga (!) ścieżkę podajemy względną do katalogu templates :
    return render(request, 'chatter/index.html')
