from django.contrib import admin
from django.urls import path

from my_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('saved_facts', views.saved_facts, name='saved_facts'),
    path('profile', views.profile, name='profile'),
]
