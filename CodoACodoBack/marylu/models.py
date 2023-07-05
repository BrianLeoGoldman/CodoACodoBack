from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=128)
    email = models.EmailField(blank=True,null=True)
