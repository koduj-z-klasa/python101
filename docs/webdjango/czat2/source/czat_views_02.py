from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .models import Wiadomosc
from django.utils import timezone
from django.contrib import messages


def index(request):
    return render(request, 'czat/index.html')


class ListaWiadomosci(ListView):
    model = Wiadomosc
    context_object_name = 'wiadomosci'
    paginate_by = 2


class DodajWiadomosc(CreateView):
    model = Wiadomosc
    fields = ['tekst', 'data_pub']
    context_object_name = 'wiadomosci'
    success_url = '/lista'

    def get_initial(self):
        initial = super(DodajWiadomosc, self).get_initial()
        initial['data_pub'] = timezone.now()
        return initial

    def form_valid(self, form):
        wiadomosc = form.save(commit=False)
        wiadomosc.autor = self.request.user
        wiadomosc.save()
        messages.success(self.request, "Dodano wiadomość!")
        return super(DodajWiadomosc, self).form_valid(form)


class EdytujWiadomosc(UpdateView):
    model = Wiadomosc
    from .forms import EdytujWiadomoscForm
    form_class = EdytujWiadomoscForm
    context_object_name = 'wiadomosci'
    template_name = 'czat/wiadomosc_form.html'
    success_url = '/lista'

    def get_context_data(self, **kwargs):
        context = super(EdytujWiadomosc, self).get_context_data(**kwargs)
        context['wiadomosci'] = Wiadomosc.objects.filter(
            autor=self.request.user)
        return context

    def get_object(self, queryset=None):
        wiadomosc = Wiadomosc.objects.get(id=self.kwargs['pk'])
        return wiadomosc


class UsunWiadomosc(DeleteView):
    model = Wiadomosc
    template_name = 'czat/wiadomosc_usun.html'
    success_url = '/lista'
