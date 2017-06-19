# -*- coding: utf-8 -*-
# czat/urls.py

from django.conf.urls import url
from . import views  # import widoków aplikacji

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loguj/$', views.loguj, name='loguj'),
    url(r'^wyloguj/$', views.wyloguj, name='wyloguj'),
    url(r'^wiadomosci/$', views.wiadomosci, name='wiadomosci'),
]
