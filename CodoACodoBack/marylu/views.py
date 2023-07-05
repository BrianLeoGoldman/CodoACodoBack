from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from marylu.models import Usuario

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        contrasena = request.POST.get('contrasena')
        usuario=Usuario.objects.filter(username__exact=username, contrasena__exact=contrasena) 
        if usuario.exists():
            # Usuario encontrado en la base de datos
            return HttpResponse('Inicio de sesión exitoso')
        else:
            # Usuario no encontrado en la base de datos
            return HttpResponse('Nombre de usuario o contraseña incorrectos')
    else:
        return HttpResponse('Método no permitido')
