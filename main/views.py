from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from .forms import Checkin

from django.contrib.auth import authenticate ,login
from django.contrib import messages
# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	return render(request, "main/home.html", {})


@login_required(login_url ='login/')
def home1Page(response):
	if response.method == "POST":
		form = Checkin(response.POST)

		if form.is_valid():

			sk = form.cleaned_data["sickness"]
			sickness = Checkin(sickness = sk)

			md = form.cleaned_data["meds"]
			meds = Checkin(meds = md)

			lo = form.cleaned_data["orderloan"]
			orderloan = Checkin(orderloan = lo)

			sickness.save()
			meds.save()
			orderloan.save()

		return render(response, "main/home1.html", {})

	else:
		form = Checkin()

	return render(response, "main/home1.html", {"form":form})
