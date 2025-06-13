from django.urls import path
from . import views

urlpatterns = [
    path('Consulta', views.Consulta, name='Consulta'),
    path('ConsultarProductos', views.ConsultarProductos, name='ConsultarProductos'),
]