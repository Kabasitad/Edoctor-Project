from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Checkin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    sickness = models.CharField(null= True, blank = True, default = "None",max_length= 200)
    meds = models.CharField(null= True, blank = True,max_length= 200, default= "None")
    orderloan = models.IntegerField(default=0)

    def __str__(self):
        return self.sickness


