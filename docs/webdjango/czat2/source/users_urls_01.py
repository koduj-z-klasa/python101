from django.urls import path
from . import views

app_name = 'users'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='index'),
]
