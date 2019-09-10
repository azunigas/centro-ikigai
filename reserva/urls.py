from django.urls import path
from . import views

app_name = 'reserva'

urlpatterns = [
    path('reserva/', views.index, name='resevas'),
]
