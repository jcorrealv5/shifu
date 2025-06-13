from django.urls import path
from . import views

urlpatterns = [
    path('Chat', views.Chat, name='Chat'),
]