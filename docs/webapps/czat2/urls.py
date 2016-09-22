# -*- coding: utf-8 -*-
# czatpro2/czat/urls.py

from django.conf.urls import url
from czat import views  # importujemy zdefiniowane w pliku views.py widoki
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from czat.models import Wiadomosc
from django.views.generic import DeleteView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rejestruj/', CreateView.as_view(
        template_name='czat/rejestruj.html',
        form_class=UserCreationForm,
        success_url='/'), name='rejestruj'),
    url(r'^loguj/', auth_views.login,
        {'template_name': 'czat/loguj.html'},
        name='loguj'),
    url(r'^wyloguj/', auth_views.logout,
        {'next_page': reverse_lazy('czat:index')},
        name='wyloguj'),
    url(r'^wiadomosci/', login_required(
        ListView.as_view(
            model=Wiadomosc,
            context_object_name='wiadomosci',
            paginate_by=10),
        login_url='/loguj'),
        name='wiadomosci'),
    url(r'^wiadomosc/$', login_required(
        views.UtworzWiadomosc.as_view(),
        login_url='/loguj'),
        name='wiadomosc'),
    url(r'^edytuj/(?P<pk>\d+)/', login_required(
        views.EdytujWiadomosc.as_view(),
        login_url='/loguj'),
        name='edytuj'),
    url(r'^usun/(?P<pk>\d+)/', login_required(
        DeleteView.as_view(
            model=Wiadomosc,
            template_name='czat/wiadomosc_usun.html',
            success_url='/wiadomosci'),
        login_url='/loguj'),
        name='usun'),
]
