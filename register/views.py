# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from main.forms import Checkin
# Create your views here.

def registerPage(request):
    
    '''if request.user.is_authenticated:
        return redirect('login')
    
    else:
    '''
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
        return redirect("register")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form":form})


def loginPage(request):
    '''if request.user.is_authenticated:
        return redirect('home1')
    else:
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate (request, username =username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home1')
        
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, "register/login.html", {})

    return render(request, "register/home1.html", {"form": Checkin()})

def logoutUser(request):
    logout(request)
    return redirect('login')


