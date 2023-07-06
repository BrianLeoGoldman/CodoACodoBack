from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from marylu.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username__exact=username)
        if user.exists() and check_password(password, user[0].password):
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
                hashed_password = make_password(password)
                new_user = User(username=username, password=hashed_password, email=email)
                new_user.save()
                return HttpResponse('New user created successfully')
            except ValidationError as e:
                return HttpResponse('There was an error: {}'.format(str(e)))
    else:
        return HttpResponse('Method not allowed')
    
