from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(index),name='home'),
    path('salir/', salir,name='salir')
]