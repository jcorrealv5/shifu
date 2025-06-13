from django.urls import path
from . import views

urlpatterns = [
    path('GraficoColumnas3D', views.GraficoColumnas3D, name='GraficoColumnas3D'),
    path('ConsultarStockProductos', views.ConsultarStockProductos, name='ConsultarStockProductos'),
]