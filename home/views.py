from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


def public_home(request):
    return render(request,'public_home.html')

@login_required
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'registration/login.html')

def login_estudiante(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return redirect('public_home')

def salir(request):
    logout(request)
    return redirect('/')

