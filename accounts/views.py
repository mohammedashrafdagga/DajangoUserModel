from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SingUpForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def registerUser(request):
    form = SingUpForm()
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            print(user)
            login(request, user)
            return redirect('profile')

    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    return render(request, 'registration/profile.html')
