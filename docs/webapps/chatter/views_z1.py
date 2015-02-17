# -*- coding: utf-8 -*-
# chatter/chatter/views.py

# HttpResponse pozwala zwracac proste wiadomości tekstowe
from django.http import HttpResponse
# render pozwala zwracac szablony
from django.shortcuts import render

def index(request):
    """Strona glowna aplikacji."""
    # aby wyświetlić (zwrócić) prosta wiadomosc tekstowa wystarczyłaby instrukcja poniżej:
    #return HttpResponse("Hello, SWOI")
    # my zwrócimy szablon index.html, uwaga (!) ścieżkę podajemy względną do katalogu templates :
    return render(request, 'chatter/index.html')
