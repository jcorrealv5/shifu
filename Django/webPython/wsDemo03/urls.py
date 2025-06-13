from django.urls import path
from . import views

urlpatterns = [
    path('Paint', views.Paint, name='Paint'),
]