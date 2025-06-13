from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL
import os

def AnimacionTexto(request):    
    return render(request, "appDemo17/AnimacionTexto.html", {"Ver": "1.0001"}) 