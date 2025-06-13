from django.urls import path
from . import views

urlpatterns = [
    path('AnimacionImagen', views.AnimacionImagen, name='AnimacionImagen'),
]