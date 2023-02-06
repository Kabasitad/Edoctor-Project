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
    
    if request.user.is_authenticated:
        return redirect('home1')
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"Account was successfully created for {user.username}")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)


        return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form":form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate (request, username =username, password = password)

        if user is not None:

            login(request, user)
            return redirect('main:home1')
                                                        
    
    return render(request, "register/login.html", {})
   
def logoutUser(request):
    logout(request)
    return redirect('register:login')
