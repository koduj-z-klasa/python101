# -*- coding: utf-8 -*-
# czatpro/czat/urls.py

from django.conf.urls import url
from czat import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
