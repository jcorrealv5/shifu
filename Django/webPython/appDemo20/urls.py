from django.urls import path
from . import views

urlpatterns = [
    path('GraficoBarras3D', views.GraficoBarras3D, name='GraficoBarras3D'),
    path('ConsultarStockProductos', views.ConsultarStockProductos, name='ConsultarStockProductos'),
]