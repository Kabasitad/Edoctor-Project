from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Checkin(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	sickness = models.CharField(null= True, blank = True, default = "None",max_length= 200)

	def __str__(self):
		return self.sickness
	

class Medicine(models.Model):
	checkin = models.ForeignKey(Checkin, on_delete=models.CASCADE) 
	text = models.CharField(null= True, blank = True,max_length= 200, default= "None")
	complete = models.BooleanField() 

	def __str__(self):
		return self.text


class OrderLoan(models.Model):
	checkin = models.ForeignKey(Checkin, on_delete=models.CASCADE) 
	orderloan = models.IntegerField(default=0)
	complete = models.BooleanField()