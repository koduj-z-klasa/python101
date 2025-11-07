from django.urls import path
from . import views  # import widoków aplikacji

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='index'),
]
