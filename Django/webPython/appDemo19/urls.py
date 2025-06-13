from django.urls import path
from . import views

urlpatterns = [
    path('GraficoBarras2D', views.GraficoBarras2D, name='GraficoBarras2D'),
    path('ConsultarStockProductos', views.ConsultarStockProductos, name='ConsultarStockProductos'),
]