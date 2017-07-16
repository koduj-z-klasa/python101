# -*- coding: utf-8 -*-
# czat/views.py

from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.edit import CreateView
from czat.models import Wiadomosc
from django.utils import timezone
from django.contrib import messages
from django.views.generic.edit import UpdateView


def index(request):
    """Strona główna aplikacji."""
    # return HttpResponse("Witaj w aplikacji Czat!")
    return render(request, 'czat/index.html')


class DodajWiadomosc(CreateView):
    model = Wiadomosc
    fields = ['tekst', 'data_pub']
    context_object_name = 'wiadomosci'
    success_url = '/dodaj'

    def get_initial(self):
        initial = super(DodajWiadomosc, self).get_initial()
        initial['data_pub'] = timezone.now()
        return initial

    def get_context_data(self, **kwargs):
        context = super(DodajWiadomosc, self).get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.all()
        return context

    def form_valid(self, form):
        wiadomosc = form.save(commit=False)
        wiadomosc.autor = self.request.user
        wiadomosc.save()
        messages.success(self.request, "Dodano wiadomość!")
        return super(UtworzWiadomosc, self).form_valid(form)


class EdytujWiadomosc(UpdateView):
    model = Wiadomosc
    from czat.forms import EdytujWiadomoscForm
    form_class = EdytujWiadomoscForm
    context_object_name = 'wiadomosci'
    template_name = 'czat/wiadomosc_form.html'
    success_url = '/wiadomosci'

    def get_context_data(self, **kwargs):
        context = super(EdytujWiadomosc, self).get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.filter(
            autor=self.request.user)
        return context

    def get_object(self, queryset=None):
        wiadomosc = Wiadomosc.objects.get(id=self.kwargs['pk'])
        return wiadomosc
