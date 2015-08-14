# -*- coding: utf-8 -*-
# czatpro/czat/urls.py

from django.conf.urls import url
from czat import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loguj/$', views.loguj, name='loguj'),
    url(r'^wyloguj/$', views.wyloguj, name='wyloguj'),
    url(r'^wiadomosci/$', views.wiadomosci, name='wiadomosci'),
    url(r'^wiadomosc/$', login_required(
        views.UtworzWiadomosc.as_view(),
        login_url='/loguj'), name='wiadomosc'),
    url(r'^wiadomosc-usun/(?P<pk>\d+)/$', login_required(
        views.UsunWiadomosc.as_view(),
        login_url='/loguj'), name='wiadomosc-usun'),
]
