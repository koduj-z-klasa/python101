from django.conf.urls import patterns, include, url
from django.contrib import admin

from chatter import views

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chatter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.my_login, name='login'),
    url(r'^logout/$', views.my_logout, name='logout'),
    url(r'^register/$', views.my_register, name='register'),
    url(r'^messages/$', views.messages, name='messages'),

    url(r'^admin/', include(admin.site.urls)),
)
