from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola, esta es la View saludo!")

def saludo_html(request):
    documento="""<html><body><h1>Hola a todos! Esta es la View saludo_html</h1></body></html>"""
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Adiós! Esta es la view despedida!")

def get_fecha(request):
    fecha_actual = datetime.datetime.now()
    documento="""<html><body><h1>Fecha: %s</h1></body></html>"""%fecha_actual
    return HttpResponse(documento)

def calcular_edad(request,edad,anio): 
    print("Este es el request: ", request)
    periodo=anio-datetime.datetime.now().year
    edad_futura=edad+periodo 
    documento="<html><body><h2>En el año %s tendrás %s años"%(anio,edad_futura) 
    return HttpResponse(documento)

def template(request):
    archivo = open("C:/Users/User/Desktop/CodoACodo-Back/CodoACodoBack/templates/plantilla.html")
    plt = Template(archivo.read())
    archivo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def template_dinamico(request):
    nombre="Juan" 
    apellido= "Gonzalez" 
    fecha = datetime.datetime.now() 
    archivo = open("C:/Users/User/Desktop/CodoACodo-Back/CodoACodoBack/templates/plantilla_dinamica.html")
    plt=Template(archivo.read())
    archivo.close() 
    ctx=Context({"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha}) 
    documento=plt.render(ctx) 
    return HttpResponse(documento)

def template_lista(request):
    temas=["Plantillas","Modelos","Formularios","Vistas"] 
    archivo = open("C:/Users/User/Desktop/CodoACodo-Back/CodoACodoBack/templates/plantilla_lista.html")
    plt=Template(archivo.read())
    archivo.close()
    ctx=Context({"temas_curso":temas}) 
    documento=plt.render(ctx) 
    return HttpResponse(documento)
