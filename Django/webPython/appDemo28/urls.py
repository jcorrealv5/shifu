from django.urls import path
from . import views

urlpatterns = [
    path('CargaMasiva', views.CargaMasiva, name='CargaMasiva'),
    path('ValidarTablaCampos', views.ValidarTablaCampos, name='ValidarTablaCampos'),
    path('GrabarBloqueRegistros', views.GrabarBloqueRegistros, name='GrabarBloqueRegistros'),
]