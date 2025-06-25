from django.urls import path
from . import views
urlpatterns = [
    path('PrediccionFirmas', views.PrediccionFirmas, name='PrediccionFirmas'),
    path('PredecirFirma', views.PredecirFirma, name='PredecirFirma')
]