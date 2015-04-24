# -*- coding: utf-8 -*-
# czat/czat/views.py

#from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """Strona główna aplikacji."""
    #return HttpResponse("Witaj w aplikacji Czat!")
    kontekst = {'user': request.user}
    return render(request, 'czat/index.html', kontekst)

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def rejestruj(request):
    """Rejestracja nowego użytkownika."""
    from django.contrib.auth.forms import UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Zostałeś zarejestrowany.")
            user = authenticate(
                    username=form.data['username'],
                    password=form.data['password1'])
            login(request, user)
            messages.success(request, "Zostałeś zalogowany.")
            return redirect(reverse('index'))

    kontekst = {'form': UserCreationForm()}
    return render(request, 'czat/rejestruj.html', kontekst)
