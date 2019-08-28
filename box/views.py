from django.shortcuts import render
from .models import Box
from django.views import generic

# Create your views here.


class BoxView(generic.ListView):
    template_name = 'box/index.html'
    context_object_name = 'box'

    def get_queryset(self):
        return Box.objects.all()

