# -*- coding: utf-8 -*-
# chatter/chatter/views.py

# HttpResponse pozwala zwracac proste wiadomości tekstowe
from django.http import HttpResponse
# render pozwala zwracac szablony
from django.shortcuts import render
# dodajemy nowe importy
from django.shortcuts import render, redirect
from django.contrib.auth import forms, authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

def index(request):
    """Strona glowna aplikacji."""
    # tworzymy zmienną (słownik), zawierającą informacje o użytkowniku
    context = {'user': request.user}
    # zmienna context przekaujemy do szablonu index.html
    return render(request, 'chatter/index.html', context)

def my_login(request):
    """Logowanie uzytkownika w sytemie."""
    form = forms.AuthenticationForm() # ustawiamy formularz logowania

    if request.method == 'POST': # sprawdzamy, czy ktos probuje sie zalogowac
        # przypisujemy nadeslane dane do formularza logowania
        form = forms.AuthenticationForm(request, request.POST)
        # sprawdzamy poprawnosc formularza lub zwracamy informacje o bledzie
        if form.is_valid(): # jezeli wszystko jest ok – logujemy uzytkownika
            user = form.get_user()
            login(request, user)
            return redirect(reverse('index')) # przekierowujemy uzytkownika na strone glowna

    context = {'form': form} # ustawiamy zmienne przekazywane do templatki
    # renderujemy templatke logowania
    return render(request, 'chatter/login.html', context)

