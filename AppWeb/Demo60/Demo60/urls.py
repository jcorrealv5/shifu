from django.urls import path
from . import views
urlpatterns = [
    path('ClasDigito0', views.ClasDigito0, name='ClasDigito0'),
    path('ClasificarDigito0', views.ClasificarDigito0, name='ClasificarDigito0')
]