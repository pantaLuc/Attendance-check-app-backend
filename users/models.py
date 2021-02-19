from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastnane = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
