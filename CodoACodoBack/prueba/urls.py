from django.urls import path
from . import views

urlpatterns = [
    path("saludo/", views.saludo),
    path("saludohtml/", views.saludo_html),
    path("despedida/", views.despedida),
    path("fecha/", views.get_fecha),
    path("edades/<int:edad>/<int:anio>", views.calcular_edad),
    path("template/", views.template),
    path("templatedinamico/", views.template_dinamico),
    path("templatelista/", views.template_lista),
    path("templateloader/", views.template_with_loader),
    path("herencia/", views.herencia_template),
    path('busqueda_productos/', views.busqueda_productos), 
    path('buscar/', views.buscar),
    path('contacto/', views.contacto)
]