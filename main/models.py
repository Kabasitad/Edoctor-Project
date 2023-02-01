from django.db import models

class Checkin(models.Model):
    sickness = models.CharField(max_length= 200)
    meds = models.CharField(max_length= 200)
    orderloan = models.IntegerField()

def __str__(self):
		return self.sickness + ' ' + self.orderloan
