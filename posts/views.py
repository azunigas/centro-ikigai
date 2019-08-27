from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Feed
from rest_framework import viewsets
from .serializers import FeedSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group
import json


# Create your views here.
def index(request):
    results = Feed.objects.all()
    jsondata = serializers.serialize('json', results)
    context = {
        'results': results,
        'jsondata': jsondata,
    }
    return render(request, 'posts/index.html', context)


def getdata(request):
    results = Feed.objects.all()
    jsondata = serializers.serialize('json', results)
    return HttpResponse(jsondata)


def base_layout(request):
    return render(request, 'posts/base.html')


class FeedView(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
