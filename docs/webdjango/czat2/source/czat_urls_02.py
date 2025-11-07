from django.urls import path
from . import views  # import widoków aplikacji
from django.contrib.auth.decorators import login_required
from .models import Wiadomosc

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', login_required(views.ListaWiadomosci.as_view()), name='lista'),
    path('dodaj/', login_required(views.DodajWiadomosc.as_view()), name='dodaj'),
    path('edytuj/<pk>', login_required(views.EdytujWiadomosc.as_view()), name='edytuj'),
    path('usun/<pk>', login_required(views.UsunWiadomosc.as_view()), name='usun'),
]
