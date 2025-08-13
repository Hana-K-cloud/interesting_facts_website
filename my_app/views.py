from django.contrib.auth import authenticate, login, logout
from .form import *
from django.shortcuts import render, redirect



# Create your views here.
def home(request):
    return render(request, 'my_app/index.html')


def signup(request):
    # post method
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home', {'form': form})

    # get method
    form = SignupForm
    return render(request, 'registration/signup.html', {'form': form})
