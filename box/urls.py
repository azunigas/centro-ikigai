from django.urls import path
from . import views


app_name = 'box'

urlpatterns = [
    path('', views.BoxView.as_view(), name='boxview'),
    path('mensaje/', views.consultaView, name='consulta')
]
