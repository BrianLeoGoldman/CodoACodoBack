from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from gestionPedidos.forms import FormularioContacto
from gestionPedidos.models import Articulo

def home(request):
    return render(request,"home.html") 

def saludo(request):
    response = HttpResponse("¡Hola desde la API!")
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET"
    return response

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

def template_with_loader(request):
    nombre="Juan" 
    apellido= "Gonzalez" 
    fecha = datetime.datetime.now() 
    return render(
        request, 
        "plantilla_dinamica.html", 
        {"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha}
    )

def herencia_template(request):
    fecha = datetime.datetime.now()
    return render(request, "hijo.html", {"now": fecha})

def busqueda_productos(request): 
    return render(request,"busqueda_productos.html") 

def buscar(request): 
    if request.GET["prd"]: 
        producto=request.GET["prd"] 
        if len(producto)>20: 
            mensaje="Texto de búsqueda demasiado largo" 
        else: 
            articulos=Articulo.objects.filter(nombre__icontains=producto) 
        return render(request,"resultados_busqueda.html",{"articulos":articulos,"query":producto}) 
    else:
        mensaje="No has introducido ningún dato" 
        return HttpResponse(mensaje)

    
def contacto(request): 
    if request.method=="POST": 
        miFormulario=FormularioContacto(request.POST) 
        if miFormulario.is_valid(): 
            infForm=miFormulario.cleaned_data 
            #Realizar operación con los datos aquí e incluir gracias.html 
            return render(request,"gracias.html", {"respuestasFormulario":infForm}) 
    else: 
        miFormulario=FormularioContacto() 
    return render(request,"formulario_contacto.html",{"form":miFormulario})