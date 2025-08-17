from django.contrib.auth import authenticate, login, logout
from .form import SignupForm
from django.shortcuts import render, redirect
from.models import Fact


# Create your views here.
def home(request):
    facts = Fact.objects.all().order_by('-id')
    return render(request, 'my_app/index.html',{'facts':facts})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=pwd)
            login(request, user)
            return redirect('home')

    form = SignupForm

    return render(request, 'registration/signup.html', {'form': form})


def saved_facts(request):
    return render(request, 'my_app/saved_facts.html')


def profile(request):
    return render(request, 'my_app/profile.html')