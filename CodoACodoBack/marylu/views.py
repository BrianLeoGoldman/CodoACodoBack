from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from marylu.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=User.objects.filter(username__exact=username, password__exact=password) 
        if user.exists():
            # Usuario encontrado en la base de datos
            return HttpResponse('Login successful')
        else:
            # Usuario no encontrado en la base de datos
            return HttpResponse('Wrong username or password')
    else:
        return HttpResponse('Method not allowed')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        old_user=User.objects.filter(username__exact=username) 
        if old_user.exists():
            # Usuario encontrado en la base de datos
            return HttpResponse('Username or email are already used')
        else:
            # Usuario no encontrado en la base de datos
            try:
                new_user = User(username=username, password=password, email=email)
                new_user.save()
                return HttpResponse('New user created successfully')
            except ValidationError as e:
                return HttpResponse('There was an error: {}'.format(str(e)))
    else:
        return HttpResponse('Method not allowed')