from django.contrib.auth.models import User
from django.shortcuts import render

def index(request):
    users = User.objects.all()
    kontekst = {'users': users}
    return render(request, 'users/index.html', kontekst)
