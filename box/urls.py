from django.urls import path
from .views import boxview


urlpatterns = [
    path('', boxview, name='boxview')
]
