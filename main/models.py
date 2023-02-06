from django.db import models
from django.utils import timezone

class Checkin(models.Model):
    
    sickness = models.CharField("Sickness",max_length= 200)
    checkin_time = models.DateTimeField("Check-in Date" , default= timezone.now)
    meds = models.TextField("Medication",)
    meds_time = models.TimeField("Set Medication Alert Time", default= timezone.now)

   
def __str__(self): 
		return self.sickness
