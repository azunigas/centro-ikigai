from django.db import models

# Create your models here.


class Box(models.Model):
    nombre = models.CharField(max_length=15)
    equipamiento = models.TextField(max_length=170)
    proposito = models.TextField(max_length=150, default='')
    imagen = models.ImageField()

    def __str__(self):
        return self.nombre


class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    mensaje = models.TextField(max_length=170)

    def __str__(self):
        return self.correo
