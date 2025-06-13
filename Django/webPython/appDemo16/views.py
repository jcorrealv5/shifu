from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from Modulos.modAccesoDatos import clienteSQL
import os

def Consulta(request):    
    return render(request, "appDemo16/Consulta.html", {"Ver": "1.0001"})   

def ConsultarOrdenesPorRango(request):
    idOrdenInicio = request.GET.get("inicio")
    idOrdenFin = request.GET.get("fin")
    pars = idOrdenInicio + "|" + idOrdenFin
    archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\03_Django\WebPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogDjango_Demo11.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspOrdenConsultarPorRangoPyCsv","IdOrdenes",pars) 
    return HttpResponse(data)