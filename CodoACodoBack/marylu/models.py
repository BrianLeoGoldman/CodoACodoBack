from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.EmailField(blank=True,null=True)
    last_login = models.DateTimeField(null=True, blank=True)
