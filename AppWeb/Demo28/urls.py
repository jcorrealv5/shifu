from django.urls import path
from . import views
urlpatterns = [
    path('RegistroFirmas', views.RegistroFirmas, name='RegistroFirmas'),
    path('GrabarFirma', views.GrabarFirma, name='GrabarFirma')
]