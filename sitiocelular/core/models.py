from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=80)
    sexo = models.CharField(max_length=1)
    correo = models.CharField(max_length=60)
    n_telefono = models.CharField(max_length=9)
    
    def __str__(self):
        return self.rut


class Celular(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=50)
    precio = models.IntegerField()
    cliente = models.ForeignKey(Cliente,on_delete=CASCADE)
    
    def __str__(self):
        return self.marca