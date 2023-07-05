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
        print(usuario)
    response = HttpResponse("El metodo login se ejecuto!")
    #response["Access-Control-Allow-Origin"] = "*"
    #response["Access-Control-Allow-Methods"] = "POST"
    return response
