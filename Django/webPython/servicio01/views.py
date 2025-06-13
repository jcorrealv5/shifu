from django.shortcuts import render
from django.http import HttpResponse
from Modulos.modAccesoDatos import clienteSQL

def ListarProductos(request):
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo28.txt"
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoListarCsv") 
    return HttpResponse(data)

def ConsultarProducto(request):
    archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Django\webPython\Modulos\Config_BD_DACP_2025.txt"
    archivoLog = r"C:\Users\jhonf\Documents\Shifu\Django\LogDjango_Demo28.txt"
    id = request.GET.get("id")
    con = clienteSQL(archivoConfig, archivoLog)
    data = con.EjecutarComandoCadena("uspProductoObtenerPorId2","ProductID",id) 
    return HttpResponse(data)