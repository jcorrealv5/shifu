from django.urls import path
from . import views

urlpatterns = [
    path('Consulta', views.Consulta, name='Consulta'),
    path('ListarProductos', views.ListarProductos, name='ListarProductos'),
]