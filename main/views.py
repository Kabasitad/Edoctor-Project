from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from .forms import CheckinForm

from django.contrib.auth import authenticate ,login
from django.contrib import messages
# Create your views here.

from django.contrib.auth.decorators import login_required
from .send_sms import sendsms


def home(request):
	return render(request, "main/home.html", {})


def home1(request):
	
	if request.method == "POST":
		form = CheckinForm(request.POST)

		if form.is_valid():
			form.save()
               
                 
			sendsms()
		return redirect('checkin')
	else:
		form = CheckinForm()
	

	return render(request, "main/home1.html", {"form":form})

def profile():
	pass
		

def orderloan():
	pass

def checkin(request):
	return render(request, "main/checkin.html", {})