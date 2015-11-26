# -*- coding: utf-8 -*-
# czatpro/czat/views.py

# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from czat.models import Wiadomosc
from django.utils import timezone
from django.views.generic.edit import CreateView


def index(request):
    """Strona główna aplikacji."""
    # return HttpResponse("Witaj w aplikacji Czat!")
    return render(request, 'czat/index.html')


def loguj(request):
    """Logowanie użytkownika"""
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Zostałeś zalogowany!")
            return redirect(reverse('czat:index'))

    kontekst = {'form': AuthenticationForm()}
    return render(request, 'czat/loguj.html', kontekst)


def wyloguj(request):
    """Wylogowanie użytkownika"""
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('czat:index'))


def wiadomosci(request):
    """Dodawanie i wyświetlanie wiadomości"""
    if request.method == 'POST':
        tekst = request.POST.get('tekst', '')
        if not 0 < len(tekst) <= 250:
            messages.error(
                request,
                "Wiadomość nie może być pusta, może mieć maks. 250 znaków!")
        else:
            wiadomosc = Wiadomosc(
                tekst=tekst,
                data_pub=timezone.now(),
                autor=request.user)
            wiadomosc.save()
            return redirect(reverse('wiadomosci'))

    wiadomosci = Wiadomosc.objects.all()
    kontekst = {'wiadomosci': wiadomosci}
    return render(request, 'czat/wiadomosci.html', kontekst)


class UtworzWiadomosc(CreateView):
    """Dodawanie wiadomości."""
    model = Wiadomosc
    fields = ['tekst', 'data_pub', 'autor']
    success_url = '/wiadomosc'

    def get_initial(self):
        initial = super(UtworzWiadomosc, self).get_initial()
        initial['data_pub'] = timezone.now()
        return initial

    def get_context_data(self, **kwargs):
        kwargs['wiadomosci'] = Wiadomosc.objects.filter(
                                autor=self.request.user)
        return super(UtworzWiadomosc, self).get_context_data(**kwargs)

    def form_valid(self, form):
        wiadomosc = form.save(commit=False)
        wiadomosc.autor = self.request.user
        wiadomosc.save()
        return super(UtworzWiadomosc, self).form_valid(form)
