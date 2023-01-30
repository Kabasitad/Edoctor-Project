from django import forms

class Checkin(forms.Form):
    sickness = forms.CharField(max_length= 200)
    meds = forms.CharField(max_length= 200)
    orderloan = forms.IntegerField()

    
