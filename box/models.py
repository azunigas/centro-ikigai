from django.db import models

# Create your models here.


class Box(models.Model):
    nombre = models.CharField(max_length=15)
    equipamiento = models.TextField(max_length=200)
    imagen = models.ImageField()

    def __str__(self):
        return self.nombre
