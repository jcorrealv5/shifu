from django.shortcuts import render
from django.http import HttpResponse
from Modulos.modAccesoDatos import clienteSQL

def Consulta(request):    
    return render(request, "appDemo03/Consulta.html")
    
def ListarProductos(request):
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo03.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoListarCsv") 
    return HttpResponse(data)