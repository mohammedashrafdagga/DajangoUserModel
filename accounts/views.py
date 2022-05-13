from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SingUpForm, UserForm, ProfileForm
from .models import Profile
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
            user = authenticate(username=username, password=password)
            print(user)
            login(request, user)
            return redirect('profile')

    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    name = str(profile.user.first_name) + ' ' + str(profile.user.last_name)
    return render(request, 'profile/profile.html', {'profile': profile, 'name': name})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    userform = UserForm(instance=request.user)
    profileform = ProfileForm(instance=profile)
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('profile')
    return render(request, 'profile/edit_profile.html', {'userform': userform, 'profileform': profileform})
