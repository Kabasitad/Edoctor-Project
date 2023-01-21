from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect


from django.contrib.auth import authenticate ,login
from django.contrib import messages
# Create your views here.


def home(response):
	return render(response, "main/home.html", {})


def added(response):
	return render(response, "main/added.html", {})

#def orderloan(response):
	