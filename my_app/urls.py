from django.contrib import admin
from django.urls import path

from my_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('saved_facts/<user>', views.saved_facts, name='saved_facts'),
    path('profile/<user>', views.profile, name='profile'),
    path('add_fact/<int:id>', views.add_fact, name='add_fact'),
    path('add_to_save_fact/<int:id>/<int:f_id>', views.add_to_save_fact, name='add_to_save_fact'),
]
