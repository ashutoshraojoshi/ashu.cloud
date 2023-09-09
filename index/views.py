from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView

# Create your views here.

def index(request):
    context = {
        'user': request.user  # Include the user variable in the context
    }
    return render(request, 'index.html', context)

def custom_login(request):
    if request.user.is_authenticated:
        # If user is already logged in, redirect to the profile page
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def sign_up(request):

    if request.user.is_authenticated:
        # If user is already logged in, redirect to the profile page
        return redirect('profile')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})

def profile(req):
    return render(req,'profile.html')
