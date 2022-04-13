"""Models for users"""
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    brithday = models.DateField(blank=True, null = True)