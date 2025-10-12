from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)


class User(AbstractUser):
 # add fields you need
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    