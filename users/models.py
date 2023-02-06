from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    number = models.IntegerField(default = 0)
    firstname = models.CharField(default = '',max_length=200)
    lastname = models.CharField(default = '',max_length=200)
    
    def __str__(self):
        return self.username