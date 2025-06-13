from django.urls import path
from . import views

urlpatterns = [
    path('AnimacionTexto', views.AnimacionTexto, name='AnimacionTexto'),
]