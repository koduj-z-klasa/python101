# -*- coding: utf-8 -*-
# czatpro/czat/urls.py

from django.conf.urls import url
from czat import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loguj/$', views.loguj, name='loguj'),
    url(r'^wyloguj/$', views.wyloguj, name='wyloguj'),
    url(r'^wiadomosci/$', views.wiadomosci, name='wiadomosci'),
]
