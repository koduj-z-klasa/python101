# -*- coding: utf-8 -*-
# chatter/chatter/views.py

from django.conf.urls import patterns, include, url
from django.contrib import admin

from chatter import views # importujemy zdefiniowane w pliku views.py widoki

admin.autodiscover()

urlpatterns = patterns('',
    # glowny adres (/) o nazwie index laczymy z widokiem index
    url(r'^$', views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
