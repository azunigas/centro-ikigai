from django.shortcuts import render
from .models import Box, Mensaje
from django.views import generic
from django.http import HttpResponse

# Create your views here.


class BoxView(generic.ListView):
    template_name = 'box/index.html'
    context_object_name = 'box'

    def get_queryset(self):
        return Box.objects.all()


def consultaView(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        correo = request.POST.get('correo', '')
        mensaje = request.POST.get('mensaje', '')
        mensaje = Mensaje.objects.create(nombre=nombre, correo=correo, mensaje=mensaje)
        mensaje.save()
        return HttpResponse('')
