from django.shortcuts import render
from .models import Box
from django.views import generic

# Create your views here.


def boxview(request):
    box = Box.objects.all()
    return render(request, 'box/index.html', {'box': box})

