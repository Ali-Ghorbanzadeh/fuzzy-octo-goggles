from django.shortcuts import render, HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    return render(request, 'index.html', {'form': UserForm})


def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    user._last_name = user.last_name
    user._last_login = user.last_login
    # user.last_name = 'gh5'
    # user.save()
    if user:
        login(request, user)
    return HttpResponse('<h1>OK</h1>')
