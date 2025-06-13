from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL
import os

def GraficoBarras3D(request):    
    return render(request, "appDemo24/GraficoBarras3D.html", {"Ver": "1.0001"})
    
def ConsultarStockProductos(request):
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo24.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspCategoriaProductosStockPyCsv") 
    return HttpResponse(data)