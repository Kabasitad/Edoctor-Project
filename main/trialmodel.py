'''from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    number = forms.IntegerField()
    

    class Meta:
        model = User
        fields = ["firstname", "lastname","username","number", "email", "password1", "password2"]

class Checkin(forms.Form):
	sickness = forms.CharField(label = "sickness",max_length= 200)

	def __str__(self):
		return self.sickness
	

class Medicine(forms.Form):
	
	meds = forms.CharField(label = "meds",max_length= 200)
	complete = forms.BooleanField() 

	def __str__(self):
		return self.text


class OrderLoan(forms.Form):
	 
	orderloan = forms.IntegerField()
	complete = forms.BooleanField()

'''