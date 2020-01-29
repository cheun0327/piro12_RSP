from django.contrib.auth import get_user_model
from django.shortcuts import render


def main(request):
    return render(request, 'account/main.html')


def login(request):
    return render(request, 'account/login.html')


def list(request):
    users = get_user_model().objects.all()
    return render(request, 'login/main.html', {'users': users})
