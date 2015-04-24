# -*- coding: utf-8 -*-
# czat/czat/views.py

from django.http import HttpResponse
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

def loguj(request):
    """Logowanie użytkownika"""
    from django.contrib.auth.forms import AuthenticationForm

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Zostałeś zalogowany!")
            return redirect(reverse('index'))

    kontekst = {'form': AuthenticationForm()}
    return render(request, 'czat/loguj.html', kontekst)

def wyloguj(request):
    """Wylogowanie użytkownika"""
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('index'))

from django.contrib.auth.decorators import login_required
from czat.models import Wiadomosc
from django.utils import timezone

@login_required(login_url='/loguj')
def wiadomosci(request):
    """Dodawanie i wyświetlanie wiadomości"""

    if request.method == 'POST':
        tekst = request.POST.get('tekst', '')
        if not 0 < len(tekst) <= 250:
            messages.error(request,
            "Wiadomość nie może być pusta, może mieć maks. 250 znaków!")
        else:
            wiadomosc = Wiadomosc(tekst=tekst,
                        data_pub=timezone.now(),
                        autor=request.user)
            wiadomosc.save()
            return redirect(reverse('wiadomosci'))

    wiadomosci = Wiadomosc.objects.all()
    kontekst = {'user': request.user, 'wiadomosci': wiadomosci}
    return render(request, 'czat/wiadomosci.html', kontekst)
