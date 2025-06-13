from django.urls import path
from . import views

urlpatterns = [
    path('ListarProductos', views.ListarProductos, name='ListarProductos'),
    path('ConsultarProducto', views.ConsultarProducto, name='ConsultarProducto'),
]