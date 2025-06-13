from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL
import os

def AnimacionImagen(request):    
    return render(request, "appDemo18/AnimacionImagen.html", {"Ver": "1.0001"}) 