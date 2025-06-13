from django.urls import path
from . import views

urlpatterns = [
    path('Menu', views.Menu, name='Menu'),
    path('Acerca', views.Acerca, name='Acerca'),
    path('Productos', views.Productos, name='Productos'),
    path('Servicios', views.Servicios, name='Servicios')
]