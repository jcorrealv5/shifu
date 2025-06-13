from django.urls import path
from . import views

urlpatterns = [
    path('Consulta', views.Consulta, name='Consulta'),
    path('ListarArchivos', views.ListarArchivos, name='ListarArchivos'),
    path('ObtenerImagenes', views.ObtenerImagenes, name='ObtenerImagenes'),
]