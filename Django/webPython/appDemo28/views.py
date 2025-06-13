from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL
import os

def CargaMasiva(request):    
    return render(request, "appDemo28/CargaMasiva.html", {"Ver": "1.0001"})   

@xframe_options_exempt
def ValidarTablaCampos(request):
    tabla = request.POST.get("tabla")
    campos = request.POST.get("campos").split(",")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo28.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    rpta = con.ValidarTablaCampos(tabla, campos)
    return HttpResponse(rpta)

@xframe_options_exempt
def GrabarBloqueRegistros(request):
    tabla = request.POST.get("tabla")
    data = request.POST.get("data")
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo28.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    rpta = con.EjecutarInsertMasivoCsv(tabla, data, ";", ",")
    return HttpResponse(rpta)