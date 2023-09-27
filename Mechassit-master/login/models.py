from django.db import models
from django.contrib.auth.models import User

class ExtendedData(models.Model):
    telefono = models.CharField(max_length=10, null=True,blank=True)
    direccion = models.CharField(max_length=128, null=True,blank=True)
    cp = models.CharField(max_length=5, null=True,blank=True)
    calidad = models.IntegerField(default=0,blank=True,null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE,blank=True)

class Vehiculos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    TIPOS_CHOICES = [
        ('carro', 'Carro'),
        ('bicicleta', 'Bicicleta'),
        ('moto', 'Moto'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPOS_CHOICES)
    modelo = models.CharField(max_length=10, null=True, blank=True)
    año = models.IntegerField(default=0, blank=True, null=True)

class Servicios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    SERVICIO_CHOICES = [
        ('mantenimiento y cambio de aceite', 'Mantenimiento y Cambio de Aceite'),
        ('frenos y sistemas de frenado', 'Frenos y Sistemas de Frenado'),
        ('alineación y balanceo de ruedas', 'Alineación y Balanceo de Ruedas'),
        ('sistema de escape', 'Sistema de Escape'),
        ('sistema eléctrico y electrónico', 'Sistema Eléctrico y Electrónico'),
        ('reparaciones de suspensión y amortiguación', 'Reparaciones de Suspensión y Amortiguación'),
    ]
    tipo = models.CharField(max_length=50, choices=SERVICIO_CHOICES)
    TIEMPO_CHOICES = [
        ('1 hora', '1 hora'),
        ('2 horas', '2 horas'),
        ('3 horas', '3 horas'),
        ('4 horas', '4 horas'),
        ('Más de 5 horas', 'Más de 5 horas'),
    ]
    tiempo = models.CharField(max_length=50, choices=TIEMPO_CHOICES)
    PRECIO_CHOICES = [
        ('$300 - $1,000', '$300 - $1,000'),
        ('$1,000', '$1,000'),
        ('$2,000', '$2,000'),
        ('$3,000', '$3,000'),
        ('$4,000', '$4,000'),
        ('$5,000 - $10,000', '$5,000 - $10,000'),
        ('$11,000 - $15,000', '$11,000 - $15,000'),
        ('Más de $16,000', 'Más de $16,000'),
    ]
    precio = models.IntegerField(max_length=50, choices=PRECIO_CHOICES)




