# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import forms, authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from chatter.models import Message
#from chatter.forms import MessageForm
from django.utils import timezone


def index(request):
    """Strona glowna aplikacji."""
    context = {'user': request.user}
    print context['user'].username
    return render(request, 'chatter/index.html', context)


def my_login(request):
    """Logowanie uzytkownika w ssytemie."""
    # ustawimy formularz logowania
    form = forms.AuthenticationForm()

    # jezeli mamy POST, to znaczy, ze ktos probuje sie zalogowac
    if request.method == 'POST':
        # przypisujemy nadeslane dane do formularza logowania
        form = forms.AuthenticationForm(request, request.POST)
        # sprawdzamy poprawnosc formularza lub zwracamy informacje o bledzie
        if form.is_valid():
            # jezeli wszystko jest ok, to logujemy uzytkownika
            user = form.get_user()
            login(request, user)
            # na koniec przekierowujemy uzytkownika na strone glowna 
            return redirect(reverse('index'))

    # ustawiamy zmienne przekazywane do templatki
    context = {'form': form}
    # renderujemy templatke logowania
    return render(request, 'chatter/login.html', context)


def my_register(request):
    """Rejestracja nowego uzytkownika."""
    # ustawiamy formularz rejestracji
    form = forms.UserCreationForm()

    # jezeli mamy do czynienia z POST, to znaczy, ze ktos
    # probuje utworzyc nowego uzytkownika
    if request.method == 'POST':
        # przypisujemy nadeslane dane do formularza tworzenia uzytkownika
        form = forms.UserCreationForm(request.POST)
        # sprawdzamy poprawnosc nadeslanych danych:
        # - jezeli wszystko jest wporzadku to tworzymy uzytkownika
        # - w przeciwnym razie zwracamy formularz wraz z informacja o bledach
        if form.is_valid():
            # zapamietujemy podana nazwe uzytkownika i haslo
            username = form.data['username']
            password = form.data['password1']
            # zapisujemy formularz tworzac nowego uzytkownika
            form.save()
            # uwierzytelniamy uzytkownika
            user = authenticate(username=username, password=password)
            login(request, user)
            # po udanyej rejestracji, przekierowujemy go na strone glowna
            return redirect(reverse('index'))

    # ustawiamy zmienne przekazywane do templatki
    context = {'form': form}
    # renderujemy templatke rejestracji
    return render(request, 'chatter/register.html', context)


def my_logout(request):
    """Wylogowywanie uzytkownika z systemu"""
    logout(request)
    # przekierowujemy na strone glowna
    return redirect(reverse('index'))


# dekorator, ktory "chroni" nasz widok przed dostepem przez osoby niezalogowane
# jezeli uzytkonik nielogowany bedzie probowal odwiedzic ten widok, to
# zostanie przekierowany na strone logowania
@login_required(login_url='/login')
def messages(request):
    """Widok wiadomosci."""
    error = None

    # jezeli mamy do czynienia z POST. to znaczy, ze ktos probuje
    # dodac nowa wiadomosc w systemie
    if request.method == 'POST':
        # pobieramy tresc przeslanej wiadomosci
        text = request.POST.get('text', '')
        # sprawdzamy, czy nie jest ona dluzna od 250 znakow:
        # - jezeli jest dluzsza, to zwracamy blad
        # - jezeli jest krotsza lub rown, to zapisujemy ja w systemie
        if not 0 < len(text) < 250:
            error = u'Wiadomość jest dłuższa niż 250 znaków'
        else:
            # ustawiamy dane dla modelu Message
            msg = Message(text=text, pub_date=timezone.now(), user=request.user)
            # zapisujemy nowa widomosc
            msg.save()
            # po udanym zapisie przekierowujemy na strone wiadomosci
            return redirect(reverse('messages'))

    # pobieramy informacje o aktualnie zalogowanym uzytkowniku
    user = request.user
    # pobieramy wszystkie wiadomosci
    messages = Message.objects.all()
    # ustawiamy zmienne przekazywane do templatki
    context = {'user': user, 'messages': messages, 'error': error}
    # renderujemy templatke wiadomosci
    return render(request, 'chatter/messages.html', context)
