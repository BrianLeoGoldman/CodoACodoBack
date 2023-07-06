from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    telefono = models.CharField(max_length=7)

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()
    def __str__(self): 
        return 'Nombre: %s - Sección: %s - Precio: %s' % (
        self.nombre, self.seccion, self.precio)

class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
