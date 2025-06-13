from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL
import os

def Consulta(request):    
    return render(request, "appDemo15/Consulta.html", {"Ver": "1.0001"})   

def ConsultarOrdenesPorRango(request):
    idOrdenInicio = request.GET.get("inicio")
    idOrdenFin = request.GET.get("fin")
    pars = idOrdenInicio + "|" + idOrdenFin
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo11.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspOrdenConsultarPorRangoPyCsv","IdOrdenes",pars) 
    return HttpResponse(data)