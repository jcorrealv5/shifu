from django.urls import path
from . import views

urlpatterns = [
    path('Consulta', views.Consulta, name='Consulta'),
    path('ListarCodigosSizeImg', views.ListarCodigosSizeImg, name='ListarCodigosSizeImg'),
    path('ObtenerDataConImagenes', views.ObtenerDataConImagenes, name='ObtenerDataConImagenes'),
]