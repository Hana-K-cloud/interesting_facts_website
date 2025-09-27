from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import SignupForm, AddFact
from django.shortcuts import render, redirect
from .models import Fact, SavedFact
from django.http import JsonResponse


# Create your views here.
def home(request):
    add_fact = AddFact()
    facts = Fact.objects.all().order_by('-id')
    return render(request, 'my_app/index.html', {'facts': facts, 'add_fact': add_fact})


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


def profile(request, user):
    add_fact = AddFact()
    facts = Fact.objects.all().order_by('-id')
    my_user = User.objects.get(username=user)
    return render(request, 'my_app/profile.html', {'my_user': my_user, 'facts': facts, 'add_fact': add_fact})


# add fact
def add_fact(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        fact = Fact.objects.create(
            user=user,
            topic=request.POST['topic'],
            fact=request.POST['fact'],
        )

        data = {
            'user': user.username,
            'topic': request.POST['topic'],
            'fact': request.POST['fact'],
        }
    return redirect('home')


def add_to_save_fact(request, id, f_id):
    user = get_object_or_404(User, id=id)
    fact = Fact.objects.get(id=f_id)
    new_fact = SavedFact.objects.create(
        user=user,
        fact=fact,
    )
    return redirect('home')


def saved_facts(request, user):
    user = get_object_or_404(User, username=user)
    s_facts = SavedFact.objects.filter(user=user).order_by('-id')
    return render(request, 'my_app/saved_facts.html', {'user': user, 's_facts': s_facts})
