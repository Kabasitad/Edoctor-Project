from django.forms import ModelForm
from main.models import Checkin

class CheckinForm(ModelForm):
    class Meta:
        model = Checkin
        fields = '__all__'
    
    
