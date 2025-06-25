from django.urls import path
from . import views
urlpatterns = [
    path('ClasDigitos', views.ClasDigitos, name='ClasDigitos'),
    path('ClasificarDigito', views.ClasificarDigito, name='ClasificarDigito')
]