from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from marylu.models import User
import requests

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
    
def forgot(request):
    if request.method == 'POST':
        to_email = request.POST.get('email')
        try:
            url = "https://api.mailgun.net/v3/sandboxc3caf8202424427689614c22199faae7.mailgun.org/messages"
            api_key = "key-f5835c7389415a57be238545bce133d2"
            from_email = "Mailgun Sandbox <postmaster@sandboxc3caf8202424427689614c22199faae7.mailgun.org>"
            subject = "Marylu password recovery"
            html_content = """
            <html>
                <body>
                    <h1>This is an automatic email from the Marylu app to recover your password</h1>
                    <p>Currently, we cannot give you a link to recover your password...</p>
                    <p>Try to remember it or create a new account. Thanks!</p>
                </body>
            </html>
            """
            data = {
                "from": from_email,
                "to": to_email,
                "subject": subject,
                "html": html_content
            }
            response = requests.post(url, auth=("api", api_key), data=data)
            if response.status_code == 200:
                return HttpResponse("Email delivery successful")
            else:
                return HttpResponse("Error on email delivery:", response.text)
        except ConnectionRefusedError:
            print("Conection was refused")
            return HttpResponse("Conection was refused")
    else:
        return HttpResponse('Method not allowed')