from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    email = forms.EmailField()
    number = forms.IntegerField()
    

    class Meta:
        model = get_user_model()
        fields = ["firstname", "lastname","username","number", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.firstname= self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.number = self.cleaned_data['number']

        if commit:
            user.save()
        return user
