from django.urls import path
from . import views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='index'),
    path('rejestruj/', CreateView.as_view(
        template_name='users/rejestruj.html',
        form_class=UserCreationForm,
        success_url='/users/'),
        name="rejestruj"),
    path('loguj/', LoginView.as_view(
        template_name='users/loguj.html',
        next_page='users:index'),
        name='loguj'),
    path('wyloguj/', LogoutView.as_view(
        next_page='users:index'),
        name='wyloguj'),
]
