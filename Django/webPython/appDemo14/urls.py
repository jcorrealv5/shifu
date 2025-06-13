from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.Login, name='Login'),
    path('CrearCaptcha', views.CrearCaptcha, name='CrearCaptcha'),
    path('ValidarLogin', views.ValidarLogin, name='ValidarLogin'),
    path('Categorias', views.Categorias, name='Categorias'),
    path('ListarCodigos', views.ListarCodigos, name='ListarCodigos'),
    path('ObtenerImagenes', views.ObtenerImagenes, name='ObtenerImagenes'),
    path('Productos', views.Productos, name='Productos'),
    path('Detalles', views.Detalles, name='Detalles'),
    path('ObtenerStockProductoPorId', views.ObtenerStockProductoPorId, name='ObtenerStockProductoPorId'),
    path('GrabarOrden', views.GrabarOrden, name='GrabarOrden'),
]